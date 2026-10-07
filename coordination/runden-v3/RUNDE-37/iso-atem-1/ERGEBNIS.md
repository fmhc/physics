# ISO-ATEM-1: Ergebnis (Code-Agent fuer die Leitung, Runde 42)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 18:54:13 CEST. Literaturabrufe 17:03:30 und 17:04:06 UTC (2 von 2). Plan ab 19:06:30 CEST, vor
    jeder Rechnung.
  - Rauchlaeufe 17:12:04 bis 17:12:22 UTC (nur Laufzeit, Schluessel, K0 und Teil-A-Reste gelesen; PLAN Abschnitt 7).
  - Eingefroren 2026-10-04 19:12:48 CEST: PLAN.md.eingefroren-20261004-191248 und
    code/iso_atem.py.eingefroren-20261004-191248; Liste in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 17:12:57 bis 17:17:16 UTC (cpu8, cpu9), Auswertung und Bild 17:17:30 bis 17:17:33 UTC, alle rc = 0.
  - Nachtrag nach dem Einfrieren (beschreibend, [D]): Diagnose 17:17:54 bis 17:18:43 UTC (cpu8), verlaengerter Ast
    17:17:25 bis 17:22:06 UTC (cpu2). Text ab 19:23:03 CEST.
- Alle Zahlen sind Rechnungen am Modell starrer Tetraeder auf der .69, keine Messdaten.
- **Kennzeichen:** [E] gerechnet, [M] von Hand vorab (nicht gegengelesen), [S] an der Quelle gelesen, [L?] Gedaechtnis,
  unsicher, [F] Festlegung im Plan, [D] Diagnose nach dem Einfrieren, ohne Urteil, [H] Hypothese.
- **Begriffe:** lambda = Zellkante / Ideal-Zellkante (F = lambda I), V/V0 = lambda^3. A = "obere", B = "untere"
  Tetraeder. phi_A, phi_B = Drehwinkel um die eigene <111>-Achse. Kippwinkel phi_m = (phi_A + phi_B)/2 [F].
  O1 = geteilte Ecke auf der Drehachse (4 je Zelle), O2 = die anderen 12. "Si-O-Si" = Winkel Mitte-Ecke-Mitte.

## 1. Ergebnis zuerst

1. **Ja: Finns Netz kann in der Zelle mit 8 Tetraedern in alle Richtungen gleich atmen, ohne ein Tetraeder zu
   verformen [E].** Die P2_13-Drehung (jedes Tetraeder dreht um seine eigene <111>-Achse) ist eine stetige, exakte
   Schar ab der Ideallage. Bei lambda = 0,97 gilt phi_A = 15,63 Grad, phi_B = 18,74 Grad, Rest 5e-16. Das stand vorher
   fest: Meine Herleitung von Hand (lambda = (1 + cos phi_A + cos phi_B)/3 mit cos(phi_A + 60 Grad) + cos(phi_B - 60 Grad)
   = 1) stimmt auf 7e-16. In der Literatur habe ich sie mit 2 Abrufen nicht gefunden.
2. **Neu und nicht ableitbar (Teil C) [E]: Es gibt eine zweite isotrope Atemform.** Aus 600 Zufallsstarts je lambda
   finden sich nur zwei Arten von Loesungen: etwa 55 % P2_13 und etwa 45 % eine niedrigere Form (Punktgruppe 222, drei
   Ausrichtungen), bei der alle 8 Tetraeder um denselben Winkel kippen (17,25 Grad bei lambda = 0,97). Beide
   ueberlappen nicht und sind bei festem lambda isoliert. Je ein Vertreter laeuft stetig in die Ideallage zurueck [D].
   Deshalb ist IA3 nach Plan nur "teilweise" eingetroffen.
3. **Volumen gegen Kippwinkel [E]:** V/V0 folgt fast genau cos^2 phi_m, wie beim flachen Atmen um eine Achse (Teil A):
   0,970 bei 10 Grad, 0,749 bei 30 Grad, 0,394 bei 50 Grad. Der Winkel an den O2-Ecken faellt etwa linear (152,1 Grad
   bei lambda = 0,97); an den O1-Ecken bleibt er gerade (180 Grad).
4. **Beruehren:** Bis lambda = 0,60 (V/V0 = 0,22, phi_m = 58 Grad) beruehren sich keine Tetraeder [E]. Im
   verlaengerten Lauf [D] beruehren sich erst bei lambda = 0,500 (phi_m = 60,0 Grad, V/V0 = 0,125) Ecken nicht
   verbundener Tetraeder. Nicht verbundene Ecken kommen sich ab phi_m = 38,6 Grad (lambda = 0,846) naeher als eine
   Kante.
5. **Die kleinste Zelle kann es nicht [E = M]:** Im Gamma-Ansatz (alle A gleich, alle B gleich) bleibt bei F = lambda I
   ein Rest von genau (1 - lambda)/sqrt 2, also 0,0212 bei lambda = 0,97. Isotropes Atmen braucht Tetraeder, die um
   verschiedene Achsen drehen, also mindestens die vierfache Zelle.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 19:12:48 CEST) durch den Modus "auswertung" des eingefrorenen Codes;
lauf-69/auswertung.json.

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| IA1 | Kontrolle: Teil A exakt; der Gamma-Ansatz erreicht F = lambda I nie (Rest > 1e-3 bei lambda = 0,97) | 95 % | **eingetroffen** | **eingetroffen** | Teil A: r_max <= 6,7e-16 bei 1, 5, 10, 20, 30 Grad. Gamma, min r_rms aus 200 Starts: 0,00707 / 0,02121 / 0,03536 / 0,07071 bei lambda = 0,99 / 0,97 / 0,95 / 0,90, gleich (1 - lambda)/sqrt 2 auf 1e-15 |
| IA2 | [H] Fuer lambda = 0,97 gibt es eine Loesung mit Rest < 1e-10, also isotropes Atmen in der kubischen Zelle | 60 % | **eingetroffen** | **eingetroffen** | Ast ab phi = 0: 1075 Punkte, r_max <= 8,2e-16 an jedem Punkt, Schritt 0,002; exakt bei 0,97: r_max 5,0e-16. Teil C bei 0,97: 344 von 600 Starts mit r_max < 1e-10 (bestes 3,6e-16) |
| IA3 | [H] Die Loesung aus IA2 hat P2_13-Symmetrie (je Tetraeder eine eigene <111>-Achse) | 50 % | **teilweise** | **eingetroffen** | B bei 0,97: alle 12 Drehteile von T, drei 2_1-Schrauben, jedes Tetraeder auf einer eigenen Dreierachse (A: 4 verschiedene, B: 4 verschiedene). Teil C bei 0,97: 189 von 344 Loesungen P2_13, 155 nicht (Punktgruppe 222) |

- **Alle drei Urteile nach Kartenwortlaut waren vorab ableitbar [M]** (PLAN Abschnitt 2). IA1 folgt aus F = (R_A +
  R_B)/2 und der Polarzerlegung; IA2 und IA3 aus der Handformel der P2_13-Schar. Die Literatur (Schritt 0) belegt sie
  nicht: zwei Abrufe, nur Abstracts, kein Satz "P2_13 = Schar starrer Tetraeder". Gemessen im engeren Sinn sind Teil C
  (zweite Atemform), Beruehrung, Si-O-Si-Winkel und Nullitaeten.
- **IA3 nach Kartenwortlaut** ist fuer die B-Loesung durch den Ansatz vorgegeben. Der Symmetrietest ist unabhaengig
  gebaut und hat sie bestaetigt; inhaltlich traegt nur das Urteil nach Plan.
- **Bedeutung, wie auf der Karte vorab festgelegt:** "IA2 trifft ein" ist ausgeloest. Finns Netz hat einen
  Gleichtakt-Atemkanal ohne Energie (im Modell starrer Tetraeder exakt null), der in alle Richtungen gleich wirkt. Das
  ist der Anschluss an ATEM-NETZ-1 (Volumenatmen). Genauer als die Karte: Es sind zwei Kanaele (P2_13 und die 222-Form),
  und keiner existiert in der kleinsten Zelle.

## 3. Volumen gegen Kippwinkel (Teil B, Ast phi > 0; lauf-69/ast.json)

Bild: **lauf-69/iso-atem-1.png** (links V/V0 gegen |phi_m| mit Spiegelast und Teil A; rechts Si-O-Si an O1 und O2).

| phi_m (Grad) | phi_A | phi_B | lambda | V/V0 | Teil A cos^2 phi (gleiches phi) | Si-O-Si an O2 (Grad) | Quelle |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 1 | 180 | Ideallage |
| 5,01 | 4,88 | 5,14 | 0,99745 | 0,99237 | 0,99240 (5 Grad) | 171,82 | Astpunkt |
| 9,92 | 9,42 | 10,43 | 0,99 | 0,97030 | | 163,82 | exakt |
| 10,02 | 9,50 | 10,53 | 0,98981 | 0,96975 | 0,96985 (10 Grad) | 163,67 | Astpunkt |
| 15,07 | 13,88 | 16,25 | 0,97694 | 0,93241 | | 155,49 | Astpunkt |
| **17,19** | **15,63** | **18,74** | **0,97** | **0,91267** | | **152,08** | exakt |
| 20,06 | 17,90 | 22,22 | 0,95910 | 0,88225 | 0,88302 (20 Grad) | 147,47 | Astpunkt |
| 22,18 | 19,50 | 24,86 | 0,95 | 0,85738 | | 144,09 | exakt |
| 25,04 | 21,55 | 28,54 | 0,93621 | 0,82058 | | 139,56 | Astpunkt |
| 30,03 | 24,75 | 35,30 | 0,90809 | 0,74884 | 0,75000 (30 Grad) | 131,76 | Astpunkt |
| 31,31 | 25,49 | 37,12 | 0,90 | 0,72900 | | 129,78 | exakt |
| 35,01 | 27,39 | 42,63 | 0,87454 | 0,66887 | | 124,10 | Astpunkt |
| 40,01 | 29,26 | 50,76 | 0,83502 | 0,58222 | | 116,57 | Astpunkt |
| 45,04 | 30,00 | 60,08 | 0,78825 | 0,48978 | | 109,09 | Astpunkt |
| 50,00 | 28,93 | 71,08 | 0,73317 | 0,39410 | | 101,60 | Astpunkt |
| 55,01 | 24,33 | 85,69 | 0,66213 | 0,29029 | | 93,00 | Astpunkt |
| 58,05 | 17,15 | 98,96 | 0,59994 | 0,21594 | | 85,29 | Planende (lambda < 0,6) |
| 60,00 | -0,03 | 120,03 | 0,49984 | 0,12488 | | 70,50 | Nachtrag [D]: erste Beruehrung |

- Die Werte sind ausgewaehlte Astpunkte (der erste mit phi_m >= Zielwert), nicht interpoliert. Teil A ist nur bei den
  fuenf gerechneten Winkeln eingetragen.
- **Si-O-Si:** O1-Ecken bleiben bei 180 Grad (auf der Achse; kleinster Wert 179,9999985 Grad, Rundung des arccos nahe
  180 Grad), alle 12 O2-Ecken haben denselben Winkel (Streuung ueber den Ast hoechstens 1,2e-6 Grad, aus derselben
  Rundung; bei lambda = 0,97 5e-14 Grad).
- **Spiegelast** (phi < 0): dieselben lambda, Winkel mit vertauschten Rollen (phi_A, phi_B) -> (-phi_B, -phi_A); 1003
  Punkte, r_max <= 8,5e-16.
- **Form der Schar [E, bestaetigt M]:** phi_A steigt bis 30 Grad (bei phi_B = 60 Grad, lambda = 0,788) und faellt dann
  wieder; phi_B laeuft weiter. Bei (phi_A, phi_B) = (0, 120 Grad) sind alle Tetraeder wieder in Ideal-Orientierung, aber
  die Zelle ist halb so gross (lambda = 1/2) und nicht verbundene Ecken fallen zusammen.
- **Beruehrung [F, D]:** Bis lambda = 0,60 kein Paar mit Trennabstand <= 0 (kleinster Wert: 0,0137 an verbundenen
  Paaren, Kegeltest; 0,196 an nicht verbundenen Paaren). Im verlaengerten Lauf (lambda bis 0,3, eingefrorener Code, nur
  anderer Parameter) liegt der erste Punkt mit Trennabstand <= 0 bei lambda = 0,49984, phi_m = 60,0 Grad, kleinster
  Eckabstand nicht verbundener Tetraeder 0,0005 PU: Ecke trifft Ecke. Danach ueberlappen sie (456 bzw. 500 Astpunkte bis
  lambda = 0,3).
- **Nicht verbundene Ecken naeher als eine Kante (1 PU)** ab phi_m = 38,6 Grad, lambda = 0,846, Si-O-Si 118,6 Grad
  (eigene Auswahl aus ast.json, siehe Selbstanzeige 3).

## 4. Teil C: isotrope Loesungen ohne Symmetrieansatz (lauf-69/zufall-1.json, zufall-2.json; Klassen in nachtrag-69/diag-c.json)

| lambda | Starts | Loesung (r_max < 1e-10) | davon P2_13 | davon nicht P2_13 (4 Drehteile) | keine (r_max >= 1e-6) | fast | ohne Ueberlappung | Nullitaet bei festem lambda |
|---|---|---|---|---|---|---|---|---|
| 0,99 | 600 | 353 | 188 | 165 | 247 | 0 | 353 | 0 (alle) |
| 0,97 | 600 | 344 | 189 | 155 | 256 | 0 | 344 | 0 (alle) |
| 0,95 | 600 | 344 | 186 | 158 | 256 | 0 | 344 | 0 (alle) |
| 0,90 | 600 | 300 | 164 | 136 | 300 | 0 | 300 | 0 (alle) |

- Je Startart (300 "nah", 300 "weit") finden sich Loesungen in aehnlicher Zahl (bei 0,97: 163 nah, 181 weit).
- **Klassen bei lambda = 0,97 und 0,99 [D]** (gleiche Symmetrie und gleiche Drehwinkel-Liste):
  - P2_13: Drehwinkel 4 x 15,6271 und 4 x 18,7438 Grad (bei 0,99: 4 x 9,4200, 4 x 10,4275), genau die Teil-B-Loesung.
  - 222-Form in drei Ausrichtungen (64 / 49 / 42 bei 0,97; 59 / 55 / 51 bei 0,99): Drehteile E, eine 2_1-Schraube um eine
    Wuerfelachse und zwei Zweier um die dazu senkrechten Flaechendiagonalen, mit Verschiebung 1/4 der Diagonale laengs
    der Achse. Alle 8 Tetraeder sind um denselben Winkel gedreht: 17,2539 Grad (0,97), 9,9364 Grad (0,99).
  - Aus der Viertel-Verschiebung folgt [M], dass die 222-Form zusaetzlich um eine halbe Flaechendiagonale verschiebbar
    ist, also eine halb so grosse Zelle hat wie die kubische. Das passt zur Zelle von alpha-Cristobalit (P4_12_12) bzw.
    zu den P2_12_12_1-Familien bei Coh/Vanderbilt [H, Zuordnung nicht geprueft].
- **Fortsetzung in lambda [D]** (je ein Vertreter, LM von lambda zu lambda):
  - P2_13: von 0,97 bis 1,0 zurueck in die Ideallage (groesste Drehung 1,5e-5 Grad, Mitten 1,5e-7 PU); abwaerts bis 0,70
    ohne Ueberlappung; Rest <= 9e-14; Nullitaet 0 bei festem lambda, 1 mit freiem lambda.
  - 222-Form: ebenso zurueck in die Ideallage (3,1e-5 Grad, 3,8e-7 PU); abwaerts bis 0,70 ohne Ueberlappung, Drehwinkel
    dort 56,6 Grad; Rest <= 1e-13; Nullitaet 0 bzw. 1.
  - Bei lambda = 1 (Restdrehung um 1e-5 Grad) haengt die Nullitaet an der Schwelle (P2_13: 0 bzw. 4; 222: 2 bzw. 2);
    dort ist der Punkt entartet, die Zahl ist nicht belastbar.
- Folge [E, D]: In der Zelle mit 8 Tetraedern gibt es (bei 600 Starts je lambda) genau zwei Arten isotroper
  Atem-Mechanismen, jeweils eine Kurve durch die Ideallage (je ein Vertreter fortgesetzt). Die Klassen habe ich bei
  0,99 und 0,97 bestimmt; bei 0,95 und 0,90 nur die Zahl der Drehteile (4 oder 12). Weitere Arten sind nicht
  aufgetaucht, das ist aber kein Beweis.

## 5. Kontrollen und Latten

- **K0:** Ideallage r_max 3,9e-16; P2_13-Tabelle bildet die Ideallage auf sich ab (24 von 24 Drehteilen aus O).
- **K_M (Handformel):** Abweichung von lambda = (1 + cos phi_A + cos phi_B)/3 hoechstens 3,3e-16, von cos(phi_A + 60) +
  cos(phi_B - 60) = 1 hoechstens 6,7e-16, ueber alle Astpunkte (auch im verlaengerten Lauf, 4,4e-16).
- **Ansatz gegen Vollsystem:** Teil B prueft alle 48 Eckkomponenten, nicht nur die 4 reduzierten Gleichungen; die
  Jacobi-Matrix am Start hat Rang 4 (Singulaerwerte 7,66 / 4,28 / 2,77 / 1,83 / 1,6e-10).
- **Beruehrtest-Probe [D]:** Zwei verschobene Tetraeder: Trennabstand -0,61 / -0,41 / -0,11 / +0,79 bei 0,1 / 0,3 / 0,6
  / 1,5 PU Versatz. Zwei Tetraeder mit gemeinsamer Ecke, um die Ecke gedreht: -0,66 / -0,36 / +0,005 / +0,029 / +0,082
  bei 5 / 30 / 60 / 90 / 180 Grad Mitte-Ecke-Mitte. Der Test erkennt Ueberlappung in beiden Faellen.
- **Latten:**
  - L1 (kann scheitern): IA1 bis IA3 nach Wortlaut konnten nach meiner Handrechnung kaum scheitern. Teil C konnte in
    beide Richtungen ausgehen (nur P2_13 oder mehr) und ist mit "mehr" ausgegangen.
  - L2 (Gegenprobe): zwei unabhaengige Wege zur selben Loesung (Ansatz B und freie Suche C, gleiche Winkel auf 1e-4
    Grad); Handformel gegen Rechnung; Spiegelast.
  - L3 (Numerik): alle Reste <= 1e-13, Abstand zur Schwelle 1e-10 mindestens drei Stellen; "keine" liegen >= 1e-6.
  - L4 (bekannt): P2_13-Modell von beta-Cristobalit [L?, nicht an der Quelle]; Gamma-Mode nur tetragonal (Dossier SP8).
    Neu fuer das Projekt: die geschlossene Formel, die zweite (222-)Atemform, Beruehrpunkt lambda = 1/2.
  - L5 (Messbezug): beta-Cristobalit hat gemessen eine kleinere Zelle als die Idealform mit geraden Bindungen [L?]; hier
    nicht geprueft. Im Modell liegt lambda = 0,96 zwischen den Si-O-Si-Winkeln 152 Grad (0,97) und 144 Grad (0,95).

## 6. Selbstanzeigen

1. **Lokale Werkzeuge ausserhalb der Liste (keine Rechnung):** ls, cat, wc -l (Lesen, Zaehlen von Zeilen), mkdir, cd,
   einmal `cat >>` mit Heredoc (Nachtrag im Plan) und scp fuer lokale Kopien (Einfrieren). date wie verlangt.
2. **Rauchlauf:** Laut Plan wollte ich nur Laufzeit, Schluessel und K0 lesen; ich habe zusaetzlich die fuenf Teil-A-Reste
   gesehen (Kontrolle, vorab ableitbar) und im Nachtrag des Plans vermerkt.
3. **Fehler in einer beschreibenden Groesse (d_OO):** Der eingefrorene Code zaehlt Paare "Ecke eines Tetraeders und
   geteilte Ecke des Nachbarn" mit; das ist eine Kante (1 PU). d_OO ist dadurch min(1, wahrer Wert). Die eingefrorene
   Auswertung meldet "d_OO < 1" schon bei phi = 0 (0,9999999999999996 < 1, Rundung). Ich habe die Stelle stattdessen per
   jq mit Schwelle 0,999999 gesucht (phi_m = 38,6 Grad). Kein Urteil haengt daran.
4. **Nach dem Einfrieren [D]:** (a) code/diag_c.py (neu, importiert den eingefrorenen Code unveraendert): Klassen, Probe
   des Beruehrtests, Fortsetzung in lambda. Erster Versuch scheiterte am Import der Datei ohne .py-Endung
   (nachtrag-69/diag-fehlversuch1.log); der zweite importierte code/iso_atem.py mit gleichem sha256. (b) Verlaengerter Ast
   mit lam_stop 0,3 statt 0,6 (Plan), um den Beruehrwinkel zu finden. Beides ohne Urteil.
5. **Spur cpu2** fuer den verlaengerten Ast (cpu8 und cpu9 waren belegt); laut Auftrag erlaubt. Freie Spuren habe ich
   mit `flock -n` auf den Lock-Dateien geprueft; das nimmt den Lock fuer einen Augenblick.
6. **Literatur:** 2 von 2 Abrufen, beide nur Abstracts (arXiv-API). Borcea/Streinu 2011 ("Deformations of crystal
   frameworks", Quarz und Cristobalit) koennte die Schar enthalten; Volltext nicht gelesen. O'Keeffe/Hyde 1976 und Barth
   1932 nur [L?].
7. **Handrechnung nicht gegengelesen:** Die P2_13-Formel und die Gamma-Untergrenze sind nur von mir hergeleitet; die
   Rechnung bestaetigt sie, eine zweite Person hat sie nicht geprueft.
8. **Festlegungen mit Gewicht [F]:** Kippwinkel = Mittel (phi_A + phi_B)/2; Rest-Lesarten r_max fuer "<", r_rms fuer
   ">"; P2_13-Test nur ueber Drehteile (keine Spiegel); Startverteilungen und -zahlen in Teil C; Beruehrung ueber
   Trennachsen und einen um 5 % gekappten Kegel an der gemeinsamen Ecke.
9. **Kosmetik im Diagnosecode:** Die Laengskomponente fuer Diagonalachsen ist modulo 1 statt modulo sqrt 2 genommen;
   die Aussage "Viertel der Diagonale" stuetzt sich auf das Doppelte der Verschiebung und gilt unabhaengig davon.
10. **Zeitbox:** Start 18:54:13, Text ab 19:23:03 CEST, Abgabe 2026-10-04 19:25:41 CEST (date, beim Schreiben dieser Zeile gemessen), also innerhalb der 75 min.

## 7. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-191248, EINGEFROREN-SHA256.txt.
- code/iso_atem.py (+ .eingefroren-20261004-191248): Modi kontrolle, ast, zufall, auswertung, bild. code/diag_c.py
  (Nachtrag).
- quellen/: A1-api-cristobalit-p213.xml, A2-api-cristobalit-alle.xml, Kopfzeilen, Abrufzeiten, SHA256SUMS.
- lauf-69/: kontrolle.json, ast.json, zufall-1.json, zufall-2.json, auswertung.json, bild.json, iso-atem-1.png, Logs,
  PRUEFSUMMEN.txt (lokal = .69).
- rauch-69/: Rauchlaeufe. nachtrag-69/: diag-c.json, ast-weit.json, Logs, REMOTE-SHA256.txt.
- .69: /home/fmh/fmhc-physics-remote/iso-atem-1/ (code/, quellen/, rauch/, lauf/, nachtrag/).

## 8. Einfach gesagt

Finns Netz aus Tetraedern, die sich nur an den Ecken beruehren, kann als Ganzes in alle Richtungen gleich schrumpfen
und wieder wachsen, ohne dass ein Tetraeder sich verbiegt. Dafuer muss sich jedes Tetraeder ein wenig um seine eigene
Achse drehen, und die Nachbarn drehen um verschiedene Achsen; mit nur zwei Sorten von Tetraedern, die alle gleich
drehen, geht es nicht. Bei 17 Grad Drehung ist das Volumen um knapp 9 Prozent kleiner, bei 50 Grad um 60 Prozent, und
erst bei einem Achtel des Volumens stossen Tetraeder aneinander. Ueberraschend gibt es zwei verschiedene Arten, so zu
atmen; die eine stand vorher schon fest, die zweite haben wir erst durch die Suche gefunden.
