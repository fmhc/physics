# GUERTEL-FINN-NETZ-1: Ergebnis (Runde 43; Guertel-Trick auf Finns Tetraeder-Netz)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 19:38:15 CEST. Plantext 19:46:13 bis 19:47:24 CEST; Code 19:49:26 bis 19:53:00 CEST.
  - **Unterbrechung (Sitzungslimit):** nach 19:53:00 CEST (letzte Dateiaenderung, mtime code/auswertung_fn.py) bis
    zur Wiederaufnahme 21:35:55 CEST. Verbraucht waren 14 min 45 s; Restzeit 105 min 15 s ab Wiederaufnahme, also bis
    23:21:10 CEST [Zusatz Leitung]. Auf der .69 lief in der Pause nichts von mir; der Ordner dort existierte noch nicht.
  - Rauchlauf 1: 19:37:47 bis 19:38:21 UTC, 16 Units auf cpu6 und cpu7, alle rc = 0. Rauchlauf 2 (Wahl und Auswertung
    nach einer Korrektur): 19:40:26 bis 19:40:29 UTC, rc = 0.
  - Eingefroren 21:42:20 CEST (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe 19:42:26 bis 19:50:01 UTC: 31 Units (6 Protokolle, Wahl, 6 SO(3)-Stoesse, 2 Referenzen, 2 Kontrollen,
    5 leere Aufrufe fuer den nicht belegten dritten Wahl-Index, 8 SO(2)-Laeufe, Auswertung), alle rc = 0, keiner
    wiederholt.
  - Text ab 21:47:34 CEST (waehrend der letzten Laeufe), fertig gestellt ab 21:53:01 CEST.
- **Kennzeichen:** [M] Mathematik; [E] Rechnung im Modell (synthetisch, keine Messdaten); [L] Literatur oder
  Gedaechtnis; [H] Hypothese; [R] im Rauchlauf gesehen.
- **Art:** synthetische Modellrechnung an einem Modellfeld (Einheitsquaternion-Feld auf zwei 3D-Graphen), keine
  Messdatenbestaetigung.
- **Netz:** Diamant (Finns Netz: Knoten = Tetraedermitten, 4 Nachbarn ueber die geteilten Ecken), Zellkante 2, also
  Knotendichte 1 wie Z^3. Kugel (12, 24): 65441 Knoten, 50632 frei, Grad 4, Bindungslaenge 0,866. Vergleich Z^3
  (12, 24): 65267 Knoten, 50624 frei, Grad 6.

## Ergebnis zuerst

1. **Der Guertel-Trick gelingt auch auf Finns Tetraeder-Netz [E].** Bei 420 und 450 Grad fuehren alle sechs Stoesse
   (eps = 0,01, 0,1, 0,3) ohne Gittersprung in die umgekehrte Verdrillung. E faellt von 7463 auf 3850,04 = E(300)
   bzw. von 8536 auf 3125,12 = E(270), jeweils auf hoechstens 7e-10 relativ. **GF2 nach Plan und Wortlaut
   eingetroffen** (6 von 6).
2. **Der Abstieg ist glatt [E].** Die Sonde min q_a . q_b bleibt in jedem Lauf bei 0,724 oder hoeher (Sprung erst bei
   0). E steigt nie ueber den Wert direkt nach dem Stoss. Ohne Stoss zerfaellt der Ast genauso, nur spaeter (703 bzw.
   468 FIRE-Schritte): Auch auf dem Diamant-Netz ist der Ast ueber 360 Grad ein Sattel, keine Rast.
3. **theta_max ist auf beiden Netzen 540 Grad [E]** (10- und 30-Grad-Protokoll, SO(3) und SO(2)). **GF1 eingetroffen.**
   Die Bindungen sind auf dem Diamant-Netz aber weniger verdreht: Sonde bei 450 Grad 0,746 gegen 0,488 auf Z^3. Der
   Sprung entsteht dort erst in der langen Relaxation bei 540 Grad, aus einem Zustand mit Sonde 0,52; auf Z^3 laeuft
   die Sonde vorher fast auf 0 (0,0099 bei 530 Grad).
4. **GF0 eingetroffen [E]:** K0 trifft GFS1 bitgleich (Abweichung 0,0 bei 420 und 450 Grad). Das SO(2)-Feld auf dem
   Diamant-Netz entdrillt nicht: alle sechs Stoesse "bleibt", E_Ende/E_vor >= 0,9997, groesster Phasensprung 1,46 rad
   (< pi).
5. **Bedeutung, wie in der Karte vorab [H]:** Ein Drehfeld auf Finns Netz kann seine Verdrillung jenseits einer vollen
   Umdrehung stetig um 720 Grad ablegen; ein Feld mit nur einer Drehebene (SO(2)) kann das nicht. Das stuetzt die
   Grundlage fuer halben Spin auf Finns Netz. Gezeigt nur quasistatisch (FIRE), fuer eine Kipprichtung und eine
   Kugelgroesse.

## Urteile (lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Wortlaut | tragende Werte |
|---|---|---|---|---|---|
| GF0 | Kontrollen: K0 auf 1e-6; SO(2) auf dem Diamant-Netz entdrillt nicht | 85 % | **eingetroffen** | **eingetroffen** | K0: E_schritt(420) = 14642,446583942661, E_schritt(450) = 16725,58389579176, E_gitter(450) = 16722,374712425655, Abweichung zu GFS1 je 0,0, Sonde 0,612 / 0,521 / 0,489; SO(2): 6 von 6 "bleibt", E_Ende/E_vor 0,99968 (420) bzw. 0,99999999 (450), max abs(dphi) im Lauf <= 1,458 |
| GF1 | [H] Vorwaertsast ohne Sprung bis mindestens 450 Grad (theta_max > 450) | 45 % | **eingetroffen** | **eingetroffen** | theta_max = 540 im 10-Grad-Protokoll (Plan) und im 30-Grad-Protokoll (Wortlaut); laufende Sonde bei 450: 0,746 (beide); Drehsinn aussen positiv bis 510 Grad |
| GF2 | [H] Bei 420 bzw. 450 Grad fuehren mindestens 2 von 3 Stoessen ohne Gittersprung in die umgekehrte Verdrillung (E auf E(720 - theta) auf 1e-6 relativ) | 50 % | **eingetroffen** (3 von 3 und 3 von 3 "umgekehrt") | **eingetroffen** (3 von 3 und 3 von 3) | rho zwischen -1,6e-13 und 4,5e-10 (Grenze 0,10); E_Ende/E_ref - 1 zwischen -2,8e-13 und 7,0e-10 (Grenze 1e-6); Sonde im Lauf >= 0,724; mittleres q_z aussen am Ende -0,429 (420) bzw. -0,394 (450), vorher +0,543 bzw. +0,559 |

- Plan und Wortlaut stimmen ueberall ueberein. Die Werte liegen weit von allen Schwellen; deren Wahl entscheidet hier
  nichts. Winkelwahl: Plan und Wortlaut je {420, 450} (theta_max > 450 in beiden Protokollen).
- E_ref aus den Referenzlaeufen: E(300) = 3850,042044576 (vom Protokollwert 3850,3139 in 122 Schritten
  nachrelaxiert, Sonde 0,910); E(270) = 3125,123322954 (schon konvergiert, 0 Schritte, Sonde 0,929). Beide im
  Vorwaertsdrehsinn (q_z aussen +0,429 bzw. +0,394).

## theta_max: Diamant gegen Z^3 bei gleicher Knotenzahl [E]

| Netz | Feld | Protokoll | theta_max (30-Grad-Raster) | Sonde bei 420 / 450 / 510 Grad | Schrittende bei 540 Grad (vor FIRE 150) | Laufzeit |
|---|---|---|---|---|---|---|
| Diamant | SO(3) | 10-Grad (Plan) | **540** | 0,802 / 0,746 / 0,630 | 0,523, Sprung erst in FIRE 150 | 137,9 s |
| Z^3 | SO(3) | 10-Grad (K0) | **540** | 0,612 / 0,488 / 0,202 | -0,140, Sprung schon im Schritt (530: 0,0099) | 183,0 s |
| Diamant | SO(3) | 30-Grad (Wortlaut) | **540** | 0,805 / 0,746 / 0,645 | 0,567, Sprung erst in FIRE 150 | 75,9 s |
| Z^3 | SO(3) | 30-Grad | **540** | 0,620 / 0,487 / 0,263 | 0,081, Sprung erst in FIRE 150 | 103,4 s |
| Diamant | SO(2) | 10-Grad | **540** | max abs(dphi) 1,253 / 1,458 / 1,698 | 1,861, Sprung erst in FIRE 150 | 28,5 s |
| Z^3 | SO(2) | 10-Grad (Zusatz) | **540** | max abs(dphi) 1,758 / 2,122 / 2,508 | 2,799, Sprung erst in FIRE 150 | 37,4 s |

- Sonde: laufendes Minimum von q_a . q_b (SO(3), Sprung bei <= 0) bzw. laufendes Maximum von abs(phi_a - phi_b)
  (SO(2), Sprung bei >= pi). Auch auf 10 Grad genau liegt der erste Sprung ueberall bei 540 Grad.
- **Lesart:**
  - Der Sprungwinkel ist gleich, die Bindungswinkel davor nicht. Bei gleichem theta sind die Diamant-Bindungen weniger
    verdreht; die kuerzere Bindung (0,866) wirkt wie erwartet [H, PLAN 0.5].
  - Trotzdem springt der Diamant schon aus Sonde 0,52 bzw. Phasensprung 1,86 rad, also jenseits von pi/2, wo die
    Bindungsenergie 2(1 - cos omega) weich wird. Z^3 haelt bis nahe an pi. Lesart [H]: Das lockere 4er-Netz stuetzt
    weich gewordene Bindungen schlechter; beide Effekte heben sich hier zufaellig bei 540 Grad auf.
  - Gesprungen wird fast ueberall erst in der langen Relaxation (FIRE 150 an Vielfachen von 90 Grad). Ob der
    Diamant-Ast bei 480 und 510 Grad eine lange Relaxation uebersteht, ist nicht geprueft; dort liefen je nur 30
    FIRE-Schritte. Fuer GF1 zaehlt 450 Grad, und dort lief FIRE 150 ohne Sprung.
- **SO(2) gegen SO(3) [M bestaetigt]:** Der ebene SO(3)-Ast ist dasselbe Problem wie das SO(2)-Feld (PLAN 0.2). E(450)
  auf dem Diamant: 8535,5647 (SO(3)) gegen 8535,5650 (SO(2)); gleicher Sprungwinkel.
- **Kontinuum [M bestaetigt]:** E_Diamant/E_Z3 bei 90 Grad = 0,506 (erwartet 1/2, PLAN 0.4).
- **Nach dem Sprung:** Das Feld wechselt die SU(2)-Klasse; E(720) liegt dann praktisch bei E(360) (Diamant 5516,384
  gegen 5516,379; Z^3 10848,052 gegen 10848,052), wie in GFS1 beschrieben.

## Laeufe je Stoss, Diamant SO(3) [E]

| theta | eps | E vor | E nach Stoss | E Ende | E_Ende/E_ref - 1 | Sonde min | Schritte | halb | P_0 | P_max (Schritt) | q_z aussen Ende | Klasse Plan / Wortlaut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 420 | 0,01 | 7463,25 | 7463,46 | 3850,0420 | 4,2e-10 | 0,793 | 532 | 292 | 0,45 | 147,2 (294) | -0,429 | umgekehrt / umgekehrt |
| 420 | 0,1 | 7463,25 | 7484,68 | 3850,0420 | 2,7e-10 | 0,793 | 423 | 217 | 4,47 | 146,3 (218) | -0,429 | umgekehrt / umgekehrt |
| 420 | 0,3 | 7463,25 | 7654,97 | 3850,0420 | 4,6e-11 | 0,781 | 397 | 193 | 13,3 | 145,3 (194) | -0,429 | umgekehrt / umgekehrt |
| 420 | 0 (Kontrolle) | 7463,25 | 7463,25 | 3850,0420 | 5,8e-10 | 0,793 | 703 | 463 | 0,029 | 148,4 (465) | -0,429 | umgekehrt / umgekehrt (beschreibend) |
| 450 | 0,01 | 8535,56 | 8535,78 | 3125,1233 | 1,1e-10 | 0,746 | 451 | 232 | 0,46 | 146,5 (234) | -0,394 | umgekehrt / umgekehrt |
| 450 | 0,1 | 8535,56 | 8556,78 | 3125,1233 | 7,0e-10 | 0,744 | 387 | 174 | 4,56 | 145,4 (176) | -0,394 | umgekehrt / umgekehrt |
| 450 | 0,3 | 8535,56 | 8725,31 | 3125,1233 | -2,8e-13 | 0,724 | 345 | 146 | 13,5 | 144,7 (148) | -0,394 | umgekehrt / umgekehrt |
| 450 | 0 (Kontrolle) | 8535,56 | 8535,56 | 3125,1233 | 3,0e-10 | 0,746 | 468 | 249 | 0,062 | 146,5 (251) | -0,394 | umgekehrt / umgekehrt (beschreibend) |

- **Spalten:** "halb" = erster Schritt mit E < (E_vor + E_ref)/2. P = Kipp-Amplitude (Anteil ausserhalb der
  (1, z)-Ebene); am Ende in allen Laeufen < 0,007. Sonde min = Minimum ueber den ganzen Lauf, einschliesslich des
  Zustands direkt nach dem Stoss. Die groesste Energie im Lauf ist jeweils die direkt nach dem Stoss.
- **Endzustand:** Spiegelbild der Referenz (q -> q quer): q_z aussen -0,429 gegen +0,429 (420/300) und -0,394 gegen
  +0,394 (450/270). Das ist die umgekehrte Verdrillung -300 bzw. -270 Grad; der Kern bleibt bei q_z(theta).
- **Vergleich mit Z^3 (GFS1, beschreibend):** Auf Z^3 brauchten die Stoesse 292 bis 424 Schritte ("halb" 117 bis 219),
  ohne Stoss 384 bzw. 594. Auf dem Diamant dauert der Zerfall in FIRE-Schritten etwas laenger; der Ablauf ist derselbe.

## SO(2)-Kontrolle auf dem Diamant-Netz (Teil C) [E]

| theta | eps | E vor | E nach Stoss | E Ende | E_Ende/E_vor | max abs(dphi) im Lauf | Schritte | Klasse Plan / Wortlaut |
|---|---|---|---|---|---|---|---|---|
| 420 | 0,01 | 7464,59 | 7465,19 | 7462,21 | 0,99968 | 1,310 | 191 | bleibt / bleibt |
| 420 | 0,1 | 7464,59 | 7480,07 | 7462,21 | 0,99968 | 1,310 | 236 | bleibt / bleibt |
| 420 | 0,3 | 7464,59 | 7574,47 | 7462,21 | 0,99968 | 1,315 | 256 | bleibt / bleibt |
| 420 | 0 (Kontrolle) | 7464,59 | 7464,59 | 7462,21 | 0,99968 | 1,310 | 184 | bleibt (beschreibend) |
| 450 | 0,01 | 8535,57 | 8535,66 | 8535,56 | 0,99999999 | 1,458 | 168 | bleibt / bleibt |
| 450 | 0,1 | 8535,57 | 8545,53 | 8535,56 | 0,99999999 | 1,458 | 224 | bleibt / bleibt |
| 450 | 0,3 | 8535,57 | 8625,89 | 8535,56 | 0,99999999 | 1,458 | 243 | bleibt / bleibt |
| 450 | 0 (Kontrolle) | 8535,57 | 8535,57 | 8535,56 | 0,99999999 | 1,458 | 61 | bleibt (beschreibend) |

- E vor bei 420 Grad ist ein Schrittzustand (FIRE 30); er relaxiert auf 7462,21 und bleibt dort. Die mittlere Phase
  aussen bleibt positiv (1,30 bzw. 1,38 rad). Das SO(3)-Feld faellt am selben Winkel auf 3850 bzw. 3125.

## Bilder

- **lauf-69/energie-verlauf.png** (eingefrorener Auswertecode): Zeilen E, Sonde und Kipp-Amplitude P (logarithmisch)
  ueber die FIRE-Schritte nach dem Stoss; Spalten 420 und 450 Grad; grau ohne Stoss; gestrichelt E(720 - theta),
  gepunktet der Ast.
  - **E** bleibt erst auf dem Ast und faellt dann in etwa 50 Schritten auf E(720 - theta), je groesser eps, desto
    frueher.
  - **Die Sonde** steigt beim Abfall von 0,73 bis 0,80 auf etwa 0,93 und kommt nie in die Naehe von 0.
  - **P** waechst bis zum Abfall auf einer Geraden, also exponentiell (instabile Richtung des Sattels), erreicht etwa
    145 und klingt dann ab.
- **lauf-69/vorwaertsast.png:** links E am Schrittende ueber theta, rechts die laufende Sonde (SO(2) umgerechnet als
  cos(max abs(dphi)/2), bei pi abgeschnitten); blau Diamant, orange Z^3; durchgezogen 10-Grad-Protokoll SO(3),
  gestrichelt 30-Grad-Protokoll, gepunktet SO(2). Die Diamant-Energie liegt bei etwa der Haelfte; die Diamant-Sonde
  faellt langsamer und springt erst bei 540 Grad aus 0,52 bis 0,57 senkrecht ab, die Z^3-Sonde laeuft vorher gegen 0.

## Kontrollen

1. **K0:** Das Z^3-Protokoll ist bitgleich zu GFS1 (gleicher Code, gleiche Saat, gleiche Bindungsreihenfolge;
   z3_gleich_g2 = true).
2. **Codehashes:** Alle 25 Laufdateien tragen code_sha256 e9f357b6... (finn.py, eingefroren) und die unveraenderten
   Hashes von stab.py, guertel2.py und guertel.py; auswertung.json traegt 0d66079a... (eingefroren).
3. **Pruefsummen:**
   - lauf-69/: 88 von 88 Dateien mit derselben sha256 wie auf der .69 (PRUEFSUMMEN-69-roh.txt, lokal mit sha256sum -c).
   - rauch-69/: 51 von 51; zwei Logs liegen lokal unter dem Namen *.rauch1.
4. **Der Stoss wirkt wie geplant:** 10024 freie Knoten der inneren Haelfte; groesster Kippwinkel 0,0099981 / 0,099981 /
   0,29994; Sonde direkt nach dem Stoss >= 0,725; Kern, Rand und aeussere Haelfte bleiben.
5. **Referenzen:** gueltig, Vorwaertsdrehsinn, konvergiert (fmax < 1e-5).
6. **Laufzeiten:** Protokolle 28,5 bis 183,0 s; SO(3)-Stoesse 15,6 bis 29,2 s; SO(2)-Stoesse 0,6 bis 2,2 s. Alle weit
   unter 10 min, wie im Rauchlauf erwartet.

## Ableitbarkeit

- **Vorab ableitbar, nur Konsistenz [M]:**
  - E_Ende = E(720 - theta) folgt aus der Symmetrie q -> q quer auf jedem Graphen, sobald der Stoss ohne Sprung im
    richtigen Tal endet. Die Uebereinstimmung auf 1e-10 ist deshalb eine Kontrolle, keine Messung.
  - E_Diamant/E_Z3 = 1/2 bei kleiner Verdrillung (gemessen 0,506) und der gleiche Ast fuer SO(2) und ebenes SO(3).
- **Gemessen, nicht ableitbar [E]:**
  - Auf dem Diamant-Netz existiert der Vorwaertsast bis 510 Grad und springt bei 540 Grad, wie auf Z^3.
  - Der Ast ist auch dort ein Sattel, und die Relaxation nimmt den stetigen Weg statt des Gittersprungs.
  - Bindungswinkel: bei gleichem theta kleiner als auf Z^3; der Sprung kommt aber aus einem weiter entfernten Zustand.
- **Ableitbarkeitsprobe der Karte:** Alle drei dort als nicht ableitbar genannten Punkte sind durch die Rechnung
  beantwortet.

## Dimensionen (AGENTS.md)

- **Innere Symmetrie, getrennt gerechnet:**
  - SO(3) [E]: Der Ast zerfaellt stetig in die um 720 Grad kleinere Verdrillung (pi_1(SO(3)) = Z_2).
  - SO(2) [E, M]: Keine Kipprichtung; der einzig moegliche Stoss (Phase) relaxiert zurueck, die Windung bleibt
    (pi_1(SO(2)) = Z). Sprunggrenze 540 Grad wie SO(3), auf beiden Netzen.
- **Raum:**
  - Gerechnet sind zwei 3D-Graphen bei fast gleicher Knotenzahl (65441 gegen 65267): Diamant (Grad 4) und Z^3 (Grad 6).
  - Die Kontinuumsaussagen (Sattel jenseits 360 Grad, radial) gelten in d = 1, 2, 3 [M]. Die Gitterbefunde gelten nur
    fuer diese beiden 3D-Netze und diese Kugelgroesse; nicht auf 1D oder 2D uebertragen.
  - Ein radialer 3D-Lauf mit einer Kipprichtung ist kein voller 3D-Stabilitaetsnachweis.
- **Offen:** lange Relaxation zwischen 480 und 510 Grad auf dem Diamant; andere Kugelgroessen; echte Zeitdynamik statt
  FIRE; der 720-Grad-Zustand selbst (das Protokoll springt vorher).

## Selbstanzeigen

1. **Unterbrechung:** Sitzungslimit nach 19:53:00 bis 21:35:55 CEST. Die Zeitbox gilt nach Vorgabe der Leitung ab
   Wiederaufnahme (bis 23:21:10 CEST). Im Plan-Kopf steht die alte Grenze 21:38:15 weiter, ergaenzt um die neue.
2. **Lesart von "in 30-Grad-Schritten":** Das Plan-Protokoll hat 10-Grad-Schritte mit 30-Grad-Auswerteraster (wie
   GFS1, fuer K0 und Teil B noetig); die woertliche Lesart (30-Grad-Schritte) lief daneben und traegt die
   Wortlaut-Urteile zu GF1. Begruendet im Plan vor dem Einfrieren. Beide geben 540 Grad.
3. **Codefehler vor dem Einfrieren:**
   - finn.gueltig_plan pruefte den Drehsinn auch bei 0 Grad (dort ist er 0) und erklaerte damit jeden Ast fuer
     ungueltig. Gefunden in Rauchlauf 1, korrigiert, in Rauchlauf 2 geprueft, im Plan vermerkt.
   - Die Absicherung "P10 oder P30 fehlt -> GF2 nicht auswertbar" habe ich nach dem Start von Rauchlauf 1 auf der .69
     per mv ersetzt; dessen Auswertung lief noch mit der alten Fassung. Geprueft in Rauchlauf 2.
4. **Kopfrechnung lokal:** Zeitbox (Restzeit und Endzeit), "8 von 50624", "E(60) passend zu 1/2" im Plan, die
   Umrechnung Sonde <-> Phasensprung (cos(omega/2)) in der Lesart oben und "jenseits von pi/2". jq lokal nur lesend
   und filternd (Auswahl, Vergleich), ohne Arithmetik. Die Vorgabe "lokal keine Rechnung" lege ich damit etwas weit aus.
5. **Werkzeuge:**
   - Lokal ausserhalb der Liste: date, ls, mkdir, cp, mv, cat, cd, Shell-Schleifen; im Monitor eine ssh-Schleife mit
     comm und sort. Kein lokaler Interpreter (kein python, awk, perl, node).
   - Auf der .69 ausserhalb des Starters: sha256sum, mkdir, mv, ls, cat, grep, tail, wc, test, jq (lesend, mit select
     und range), systemctl --user list-units, uptime, setsid, nohup, sleep-Warteschleifen in den Ketten. Kein Python
     ausserhalb von kleintest.sh; kein pkill, kein pgrep -f.
6. **Haengender ssh-Start:** Der Startaufruf der Hauptketten blieb haengen (die per && verkettete Hintergrundgruppe hielt
   den ssh-Kanal offen) und endete erst mit der cpu6-Kette um 19:50:01 UTC. Auf die Laeufe hatte das keine Wirkung (wie
   GFS1, Selbstanzeige 8).
7. **Rauchlauf-Dateien:** wahl.json, auswertung.json und die zwei Bilder aus Rauchlauf 1 hat Rauchlauf 2 auf der .69
   ueberschrieben; lokal liegen sie als *.rauch1, ohne Gegenpruefsumme.
8. **Hintergrundausgaben:** Das Werkzeug hat die Ausgaben meiner Hintergrundbefehle in seinen Sitzungsordner
   (/tmp/claude-1000/.../tasks/) geschrieben. In den Scratchpad der Leitung habe ich nichts geschrieben.
9. **Farbpruefung:** Den Paletten-Validator des dataviz-Skills (node) habe ich wegen des lokalen Interpreterverbots
   nicht gestartet; verwendet ist die dokumentierte, vorab gepruefte Referenzpalette (wie GFS1).
10. **Vor dem Einfrieren gelesen:** GFS1-Ergebnis und dessen prot.json (K0-Bezugswerte, Knotenzahlen von Z^3), beides
    veroeffentlicht und im Plan genannt.
11. Kein Journaleintrag, kein Peerbus, kein Commit; das liegt bei der Leitung.

## Kartenvorschlaege (hoechstens zwei)

1. **GUERTEL-FINN-NETZ-2 [H]: Haelt der Diamant-Ast zwischen 450 und 540 Grad?**
   - **Rechnung:** an 480 und 510 Grad lange FIRE-Relaxation (bis Konvergenz, hoechstens 3000) auf Diamant und Z^3,
     SO(3) und SO(2); dazu Stoesse wie hier bei 480 und 510 Grad.
   - **Vorhersage [H]:** Der Diamant springt schon bei 480 oder 510 Grad (Bindungen ueber pi/2), Z^3 nicht vor 540.
   - **Ableitbarkeit:** nicht ableitbar; Laufzeit unter 1 min je Lauf.
2. **GUERTEL-FINN-NETZ-GROESSE [H]:** dieselbe Rechnung auf Diamant-Kugeln (8, 16) und (16, 32), parallel zu
   GUERTEL-FELD-STAB-2. Vorhersage: GF2 haelt auf beiden, theta_max waechst mit der Kugel.

## Dateien

- **Plan:** PLAN.md, PLAN.md.eingefroren-20261004-214220, EINGEFROREN-SHA256.txt.
- **Code:** code/finn.py und code/auswertung_fn.py (neu); code/stab.py, code/guertel2.py, code/guertel.py (Kopien aus
  GFS1, Hashes wie dort); je mit .eingefroren-20261004-214220.
- **Ketten:** ketten/rauch-cpu6.sh, rauch-cpu7.sh, rauch2-cpu6.sh, lauf-cpu6.sh und lauf-cpu7.sh (die beiden letzten
  eingefroren).
- **Eingabe:** eingaben-gfs1/prot.json (Kopie aus GFS1 lauf-69, K0-Bezug).
- **Rauchlauf:** rauch-69/ (Protokolle bis 60 Grad, Stoesse, Wahl, Auswertung, Bilder, Logs, PRUEFSUMMEN-69-roh.txt).
- **Hauptlaeufe:** lauf-69/
  - prot-{diamant,z3}-{so3,so2}-d10.json und prot-{diamant,z3}-so3-d30.json, Zustaende als -zust.npz;
  - wahl.json; stoss-diamant-so3-T{420,450}-e{0.01,0.1,0.3,0}.json, Referenzen stoss-diamant-so3-T{300,270}-e0.json;
    stoss-diamant-so2-T{420,450}-e{0.01,0.1,0.3,0}.json, je mit -end.npz;
  - auswertung.json, energie-verlauf.png, vorwaertsast.png, Logs, kette-*.out, PRUEFSUMMEN-69-roh.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/guertel-finn-netz-1/ (code/, ketten/, rauch/, lauf/, eingaben-gfs1/).

## Einfach gesagt

Wir haben dasselbe Drehfeld wie vorher auf dem Wuerfelgitter jetzt auf Finns Tetraeder-Netz gesetzt, in dem jeder
Knoten nur vier Nachbarn hat. Dreht man die Mitte um 420 oder 450 Grad und stoesst das Feld leicht schraeg an, legt es
sich in allen sechs Faellen glatt in die kuerzere Gegendrehung um, ohne dass das Netz irgendwo reisst: Das ist der
Guertel-Trick, jetzt auch auf Finns Netz. Ein Feld, das sich nur in einer Ebene drehen kann, bleibt dagegen verdreht,
genau wie erwartet. Beim Weiterdrehen reisst Finns Netz erst bei 540 Grad, so spaet wie das Wuerfelgitter, obwohl seine
Verbindungen anders belastet werden. Es bleibt eine Modellrechnung auf einem einzigen Netz und kein Nachweis in der
Natur.
