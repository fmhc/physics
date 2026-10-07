# KRUEMMUNGS-SANDHAUFEN-2D-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 48)

- **Zeiten (date, CEST):** Start 11:13:35. Code ksh.py ab 11:26:33, Rauchtest-Kopie auf der .69 11:30:26, Rauchketten
  gestartet 09:30:31 UTC (= 11:30:31 CEST). Plantext ab 11:30:36. Einfrierzeit steht in EINGEFROREN-SHA256.txt.
- Grundlage: KARTE.md (Vorhersagen KH0 bis KH3 unveraendert), DOSSIER KRUEMMUNG-SPANNUNG-SPIN-L 6.2, SOC-RAUM-L 4.5/4.6/8.
- Alles ist eine synthetische, kombinatorische Modellrechnung, keine Messdatenbestaetigung. Kennzeichen: [M] Mathematik
  vorab, [F] Festlegung dieses Plans, [L] Literatur aus dem Gedaechtnis, [H] Hypothese, [ES] eigener Schluss.
- Code: code/ksh.py (ein Skript: `lauf`, `btw`, `aus`). Nur Python-Standardbibliothek im Kern, numpy/scipy fuer
  Netzbau und Fits, matplotlib fuer Bilder. Laeufe nur auf der .69 ueber kleintest.sh (1 Kern, RuntimeMaxSec 600).

## 1. Startnetze [F]

- **Kugel:** konvexe Huelle von N gleichverteilten Punkten auf S^2 (= sphaerische Delaunay-Zerlegung), N = 500, 2000,
  8000 genau; Netzsaat 1000 + N. Pruefung beim Bau: alle N Ecken benutzt, F = 2N - 4.
- **Offene Scheibe:** N_rand = round(2 sqrt(pi N)) Punkte gleichabstaendig auf dem Einheitskreis (79, 159, 317) und
  N - N_rand gleichverteilte Punkte im Kreis vom Radius 1 - h/2 (h = 2 pi / N_rand), Delaunay. Netzsaat 2000 + N.
  Pruefung: Randkanten = genau der Kreis, alle Ecken benutzt, kein Grad < 3 (sonst neue Saat, hoechstens 20 Versuche).
  N_rand ~ 2 sqrt(pi N) gibt am Rand etwa denselben Punktabstand wie innen.
- **Begruendung:**
  - Beide Geometrien mit derselben Bauweise (zufaellige Delaunay-Zerlegung): Der Vergleich Kugel gegen Scheibe
    trennt dann nur Senke gegen keine Senke.
  - N genau wie in der Karte. Eine geodaetische Kugel gaebe nur N = 10 m^2 + 2 (492, 1962, 7842) und startete im
    Sonderzustand "alle Ladungen |q| <= 1, Ikosaedersymmetrie".
  - Das Modell ist rein kombinatorisch: Nach dem Bau zaehlen nur Nachbarschaften, die Punktlagen nicht mehr. Der
    stationaere Zustand der getriebenen Kette haengt nicht vom Startnetz ab [M fuer eine ergodische endliche Kette]; das
    Startnetz bestimmt nur die Einschwingzeit.
  - Gegenargument: Die Zufalls-Delaunay startet mit vielen |q| >= 2 (Grad 4 und 8). Darum gibt es vor dem Einschwingen
    eine nicht gemessene Anfangsrelaxation (Abschnitt 5).
- **Ladung:** innen q_v = 6 - c(v). Randecken (nur fuer Kontrollsummen): q_v = 4 - c(v) (flacher Rand); dann gilt
  Summe q = 6 chi auf beiden Flaechen [M]: Kugel 12, Scheibe 6.

## 2. Kippregel und Arme [F]

- Eine **innere** Ecke v mit abs(q_v) >= 2 (Grad <= 4 oder >= 8) ist instabil. Randecken kippen nie.
- **q_v >= 2:** Flip einer Ringkante (u, w) des Sterns von v; das zweite Dreieck an (u, w) hat die Spitze z; die neue
  Kante ist (v, z). Wirkung: q_v - 1, q_z - 1, q_u + 1, q_w + 1.
- **q_v <= -2:** Flip einer Kante (v, x) mit den Spitzen c, d; neue Kante (c, d). Wirkung: q_v + 1, q_x + 1, q_c - 1,
  q_d - 1.
- Damit sinkt abs(q_v) je Kipp-Flip um genau 1 [M]; die drei anderen Ladungen aendern sich um +-1.
- **Wellen (beide Arme):** Eine Lawine laeuft in Wellen. Zu Beginn einer Welle wird die Menge U der instabilen inneren
  Ecken festgehalten. Jede Ecke aus U, die bei ihrer Reihe noch instabil ist, macht genau einen Kipp-Flip. Ecken, die
  waehrend der Welle instabil werden, kommen in der naechsten Welle dran.
- **Arm Z (zufaellig, Hauptarm):** Reihenfolge in der Welle zufaellig gemischt; der Flip wird gleichverteilt unter den
  zulaessigen Flips des passenden Typs gezogen.
- **Arm D (deterministisch, Kontrollarm):** Reihenfolge aufsteigend nach Eckennummer; gewaehlt wird der zulaessige Flip
  mit dem kleinsten Kantenschluessel der geflippten Kante.
- Die Eckennummern sind Zufallsnummern der Punkterzeugung, also ohne Bezug zur Geometrie. Arm D unterscheidet sich von Z
  nur durch die fehlende Zufaelligkeit, nicht durch eine Energieregel (wie BTW gegen Manna [L]).
  - Eine energetisch gierige Wahl (kleinste lokale Summe q^2) waere ein dritter Arm; er ist nicht Teil dieses Plans.

## 3. Zulaessigkeit, blockierte Ecken, Abbruch [F]

- Ein Flip (a, b) -> (c, d) ist zulaessig, wenn (a, b) eine innere Kante ist (zwei Dreiecke), Grad(a) >= 4 und
  Grad(b) >= 4 (nach dem Flip kein Grad < 3) und (c, d) noch keine Kante ist (keine Doppelkante). Das gilt fuer Antrieb
  und Kippen gleich, auch fuer Randecken als a, b, c, d. Randkanten werden nie geflippt.
- **Kein zulaessiger Flip:** Die Ecke ist in dieser Welle blockiert und bleibt instabil (gezaehlt als
  "blockiert_versuche"). Macht in einer Welle keine Ecke einen Flip, endet die Lawine mit Status 1 ("blockiert"). Die
  blockierten Ecken bleiben instabil und werden in jeder folgenden Lawine wieder versucht.
- **Abbruch:** Eine Lawine endet mit Status 2, wenn s = 50 N erreicht ist (Kugel ohne Senke kann endlos laufen).
- **Zyklus (nur Arm D):** Arm D ist innerhalb einer Lawine deterministisch. Kehrt die Flaeche am Ende einer Welle in eine
  schon gesehene Kantenmenge zurueck (64-bit-Zobrist-Hash der Kantenmenge), laeuft die Lawine periodisch weiter; sie
  endet mit Status 3 ("Zyklus").
- Status 0 = stabil (keine instabile Ecke mehr).

## 4. Antrieb, Zeitskalentrennung, Messgroessen [F]

- **Antrieb:** Je Schritt ein Flip einer gleichverteilt gezogenen inneren Kante; ist er unzulaessig, wird neu gezogen
  (also gleichverteilt unter den zulaessigen). Danach laeuft die Lawine zu Ende; erst dann folgt der naechste Antrieb.
- **Messgroessen je Schritt:**
  - s = Zahl der Kipp-Flips (der Antriebsflip zaehlt nicht).
  - Dauer T = Zahl der Wellen mit mindestens einem Flip.
  - Flaeche A = Zahl verschiedener Ecken, die gekippt sind.
  - Status 0 bis 3.
- Lawine = Schritt mit s >= 1. Der Anteil der Schritte mit s = 0 wird berichtet.
- Zeitreihe alle 1000 Schritte: mittleres s, Defektanteil (innere Ecken mit q != 0), mittleres q^2, Zahl instabiler
  (blockierter) Ecken, Randgrad (Mittel, Maximum), kleinster und groesster Grad.

## 5. Einschwingen, Messdauer, Zahl der Lawinen [F]

- Zuerst eine **Anfangsrelaxation** ohne Antrieb (Abbruch bei 100 N Flips), nicht gemessen.
- **Einschwingen:** 10 N Schritte (Antrieb + Lawine), hoechstens 40 % des Fallbudgets; nicht gemessen. Ob das
  Zeitlimit griff, steht als "zeitbegrenzt" in der Ausgabe.
- **Messung:** bis 300 000 Schritte oder bis das Fallbudget (Wanduhr ab Fallbeginn) verbraucht ist. Fallbudgets
  (Sekunden): N = 500: 50, N = 2000: 90, N = 8000: 300 (BTW: 40, 80, 300; Antriebsrate: 150 je Fall). Die Zahl der
  Lawinen ergibt sich daraus und wird berichtet.
- **Stationaritaet:** Mittelwert von s in erster gegen zweite Messhaelfte, je mit Blockfehler (10 Bloecke);
  z = Differenz / kombinierter Fehler. z > 3 heisst "Drift" und wird beim Urteil als Vorbehalt genannt, aendert es aber
  nicht. Dazu die Zeitreihe des Defektanteils (beschreibend).

## 6. Mechanische Auswerteregeln [F]

- **Fitstichprobe:** Lawinen mit s >= s_min = 2 und Status 0 oder 1 (Abbrueche und Zyklen nicht). Traeger der Modelle:
  ganze Zahlen von 2 bis 50 N (BTW: bis max(50 N, 10 max s)).
- **Modelle** (diskret, Maximum-Likelihood):
  - M1: p(s) ~ s^(-tau) exp(-s/s_c) (Potenzgesetz mit Abschneiden), 2 Parameter.
  - M2: p(s) ~ exp(-s/s_0) (Exponential), 1 Parameter.
  - M3: p(s) ~ exp(-(s/s_0)^beta) (gestreckte Exponentialfunktion), 2 Parameter.
  - Normierung: exakte Summe bis s = 3000, darueber Integral auf einem log-Gitter (4001 Punkte).
  - AIC = 2k + 2 NLL.
- **"Potenzgesetz ueber mindestens 2 Dekaden" (P2D)** heisst, alle fuenf Bedingungen gelten:
  - (a) M1 schlaegt beide Alternativen deutlich: AIC(M2) - AIC(M1) >= 10 und AIC(M3) - AIC(M1) >= 10.
  - (b) Fenster: s_c(M1) >= 100 s_min = 200, also reicht der Potenzbereich [s_min, s_c] ueber mindestens 2 Dekaden.
  - (c) Fitguete: Log-Bins (10 je Dekade ab s = 2); in jedem Bin mit mindestens 100 Lawinen und Obergrenze <= s_c/2
    weicht die Zahl hoechstens um den Faktor 10^0,15 (1,41) vom M1-Erwartungswert ab; mindestens ein solcher Bin.
  - (d) Die Daten fuellen das Fenster: mindestens 50 Lawinen mit s >= 200.
  - (e) Abbruchanteil (Status 2 oder 3) unter den Lawinen s >= 1 hoechstens 0,1 %.
- **Entscheidbarkeit:** P2D = "ja" nur mit mindestens 5000 Lawinen in der Fitstichprobe. P2D = "nein", wenn (e) verletzt
  ist (gleich welche Zahl), oder wenn bei mindestens 1000 Lawinen eine der Bedingungen (a) bis (d) verletzt ist. Sonst
  "nicht bestimmbar".
- **tau:** M1-Schaetzwert; 95-%-Intervall aus Block-Bootstrap (20 zeitlich zusammenhaengende Bloecke, 100 Ziehungen).
- **s_c fuer KH3 (Hauptschaetzer):** Momentverhaeltnis s_c2 = <s^2>/<s> ueber alle Lawinen s >= 1 (auch Abbrueche mit
  ihrem s). Fuer 1 < tau < 2 waechst s_c2 wie das Abschneiden [L, Standard der Endlichgroessen-Skalierung]. Fehler aus
  Block-Bootstrap (20 Bloecke, 200 Ziehungen). Zweitschaetzer (nur berichtet): s_c aus M1.
- **D:** Steigung der Ausgleichsgeraden log s_c2 gegen log N ueber N = 500, 2000, 8000. Fehler: 200 Bootstrap-
  Tripel (je N unabhaengig gezogen), 95-%-Intervall aus den 2,5- und 97,5-%-Quantilen.
- Dauer T und Flaeche A: M1-Fit auf T >= 2 bzw. A >= 2, nur beschreibend.

## 7. Urteilsregeln [F]

- **Eichung (BTW, Abschnitt 8):** bestanden, wenn P2D fuer BTW bei N = 8000 "ja" ist. Ist sie nicht bestanden, verwirft
  die Methode auch einen bekannten Sandhaufen. Dann wird jedes Urteil, das auf P2D = "nein" beruht, zu "nicht
  entscheidbar (Eichung)". Urteile aus P2D = "ja" bleiben.
- **KH0 (Plan = Wortlaut):** eingetroffen, wenn auf der Kugel (beide Arme, alle drei N, Anfangsrelaxation,
  Einschwingen und Messung) nach jedem Schritt Summe q = 12 exakt ist, kein Grad < 3 auftritt, die Kantenzahl gleich
  bleibt (Doppelkante = Ueberschreiben eines Schluessels) und alle vollen Strukturpruefungen fehlerfrei sind (alle
  2000 Schritte und an jedem Phasenende: Grade, Kanten, Dreiecke, Euler-Charakteristik, Ladungssumme, jeder Stern ein
  geschlossener Kreis). Sonst nicht eingetroffen.
- **KH1 nach Plan:** Hauptarm Z, Scheibe, N = 8000. Eingetroffen, wenn P2D = "ja" und 1,0 <= tau <= 1,6 (Schaetzwert).
  Nicht eingetroffen, wenn P2D = "nein" oder tau ausserhalb. Sonst nicht entscheidbar.
- **KH2 nach Plan:** Hauptarm Z, Kugel, alle drei N. Eingetroffen, wenn P2D bei allen drei N "nein" ist. Nicht
  eingetroffen, wenn P2D bei mindestens einem N "ja" ist. Sonst nicht entscheidbar.
- **KH3 nach Plan:** Hauptarm Z, Scheibe. Eingetroffen, wenn die untere 95-%-Grenze von D > 0,3 ist und s_c2 mit N
  streng waechst. Nicht eingetroffen, wenn die obere 95-%-Grenze <= 0,3 ist. Sonst nicht entscheidbar.
- **Nach Kartenwortlaut:** Die Karte nennt keinen Arm. Gleiche Regel fuer Arm Z und Arm D; gleiches Urteil in beiden
  Armen = dieses Urteil; verschiedene entscheidbare Urteile = "armabhaengig (teilweise)"; ist ein Arm nicht
  entscheidbar = "nicht entscheidbar".
- Die Urteile rechnet `ksh.py aus` (eingefroren) mechanisch aus aus/urteile.json. Alles nach der ersten Sicht ist
  Nachtrag, markiert und nur beschreibend.

## 8. Kontrollen [F]

- **BTW auf demselben Graphen:** BTW-Sandhaufen auf den Start-Scheibengraphen derselben Saat (N = 500, 2000, 8000).
  Schwelle = Grad, Kippen gibt je ein Korn an jeden Nachbarn, Randecken sind Senken. Start aus der hoechsten stabilen
  Belegung (rekurrent), 2 N Koerner Einschwingen. Gleiche Auswertung (P2D, tau, s_c2, D).
  - Erwartung [L]: tau ~ 1,2 bis 1,3, s_c ~ L^2,7 ~ N^1,35.
  - Das prueft die Methode, nicht das Modell.
- **Zufaellig gegen deterministisch:** Arm D auf denselben Netzen, gleiche Auswertung (Kartenwortlaut-Spalte).
- **Antriebsrate (versteckter Parameter, SOC-RAUM-L 4.6):** Scheibe, Arm Z, N = 2000. Waehrend der Lawine folgt mit
  Wahrscheinlichkeit r nach jedem Kipp-Flip ein zusaetzlicher Antriebsflip (er zaehlt nicht in s). r = 0 ist der
  Hauptlauf (volle Zeitskalentrennung), dazu r = 0,01 und 0,1. Berichtet: tau, s_c2, P2D je r.
  - Merkmal "Exponent stabil": abs(tau(0,01) - tau(0)) <= 0,1.
  - Wandern tau oder s_c2 mit r, ist das versteckte Abstimmung (Bonachela/Munoz laut SOC-RAUM-L); nur beschreibend,
    kein eigenes Urteil.
- **Zusatzkontrolle Scheibe:** gleiche Pruefungen wie KH0 mit Summe q = 6 (Rand als 4 - c gezaehlt), beschreibend.

## 9. Laufliste (.69, kleintest.sh; Arbeitsordner /home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-1/)

| Lauf | Spur | Aufruf (python code/ksh.py ...) | Wanduhr erwartet |
|---|---|---|---|
| L1 | cpu | lauf --geo kugel --arm Z --N 500,2000,8000 --budget 50,90,300 --seed 11 --out lauf/kugel-Z | ~450 s |
| L2 | cpu7 | lauf --geo kugel --arm D --N 500,2000,8000 --budget 50,90,300 --seed 12 --out lauf/kugel-D | ~450 s |
| L3 | cpu | lauf --geo scheibe --arm Z --N 500,2000,8000 --budget 50,90,300 --seed 13 --out lauf/scheibe-Z | ~450 s |
| L4 | cpu7 | lauf --geo scheibe --arm D --N 500,2000,8000 --budget 50,90,300 --seed 14 --out lauf/scheibe-D | ~450 s |
| L5 | cpu | lauf --geo scheibe --arm Z --N 2000 --budget 150 --r 0.01,0.1 --seed 15 --out lauf/rate | ~300 s |
| L6 | cpu7 | btw --N 500,2000,8000 --budget 40,80,300 --seed 16 --out lauf/btw | ~420 s |
| AUS | cpu | aus --ein lauf/kugel-Z.json lauf/kugel-D.json lauf/scheibe-Z.json lauf/scheibe-D.json lauf/btw.json lauf/rate.json --out aus/urteile.json --bild aus | ~2 min |

- Je Lauf hoechstens 600 s (RuntimeMaxSec). Bricht ein Lauf ab (rc != 0), wird er einmal mit demselben Aufruf
  wiederholt (gekennzeichnet). Fehlt danach ein Fall, ist das betroffene Urteil "nicht entscheidbar".
- Eingefrorener Code per scp in einen neuen Ordner, dann mv nach code/ (nie in place). Laufketten code/kette-cpu.sh
  und code/kette-cpu7.sh nur mit der Reihenfolge dieser Liste. AUS startet in der Kette cpu, sobald die Kette cpu7 ihre
  Marke lauf/kette-cpu7.fertig geschrieben hat (Warten hoechstens 20 min).
- Schlusszeit: Nach 12:55 CEST startet kein neuer Lauf.

## 10. Rauchtests (vor dem Einfrieren)

- Gleicher Code mit Budgets 2, 2, 4 s je Fall (Saaten 91 bis 96), Ausgabe nach rauch/. Gelesen werden nur rc,
  Laufzeiten, Dateinamen und JSON-Schluessel, keine Werte zu Lawinen, Fits oder Urteilen.
- Ergebnis (09:30:30 bis 09:32:33 UTC, Code code-r1 sha256 50b76939...): r1 bis r7 alle rc = 0. Laufzeit des Falls
  scheibe-D-N8000 16,7 s bei Budget 4 s (Ueberschreitung durch Anfangsrelaxation bzw. eine lange Lawine; im
  Hauptlauf bei 300 s Budget unkritisch). Die Auswertung r7 gab zwei Warnungen (leere Messhaelfte bei Faellen ohne
  Messschritte, Legende ohne Eintraege). Danach zwei Robustheitsaenderungen vor dem Einfrieren: Mittelwert einer leeren
  Haelfte = None, Legende nur mit Eintraegen. Sonst keine Codeaenderung.

## 11. Erwartung des Code-Agenten (vorab, nicht bindend, nur zur Kalibrierung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| E1 | KH0 eingetroffen | 95 % |
| E2 | Die Scheibe zeigt nach Plan kein P2D (KH1 nicht eingetroffen) | 60 % |
| E3 | Die Kugel hat einen Abbruch- oder Zyklusanteil ueber 0,1 % in mindestens einem Arm | 40 % |
| E4 | BTW-Eichung bestanden | 80 % |
| E5 | KH3 nach Plan eingetroffen | 35 % |

## 12. Vorab-Negativliste

- Kein Ergebnis dieses 2D-Modells sagt etwas ueber Lambda, Schwerewellen oder Finns 3D-Netz direkt.
- "SOC gezeigt" nur, wenn KH1 und KH3 eingetroffen sind UND die Antriebsrate-Kontrolle stabil ist; sonst hoechstens
  "Potenzgesetz unter diesen Regeln".
- Ein Exponent ohne die BTW-Eichung derselben Methode wird nicht zitiert.
