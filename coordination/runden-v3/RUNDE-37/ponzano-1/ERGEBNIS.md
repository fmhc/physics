# PONZANO-1: Ergebnis (Runde 37, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 02:28:56 CEST.
  - Rauchlaeufe 00:29:26 bis 00:48:17 UTC.
  - Eingefroren 02:48:23 CEST: PLAN.md.eingefroren-20261004-024823 und code/ponzano.py.eingefroren-20261004-024823;
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 00:48:30 bis 00:56:00 UTC; Auswertung 00:56:05 bis 00:56:09 UTC; alle rc = 0.
  - Text ab 02:58:08 CEST.
- Plan und Rechencode sind nach dem Einfrieren unveraendert. Die Pruefsummen auf der .69 und lokal stimmen ueberein,
  lauf-69/ ist bitgleich mit der .69.
- Alle Zahlen sind exakte bzw. 50-stellige Rechnungen der Drehimpulsalgebra auf der .69, Spur cpu. Es sind keine
  Messdaten.
- **Kennzeichen:**
  - [S] an der Quelle gelesen: keine; in dieser Karte habe ich keine Quelle abgerufen;
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher;
  - [M] eigene Mathematik, [E] hier gerechnet, [H] Hypothese, [F] Festlegung im Plan.

## 1. Ergebnis zuerst

1. **Regges Wirkung steckt im 6j-Symbol [E].**
   - Das exakte 6j-Symbol folgt der Ponzano-Regge-Formel cos(sum (j+1/2) theta + pi/4)/sqrt(12 pi V).
   - Bei lambda = 100 ist die Abweichung e = 3,0e-4 (Form A) bzw. 6,6e-4 (Form B), also 30- bis 70-mal unter der
     Schwelle 0,02. Sie faellt wie 1/lambda (Steigung -0,96 bzw. -0,75).
   - Die Phase sitzt genau: In einer Spinfolge (Form A, lambda = 50) liegen alle 193 Vorzeichenwechsel des 6j im
     selben ganzzahligen Intervall wie die des Kosinus. Der groesste Lageunterschied betraegt 0,0016 Spin-Einheiten.
   - **PO1 eingetroffen.**
2. **Exakte Algebra ohne Ausnahme [E]:**
   - Orthogonalitaet: 101 Paare.
   - Biedenharn-Elliott (Pachner 2-3): 20 Zufallssaetze; dazu die sechs grossen Faelle von PO3 auf 1e-49.
   - 24 Symmetrien an 50 Symbolen.
   - 15 831 Vergleiche mit sympy, Sonderwert {a b c; 0 c b}.
   - Alles exakt rational; der mpmath-Pfad weicht um <= 4e-51 ab.
   - **PO0 eingetroffen.** "Umbenennen ist frei" gilt in 3D als exakte Identitaet [L, hier nachgerechnet].
3. **Ohne echtes Tetraeder klingt das 6j exponentiell ab [E].**
   - Form N: ln abs(6j) = -8,63 - 2,292 lambda.
   - R^2 = 0,999996 ueber lambda = 20 bis 200; bei lambda = 200 ist abs(6j) = e^-467.
   - **PO2 eingetroffen.**
4. **PO3 nicht eingetroffen [E].**
   - Der Schwerpunkt der Summandenbetraege liegt in allen sechs Faellen 28 bis 34 % unter der flachen Laenge x*.
   - Er sitzt da, wo ihn die Huellkurve (2x+1)/sqrt(V1 V2 V3) vorab hingelegt hat: Abweichung <= 3 % vom
     Huellkurvenschwerpunkt aus dem Rauchlauf. So war es im Plan vorhergesagt (A4, 85 %).
5. **Die Phase sammelt sich trotzdem geometrisch, an zwei Stellen [E, beschreibend, nicht geurteilt]:**
   - Die vorzeichenbehaftete Summe holt ihren Wert aus einem Fenster um x* (flacher Schluss, sum der Innenwinkel = 2 pi)
     und einem Fenster um x_fold (zweite, gefaltete flache Einbettung derselben neun Laengen).
   - **Fenster um x*:** Es trifft den PR-Term des konvexen Doppeltetraeders cos(S1 + S2 + pi/2)/(24 pi sqrt(V1 V2)) auf
     0,02 bis 2,1 %.
   - **Fenster um x_fold:** Es trifft den gefalteten Term cos(S1 - S2)/(24 pi sqrt(V1 V2)) auf 0,01 bis 0,25 %.
   - **Dazwischen** heben sich die Summanden weg: Die Betragssumme ist 13- bis 1409-mal groesser als das Ergebnis.
   - Das ist die Lesart der Karte fuer den Fall, dass PO3 ausbleibt: "die einfache Lesart gilt nur fuer die Phase,
     nicht fuer das Gewicht". Dazu kommt ein zweiter, gefalteter Sammelpunkt, den die Karte nicht nennt.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 5 durch code/auswertung.py; Werte in lauf-69/auswertung.json.

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | Kennzahlen |
|---|---|---|---|---|
| PO0 | Orthogonalitaet, BE, Symmetrien exakt bzw. 1e-30; Fremdbibliothek exakt | 90 % | **eingetroffen** | (a) 101 Paare in 10 Saetzen, 0 Fehler; (a2) j = 60 bis 90: 4,0e-51; (b) BE 20 Saetze (3 bis 11 x-Werte), 0 Fehler, mpmath 4,1e-51; (c) 50 x 24, 0 Fehler; (d) sympy 15 831 Faelle, 0 Fehler; (e) 0 Fehler; (f) 2,8e-51 |
| PO1 | Steigung in [-1,3; -0,7]; e(100) < 0,02 an beiden Formen | 70 % | **eingetroffen** | A: Steigung -0,957, e(100) = 3,0e-4. B: Steigung -0,751, e(100) = 6,6e-4 |
| PO2 | ln abs(6j) linear in lambda, R^2 > 0,99 (lambda = 20 bis 200) | 70 % | **eingetroffen** | N: R^2 = 0,9999960, Steigung -2,2916 je lambda-Schritt |
| PO3 | [H] Schwerpunkt nach Betrag innerhalb +-10 % von x* bei lambda >= 50 | 45 % | **nicht eingetroffen** | Abstand 0,328 / 0,334 / 0,336 (K1 bei lambda = 50/100/200), 0,276 / 0,289 / 0,280 (K2). Kontrolle BE <= 6,5e-50 in allen sechs Faellen |

**Agenten-Vorhersagen** (PLAN Abschnitt 6, vor den Hauptlaeufen)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (90 %) | PO0 eingetroffen; Edmonds 6.2.12 gilt in dieser Form | **eingetroffen**. Die Form ist per Rechnung bestaetigt (20 Zufallssaetze exakt, sechs grosse Faelle auf 1e-49) |
| A2 (60 %) | e(100) < 0,02; Steigungen schwanken, beide im Band | **eingetroffen**, B knapp (-0,751 gegen die Grenze -0,7) |
| A3 (85 % / 60 %) | PO2 fuer N; N_rand ebenfalls R^2 > 0,99 | **eingetroffen** / **eingetroffen** (N_rand: R^2 = 0,99997) |
| A4 (85 %) | PO3 nicht eingetroffen; x_c nahe am Huellkurvenschwerpunkt, 29 bis 35 % unter x* | **eingetroffen**: 28 bis 34 %, Abweichung vom Huellkurvenschwerpunkt 0,4 bis 3,0 % |
| A5 (50 %) | Fenster um x* trifft den konvexen PR-Term auf <= 30 % bei lambda = 200 | **eingetroffen**: 0,10 % (K1), 0,33 % (K2) |

## 3. Tabellen

### 3.1 PO1: e(lambda) = abs(6j - PR) * sqrt(12 pi V) [E]

| lambda | 5 | 10 | 20 | 50 | 100 | 200 | Steigung (log-log) | R^2 (log-log) |
|---|---|---|---|---|---|---|---|---|
| A (6, 7, 8, 7, 9, 5) | 5,97e-3 | 1,57e-3 | 1,55e-3 | 4,69e-4 | 2,97e-4 | 1,36e-4 | -0,957 | 0,967 |
| B (4, 9, 7, 10, 8, 6) | 5,61e-3 | 6,88e-3 | 4,25e-4 | 9,72e-4 | 6,61e-4 | 3,54e-4 | -0,751 | 0,663 |

- **e(lambda) schwankt stark.** Die dichte Kurve (lambda = 1 bis 200, Bild bild-fehler-loglog.png) springt zwischen
  Nachbarwerten um Faktoren bis etwa 100. Der 1/lambda-Fehlerterm hat selbst eine Phase [L?: Dupuis/Livine,
  Korrekturen zu PR].
- **Obere Huelle, nachtraeglich und nicht geurteilt:** max e ueber lambda = 10 bis 20 gegen 100 bis 200:
  - A: 2,29e-3 -> 2,97e-4, Steigung etwa -0,89;
  - B: 6,88e-3 -> 6,98e-4, Steigung etwa -0,99.
- **Phase (Spinfolge Form A, lambda = 50, j6 = CD):**
  - geometrischer Bereich j6 = 162 bis 606, innerer Bereich 206,4 bis 561,6;
  - 193 Vorzeichenwechsel des 6j, 193 des Kosinus, alle 193 im selben Intervall;
  - Lageunterschied der interpolierten Nullstellen hoechstens 0,0016, im Mittel 0,0003;
  - max e im inneren Bereich 1,9e-3.
  - Bild bild-spinfolge.png: Ausserhalb (grau) faellt das 6j ab, an den Raendern stehen die Airy-artigen Umkehrpunkte.

### 3.2 PO2: nicht geometrische Formen [E]

| Form | b | V^2/V_reg^2 | Steigung je lambda | R^2 (20..200) | ln abs(6j) bei 20 / 200 | Vorzeichen (lambda = 20..30) |
|---|---|---|---|---|---|---|
| N (geurteilt) | (10, 6, 7, 9, 6, 5) | -1,14 | -2,2916 | 0,9999960 | -53,6 / -466,6 | konstant + |
| N_rand (beschreibend) | (6, 7, 8, 7, 9, 13) | -0,33 | -0,7812 | 0,9999652 | -23,6 / -164,7 | wechselnd |

- V^2 < 0 fuer alle lambda = 1 bis 200 (beide Formen).
- Den Exponenten aus der PR-Fortsetzung (Winkel des nicht euklidischen Tetraeders) [L] habe ich nicht nachgerechnet.

### 3.3 PO3: 2-3-Zug [E]

Zeilen = Zahl der x-Werte, also 351 / 701 / 1401 bei lambda = 50 / 100 / 200.

| Fall | x* | x_c (Betrag) | abs(x_c - x*)/x* | Huellkurve (Rauch) | x_fold | Profilmax. | Fenster x* / PR konvex | Fenster x_fold / PR gefaltet | Betragssumme / abs(R) |
|---|---|---|---|---|---|---|---|---|---|
| K1, 50 | 278,1 | 187,0 | 0,328 | 181,5 | 52,2 | 52 | 0,9998 | 1,0025 | 232 |
| K2, 50 | 308,4 | 223,2 | 0,276 | 219,9 | 108,6 | 108 | 1,0214 | 0,9988 | 26,9 |
| K1, 100 | 555,9 | 369,7 | 0,335 | 360,0 | 104,9 | 105 | 0,9925 | 0,9997 | 22,0 |
| K2, 100 | 616,4 | 438,1 | 0,289 | 439,7 | 217,6 | 616 | 1,0015 | 0,9995 | 13,3 |
| K1, 200 | 1111,4 | 737,7 | 0,336 | 719,3 | 210,3 | 1112 | 1,0010 | 0,9984 | 31,0 |
| K2, 200 | 1232,4 | 887,7 | 0,280 | 879,1 | 435,6 | 1232 | 0,9967 | 0,99986 | 1409 |

- **Spalten:**
  - "Profilmax." ist die Lage des Maximums von abs(sum s(x) exp(-(x-c)^2/(2 lambda))).
  - "Fenster" ist die Summe mit Plateau +-3 sqrt(lambda) und cos^2-Uebergang bis +-6 sqrt(lambda).
- **Profilmaximum:** Es liegt immer an einer der beiden flachen Einbettungen, auf weniger als eine Einheit genau
  (Gitter der ganzen x). Welche gewinnt, haengt davon ab, welcher der beiden PR-Terme gerade betragsgroesser ist; beide
  Kosinus schwingen mit lambda.
- **Beide Fenster zusammen gegen das exakte Produkt R:** 0,993 / 1,001 / 0,998 / 1,001 / 1,001 / 0,900.
  - Bei K2, lambda = 200 heben sich die beiden PR-Terme fast auf: +6,38e-11 und -6,16e-11 ergeben R = 2,24e-12.
  - Dort werden Restfehler der Fenster zu 10 % von R.
  - PR fuer das Produkt selbst: 0,9897 von R.
- **Bild** bild-pachner-K1.png / -K2.png (lambda = 100):
  - Die Summanden fuellen den ganzen geometrischen Bereich.
  - Die Teilsumme springt nur bei x_fold und bei x* und ist dazwischen flach.
  - Das geglaettete Profil hat genau zwei Gipfel.
- Die Lage von x_fold am unteren Umkehrpunkt (K1: x_fold = 104,9, erster geometrischer Wert 105) liegt an der
  Konfiguration [M]: T1 und T2 sind aehnlich, darum sind in der gefalteten Lage alle drei Scharnierwinkel klein.

## 4. Kontrollen

- **Exakt gegen 50 Stellen:**
  - mpmath-Pfad gegen exakten Pfad 2,8e-51;
  - BE in den sechs PO3-Faellen: Summe gegen Produkt <= 6,5e-50 relativ, bei Ausloeschung bis Faktor 1409.
- **Unabhaengige Umsetzung:**
  - sympy.physics.wigner.wigner_6j, exakt: alle 15 625 Tupel mit 2j <= 4, darunter 13 600 mit verletzter Paritaet,
    die sympy ablehnt und meine Seite null setzt, sowie 570 von null verschiedene;
  - 200 Zufallssymbole bis j = 12;
  - die Formen A, B und N bei lambda = 5 und 10, also j bis 100.
  - Kein Unterschied.
- **Sonderwert** {a b c; 0 c b} = (-1)^(a+b+c)/sqrt((2b+1)(2c+1)): alle zulaessigen Tripel mit 2j <= 12 exakt.
- **Geometrie:**
  - V aus Einbettung gegen Cayley-Menger: 2e-50.
  - Schlaefli-Probe d(sum l theta)/dl_k = theta_k (Form A, lambda = 50, zentrale Differenz h = 1e-12):
    1,3e-29.
  - x* aus der Einbettung gegen den Defizitwinkel an DE: 2 pi - sum phi_i <= 3,2e-50 (Rauchlauf geometrie).
  - Durchstosspunkt von DE baryzentrisch positiv; beide Bipyramiden sind konvex.
- **Konvention** (Rauch, gleichseitiges Tetraeder j = 10 bis 80):
  - Aussenwinkel mit +pi/4: e = 6,8e-3 bis 1,5e-5.
  - Die drei anderen Moeglichkeiten liegen bei e = 0,4 bis 2,0.
- **Latten (v3):**
  - L1 (kann scheitern): PO1 bis PO3 ja, PO3 ist gescheitert. PO0 konnte nur an Code- oder Formfehlern scheitern.
  - L2 (Gegenprobe): sympy, Sonderwert, CM gegen Einbettung, Schlaefli, Defizit gegen Einbettung, BE bei grossem
    lambda, Huellkurve gegen Messung.
  - L3 (Numerik): exakt rational, sonst 50 Stellen ohne Ausloeschung.
  - L4 (schon bekannt):
    - Ponzano/Regge 1968, Roberts 1999, Biedenharn-Elliott und der verbotene Bereich [L].
    - Dass die PR-Asymptotik beide Orientierungen enthaelt und die stationaere Phase der Zustandssumme die
      Regge-Gleichungen gibt, gilt als bekannt [L?].
    - Neu hier sind nur die Zahlen und die Fensterprobe.
  - L5 (Messbezug): keiner.

## 5. Selbstanzeigen

1. **Zwei geschaetzte Zeiten im eingefrorenen Plan:**
   - "Hintergrund ... bis 02:31" und "Plantext ab 02:46:30" habe ich nicht mit date gemessen.
   - Gemessen sind 02:28:56 (Start), 02:37:33, 02:45:18 (vor dem Geometrie-Rauchlauf), 02:46:09 (nach der
     Konventionsprobe) und 02:48:23 (Einfrieren).
   - Der Plantext entstand zwischen 02:46:09 und 02:48:23. Ein Teil davon (Konventionen, Formen) stand schon vorher
     als Code fest.
   - Der Plan bleibt unveraendert.
2. **PO3 war vorab weitgehend ableitbar:**
   - Schon beim Festlegen von K1 hatte ich von Hand abgeschaetzt, dass der Schwerpunkt um die Mitte des geometrischen
     Bereichs liegt und x* im oberen Teil.
   - Der Geometrie-Rauchlauf (ohne 6j) gab dann die Huellkurvenschwerpunkte, und A4 stand mit 85 % im Plan.
   - K1 und K2 standen als Code-Konstanten fest, bevor die Geometrieprobe lief. Keine Konfiguration wurde nach einem
     Ergebnis ausgewaehlt oder verworfen.
   - **Aber [M]:** Das Urteil haengt an der Wahl.
     - Bei flachen Bipyramiden (kleine Scharnierwinkel phi1 + phi2) liegt x* unten im Bereich, bei hohen oben.
     - Dazwischen kann x* zufaellig nahe am Huellkurvenschwerpunkt liegen. Dort traefe der Betragsschwerpunkt das
       +-10-%-Band, ohne dass sich das Gewicht bei x* sammelt.
     - Belastbar ist darum nicht "28 bis 34 %", sondern: x_c folgt in allen sechs Faellen der Huellkurve
       (<= 3 %), nicht x*.
3. **PO1 hing an der Stichprobe:**
   - Form B lag mit -0,751 knapp im Band (Grenze -0,7). Ihr log-log-R^2 ist 0,66, weil e(lambda) oszilliert.
   - Mit anderen lambda-Werten haette dieselbe Rechnung das Band verfehlen koennen.
   - Die nachtraegliche obere Huelle (Abschnitt 3.1) ist nicht geurteilt.
   - Die Aussage e(100) < 0,02 hat dagegen einen Abstand von Faktor 30.
4. **auswertung.py nach dem Einfrieren geschrieben:**
   - entstanden, waehrend die Hauptlaeufe liefen, und vor dem Ansehen eines Ergebnisses um 02:50:32 gehasht;
   - Nachtrag in EINGEFROREN-SHA256.txt; seither unveraendert.
   - Die Regeln stehen im eingefrorenen Plan.
5. **Rauchlauf "trocken" fehlt im Plan:**
   - code/trocken.py lief vor dem Einfrieren (00:48:16 UTC), steht aber nicht in PLAN Abschnitt 7.
   - Er gab nur "durchgelaufen" aus: PO3-Codepfad bei K1 und lambda = 2, ein BE-Satz, drei sympy-Aufrufe; keine
     Pruefwerte.
6. **Was ich vor dem Einfrieren gesehen habe:**
   - die Geometrie aller Formen;
   - vier 6j-Werte am gleichseitigen Tetraeder samt PR-Abgleich, also die Konventionsprobe.
   - Der Zeitlauf hat drei 6j bei lambda = 200 gerechnet, aber nur Laufzeiten ausgegeben.
7. **Wahl der PO2-Form:**
   - Geurteilt wurde die stark nicht geometrische Form N (V^2/V_reg^2 = -1,14), beschreibend die schwaechere N_rand
     (-0,33).
   - Beide waren vor jeder 6j-Rechnung an ihnen festgelegt, und beide erfuellen R^2 > 0,99.
   - Noch naeher am Rand (Airy-Uebergang) habe ich nicht gerechnet.
8. **Ueber die Karte hinaus:**
   - x_fold, die PR-Aufteilung der rechten Seite in zwei Terme und die Fensterprobe sind meine Zusaetze.
   - Sie sind im Plan als beschreibend markiert und nicht geurteilt.
   - Die Stationaritaetsbedingung am gefalteten Punkt (phi_k = phi_i + phi_j) habe ich nur hergeleitet, nicht
     nachgerechnet [M].
9. **Quellen:**
   - Edmonds 6.2.12, Roberts 1999 und die PR-Konvention stammen aus dem Gedaechtnis [L].
   - Bestaetigt sind sie nur durch Rechnung: BE exakt; Konvention am gleichseitigen Tetraeder.
10. **Spuren:**
   - nur cpu, hoechstens ein Lauf zugleich;
   - 15 Starts (5 Rauch, 9 Haupt, 1 Auswertung), alle rc = 0;
   - laengster Lauf 197 s (K2, lambda = 200).
11. **Zeitbox:** Start 02:28:56, Text ab 02:58:08 CEST, innerhalb der 90 min.
12. **auswertung.json nachbearbeitet:**
    - Die Felder "vermerk" fuer PO0, PO1 und PO3 habe ich um 03:00:45 CEST per jq eingetragen.
    - Urteile, Werte und beschreibende Groessen sind gegen die Maschinenfassung lauf-69/auswertung.maschine.json
      (bitgleich mit der .69) per diff identisch.
    - Neben "urteile" enthaelt die Datei einen zweiten Schluessel "beschreibend" (nicht geurteilte Groessen).

## 6. Bedeutung (wie auf der Karte vorab festgelegt)

- **PO1 eingetroffen:**
  - In Finns Bild, Striche als Drehimpulse, steckt Regges Wirkung schon in der Quantenmechanik eines einzelnen
    Tetraeders.
  - Phase und Amplitude stimmen, die Nullstellen auf 0,002 Spin-Einheiten.
  - Einsteins Wirkung in 3D muss also nicht eingegeben werden; sie ist der klassische Grenzfall der Kopplung von
    Drehimpulsen [L, hier an zwei Formen nachgerechnet].
- **PO0:** Biedenharn-Elliott zeigt die Regel "Umbenennen ist frei" in 3D exakt, als Identitaet. Das gilt auch bei
  Spins bis 1800, auf 1e-49.
- **PO3 nicht eingetroffen:**
  - Nach der Karte ist das 2-3-Gewicht nicht geometrisch lokalisiert, und die einfache Lesart gilt nur fuer die
    Phase.
  - Die beschreibenden Groessen stuetzen genau das, mit einer Ergaenzung [E]: Die Phase sammelt sich an zwei
    geometrischen Stellen.
    - x*: Die drei Tetraeder schliessen flach um die innere Kante. Dort steht Regges Bewegungsgleichung (Defizit 0),
      aus Interferenz.
    - x_fold: die gefaltete Einbettung.
  - Jede Stelle traegt genau ihren PR-Term. Dazwischen loeschen sich die Summanden aus.
  - Die Bewegungsgleichung folgt also aus Interferenz, aber nicht eindeutig; die zweite, gefaltete Loesung gehoert
    dazu.
- **Grenze [L]:**
  - Das ist 3D-Schwerkraft ohne Wellen.
  - In 4D gilt Aehnliches nur naeherungsweise (Spinschaum-Modelle).
  - Wie in REGGE-4D-1 ist hier nichts aus Punkten und Strichen allein hergeleitet; die Regel steckt in der
    SU(2)-Kopplung.
- **Naechster Schritt [H]:**
  - Die Fensterprobe auf einen 1-4- oder 3-3-Zug uebertragen; dort gibt es mehrere innere Kanten.
  - Oder q-deformiert rechnen (Turaev-Viro), um zu sehen, ob die kosmologische Konstante als Volumenterm in der Phase
    erscheint [L?].

## 7. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-024823, EINGEFROREN-SHA256.txt
- code/:
  - ponzano.py: exakte 6j, Geometrie, Teile po0 bis po3
  - auswertung.py: Urteile und Bilder
  - beide mit Kopien *.eingefroren-*
  - umgebung.py, trocken.py: Rauch
- lauf-69/:
  - po0.json, po1.json, po2.json, po3-K{1,2}-{50,100,200}.json mit .log
  - auswertung.json (mit Vermerken), auswertung.maschine.json, auswertung.log, haupt-kette.log, PRUEFSUMMEN.txt
  - Bilder: bild-spinfolge.png, bild-fehler-loglog.png, bild-abfall.png, bild-pachner-K1.png, bild-pachner-K2.png
- rauch-69/: umgebung.log, geometrie.json, zeit.json, konvention.json
- Auf der .69: /home/fmh/fmhc-physics-remote/runde37-ponzano/ (code/, rauch/, lauf/)

## 8. Einfach gesagt

Wir haben auf jeden Strich eines Tetraeders eine Drehimpulszahl geschrieben und daraus mit reiner Quantenmechanik eine
einzige Zahl berechnet, das 6j-Symbol. Fuer grosse Zahlen schwingt sie genau so, wie es Regges Formel aus den
Strichlaengen und den Knickwinkeln an den Kanten vorhersagt (auf wenige Zehntausendstel genau), und wo die Striche zu
keinem echten Tetraeder passen, wird sie exponentiell winzig. Ersetzt man zwei Tetraeder auf einem gemeinsamen Dreieck
durch drei Tetraeder um einen neuen Strich, bleibt das Ergebnis exakt gleich; das Netz umzubauen kostet nichts. In der
Summe ueber die Laenge des neuen Strichs entsteht das Ergebnis an genau zwei Stellen: wo die drei Tetraeder flach
zusammenpassen und an einer zweiten, gefalteten Stelle; ueberall sonst heben sich die Beitraege auf. Die Karte fragte
aber nach dem Schwerpunkt der Beitragsgroessen, und der liegt rund 30 % unter der flachen Laenge, deshalb ist PO3 nicht
eingetroffen.
