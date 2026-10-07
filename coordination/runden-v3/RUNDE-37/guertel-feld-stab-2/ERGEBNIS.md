# GUERTEL-FELD-STAB-2: Ergebnis (Runde 43, Fast Lane, Robustheit)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 19:24:34 CEST. Plantext ab 19:33:14 CEST, vor dem Code. Code zwischen den date-Messungen
    19:35:49 und 19:39:48 CEST.
  - Rauchlauf 1: 17:39:51 bis 17:40:37 UTC (zehn Units, Spur cpu3, alle rc = 0); Rauchlauf 2: 17:42:27 bis
    17:42:31 UTC (zwei Units, rc = 0). Abschnitt 7 des Plans ab 19:43:14 CEST.
  - Eingefroren 19:44:03 CEST (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe 17:44:09 bis 17:54:35 UTC: 26 Units auf cpu3 und cpu5 (25 Rechnungen und die Auswertung), alle
    rc = 0, keiner wiederholt.
  - **Unterbrechung (Sitzungslimit; laut Leitung gegen 19:53, Limit seit 21:20 zurueckgesetzt):** letzte date-Messung
    davor 19:52:44 CEST; fortgesetzt 21:35:49 CEST (date).
    Waehrenddessen liefen die Ketten auf der .69 zu Ende; die eingefrorene Auswertung lief dort automatisch
    17:54:31 bis 17:54:35 UTC. Restzeit der Zeitbox (bis 20:54:34 CEST) war 61 min 50 s, gerechnet ab 21:35:49
    CEST also bis 22:37:39 CEST.
  - Text ab 21:39:54 CEST.
- **Kennzeichen:** [M] Mathematik; [E] Rechnung im Modell (synthetisch, keine Messdaten); [L] Literatur oder
  Gedaechtnis; [H] Hypothese; [R] im Rauchlauf gesehen.
- **Art:** synthetische Modellrechnung an Modellfeldern (SO(3) auf Z^3, SO(2) auf Z^2), keine Messdatenbestaetigung.

## Ergebnis zuerst

1. **Auf dem feinen Gitter (16, 32) haelt der Guertel-Trick [E].** Alle drei Stoesse bei 450 Grad fuehren ohne
   Gittersprung in die umgekehrte Verdrillung: E faellt von 23135,69 auf 8431,7141 = E(270), auf hoechstens 7,5e-11
   relativ; die Sonde bleibt bei 0,73 oder hoeher, q_z aussen kippt von +0,561 auf -0,395. Bei 420 Grad (Zusatz)
   ebenso, alle drei auf E(300).
2. **Auf dem groben Gitter (8, 16) gibt es bei 450 Grad keinen Vorwaertsast mehr [E].** Der ungestossene Ast springt
   schon bei 400 Grad; der Zustand bei 450 Grad ist gesprungen (Sonde -0,998). Alle drei Stoesse sind deshalb "sprung".
   **GT1 ist nach Plan und nach Wortlaut nicht eingetroffen**, allein wegen (8, 16). Die Schreibtischrechnung im Plan
   hatte das erwartet (Sprung um 375 Grad).
3. **Die Sprunggrenze waechst mit der Aufloesung [E]: theta_max = 420, 540 und 630 Grad** fuer (8, 16), (12, 24) und
   (16, 32). **GT2 ist nach Plan und nach Wortlaut eingetroffen.** (12, 24) trifft N1 (540 Grad).
4. **Auf (16, 32) legt sich der ungestossene Ast im Protokoll selbst um [E, beschreibend].** Ab 540 Grad faellt E
   stetig (Sonde > 0), bei 720 Grad ist das Feld glatt (E = 1e-7), also in der Ausgangsklasse: der volle Guertel-Trick
   ohne Stoss. Die Sonde wird dabei nur kurz negativ (620 und 630 Grad) und ist nach dem Gitter-FIRE bei 630 Grad
   wieder positiv. Nach der eingefrorenen Regel zaehlt das als Sprung bei 620 Grad; der Energie nach ist es kein
   Klassenwechsel (Lesart [H], Abschnitt Teil B).
5. **GT0 ist eingetroffen [E]:** (12, 24) reproduziert GFS-1 bitgleich (Protokoll, drei Stoesse, Referenz). Die
   SO(2)-Kontrolle entdrillt nicht: Alle drei Stoesse fallen auf den Ast zurueck (auf 2e-10), ohne Phasensprung.

## Urteile (lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Kartenwortlaut | tragende Werte |
|---|---|---|---|---|---|
| GT0 | Kontrolle: SO(2) entdrillt nicht (E bleibt auf dem Ast oder springt); (12, 24) bei 450 Grad reproduziert GFS-1 auf 1e-6 relativ | 90 % | **eingetroffen** | **eingetroffen** | SO(2): 3 von 3 "ast", E_end gegen E_Ast,ref = 506,0337977 je -1e-10 bis -2e-10, max abs(phi_a - phi_b) 1,279 < pi. (12, 24): E_schritt(450) = 16725,58389579176, E_gitter(450) = 16722,374712425655, E_end(450) = 6161,0576998 (drei eps), E_ref(270) = 6161,057699788991, jeweils Abweichung 0,0 zu GFS-1; Klassen 3 von 3 "umgekehrt" |
| GT1 | [H] Auf (8, 16) und (16, 32) fuehren je 3 von 3 Stoessen bei 450 Grad ohne Gittersprung in die umgekehrte Verdrillung (E auf E(270) auf 1e-6 relativ) | 60 % | **nicht eingetroffen** | **nicht eingetroffen** | (8, 16): 3 von 3 "sprung" (Sonde vor dem Stoss -0,998, im Lauf bis -0,9988; E_end 445,619 = E(90) der gesprungenen Klasse, E(270) = 3916,38). (16, 32): 3 von 3 "umgekehrt" (E_end/E_ref - 1 = 7,5e-11, 7,4e-11, 7,9e-12; Sonde im Lauf >= 0,732; q_z aussen +0,561 -> -0,395) |
| GT2 | [H] Sprunggrenze waechst streng mit der Aufloesung: (8, 16) < (12, 24) < (16, 32) | 55 % | **eingetroffen** | **eingetroffen** | theta_J = 400 / 540 / 620 Grad (Plan und Wortlaut gleich), theta_max (30-Grad-Raster) = 420 < 540 < 630 |

- Plan und Wortlaut stimmen ueberall ueberein; die Werte liegen weit von allen Schwellen (1e-6, 1e-3, 10 %).
- **Bedeutung nach der Karte:** Fall "GT1 verfehlt" ("Der Befund haengt am Gitter"). Genauer: Er haengt am groben
  Gitter. Auf (12, 24) und (16, 32) haelt der Trick, auf (8, 16) kommt der Gittersprung vor 450 Grad.

## Teil A: Stoesse bei 450 Grad [E]

| Gitter | eps | E vor | E nach Stoss | E Ende | E(270) | Ende/E(270) - 1 | Sonde min | Schritte | halb | P_max (Schritt) | q_z aussen vor / Ende | Klasse Plan / Wortlaut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (8, 16) | 0,01 | 455,34 | 455,91 | 445,6187 | 3916,379 | -0,886 | -0,9988 | 136 | 0 | 0,37 (0) | 0,136 / 0,143 | sprung / sprung |
| (8, 16) | 0,1 | 455,34 | 512,36 | 445,6187 | 3916,379 | -0,886 | -0,9987 | 165 | 0 | 3,71 (0) | 0,136 / 0,143 | sprung / sprung |
| (8, 16) | 0,3 | 455,34 | 963,82 | 445,6187 | 3916,379 | -0,886 | -0,9988 | 167 | 0 | 11,0 (0) | 0,136 / 0,143 | sprung / sprung |
| (12, 24) | 0,01 | 16722,37 | 16722,75 | 6161,0577 | 6161,0577 | 6,7e-12 | 0,489 | 424 | 200 | 139,6 (201) | 0,553 / -0,393 | umgekehrt / umgekehrt |
| (12, 24) | 0,1 | 16722,37 | 16759,31 | 6161,0577 | 6161,0577 | 1,0e-11 | 0,486 | 320 | 138 | 143,5 (139) | 0,553 / -0,393 | umgekehrt / umgekehrt |
| (12, 24) | 0,3 | 16722,37 | 17052,10 | 6161,0577 | 6161,0577 | -3,5e-15 | 0,466 | 292 | 117 | 143,1 (118) | 0,553 / -0,393 | umgekehrt / umgekehrt |
| (16, 32) | 0,01 | 23135,69 | 23136,32 | 8431,7141 | 8431,7141 | 7,5e-11 | 0,749 | 433 | 219 | 225,5 (221) | 0,561 / -0,395 | umgekehrt / umgekehrt |
| (16, 32) | 0,1 | 23135,69 | 23197,70 | 8431,7141 | 8431,7141 | 7,4e-11 | 0,748 | 369 | 164 | 223,9 (166) | 0,561 / -0,395 | umgekehrt / umgekehrt |
| (16, 32) | 0,3 | 23135,69 | 23691,21 | 8431,7141 | 8431,7141 | 7,9e-12 | 0,732 | 340 | 138 | 222,9 (140) | 0,561 / -0,395 | umgekehrt / umgekehrt |

- **Spalten:** "Sonde min" ueber den ganzen Lauf einschliesslich Start- und Stosszustand. "halb" = erster Schritt mit
  E < (E_vor + E_ref)/2. P = Kipp-Amplitude (Feldanteil ausserhalb der (1, z)-Ebene).
- **(8, 16):** Der Startzustand ist schon gesprungen (Protokoll, Teil B). E_vor = 455,34 liegt nahe E(90) der
  gesprungenen Klasse, und jede Relaxation endet dort (445,6187 = E_gitter(90) = 445,61874672674895). Der Stoss klingt
  nur ab.
- **(16, 32):** gleiches Bild wie (12, 24): Der Ast ist ein Sattel, P waechst exponentiell, E faellt (im Bild in etwa
  50 Schritten) auf E(270), die Sonde steigt dabei auf 0,923. Endzustand ist das Spiegelbild der Referenz (q_z aussen
  -0,3954 gegen +0,3954, min q0 je -0,6101).
- **Referenzen (urteilsbildend), alle gueltig:** E(270) = 3916,379371493601 (8, 16; 0 Schritte), 6161,057699788991
  (12, 24; 0 Schritte), 8431,714127449115 (16, 32; 8 Schritte); Sonde 0,722 / 0,869 / 0,923, q_z aussen > 0,
  fmax < 1e-5.
- **Zusatz (16, 32) bei 420 Grad (beschreibend):** Referenz E(300) = 10393,18011395852 (135 Schritte ab dem
  Protokollwert 10393,6279). Alle drei Stoesse "umgekehrt" nach Plan und Wortlaut: E 20207,57 -> 10393,1801,
  Abweichung -3,1e-11 / -1,5e-11 / 1,9e-10; Sonde >= 0,783; Schritte 520 / 428 / 370; halb 273 / 205 / 182;
  q_z aussen +0,544 -> -0,430.
- **Stoss wirkt wie geplant:** groesster Kippwinkel 0,0099998 / 0,099998 / 0,29999 auf (16, 32) an 23.574 Plaetzen
  (12, 24: 9924; 8, 16: 2932).

## Teil B: Sprunggrenze theta_max [E]

| Gitter (SO(3), Z^3) | theta_J Plan / Wortlaut (10 Grad) | **theta_max (30-Grad-Raster)** | Sonde davor (Winkel) | Sonde bei theta_J | E(720) | Klasse bei 720 Grad |
|---|---|---|---|---|---|---|
| (8, 16) | 400 / 400 | **420** | 0,0553 (390) | -0,0843 | 6788,236 = E(360) | gewechselt (ein Sprung) |
| (12, 24) | 540 / 540 | **540** | 0,0099 (530) | -0,1397 | 10848,052 = E(360) | gewechselt (ein Sprung), wie N1 |
| (16, 32) | 620 / 620 | **630** | 0,2783 (610) | -0,6624 | 1,06e-7 = E(0) | Ausgangsklasse (glatt entdrillt) |

- Ein theta_U (glattes Umlegen, q_z aussen < 0 vor dem Sprung) gibt es auf keinem Gitter; q_z aussen wird auf
  (16, 32) erst bei 630 Grad negativ.
- **(8, 16):** Der Ast waechst bis 390 Grad (E 7853,7, Sonde 0,055) und springt dann an einer Bindung (Sonde -0,084
  bei 400, -0,50 bei 420). Nach dem Gitter-FIRE bei 450 Grad liegt E bei 455,3. Danach ist E 360-periodisch:
  E_gitter(540) = 1767,316 = E(180), E_gitter(630) = 3916,379 = E(270), E(720) = E(360).
- **(12, 24):** wie N1: Sonde 0,0099 bei 530, -0,14 bei 540, E(540) = 13178,3, E(720) = E(360). In allen
  verglichenen Werten bitgleich mit der N1-Datei (E und Sonde bei 530, 540 und 720 Grad, alle neun Gitterwerte; per jq
  gelesen).
- **(16, 32), beschreibend:**
  - Bis 530 Grad Vorwaertsast (E 31843,9, Sonde 0,625, P 0,11).
  - Im Gitter-FIRE bei 540 Grad (150 Schritte) beginnt der Zerfall: E faellt von 33020,2 auf 20590,3, P steigt auf
    191, die Sonde bleibt >= 0,571. Bis 600 Grad faellt E weiter (8332,5), Sonde 0,64 bis 0,83, q_z aussen sinkt
    von 0,60 auf 0,10.
  - Bei 610 Grad sinkt die Sonde auf 0,278, bei 620 auf -0,662, bei 630 (Schritt) auf -0,765. Das Gitter-FIRE bei 630
    Grad endet mit Sonde 0,992 und E = 942,373 = E(90) des Vorwaertsasts (942,349), also der umgekehrten Verdrillung
    630 - 720 = -90 Grad. Ab 640 Grad bleibt die Sonde ueber 0,993; bei 720 Grad ist E = 1,06e-7.
  - **Lesart [H]:** Die negative Sonde bei 620 und 630 Grad ist eine kurze Vorzeichenstoerung waehrend des schnellen
    Umlegens (P um 130), kein Klassenwechsel: Ein Sprung haette die Energie auf die gesprungene Klasse gesetzt (bei 630
    Grad E(270) = 8431,7, bei 720 Grad E(360) = 14911,0), gemessen sind E(90) und 0. Nach der eingefrorenen Regel zaehlt
    sie trotzdem als Sprung (theta_max = 630); ich regle das nicht nach. Fuer GT2 ist es gleich: Auch "kein Sprung"
    waere groesser als 540.
- **Bild lauf-69/sprunggrenze.png:** E und Sonde des Protokollzustands ueber theta, je Gitter; gestrichelt theta_max.

![Sprunggrenze](lauf-69/sprunggrenze.png)

## Teil C: SO(2)-Kontrolle [E]

- SO(2) auf der Z^2-Scheibe (12, 24), 450 Grad. Referenz ohne Stoss: E_Ast,ref = 506,03379765016035 (39 Schritte ab
  dem Protokollwert 506,0337977936, fmax 9,4e-6), max abs(phi_a - phi_b) = 1,279 < pi.
- Stoesse eps = 0,01 / 0,1 / 0,3: E steigt auf 506,040 / 506,653 / 511,628 und faellt in 144 / 200 / 214 Schritten auf
  den Ast zurueck (Abweichung -1,4e-10 / -2,1e-10 / -1,9e-10 zu E_Ast,ref). Kein Phasensprung (max 1,279 rad).
- Das ist, was pi_1(SO(2)) = Z verlangt [M]: Der Stoss in der einzigen Richtung klingt ab; eine Entdrillung gibt es
  nicht. Werkzeugprobe bestanden.

## Bild: Energieverlauf je Stoss

**lauf-69/energie-verlauf.png** (eingefrorener Auswertecode):

- Spalten: (8, 16), (12, 24), (16, 32) bei 450 Grad (SO(3)) und die SO(2)-Kontrolle. Zeilen: E, Sonde, Kipp-Amplitude
  P (logarithmisch) ueber die FIRE-Schritte nach dem Stoss. Gestrichelt E(270), gepunktet der Ast.
- (12, 24) und (16, 32): E bleibt erst auf dem Ast und faellt dann steil auf E(270); je groesser eps, desto frueher.
  P waechst bis zum Abfall auf einer Geraden (exponentiell) und klingt danach ab; die Sonde steigt beim Abfall.
- (8, 16): Die Sonde liegt von Anfang an bei -1 (X am Schritt 0); E faellt nur vom Stosswert auf den gesprungenen
  Zustand.
- SO(2): E faellt vom Stosswert auf den Ast zurueck; die Sonde bleibt weit unter pi.

![Energieverlauf](lauf-69/energie-verlauf.png)

## Kontrollen

1. **GT0:** (12, 24) bitgleich zu GFS-1 (gleicher Code, gleiche Saat): Protokoll bei 450 Grad, drei Stoesse,
   Referenz. Rauchlauf: (12, 24) bei 20 Grad bitgleich, Abschnittsprobe (8, 16) 0 -> 10 -> 20 bitgleich zu 0 -> 20.
2. **Fortsetzung (16, 32) bei 450 Grad:** Der zweite Abschnitt setzt nahtlos fort (460 Grad nach 450); die sha256 der
   Fortsetzungsdatei im Laufkopf stimmt mit prot-g16a-ck.npz ueberein.
3. **Codehashes:** Alle 25 Laufdateien tragen code_sha256 32c21633... (stab2.py, eingefroren), g2 c9374a98...,
   g1 795f474d...; auswertung.json traegt e0cdb5f1... (eingefroren). Die eingefrorenen Dateien sind unveraendert
   (sha256sum -c gegen EINGEFROREN-SHA256.txt, 12 von 12 OK).
4. **Pruefsummen:** 91 von 91 Laufdateien und 45 von 45 Rauchlaufdateien haben auf beiden Rechnern dieselbe sha256
   (lauf-69/ und rauch-69/PRUEFSUMMEN-69-roh.txt, lokal mit sha256sum -c).
5. **Laufzeiten:** Protokoll (16, 32) 272,7 s und 161,3 s, (12, 24) 191,9 s, (8, 16) 64,6 s; Stoesse (16, 32) 45 bis
   68 s, (12, 24) 17 bis 25 s, (8, 16) unter 4 s. Alle unter 10 min. Alle Stoesse und Referenzen konvergierten
   (fmax < 1e-5) in hoechstens 520 Schritten.

## Ableitbarkeit

- **Vorab ableitbar [M]:** Sattel im Kontinuum; E_Ende = E(720 - theta) aus der Symmetrie q -> q quer (die
  Uebereinstimmung auf 1e-11 ist eine Kontrolle, keine Messung); die Bitgleichheit von GT0 (gleicher Code, gleiche
  Saat); theta_max(12, 24) = 540 aus N1; grob auch GT2 (Kernbindungswinkel je Grad etwa 2/(r0 + 1)).
- **Schreibtischrechnung gegen Rechnung:** erwartet etwa 375 Grad auf (8, 16), gemessen 400 (theta_J); erwartet etwa
  705 Grad auf (16, 32), gemessen 620. Die Schaetzung kannte den Zerfall nicht, der auf (16, 32) bei 540 Grad vor dem
  Sprung einsetzt.
- **Gemessen, nicht ableitbar [E]:** dass (8, 16) vor 450 Grad springt; dass (16, 32) sprungfrei entdrillt (gestossen
  bei 420 und 450 Grad, ungestossen im Protokoll ab 540 Grad); die kurze Sondenverletzung auf (16, 32); die
  Zeitskalen (halb 138 bis 219 Schritte bei 450 Grad).

## Dimensionen (AGENTS.md)

- **Innere Symmetrie:**
  - SO(3), gerechnet [E] auf Z^3: Auf (12, 24) und (16, 32) legt das gestossene Feld 720 Grad ohne Klassenwechsel ab
    (450 -> -270 Grad; pi_1(SO(3)) = Z_2), auf (16, 32) auch ungestossen im Protokoll; auf (8, 16) gewinnt vorher der
    Gittersprung.
  - SO(2), gerechnet [E] auf Z^2: keine Entdrillung, der Stoss klingt ab (pi_1(SO(2)) = Z) [M].
- **Raum:**
  - SO(3) nur auf dem Z^3-Kugelgitter, SO(2) nur auf der Z^2-Scheibe. Nicht gerechnet: SO(2) auf Z^3, SO(3) auf Z^2,
    alles in 1D. Gitterergebnisse werden nicht zwischen Dimensionen uebertragen; die Gitterwinkel skalieren in 2D und
    3D verschieden.
  - Die Sattel-Aussage des Kontinuums gilt radial fuer d = 1, 2, 3 [M]. Ein radialer 3D-Lauf ist weder ein 1D-Modell
    noch ein voller 3D-Stabilitaetsnachweis; gestossen wurde eine Kipprichtung.
- **Offen:** echte Zeitdynamik statt FIRE; ob die Sondenstoerung auf (16, 32) an der Protokollgeschwindigkeit haengt.

## Selbstanzeigen

1. **Unterbrechung:** Sitzungslimit zwischen 19:52:44 CEST (letzte date-Messung) und 21:35:49 CEST (date). Die Ketten
   und die eingefrorene Auswertung liefen in dieser Zeit auf der .69 zu Ende (letzte Unit 17:54:35 UTC). Die Zeitbox
   zaehle ich mit der Restzeit 61 min 50 s ab 21:35:49, also bis 22:37:39 CEST (Kopfrechnung).
2. **Aenderung nach dem Rauchlauf, vor dem Einfrieren:** Der SO(2)-Bezug nach Plan ist jetzt ein Referenzlauf eps = 0
   statt des Protokollzustands, nachdem ich bei 20 Grad gesehen hatte, dass der Protokollzustand (1,0354) ueber dem
   relaxierten Wert (1,0278) liegt und die Plan-Klasse deshalb faelschlich "entdrillt" ergab. Das betrifft nur die
   Kontrolle (GT0a), steht in PLAN.md Abschnitt 7 und ist eingefroren.
   Mit dem alten Bezug haette die Kontrolle bei 450 Grad auch bestanden (Abweichung zum Protokollzustand -4e-10 bis
   -5e-10); gesehen habe ich das erst nach dem Einfrieren.
3. **Lesart der Karte:** "Schritte von 30 Grad" habe ich als Ableseraster des 10-Grad-Protokolls gelesen, nicht als
   30-Grad-Protokoll (Begruendung im Plan, vor dem Einfrieren).
4. **Kopfrechnung:** die Schreibtischrechnung im Plan (Koeffizienten 2/(r0 + 1), Faktor 1,75, Schaetzungen 375 und 705
   Grad), die Laufzeitschaetzungen und die Zeitbox-Restzeit. Alle anderen Zahlen stammen aus den Laufdateien und aus
   auswertung.json (jq nur lesend, mit select und transpose zur Anzeige).
5. **GFS-1-Werte vor dem Einfrieren gesehen:** im veroeffentlichten GFS-1-Ergebnis und im Rauchlauf (E_schritt bei
   20 Grad). Die Urteile lesen sie mechanisch aus Kopien (eingaben-gfs1/, sha256 eingefroren).
6. **Werkzeuge:**
   - Lokal ausserhalb der Liste: date, ls, mkdir, cp, cat (Heredoc fuer die Kettenskripte, gequotet), cut, wc, cd;
     Warteschleifen mit ssh und sleep (until-Schleifen, ein Monitor). Kein lokaler Interpreter, keine Rechnung per
     Werkzeug.
   - Auf der .69 ausserhalb des Starters: mkdir, ls, du, grep, cat, sha256sum, mv, touch, date, setsid/nohup und die
     Kettenskripte mit sleep-Warteschleifen. Kein Python ausserhalb von kleintest.sh.
7. **Start der Hauptketten:** Der lokale ssh-Aufruf blieb haengen (wie in GFS-1) und lief als Hintergrundaufgabe weiter;
   ohne Wirkung auf die Laeufe. Einige spaetere ssh-Aufrufe meldeten "ControlSocket already exists" (ohne Folgen).
8. **Feldname:** "schreibzeit_utc" im Laufkopf ist die Schreibzeit am Laufende; die Startzeiten stehen in den Logs.
9. **Kein Journaleintrag, kein Peerbus, kein Commit;** das liegt bei der Leitung.
10. **Ausserhalb des Kartenordners:** gelesen habe ich die dataviz-Anleitung und ihre Palette (Skill-Ordner unter
    /tmp/claude-1000/bundled-skills). Die Ausgaben meiner Hintergrund-Warteschleifen legt die Umgebung selbst unter
    /tmp/claude-1000/.../tasks/ ab; selbst geschrieben habe ich dort und im Scratchpad der Leitung nichts.

## Kartenvorschlaege (hoechstens zwei)

1. **GUERTEL-FELD-KLASSE-1 [H]: Sprung oder Vorzeichenstoerung?** Auf (16, 32) wurde die Sonde bei 620 und 630 Grad
   negativ, ohne dass die Klasse wechselte (E bei 630 = E(90), bei 720 = 0). Rechnung: dasselbe Protokoll mit
   Aufzeichnung der Bindungen mit q_a . q_b <= 0 (Ort, Anzahl) und einer Klassensonde (Vorzeichen des gehobenen
   Kernwerts entlang mehrerer Pfade vom Rand). Vorhersage [H]: einzelne Bindungen nahe dem Kern, nach weniger als 30
   FIRE-Schritten verheilt.
2. **GUERTEL-FELD-TEMPO-1 [H]: Zerfall gegen Sprung, abhaengig vom Protokolltempo.** Auf (16, 32) kam der Zerfall
   (540 Grad) vor dem Sprung, auf (12, 24) nicht. Rechnung: (8, 16) und (12, 24) mit 3- und 10-mal mehr FIRE-Schritten
   je 10 Grad. Vorhersage [H]: Mit langsamerem Protokoll legt sich auch (12, 24) vor 540 Grad glatt um; (8, 16) springt
   weiter vorher, weil sein Ast schon bei 400 Grad an der Bindungsgrenze ist.

## Dateien

- **Plan:** PLAN.md, PLAN.md.eingefroren-20261004-194403, EINGEFROREN-SHA256.txt.
- **Code:** code/stab2.py und code/auswertung.py (neu, aus GFS-1 kopiert und erweitert), code/guertel2.py und
  code/guertel.py (Kopien, Hashes wie GUERTEL-2), je mit .eingefroren-20261004-194403.
- **Skripte:** skripte/kette-K3.sh und skripte/kette-K5.sh (eingefroren), skripte/kette-rauch.sh und
  skripte/kette-rauch2.sh.
- **Eingaben:** eingaben-gfs1/ (Kopien der GFS-1-Laufdateien prot.json, stoss-T450-e*.json, stoss-T270-e0.json).
- **Rauchlauf:** rauch-69/ (Laeufe bis 20 Grad, Abschnittsprobe, Auswertung, Bilder, Logs, PRUEFSUMMEN-69-roh.txt).
- **Hauptlaeufe:** lauf-69/
  - prot-g8, prot-g12, prot-g16a, prot-g16b, prot-s2 (json, -zust.npz, -ck.npz);
  - stoss-{g8,g12,g16}-T450-e{0.01,0.1,0.3}, stoss-{g8,g12,g16}-T270-e0, stoss-g16-T420-e*, stoss-g16-T300-e0,
    stoss-s2-T450-e{0,0.01,0.1,0.3} (json, -end.npz);
  - auswertung.json, energie-verlauf.png, sprunggrenze.png, Logs, PRUEFSUMMEN-69-roh.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/guertel-feld-stab-2/ (code/, skripte/, eingaben-gfs1/, rauch/, lauf/).

## Einfach gesagt

Wir haben ein Feld aus kleinen Drehrahmen um einen Kern um 450 Grad verdreht und angestossen, diesmal auf einem
groeberen und einem feineren Rechengitter. Auf dem feinen Gitter legt sich das Feld genau wie zuvor glatt in die kuerzere
Gegendrehung um; dort passiert das sogar ohne Anstoss, und nach zwei vollen Umdrehungen ist das Feld wieder ganz glatt.
Auf dem groben Gitter reisst das Feld schon bei 400 Grad an einer Stelle, bevor der Trick ueberhaupt moeglich ist. Die
Grenze, ab der das Feld reisst, steigt mit der Feinheit des Gitters: 420, 540 und 630 Grad, und auf dem feinsten Gitter
ist es nur noch eine kurze Stoerung mitten im glatten Umlegen. Das passt zum Bild, dass der Guerteltrick im glatten
Grenzfall immer klappt und nur grobe Gitter ihn verhindern; es bleibt eine Modellrechnung, kein Nachweis in der Natur.
