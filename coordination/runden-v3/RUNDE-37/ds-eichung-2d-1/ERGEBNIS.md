# DS-EICHUNG-2D-1: Ergebnis (Rechenagent, Claude-Subagent fuer die Leitung claude-primary)

- Vorab-Datei VORAB.md vor der ersten Rechnung. Karte (E1 bis E4) unveraendert. Synthetisch, keine Messdaten.
- Rohdaten und Tabellen: lauf-69/ (JSON je Lauf, auswertung.md, Ketten, Logs); Code: code/; Pruefsummen: PRUEFSUMMEN.txt.
- Messfunktionen unveraendert aus NETZ-DYN-1 (netzdyn.schalen, rueckkehr, ds_kurve; auswertung.dh_fenster, mittl_abstand), sha256 in PRUEFSUMMEN.txt gleich auf Laptop und .69.

## Ergebnis zuerst

1. **Die D1-Zahl d_H = 2,2 bis 2,3 ist kein Fehler im Netzkern und keine Nichtgleichgewichts-Folge, aber auch kein reiner Fensterfehler: Sie bleibt bis N = 64000 bestehen.**
   - Ein unabhaengiger Sampler der 1+1D-CDT (Schichtlaengen exakt gewichtet, Streifen gleichfoermig) gibt dieselben Zahlen wie netzdyn:
     <r> = 30,42 (N 4000) gegen 30,22 (netzdyn) und 56,30 (N 16000) gegen 56,27 bis 56,85 (netzdyn, drei Abschnitte); d_s-Kurven auf 0,01 gleich.
   - Fortsetzung des netzdyn-Laufs N2 = 16000 um etwa 1400 Sweeps: <r> 56,27, 56,43, 56,79, 56,85, also hoechstens +1 % Drift. D1 war nicht wegen zu kurzer Laufzeit verzerrt.
   - Groessenskalierung der CDT mit mehr Groessen: d_H = 2,25 (4000 nach 16000), 2,20 (16000 nach 64000), Anpassung ueber alle 2,22 (Bootstrap-Bereich 2,22 bis 2,23). Das **faellt nicht auf unter 2,15**.
   - Lokale d_H (r 6 bis 20) ist von N unabhaengig: 2,31, 2,33, 2,32 bei N = 4000, 16000, 64000. Bis r = 40 bleibt die zentrale Steigung bei 2,3 bis 2,4 (N 64000).
   - Das Netz-Werkzeug misst auf diesem Ensemble also stabil etwa 2,2 bis 2,35. Ob das eine echte Eigenschaft des Abstands im dualen Netz der CDT ist (Literatur: d_H = 2 [L], dort Eigenzeit-Abstand) oder eine sehr langsam abklingende Gitterkorrektur, ist **nicht entschieden**.
2. **Auf Zufallskarten mit bekannter Antwort (d_H = 4, d_s = 2 [L]) liegen die Werkzeug-Zahlen bei N <= 10^5 deutlich darunter.**
   - Viereckskarten (exakt, CVS): d_H aus <r>, Anpassung ueber N = 1000 bis 100000: 3,38; Paare 3,14, 3,27, 3,79 (16000 nach 64000, Bereich 3,64 bis 3,95). Lokal (r 6 bis 20) 1,6 bis 3,1, bei grossem N auf etwa 3,0 bis 3,3 ansteigend.
   - Mit Versatz <r> = a N^(1/4) + b passt d_H = 4 (a = 3,92, b = -5,7, chi2/ndf = 1,2); d_H = 3 oder 2 mit Versatz passen nicht (chi2/ndf 20 bzw. 156). Die Daten sind also mit d_H = 4 plus grossem negativem Versatz vertraeglich, mehr nicht.
   - d_s: Plateau sigma 20 bis 60 bei 1,55 bis 1,69, Maximum 1,68 (N 1000), 1,79 (4000), 1,83 (16000), 1,77 (64000), 1,81 (100000, 55 Proben). Bis sigma 3000 (N 4000, 16000): Maximum 1,82 bzw. 1,81. d_s = 2,0 +- 0,1 wird nicht erreicht.
3. **E1 bis E4:** E1 und E2 verfehlt, E3 verfehlt, E4 entgegengesetzt gerichtet (Abgleich unten). Auf der CDT-Seite liegt d_s dagegen bei 2,00 (sigma 300 bis 600, 2,01 bis 2,03 bei N 64000).
4. **Fuer grosse 4D-Laeufe folgt (Hypothese, aus dem 2D-Befund):** Ein d_H aus dem Fenster r 6 bis 20 oder aus einem Paar von zwei Groessen ist bei Durchmessern von 12 bis 14 (4D-Laeufe aus NETZ-DYN-1) nicht deutbar. Noetig sind mindestens drei bis vier Groessen mit gleicher Gestalt, volle Schalen (keine Abschneidung), Versatz im Ansatz und ein Gegentest an einem Ensemble mit bekannter Antwort bei gleichem N. Details unten.
5. **Nicht gerechnet:** spannbaumgewichtete Variante (Auftragspunkt 5; keine Zeit, und das Werkzeug braucht dafuer ein regulaeres Netz). Dreieckssampler exakt: nicht gebaut (siehe Grenzen).

## Methoden (was gerechnet wurde)

- **Vierecke (CVS):** Zyklenlemma-Dyck-Pfad, Etiketten-Schritte gleichverteilt in {-1,0,1}, Zusatzstelle fuer die Ecke 0, Nachfolgerregel, Rotationssystem aus den Sehnen, Flaechenverfolgung. Je Probe geprueft: Eulerzahl 2, alle Flaechen Vierecke, Dual 4-regulaer (in allen Proben bestanden). Dual hat Selbstschleifen (Bruecken, etwa 17 bis 33 % der Kantenenden); die Irrfahrt behandelt sie wie jede andere Kante.
  - Das sind **Vierecke, nicht die geforderten Dreiecke**. Gleiche Universalitaetsklasse (reine 2D-Gravitation), aber nicht dasselbe Ensemble.
- **Dreiecke (Flips):** einfache Triangulierung, Start Bipyramide, Flip nur wenn Grad >= 4 an den Enden und keine Doppelkante entsteht; Pruefung (Nachbarschaft, Eulerzahl 2) am Anfang und Ende jedes Abschnitts bestanden. Annahmerate 0,75 (N 16000). Nur bis N = 16000. Gleichfoermigkeit ueber einfache Triangulierungen gleicher Eckenzahl angenommen (Annahme, nicht gezeigt).
- **CDT (netzdyn):** unveraenderter Code, Fortsetzung der Zwischenstaende (Kopie von s0a), je Abschnitt --neu_mess.
- **CDT (l-Kette, neu):** Gewicht der Schichtlaengen W(l) = Produkt binom(l_t + l_(t+1) - 1, l_t - 1) (eigene Herleitung: Streifen zwischen zwei bezeichneten Ringen binom(a+b,a) a b / (a+b), durch Schichtbezeichnungen geteilt, Wurzel an Schicht 0; **nicht aus der Literatur belegt**). Metropolis mit Paaraustausch, Thermalisierung 4 bis 10 l^2 T Zuege, Abstand 0,5 l^2 T. Komplex mit netzdyn.Netz aufgebaut, Netz.pruefe bestanden (Euler 0, Profil = l), Dual per Netz.dual().
  - Seitenbefund: relative Profilstreuung der l-Kette 0,34 (N 4000), 0,36 (16000), 0,37 bis 0,39 (64000) gegen 0,26 bis 0,35 in netzdyn (N 16000: 0,32, 0,35, 0,28, 0,26 je Abschnitt; N 4000: 0,30). Leicht groesser; ob das an den Gewichten oder an zu kurzen netzdyn-Laeufen liegt, ist nicht geprueft. <r> und d_s stimmen trotzdem.
- **Messung:** wie NETZ-DYN-1: 24 (bei N >= 64000 zwoelf, nur jede 2.-6. Probe) Startpunkte fuer P(sigma), sigma bis 600 (dslang-Laeufe bis 3000), 16 Startpunkte fuer die Schalen, sch_rmax = 150 (wie s0a2) bzw. 400/450 bei den grossen Laeufen.

## Tabellen

Volle Tabellen: lauf-69/auswertung.md. Fehler: Standardfehler des Mittels ueber Proben. Unabhaengige Proben bei Vierecken und l-Kette; bei den Flips sind aufeinanderfolgende Proben nur grob unabhaengig.

### Messung je Groesse

| Familie | N | Proben | <r> | d_H lokal 6..20 | d_s sigma 30 / 100 / 300 | d_s-Maximum (sigma) |
|---|---|---|---|---|---|---|
| Vierecke (CVS) | 1000 | 400 | 16,37 +- 0,09 | 1,62 | 1,56 / 1,66 / 1,67 | 1,68 (189) |
| Vierecke | 4000 | 300 | 25,46 +- 0,15 | 2,62 | 1,56 / 1,68 / 1,77 | 1,79 (599) |
| Vierecke | 16000 | 91 | 38,92 +- 0,46 | 2,97 | 1,54 / 1,68 / 1,79 | 1,83 (599) |
| Vierecke | 64000 | 91 | 56,11 +- 0,52 | 3,08 | 1,57 / 1,66 / 1,72 | 1,77 (599) |
| Vierecke | 100000 | 55 | 64,98 +- 0,89 | 3,02 | 1,65 / 1,81 / 1,76 | 1,81 (135) |
| Dreiecke (Flips) | 1000 | 803 | 18,62 +- 0,06 | 1,93 | 1,58 / 1,61 / 1,58 | 1,61 (113) |
| Dreiecke | 4000 | 241 | 30,93 +- 0,18 | 2,51 | 1,61 / 1,65 / 1,66 | 1,66 (221) |
| Dreiecke | 16000 | 45 | 49,86 +- 0,82 | 2,70 | 1,61 / 1,64 / 1,69 | 1,73 (599) |
| CDT l-Kette | 4000 | 197 | 30,42 +- 0,04 | 2,31 | 1,85 / 1,96 / 2,00 | 2,00 (418) |
| CDT l-Kette | 16000 | 66 | 56,30 +- 0,10 | 2,33 | 1,84 / 1,95 / 2,01 | 2,01 (536) |
| CDT l-Kette | 64000 | 48 | 105,82 +- 0,23 | 2,32 | 1,83 / 1,95 / 2,01 | 2,03 (599) |
| CDT netzdyn D1 (alt) | 3982 | 1756 | 30,22 | 2,33 | 1,85 / 1,96 / 2,00 | 2,00 |
| CDT netzdyn D1 (alt) | 15939 | 706 | 56,27 | 2,35 | 1,84 / 1,95 / 2,01 | 2,02 |
| CDT netzdyn Fortsetzung | 15940 bis 15946 | 670, 627, 635 | 56,43, 56,79, 56,85 | 2,32, 2,33, 2,33 | 1,84 / 1,95 / 2,00 | 2,01 |

Hinweis: Zwei Laeufe mit sch_rmax = 150 waren bei N = 64000 (CDT, <r> 93,4, 19 Proben) und N = 100000 (Vierecke, 34 Proben) abgeschnitten und sind **nicht** in den Tabellen und Anpassungen (Dateien cdtx-T160-N64000-s303, quad-N100000-s105 bleiben als Rohdaten liegen); sie wurden mit sch_rmax 450 bzw. 400 neu gerechnet. Die 64000er CDT-Zeile fasst zwei Laeufe (s311, s312) zusammen.

### Groessenskalierung d_H aus <r> (Bootstrap, 16 bis 84 %)

| Familie | Paar / Anpassung | d_H | Bereich |
|---|---|---|---|
| Vierecke | 1000 -> 4000 / 4000 -> 16000 / 16000 -> 64000 / 64000 -> 100000 | 3,14 / 3,27 / 3,79 / 3,04 | 3,09-3,20 / 3,17-3,37 / 3,64-3,95 / 2,73-3,43 |
| Vierecke | Anpassung alle | 3,38 | 3,35 bis 3,40 |
| Dreiecke | 1000 -> 4000 / 4000 -> 16000 | 2,73 / 2,90 | 2,70-2,77 / 2,80-3,01 |
| CDT l-Kette | 4000 -> 16000 / 16000 -> 64000 | 2,25 / 2,20 | 2,24-2,26 / 2,19-2,21 |
| CDT l-Kette | Anpassung alle | 2,22 | 2,22 bis 2,23 |

### Anpassung <r> = a N^(1/d_H) + b (d_H fest, chi2 je Freiheitsgrad)

| Familie | d_H = 2 | d_H = 3 | d_H = 4 |
|---|---|---|---|
| Vierecke (5 Groessen) | 156 (b = +11,2) | 19,6 (b = +2,8) | 1,2 (b = -5,7) |
| Dreiecke (3 Groessen) | 33,8 | 0,43 | 2,7 |
| CDT l-Kette (3 Groessen) | 33,4 (b = +5,1) | 566 | 1437 |

(Dreiecke nur drei Groessen, zwei Parameter, ein Freiheitsgrad: nicht aussagekraeftig.)

### Lokales Wachstum der CDT-Schalen

- Lineare Anpassung n(r) = a (r - r0) im Fenster r 6 bis 20: r0 = 2,9 (D1 s0b2), 3,1 (s0a2), 2,75 / 2,97 / 2,88 (l-Kette N 4000 / 16000 / 64000). Das flache Torusnetz hat r0 = 0 (d_H = 2,000).
- Ein Versatz r0 etwa 3 allein macht die lokale Steigung bei r = 10 zu 1 + 10/7 = 2,4, bei r = 20 zu 2,2. Er erklaert aber nur das Fenster nahe 6 bis 20; fuer r = 20 bis 40 bei N = 64000 bleibt die Steigung bei 2,34 bis 2,40, also nicht gegen 2 laufend.

### Zentrale lokale d_H(r) (Auszug)

| Familie | N | r=3 | r=6 | r=10 | r=16 | r=25 | r=40 |
|---|---|---|---|---|---|---|---|
| Vierecke | 16000 | 2,22 | 2,70 | 2,94 | 3,04 | 2,45 | -0,02 |
| Vierecke | 100000 | 2,26 | 2,75 | 2,98 | 3,13 | 3,33 | 2,60 |
| CDT l-Kette | 16000 | 2,04 | 2,27 | 2,35 | 2,37 | 2,35 | 1,84 |
| CDT l-Kette | 64000 | 2,04 | 2,28 | 2,32 | 2,34 | 2,34 | 2,34 |

Bei kleinem N faellt die Kurve fuer grosse r durch den Durchmesser ab (z. B. N 1000 nach r = 16); gueltig sind nur r deutlich unter dem Maximum von n(r).

## Abgleich E1 bis E4 (beschreibend)

| Nr | Erwartung der Karte | Gemessen | Ausgang |
|---|---|---|---|
| E1 | Zufallstriangulierungen: d_s 1,9 bis 2,1 | Vierecke und Dreiecke: Plateau 1,55 bis 1,69, groesstes Maximum 1,83 (Vierecke N 16000, sigma bis 3000: 1,82); steigt mit N (1,68, 1,79, 1,83) dann 1,77 und 1,81 bei 64000 und 100000 (weniger Proben, zwoelf Startpunkte) | ausserhalb des Fensters |
| E2 | d_H Skalierung 3,7 bis 4,3; lokal darunter | Vierecke: Anpassung 3,38, nur das Paar 16000 -> 64000 gibt 3,79; Dreiecke 2,7 bis 2,9; lokal 1,6 bis 3,3, also unter der Skalierung | Skalierung ausserhalb des Fensters (mit einer Ausnahme bei einem Paar); lokal darunter wie erwartet |
| E3 | CDT d_H von 2,23 auf unter 2,15 bei groesserem N | 2,25 (4000 -> 16000), 2,20 (16000 -> 64000), Anpassung 2,22; lokal 2,31 bis 2,33 | nicht eingetroffen |
| E4 | lokale Verschiebung nach oben, auf beiden Ensembles gleich gerichtet | CDT: lokal ueber dem Skalenwert 2 (2,3). Karten: lokal unter dem Skalenwert 4 (3,0 bis 3,3 bei 10^5) | entgegengesetzt gerichtet |

Eigene Vorab-Erwartungen (VORAB.md): V1 (d_s 2,0 +- 0,1 bei Vierecken) 70 % und V2 (d_H 3,7 bis 4,3) 50 % nicht eingetroffen; V3 (lokal unter Skalierung) eingetroffen; V4 (CDT lokal >= 2,2 bleibt) eingetroffen; V5 (Skalierung auf unter 2,15) 45 % nicht eingetroffen; V6 (nicht gleich gerichtet) eingetroffen; V7 (reiner Fensterartefakt, 55 %) nur teilweise: Der Versatz erklaert das Fenster bei kleinen r, nicht die <r>-Skalierung.

## Urteil zu Punkt 6

- **Ist d_H = 2,3 aus D1 ein Methodenartefakt?**
  - Netzkern und Lauflaenge: nein (unabhaengiger Sampler gleich, Drift im Fortsetzungslauf <= 1 %).
  - Kleines Volumen: nein (gleiche Zahl bei 16-fachem N).
  - Schaetzer: **teilweise.** Die lokale Steigung im Fenster haengt von einem Versatz r0 etwa 3 im Schalenwachstum ab, der N-unabhaengig ist (UV-Struktur); auf dem flachen Netz ist er 0.
  - Rest: <r> skaliert mit 2,2 und n(r) waechst bis r = 40 wie r^1,35. Das ist entweder eine echte Eigenschaft des Graphenabstands im dualen CDT-Netz (nicht im Widerspruch zur Eigenzeit-Literatur, die einen anderen Abstand misst, aber das ist nur eine Lesart) oder eine Gitterkorrektur, die langsamer als 1/Wurzel(N) abklingt (<r>/Wurzel(N) = 0,481, 0,445, 0,418 bei N = 4000, 16000, 64000: Differenzen -0,036, -0,027 statt einer Halbierung). **Offen.** Ein Gegentest ist ein Ensemble mit d_H = 2 und bekanntem Graphenabstand (etwa ein flaches Delaunay-Netz; [S Abstract] arXiv:2405.11673 beweist nur die Konvergenz von Irrfahrten auf Delaunay-Netzen gegen Brownsche Bewegung mit kanonischen Leitwerten und bringt fuer d_H keine Zahl; nicht verwendet).
- **Welche Korrektur braucht das Werkzeug fuer grosse 4D-Laeufe?** (Hypothesen, aus 2D abgeleitet)
  1. Kein d_H aus einem festen Fenster (r 6 bis 20) oder einem Paar von zwei Groessen. Auf Viereckskarten liegen beide bei N = 10^5 noch bei etwa 3,0 bis 3,3 statt 4. Mindestens drei bis vier Groessen mit gleicher Gestalt (hier: T/Wurzel(N) fest) und eine Anpassung mit Versatz und mit festgehaltenem Vergleichsexponenten; dazu die Frage, ob d_H = 4 (mit b) oder ein kleinerer Wert besser passt.
  2. Volle Schalen (sch_rmax groesser als der Durchmesser, Abschneideflag pruefen): zwei meiner Laeufe waren bei r = 150 abgeschnitten und gaben <r> = 93 statt 106 (CDT N 64000).
  3. d_s: Erst ab N etwa 10^5 mit sigma bis mehrere hundert lesbar; auf Karten mit d_s = 2 liegt das Maximum bei N <= 10^5 bei 1,8. Der 4D-Befund "Maximum 3,9 bis 4,2 bei Torus mit N4 = 7000 bis 23000" ist daher eine Groessenabbildung des Gitters, wie in NETZ-DYN-1 schon vermutet, und kein Kandidat fuer ein Plateau.
  4. Gegentest bei gleichem N: eine Karte mit bekannter Antwort gleicher Groesse (hier: Viereckskarten) mit demselben Werkzeug mitrechnen und die Abweichung als Skala fuer die 4D-Zahl nehmen.

## Grenzen

- Viereckskarten statt Dreiecke fuer die grossen N; die Dreiecks-Flipkette nur bis N = 16000 (Dreiecks-N = 4000 bis 16000: nur 45 bis 241 Proben, Bootstrap-Bereiche zu eng, weil aufeinanderfolgende Proben nicht unabhaengig sind).
- Gleichfoermigkeit der Flipkette (Gleichgewicht, Ergodizitaet) nicht bewiesen; Gleichgewicht nur ueber <r> (erste gegen zweite Haelfte, 18,61/18,62 bei N 1000 und 30,89/30,96 bei N 4000; bei N 16000 53,5 +- 1,8 gegen 46,6 +- 0,7 im zweiten Lauf, also unruhig).
- Gewichte der l-Kette sind meine Herleitung; Beleg nur die Gleichheit von <r> und d_s mit netzdyn bei N 4000 und 16000 und die leicht abweichende Profilstreuung (siehe Methoden).
- Proben bei den grossen N wenige (CDT 64000: 48, Vierecke 100000: 55, d_s dort nur 12 Startpunkte und nur jede 2. bis 6. Probe): <r> auf 0,2 bis 1,4 %, d_s-Werte auf einige 0,01 unsicher. Die d_s-Zahl bei 64000/100000 ist daher schwaecher als bei 16000.
- Die dslang-Laeufe (sigma bis 3000) haben nur 15 (N 16000) bzw. 51 (N 4000) Proben mit je 24 Startpunkten.
- Die Fensterwahl (r 6 bis 20, sigma 20 bis 60) wurde nach dem Befund nicht veraendert; weitere Fenster stehen nur zusaetzlich (r 10 bis 30 beim Versatz, zentrale Kurve).
- Der Befund E3 widerlegt nicht d_H = 2 der CDT-Literatur: gemessen ist der Graphenabstand im dualen Netz im Bereich N = 4000 bis 64000.

## Regelabweichungen

- Ein Befehl schrieb kurz eine Datei nach /tmp (Dummy, sofort geloescht) und nutzte /dev/null als Umleitung; dazu liefen die ersten Hintergrundstarts mit `< /dev/null`. Danach vermieden (Logdateien). Das Werkzeug-Harness legt ausserdem selbst Ausgabedateien fuer Hintergrundbefehle unter /tmp/claude-1000 an (nicht von mir geschrieben).
- Ein stoerender Lauf auf cpu8 (anderer Agent, antigravity-nachbau-1) hielt meine Spur zeitweise; ich habe nichts davon angefasst.
- Die Ketten kette-cdtx und kette-quad habe ich selbst abgebrochen (eigene Prozesse, nach Erkennen der Abschneidung bei sch_rmax 150); abgebrochen waren dabei cx32000 (nie fertig) und cx64000b und q100000b.
- Abweichung von der Auftragsformulierung: Vierecke statt Dreiecke bei grossen N (siehe oben), sch_rmax 400/450 statt 150 bei den grossen Laeufen, zwoelf statt 24 Startpunkte fuer d_s bei N >= 64000.
- Zusatzlaufspuren: Es wurden nur cpu8, cpu9, cpu10 benutzt, jeder Lauf unter 10 min, df vorher (17 GB frei, ueber der Grenze von 10 GB). Die Gesamtzeit lag bei etwa 63 min.
- Zeitstempel: Rechenzeiten der .69 laufen in UTC (2 h hinter Berliner Zeit); lokale Zeiten per date.

## Einfach gesagt

Wir haben unser Messwerkzeug an Zufallsflaechen getestet, bei denen man die richtige Antwort kennt, und gesehen: Bei den Groessen, die wir rechnen koennen (bis etwa hunderttausend Stuecke), misst es "zu kleine" Dimensionen, weil diese Zahlen nur sehr langsam gegen den richtigen Wert laufen. Die 2,3 aus unserer 1+1-dimensionalen Kontrolle sind kein Rechenfehler und kommen nicht von zu kurzen Laeufen, bleiben aber auch bei sechzehnmal groesseren Netzen bei etwa 2,2; ob das echte Physik oder eine sehr langsame Gitterkorrektur ist, wissen wir noch nicht. Fuer die grossen 4D-Laeufe heisst das: nie eine Dimension aus einem einzelnen Fenster oder zwei Groessen ablesen, sondern mehrere Groessen, volle Messung und immer eine Vergleichsflaeche mit bekannter Antwort gleicher Groesse mitrechnen.

- Abschluss: 2026-10-07 14:40:06 CEST (date).
