# GUERTEL-FELD-STAB-1: Ergebnis (Runde 42; Sattel oder Rast?)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 19:00:04 CEST. Code 19:07 bis 19:10 CEST; Plantext ab 19:11:11 CEST.
  - Rauchlauf 17:10:44 bis 17:11:08 UTC: fuenf Units, Spur cpu3, alle rc = 0.
  - Eingefroren 19:13:21 CEST (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe 17:13:32 bis 17:17:57 UTC: 12 Units, alle rc = 0, keiner wiederholt. Das sind Protokoll, sechs
    Stoesse, zwei Kontrollen, zwei Referenzen und die Auswertung.
  - Text ab 19:19:15 CEST.
- **Kennzeichen:**
  - [M] Mathematik; [E] Rechnung im Modell (synthetisch, keine Messdaten); [L] Literatur oder Gedaechtnis;
    [H] Hypothese; [R] im Rauchlauf gesehen.
- **Art:** synthetische Modellrechnung an einem Modellfeld (SO(3)-Orientierungsfeld auf Z^3), keine
  Messdatenbestaetigung.

## Ergebnis zuerst

1. **Auf dem Gitter (12, 24) ist der Vorwaertsast jenseits von 360 Grad ein Sattel, keine Rast [E].**
   - Alle sechs Stoesse (420 und 450 Grad; eps = 0,01, 0,1, 0,3) fuehren ohne Gittersprung in die umgekehrte
     Verdrillung.
   - E faellt von 14642 auf 7584,65 = E(300) bzw. von 16722 auf 6161,06 = E(270), jeweils auf 2e-10 relativ.
   - **GS1 ist nach Plan und nach Wortlaut eingetroffen.**
2. **Der Abstieg ist glatt [E].**
   - Die Sonde min q_a . q_b bleibt in jedem Lauf bei 0,466 oder hoeher; ein Sprung waere erst bei 0. Waehrend des
     Abstiegs steigt sie auf 0,83 bzw. 0,87.
   - Die Energie steigt nie ueber ihren Startwert: Auf diesem Weg gibt es keine Huerde.
   - Alle Laeufe konvergieren nach 292 bis 424 FIRE-Schritten (fmax < 1e-5).
3. **Ohne Stoss zerfaellt der Ast genauso, nur spaeter [E]** (Kontrolle; Zusatz, nicht urteilsbildend):
   - Ausgeloest nur durch das Protokollrauschen: bei 450 Grad nach 384, bei 420 Grad nach 594 Schritten, wieder ohne
     Sprung und in die umgekehrte Verdrillung.
   - Die Kipp-Amplitude waechst dabei exponentiell, etwa 0,055 bzw. 0,043 je Schritt. Der Stoss beschleunigt nur.
   - Damit ist die offene Frage aus GUERTEL-2 (N1) beantwortet: Der Ast ist nicht metastabil, er zerfaellt langsam.
     Lesart [H]: Mit 30 bzw. 150 FIRE-Schritten je Winkel lief das Protokoll dem Zerfall davon,
     bis bei 540 Grad der Gittersprung kam.
4. **GS0 ist eingetroffen [E]:** Das Protokoll trifft N1 bei 420 und 450 Grad bitgleich (Abweichung 0,0).
5. **Bedeutung, wie in der Karte vorab [H]:**
   - Das Feld um einen drehenden Kern legt 720 Grad Verdrillung stetig ab (450 -> -270 Grad, 420 -> -300 Grad), ohne
     Gittersprung. Das ist der Guertel-Trick im Feld, die Grundlage fuer den halben Spin (Luecke L4).
   - Gezeigt ist das nur fuer SO(3) auf einem 3D-Gitter, quasistatisch (FIRE), auf einem einzigen Gitter. In der
     Ebene der Werte (SO(2)) gibt es den Trick nicht [M].

## Urteile (lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Wortlaut | tragende Werte |
|---|---|---|---|---|---|
| GS0 | Kontrolle: Vorwaertsast bei 420 und 450 Grad aus GUERTEL-2 (N1) reproduziert (Energie auf 1e-6 relativ) | 85 % | **eingetroffen** | **eingetroffen** | E_schritt(420) = 14642,446583942661, E_schritt(450) = 16725,58389579176, E_gitter(450) = 16722,374712425655; Abweichung zu N1 je 0,0; Sonde 0,612 / 0,521 / 0,489 (> 0) |
| GS1 | [M Kontinuum, H Gitter] Der Ast ist ein Sattel: Der Stoss fuehrt ohne Gittersprung in die umgekehrte Verdrillung (E faellt auf etwa E(720 - theta)) | 50 % | **eingetroffen** (6 von 6 "umgekehrt") | **eingetroffen** (6 von 6 "umgekehrt") | rho zwischen -7e-11 und 2e-10 (Grenze 0,10); E_end/E_ref = 1 auf 2e-10 (Wortlaut-Band 10 %); Sonde im Lauf >= 0,466; mittleres q_z aussen am Ende -0,393 (450) bzw. -0,427 (420), vorher +0,553 bzw. +0,540 |

- Plan und Wortlaut stimmen ueberall ueberein. Die Werte liegen weit von allen Schwellen; deren Wahl entscheidet hier
  nichts.
- E_ref stammt aus den Referenzlaeufen: E(300) = 7584,6486 (vom Protokollwert 7585,2077 aus in 118 Schritten
  nachrelaxiert) und E(270) = 6161,0577 (schon konvergiert, 0 Schritte). Beide sind gueltig (Sonde 0,832 bzw. 0,869).

## Laeufe je Stoss [E]

| theta | eps | E vor | E nach Stoss | E Ende | Sonde min | Schritte | halb | P_0 | P_max (Schritt) | q_z aussen Ende | Klasse Plan / Wortlaut |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 420 | 0,01 | 14642,45 | 14642,82 | 7584,6486 | 0,595 | 387 | 219 | 0,42 | 146,2 (220) | -0,427 | umgekehrt / umgekehrt |
| 420 | 0,1 | 14642,45 | 14680,03 | 7584,6486 | 0,593 | 332 | 166 | 4,24 | 145,6 (167) | -0,427 | umgekehrt / umgekehrt |
| 420 | 0,3 | 14642,45 | 14978,38 | 7584,6486 | 0,589 | 354 | 148 | 12,6 | 144,9 (149) | -0,427 | umgekehrt / umgekehrt |
| 420 | 0 (Kontrolle) | 14642,45 | 14642,45 | 7584,6486 | 0,595 | 594 | 365 | 0,025 | 146,3 (365) | -0,427 | umgekehrt / umgekehrt (beschreibend) |
| 450 | 0,01 | 16722,37 | 16722,75 | 6161,0577 | 0,489 | 424 | 200 | 0,40 | 139,6 (201) | -0,393 | umgekehrt / umgekehrt |
| 450 | 0,1 | 16722,37 | 16759,31 | 6161,0577 | 0,486 | 320 | 138 | 4,25 | 143,5 (139) | -0,393 | umgekehrt / umgekehrt |
| 450 | 0,3 | 16722,37 | 17052,10 | 6161,0577 | 0,466 | 292 | 117 | 12,7 | 143,1 (118) | -0,393 | umgekehrt / umgekehrt |
| 450 | 0 (Kontrolle) | 16722,37 | 16722,37 | 6161,0577 | 0,489 | 384 | 173 | 0,145 | 141,8 (174) | -0,393 | umgekehrt / umgekehrt (beschreibend) |

- **Spalten:**
  - "halb" = erster Schritt mit E < (E_vor + E_ref)/2.
  - P = Kipp-Amplitude, also der Feldanteil ausserhalb der (1, z)-Ebene. Am Ende ist P in allen Laeufen < 0,006.
  - Sonde min = Minimum ueber den ganzen Lauf, einschliesslich des Zustands direkt nach dem Stoss.
- **Endzustand:** Er ist das Spiegelbild (q -> q quer) der Referenz.
  - Mittleres q_z aussen: -0,393 gegen +0,393 (450/270) und -0,427 gegen +0,427 (420/300).
  - min q0 bei 450: -0,5782 wie im Protokollzustand bei 270 Grad.
  - Das ist die umgekehrte Verdrillung -270 bzw. -300 Grad; der Kern bleibt dabei bei q_z(theta) = q_z(theta - 720).
- **Stosskosten:** E_nach - E_vor = 0,38 / 37 / 330 bis 336 fuer eps = 0,01 / 0,1 / 0,3. Das waechst wie eps^2, wie
  fuer eine kleine Kippung zu erwarten [M].
- **Zerfall:** Je groesser eps, desto frueher der Abstieg: "halb" bei 450 Grad 200 / 138 / 117, bei 420 Grad
  219 / 166 / 148.
- **Kontrolle 450:** Sie faellt frueher (173) als eps = 0,01 (200), obwohl ihr P_0 kleiner ist. Ihr Rauschen ist in
  der Protokollstrecke von 420 bis 450 Grad (drei Schritte und 150 Gitter-Schritte) gewachsen: P stieg von 0,025
  (420) auf 0,145 (450). Vermutlich liegt es dadurch schon weitgehend in der instabilen Richtung [H].
- **Beschreibende Zusatzwerte** (lokal mit jq aus den Verlaufsdaten, nicht in der eingefrorenen Auswertung):
  - Wachstumsrate von P zwischen P = 1 und P = 10: 0,043 je Schritt (420, Kontrolle und eps 0,01) und 0,054 bis 0,055
    (450). Die Reihenfolge (bei 450 instabiler als bei 420) passt zum Kontinuum [M]; einen Zahlenvergleich ziehe ich
    nicht, weil FIRE keine reine Gradientenstroemung ist.
  - Groesster Energieanstieg zwischen zwei Schritten 1,46 (FIRE-Traegheit), gegen einen Abfall um etwa 10.000.

## Bild

**lauf-69/energie-verlauf.png** (eingefrorener Auswertecode):

- Zeilen: E, Sonde und Kipp-Amplitude P (logarithmisch) ueber die FIRE-Schritte nach dem Stoss.
- Spalten: 420 und 450 Grad. Grau ist der Lauf ohne Stoss; gestrichelt E(720 - theta), gepunktet der Ast.
- **E** bleibt erst auf dem Ast und faellt dann in etwa 50 Schritten auf E(720 - theta).
- **Die Sonde** steigt beim Abfall von 0,49 bzw. 0,60 auf 0,87 bzw. 0,83 und kommt nie in die Naehe von 0.
- **P** waechst bis zum Abfall auf einer Geraden, also exponentiell. Das ist die instabile Richtung des Sattels. Am
  Abfall erreicht P etwa 140 (das Feld schwingt aus der z-Ebene heraus) und klingt dann ab.

## Kontrollen

1. **GS0:** Das Protokoll ist bitgleich zu N1 (gleicher Code, gleiche Saat; Zufallsfolge bis 450 Grad identisch).
2. **Codehashes:** Alle zehn FIRE-Laeufe und das Protokoll tragen code_sha256 b7093e59... (stab.py, eingefroren),
   g2 c9374a98... und g1 795f474d.... auswertung.json traegt 5cc0215c... (eingefroren).
3. **Pruefsummen:** 43 von 43 Laufdateien und 17 von 17 Rauchlaufdateien haben auf beiden Rechnern dieselbe sha256
   (lauf-69/ und rauch-69/PRUEFSUMMEN-69-roh.txt, lokal mit sha256sum -c geprueft).
4. **Der Stoss wirkt wie geplant:**
   - 9924 freie Plaetze der inneren Haelfte.
   - Groesster Kippwinkel 0,0099964 / 0,099964 / 0,29989 (das Sinusprofil erreicht auf dem Gitter 0,9996 eps).
   - Kern, Rand und aeussere Haelfte bleiben.
   - Die Sonde direkt nach dem Stoss ist > 0 (>= 0,467).
5. **Referenzen:** gueltig, Vorwaertsdrehsinn (q_z aussen +0,427 / +0,393), konvergiert.
6. **Laufzeiten:**
   - Protokoll 140,9 s; Stoesse und Kontrollen 16,7 bis 34,7 s; Referenzen 7,9 s und 0,2 s.
   - Alle weit unter 10 min. Die Schaetzung im Plan (3 min je Lauf) galt fuer volle 3000 Schritte; alle Laeufe
     konvergierten frueher.

## Ableitbarkeit

- **Vorab ableitbar, nur Konsistenz [M]:**
  - Im Kontinuum ist der Ast fuer theta > 360 Grad ein Sattel (konjugierter Punkt, Jacobi-Eigenwert -0,27 bzw. -0,36).
  - Der Endwert E(720 - theta) folgt exakt aus der Symmetrie q -> q quer, auch auf dem Gitter, sofern kein Sprung
    passiert. Dass E_end auf 2e-10 mit E_ref uebereinstimmt, ist deshalb eine Kontrolle, keine Messung.
  - Ebenso die Reihenfolge der Instabilitaet (450 vor 420).
- **Gemessen, nicht ableitbar [E]:**
  - Auf (12, 24) ist der Ast nicht gittergestuetzt (keine Rast), und die Relaxation nimmt den stetigen Weg statt des
    Gittersprungs.
  - Zeitskalen: 117 bis 424 Schritte mit Stoss, 384 bzw. 594 ohne.
  - Kleinste Sonde 0,466. Mit q_a . q_b = cos(omega/2) entspricht das einer groessten Bindungsdrehung von etwa
    2,17 rad, nahe den 2,1 rad aus der Ableitbarkeitsprobe der Karte und unter pi.
- **Ableitbarkeitsprobe der Karte** ("auf dem Gitter nicht ableitbar, weil 2,1 rad"): bestaetigt in dem Sinn, dass
  erst die Rechnung zeigt, dass das Gitter hier wie das Kontinuum reagiert.

## Dimensionen (AGENTS.md)

- **Innere Symmetrie:**
  - SO(3), gerechnet [E]: Der Ast zerfaellt stetig in die um 720 Grad kleinere Verdrillung (pi_1(SO(3)) = Z_2).
  - SO(2), nicht gerechnet: Es gibt keine Kipprichtung, und die Windung ist durch pi_1(SO(2)) = Z geschuetzt. Die
    Frage ist dort leer [M]. GUERTEL-2 (GZ4) [E] zeigte das Anwachsen um etwa k^2.
- **Raum:**
  - Gerechnet ist nur das Z^3-Kugelgitter (12, 24).
  - Die Sattel-Aussage des Kontinuums gilt fuer radiale Profile in d = 1, 2, 3 [M].
  - Das Gitterergebnis gilt nur fuer dieses Gitter. Auf (6, 24) sprang das Feld in GUERTEL-2 bei 450 Grad waehrend der
    Relaxation [E, GUERTEL-2]. Die Glaette entscheidet also mit, und die Grenze zwischen 6 und 12 ist nicht bestimmt.
  - Nicht auf 1D oder 2D uebertragen.
- **Richtungen:** Gestossen wurde nur eine Kipprichtung (nach x). Fuer "Sattel" genuegt eine instabile Richtung.
  "Rast" ist auf diesem Gitter widerlegt, weil der Ast auch ohne gezielten Stoss zerfaellt.
- **Offen:** der 720-Grad-Zustand selbst (das Protokoll springt vorher, bei 540 Grad); echte Zeitdynamik statt FIRE.

## Selbstanzeigen

1. **Reihenfolge:**
   - Den Code (19:07 bis 19:10 CEST) habe ich vor dem Plantext (ab 19:11:11) geschrieben, beides vor jedem
     Hauptlauf.
   - Die Rauchlauf-Kette habe ich um 19:11:08 CEST gestartet (Unit-Start 17:10:44 UTC), also kurz vor Beginn des
     Plantexts. Gesehen habe ich dabei nur Codepfad, Laufzeit und Werte bei 10 und 20 Grad, nichts bei 270 bis 450.
2. **Widerspruch im Plan:**
   - Die Referenzlaeufe stehen in Abschnitt 2 unter "Zusatz ... nicht urteilsbildend". Die Urteilsregeln in Abschnitt
     4 verwenden aber E_ref aus genau diesen Laeufen. Sie sind also urteilsbildend.
   - Ohne Nachrelaxation (Protokollwerte 7585,21 bzw. 6161,06) laege rho bei etwa 1e-4. Am Urteil aendert das nichts.
3. **Kippprofil:**
   - Die Karte sagt "um eps gekippt". Ich habe ein Sinusprofil festgelegt: groesster Winkel eps, 0 an Naht und Kern.
   - Ein gleichfoermiges Kippen der ganzen inneren Haelfte (Bruch am Kern) habe ich nicht gerechnet. Begruendung im
     Plan, vor dem Einfrieren.
4. **N1-Werte vor dem Einfrieren gelesen:** E und Sonde bei 270, 300, 420 und 450 Grad sowie fmax(450), per jq aus
   der GUERTEL-2-Datei. Das sind die GS0-Bezugswerte; sie waren in GUERTEL-2 schon veroeffentlicht.
5. **Lokale Rechnung mit jq:**
   - "halb", Wachstumsraten von P, Monotonie und groesster Anstieg habe ich lokal per jq aus den Laufdateien gerechnet.
     Das ist beschreibend und nicht in der eingefrorenen Auswertung.
   - Kopfrechnung sind die Umrechnung 0,466 -> 2,17 rad und die Schaetzung "rho etwa 1e-4" in Selbstanzeige 2.
   - Die Vorgabe "lokal keine Rechnung" lege ich damit weit aus.
6. **Feldname:** "start_utc" im Kopf der Laufdateien wird beim Schreiben gesetzt, also am Laufende (Muster aus
   GUERTEL-2). Die echten Startzeiten stehen in den Logs.
7. **Werkzeuge:**
   - Lokal ausserhalb der Liste: date, ls, cat, head, cut, mkdir, cp, echo; dazu sort, comm und eine Shell-Schleife im
     Monitor. Kein lokaler Interpreter (kein python, awk, perl).
   - Auf der .69 ausserhalb des Starters:
     - lesend: ls, cat, grep, sed, cut, wc, uptime, nproc, systemctl --user list-units;
     - date; sha256sum; mkdir; touch; jq (lesend);
     - Warteschleifen mit sleep in den Ketten.
     - matplotlib habe ich per ls im site-packages geprueft. Kein Python ausserhalb von kleintest.sh.
8. **Start der Hauptketten:** Der lokale ssh-Aufruf blieb haengen (offene Kanaele der nohup-Ketten) und lief als
   Hintergrundaufgabe bis zum Ende der Ketten weiter. Auf die Laeufe hatte das keine Wirkung.
9. **Kein Journaleintrag, kein Peerbus, kein Commit;** das liegt bei der Leitung.

## Kartenvorschlaege (hoechstens zwei)

1. **GUERTEL-FELD-GITTER-1 [H]: Wo kippt "stetig" in "Sprung"?**
   - **Rechnung:** derselbe Stoss mit Kontrolle auf (6, 24), (8, 24) und (10, 24) bei 420 und 450 Grad.
   - **Vorhersage [H]:** Auf (6, 24) springt auch der Stoss eps = 0,01; die Grenze liegt bei r0 zwischen 8 und 10.
   - **Ableitbarkeit:** Ableitbar ist nur die Gitterwinkel-Abschaetzung, nicht der Ausgang.
   - **Laufzeit:** Protokoll etwa 2,5 min je Gitter, Stoss unter 1 min (Platzzahl haengt nur an R).
2. **GUERTEL-FELD-DYN-1 [H]: Echte Zeitdynamik statt FIRE.**
   - **Rechnung:** Der Kern dreht mit fester Rate (Finns Viertakt). Gibt das Feld je 720 Grad Kerndrehung die
     Verdrillung als Welle ab, ohne Sprung?
   - **Vorhersage:** periodisches Abloesen mit Periode 720 Grad, 50 %.

## Dateien

- **Plan:** PLAN.md, PLAN.md.eingefroren-20261004-191321, EINGEFROREN-SHA256.txt.
- **Code:**
  - code/stab.py (neu) und code/auswertung.py (neu);
  - code/guertel2.py und code/guertel.py (Kopien aus GUERTEL-2, Hashes wie dort);
  - je mit .eingefroren-20261004-191321.
- **Eingabe:** eingaben-n1/feld-3d-r12-R24-prot-saat.json (Kopie des N1-Laufs aus GUERTEL-2).
- **Rauchlauf:** rauch-69/ (Protokoll bis 20 Grad, drei Stoss-Tests, Auswertung, Bild, Logs, PRUEFSUMMEN-69-roh.txt).
- **Hauptlaeufe:** lauf-69/
  - prot.json, prot-zust.npz;
  - stoss-T{420,450}-e{0.01,0.1,0.3,0}.json und -end.npz; stoss-T300-e0 und stoss-T270-e0 (Referenzen);
  - auswertung.json, energie-verlauf.png, Logs, PRUEFSUMMEN-69-roh.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/guertel-feld-stab-1/ (code/, rauch/, lauf/, eingaben-n1/).

## Einfach gesagt

Wir haben ein Feld aus vielen kleinen Drehrahmen um einen Kern herum mehr als eine ganze Umdrehung weit verdreht, auf
420 und 450 Grad. Dann haben wir es ganz leicht schraeg angestossen. In allen Faellen hat sich das Feld von selbst in
die kuerzere Gegendrehung umgelegt: Aus 450 Grad vorwaerts wurden 270 Grad rueckwaerts. Dabei ist es glatt
verlaufen, ohne dass das Rechengitter irgendwo reissen musste. Das ist der Guertel-Trick: Zwei volle Umdrehungen
lassen sich glatt wegschieben, eine allein nicht. Das passiert sogar ohne Anstoss, nur etwas spaeter; die Verdrehung
ueber eine Umdrehung hinaus ist also ein wackliger Sattel und kein sicherer Rastplatz. Das stuetzt die Idee, dass so
ein Feld den halben Spin tragen kann. Es bleibt aber eine Modellrechnung auf einem einzigen Gitter und ist kein
Nachweis in der Natur.
