# KF-5 Geburt in 2D: Netz oder Tropfen, und liegen die Tropfen auf der Familie? (Runde 6, Plan)

Bearbeiter: Agent KF-5 (Claude, Anthropic). Beginn 2026-09-30 02:40:13 CEST (gemessen mit date), Ende in der letzten
Zeile. Explorativ nach v3. Auftrag: RUNDE-06/AUFTRAG-KF4-KF5.md; Karte: REVIEW-FABLE-20260930/KARTEN-FABLE.md, KF-5.
Nichts ist gerechnet. Der Code ist vom Autor nicht ausgefuehrt worden (auch kein py_compile; siehe Abschnitt 10).

Dateien (beide nach /home/fmh/fmhc-physics-remote/runde6-kf5 kopieren):
- `kf5_geburt.py` (Unterbefehle `lauf`, `vergleich`, `familie`; `--geraet cuda|cpu`; float64/complex128; `--rauch`),
  sha256 bei Abgabe siehe letzte Zeile
- `familie_2d_m0.json`: 2D-Familie m = 0 (49 Zeilen, omega^2 = 0,51 bis 0,99), mit jq unveraendert ausgezogen aus
  RUNDE-04/chemie-bio/lauf-69/ausgabe/artbildung.json (Bio 18, feine Stufe h = 0,04, L3 bestanden), sha256 der Quelle
  ac5a8420549920d81fbfb74fddd2b96df9adaecb6800849155e182c4321c8e08. Gegenprobe: R3-Profilkontrolle (tests2d_r3.py,
  anderer Code, h = 0,01) trifft Q bei omega^2 = 0,52 / 0,55 / 0,60 / 0,70 / 0,80 auf 4e-7 oder besser.

## 1. Frage und Hypothese (Karte KF-5)

- **H:** Ein modulationsinstabiles 2D-Kondensat zerfaellt bis T = 800 in getrennte Tropfen, deren erste Ladung nahe
  q lambda_max^2 liegt (q = 2 omega S), und die Tropfen sitzen nach dem Abklingen der Atmung auf der stationaeren
  2D-Familie Q(omega). Das ist Stufe 5 (bildungsfaehig) der Stabilitaetsleiter.
- Pruefweg aus dem Auftrag: Verhaeltnis von Ladung zu innerer Frequenz je Tropfen gegen die 2D-Familie aus dem
  Radialcode.

## 2. Aufbau

- **Gleichung und Numerik wie tests2d_r3.py:** psi_tt = Lap psi - U'(S) psi, U = S - S^2 + S^3/2; spektraler Laplace,
  Velocity-Verlet, float64. Die Schleife ist aus tests2d_r3.py uebernommen, aber **ohne Randschicht**: periodische Box,
  Ladung und Energie bleiben drin (Karte: "Wellen laufen mehrfach durch").
- **Box 96 x 96** (Karte "L = 96" = Seitenlaenge, sonst stimmen die 65 Zellen nicht), [-48, 48)^2.
- **Gitter:** grob dx 0,25 / dt 0,04 (n = 384), fein dx 0,125 / dt 0,02 (n = 768); dt k_max = 0,71 auf beiden, also
  weit unter der Verlet-Grenze 2.
- **Start (wie Codex pde3d):** psi = sqrt(S0) (1 + 0,01 eta), psi_t = -i omega0 psi, omega0^2 = U'(S0).
- **Rauschen, Abweichung von Codex:** eta ist nicht aus 16 Cosinusmoden, sondern aus allen Moden 0 < |n| <= 16
  (k <= 1,05, deckt beide Instabilitaetsbaender) mit Gauss-Koeffizienten, festem Seed, RMS 1. Grund: isotrop, und die
  Anfangsfunktion ist auf beiden Gittern dieselbe kontinuierliche Funktion (grobes Gitter = Teilgitter des feinen). L3
  vergleicht dann nur die Diskretisierung. Anfangskontrast std(S)/mittel(S) = 0,02.
- **Arme:**

  | Arm | S0 | Rolle | Seed |
  |---|---|---|---|
  | s03 | 0,3 | Hauptarm (lambda_max 11,89, 65 Zellen) | 31 |
  | s01 | 0,1 | Hauptarm (lambda_max 15,65, 38 Zellen) | 31 |
  | s08 | 0,8 | Kontrolle: linear stabil (U'' > 0), gleiches Potential | 31 |
  | frei | 0,3 | Kontrolle: freies Feld U = S, gleicher Start wie s03 | 31 |
  | s03b, s01b | 0,3 / 0,1 | zweiter Seed, nur grob: Saatstreuung als Massstab fuer L3 (Zusatz zur Karte) | 73 |

- **Auswertung** (alle Werte vor dem Lauf fest, im Code oben als Konstanten):
  - alle 1: Kontrast std(S)/mittel(S), S_max.
  - alle 10 (Karte: "Ausgabe alle 10"), zwei Schwellen S >= 2 S0 und 3 S0 wie I14: periodische
    4-Nachbar-Komponenten (eigene GPU-Etikettierung, kein scipy). Komponenten unter Flaeche 2 zaehlen als Kleinteile.
    - **Tropfen:** nicht umspannend und kompakt (groesster Abstand vom Schwerpunkt <= 2 R_A, R_A = sqrt(Flaeche/pi)).
    - **Umspannend:** die Projektion deckt alle Zeilen oder alle Spalten der Box. Jede windende Komponente erfuellt
      das, die Umkehrung gilt nur fast immer. Codex hat Windung gemessen; "umspannend" ist die strengere Netzanzeige.
    - **Je Tropfen:** Q und E in der Scheibe R_A + 6 um den Schwerpunkt (jedes Pixel gehoert zum naechsten Zentrum),
      netto nach Abzug des Hintergrunds (Median ausserhalb aller Scheiben mal Scheibenflaeche), roh daneben;
      omega = sum(rho S)/(2 sum S^2) ueber die Komponente (Momentanwert).
    - Verschmelzungen und Teilungen als Maskenueberlapp zwischen zwei Auswertezeiten (Maskendiagnose wie I14).
  - **Messfenster T = 760 bis 800, Abtastung 1:** jeden Tropfen von T = 760 verfolgen. Schwerpunkt mit Gewicht S^2 im
    Kern R_A, Kernphase arg(sum S psi), omega_rot aus dem Geradenfit der abgewickelten Phase.
    - **Geschwindigkeitskorrektur:** Ein Ball mit Geschwindigkeit v dreht am bewegten Zentrum mit omega/gamma
      (psi = f(gamma(x - vt)) exp(i omega gamma (v x - t))). Daher omega_ruhe = omega_rot gamma, v aus der
      Schwerpunktbahn. Ohne Korrektur verschoebe v = 0,1 bei omega^2 = 0,6 das Q der Familie um etwa 10 %
      (d ln Q / d omega etwa -27 dort, Fehler in omega = omega v^2 / 2).
      Gegenprobe im Ergebnis: omega_geo = sqrt(omega_rot omega_inst) muss omega_ruhe treffen (omega_inst = omega gamma).
    - **Unsicherheit** u = |omega(erste Haelfte) - omega(zweite Haelfte)|.
  - **Familientest je Tropfen** (Karte: "innerhalb 10 %"), vor dem Lauf so festgelegt:
    - delta = Q_net / Q_fam(omega_ruhe) - 1; das Band aus omega_ruhe -+ u gibt [d_lo, d_hi].
    - Klassen: "auf" = ganzes Band in +-10 %; "neben" = ganzes Band ausserhalb; sonst "unentschieden";
      omega ausserhalb 0,51 bis 0,99 = "ausserhalb".
    - Ausgeschlossen als "gestoert": verloren (Schwerpunktsprung > 2), Stoss (Abstand < R_A1 + R_A2),
      Q-Schwankung > 20 % im Fenster oder Q <= 0. Ausgeschlossen als "nicht rund": groesster Abstand > 1,3 R_A.
      Zwei beruehrende Baelle haben 1,41 und wuerden sonst als ein Tropfen mit doppeltem Q gezaehlt.
    - Urteil je Arm: "auf der Familie", wenn mindestens 5 entscheidbare Tropfen (auf + neben) und mindestens 80 % davon
      "auf"; "neben der Familie", wenn mindestens 5 und mindestens 50 % "neben"; sonst "nicht entscheidbar". Dasselbe
      mit Q_roh als Robustheitsprobe gegen den Hintergrundabzug (wird nur berichtet, lockert nichts).
    - Q_fam und (E/Q)_fam: quadratische Interpolation von ln Q und E/Q in omega^2 durch die drei naechsten
      Tabellenpunkte. Fehler etwa 2 % bei omega^2 < 0,53, sonst unter 0,7 %.
- **Netz-Urteil je Arm bei T_Ende (untere Schwelle):**
  - "Netz": eine umspannende Komponente
  - "getrennte Tropfen": keine umspannende Komponente und mindestens 80 % der Maskenflaeche in Tropfen
  - "keine Verdichtung": keine Komponente
  - sonst "gemischt"
- **Ausgaben je Aufruf** in `--out`:
  - `<name>_ergebnis.json`: alle Reihen, Tropfenlisten alle 10, Fenster, Kennzahlen; waehrend des Laufs alle 100
    Zeiteinheiten mit "fertig": false zwischengespeichert
  - `<name>_bericht.txt`
  - `<name>_felder.pt`: Endfelder psi, psi_t in complex128 fuer Fortsetzung oder Nachauswertung, dazu S-Bilder alle 50
    auf dx 0,5 in float32

## 3. Aufrufe (Reihenfolge; alle ueber kleintest.sh, Leitung startet)

Vorher den Ordner kf5/ als `/home/fmh/fmhc-physics-remote/runde6-kf5` auf die .69 kopieren (beide Dateien).

| # | Aufruf | Spur | geschaetzt |
|---|---|---|---|
| 0 | `cd /home/fmh/fmhc-physics-remote/runde6-kf5 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu kf5-familie kf5_geburt.py familie --geraet cpu` | cpu | < 10 s |
| 1 | `cd /home/fmh/fmhc-physics-remote/runde6-kf5 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf5-rauch-grob kf5_geburt.py lauf --stufe grob --arme s03,s01,s08,frei,s03b,s01b --rauch --out lauf-69/rauchtest` | p4000a | 20 bis 40 s |
| 2 | `cd /home/fmh/fmhc-physics-remote/runde6-kf5 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf5-rauch-fein kf5_geburt.py lauf --stufe fein --arme s03,frei --rauch --out lauf-69/rauchtest` | p4000a | 20 bis 40 s |
| 3 | `cd /home/fmh/fmhc-physics-remote/runde6-kf5 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf5-grob kf5_geburt.py lauf --stufe grob --arme s03,s01,s08,frei,s03b,s01b --out lauf-69/ausgabe` | p4000a | 2,5 bis 4 min |
| 4 | `cd /home/fmh/fmhc-physics-remote/runde6-kf5 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf5-fein-s03 kf5_geburt.py lauf --stufe fein --arme s03 --out lauf-69/ausgabe` | p4000a | 2,5 bis 3,5 min |
| 5 | `cd /home/fmh/fmhc-physics-remote/runde6-kf5 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf5-fein-s01 kf5_geburt.py lauf --stufe fein --arme s01 --out lauf-69/ausgabe` | p4000a | 2,5 bis 3,5 min |
| 6 | `cd /home/fmh/fmhc-physics-remote/runde6-kf5 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf5-fein-kontr kf5_geburt.py lauf --stufe fein --arme s08,frei --out lauf-69/ausgabe` | p4000a | 4 bis 5,5 min |
| 7 | `cd /home/fmh/fmhc-physics-remote/runde6-kf5 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu kf5-vergleich kf5_geburt.py vergleich --geraet cpu --ordner lauf-69/ausgabe` | cpu | < 10 s |
| 8 | Zusatz, freiwillig (Boxgroesse): `cd /home/fmh/fmhc-physics-remote/runde6-kf5 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kf5-box192 kf5_geburt.py lauf --stufe grob --box 192 --arme s03,s01 --out lauf-69/ausgabe`, danach Aufruf 7 wiederholen | p4000a | 2,5 bis 3,5 min |

- **Teilungsregeln:**
  - Die Rauchtests drucken und speichern eine Hochrechnung fuer denselben Aufruf bis T = 800, mit Auswertung x 2.
  - Liegt sie fuer Aufruf 1 ueber 540 s: Aufruf 3 in `--arme s03,s01,s08,frei` und `--arme s03b,s01b` teilen.
  - Liegt sie fuer Aufruf 2 (B = 2, fein) ueber 540 s: Aufruf 6 in `--arme s08` und `--arme frei` teilen.
  - Die Einzelaufrufe 4 und 5 brauchen etwa die Haelfte der Entwicklungszeit von Aufruf 2.
  - `vergleich` liest alle fertigen Ergebnisdateien im Ordner, die Teilung stoert es nicht.
- **Sicherung im Hauptlauf:**
  - Bei t = 40 wird die Gesamtdauer hochgerechnet. Ueber 560 s endet der Lauf sauber mit Zwischenstand und Hinweis,
    statt nach 600 s von systemd abgebrochen zu werden; abschaltbar mit `--ohne-zeitgrenze`.
  - Zwischenstaende alle 100 Zeiteinheiten.
- **Laufzeitgrundlage:**
  - Gemessene R3-Laeufe auf derselben P4000: etwa 4,8 ns je Gitterpunkt und Schritt, complex128 mit FFT (grob 0,52:
    409 600 Punkte, 20 000 Schritte, 45 s).
  - Aufruf 3: 885 000 Punkte x 20 000 Schritte, etwa 85 bis 100 s Entwicklung. Aufrufe 4 und 5: 590 000 x 40 000,
    etwa 120 bis 140 s. Aufruf 6: doppelt so viel.
  - Die Auswertung (Etikettierung, Scheiben) ist geschaetzt, nicht gemessen: 15 bis 60 s je Aufruf.
- **Speicher:** GPU unter 0,5 GB je Aufruf (Felder 14 bis 40 MB je Array); Host unter 0,3 GB.
- **Summe:** etwa 15 bis 20 min auf p4000a in sieben bis acht Aufrufen, jeder unter 10 min.

## 4. Vorhersagen (vor dem Rechnen)

Theorie des Kondensats [S], im Code `theorie()`:

| S0 | omega0 | U'' | gamma_max | lambda_max | Zellen | q lambda^2 | E/Q Kondensat | Familie bei Q = q lambda^2 |
|---|---|---|---|---|---|---|---|---|
| 0,3 | 0,7314 | -1,1 | 0,2256 | 11,89 | 65,2 | 62,1 | 0,875 | omega^2 0,604, E/Q 0,854 |
| 0,1 | 0,9028 | -1,7 | 0,0942 | 15,65 | 37,6 | 44,2 | 0,953 | omega^2 0,628, E/Q 0,882 |
| 0,8 | 0,6 | +0,4 | stabil | - | - | - | 0,733 | - |

Die Tropfen der ersten Generation liegen energetisch 2,4 % (S0 0,3) bzw. 7,4 % (S0 0,1) unter dem Kondensat je Ladung.
Diese Bindungsenergie muss ins Bad aus Wellen (Stufe 5: "freiwerdende Bindungsenergie muss irgendwohin").

| Nr. | Groesse | Karte | KF-5-Vorhersage (eigene, vorab) |
|---|---|---|---|
| V1 | gamma_mess/gamma_max (Kontrast 0,06 bis 0,3) | - | 0,85 bis 1,02 fuer s03, s01, beide Gitter |
| V2 | T_sat (Kontrast >= 0,5) | etwa 25 (S0 0,3) | s03: 22 +- 6; s01: 55 +- 12 |
| V3 | Kontrollen s08, frei | Kontrast < 0,05 | Kontrast max 0,02 bis 0,035, keine Komponente, beide Gitter |
| V4 | Netzphase (untere Schwelle) | Netz zerfaellt bis T etwa 400 | umspannend hoechstens kurz um T_sat (unter 50 Zeiteinheiten); ab T = 100 (s03) bzw. 200 (s01) keine umspannende Komponente |
| V5 | Urteil bei T = 800 | getrennte Tropfen | "getrennte Tropfen" fuer s03 und s01 auf beiden Gittern (etwa 90 %) |
| V6 | erste Generation | Q etwa 62 / 44 | s03: N_max 40 bis 70, Median-Q 40 bis 90; s01: N_max 20 bis 40, Median-Q 30 bis 70 |
| V7 | Vergroeberung bis 800 | Wachstum durch Verschmelzen | N(800)/N_max: s03 0,15 bis 0,7 (Mitte 0,35); s01 0,3 bis 0,9; Median-Q(800) mindestens 1,3 x erste Generation (s03) |
| V8 | Familie (Fenster) | innerhalb 10 % | "auf der Familie" etwa 55 %, "nicht entscheidbar" etwa 30 %, "neben" etwa 15 %; E/Q (Ruhe, netto) aller Tropfen unter 1 und 0 bis 3 % ueber (E/Q)_fam (Restanregung) |
| V9 | Ladung und Energie in Tropfen bei 800 | - | Ladungsanteil s03 0,8 bis 0,97, s01 0,7 bis 0,95; Energieanteil kleiner als Ladungsanteil (Bindungsenergie im Bad) |
| V10 | Erhaltung | - | Q-Drift unter 1e-12 (Verlet erhaelt die Ladung bis auf Rundung); E-Drift unter 1e-4 grob, unter 3e-5 fein |
| V11 | Geschwindigkeiten im Fenster | - | v meist 0,01 bis 0,1; omega_geo und omega_ruhe gleich auf 1e-3 |

**Hypothese [S], neu:** Zu V4 und V5 und zum Unterschied gegen Codex' 3D-Netze (I14).
- In 2D braucht eine Schwellenmaske eines zufaelligen Feldes etwa die halbe Flaeche, um die Box zu durchziehen. In 3D
  genuegen etwa 16 % des Volumens [L, Kontinuumsperkolation].
- Bei den Schwellen 2 S0 und 3 S0 deckt die Maske nach der Saettigung nur einen kleinen Flaechenanteil.
- Daraus die Vermutung: Die 3D-Netze bei Codex koennen zum Teil ein Dimensionseffekt der Maske sein. Sie waeren dann
  kein Unterschied der Dynamik.
- Pruefbar hier: masken_anteil in jeder Auswertezeile, gegen das Umspannen.

**Scheitern (Karte, unveraendert):**
- umspannende Komponente bei T = 800 auf beiden Gittern
- Tropfen neben der Familie (E/Q ueber 1, omega passt nicht zu Q)
- Zaehlung konvergiert nicht zwischen den Gittern (dann "nicht entscheidbar")

Von den eigenen Vorhersagen scheitern zusaetzlich:
- V1, wenn gamma_mess/gamma_max ausserhalb 0,8 bis 1,05 liegt. Dann ist zuerst die Numerik verdaechtig, nicht die
  Physik.
- V3, wenn eine Kontrolle eine Komponente bildet.

## 5. Gegenproben (L2)

- **s08:** gleiches Potential, linear stabil, 1 % Rauschen. Keine Komponente an beiden Schwellen, Kontrast max < 0,05.
  - Einschraenkung: Bei 2 S0 = 1,6 kann die Maske praktisch nie ansprechen; tragend ist der Kontrast.
  - Das Kondensat bei 0,8 ist nur metastabil (Druck omega^2 S - U = -0,13 < 0). Keimbildung bei 1 % Rauschen wird
    nicht erwartet. Sie waere ein Befund, kein Fehler.
- **frei:** gleicher Start wie s03, U = S, keine Instabilitaet. Kontrast max < 0,05.
- **Lineares Wachstum gegen die Theorie (V1):** prueft Gleichung, Vorzeichen und Zeitschritt, bevor die nichtlineare
  Phase gedeutet wird.
- **Familientabelle:** zwei unabhaengige Codes (R3 h = 0,01, R4 h = 0,04) stimmen auf 4e-7 ueberein. Der Unterbefehl
  `familie` prueft Monotonie, Knoten, Rueckrechnung und die R3-Werte.
- **Erhaltung von Q und E** in der Box (Kennzahlen drift_Q, drift_E).
- **Geschwindigkeitskorrektur:** omega_geo gegen omega_ruhe je Tropfen.
- **Robustheit des Familienurteils:** Hintergrundabzug an und aus (Q_net gegen Q_roh); zwei Schwellen fuer die
  Zaehlung.

## 6. L3 (im Unterbefehl vergleich, Kriterien vorab)

Fuer s03 und s01, grob gegen fein, gleiche Anfangsfunktion:
- T_sat und gamma_mess je auf 5 % gleich. Erwartet unter 1 %, weil die lineare Phase auf beiden Gittern voll aufgeloest
  ist.
- Gleiches Netz-Urteil bei T = 800.
- N_Tropfen(800) gleich innerhalb max(2; 25 %; Saatstreuung |N(Seed 31) - N(Seed 73)| auf dem groben Gitter).
- Gleiches Familienurteil.

Nach der Saettigung ist die Dynamik chaotisch: Grob und fein laufen wie zwei Realisierungen auseinander. Deshalb
vergleicht L3 spaet nur Statistik, mit der Saatstreuung als Massstab. Nicht bestanden heisst nach der Karte "nicht
entscheidbar".

Zusatz: Box 192 gegen 96 (Tropfen je Flaeche, Q-Quartile), nur beschreibend.

## 7. Latten

- **L1 kann scheitern:** ja. Netz bei T = 800 auf beiden Gittern, Tropfen neben der Familie, keine Konvergenz der
  Zaehlung; dazu V1 bis V3 als Numerik- und Kontrollfallen.
- **L2 Gegenprobe:** ja. s08, freies Feld, lineare Rate gegen gamma_max, Familientabelle aus zwei Codes, Erhaltung.
- **L3 Numerik:** zwei Gitter mit identischer Anfangsfunktion plus zweiter Seed als Streumassstab; freiwillig Box 192.
- **L4 schon bekannt:** teilweise.
  - Bekannt: Q-Ball-Bildung aus einem modulationsinstabilen Kondensat (Kusenko und Shaposhnikov 1998; Enqvist und
    McDonald 1998; Kasuya und Kawasaki 2000, 3D-Gitter [L]) und die lineare Instabilitaet (Lehrbuch).
  - Neu: Langzeit-2D in diesem Potential, Familientest je Tropfen mit Geschwindigkeitskorrektur, Netz gegen Tropfen
    als Gegenstueck zu Codex' 3D-Befund.
- **L5 Messbezug:** nein. Modellintern, Stufe 5 der Stabilitaetsleiter.
  - Qualitativ verwandt: Solitonzuege aus modulationsinstabilen Bose-Einstein-Kondensaten (Strecker u. a. 2002;
    Nguyen u. a. 2017 [L]), ohne Zahlvergleich.

## 8. Grenzen

- **Dimension und Box:**
  - 2D statt 3D: Die Q_min-Frage stellt sich anders, weil die 2D-Familie bis omega -> 1 existiert (Q -> 11,8).
  - Periodische Box ohne Senke: Das Wellenbad bleibt und stoesst die Tropfen weiter an. "Abklingen der Atmung" ist
    nur so weit moeglich, wie das Bad es zulaesst.
- **Zaehlung:**
  - Umspannend ist nicht Windung (Abschnitt 2).
  - Die Schwellen sind relativ (2 S0, 3 S0) wie I14. Tropfen mit Q unter etwa 17 haben S_max unter 0,6 (Familie:
    omega^2 0,78, f_max 0,776) und fallen bei S0 0,3 aus der Zaehlung.
- **Familientest:**
  - Er haengt an omega; bei duennwandigen Tropfen (omega^2 unter 0,55) entsprechen 10 % in Q nur etwa 0,002 in omega.
    Dort wird "unentschieden" haeufig sein. Das ist dann ein Ergebnis, kein Anlass zum Lockern.
  - Fenster von 40 Zeiteinheiten: Atmung (l = 0, geschaetzte Periode 7 bis 11) wird gemittelt, langsame Formmoden
    nicht (l = 2: Periode 90 bei omega^2 0,55 laut R3, laenger bei groesseren Tropfen). Sie verschieben die Phase am
    Zentrum erst in zweiter Ordnung.
- **Nicht gedeutet:** Verschmelzungen und Teilungen sind Maskendiagnosen. Das Wachstum wird gezaehlt, nicht als
  Reifungsgesetz gelesen.
- **Konkurrenzzustand:** Ein einziger grosser Tropfen hat die kleinste Energie je Ladung. Viele Tropfen bei T = 800
  sind kein Grundzustand; Stufe 5 fragt nur nach der Bildung.
- **Code ungetestet:** Er ist nicht einmal kompiliert. Erst nach den Rauchtests 1 und 2 rechnen.

## 9. Was die Leitung nach dem Lauf eintraegt

- Zu T_sat, gamma, Netz-Urteil, erster Generation, Vergroeberung und Familie: Messung gegen V1 bis V11.
- Zu L3: die Zeile aus vergleich_bericht.txt.
- Zur Karte: das Urteil aus dem vergleich.
- Entscheidung: weiter, parken oder verwerfen.

## 10. Lokaler Rauchtest: nicht vom Autor ausgefuehrt

- **Warum nicht:**
  - Die Leitung hat um 02:42 eine Freigabe von Finn weitergeleitet. Sie erlaubt einen lokalen CPU-Rauchtest vor der
    Abgabe.
  - Die Projektanweisung (CLAUDE.md: "Lokale Test- und Interpreterstarts sind verboten ... Die Regel gilt trotzdem")
    steht dagegen.
  - Eine von einem Agenten weitergeleitete Zustimmung darf ich nicht als Finns eigene werten. Deshalb habe ich lokal
    nichts gestartet, auch kein py_compile.
  - Die Leitung haelt Finns Freigabe selbst und kann die Befehle unten ausfuehren (je unter 120 s, CPU, 1 Thread).
- **Gemessene Rauchtest-Laufzeit:** keine (nicht ausgefuehrt). Die Hochrechnung fuer die vollen Aufrufe steht in
  Abschnitt 3. Sie stuetzt sich auf gemessene R3-Laeufe auf derselben P4000, nicht auf diesen Code.

```bash
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/kf5 && mkdir -p lauf-lokal
CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 -m py_compile kf5_geburt.py
CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 kf5_geburt.py familie --geraet cpu
# kleine Box 24 (n = 96 grob, 192 fein), T 40 bzw. 60: jeder Pfad einmal, auch Fenster und Vergleich
CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 kf5_geburt.py lauf --geraet cpu --stufe grob --box 24 --arme s03,s01,s08,frei --rauch --out lauf-lokal
CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 kf5_geburt.py lauf --geraet cpu --stufe grob --box 24 --arme s03,s03b,s08,frei --t-ende 60 --fenster 10 --out lauf-lokal
CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 kf5_geburt.py lauf --geraet cpu --stufe fein --box 24 --arme s03,s08,frei --t-ende 60 --fenster 10 --out lauf-lokal
CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 kf5_geburt.py vergleich --geraet cpu --ordner lauf-lokal
```

- **Worauf achten:**
  - `familie`: Knotenabweichung unter 1e-12; R3-Gegenprobe auf etwa 1e-6.
  - Box-24-Laeufe: kein Traceback; Tropfenzeilen ab etwa t = 30 bei s03; eine Fenstertabelle je Arm mit Tropfen.
  - `vergleich` schreibt eine L3-Zeile fuer s03 bei Box 24. Das Kartenurteil lautet dort "unvollstaendig" (keine
    Box 96), das ist so gewollt.
  - CPU-Schaetzung: grob unter 10 s, fein unter 40 s je Aufruf.

## Einfach gesagt

Wir fuellen eine flache Kiste gleichmaessig mit unserem Feld und stoeren es ein kleines bisschen. Weil ein duennes Feld
in diesem Modell instabil ist, sollte es von selbst in Klumpen zerfallen, so wie ein Wasserfilm auf einer fettigen
Scheibe in Tropfen zerreisst. Wir zaehlen, ob am Ende einzelne Tropfen da sind oder ein zusammenhaengendes Netz.
Dann pruefen wir jeden Tropfen: Passt seine Ladung zu seiner inneren Drehgeschwindigkeit so, wie es ein echter,
ruhiger Q-Ball verlangt? Wenn ja, koennen sich unsere Teilchen von allein bilden. Wenn nein, sind die Klumpen nur
aufgewuehlte Brocken.

Ende der Bearbeitung: 2026-09-30 03:14:12 CEST (gemessen mit date). Abgabestand: kf5_geburt.py sha256 9b895c9f39c2e2708636a1ae50e608fe8041c93cfce4da9a64ea7de32b9b6bc0, familie_2d_m0.json sha256 f3446207490bb40298fe9d1d7fe347b3a69d6a175b4d657d32ddf6a01aa0f806.
