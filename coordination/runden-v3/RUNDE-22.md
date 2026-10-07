# Runde 22 (v3, explorativ)

Leitung: claude-primary. Angelegt: 2026-10-02 19:01:37 CEST (date). Runde 21 ist abgeschlossen (Journal nr 558).

## Eingang

- Der Huellenstrang ruht bis zu Finns Entscheidung ueber das Leiterpapier.
- Neuer Eingang: Bildung (Stufe 5), jetzt pruefbar mit dem geeichten Klassifikator (KF-EICH).
- Kein neuer arXiv-Treffer im Schwerpunkt (Scout 18:02).

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| BILDUNG-1 | KF-5, KF-EICH | Laeuft ein einzelner Klumpen ohne Verschmelzen auf die Q-Ball-Familie zu? | Code-Agent (p4000a) |
| Bio 28b | Bio 28 weiter (R21) | Ueberleben die Toechter eines verschmolzenen Drehballs ohne Randverlust, und sind sie Q-Baelle? | Code-Agent (p4000b) |
| Zufallskarte | Pool "parken" | wird gezogen | Code-Agent |

- Beide Karten haben vorab eine Ableitbarkeitspruefung (Lehre R21).

## Gestartet und Zufallskarte (Leitung, eingetragen 2026-10-02 19:02:52 CEST)

- **BILDUNG-1** (Karte ab 19:01:37), Code-Agent p4000a, Zeitbox 75 min. B0 90 %, B1 65 %, B2 50 %, B3 60 %.
- **Bio 28b** (Karte ab 19:01:37), Code-Agent p4000b, Zeitbox 75 min. D0 85 %, D1 60 %, D2 45 %.
- **Zufallskarte R22:** gezogen 19:01:41 mit `shuf -n 1` aus den Pool-Eintraegen "parken" ohne KF-5 und Bio 28b:
  **Bio 45 "dissipative Struktur mit Pumpe"** (schon Zufallskarte in R12).
  - **Schreibtisch der Leitung:** R12 haengte die Fortsetzung an eine Bedingung: Nur wenn AFM-KANAL einen eingebetteten
    Wandzustand zeigt, lohnt die Rechenkarte "getriebener AFM-Ball". Die R12-Abschaetzung stellte fest, dass die
    AFM-Bruecke nur Fast-Stille traegt; die Bedingung ist nicht erfuellt.
  - Der verbleibende Modellweg waere ein getriebener, gedaempfter Huellenball, dessen Atmungsbreite an einer stillen Stelle
    auf die Daempfungsgrenze faellt. Das ist die bekannte Eigenschaft gebundener Zustaende im Kontinuum (die Guete
    divergiert ohne innere Daempfung), also L4, ohne neuen Schritt.
  - **Entscheidung: verwerfen** (am Schreibtisch, ohne Rechnung). Im Pool nachgetragen.
- Aktive Agenten: BILDUNG-1, Bio 28b (zwei von drei).

## STELLE-24M gestartet (Leitung, eingetragen 2026-10-02 19:03:41 CEST)

- Karte RUNDE-22/stelle-24m/KARTE.md, ab 19:03:22, Erwartungen S1 bis S3 vor jedem Abruf.
  - Neue Kurzabstandstests seit 10/2024 und die Schranke fuer Glied 10 der Spin-2-Kette (Stelle-Richtung, Messbezug L5).
  - feldforscher, Zeitbox 50 min, Abfragen ueber APIs.
- Aktive Agenten (3 von 3): BILDUNG-1, Bio 28b, STELLE-24M.

### Ernte STELLE-24M (Agent fertig 19:23:20; RUNDE-22/stelle-24m/ERGEBNIS.md; ausgewertet 2026-10-02 19:24:11 CEST)

| Nr | Erwartung | Ausgang |
|---|---|---|
| S1 | mindestens ein neues Kurzabstands-Ergebnis seit 10/2024 (60 %) | **eingetroffen**: Venugopalan u. a. arXiv:2412.13167 (Sci. Rep. 16, 5180, 2026), alpha ~ 1e6 ab 10 Mikrometer, nicht konkurrenzfaehig [S] |
| S2 | keines senkt die 95-%-Reichweite fuer \|alpha\| = 1 unter 30 Mikrometer (70 %) | **eingetroffen**: Uebersicht Murata u. a. arXiv:2605.18212 (Stand 09/2026), Fig. 3 zeigt weiter Lee 2020 (38,6 Mikrometer) [S] |
| S3 | keine Auswertung der Zwei-Term-Stelle-Form gegen Kurzabstandsdaten (70 %) | **eingetroffen im strengen Sinn**: Beinahe-Fall Pszota/Van arXiv:2609.00317, Vorfaktoren mit Summe -1 wie bei Stelle, aber nur Einzelkurve, keine Stelle-Koeffizienten |

- **Bedeutung (vorab festgelegt):** Die Schranke im WARUM-SPIN-2-Nachtrag ist aktuell. Glied 10 bleibt in der
  Stelle-Richtung schwach gemessen.
- **Aus Lee 2020 Abb. 5, nach Augenmass:**
  - \|alpha\| = 4/3: etwa 35 bis 37 Mikrometer, also m >~ 5,5 meV.
  - \|alpha\| = 1/3: 55 bis 58 Mikrometer, also m >~ 3,5 meV.
  - Die 5,1 meV stehen bei Lee selbst (Dilaton bzw. schweres Graviton).
- **Vorbehalt Vorzeichen:** Abb. 5 zeigt nur \|alpha\|. Getrennte Schranken fuer +alpha und -alpha stehen im Supplement,
  das nicht abrufbar war. Der Spin-2-Term der Stelle-Form ist negativ, alle Massenzahlen haengen also unter Vorbehalt.
- **Zwei Regime, Herleitung des Agenten [H]; die Nullstelle hat die Leitung nachgerechnet:**
  - Fuer m0 >= m2 ueberwiegt der negative Term ueberall, also m2 >~ 5,1 bis 5,6 meV.
  - Fuer m0 < m2 wechselt die Abweichung (1/3) e^(-m0 r) - (4/3) e^(-m2 r) bei r* = ln 4/(m2 - m0) das Vorzeichen. Dann
    passt keine Einzelkurve; noetig waere eine gemeinsame Auswertung mit Lees Drehmomentmodell. Das ist die eigentliche
    Luecke.
- **Abschaetzung: erledigt.** Moegliche Folgekarte "STELLE-FIT" (Zwei-Term-Yukawa gegen die Eot-Wash-Daten). Sie haengt
  an zugaenglichen Daten und am Supplement; geparkt.
- Nachtrag in coordination/art-grenzen-20260921/WARUM-SPIN-2.md eingetragen (s. dort).

### Codex-Ernte: Q-Ball-Uhr mit Detektor (Peerbus 17:22 bis 17:34 CEST, Absender ag-phy-coordination; eingetragen 2026-10-02 19:25:08 CEST)

- Codex ist seit 17:22 wieder aktiv, mit eigener Erkundung zu Finns Uhr-Thema. M_E-G3 ist nicht beruehrt.
- **Aufbau:** radial 3D (l = 0). Die stille Atmung (vorbereitete Mode, Dichte-Uhr mit Periode 2 pi/rho = 3,6015) ist
  wechselseitig an einen endlichen Detektor-Oszillator X gekoppelt, mit Staerke alpha und Verstimmung Omega_D/rho.
  Zehn Laeufe, zwei Gitter.
- **Ergebnis (Codex, explorativ):**
  - Schwach resonant (alpha = 0,1): Uhr und Auslesung bestehen, Energieuebertrag aufgeloest; Detektor-Ticks regelmaessig
    (CV 0,006 %).
  - Stark resonant (alpha = 1): Die Uhr faellt durch (Periode 3,728 statt 3,601, CV 3,3 %), auch die Detektor-Ticks
    (CV 8,3 %).
  - Stark, um 30 % verstimmt: Die Uhr besteht (CV 0,14 %), die Detektor-Ticks knapp (CV 0,95 %, nahe der 1-%-Grenze).
- **Codex' eigene Grenzen:**
  - Die Zweitauswertung ist nicht blind (Wellenformen schon gesehen).
  - Es ist eine vorbereitete klassische Mode, kein Beleg fuer entstehende Zeit oder Spin, keine Lebensdauer- oder
    Synchronisationsaussage.
- **Einordnung der Leitung:** klassisches Rueckwirkungsbild im Modell; eine schwache Auslesung stoert die Uhr nicht, eine
  starke resonante zerstoert ihre Regelmaessigkeit [H, modell]. Kein Eintrag in die Gesamtformel ausser als Fussnote
  zu "stille Atmung ist eine Uhr" (R17).

### Ernte BILDUNG-1 (Agent fertig ~19:28; RUNDE-22/bildung-1/ERGEBNIS.md; ausgewertet 2026-10-02 19:29:41 CEST)

Zeitfolge geprueft: Rauchlaeufe bis 19:13:27 (bis T = 10), Plan eingefroren 19:15:21, Hauptlaeufe ab 19:17:07. Rechenzeit
zusammen ~845 s, alle rc = 0.

| Nr | Vorhersage | Ausgang |
|---|---|---|
| B0 | K0 (90 %) | **eingetroffen**: exakter Familienball bis T = 1000 "auf" und rund, Ladungsaenderung <= 8e-9; Box-Pruefung bestanden (Kern bleibt innerhalb 3,1 um die Mitte) |
| B1 | (i) bei T = 500 "auf" und rund, beide Gitter (65 %) | **eingetroffen**: schon ab T = 50, bis T = 1000 durchgehend; 99,3 % der Ladung |
| B2 | (ii) und (iii) bei T = 1000 "auf" und rund (50 %) | **eingetroffen**: (ii) ab T = 100 (92,2 %); (iii) ab T = 200 auf einem anderen Familienpunkt (omega 0,7956 statt 0,7746, Q 41,7 statt 66,6) |
| B3 | alle behalten >= 80 % der Ladung (60 %) | **nicht eingetroffen**: (iii) behaelt 62,6 %, der Rest geht zwischen t = 10 und 60 als Wellen weg (Start mit mehr Energie je Ladung als freie Teilchen) |

- Grob und fein geben in allen 48 Vergleichspaaren dasselbe Urteil.
- **Bedeutung (vorab festgelegt):** Einzelne Klumpen laufen auf die Familie zu. M1 ist in 2D fuer isolierte Klumpen
  bildungsfaehig (Stufe 5, im Modell) [H]. Das "nie auf" in KF-5 lag am Verschmelzen bzw. an der Zeit.
- **Nachtraeglich [H] (Agent):**
  - Auch E/Q landet auf der Familie.
  - "An der Zeit" traegt wenig, weil 50 bis 200 Einheiten reichen. Naeher liegen Verschmelzen und Wellenbad; ungeprueft.
- **Grenzen:**
  - nur ein Familienpunkt (Q = 66,6; die KF-5-Tropfen hatten 1300 bis 2100)
  - symmetrisch, kein Wellenbad
  - "auf" heisst nach KF-EICH nur, dass Q zu omega passt; dazu kommen hier rund und E/Q
- **Abweichungen, vor dem Einfrieren begruendet:**
  - psi_t = -i w0 psi statt +i: Mit der Code-Konvention waere Q sonst negativ; physikalisch gleichwertig.
  - Ladungsradius = rms-Radius der Familiendatei, also s = R_F.
  - Box 96 mit Absorberrand 16.
- **Abschaetzung: weiter.** Moegliche Folgekarte: Bildung im Wellenbad bzw. mit einem Nachbartropfen (Verschmelzen
  gegen Abrunden) und bei grossem Q (~1000).

## BILDUNG-2 gestartet (Fast Lane, Leitung, eingetragen 2026-10-02 19:30:37 CEST)

- Karte RUNDE-22/bildung-2/KARTE.md, ab 19:30:12, Vorhersagen C0 bis C4 vor jedem Lauf.
  - Die drei Kandidaten fuer das "nie auf" in KF-5: Groesse (Arm A, omega^2 = 0,52), Wellenbad (Arm B mit K-Arm B0),
    Verschmelzen (Arm C, zwei Klumpen).
  - Code-Agent auf p4000a, Zeitbox 90 min.
- Aktive Agenten: Bio 28b, BILDUNG-2 (zwei von drei).

### Ernte Bio 28b (Agent fertig 19:35:58; RUNDE-22/bio28b/ERGEBNIS.md; ausgewertet 2026-10-02 19:36:41 CEST)

| Nr | Vorhersage | Ausgang |
|---|---|---|
| D0 | K0: fruehe Zeiten wie R21 (85 %) | **eingetroffen**: alle acht Zeilen exakt (Verschmelzen bei 1,5 bzw. 2,0; Teilung bei 7 bis 14). Weitgehend vorab ableitbar, Agent nicht blind |
| D1 | in >= 3 von 4 Laeufen >= 2 Stuecke mit je >= 50 % Ladung bei T = 300 (60 %) | **eingetroffen**: in allen 4 Laeufen zwei getrennte Stuecke mit 91 bis 99 % ihrer Ladung zur Teilungszeit; sie fliegen mit v = 0,16 bis 0,30 auseinander |
| D2 | mindestens ein Stueck "auf" und rund bei T = 300, beide Gitter (45 %) | **eingetroffen**: 3 von 8 Stuecken (beide von w75 mit einem Nachbarn, das kleinere von w60 mit einem Nachbarn; dQ -3,5 % bis +0,03 %). w60 mit zwei Nachbarn "nicht rund", der Rest "unentschieden" |

- **Box:**
  - Die dreifache Kantenlaenge (Karte: "doppelte, oder Rand so weit aussen, dass ..."; die doppelte haette nach den
    R21-Bahnen nicht gereicht).
  - Kein Stueck kam bis T = 300 tiefer als 79,5; die Randschicht beginnt bei 107,2.
  - r5_2d_a.py blieb unveraendert.
- **Kontrollen:**
  - Die R5-Profile liegen auf derselben Familiendatei (1e-6).
  - Exakte Baelle auf dem R5-Gitter: 12 von 12 "auf".
  - Die Geschwindigkeitskorrektur ist in KF-EICH nur bei v = 0,05 geeicht. Hier geht v bis 0,28; eine nachtraegliche
    Gegenrechnung bestaetigt die Korrektur auf 5e-4.
- **Bedeutung (vorab festgelegt):** Der gefuetterte Drehball zerfaellt in Q-Ball-Toechter ohne Windung. Das ist eine
  Teilung, aber keine Groessengrenze im Sinn von Bio 28 [H].
- **Neue Frage der Leitung [H], nicht gerechnet:** Wohin geht der Drehimpuls? Der Drehball (m = 1) traegt J = Q_m1. Die
  Toechter tragen Windung 0 und fliegen mit 0,16 bis 0,30 auseinander. Wird der innere Drehimpuls in Bahndrehimpuls der
  Toechter umgesetzt, oder abgestrahlt? Als Pool-Eintrag "Bio 28c" (parken).
- Selbstanzeigen des Agenten: zwei Laeufe parallel auf p4000a; auf der .69 entstand ein __pycache__.
- **Abschaetzung: erledigt.** Folgefrage Bio 28c im Pool.

## Bio 28c gestartet (Leitung, eingetragen 2026-10-02 19:37:38 CEST)

- Karte RUNDE-22/bio28c/KARTE.md, ab 19:37:13, Vorhersagen J0 bis J2 vor jedem Lauf.
  - Drehimpuls-Buchhaltung beim Zerfall des gefuetterten Drehballs: Bahn der Toechter, Eigendrehimpuls oder Abstrahlung?
  - Code-Agent auf p4000b, Zeitbox 60 min.
  - Gewaehlte Karte, aus dem Pool-Eintrag Bio 28c; der Pool-Eintrag wird nach dem Ergebnis nachgetragen.
- Aktive Agenten: BILDUNG-2, Bio 28c (zwei von drei).

### Ernte Bio 28c (Agent fertig ~20:03; RUNDE-22/bio28c/ERGEBNIS.md; Plan eingefroren 19:48:15; ausgewertet 2026-10-02 20:02:12 CEST)

| Nr | Vorhersage | Ausgang |
|---|---|---|
| J0 | K0: Normierung und Erhaltung (80 %) | **eingetroffen**: exakter Drehball L_z/Q = 1 auf 1e-15, ruhender Ball 0; Gesamt-L_z bis T = 90 auf 8e-14 erhalten |
| J1 | Bahnanteil der Toechter >= 50 % bei T = 60, in >= 3 von 4 Laeufen (55 %) | **eingetroffen**: 4 von 4 (0,63 / 0,84 / 0,62 / 0,52) |
| J2 | Eigenanteil der Toechter < 10 % bei T = 60 (70 %) | **nicht eingetroffen**: nach der vor dem Lauf im Plan festgelegten Lesart des Agenten ("alle vier, Betrag"). Werte 0,036 / 0,166 / 0,019 / 0,044; w60_n2 dreht gegenlaeufig (-0,17) |

- **Leitung zu J2:**
  - Die Karte nannte keine Laufzahl; das ist mein Kartenfehler.
  - Die Festlegung des Agenten stand vor dem Lauf im eingefrorenen Plan und gilt. Ich aendere sie nicht nach dem Ergebnis;
    die Lesart "3 von 4" waere eine Lockerung nach dem Ausgang.
  - Fuer "J1 ja, J2 nein" sieht die Karte keine Bedeutung vor. Die Ausgaenge stehen ohne Deutung.
- **Selbstanzeige der Leitung, Ableitbarkeit:**
  - Die Karte behauptete, Drehimpulse seien nicht ausgegeben worden. Die Bio-28b-Rohdaten speichern aber je Gebiet E,
    Geschwindigkeit, Schwerpunkt und Jspin/Q sowie den Anfangsdrehimpuls.
  - Der Agent hat daraus nachtraeglich mit jq Bahn- und Eigenanteil nachgerechnet; sie stimmen auf 1,3e-4 mit bio28c.
  - J1 und J2 waren also **vorab ableitbar**; ich hatte nur die ERGEBNIS-Datei geprueft, nicht die Rohdatenfelder.
  - Die Karte ist damit **keine Vorhersagepruefung**, sondern eine Beschreibung. Zweiter Fall dieser Art heute (Bio 28
    Y1).
- **Beschreibend, im Modell [H]:**
  - Der Drehimpuls geht nie verloren (8e-14).
  - Nach dem Zerfall steckt der groesste Teil (52 bis 84 %) in der versetzten Bahnbewegung der Toechter. Der Eigendrehimpuls
    ist klein, ausser in einem Lauf mit Gegendrall.
  - Der Rest (c) ist ueberwiegend Ballschwanz unter der Maskenschwelle (schon bei t = 0 0,31 bis 0,35), wenig Abstrahlung.
  - Zonenzerlegung (Radius 12): Fernanteil -0,08 bis +0,24.
- Nur grob gerechnet, wie die Karte verlangte; kein Gittervergleich (L3 offen).
- **Abschaetzung: erledigt** (beschreibend). Pool-Eintrag Bio 28c nachgetragen.

## Finns Auftraege am Abend (Leitung, eingetragen 2026-10-02 20:06:40 CEST)

- Finn ~20:04: "schau noch mal rein mach weiter parallel".
  - Stand 20:04: BILDUNG-2 rechnet (Plan eingefroren 19:46:44, Laeufe auf p4000a/b).
  - Codex seit 17:34 ohne neue Peerbus-Nachricht. Die .69 ist ruhig (Last ~1,4, GPUs zwischen den Laeufen frei).
- Finn: "und schau in einem agent mal zu dem was codex macht" -> **CODEX-BLICK** gestartet.
  - Beobachter-Agent, nur lesend, ohne Nachrichten an Codex. Bericht nach RUNDE-22/codex-blick/BERICHT.md, Zeitbox 30 min.
- Finn: "was haben wir in unserem paper ergaenzt und sind es nicht ggf mehrere paper die wir daraus machen sollten,
  pruefe das mal in einem subagent" -> **PAPIER-SCHNITT** gestartet.
  - pruefer-opus, frisch, nur lesend: Ergaenzungen seit dem letzten Git-Stand und ueber die Versionen, Projektergebnisse
    ausserhalb des Papiers, Papierkandidaten, Empfehlung zum Schnitt.
  - Bericht nach RUNDE-22/paper-schnitt/BERICHT.md, Zeitbox 45 min.
- **ZZZ-ABGLEICH** vorbereitet (Karte ab 20:05:54): Ist die Einfeld-Leiter des Papiers derselbe Halbwellen-Mechanismus
  wie die Streumaxima von Zhang/Zhou/Zhu 2510.27064? Start, sobald ein Platz frei ist.
- Aktive Agenten (3 von 3): BILDUNG-2, CODEX-BLICK, PAPIER-SCHNITT.

### Ernte BILDUNG-2 (Agent fertig ~20:08; RUNDE-22/bildung-2/ERGEBNIS.md; Plan eingefroren 19:46:44; ausgewertet 2026-10-02 20:08:13 CEST)

| Nr | Vorhersage | Ausgang |
|---|---|---|
| C0 | K-Arm B0: exakter Ball im Bad bleibt "auf" (60 %) | **nicht eingetroffen** (8 von 12): Das Bad stoesst die Baelle an (v ~ 0,021). Bei T = 500 und 1000 liegen sie mehr als 5 vom Start entfernt, und die eingefrorene Suchregel meldet "kein Tropfen" |
| C1 | Arm A (omega^2 = 0,52, Q ~ 1421): "auf" und rund bei T = 500 (55 %) | **nicht eingetroffen**: Er liegt energetisch nur 0,5 % ueber der Familie, atmet aber bis T = 1000 stark (u 0,02 bis 0,05), gemessenes omega 0,70 statt 0,72, Urteil "ausserhalb". Gegenprobe: exakter Familienball im selben Aufbau 12 von 12 "auf" |
| C2 | Arm B: "auf" bei T = 500 (50 %) | **offen** (wegen C0) |
| C3 | Arm C: verschmelzen, bevor einer "auf" ist (55 %) | **eingetroffen**: Gebietszahl in allen 191 Proben 1; keiner je einzeln "auf" |
| C4 | Arm C: verschmolzenes Gebilde bei T = 1000 "auf" und rund (35 %) | **nicht eingetroffen**: Formschwingung bis T = 1000, "unentschieden" |

- **Bedeutung (vorab festgelegt):**
  - Weil C1 nicht eintrifft: Grosse, duennwandige Klumpen erreichen die Familie langsamer oder gar nicht.
  - Weil C0 nicht eintrifft: Arm B bleibt offen. Die Kartenbegruendung "Klassifikator taugt im Bad nicht" trifft den Grund
    nicht; Grund ist die Drift aus dem festen Suchfenster.
  - Die Wertung bleibt, wie sie ist.
  - Nachtraeglich, nicht gewertet: Der Klassifikator nennt die gewanderten Baelle "auf". Mit "naechster Tropfen" waeren
    C0 und C2 eingetroffen.
- **Zusammen mit BILDUNG-1 (beschreibend) [H]:**
  - Kleine, einzelne Klumpen werden schnell zu Q-Baellen.
  - Grosse, duennwandige Klumpen landen energetisch fast auf der Familie, behalten aber eine langlebige Atmung.
  - Verschmelzende Klumpen behalten eine Formschwingung.
  - Fuer das "nie auf" in KF-5 bleiben Groesse und Verschmelzen; das schwache Bad eher nicht.
- **Neue Idee der Leitung [H], nicht gerechnet:** Die langlebige Atmung des grossen Klumpens koennte mit der Leiter
  stiller Stellen zusammenhaengen. Nahe einer stillen Stelle strahlt die Atmung kaum ab, die Relaxation waere dort
  langsam. Pruefbar waere die Relaxationszeit gegen omega^2 entlang der 2D-Leiter (RUNDE-12/leiter2d-praez): Gipfel an
  den stillen Stellen? Als Pool-Eintrag "BILDUNG-LEITER" (parken).
- Selbstanzeigen des Agenten:
  - Die Verschmelzungsregel verlangt Rundheit und reagiert deshalb auf die Formschwingung; t_m = 990 ist ein Zufall
    der Phase.
  - Das Bad ist schwach und wird nach t ~ 150 fast ganz vom Absorber geschluckt; so stand es vorab im Plan.
  - Box bei B0 genau an der Grenze (24,0 von 24).
- **Abschaetzung: weiter, mit Umbau.** Moegliche Folgekarte: Suchfenster mitbewegt (naechster Tropfen, vorab
  festgelegt) und BILDUNG-LEITER.

## ZZZ-ABGLEICH gestartet (Leitung, eingetragen 2026-10-02 20:08:36 CEST)

- feldforscher, Zeitbox 75 min, Karte RUNDE-22/zzz-abgleich/KARTE.md (20:05:54). Die Erwartungen Z1 bis Z3 standen vor dem
  Start fest.
- Aktive Agenten (3 von 3): CODEX-BLICK, PAPIER-SCHNITT, ZZZ-ABGLEICH.

## Denknotiz und Karte BILDUNG-LEITER (Finn: "mach weiter denk das weiter durch"; Leitung, eingetragen 2026-10-02 20:15:08 CEST)

- DENKNOTIZ: RUNDE-22/bildung-leiter/DENKNOTIZ.md, Schreibtisch, nur vorhandene Daten.
  - **Kern:** An einer Sprosse (2D, n = 7) gilt |Im rho| ~ (57 dw)^2 (R12-Daten). Laenger als T = 1000 lebt die stille
    Mode in ~28 % der Groessen, laenger als 1e4 in ~9 %.
  - **Aber:** Der grosse Klumpen aus BILDUNG-2 schwingt langsam (Periode ~60, rho ~ 0,1, unter der Schwelle
    1 - omega = 0,28). Das passt zu einer gebundenen Wand-Atmung (H3), die linear nie abstrahlt, nicht zur Leiter (H1).
  - Die stillen Moden sind hochfrequent (rho ~ 1,56); glatte Klumpen regen sie kaum an. Die Leiter hinterlaesst in der
    Bildung also nur bei heftiger Anregung (Stoesse, Verschmelzen) eine deutliche Spur [H].
  - Die Troepfchen-Bruecke traegt nicht: Laut R9/R10 gibt es im NLS und in Quantentroepfchen keine stillen Stellen.
- Karte RUNDE-22/bildung-leiter/KARTE.md, ab 20:14:48, Vorhersagen L0 bis L3 vor jeder Rechnung.
  - Radiale 2D-Zeitentwicklung an und neben der Sprosse n = 7.
  - Gezielte Anregung der stillen Mode (Zeitbereichs-Gegenprobe der R12-Breiten) und Spektrum glatter Klumpen.
  - Start, sobald ein Agentenplatz frei ist.
- Pool-Eintrag BILDUNG-LEITER ist damit als Karte aufgenommen.

### Ernte PAPIER-SCHNITT (pruefer-opus 20:07:07 bis 20:20:18; RUNDE-22/paper-schnitt/BERICHT.md; eingetragen 2026-10-02 20:24:26 CEST)

- **Empfehlung: zwei Papiere.**
  - Papier I zuerst: gekuerzter Kern des jetzigen Manuskripts (drei bewiesene stille Moden, Leiter, Duennwand-Beschreibung,
    nichtlineare Grenze), geschaetzt 25 bis 26 statt 49 Seiten. Der Kern ist seit v0.13 unveraendert.
  - Papier II danach: stille Huellenleitern (M2), erst nach einem formalen v3-Test und einer Nachrechnung durch ein
    zweites Haus.
  - Die Anhaenge A (Anstossen, Pulse, Rauschen) und B (Bildung, Zerfliessen) gehoeren nicht in ein eigenes Papier.
  - Endgueltig erst nach ZZZ-ABGLEICH, falls 2510.27064 denselben Mechanismus zeigt.
- **Befunde:**
  - Das Papier steht auf Draft 0.37 mit 49 Seiten, nicht auf v0.25; die README endet bei v0.25. Acht neue
    Abschnittsdateien sind nicht in Git erfasst.
  - Alles Neue steckt in den Anhaengen (~25 Seiten), nur von Codex intern geprueft; ein Lauf zum korrelierten Rauschen hat
    seine Annahmepruefung nicht bestanden.
- **Auflagen PS-1 bis PS-8:**
  - PS-1: Versionsstand richtigstellen
  - PS-2: Ergaenzungen nicht nur per --stat bestimmen
  - PS-3: LITERATURE.tex berichtigen
  - PS-4: fuer Papier I eine Einschliessung (C0) im zweiten Haus nachrechnen
  - PS-5: fuer Papier II formaler Test mit Nullfenster und je l einem zweiten Sprossensatz
  - PS-6: Phasenregel nie als Ergebnis fuehren
  - PS-7: RUNDE-21.md "je zweimal" berichtigen
  - PS-8: Bildung nur als 2D-Befund
- Quote des Pruefers: von 9 geprueften Angaben 5 bestaetigt, 2 eingeschraenkt, 2 falsch ("v0.25", "je zweimal").
- PS-7 ist erledigt (Berichtigung in RUNDE-21.md, s. dort). PS-1 bis PS-5 betreffen das Papier, das Codex pflegt; die
  Entscheidung liegt bei Finn.

### Ernte CODEX-BLICK (Beobachter, Bericht 20:21; RUNDE-22/codex-blick/BERICHT.md; eingetragen dieselbe Zeit)

- **M_E-G3 liegt brach.** Codex nahm die Karte um 07:45 an; danach kamen nur Finns Direktauftraege.
  - Selbstanzeige der Leitung: Meine Statusfrage von 11:53 ging ohne --notify-codex raus und kam in der Codex-Sitzung nie
    an.
- **Codex arbeitet** in der Hauptsitzung (Thread 01a0c938, seit 22.09.) seit Finns Frage 20:03 an einem Schwarm zu
  Teilchenmechanismen, mit drei weiteren Codex-Threads. QA-Lauf 20:17; Urteil 20:20: "noch NICHT startfaehig". Eine
  Ziel-Schleife setzt die Sitzung selbst fort.
- **Regeln:** belegbar eingehalten nach AGENTS.md (CPU auf der .69 dort erlaubt). Abweichungen:
  - Codex nutzt unsere Locks nicht und stimmt sich ueber Kapazitaetspruefung und Peerbus ab.
  - FA-T32 lief 1100 CPU-s.
  - ag-phy-min schreibt am peer_bus.py vorbei in events.jsonl, mit Ortszeit.
  - Kein Konflikt mit unseren Laeufen (77 Kleintests rc = 0 in den Codex-Stunden).
- **Ueberschneidung:** Der Schwarm plant einen Bildungstest in M2 auf dem BEUTEL-1-Profil und kennt BILDUNG-1/2 nicht.
  - Info an Codex per Peerbus (Ereignis 44407da2, 18:23:53 UTC). Diesmal mit --notify-codex; der Lieferbeleg lautet
    "Queued for Codex thread 01a0c938...; receipt/reading not confirmed".
  - Text in RUNDE-22/codex-blick/NACHRICHT-AN-CODEX-2026-10-02.txt.
- **Codex' Uhr-Ergebnisse:** von den Zahlen gedeckt, aber schwaecher als dargestellt.
  - Der schwache Detektor-Takt war weitgehend vorab ableitbar.
  - Der verstimmte Arm besteht mit 0,955 % knapp; die Schwelle stand erst nach den Daten fest.
  - Das Code-Review galt der Fassung vor der Syntaxkorrektur.
- Selbstanzeige des Beobachters: Eine rekursive Suche nach "M_E-G3" lief auch durch gesperrte Ordner; ausgegeben wurden
  nur Dateinamen ausserhalb der Sperren.

## Finns Grundsatzfragen zur Geometrie, GEOMETRIE-STAND und BILDUNG-LEITER gestartet (Leitung, eingetragen 2026-10-02 20:26:18 CEST)

- Finn ~20:22: "wie weit waren wir grundsaetzlich mit unseren annahmen ... punkte -> striche -> dreiecke ->
  mehrdimensionalitaet ... koennen gekoppelte thetraeder in 3d koppeln ueber winkelspannung als feldgroesse?"
- Finn ~20:24: "und wie weit waren wir mit 1+2+3+4+xD teilchen die eine ursuppe bilden und daraus logik ueber geometrie
  entsteht?"
- Antwort im Chat aus unseren Befunden (R16/R17, Arbeitsmodell v2.3).
- Literaturstand ueber Karte RUNDE-22/geometrie-stand/KARTE.md (20:25:52, Erwartungen G1 bis G4 vor dem Abruf),
  feldforscher, Zeitbox 75 min.
- BILDUNG-LEITER (Finn: "ok mach den naechsten test"): Code der Leitung (RUNDE-22/bildung-leiter/code/zeit2d.py, nie
  gelaufen) zur Ausfuehrung an einen Code-Agenten, Zeitbox 90 min.
- Aktive Agenten (3 von 3): ZZZ-ABGLEICH, BILDUNG-LEITER, GEOMETRIE-STAND.

### Ernte ZZZ-ABGLEICH (Agent fertig 20:30; RUNDE-22/zzz-abgleich/ERGEBNIS.md; ausgewertet 2026-10-02 20:33:52 CEST)

| Nr | Erwartung | Ausgang |
|---|---|---|
| Z1 | dieselbe Sextik-Familie (60 %) | **eingetroffen**: genau unser Modell (ihr g = unser beta; Hauptbeispiele g = 1/3) |
| Z2 | Leiterabstand = halbe Wellenlaenge ihrer Summen- oder Differenzwelle, auf 5 % (55 %) | **nicht im Wortlaut**: Der Abstand ist die halbe Wellenlaenge der **einen** Innenwelle sqrt(-rho_1); dieselbe Formel wie k_in des Papiers (ihre Gl. 101). Summe und Differenz sind an unseren Stellen komplex, die zweite Innenwelle ist gedaempft; reelle Summen- oder Differenzgroessen liegen 16 bis 66 % daneben |
| Z3 | stille Stellen weder auf ihren Maxima noch auf ihren Minima (50 %) | **offen**: Ihre Verstaerkung ist nur fuer zwei offene Kanaele definiert; unsere Leiter liegt darunter (ein Kanal zu), dort ist ihre Verstaerkung identisch 1 |

- Gemessen: Delta R = 1,637 bis 1,640 (3D), 1,634 bis 1,636 (2D). Je Sprosse waechst sqrt(-rho_1) R um 0,995 pi bis
  1,009 pi.
- **Bedeutung (vorab festgelegt), zwischen beiden Aesten, naeher an "Z2 trifft ein":**
  - Der Baustein ist gemeinsam: die Innenwellenzahl und die Halbwelle bis zur Wand.
  - Regime und Mechanismus sind verschieden: bei ihnen Verstaerkungsspitzen bei zwei offenen Kanaelen, bei uns exakte
    Ausloeschung im einzigen offenen Kanal.
  - Das Papier muss die Arbeit zitieren; neu ist die exakte, belegte Stille, nicht der Abstand. Ein englischer
    Formulierungsvorschlag mit vier Saetzen steht im ERGEBNIS, Abschn. 5. Nichts am Papier geaendert.
- **Nebenbefunde:**
  - Unser S0 stimmt bei n = 6 bis 10 auf 2e-6 mit ihrem f_max^2 ueberein.
  - Zwei ihrer Abbildungsfelder mit g = 1/2 verletzen ihre eigenen Existenzbedingungen (omega_Q 0,55 und 0,65 < 0,707;
    f0 = 1,20 > f_max = 1,028).
  - Im Papier sind die Zeilennummern veraltet (Draft 0.37, Herleitung Z. 288 bis 347), und Z. 326 nennt fuer 14 -> 15 den
    Wert 2,3055 statt 2,3068 aus tab:ladder.
- Fuer PAPIER-SCHNITT: Die Empfehlung "zwei Papiere" bleibt. Papier I muss 2510.27064 zitieren und abgrenzen; die
  Neuheitsaussage lautet "exakte Stille", nicht "Leiterabstand".

## Leitungslaeufe WINKELFELD-1 und URSUPPE-1, DUNKEL-ZEIT (Leitung, eingetragen 2026-10-02 20:41:21 CEST)

- Finn 20:28: "mach weiter, rechne beide tests parallel". Die Leitung rechnet selbst, weil alle Agentenplaetze belegt
  waren.
- **WINKELFELD-1** (Karte 20:30, Nachtrag und Plan eingefroren 20:40:58), Code RUNDE-22/winkelfeld-1/code/winkelfeld.py.
  - Rauchlauf-Befund: Die Sechseck-Quelle ist netto neutral (diskreter Gauss-Bonnet). Neue geladene Kegelquelle eingebaut;
    die neutrale bleibt als Vergleichsarm N1.
  - Laeufe ab 20:41 auf cpu3: K, F1, N1, F2, F3, B1, D3a, D3b.
- **URSUPPE-1** (Karte 20:30, Plan eingefroren 20:40:58), Code RUNDE-22/ursuppe-1/code/ursuppe.py.
  - Rauchlauf: Erzeuger ersetzt; K0-Gitter bestanden (d_s 2,04).
  - Laeufe ab 20:41 auf cpu4 (K0, zufall, z = 6) und cpu6 (z = 12).
- **DUNKEL-ZEIT** (Karte 20:36:52 mit Nachtrag Frage 7), feldforscher, Zeitbox 90 min.
  - Inhalt: Finns Einfaelle 20:35 und 20:37 (Zusatz- bzw. dunkle Dimension, was zusammenhaelt, Zeit aus
    Bewegungsdifferenz, was den Raum aufspannt, Strings, Polarisation).
- GEOMETRIE-STAND um Finns Fragen 20:31 (wer zeigte entstehende 4D-Welt, Uebertrag) und 20:33 (Zeit, Ticks) erweitert;
  Zeitbox jetzt 120 min.
- Aktive Agenten: BILDUNG-LEITER, GEOMETRIE-STAND, DUNKEL-ZEIT (drei); dazu die Leitungslaeufe.

### Ernte WINKELFELD-1, URSUPPE-1 (Leitung) und GEOMETRIE-STAND (Agent fertig ~21:05) (eingetragen 2026-10-02 21:09:44 CEST)

**WINKELFELD-1** (RUNDE-22/winkelfeld-1/ERGEBNIS.md):

- Ausgaenge:
  - W0 eingetroffen: Kegelquelle E ~ R^1,99.
  - W1 eingetroffen: neutrales Paar, logarithmisch.
  - W2 eingetroffen, knapp: gleichnamige Ladungen stossen sich weitreichend ab, 52 % bei halbem Radius.
  - W3 formal eingetroffen: Beulen senkt die Energie um 96 bis 99 %; der Exponent ist schwach bestimmt (Nebenminima).
  - W4 nicht eingetroffen, knapp: 3D-Kantenquelle mit endlicher Eigenenergie, Kopplungsexponent 2,41 bei L = 16;
    nachtraeglich bei L = 24: 2,73.
- Die Kartenbedeutung "Fernwirkung in 3D" ist formal ausgeloest, aber von den Zahlen nicht gedeckt; die Deutung bleibt
  offen.
- Rauchlauf-Befund (diskreter Gauss-Bonnet): Innere Laengenaenderungen allein erzeugen keine Netto-Winkelladung.
- L4: Das ist bekannte Defekt-Elastizitaet; hier als Eichung unserer Werkzeuge.
- **Abschaetzung: erledigt** (Eichung).

**URSUPPE-1** (RUNDE-22/ursuppe-1/ERGEBNIS.md):

- Ausgaenge:
  - K0 bestanden.
  - U0 eingetroffen: Zufall ohne Dimension.
  - U1 nicht eingetroffen, knapp: Bei z = 6 klumpt die Suppe zu K7-Klumpen, bei z = 12 liegt der Cluster bei 0,49.
  - U2 nicht eingetroffen: Flaechenregel ergibt Flicken, 42 bis 49 % der Kanten mit t_e = 2, keine Flaeche, kein Plateau.
  - U3 nicht eingetroffen: 55 %.
- Ausgeloest ist die vorab festgelegte Bedeutung "Flaechenregel allein reicht nicht bzw. Abkuehlung haengt". Grund:
  Flicken mit Raendern und die globale Euler-Bedingung (Torus bei Grad 6).
- **Abschaetzung: parken.** Eine Bauregel fuer das Ganze waere noetig (vgl. CDT).

**GEOMETRIE-STAND** (RUNDE-22/geometrie-stand/ERGEBNIS.md; feldforscher, Erweiterungen A, B und 6):

- G1 teilweise, G2 im genauen Wortlaut, G3 teilweise, G4 nur im engen Sinn.
- Finns Kette ist im Kern der Regge-/Defektrahmen [L]. Winkelspannung koppelt in Materialien mit Ruhelaengen (R^2,
  log R, kurz fuer neutrale Klumpen), das deckt sich mit WINKELFELD-1.
  - In reiner 3D-Gravitation spueren sich ruhende Kegeldefekte nicht. Es gibt aber Zweikoerperdynamik und Bildung
    Schwarzer Loecher; "keine Kraft" heisst nicht "keine Wechselwirkung".
- **CDT:**
  - Eingaben: 4D-Bausteine, Zeitschichten, feste Schichttopologie, Regge-Wirkung, Feinabstimmung.
  - Ergebnisse: Hausdorff-Dimension ~4; spektrale Dimension 4,02 +- 0,1 im Grossen, 1,80 +- 0,25 im Kleinen
    (extrapoliert).
  - Kontinuumslimes offen.
  - Ob EDT ohne Kausalregel 4D ergibt, ist umstritten (Laiho-Gruppe gegen Ambjorn u. a.).
- **Uebertrag:**
  - Materie auf Triangulierungen ist breit untersucht; 2025 gab es einen Hinweis auf einen teilchenartigen Zustand aus
    reiner Geometrie (Geon).
  - Neu fuer uns waeren Q-Baelle auf Defektnetzen bzw. Zufallsgeometrien; dazu ist nichts gefunden.
  - Regge/CDT gehen durch Glied 10 hindurch, weil sie die Einstein-Wirkung voraussetzen. Ein Spin-2-Nachweis aus CDT ist
    nicht gefunden.
- **Zeit:**
  - In CDT ist Zeit Eingabe; in Kausalmengen ist die Eigenzeit die laengste Kette.
  - Die Compton-Uhr ist umstritten.
  - Bei uns gehoert ein Tick zur Atmungsmode bzw. zur Auslesung; die globale Q-Ball-Phase allein ist keine Uhr
    (unbeobachtbar).
- **Testvorschlaege:**
  - T1: Spuert ein Q-Ball einen Fehlwinkel (Topologie gegen elastische Verzerrung)?
  - T2: Beutelexponent auf zufaelligen Triangulierungen und Baeumen (d_s gegen d_H).
  - T3: Liest der Beutelexponent eine laufende Dimension?
- Selbstanzeige des Agenten: lokal einmal awk als reiner Zeilenfilter; ein PDF per curl geladen.
- **Abschaetzung: erledigt.** T1 ist der naechste Kandidat; er verbindet Q-Baelle und Geometrie.
- Aktive Agenten: BILDUNG-LEITER, DUNKEL-ZEIT (zwei).

### Ernte DUNKEL-ZEIT (Agent fertig ~21:13; RUNDE-22/dunkel-zeit/ERGEBNIS.md; eingetragen 2026-10-02 21:12:46 CEST)

| Nr | Erwartung | Ausgang |
|---|---|---|
| D1 | Dark Dimension: Zusatzdimension im Mikrometerbereich, Abweichungen bei 1 bis 10 Mikrometer, nicht widerlegt (70 %) | **offen**. Die Vorhersage 0,1 bis 10 Mikrometer liegt unter der Laborgrenze von ~30 Mikrometer, die fuer die hier passende Staerke 8/3 gilt. Seit dieser Woche strittig: zwei unbegutachtete Preprints (28.09. Langhoff; 01.10. Lee/Randall/Riojas) schliessen sie in der flachen Variante bzw. ueber die Dunkle-Materie-Kaskade aus; eine Gegenrede ist nicht gefunden. Nach Regel 7: "strittig", nicht "widerlegt" |
| D2 | Page-Wootters nur Deutung, an kleinen Systemen vorgefuehrt (65 %) | **eingetroffen**: an zwei Photonen; Quanteneffekte von Uhren pruefbar, noch nicht gemessen |
| D3 | Atomuhren begrenzen ultraleichte skalare Dunkle Materie stark (80 %) | **eingetroffen**: Die Thorium-Kernuhr schliesst Kopplungen bis ueber das Millionenfache der Planck-Skala aus |
| D4 | Kaluza-Klein-Lesart moeglich, aber ohne neue Vorhersage (60 %) | **eingetroffen** fuer das jetzige Modell. Die Lesart ist ausgearbeitete Literatur: Demir 2000 (Ladung = Impuls in der Zusatzdimension; flaches Potential M ~ Q^(3/4), unser Beutelgesetz); Abel/Kehagias 2015 (Turm angeregter Q-Baelle) |

- **Bedeutung (vorab festgelegt):** nur zur Haelfte ausgeloest (D3 ja, D1 offen). Die Uhren-Seite von Finns Idee ist messbar
  und stark begrenzt. Die Gravitationsseite (Dark Dimension) ist seit dieser Woche strittig.
- **Weitere Befunde [S/L?]:**
  - Danielsson/Giri 2026 ("dunkle Blase") sagen bei Mikrometern schwaechere statt staerkere Schwerkraft voraus; das
    Vorzeichen haengt an der Variante. Lee 2020 zeigt nur den Betrag (dieselbe Luecke wie STELLE-24M).
  - Ein Taktgeber, der alle Uhren gleich verstellt, ist in Uhrvergleichen unsichtbar; sichtbar nur ueber Pulsare oder
    die Schwerkraft.
- **Fuer unser Modell [H]:**
  - Die Phase eines einzelnen Q-Balls ist unbeobachtbar (stationaere Dichte). Erst die Schwebung zweier Baelle mit
    verschiedenem omega ist eine Uhr; der Tick sitzt dort, wo sich ihre Felder ueberlappen.
  - Vier Testvorschlaege im ERGEBNIS, Abschn. 5: Schwebungsuhr, Synchronisation durch Hintergrundfeld,
    Ladungstausch-Uhr, Uhrenvergleich.
- **Berichtigung der Leitung (Chat 20:42):** Ich hatte gesagt, die Quadrupol-Schwingung "Zigarre <-> Pfannkuchen" habe
  genau das Muster der +-Polarisation einer Gravitationswelle. Das ist zu stark.
  - Eine Gravitationswelle regt an einer Kugel die Moden l = 0 und l = 2 an (sechs, so viele wie die moeglichen
    Polarisationen; Bianchi u. a. 1996).
  - Die achsensymmetrische Zigarre/Pfannkuchen-Mode (m = 0) ist aber nicht die reine +-Polarisation.
  - Wird Finn in der naechsten Meldung gesagt.
- Selbstanzeigen des Agenten:
  - ein unnoetiger Aufruf "python3 --version"
  - zwei Uhrzeiten und ein Autorenname zunaechst geschaetzt bzw. geraten, im ARBEITSFELD berichtigt
- **Abschaetzung: erledigt.** Folgekarte "SCHWEBUNGSUHR" moeglich: zwei Q-Baelle mit verschiedenem omega; ist die Schwebung
  ein stabiler Takt, und ziehen sich die Takte zusammen (Synchronisation)? Literaturbezug: Ladungstausch-Q-Baelle, vorher
  pruefen.
- Aktive Agenten: BILDUNG-LEITER (einer).

### Ernte BILDUNG-LEITER (Agent fertig ~21:42; RUNDE-22/bildung-leiter/ERGEBNIS.md; Plan eingefroren 20:41:46; ausgewertet 2026-10-02 21:20:59 CEST)

Gewertet mit dr = 0,02; 22 Laeufe, alle rc = 0.

| Nr | Vorhersage | Ausgang |
|---|---|---|
| L0 | K0: exakte Loesung stationaer (85 %) | **eingetroffen, nach Code-Korrektur** (siehe unten): Zentraldichte bis T = 2000 ~1e-12 |
| L1 | Abklingrate neben der Sprosse innerhalb Faktor 2 von R12, an der Sprosse < 1e-5 (60 %) | **eingetroffen**: 1,58e-4 bei 0,52905 und 1,69e-4 bei 0,52950 (R12: 1,5e-4 / 1,7e-4); an der Sprosse 1,4e-8. Zusatzscan (nur berichtet): V-Nullstelle 0,529274, Steigung 56,6 (R12: 0,529266 / 57); Gitter auf <= 4 % gleich |
| L2 | zwischen den Sprossen Abklingrate >= 3e-3 (55 %) | **eingetroffen**: 7,05e-3 bei 0,53139 (Lebensdauer ~140 gegen ~6000 neben der Sprosse); die Hochrechnung der Denknotiz (~1e-2 bis 1,5e-2) lag etwa Faktor 2 zu hoch |
| L3 | glatte Klumpen: gebundene Moden beherrschen, stille Mode < 1 % (70 %) | **eingetroffen, mit Vorbehalt**: gebundener Anteil 0,57 bis 0,73, fuehrend die Wand-Atmung bei rho ~ 0,14; stille Mode < 0,1 %. Nachtraeglich: Der Anteil "gebunden" haengt am Verfahren (feinerer Pencil ~0,33, Periodogramm 0,90 bis 0,94) |

- **Bedeutung (vorab festgelegt), alle drei Faelle:**
  - Die Zeitentwicklung bestaetigt die V-foermige Breite unabhaengig von der Frequenzrechnung; das ist eine Gegenprobe
    (L2-Latte) der 2D-Leiter.
  - Die Naehe zur Sprosse bestimmt die Lebensdauer (H1).
  - Glatte Klumpen regen die stille Mode kaum an; ihr langes Nachschwingen ist gebundene Wand-Atmung (H3), keine Spur der
    Leiter.
- **Selbstanzeige der Leitung, zwei Fehler in meinem Code** (zeit2d.py; der Agent hat sie in zeit2d_v2.py vor dem Einfrieren
  behoben, meine Fassung blieb unveraendert):
  - (1) Der Startschritt des Leapfrog war fuer die rotierende Loesung nicht exakt (Taylor statt f e^(+i omega dt)). Die
    Zentraldichte wanderte bis T = 20 um 2e-5, ueber der K0-Schranke.
  - (2) Der nl-Arm stuerzte bei kurzem T ab (leere Auswertefenster).
- Abweichung vom Kartenwortlaut, benannt: Arm M startet mit einem Wandstoss statt mit dem Pol-Eigenvektor; die Mode ist im
  Spektrum eindeutig getrennt.
- Der Ball ist kleiner als in Karte und Plan angenommen: "R ~ 31" war der Rechenrand von R12, r_halb ~ 11,9.
- Selbstanzeigen des Agenten: zwei Shell-Fehler ohne Rechenfolgen; fremde Laeufe schoben sich zwischen seine.
- **Abschaetzung: erledigt.**

## Abschaetzung Runde 22 (Leitung, 2026-10-02 21:21:25 CEST)

| Karte | Ergebnis kurz | Abschaetzung |
|---|---|---|
| STELLE-24M | S1 bis S3 eingetroffen; Lee 2020 bleibt Bestwert; Zwei-Term-Stelle-Form nirgends ausgewertet | erledigt (Nachtrag WARUM-SPIN-2) |
| BILDUNG-1 | B0 bis B2 eingetroffen, B3 nicht: einzelne kleine Klumpen werden Q-Baelle (2D) | erledigt; Stufe 5 fuer isolierte kleine Klumpen [H] |
| Bio 28b | D0 bis D2 eingetroffen: Toechter ueberleben, 3 von 8 "auf" | erledigt |
| Bio 45 (Zufall) | Bedingung aus R12 nicht erfuellt | verworfen (Schreibtisch) |
| BILDUNG-2 | C1 nicht (grosser Klumpen atmet), C3 ja, C4 nicht, C0 nicht (Drift) -> C2 offen | erledigt; Folge in BILDUNG-LEITER aufgegangen |
| Bio 28c | J0 und J1 ja, J2 nicht (Lesart des Agenten); vorab ableitbar | erledigt (beschreibend) |
| CODEX-BLICK | M_E-G3 liegt brach; Codex-Schwarm plant M2-Bildung | erledigt; Info an Codex zugestellt |
| PAPIER-SCHNITT | zwei Papiere; PS-1 bis PS-8 | erledigt; PS-7 berichtigt, der Rest bei Finn/Codex |
| ZZZ-ABGLEICH | gleiche Innenwelle, anderer Mechanismus | erledigt; zitieren |
| GEOMETRIE-STAND | Regge-/Defektrahmen ist Literatur; CDT: 4 steckt in den Bausteinen | erledigt |
| WINKELFELD-1 | W0 bis W3 ja, W4 knapp nicht; bekannte Defekt-Elastizitaet; Gauss-Bonnet-Befund | erledigt (Eichung) |
| URSUPPE-1 | U0 ja, U1 bis U3 nicht: keine Dimension aus der Suppe | parken |
| DUNKEL-ZEIT | D2 bis D4 ja, D1 offen (Dark Dimension strittig) | erledigt; Folgekarte SCHWEBUNGSUHR |
| BILDUNG-LEITER | L0 bis L3 ja: Zeitbereich bestaetigt das V; glatte Klumpen = Wand-Atmung | erledigt |

- **Latten-Bilanz (v3):**
  - L1: alle Rechenkarten.
  - L2: BILDUNG-LEITER (unabhaengige Gegenprobe der R12-Breiten), KF-Kontrollen, K0 in URSUPPE.
  - L3: zwei Gitter in BILDUNG-1/2, BILDUNG-LEITER, Bio 28b; nicht in WINKELFELD und Bio 28c.
  - L4: WINKELFELD, GEOMETRIE-STAND, Teile von DUNKEL-ZEIT.
  - L5: STELLE-24M, DUNKEL-ZEIT (Uhren und Kurzabstand).
- **Zufallskarten bisher:** R20 KF-5 parken, R21 Bio 28 verworfen, R22 Bio 45 verworfen.
- **Lehren der Runde:**
  - (1) Rohdatenprobe vor jeder Vorhersage (Bio 28c), jetzt in der Gedaechtnisregel.
  - (2) Peerbus an Codex nur mit --notify-codex; sonst kommt die Nachricht nicht an.
  - (3) Netto-Winkelladung braucht Topologie bzw. Rand (Gauss-Bonnet); der Rauchlauf fing den Kartenfehler.
  - (4) Ein Startschritt fuer rotierende Loesungen muss exakt sein (BILDUNG-LEITER K0).
  - (5) Ich habe Finn zweimal zu stark formuliert: "4D entsteht automatisch" und "Zigarre <-> Pfannkuchen = +-Polarisation".
    Beides ist berichtigt; die Literaturagenten haben es gefunden.

## Gesamtformel, Nachtrag am 02.10. spaet (Leitung, nur Belegtes; Fortschreibung des Stands in RUNDE-20.md)

1. **Ein Feld (M1):**
   - Die stille Mode der 2D-Leiter ist im Zeitbereich bestaetigt (V, Nullstelle und Steigung wie im Frequenzbereich).
   - Der Leiterabstand ist die Halbwelle der einen Innenwelle, dieselbe Formel wie bei Zhang/Zhou/Zhu. Neu ist die exakte
     Stille, nicht der Abstand.
   - **Bildung (2D):** Einzelne kleine Klumpen werden Q-Baelle. Grosse behalten eine gebundene Wand-Atmung; verschmelzende
     behalten Formschwingungen.
   - Gefuetterte Drehbaelle zerfallen in Toechter ohne Windung, die den Drehimpuls als Bahn tragen.
2. **Zwei Felder (M2):**
   - Die Sprossenregel ist fuer l = 0, 1, 2 je einmal vorab bestanden (R20, R21).
   - Die Phasenregel gilt nur auf reifen Leitern.
   - FLS-Literatur: stille Leitern nach Recherchestand nicht beschrieben.
3. **Geometrie und Dimension:**
   - Winkelspannung ist als Netto-Ladung ein Feld mit Fernwirkung; neutrale Klumpen und 3D-Scharniere wirken kurz [S,
     Modell; Literatur].
   - Eine Graph-Suppe mit lokalen Regeln ergibt keine Dimension. CDT braucht Bausteine fester Dimension und eine Zeitregel
     [L].
4. **Zeit:**
   - Ein Tick gehoert zur Atmungsmode bzw. zur Schwebung zweier Baelle, nicht zur Phase eines einzelnen [H].
   - Ein universeller Taktgeber ist in Uhrvergleichen unsichtbar [L].
5. **Gravitation:**
   - Glied 10: Kurzabstandsschranken aktuell. Die Dark Dimension ist seit dieser Woche strittig [L?].

## Einfach gesagt (Runde 22)

Q-Baelle koennen von selbst entstehen, wenn ein einzelner Klumpen allein ist; grosse Klumpen behalten aber lange eine
leise innere Atmung, und zusammenstossende wackeln weiter. Die "stillen Stellen" haben wir jetzt auch im echten
Zeitverlauf gesehen: Genau dort klingt eine Schwingung praktisch nie ab. Zur Geometrie: Fehlt in einem Netz ein Baustein,
entsteht weitreichende Spannung, die das Netz zur Kruemmung draengt; aus einer blossen Suppe von Punkten entsteht aber
kein Raum. Und eine Uhr braucht immer zwei Dinge, die man vergleicht.

## Rundenabschluss (Leitung, 2026-10-02 21:21:55 CEST)

- Journal claude-runde-v3-22-20261002, Index nr 559; pruefen ohne Befund; Quellen-Hashes in
  RUNDE-22/journal-quellen.txt.
- Sicherung r21 siehe Ausgabe; r22 gestartet (Log ...-r22.log). Hinweis: Die Rohsignale von BILDUNG-LEITER (57 MB) liegen
  nur auf der .69 und gehen mit der rsync-Sicherung zum TS440.
- Uebernommen nach Runde 23 (Nachtbetrieb):
  - SCHWEBUNGSUHR (Karte offen)
  - T1 "Q-Ball am Fehlwinkel"
  - M_E-G3 (Codex)
  - Papierentscheidung (Finn)
  - taegliche Pflichten nach Mitternacht
