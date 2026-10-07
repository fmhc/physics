# DANZER-NAEHERUNG-2: Plan (Runde 47, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Karte KARTE.md bindend; D2-0 bis D2-3 und ihre Bedeutung unveraendert.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):** Start 2026-10-05 08:33:04 CEST. Code ab etwa 08:46, Plan ab 09:00:09 CEST.
  Zeitbox 120 min, also bis 10:33 CEST.
- **Vor diesem Plan liefen vier Rauchtests** ueber kleintest.sh (R1 cpu3 06:51:30 bis 06:52:10, R2 cpu3 06:52:44 bis
  06:53:18, R3 cpu4 06:53:26 bis 06:56:06, R4 cpu4 06:57:36 bis 06:59:22 UTC). Sie geben Bau, Sterne, Kontrollen und
  Zeiten aus, keine a2- oder beta-Werte. Ein Aufruf (R3, erster Versuch) brach nach 30 ms ab (falsches Arbeitsverzeichnis,
  rc = 2). **R3 lief 160 s und damit ueber der 120-s-Grenze** (Selbstanzeige im Ergebnis). Danach habe ich die LU-Zerlegung
  umgestellt (symmetrisch, ohne Pivotsuche) und die Taylor-Operatoren blockweise angewandt; R4 (gleicher Inhalt) lief 106 s.
- **Nach dem Planentwurf, vor dem Einfrieren:** R5 (rechnen 1/1 S,M Saaten 0,1, 30 Richtungen, --probe
  --zitter-kontrolle --einheit; 07:02:01 bis 07:02:20 UTC, 18,9 s) und R6 (auswerten darauf; 07:02:20 bis 07:02:23 UTC,
  2,4 s), nur als Durchlaufprobe beider Pfade. Gelesen habe ich nur rc (0, 0) und grep auf "Traceback/Error" (0 Treffer);
  keine Werte.
- **Kennzeichen:** [M] eigene Mathematik (ungeprueft), [E] gerechnet, [P] Projektdatei, [F] Festlegung dieses Plans,
  [H] Hypothese, [R] aus den Rauchtests (vor dem Plan gesehen).
- Alles ist synthetische Rechnung an gedachten, unendlich periodischen Netzen. Keine Messdaten.

## 0. Gelesen (vor dem Plan)

- KARTE.md; DANZER-NAEHERUNG-1: ERGEBNIS.md, PLAN.md, code/danzer_naeherung.py, lauf-69 (nur Netz-Felder: Fenster-Margen,
  Rhomboedertypen, gamma).
- TAKT-UMKLAPP-1: KARTE.md, ERGEBNIS.md Abschnitt 2 und Nachtrag 4.5 a, code/tu.py (umkreis_tet, umkreis_drei, einheit,
  hodge), tg.PAARE, uk.FL. licht-finn-netz-1 und hodge-l nicht gebraucht.
- Kein Projekt-grep.

## 1. Bau [F] (unveraendert aus DANZER-NAEHERUNG-1) und 5/3

- code/danzer_naeherung.py und code/licht_netz.py sind unveraenderte Kopien (sha256 0571953e... und 98d3960a...,
  gleich den Originalen). Neu ist nur code/dn2.py; es importiert den Bau unveraendert: naeherung, ecken (Fenster),
  rhomboeder, kanten_key, flaechen_key, Fenster-Stoerung gamma = 1e-7 xi_Saat, Zitter sigma_D = 1e-6, periodisches
  Delaunay (26 Nachbarbilder, Schwerpunkt in der Zelle), Saaten default_rng([3746, p, q, s]) mit derselben Zugfolge.
  netz2 rechnet dieselben Kanten- und Flaechennummern wie danzer_naeherung.netz.
- **5/3:** p = 5, q = 3. L = (2 p tau + 2 q)/N = 11,661, eps = (q tau - p)/(p tau + q) = -0,01316 [M].
  Rauchtest R4 (Saat 0) [R]:
  - V = 2440 (erwartet L^3 vol(W)/8 = 2440,000), E = 17080 = 7 V, F = 29280 = 12 V, T = 14640 = 6 V, Euler 0.
  - 1 Komponente, jedes Dreieck in genau 2 Tetraedern, Volumensumme gegen L^3 1,4e-16, kein flaches Tetraeder,
    Tetraedervolumen 0,0784 bis 0,1268 (wie 1/1 bis 3/2).
  - 2440 Rhomboeder fuellen die Zelle (1,4e-16), keine fehlende Ecke. Delaunay verletzt 0, Zusatzpunkte auf Umkugeln
    12 064 (4,9 je Ecke). Fensterpunkte naeher als 1e-5 am Rand: 180; kleinste Marge 1,5e-8.
- Die Pruefungen laufen je Saat mechanisch wie in DANZER-NAEHERUNG-1 (netz2: Zusammenhang, Euler, Mannigfaltigkeit,
  Volumen, Delaunay-Leerkugel vektorisiert mit gleicher Schwelle 1e-9, Rhomboeder).

## 2. DEC-Operatoren [F]

- **Hodge-Sterne:** umkreisbasiert und vorzeichenbehaftet, Rechenweg woertlich aus tu.py (hodge): *1 = duale Flaeche /
  Kantenlaenge, *2 = duale Laenge / Dreiecksflaeche, *0 = duales Volumen je Ecke (Summe l A*/6 an beiden Enden).
  P1-Gewichte werden nicht verwendet. Gegenprobe (1/1, 2/1, je 8 Saaten, R1): gleich den Sternen der Schleife in
  danzer_naeherung.netz auf <= 5,6e-15 (*1) und <= 3,3e-14 (*2) [R].
- **Null:** |*1| bzw. |*2| <= 1e-9 x Maximum (wie DANZER-NAEHERUNG-1). Die Luecke ist gross: Null-*1 <= 9e-30, kleinstes
  echtes *1 = 0,1004; Null-*2 <= 8e-15, kleinstes echtes *2 = 0,449 (alle Ordnungen) [R].
- **Skalar:** d0^H *1 d0 phi = omega^2 *0 phi. Gerechnet als K = B^H B mit B = *1^(1/2) d0 *0^(-1/2) auf den Kanten mit
  *1 > 0; Kanten mit *1 = 0 tragen nichts bei. Bloch-Phasen wie DANZER-NAEHERUNG-1 (Lagen relativ zur Kantenmitte).
- **Maxwell (Coulomb-Phase):** d1^H *2 d1 a = omega^2 *1 a.
  - Kanten mit *1 = 0 haben keine Masse. Sie werden statisch kondensiert (exaktes Minimum der Energie ueber diese
    Kanten). Allgemein verschmilzt das die aktiven Dreiecke an einer solchen Kante zu einem Vieleck mit *2 = L*/Flaeche
    (code: flaechen_verschmelzen) [M].
  - **[R] Auf allen gerechneten Netzen hat keine masselose Kante ein aktives Dreieck** (alle Dreiecke an ihr haben
    *2 = 0). Die masselosen Kanten sind also ganz entkoppelt und fallen heraus; kein Vieleck hat mehr als ein Dreieck.
    Kontrolle "kondensation": Energie mit expliziter Kondensation gegen Vieleck-Energie, Abweichung <= 4e-16 [R].
  - Gerechnet als K' = C~^H C~ + G~ G~^H mit C~ = *2^(1/2) d1 *1^(-1/2) (aktive Dreiecke x massive Kanten) und
    G~ = Wurzel(4) *1^(1/2) d0 *0^(-1/2). C~ G~ = 0 (Kontrolle). Die Laengsmoden liegen bei 4 omega_skalar^2 (Faktor 4
    trennt sie von den Photonen, die bei gleichem Tempo laegen) [F]. Photonen = Ritz-Vektoren mit
    |G~^H v|^2 / (omega^2 |v|^2) < 0,5 (Laengsmoden: 1), bei exakten Eigenwerten < 1e-6 wie DANZER-NAEHERUNG-1.
- **Eigenwerte:** Rayleigh-Ritz in der k.p-Basis wie DANZER-NAEHERUNG-1 (Maxwell: harmonische Formen bei k = 0 und
  R K_m B_(j-m) bis Ordnung 4; Skalar: Konstante *0^(1/2) bis Ordnung 6). omega = Singulaerwert von B(k) S (K = B^H B),
  nicht Eigenwert von S^H K S: Das haelt die relative Genauigkeit kleiner omega [M].
  - Gegenprobe je Saat: Skalar an 2 Zufallsrichtungen x 2 k (Fensterraender) gegen exakte Eigenwerte (dicht bis
    V = 700, sonst Shift-Invert); Maxwell ebenso (5/3: 1 Richtung x 2 k) gegen exakte Shift-Invert-Eigenwerte.
  - **Schwelle 1e-6 relativ**, sonst ist der Zweig der Saat unsicher gekennzeichnet. Rauchtests: <= 1,4e-11 [R].
- **Einheitsgewichte (Vergleich D2-3):** Werte aus DANZER-NAEHERUNG-1 (lauf-69/auswertung.json, Saatmittel), Kopie als
  Eingabe der Auswertung [P]. Option --einheit rechnet sie auf denselben Netzen neu (nur beschreibend, nur falls Zeit).

## 3. Kontrollen (je Saat, im JSON)

- D2-0-Groessen: Grundtempo-Spanne (max c - min c)/Mittel c ueber 40 Richtungen je Saat und Zweig (skalar, maxwell_lo,
  maxwell_hi, maxwell_mittel); beta je Saat.
- **Zitter-Kontrolle [F]:** fuer die erste Saat je Ordnung (1/1, 2/1, 3/2) ein zweites Netz mit gleichem gamma (gleiche
  Ecken) und anderem Zitter (default_rng([3746, p, q, s, 1001])). Prueft genau die Kartenaussage zu den Kugel-
  Gleichstaenden und misst den numerischen Boden von beta.
- Identitaeten: T1 = sum *1 l l^T und T2 = sum L* A n n^T gegen Vol I; Abschluss der dualen Zellen; sum *0 = Vol.
- C~ G~ = 0 (3 Zufalls-k), K0 H = 0, C0 D = 0, Kondensation, Ritz-Gegenprobe, Vorzeichen von *0, *1, *2 (negativ, null,
  positiv), Eckenmenge (sha256) und Fingerabdruecke der Gewichte (sha256 der sortierten *0 und der sortierten positiven
  *1, gerundet).

## 4. Messung von beta [F] (wie DANZER-NAEHERUNG-1)

- 40 Fibonacci-Richtungen auf der oberen Halbkugel (danzer_naeherung.halbkugel), gleiche Richtungen.
- Hauptfenster k in [0,03; 0,12] pi/L, 8 Punkte; Probe [0,015; 0,06] pi/L nur fuer die erste Saat von 1/1, 2/1, 3/2
  (beschreibend; 5/3 ohne Probe wegen der Laufzeit).
- Fit licht_netz.fit(kk, omega, 6, gerade=True), Zerlegung danzer_naeherung.zerlegen: beta = Koeffizient von
  S4 = sum n_i^4 (Projektion auf K4). Beide Funktionen werden unveraendert importiert (danzer_naeherung.operator_messen).
- Je Ordnung Mittel und SD ueber die Saaten. Hauptgroessen wie DANZER-NAEHERUNG-1: skalar und maxwell_mittel
  (= Wurzel((omega_lo^2 + omega_hi^2)/2)); maxwell_lo und maxwell_hi beschreibend.

## 5. Saaten und Laufliste [F]

- 1/1, 2/1, 3/2: die 8 Saaten 0 bis 7 aus DANZER-NAEHERUNG-1. 5/3: Saaten 0 und 1 (je ein Lauf).
- Nur .69, kleintest.sh, Spuren cpu3 und cpu4, ein Thread, je Lauf <= 600 s. Arbeitsordner
  /home/fmh/fmhc-physics-remote/danzer-naeherung-2/ (code/, lauf/, rauch/).
- Laufzeiten geschaetzt aus R1 bis R4: 1/1 etwa 3 s je Saat, 2/1 etwa 15 s, 3/2 etwa 70 s, 5/3 etwa 400 s.

| Lauf | Spur | Aufruf (code/dn2.py ...) | erwartet |
|---|---|---|---|
| L1 | cpu3 | rechnen 1/1 S,M 0,1,2,3,4,5,6,7 lauf/n11.json --probe --zitter-kontrolle | < 1 min |
| L2 | cpu3 | rechnen 2/1 S,M 0,1,2,3,4,5,6,7 lauf/n21.json --probe --zitter-kontrolle | ~ 3 min |
| L3a | cpu4 | rechnen 3/2 S,M 0,1,2,3 lauf/n32a.json --probe --zitter-kontrolle | ~ 6,5 min |
| L3b | cpu3 | rechnen 3/2 S,M 4,5,6,7 lauf/n32b.json | ~ 5 min |
| L4a | cpu4 | rechnen 5/3 S,M 0 lauf/n53a.json | ~ 7 min |
| L4b | cpu3 | rechnen 5/3 S,M 1 lauf/n53b.json | ~ 7 min |
| L5 | cpu3 oder cpu4 | auswerten lauf/auswertung.json lauf/bild-danzer-naeherung-2.png lauf/dn1-auswertung.json lauf/n*.json | < 1 min |

- Reihenfolge: 1/1 bis 3/2 zuerst (Teilbericht moeglich), dann 5/3. Reicht die Zeit nicht, wertet L5 aus, was da ist.
- Nur falls Zeit bleibt (beschreibend, kein Urteil): 5/3 mit --einheit fuer das Bild.
- Faellt ein Lauf aus (Fehler, 600 s), steht das im Ergebnis. Eine Codeaenderung danach ist eine Selbstanzeige mit neuer
  eingefrorener Fassung.

## 6. Urteilsregeln (mechanisch, Funktion urteilen)

- **D2-0 (Kartenwortlaut):**
  - Grundtempo: (max c - min c)/Mittel c < 1e-10 fuer jede Ordnung, jede Saat, Zweige skalar, maxwell_lo, maxwell_hi.
  - beta: max - min ueber die Saaten < 1e-10 je Ordnung (mindestens 2 Saaten).
  - Plan: Hauptgroessen skalar und maxwell_mittel; "Karte alle Zweige" nimmt lo und hi dazu.
  - Alles erfuellt: eingetroffen. Sonst nicht eingetroffen (alle Einzelwerte im Ergebnis).
- **D2-1:** R = abs(Mittel beta(3/2)) / abs(Mittel beta(1/1)) < 1/3 je Hauptgroesse. Beide: eingetroffen; keine: nicht
  eingetroffen; sonst geteilt.
- **D2-2:** R = abs(Mittel beta(5/3)) / abs(Mittel beta(3/2)) < 0,6 je Hauptgroesse, Gesamt wie D2-1. Fehlt 5/3: nicht
  auswertbar.
- **D2-3:** abs(Mittel beta_DEC) < abs(Mittel beta_Einheit, DANZER-NAEHERUNG-1) fuer 1/1, 2/1, 3/2 und beide
  Hauptgroessen (6 Vergleiche). Alle: eingetroffen; keiner: nicht eingetroffen; sonst geteilt. Fuer 5/3 gibt es keinen
  Wert aus DANZER-NAEHERUNG-1; "auf jeder Ordnung" lese ich als "auf jeder Ordnung, fuer die DANZER-NAEHERUNG-1 einen
  Wert hat" [F].
- Beschreibend: Vorzeichen von beta, Verhaeltnisse 2/1:1/1, 3/2:1/1, 5/3:3/2, Probe-Fenster, Zitter-Kontrolle,
  Sterne, Kondensation.

## 7. Gleichstaende: folgt D2-0? (Pruefung vor dem Einfrieren)

- **Kugel-Gleichstaende (Kartenaussage) [M, R]:** An einem Gleichstand fallen die Umkugelmittelpunkte zusammen. Die duale
  Flaeche einer Kante ist das Vieleck der Umkugelmittelpunkte der Tetraeder um sie; es haengt nicht von der Aufloesung
  ab, und Kanten, die es nur in einer Aufloesung gibt, haben *1 = 0. Ebenso hat jedes Dreieck im Inneren eines
  Gleichstands *2 = 0. Ein Dreieck auf einem Kreis zwischen zwei verschiedenen Gleichstaenden haette *2 != 0; dann
  braucht es die Kondensation, die das Vieleck wiederherstellt. Hier kommt das nicht vor [R]: Alle masselosen Kanten
  liegen ganz im Inneren von Gleichstaenden. **Die DEC-Operatoren haengen also nicht vom Zitter ab.** Die
  Zitter-Kontrolle prueft das.
- **Grundtempo [M], staerker als die Karte:**
  - Die Karte begruendet die Isotropie mit kubischer Symmetrie. Die einzelnen Netze sind aber nicht kubisch.
    DANZER-NAEHERUNG-1 Plan 7: gamma != 0 bricht T_h, bei 1/1 gibt es keine T_h-symmetrische gueltige Pflasterung.
  - Hier folgt c = 1 trotzdem, fuer jedes periodische Netz mit umkreisbasierten Sternen:
    - Die dualen Zellen fuellen den Raum. Mit dem Divergenzsatz je dualer Zelle folgt sum_e *1_e l_e l_e^T = Vol I, mit
      dem Divergenzsatz je Tetraeder sum_f L*_f A_f n_f n_f^T = Vol I. Beide gelten nur global, nicht je Tetraeder.
    - Die dualen Zellen und die dualen Vielecke sind geschlossen. Deshalb faellt die Korrektur zweiter Ordnung weg,
      fuer den Skalar ebenso wie fuer eps_eff und mu_eff.
    - Also gilt omega^2 = k^2 (1 + O(k^2)) fuer den Skalar und beide Photonen, ohne Doppelbrechung in fuehrender Ordnung.
  - [R] T1/Vol und T2/Vol weichen von I um <= 5e-15 ab; der Abschluss der dualen Zellen haelt auf <= 1e-15.
  - **Erwartung: Grundtempo-Teil von D2-0 eingetroffen, Spanne im Bereich der Fit-Rundung (1e-13 bis 1e-11).** Das ist
    vorab ableitbar und keine Messung.
- **beta ueber die Saaten: folgt NICHT allein aus den Kugel-Gleichstaenden [R, M]:**
  - Die Saat bestimmt auch gamma (1e-7). gamma entscheidet ueber Gitterpunkte genau auf dem Fensterrand (Fenster-
    Gleichstaende; kleinste Marge 1e-9 bis 1e-8 in allen Ordnungen).
  - [R] Die Eckenmengen (sha256 der 6D-Koordinaten) sind von Saat zu Saat verschieden, in allen Ordnungen.
  - Bei 1/1 sind die Fingerabdruecke der Gewichte (sortierte *0 und *1) in allen 8 Saaten gleich, passend zu
    symmetriegleichen Pflasterungen.
  - Bei 2/1 gibt es unter den 8 Saaten mindestens 4 verschiedene *1-Fingerabdruecke (*0 in 3 Klassen). Bei 3/2 haben die
    3 geprueften Saaten drei verschiedene *1-Fingerabdruecke (gleiche *0).
  - Das sind verschiedene, gleich gueltige Pflasterungen (Phason-Wahl am Fensterrand), nicht verschiedene Aufloesungen
    desselben Gleichstands.
- **Erwartung daraus:**
  - D2-0 nach Kartenwortlaut **nicht eingetroffen**, ueber den beta-Teil ab 2/1. Ursache: Fenster-Gleichstand, nicht
    Kugel-Gleichstand; die Groesse der Saatstreuung ist nicht ableitbar.
  - Bei 1/1 und in der Zitter-Kontrolle erwarte ich Gleichheit bis auf den numerischen Boden.
  - Ob 1e-10 erreichbar ist, weiss ich nicht. Abschaetzung [M]: Rundung ~1e-14 in omega, Fit-Verstaerkung 1e3 bis 1e5,
    also beta-Boden ~1e-11 bis 1e-9. Die Zitter-Kontrolle misst ihn.
  - Das ist Vorab-Kenntnis aus den Rauchtests [R], keine Messung von beta.
  - **Bedeutung nach Karte bei D2-0 verfehlt:** "Fehler im Bau oder ein Gleichstand ohne Kugel-Entartung. Erst klaeren,
    dann weiter." Geklaert ist es schon hier: ein Fenster-Gleichstand. D2-1 bis D2-3 rechne ich trotzdem, als Saatmittel wie
    DANZER-NAEHERUNG-1.
- **Negative Sterne [R]:** In keinem geprueften Netz (1/1, 2/1 je 8 Saaten, 3/2 Saaten 0 bis 2, 5/3 Saat 0) gibt es negative
  *0, *1 oder *2. Das passt zu Delaunay (Hirani u. a. 2013 ueber HODGE-L [P]). Die Nullen sind die Gleichstaende:
  *1 null 8,8 bis 8,9 %, *2 null 20,6 bis 20,8 %.
- **Nicht ableitbar:** Betrag und Abfall von beta mit DEC-Gewichten, ein Boden, das Verhaeltnis zu den Einheitsgewichten.

## 8. Agenten-Vorhersagen (vor jeder Hauptrechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| B1 | D2-0 Grundtempo-Teil: alle Spannen < 1e-10 | 90 % |
| B2 | D2-0 nach Kartenwortlaut nicht eingetroffen (beta-Teil, Fenster-Gleichstand) | 85 % |
| B3 | Zitter-Kontrolle: beta-Abweichung < 1e-8 in allen drei Ordnungen | 75 % |
| B4 | Saatmittel von beta mit DEC-Gewichten negativ in allen vier Ordnungen (skalar) | 55 % |
| B5 | D2-3 eingetroffen | 45 % |
| B6 | Ritz-Gegenprobe <= 1e-6 in allen Saaten | 95 % |

## 9. Einfrieren

- Eingefroren werden PLAN.md und code/dn2.py als Kopien *.eingefroren-<Zeit>, sha256 in EINGEFROREN-SHA256.txt, auf der
  .69 dieselben Pruefsummen. danzer_naeherung.py und licht_netz.py sind unveraenderte Kopien. Danach keine Aenderung an
  Plan, Code oder Regeln.
