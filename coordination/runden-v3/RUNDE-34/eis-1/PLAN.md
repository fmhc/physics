# EIS-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 34)

- Abschnitte 1 bis 5 (Modell, Laeufe, Messgroessen, Urteile, Kontrollen mit Schreibtisch) geschrieben ab
  2026-10-03 18:40:10 CEST (date). Die Rauchlaeufe (Abschnitt 6, Gittergroessen 2 und 6, nicht die echten) habe ich um
  16:38:46 UTC (18:38:46 CEST) gestartet, kurz vor diesem Text; ihre Ausgaben lese ich erst nach dem Schreiben der
  Abschnitte 1 bis 5. Abschnitt 6 und die Pruefsummen (7) kommen danach, vor dem Einfrieren.
- Karte: KARTE.md (unveraendert). Vorhersagen E0 bis E3 und ihre Bedeutung stehen dort fest.
- Code (code/): gitter.py (Geometrie), eis_kern.c und eis_mc.py (Teil 1), stabnetz.py (Teile 2 und 3),
  auswertung.py (mechanische Urteile), rauch.sh und laeufe.sh (Startskripte).
- Einheiten: Kantenlaenge der kubischen Zelle = 1, alle Abstaende r in Zellkanten. Spin-Eis: F in Einheiten von T.
  Stabnetze: k = 1, Fehlpass delta = 1 (linear, Kraefte skalieren mit delta).

## 1. Modell

- **Pyrochlor-Gitter:** kubische Zelle mit 16 Ecken (fcc-Gitter mit Basis (0,0,0), (0,1/4,1/4), (1/4,0,1/4),
  (1/4,1/4,0)), periodisch, L^3 Zellen. Je Ecke ein oberes und ein unteres Tetraeder (Mitten = Ecke +- 1/8 (+-1,+-1,+-1)
  je Untergitter); die Mitten bilden das Diamantgitter. Soll: 16 L^3 Ecken, 8 L^3 Tetraeder, 48 L^3 Kanten (Laenge
  sqrt(2)/4), je Ecke 6 Nachbarn. gitter.py prueft das in jedem Lauf.
- **Teil 1, Spin-Eis (T -> 0):**
  - Ising-Spin je Ecke entlang der Verbindung der beiden Tetraedermitten; sigma = +1 heisst "zeigt ins obere
    Tetraeder". Fuer Tetraeder t ist ein Spin "rein", wenn er in t hinein zeigt. Q_t = (#rein - #raus)/2.
  - Anfang: Eiszustand (Untergitter 0, 1: +1; 2, 3: -1; alle Q = 0, geprueft), dann ein Spin umgeklappt: Q = +1 in
    einem unteren, Q = -1 in einem oberen Tetraeder.
  - Zug: einer der zwei Defekte mit W. 1/2, eine der 4 Ecken seines Tetraeders mit W. 1/4. Der +1-Defekt springt nur
    ueber einen "rein"-Spin, der -1-Defekt nur ueber einen "raus"-Spin: Umklappen, der Defekt sitzt danach im
    Nachbartetraeder dieses Spins. Sonst Ablehnung (Bleiben). Waere das Nachbartetraeder der andere Defekt
    (Vernichtung), wird abgelehnt.
  - Gleichgewicht: Jeder Zustand mit genau zwei Defekten (|Q| = 1) hat genau 6 erlaubte Zuege (je Defekt 3 passende
    Spins), jeder mit W. 1/8 vorgeschlagen; der Rueckzug hat dieselbe W. Der Vorschlag ist symmetrisch, Ablehnung =
    Bleiben, also ist die Gleichverteilung ueber alle Zustaende mit zwei Defekten stationaer. Eine Metropolis-Korrektur
    ist nicht noetig, weil die Zahl der waehlbaren Spins nicht vom Tetraeder abhaengt (immer 3 von 4; geprueft ueber
    den Ablehnungsanteil 1/4 und die Ladungspruefung).
  - Gegentypen: Mit dieser Konvention lebt ein +1-Defekt auf beiden Tetraederarten; jeder Sprung wechselt die Art.
    g(r) zaehlt deshalb alle geordneten Tetraederpaare (t+, t-), t+ != t-, beider Arten. Gemessen und berichtet: Anteil
    des +1-Defekts auf oberen Tetraedern (erwartet 1/2).
  - Abtastung im C-Kern (gcc -O2 in der Spur uebersetzt, Zufall xoshiro256**). Einlauf ohne Messung, dann Bloecke fester
    Laenge bis zu einer internen Zeitgrenze; je Block ein eigenes Histogramm von r^2 (Minimalbild, ganzzahlig in 1/64)
    alle m Schritte.
- **Teil 2, Pyrochlor-Stabnetz:** Knoten = Pyrochlor-Ecken, Staebe = die 48 L^3 Kanten (k = 1, Ruhelaenge = Abstand).
  Kompatibilitaetsmatrix C (Staebe x 3N), Dehnung e = C u. Fehlpass: Eigendehnung delta = 1 im Stab von (0,0,0) nach
  (0,1/4,1/4) (Richtung [011]).
- **Teil 3, Tetraeder-Oktaeder-Netz:** fcc-Knoten (4 L^3), Staebe zu allen 12 naechsten Nachbarn (24 L^3 Staebe).
  Fehlpass delta = 1 im Stab von (0,0,0) nach (0,1/2,1/2) (ebenfalls [011]).
- **Loeser (Teile 2, 3):**
  - Hauptweg: minimiere |C u - e0|^2 / 2 mit scipy.sparse.linalg.lsqr ohne Regularisierung (atol = btol = 1e-15). Die
    Stabkraefte t = C u - e0 sind die Projektion von -e0 auf den Kern von C^T (Eigenspannungen); Starrkoerper- und
    Gittermoden aendern C u nicht, darum ist t eindeutig, und es braucht keine Zusatzfeder (Regel: keine).
  - Gegenweg: exakte Projektion ueber die Bloch-Zerlegung der kubischen Zelle: je Wellenvektor q = 2 pi n / L die
    Matrix C(q) (Pyrochlor 48 x 48, fcc 24 x 12), SVD, Eigenspannungen = linke Singulaervektoren zu Singulaerwerten
    < 1e-9 x groesster Singulaerwert (ueber alle q). t aus der inversen FFT der Projektor-Spalte.
- **Eigenspannungen zaehlen (E3):** Staebe minus Rang(C).
  - Hauptweg: dichte SVD der reellen Matrix fuer L = 3, 4, 5 (Rangschwelle 1e-9 x groesster Singulaerwert, die Luecke
    zwischen groesstem "Null"- und kleinstem Nicht-Null-Wert wird berichtet).
  - Gegenweg: Bloch-Summe ueber alle q fuer L = 3, 4, 5, 8, 12.

## 2. Laeufe (echt)

| Lauf | Teil | Groesse | Zweck |
|---|---|---|---|
| eis_L12_s1, eis_L12_s2 | 1 | L = 12, Seeds 1 und 2 | E0 (gewertet) |
| eis_L8_s1, eis_L8_s2 | 1 | L = 8, Seeds 1 und 2 | Endlichkeitskontrolle |
| stab_pyro_L12, stab_pyro_L8 | 2 | L = 12 (gewertet), 8 | E2 |
| stab_fcc_L12, stab_fcc_L8 | 3 | L = 12 (gewertet), 8 | E1 |
| zaehl_pyro_dicht | 2 | L = 3, 4, 5 | E3 (gewertet) |
| zaehl_pyro_bloch | 2 | L = 3, 4, 5, 8, 12 | Gegenweg E3 |
| zaehl_fcc_dicht, zaehl_fcc_bloch | 3 | L = 3, 4, 5 (dicht), 3, 4, 5, 8, 12 (Bloch) | Vergleich |
| auswertung | alle | | Urteile, lauf-69/auswertung.json |

- Spin-Eis je Lauf: interne Zeitgrenze 540 s (Spur bricht bei 600 s ab), Stichprobe alle m = 4 Schritte. Einlauf- und
  Blocklaenge lege ich nach der im Rauchlauf gemessenen Geschwindigkeit fest (Abschnitt 6), vor dem Einfrieren.
- Spuren: hoechstens zwei zugleich (cpu und cpu2), je Spur nacheinander; Startskript code/laeufe.sh.
- Bricht die Spur einen Lauf ab (rc != 0), wird er offengelegt und nicht gewertet. Fehlt ein gewerteter Lauf, ist das
  zugehoerige Urteil "nicht auswertbar".

## 3. Messgroessen

- **Spin-Eis:**
  - P(r) = Anteil der Stichproben mit Defektabstand r (Minimalbild zwischen den Tetraedermitten, exakte Schalen r^2).
  - g(r) = Zahl der geordneten Tetraederpaare im Abstand r (alle Arten), normiert auf alle Paare.
  - F(r) = -ln[P(r)/g(r)] (F = 0 bei Gleichverteilung); Fehler je Schale aus der Streuung der Blockwerte von P.
  - Ausgleich F = a - C r^(-p) mit Gewichten 1/sigma_F^2; p auf festem Gitter 0,05 bis 6 (Schritt 0,001), a und C
    linear. **Bereich: 0,8 <= r <= 0,19 L** (L = 12: [0,8; 2,28]; L = 8: [0,8; 1,52]). Ausgeschlossen sind damit die
    zwei innersten Schalen (0,433 und 0,707), also der Kern.
  - Begruendung der Obergrenze (Schreibtisch, vor jeder Rechnung): Auf dem Torus ist das Coulomb-Potential
    1/(4 pi r) + r^2/(6 L^3) + ...; der oertliche Exponent des Ausgleichs ist dann p_eff = 1 + 3x/(1-x) mit
    x = (4 pi/3)(r/L)^3. Bei r = 0,19 L ist p_eff = 1,09; weiter aussen waechst der Fehler schnell.
  - Unsicherheit von p: Jackknife ueber 10 Blockgruppen (nur berichtet).
  - Gegenprobe (nur berichtet): Gitter-Coulomb in Gauss-Naeherung, F_G = 2 [G(0) - G(r)] mit G = Pseudo-Inverse des
    Diamant-Laplace auf demselben Torus, durch dieselbe Ausgleichsroutine mit denselben Schalen und Gewichten.
- **Stabnetze:**
  - Je Stab: |t|, Abstand r seines Mittelpunkts vom Mittelpunkt des Fehlpass-Stabs (Minimalbild), Richtung.
  - Abstandsklassen der Breite 0,25.
  - Richtungskegel mit halbem Oeffnungswinkel 10 Grad um Achsen (beide Richtungen), in Gruppen nach dem Winkel zum
    Fehlpass-Stab ([011]): 110_par ([011], 0 Grad), 110_senk ([01-1], 90), 110_60 ([110], [1-10], [101], [10-1];
    60), 100_senk ([100], 90), 100_45 ([010], [001]; 45), 111_35 ([111], [-111]; 35,3), 111_90 ([11-1], [1-11]; 90).
  - Je Klasse und Kegel: Maximum von |t| (Huellkurve) mit dem Abstand des Stabs, der es annimmt. Kugelgemittelt: Maximum
    und quadratisches Mittel ueber alle Staebe der Klasse.
  - Exponent = minus Steigung von log(max |t|) gegen log r, kleinste Quadrate, ueber die Klassen mit Mitte in
    **[1,0; L/4]** (L = 12: [1; 3], L = 8: [1; 2]) und max |t| > 1e-9 (Messschwelle). Mindestens 3 Klassen, sonst
    "kein Exponent (Kraft unter der Schwelle)".
  - Linie durch den Fehlpass-Stab (kollineare, parallele Staebe): Kraefte berichtet; groesste |t| abseits dieser Linie
    berichtet.
- **Zusatz (nur berichtet):** Wechselwirkungsenergie zweier Fehlpaesse in Stab b0 und b ist delta^2 P(b, b0) = -delta t_b
  (Reziprozitaet). Sie folgt also ohne eigenen Lauf aus derselben Antwort; ich berichte sie als diese Identitaet.

## 4. Urteile (mechanisch, auswertung.py)

Woertlich aus der Karte:

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| E0 | Spin-Eis: F(r) ist anziehend, und der beste Exponent p liegt in [0,8; 1,2] (Coulomb); Kontrolle aus der Literatur | 80 % |
| E1 | Steifes Tetraeder-Oktaeder-Netz: Stabkraft eines Fehlpasses faellt mit Exponent in [2,5; 3,5] (Elastizitaet, Dipol) | 75 % |
| E2 | Isostatisches Pyrochlor-Netz: in mindestens einer Gitterrichtung faellt die Stabkraft mit Exponent <= 1,5, also deutlich langsamer als im steifen Netz | 55 % |
| E3 | Pyrochlor-Netz: Die Zahl der Eigenspannungen waechst mit der Gittergroesse (ausgedehnte Eigenspannungen, wie bei RUM-Gittern), statt konstant zu bleiben | 60 % |

Regeln:
- **E0:** eingetroffen genau dann, wenn bei L = 12 (beide Seeds zusammen) C > 0 (anziehend) und das beste p in
  [0,8; 1,2] liegt. L = 8 und die Gauss-Gegenprobe werden berichtet und aendern das Urteil nicht.
- **E1:** eingetroffen genau dann, wenn bei L = 12 der Exponent der kugelgemittelten Huellkurve (Maximum je Klasse) in
  [2,5; 3,5] liegt.
- **E2:** eingetroffen genau dann, wenn bei L = 12 der kleinste Exponent ueber die sieben Kegelgruppen (Maximum je
  Klasse, nur Gruppen mit mindestens 3 Klassen ueber der Schwelle) <= 1,5 ist. Hat keine Gruppe genug Klassen ueber der
  Schwelle, ist E2 nicht eingetroffen.
- **E3:** eingetroffen genau dann, wenn die Zahl der Eigenspannungen des Pyrochlor-Netzes (dichte SVD, Staebe minus
  Rang) ueber L = 3, 4, 5 streng steigt.
- Bedeutung: nach der Karte, ohne Aenderung. Deutungen in ERGEBNIS.md als [H].

## 5. Kontrollen und Schreibtisch

- **Schreibtisch (vor jeder Rechnung, [M] bzw. [H]):**
  - Spin-Eis, Gauss-Naeherung: Jede Kante traegt Fluss +-1, der divergenzfreie Anteil haelt die Haelfte der
    Freiheitsgrade, also Steifigkeit K' = 1/2 und F(r) = 2 [G(0) - G(r)] mit G ~ 1/(4 pi r) (Diamant-Laplace,
    Zellkante 1). Erwartung: F(r) ~ a - 0,16/r. Der Unterschied von r = 0,8 bis 2,28 ist nur ~0,13 T; die
    Statistik muss F je Schale auf ~0,005 treffen. [H] fuer den genauen Vorfaktor (das echte Eismodell weicht von der
    Gauss-Naeherung ab).
  - Pyrochlor-Stabnetz, Maxwell: 48 L^3 Staebe = 48 L^3 Freiheitsgrade, also Nullmoden = Eigenspannungen.
  - [M] Jede Kante liegt auf einer geraden Linie entlang einer der sechs <110>-Richtungen (in jedem Tetraeder eine Kante
    je Richtung). Eine Linie schliesst sich auf dem Torus nach 4 L Staeben; es gibt 12 L^2 Linien. Gleicher Zug entlang
    einer geraden Linie ist im Gleichgewicht, also ist jede Linie eine Eigenspannung: mindestens 12 L^2
    (L = 3, 4, 5: 108, 192, 300). Vorhersage [H]: genau 12 L^2, dann E3 eingetroffen.
  - Sind die Linien alle Eigenspannungen, so ist P(b, b0) = 1/(4 L) fuer b auf der Linie des Fehlpass-Stabs und 0
    sonst. Erwartet: t = -delta/(4 L) auf allen 4 L Staeben dieser Linie (L = 8: -0,03125; L = 12: -0,02083), null
    abseits. Exponent in 110_par dann ~0, die anderen Kegel ohne Kraft ueber der Schwelle; E2 waere eingetroffen, aber
    mit einer Kraft, die mit 1/L faellt (Endlichkeitseffekt der geschlossenen Linie).
  - fcc-Netz: 24 L^3 Staebe, 12 L^3 Freiheitsgrade, nur 3 Translationen als Nullmoden erwartet, also 12 L^3 + 3
    Eigenspannungen. Antwort wie ein elastischer Kraftdipol, |t| ~ 1/r^3; im Fehlpass-Stab etwa -delta/2.
- **Spin-Eis:**
  - Eisregel nach jedem Zug: Ladung des verlassenen Tetraeders 0, des neuen +-1 (im Kern gezaehlt, Soll 0 Fehler).
  - Nach jedem Block: alle Tetraeder, genau ein +1 und ein -1 an den gefuehrten Orten, kein |Q| = 2.
  - Ablehnungsanteil wegen Orientierung (Soll 1/4), Anteil +1 auf oberen Tetraedern (Soll 1/2).
  - Einlauf: Betrag des Gesamtmoments sinkt vom polarisierten Anfang auf Rauschniveau (berichtet).
  - Seeds gegeneinander und erste gegen zweite Haelfte (berichtet).
  - Endlichkeit: L = 8 gegen 12, dazu die Gauss-Gegenprobe auf beiden Groessen.
- **Stabnetze:**
  - Gitterzahlen (Knoten, Staebe, Nachbarn, Stablaengen).
  - Gleichgewicht der Kraefte: max |C^T t| (Soll < 1e-8).
  - lsqr gegen Bloch-Projektion: max |t_lsqr - t_Bloch| (Soll < 1e-8).
  - Eigenspannungen dicht gegen Bloch bei L = 3, 4, 5 (Soll gleich).
  - Endlichkeit: L = 8 gegen 12.

## 6. Rauchlaeufe und Aenderungen danach (geschrieben ab 18:46:16 CEST, date)

- **Rauchlaeufe** (Ordner rauch-69/, Groessen 2 und 6, keine echte Groesse), gestartet 16:38:46 UTC, Ausgaben gelesen
  ab 18:41:45 CEST (nach Abschnitt 1 bis 5):
  - Spin-Eis L = 6, Seed 99: Einlauf 1e8, 18 Bloecke zu 2e8 Schritten, 80 s, 4,7e7 Schritte/s. Eisregel-Fehler lokal
    0, Vollpruefung nach jedem Block in Ordnung, Ablehnung wegen Orientierung 0,2500, +1 auf oberen Tetraedern 0,49999.
    Gesamtmoment 1994 -> 81 schon nach 5e6 Schritten, danach Rauschen (20 bis 150).
  - Stabnetze: Pyrochlor dicht L = 2: 48 Eigenspannungen (= 12 L^2); Bloch L = 2 und 6: 48 und 432 (= 12 L^2).
    fcc dicht L = 2: 99 (= 12 L^3 + 3), Bloch L = 6: 2595 (= 12 L^3 + 3). Luecke der Singulaerwerte: groesster
    "Null"-Wert <= 1,5e-15, kleinster anderer >= 0,18.
  - Antwort L = 6: Pyrochlor t_b0 = -0,0416667 = -1/(4 L), alle 24 Staebe der Linie gleich, abseits <= 4,6e-16;
    fcc t_b0 = -0,5006. Gleichgewichtsrest <= 1,3e-15, lsqr gegen Bloch <= 6,7e-16. Der Schreibtisch aus Abschnitt 5
    stimmt damit bei L = 2 und 6.
  - Gesehen, ohne Regelaenderung: In der Kugel-Huellkurve des fcc-Netzes liegen die Staebe der Fehlpass-Linie (bei
    0,71; 1,41; 2,12; 2,83) etwa 3- bis 4-mal ueber den Nachbarklassen (Zickzack). Die E1-Regel bleibt.
  - Gesehen beim Spin-Eis L = 6: F(r) + 0,159/r ist ab r ~ 1,2 nahezu konstant; die Gauss-Gegenprobe zeigt dieselbe
    Form. Die Ausgleichsrechnung bei L = 6 war entartet (nur 3 Schalen in [0,8; 1,14], p am Gitterende 6); das liegt an
    der kleinen Groesse.
- **Aenderungen nach dem Rauchlauf (vor dem Einfrieren):**
  1. **Untergrenze des E0-Bereichs 0,8 -> 1,15.** Grund: Bei L = 6 liegen die Schalen 0,829 und 1,0 sowohl im
     Monte-Carlo als auch in der Gauss-Gegenprobe etwa 0,01 ueber einer glatten Kurve a - C/r; ab der Schale 1,225
     streuen sie nur noch um <= 0,002. Der Gitterkern reicht also bis einschliesslich der Schale 1,09. Neuer Bereich:
     **1,15 <= r <= 0,19 L** (L = 12: [1,15; 2,28], 16 Schalen erwartet; L = 8: [1,15; 1,52]). Der Ausgleich ab 0,8
     wird nur berichtet. Die E0-Regel (C > 0, p in [0,8; 1,2] bei L = 12) bleibt sonst gleich.
  2. **Mehr Statistik fuer L = 12:** vier Seeds (1 bis 4) statt zwei, weil der engere Bereich p schlechter festlegt
     (Schaetzung sigma_p ~ 0,05). L = 8: zwei Seeds.
  3. **Laufparameter Spin-Eis:** Einlauf 2e9 Schritte (Momentabbau bei L = 6 in < 5e6; Reserve fuer L = 12 > 100-fach),
     Bloecke zu 5e8 Schritten, Stichprobe alle m = 4 Schritte, interne Zeitgrenze 540 s.
  4. **auswertung.py:** Schutz fuer leere oder zu kleine Bereiche (< 4 Schalen: "nicht auswertbar"), zusaetzlicher
     Ausgleich ab 0,8 (nur berichtet). Sonst unveraendert.
- **Laeufe:** code/laeufe.sh. Spur cpu: eis_L12_s1 bis s3. Spur cpu2: alle Stabnetz-Laeufe, dann eis_L12_s4, eis_L8_s1,
  eis_L8_s2. Danach auswertung.py auf cpu.

## 7. Einfrieren

- Eingefroren als PLAN.md.eingefroren-<Zeit> und code/*.eingefroren-<Zeit> (schreibgeschuetzt), vor dem ersten echten
  Lauf. Die Skripte schreiben ihre eigene sha256-Pruefsumme in jede Ausgabe (skript_sha256, kern_sha256).
