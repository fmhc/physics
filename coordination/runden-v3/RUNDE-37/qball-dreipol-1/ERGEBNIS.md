# QBALL-DREIPOL-1: Ergebnis (Code-Agent, Runde 42)

- Code-Agent fuer claude-primary. Start 2026-10-04 17:14:57 CEST; ERGEBNIS geschrieben ab 17:57:53 CEST (date).
- **Eingefroren** 17:42:24 CEST: PLAN.md.eingefroren-20261004-174224 und code/*.eingefroren-20261004-174224, Hashes in
  EINGEFROREN-SHA256.txt. Um 17:56:49 CEST erneut geprueft: unveraendert. Auf der .69 liefen dieselben Hashes.
- **Laeufe** (.69, kleintest.sh, Spuren p4000a und p4000b, numpy/scipy auf einem Kern in der Einheit):
  - Hauptlaeufe 15:42:31 bis 15:53:13 UTC, alle rc = 0. Auswertung 15:54:51 bis 15:54:55 UTC.
  - Nachtrag (nach Sicht der Hauptwerte, ohne Urteil) 15:53 bis 15:54:40 UTC.
- Kennzeichen wie in der Karte: [M] Mathematik, [E] Messung im Modell, [P] Projektdatei, [L] Literatur aus dem
  Gedaechtnis, [H] Hypothese.
- Alles ist eine synthetische Rechnung im Modell (2+1, Papier-I-Potential mit drei Komponenten). **Keine
  Messdatenbestaetigung.**

## Ergebnis zuerst

1. **Kontrolle bestanden, vorab ableitbar [E, M].** Fuer alle 45 Zustaende folgt E(Q) je innere Richtung der wirksamen
   Kopplung g_eff = g4 sum n_a^4 auf hoechstens 5,3e-7 (QD0).
   - Bei g4 = -0,1 gewinnt ein Pol, bei g4 = +0,1 die gleiche Mischung.
2. **Verschiedene Pole spueren sich im Schwanz viel schwaecher als gleiche [E].**
   - Die Wechselwirkung verschiedener Pole faellt wie e^{-2 kappa d}, die gleicher Pole wie e^{-kappa d}. Gemessene
     Raten fuer verschiedene Pole: 1,377 / 1,233 / 1,093 gegen 2 kappa = 1,398 / 1,255 / 1,114.
   - Bei d = 2R (Waende beruehren sich) ist der eingespannte Wert fuer gleiche Pole in Phase aber **abstossend**
     (+6,0 bis +6,5): Die Waende ueberlappen in der Feldsumme. Das Betragsverhaeltnis verschieden/gleich betraegt
     0,25 / 0,30 / 0,331.
   - **QD1 (Plan) ist damit eingetroffen, aber nur knapp** (g4 = +0,1: 0,331 gegen 1/3). Das Urteil haengt am
     genauen Abstand: Bei 2,25R oder 2,5R faellt es bei mindestens einem g4 durch.
   - Nach Kartenwortlaut (verschiedene Pole relaxiert) ist QD1 nicht eingetroffen: 0,37 / 0,46 / 0,55.
3. **Drei verschiedene Pole binden [E; der Energievergleich war vorab ableitbar].**
   - Der Fluss bei festen Ladungen verschmilzt das beruehrende Dreieck bei g4 = +0,1 nach 300 Schritten zum gleich
     gemischten Ball. Bindung B = 15,52, das sind 9,6 % von 3 E_1. **QD2 ist eingetroffen.**
   - **Neu [E]:** Bei g4 = -0,1 endet der Fluss nicht im Mischball, sondern in einem festen Dreieck aus drei
     einfarbigen Klumpen (Paarabstand 1,245 R). Es liegt 0,146 unter dem Mischball (beschreibend, ohne Urteil).
4. **In echter Zeit pulsiert der Dreier, statt ruhig zu verschmelzen [E].**
   - Die drei Pole fallen durch die gemeinsame Mitte, stehen danach als umgekehrtes Dreieck und kehren um. Mittendurchgaenge
     folgen im Abstand 70 / 47 / 40 Zeiteinheiten (g4 = -0,1 / 0 / +0,1); die groesste Ausdehnung liegt bei 1,57R bis
     2,03R (Start 2R).
   - Bis t = 200 bleiben 99,3 / 98,5 / 96,5 % jeder Polladung im Klumpengebiet. **QD3 ist eingetroffen** (Plan: c1;
     Kartenwortlaut: c2, der verschmolzene Ball ruht unveraendert).
   - Einschraenkung: Im symmetrischen Dreieck verbietet schon die Energieerhaltung das Auseinanderfliegen
     (Selbstanzeige 5).
5. **Bedeutung [H]:** Ein "Baryon-Q-Ball" aus drei Polen existiert im Modell, aber nichts zeichnet die Drei aus.
   - Q-Baelle kleben generell zusammen, auch zwei verschiedene oder drei gleiche Pole.
   - Ein einzelner Pol ist allein stabil; es gibt keinen Einschluss.
   - Die drei Ladungen sind U(1)^3, nicht SU(3).
   - Die Anisotropie entscheidet nur die Gestalt: g4 > 0 ergibt einen gemischten Klumpen, g4 < 0 ein Dreieck aus drei
     einfarbigen Klumpen.

## Urteile (mechanisch, lauf-69/auswertung.json; Vorhersagen der Karte unveraendert)

| Nr | Vorhersage (Karte) | Wahrsch. | Plan | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| QD0 | E(Q) je Richtung folgt g_eff (< 1 %) | 90 % | **eingetroffen** | **eingetroffen** | 45 Zustaende konvergiert (2D und radial), max abs(delta) = 5,3e-7; vorab ableitbar |
| QD1 | verschiedene Pole wechselwirken bei d = 2R mindestens 3-mal schwaecher als gleiche in Phase | 60 % | **eingetroffen** (knapp) | **nicht eingetroffen** | eingespannt: abs(E_versch)/abs(E_gleich) = 0,252 / 0,299 / 0,331; relaxiert: 0,370 / 0,456 / 0,553 (g4 = -0,1 / 0 / +0,1) |
| QD2 | beim Mischungs-g4 ist der Dreier gebunden | 35 % | **eingetroffen** | **eingetroffen** | g4 = +0,1: B = 15,522 (Schwelle 0,161), Anteil im Klumpengebiet >= 0,99998, verschmolzen; E_Ende = E_mix(180) aus (a) bis 3e-14; vorab ableitbar |
| QD3 | wenn QD2: der Dreier bleibt bis t = 200 zusammen, kein Ein-Pol-Zerfall | 30 % | **eingetroffen** | **eingetroffen** | c1: min Q_a,in/Q_a = 0,9646, Hoechstanteil 0,3335, dE 2,9e-6, dQ 4,7e-16; c2: 0,99998 / 0,3334 / 1,2e-8 |

- **QD1 im Einzelnen** (eingespannt, d = 2R): gleicher Pol in Phase +5,993 / +6,188 / +6,472; verschiedene Pole
  -1,513 / -1,852 / -2,143.
  - Das Plan-Urteil vergleicht Betraege. Es zaehlt also einen abstossenden gegen einen anziehenden Wert; der
    Vorzeichenwechsel des Kanals "gleich in Phase" liegt zwischen 2R und 2,25R.
  - Verhaeltnis bei 2,25R: 0,49 / 1,20 / 7,9; bei 2,5R: 0,20 / 0,30 / 0,55. Die Regel war vorab auf 2R gebunden; sie
    bleibt so.
- **QD1 Kartenwortlaut:** Die relaxierte Rechnung haelt nur den Schwerpunkt jeder Komponente fest. Der Nachtrag zeigt,
  dass dabei Ladung in den anderen Ball wandert (Tabelle 4). Der relaxierte Wert misst also nicht nur den Abstand,
  sondern auch einen Farbaustausch.
- **QD2:** Der Vermerk "vorab ableitbar" steht mechanisch in auswertung.json (Plan 2.4). Neu ist nur die Groesse:
  9,6 % Bindung.
- **QD3:** Der Ein-Pol-Zerfall ist durch die getrennte Ladungserhaltung ausgeschlossen (Plan 2.5). Zur Ableitbarkeit
  von "zusammen" siehe Selbstanzeige 5.

## Tabellen

### 1. Kontrolle (a): E und omega je Richtung (2D-Gitter, Ladung je Komponente Q n_a^2)

| g4 | Richtung | g_eff | E(Q = 60) | omega(60) | E(Q = 180) | omega(180) |
|---|---|---|---|---|---|---|
| -0,1 | ein Pol | -0,1 | 48,5129 | 0,7151 | 131,4051 | 0,6771 |
| -0,1 | zwei Pole | -0,05 | 50,0322 | 0,7485 | 137,1881 | 0,7139 |
| -0,1 | gleich gemischt | -0,0333 | 50,5015 | 0,7589 | 138,9807 | 0,7253 |
| 0 | alle drei (gleich bis 1e-14) | 0 | 51,3895 | 0,7786 | 142,3831 | 0,7470 |
| +0,1 | ein Pol | +0,1 | 53,6940 | 0,8306 | 151,3081 | 0,8041 |
| +0,1 | zwei Pole | +0,05 | 52,6048 | 0,8059 | 147,0697 | 0,7769 |
| +0,1 | gleich gemischt | +0,0333 | 52,2144 | 0,7971 | 145,5600 | 0,7673 |

- Q = 30, 90 und 120 sind ebenso gerechnet (lauf-69/a.json, Bild energie_Q.png).
- E/Q faellt mit Q bei allen g4. Fuer einen Pol: 0,885 auf 0,730 (g4 = -0,1), 0,920 auf 0,791 (0), 0,946 auf 0,841 (+0,1)
  fuer Q = 30 bis 180.
- Abweichung 2D gegen radial: 0,8e-7 bis 5,3e-7. Der radiale Bezug selbst liegt bei dr = 0,01 um -1,8e-7 neben
  QB-BS-2D (g = 0, Q = 100: 82,139693 gegen 82,139708 [P]); bei dr = 0,02 um -7,1e-7 (zweite Ordnung).

### 2. Wechselwirkung zweier Q-Baelle (Q1 = 60 je Ball, eingespannt, feste Ladungen; Bild lauf-69/wechselwirkung.png)

R = R_halb des Einpolballs: 3,176 / 3,159 / 3,193 fuer g4 = -0,1 / 0 / +0,1. Je Zelle: gleich in Phase | gleich
gegenphasig | verschieden | Dreieck aus drei Polen mit Seite d.

| d/R | g4 = -0,1 | g4 = 0 | g4 = +0,1 |
|---|---|---|---|
| 1,5 | +77,3 / +21,3 / +0,957 / +11,4 | +58,7 / +27,3 / -1,162 / +3,26 | +45,2 / +34,6 / -2,640 / -2,64 |
| 2 | **+5,99** / +6,60 / **-1,513** / -3,71 | **+6,19** / +8,38 / **-1,852** / -4,73 | **+6,47** / +10,80 / **-2,143** / -5,64 |
| 2,25 | -2,42 / +4,01 / -1,178 / -3,35 | -1,11 / +4,92 / -1,342 / -3,81 | +0,19 / +6,25 / -1,502 / -4,27 |
| 2,5 | -3,41 / +2,53 / -0,677 / -2,00 | -2,63 / +2,99 / -0,799 / -2,35 | -1,67 / +3,72 / -0,920 / -2,70 |
| 3 | -1,405 / +0,986 / -0,136 / -0,408 | -1,422 / +1,158 / -0,193 / -0,578 | -1,275 / +1,403 / -0,258 / -0,770 |
| 4 | -0,123 / +0,114 / -0,0025 / -0,0076 | -0,169 / +0,160 / -0,0057 / -0,0171 | -0,209 / +0,213 / -0,0113 / -0,0338 |
| 6 | -0,0011 / +0,0011 / -4,4e-7 / -1,3e-6 | -0,0026 / +0,0026 / -2,6e-6 / -7,7e-6 | -0,0049 / +0,0050 / -1,1e-5 / -3,4e-5 |

- **Verschiedene Pole relaxiert** (Schwerpunktstifte), d/R = 1,5 / 2 / 2,5 / 3 / 4:
  - g4 = -0,1: -2,769 / -2,215 / -1,345 / -0,377 / -0,0042
  - g4 = 0: -3,850 / -2,820 / -1,683 / -0,518 / -0,030 (4R: Wandzeit, nicht konvergiert)
  - g4 = +0,1: -4,846 / -3,576 / -2,273 / -0,990 / -0,370 (4R: Wandzeit, nicht konvergiert)
- **Schwanzraten** (ln E(5R)/E(6R) durch R) [E]:
  - gleiche Pole 0,728 / 0,657 / 0,583 gegen kappa = sqrt(1 - omega^2) = 0,699 / 0,627 / 0,557. Der Ueberschuss von etwa
    0,03 passt zum 2D-Vorfaktor d^{-1/2}: (ln 1,2)/(2R) = 0,029 [M, Naeherung].
  - verschiedene Pole 1,377 / 1,233 / 1,093 gegen 2 kappa = 1,398 / 1,255 / 1,114.
- **Gegenphasig** ist der gleiche Pol bei allen d abstossend; im Schwanz spiegelbildlich zum Kanal "in Phase"
  (-0,0011 gegen +0,0011 bei 6R).
- **Eingespannt verschiedene Pole:**
  - Bei kleinem d stossen sie sich ab (a + b > 4/3 im Kernueberlapp, Plan 2.3): positiv bis 1,5R (g4 = -0,1), bis
    1,25R (0) bzw. bis 0,75R (+0,1).
  - Das Minimum liegt bei ~2R (g4 = -0,1), ~1,75 bis 2R (0) bzw. ~1,5 bis 1,75R (+0,1).
  - Relaxiert ist es bei 1,5R ueberall anziehend. Bei g4 = -0,1: eingespannt +0,96, relaxiert -2,77.

### 3. Dreier (Q1 = 60 je Pol, Start: beruehrendes Dreieck, Seite d0 = 2R, Klumpengebiet R_K = rho + 3R)

**Fluss bei festen Ladungen (ohne Stifte):**

| g4 | 3 E_1 | E Start (eingespannt) | E Flussende | B = 3 E_1 - E_Ende | Gestalt | Schritte | E gleich gemischt (a) |
|---|---|---|---|---|---|---|---|
| -0,1 | 145,539 | 141,831 | **138,835** | 6,704 (4,6 %) | **Dreieck**, Paarabstand 3,955 = 1,245 R | 1050 | 138,981 |
| 0 | 154,168 | 149,439 | 142,383 | 11,785 (7,6 %) | verschmolzen | 500 | 142,383 |
| +0,1 | 161,082 | 155,437 | 145,560 | 15,522 (9,6 %) | verschmolzen | 300 | 145,560 |

- Alle drei Fluesse sind konvergiert (max abs(Residuum) < 1e-7).
- Bei g4 = -0,1 ist das Ende ein stationaeres Dreieck aus drei einfarbigen Klumpen. Es liegt 0,146 unter dem
  gleich gemischten Ball.
  - Gerechnet ist es nur im symmetrischen Unterraum: Der Fluss erhaelt die Spiegelung und naeherungsweise C3. Ob es
    gegen unsymmetrische Verformung ein Minimum oder ein Sattel ist, ist offen [H].

**Zeitentwicklung c1** (vom eingespannten Dreieck, Baelle in Ruhe, Rauschen 1e-3, Saat 1, dt = 0,025; Bilder
lauf-69/dreier.png, lauf-69/abstaende.png):

| g4 | Mittendurchgaenge bei t | groesste Ausdehnung (t: Paarabstand/R) | min Q_a,in/Q_a | dE/E |
|---|---|---|---|---|
| -0,1 | 36,0; 106,5; 176,0 | 70,0: 2,03; 141,0: 1,97 | 0,993 | 4,1e-6 |
| 0 | 23,0; 70,5; 116,5; 163,0 | 46,5: 2,00; 94,5: 1,97; 138,5: 1,92; 186,5: 1,96 | 0,985 | 2,2e-6 |
| +0,1 | 20,0; 59,5; 99,0; 138,5; 179,5 | 39,5: 1,75; 79,5: 1,66; 118,5: 1,89; 158,5: 1,78; 199,5: 1,57 | 0,965 | 2,9e-6 |

- Die Pole gehen durcheinander hindurch. Pol 1 startet bei (0; 3,687), ist bei t = 20 in der Mitte und bei t = 40 bei
  (0; -3,226) (g4 = +0,1). Das Bild zeigt bei t = 200 das umgekehrte Dreieck (g4 = -0,1 und +0,1).
- Ladung verlaesst das Klumpengebiet stufenweise bei jedem Mittendurchgang (abstaende.png, rechts); das deute ich als
  Abstrahlung [H].
- Die Energie im Start liegt ueber dem Flussende: um 3,0 / 7,1 / 9,9. Diese Energie steckt in der Pulsation.
- In auswertung.json heisst ein Feld "t_verschmolzen" (c1, g4 = +0,1: 18,5). Es meint den ersten Mittendurchgang,
  kein bleibendes Verschmelzen.

**Proben bei g4 = +0,1:**

| Lauf | min Q_a,in/Q_a | Paarabstaende/R bei t = 200 | dE/E |
|---|---|---|---|
| c1, Saat 1, dt = 0,025 (Haupt) | 0,964620 | 1,5554 / 1,5547 / 1,5728 | 2,9e-6 |
| c1, Saat 2 | 0,964662 | 1,5561 / 1,5552 / 1,5734 | 2,9e-6 |
| c1, dt = 0,0125 | 0,964625 | 1,5554 / 1,5547 / 1,5727 | 7,2e-7 (Faktor 4: dt^2) |
| c2 (vom Flussende) | 0,999977 | <= 5,1e-4 | 1,2e-8 |

- **Symmetriebruch:** Die relative Spreizung der drei Paarabstaende waechst von 1e-4 auf 1,1 bis 1,2 % bei t = 200,
  in beiden Saaten gleich.
  - Das ist deterministisch: Das quadratische Gitter und die Box haben kein C3; Pol 1 sitzt auf der Spiegelachse.
  - Eine vom Rauschen getriebene Instabilitaet zeigt sich bis t = 200 nicht.

### 4. Nachtrag (ohne Urteil, nach Sicht der Hauptwerte): Ladungsverlagerung in der Stiftrelaxation

Fremdanteil heisst: Anteil von abs(psi_1)^2 auf der Seite des anderen Balls (x < 0) bzw. umgekehrt
(lauf-69/nachtrag/nachtrag.json, Code code/nachtrag.py).

| g4 | d/R | E_int eingespannt / relaxiert | Fremdanteil eingespannt | Fremdanteil relaxiert |
|---|---|---|---|---|
| -0,1 | 2 | -1,513 / -2,215 | 0,048 / 0,064 | 0,099 / 0,117 |
| 0 | 2 | -1,852 / -2,820 | 0,055 / 0,072 | 0,163 / 0,180 |
| +0,1 | 2 | -2,143 / -3,576 | 0,064 / 0,081 | 0,200 / 0,218 |
| +0,1 | 4 (Wandzeit) | -0,0113 / -0,3725 | 0,0018 / 0,0024 | 0,106 / **0,329** |

- Bei 4R und g4 = +0,1 hat Komponente 2 am fremden Platz eine Hoechstdichte von 0,40 (am eigenen 0,52). Die
  Stiftrelaxation baut also Mischbaelle an beiden Plaetzen, solange die Schwerpunkte stimmen.
- Bei 2R sind die E_int-Werte identisch mit b_*.json. Bei 4R (Wandzeit) haengt der Wert an der erreichten Schrittzahl:
  -0,3725 nach 3800 Schritten gegen -0,3700 nach 3550 Schritten in b_p01.json.

## Kontrollen

- **Erhaltung:** Ladung je Komponente <= 8,3e-16 relativ in allen Zeitentwicklungen. Energie <= 4,1e-6; mit dt/2
  7,2e-7. Tor 1e-3.
- **Konvergenz:** 45/45 Zustaende in (a) und 45/45 radial. Einpolbaelle mit Residuum <= 2e-11. Fluesse in (c) mit
  Residuum < 1e-7. Stiftrelaxation bei 2R konvergiert (Energiekriterium).
- **Gitter:** N = 320 gegen 256 bei gleichem L aendert E des Einpolballs um 2,2e-16 relativ (Rauchlauf).
- **Extern:** radialer Bezug gegen QB-BS-2D bei Q = 100: -1,8e-7 [P].
- **Fluss gegen (a):** Das Flussende bei g4 = 0 und +0,1 trifft E_mix(180) aus (a) auf 6e-12 bzw. 3e-14.
- **Lokalisierung:** Anteil im Klumpengebiet am Flussende >= 0,99998. Das Rauschen sitzt nur auf den Baellen.

## Selbstanzeigen

1. **Reihenfolge:** Code, Rauchlauf r1, die volle QD0-Kontrolle und die Leitungstests liefen, waehrend der Plantext
   entstand (im Plan offen gelegt).
   - Gesehen habe ich dabei Zeiten, QD0-Werte und den Einpolball bei g4 = +0,1, keine Hauptwerte. Ausnahme ist
     Punkt 3.
2. **Erster Kontrolllauf abgebrochen:** Der radiale Bezug lief bei Q = 180, g = -0,1 ueber. Ich habe ihn vor dem
   Einfrieren berichtigt (tau = 0,5, Neustart bei Ueberlauf; PLAN 9a.1).
3. **Leitungstest angesehen, Tor geaendert (vor dem Einfrieren):**
   - Den Flussendzustand des Leitungstests mit Q1 = 25 habe ich zur Fehlersuche angesehen: Die Pole rueckten schnell
     zusammen (PLAN 9a.3).
   - Danach setzte ich das Energietor fuer QD3 von 1e-4 auf 1e-3 (PLAN 9a.2).
   - Beides geschah vor dem Einfrieren. Am Ausgang aendert das Tor nichts: gemessen 2,9e-6.
4. **Plan und Code weichen ab:** Der Plan nennt fuer die Stiftrelaxation sieben Abstaende (1,5 / 1,75 / 2 / 2,25 /
   2,5 / 3 / 4 R). Das eingefrorene Laufskript gab keine Liste mit; gerechnet wurden die fuenf Standardwerte des Codes
   (1,5 / 2 / 2,5 / 3 / 4). QD1 braucht nur 2R; das Urteil ist nicht betroffen.
5. **Ableitbarkeit von QD3 erst nach dem Lauf gesehen:**
   - Im symmetrischen Dreieck ist "zusammen bleiben" weitgehend durch die Energieerhaltung erzwungen. Der Start liegt
     unter drei getrennten Baellen: E(0) = 155,44 < 3 E_1 = 161,08.
   - Auch mit Abstrahlung kann der Dreier nicht symmetrisch auseinanderfliegen [M]: Drei freie Baelle der Ladung
     Q' <= 60 plus Strahlung (E >= abs(Q)) kosten mindestens 3 E_1(60), weil E_1(Q) - Q mit Q faellt.
   - Offen waren nur zwei Wege. Erstens unsymmetrischer Zerfall: zwei Pole zusammen, einer frei. Er ist bei g4 = +0,1
     energetisch moeglich (100,23 + 53,69 = 153,92 < 155,44), ebenso bei g4 = 0 (148,70 < 149,44). Zweitens Strahlung
     ueber 10 %.
   - Beides trat bis t = 200 nicht ein. Diese Probe gehoerte in Abschnitt 2 des Plans.
   - Informativ an QD3 ist also: kein Symmetriebruch aus 1e-3-Rauschen bis t = 200, Strahlungsverlust 3,5 %, und die
     Pulsation.
6. **QD1 haengt am Ansatz:** Der eingespannte Kanal "gleich in Phase" ist bei 2R abstossend; die Feldsumme ueberzaehlt
   den Wandueberlapp. Das Urteil haengt am genauen Abstand (Tabelle 2) und hat bei g4 = +0,1 nur 0,6 % Spielraum. Fuer
   gleiche Pole gibt es keine relaxierte Rechnung.
7. **Nachtrag nach Sicht:** code/nachtrag.py und Tabelle 4 entstanden nach Sicht der Hauptwerte. Sie aendern kein
   Urteil.
   - Zwei relaxierte Punkte bei 4R (g4 = 0 und +0,1) endeten in der Wandzeit. Sie gehen in kein Urteil ein.
8. **Gewinner bei g4 = 0:** In auswertung.json steht "ein_pol", die Energien sind aber bis 1e-14 gleich (U(3)). Nur
   die Rundung entscheidet; das Feld wird nicht verwendet.
9. **ssh:** Lange wartende Verbindungen waren hoechstens drei (zwei Laufskripte, dazu der Nachtrag in der Warteschlange
   des Locks). Mit kurzen Abfragen der Ueberwachung und eigenen Abfragen koennen kurzzeitig fuenf gleichzeitig offen
   gewesen sein.
10. **Leitungstestwerte:** rauch-69/pipe/ enthaelt Werte mit Q1 = 25 und unkonvergierten Fluessen. Das sind keine
    Hauptwerte. Die Flussendzustaende (*_fluss.npy, je 3 MB) liegen nur auf der .69; ihre Hashes stehen in
    lauf-69/PRUEFSUMMEN.txt.
11. **Nicht geoeffnet** habe ich Versiegeltes (VERSIEGELT, vertraege-20260925, KS-1, T8-SOLL, ks-1-dk-*),
    Geheimnisdateien und Codex-Dateien. Papier I habe ich nur gelesen.
12. **Nicht erledigt:** keine Peerbus-Nachricht, kein Commit, kein Journaleintrag. Die Schreibrechte waren auf zwei
    Ordner begrenzt; der Journaleintrag liegt bei der Leitung.
13. **Zeiten:** .69-Stempel in UTC, lokale in CEST, alle per date bzw. aus der Starter-Ausgabe.
14. **Sitzungsordner:** Die Ausgaben meiner Hintergrund-Befehle (Warteschleifen, ssh-Rueckgaben) legt das Werkzeug
    selbst unter /tmp/claude-1000/.../tasks/ ab. Ich habe dort nichts angelegt und keine Projektdatei abgelegt.

## Bedeutung (nach der Vorab-Bedeutung der Karte)

- **"QD2 und QD3 treffen ein: Ein Baryon-Q-Ball aus drei Polen ist im Modell moeglich" ist ausgeloest**, mit vier
  Einschraenkungen:
  1. Die Bindung ist nicht dreierspezifisch [E, a]. Zwei verschiedene Pole binden auch: Der Zweipolball mit Q = 120
     liegt bei 100,23 gegen 2 E_1 = 107,39 (g4 = +0,1). Drei gleiche Pole binden auch: Ein Pol mit Q = 180 liegt bei
     151,31 gegen 161,08. Grund ist das fallende E/Q, also Q-Ball-Physik [L, Standard].
  2. Es gibt keinen Einschluss: Ein einzelner Pol ist ein stabiler Q-Ball.
  3. Die drei Ladungen sind getrennt erhaltene U(1); es gibt keine SU(3) und kein Farbsingulett im strengen Sinn.
  4. QD2 war vorab ableitbar. QD3 war im symmetrischen Dreieck weitgehend erzwungen (Selbstanzeige 5).
- **Was die Tetraeder-Anisotropie wirklich tut [E]:**
  - Bei g4 > 0 ist der dreifarbig gemischte Ball die billigste Form fuer eine gegebene Gesamtladung. Das ist das
    naechste Gegenstueck zu einer "Singulett-Vorliebe".
  - Bei g4 < 0 bleiben drei verschiedene Pole als Dreieck aus einfarbigen Klumpen zusammen, tiefer als der Mischball.
    Das ist das naechste Bild fuer "drei getrennte Bausteine, die zusammenhalten" [H].
- **Dynamik [E]:** Ohne Reibung verschmilzt der Dreier nicht, er pulsiert. Die Pole laufen periodisch durcheinander
  hindurch und verlieren je Durchgang etwas Ladung als Strahlung (bis t = 200: 0,7 bis 3,5 %). Der Endzustand bei
  langer Zeit ist offen.
- **Kleber:** Einschluss muesste weiter vom Kleber kommen (GLUONEN-L, KOPPLUNG-TETRA-1). Dieser Test spricht weder
  dafuer noch dagegen.
- **Moegliche Fortsetzung** (Entscheidung bei der Leitung):
  - Das Dreieck bei g4 < 0 ohne Symmetriezwang pruefen (Hesse-Spektrum oder Fluss mit Rauschen).
  - Laengere Zeitentwicklung, um den Endzustand der Pulsation zu sehen.
  - Ein Gegenstueck mit phasenabhaengigem Quartterm (bricht U(1)^3), damit die Pole Ladung tauschen koennen.
- **Lattenbezug:** L1 erfuellt; QD1 haette verfehlen koennen und ist es nach Kartenwortlaut. L5 (Messbezug) fehlt; alles
  ist synthetisch.

## Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-174224, EINGEFROREN-SHA256.txt
- code/: dreipol.py, auswertung.py, laeufe-p4000a.sh, laeufe-p4000b.sh, je mit .eingefroren-20261004-174224;
  nachtrag.py (nicht eingefroren, Nachtrag)
- rauch-69/: r1.json und r1.log (Rauchlauf), a/ (volle QD0-Kontrolle und Log des abgebrochenen Erstlaufs), pipe/
  (Leitungstest Q1 = 25)
- lauf-69/:
  - auswertung.json (Urteile, Tabellen) und PRUEFSUMMEN.txt
  - a.json, b_{m01,0,p01}.json, c_{m01,0,p01}.json (+ _bilder.npz), c1s2_p01.json, c1dt_p01.json, dazu die Logs
  - Bilder: wechselwirkung.png, dreier.png (Dreier zu t = 0, 100, 200), abstaende.png, energie_Q.png
  - nachtrag/nachtrag.json und nachtrag.log

## Einfach gesagt

Wir haben Q-Baelle mit drei "Farben" gebaut: Jede Farbe ist ein eigenes Feld, das sich in sich dreht. Eine kleine
Zusatzkraft aus der Tetraeder-Symmetrie entscheidet, ob eine reine Farbe oder eine gleichmaessige Mischung am wenigsten
Energie kostet, und die Rechnung bestaetigt das auf sieben Stellen. Verschiedenfarbige Baelle spueren sich auf Abstand
viel schwaecher als gleichfarbige. Drei sich beruehrende Baelle verschiedener Farbe halten zusammen: Mit Reibung
verschmelzen sie zu einem bunten Ball oder bilden ein festes Dreieck, ohne Reibung fallen sie immer wieder
durcheinander hindurch wie ein atmender Klumpen. Das sieht aus wie ein Baryon aus drei Farben, ist aber keine
Besonderheit, denn Q-Baelle kleben generell zusammen und ein einzelner Ball ist allein voellig stabil; fuer echten
Farbeinschluss wie bei Quarks fehlt weiter ein Kleber.
