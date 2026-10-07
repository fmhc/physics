# ERGEBNIS BAD-TAKT (Runde 23)

- Code-Agent im Auftrag der Leitung claude-primary. Geschrieben ab 2026-10-02 22:51:18 CEST (date).
- Zeiten (alle mit date gemessen; .69 in UTC, hier in CEST umgerechnet):
  - Auftragsbeginn 22:30:24.
  - Rauchlauf 22:39:08 bis 22:43:58, vor dem Einfrieren; Parameter in keinem echten Lauf.
  - Plan eingefroren 22:45:57 (PLAN.md.eingefroren-20261002-224557, schreibgeschuetzt; PLAN.md seither unveraendert,
    gleicher sha256).
  - Echte Laeufe auf der .69 ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4, cpu6): Aufrufe ab 22:46:07, letzter Lauf
    fertig 22:46:49.
  - Auswertung nach Plan 22:46:56 bis 22:46:57, Bitvergleich 22:46:57.
  - Literatur ab 22:48:53, also nach allen Laeufen.
  - Nachtraege ausserhalb des Plans (keine Urteilsgrundlage): 22:50:44 und 22:52:20.
- Explorativ (v3). Modell M1 in 1D, drei Baelle (omega^2 = 0,58 / 0,62 / 0,66, D = 18, Amplitude x 1,05), Box L = 45,
  T = 6000. Deutungen sind Hypothesen [H].
- Die Urteile stammen mechanisch aus badtakt1d.py auswerten (Funktion urteile) nach den eingefrorenen Regeln
  (lauf-69/auswertung.json, lauf-69/auswertung.log).

## 1. Ergebnis zuerst

1. **Bis T = 6000 weder Synchronisation noch Vergroeberung, in beiden Phasensaetzen.**
   - Nach dem Einschwingen (erstes Fenster, t = 100 bis 837,5) bleiben Takte und Ladungen stehen.
   - In den Fenstern 2 bis 8 bewegt sich jedes omega_i um hoechstens 2,4e-5 (Phasensatz A, beide Gitter) bzw. 1,7e-4
     (B), jedes Q_i um hoechstens 8,5e-4 (A) bzw. 4,5e-3 (B). Eine durchgehende Richtung gibt es nicht.
   - Alle drei Baelle bleiben bestehen, in jedem Dichtebild drei Maxima > 0,1.
2. **Urteile:** BT1 eingetroffen, BT2 nicht eingetroffen, BT3 eingetroffen, BT4 eingetroffen.
   - BT1 trifft nur dem Wortlaut nach ein: Delta steigt um 1,7e-5 (+0,04 %; B: +7,4e-5).
     - In B1 ist der Anstieg ein einzelner Schritt vom ersten zum zweiten Fenster (Einschwingen), danach ist Delta flach.
       In B2 steigt Delta bis zum 4. Fenster und faellt danach leicht.
     - In der Kontrolle ohne Bad ist der Schritt dreimal so gross wie in B1 (+5,2e-5).
   - BT2 scheitert, weil auch der groesste Ball verliert (-9,1e-4 / -9,9e-4 / -1,41e-3). Gewonnen hat in allen Laeufen der
     mittlere, auch in der Kontrolle.
   - Diese Kombination (BT1 und BT4 ja, BT2 nein) steht in keiner Bedeutungszeile der Karte. Sie wird in Abschnitt 4
     beschrieben, nicht umgedeutet.
3. **Das Bad aendert Takte und Ladungen nicht messbar.**
   - Das Bad haelt 0,0032 Ladung, das sind 3,2e-4 der Gesamtladung (n ~ 3,6e-5 je Laenge, wie im Plan erwartet).
     - Gemessen als Verlust der Kontrolle; die Abstrahlung endet nach t ~ 2000.
     - Es sitzt knapp ueber der Massenschwelle (omega ~ 1,005, positive Ladung).
   - Bad minus Kontrolle im letzten Fenster:
     - Q_i: +5,5e-4 / +6,1e-4 / +7,1e-4. Das entspricht dem Badanteil, der ohnehin durch jeden Ballbereich laeuft
       (erwartet 5,8e-4).
     - omega_i: hoechstens 7,4e-5.
   - Sichtbar wirkt das Bad nur auf zwei Dinge:
     - Die Zentrumsdichte zittert dauerhaft (halbe Spanne 0,016 bis 0,027 in allen Bad-Laeufen; ohne Bad abklingend auf
       3e-4).
     - Die aeusseren Baelle wandern schneller auseinander: Ihr Abstand waechst vom ersten zum letzten Fenster um 11,5
       statt um 6,8 (Phasensatz A).
4. **Zu Finns "Ploppen" [H]: ja, aber jeder Ball in seine eigene Groesse, nicht in eine gemeinsame.**
   - Die Zusatzladung der Anregung (10 %) bleibt fast ganz im jeweiligen Ball; abgestrahlt werden nur 3,2e-4 der
     Gesamtladung.
   - Jeder Ball liegt schon im ersten Fenster auf der Q-Ball-Familie: Die Paare (omega_i, Q_i) treffen die Kurve Q(omega)
     auf 5,3e-4 oder besser (alle Laeufe, erstes und letztes Fenster; Nachtrag, nicht im Plan).
   - Die Takte laufen dadurch 2,2 / 2,7 / 2,9 % langsamer als omega_d.
   - Die Spreizung bleibt bei 0,0442 (A) bzw. 0,0435 (B) stehen, statt 0,0508.
5. **Kontrollen und Literatur:**
   - Kontrollen:
     - Ladungserhaltung im Bad-Arm 2e-14 bis 1,1e-13 relativ.
     - Der Lauf in drei Abschnitten ist bitgleich zum Lauf in einem Stueck.
     - Zweites Gitter: alle Urteile gleich, L3 bestanden (Faktoren 13,5 / 11,3 / 5,1).
   - Literatur (L4, [S] = an Auszuegen geprueft):
     - Im thermodynamischen Gleichgewicht mit einem Bad bleibt ein einziger Q-Ball (Laine/Shaposhnikov 1998 [S]).
     - Lineare Wellenstreuung an Q-Baellen erhaelt die Teilchenzahl (Saffin/Xie/Zhou [S]).
     - Ein Ladungsaustausch Bad <-> Ball kommt also erst in hoeherer Ordnung [H]. Wie schnell ein duennes klassisches
       Bad das Gleichgewicht erreicht, fand ich nicht [L?].

## 2. Vorab gegen Ausgang

Fenstermittel nach dem Nachtrag der Karte: 8 Fenster der Laenge 737,5 in [100; 6000].
- "Erstes" heisst [100; 837,5], "letztes" [5262,5; 6000].
- Groesster Ball = Ball 1 (omega^2 = 0,58), kleinster = Ball 3 (0,66), in allen Laeufen nach dem ersten Fenster bestimmt.
- Streuung = std der Folgefenster-Differenzen / sqrt 2.

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang | Zahlen |
|---|---|---|---|---|
| BT1 | Bad-Arm: Die Spreizung Delta waechst bis T = 6000 (keine Synchronisation) | 65 % | **eingetroffen** (beide Phasensaetze, Gitter einig) | Delta erst -> letzt: B1 0,044201 -> 0,044218 (+1,7e-5, Streuung 9,5e-6); B2 0,043487 -> 0,043561 (+7,4e-5, Streuung 2,9e-5); B1f +1,8e-5. B1: Schritt vom 1. zum 2. Fenster, danach flach; B2: Anstieg bis zum 4. Fenster, danach leicht fallend. Kontrolle K1: +5,2e-5 |
| BT2 | Bad-Arm: Der groesste Ball gewinnt Ladung, der kleinste verliert, auf beiden Gittern | 65 % | **nicht eingetroffen** | Groesster: -9,1e-4 (B1), -9,9e-4 (B1f), -1,41e-3 (B2), Streuung 3,2e-4 bis 5,1e-4. Kleinster: -3,7e-4 / -3,0e-4 / -1,32e-3 (dieser Teil trifft zu). Mittlerer: +1,07e-3 / +9,9e-4 / +2,48e-3. K1 gleiches Muster (-1,13e-3 / +1,06e-3 / -6,3e-4). Badkorrigiert (nur berichtet): ebenfalls nicht eingetroffen |
| BT3 | Kontrolle: Jedes omega_i aendert sich bis T = 6000 um < 1 % | 60 % | **eingetroffen** | Groesste relative Aenderung erst -> letzt 9,1e-5 (Ball 3). Nur berichtet, gegen omega_d: 2,2 / 2,7 / 2,8 %; dieser Sprung liegt vor t = 100 (Anregung) |
| BT4 | Bad-Arm: Kein Ball ploppt in eine gemeinsame Groesse; die Spreizung faellt nie unter die Haelfte des Anfangswerts | 75 % | **eingetroffen** (beide Phasensaetze, Gitter einig) | Das kleinste Delta ist in B1, B1f und B2 das erste Fenster (min/erst = 1,00). Nur berichtet, gegen Delta_d = 0,0508: min 0,0435 = 0,86 Delta_d |

- Fensterregel des Nachtrags: In allen Fenstern aller Laeufe gemessen erfuellt. Die langsamste Paarschwebung ist (1,2)
  mit Periode 295 bis 301, das Fenster ist also das 2,45- bis 2,5-fache.
- Siehe aber Abschnitt 5: Ein noch langsamerer Dreiball-Takt (Periode 3400 bis 3800) ist laenger als jedes Fenster [H].

## 3. Fenstermittel je Lauf (Drift gegen Pendeln)

Gemeinsam: omega^2 = 0,58 / 0,62 / 0,66, D = 18, Amplitude 1,05, L = 45, T = 6000.
- omega_d (Startfrequenz der freien Baelle) = 0,761607 / 0,787433 / 0,812440 bei dx 0,1.
- Q angeregt (Formel, t = 0) = 3,72040 / 3,29073 / 2,96621.
- Q_bad = Q_box - Q_1 - Q_2 - Q_3. Es enthaelt auch die Ballschwaenze jenseits 8 (~1e-3).

**B1: Bad, Phasen (0, 0, 0), dx 0,1**

| Fenster | t | omega_1 | omega_2 | omega_3 | Delta | Q_1 | Q_2 | Q_3 | Q_bad |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 100 bis 837,5 | 0,744999 | 0,766267 | 0,789200 | 0,044201 | 3,72572 | 3,29322 | 2,96091 | 0,00219 |
| 2 | 837,5 bis 1575 | 0,745016 | 0,766213 | 0,789241 | 0,044225 | 3,72459 | 3,29494 | 2,96029 | 0,00221 |
| 3 | 1575 bis 2312,5 | 0,745020 | 0,766207 | 0,789251 | 0,044231 | 3,72490 | 3,29419 | 2,96071 | 0,00223 |
| 4 | 2312,5 bis 3050 | 0,745019 | 0,766218 | 0,789245 | 0,044225 | 3,72461 | 3,29450 | 2,96057 | 0,00235 |
| 5 | 3050 bis 3787,5 | 0,745020 | 0,766214 | 0,789257 | 0,044237 | 3,72481 | 3,29427 | 2,96041 | 0,00254 |
| 6 | 3787,5 bis 4525 | 0,745020 | 0,766207 | 0,789261 | 0,044241 | 3,72461 | 3,29452 | 2,96050 | 0,00241 |
| 7 | 4525 bis 5262,5 | 0,745019 | 0,766212 | 0,789237 | 0,044218 | 3,72480 | 3,29426 | 2,96058 | 0,00240 |
| 8 | 5262,5 bis 6000 | 0,745019 | 0,766210 | 0,789237 | 0,044218 | 3,72481 | 3,29429 | 2,96053 | 0,00240 |

**B1f: Bad, Phasen (0, 0, 0), dx 0,05 (zweites Gitter)**

| Fenster | t | omega_1 | omega_2 | omega_3 | Delta | Q_1 | Q_2 | Q_3 | Q_bad |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 100 bis 837,5 | 0,744973 | 0,766241 | 0,789171 | 0,044199 | 3,72645 | 3,29395 | 2,96164 | 0,00219 |
| 2 | 837,5 bis 1575 | 0,744991 | 0,766184 | 0,789219 | 0,044228 | 3,72530 | 3,29573 | 2,96097 | 0,00223 |
| 3 | 1575 bis 2312,5 | 0,744997 | 0,766178 | 0,789223 | 0,044227 | 3,72566 | 3,29488 | 2,96147 | 0,00222 |
| 4 | 2312,5 bis 3050 | 0,744993 | 0,766187 | 0,789208 | 0,044214 | 3,72528 | 3,29535 | 2,96136 | 0,00223 |
| 5 | 3050 bis 3787,5 | 0,744991 | 0,766189 | 0,789220 | 0,044229 | 3,72560 | 3,29497 | 2,96121 | 0,00244 |
| 6 | 3787,5 bis 4525 | 0,744991 | 0,766197 | 0,789214 | 0,044223 | 3,72553 | 3,29499 | 2,96134 | 0,00237 |
| 7 | 4525 bis 5262,5 | 0,744993 | 0,766196 | 0,789216 | 0,044223 | 3,72561 | 3,29488 | 2,96130 | 0,00243 |
| 8 | 5262,5 bis 6000 | 0,744993 | 0,766189 | 0,789210 | 0,044217 | 3,72546 | 3,29494 | 2,96134 | 0,00249 |

**B2: Bad, Phasen (0, 2/3, 4/3) pi, dx 0,1**

| Fenster | t | omega_1 | omega_2 | omega_3 | Delta | Q_1 | Q_2 | Q_3 | Q_bad |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 100 bis 837,5 | 0,745339 | 0,766568 | 0,788826 | 0,043487 | 3,71679 | 3,28889 | 2,96538 | 0,00208 |
| 2 | 837,5 bis 1575 | 0,745372 | 0,766464 | 0,788895 | 0,043523 | 3,71609 | 3,28916 | 2,96583 | 0,00205 |
| 3 | 1575 bis 2312,5 | 0,745415 | 0,766290 | 0,789012 | 0,043597 | 3,71466 | 3,29369 | 2,96278 | 0,00200 |
| 4 | 2312,5 bis 3050 | 0,745424 | 0,766303 | 0,789032 | 0,043608 | 3,71511 | 3,29222 | 2,96366 | 0,00214 |
| 5 | 3050 bis 3787,5 | 0,745412 | 0,766361 | 0,788958 | 0,043546 | 3,71464 | 3,29203 | 2,96430 | 0,00217 |
| 6 | 3787,5 bis 4525 | 0,745412 | 0,766365 | 0,788979 | 0,043567 | 3,71532 | 3,29172 | 2,96395 | 0,00214 |
| 7 | 4525 bis 5262,5 | 0,745413 | 0,766364 | 0,788951 | 0,043538 | 3,71484 | 3,29193 | 2,96417 | 0,00218 |
| 8 | 5262,5 bis 6000 | 0,745411 | 0,766366 | 0,788972 | 0,043561 | 3,71538 | 3,29137 | 2,96406 | 0,00233 |

**K1: Kontrolle, Rand absorbierend, Phasen (0, 0, 0), dx 0,1**

| Fenster | t | omega_1 | omega_2 | omega_3 | Delta | Q_1 | Q_2 | Q_3 | Q_bad |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 100 bis 837,5 | 0,744998 | 0,766293 | 0,789239 | 0,044241 | 3,72539 | 3,29263 | 2,96046 | 0,00126 |
| 2 | 837,5 bis 1575 | 0,745017 | 0,766235 | 0,789312 | 0,044296 | 3,72395 | 3,29437 | 2,95958 | 0,00103 |
| 3 | 1575 bis 2312,5 | 0,745023 | 0,766228 | 0,789320 | 0,044297 | 3,72459 | 3,29334 | 2,95989 | 0,00100 |
| 4 | 2312,5 bis 3050 | 0,745019 | 0,766243 | 0,789310 | 0,044291 | 3,72403 | 3,29385 | 2,95988 | 0,00104 |
| 5 | 3050 bis 3787,5 | 0,745016 | 0,766247 | 0,789310 | 0,044294 | 3,72457 | 3,29349 | 2,95975 | 0,00099 |
| 6 | 3787,5 bis 4525 | 0,745017 | 0,766247 | 0,789309 | 0,044292 | 3,72421 | 3,29365 | 2,95990 | 0,00103 |
| 7 | 4525 bis 5262,5 | 0,745018 | 0,766246 | 0,789309 | 0,044291 | 3,72442 | 3,29344 | 2,95992 | 0,00102 |
| 8 | 5262,5 bis 6000 | 0,745018 | 0,766244 | 0,789311 | 0,044293 | 3,72426 | 3,29368 | 2,95982 | 0,00103 |

Lesehilfe:
- **Drift oder Pendeln:**
  - In B1, B1f und K1 aendern sich die Werte vom 1. zum 2. Fenster am staerksten. Danach springen die Fenstermittel ohne
    Richtung hin und her: omega in der 5. bis 6. Stelle, Q in der 4. Stelle.
  - Die Steigungen der Fenstermittel ueber die Zeit sind klein. B1: Q_1 -9,7e-5, Q_2 +7,8e-5, Q_3 -3,1e-5 je 1000; alle
    omega unter 7e-6 je 1000.
  - Die Q-Folgedifferenzen wechseln in B1, B1f und K1 vier- bis sechsmal das Vorzeichen (B2: drei- bis fuenfmal).
- **B2** hat einen zweiten Schritt vom 2. zum 3. Fenster: Q_2 +4,5e-3, Q_3 -3,1e-3, und omega gegenlaeufig. Danach gibt
  Q_2 langsam wieder ab (3,29369 -> 3,29137).
- **Q-omega-Kopplung:** Q- und omega-Aenderungen laufen gegenlaeufig, wie es die Familienkurve verlangt (mehr Ladung,
  kleineres omega).
  - Beispiel B2, Ball 2, 2. -> 3. Fenster: +4,5e-3 in Q, -1,7e-4 in omega.
  - Das Verhaeltnis -26 hat dieselbe Groessenordnung wie die Familiensteigung dQ/domega ~ -17 an dieser Stelle, ist aber
    nicht gleich. Die Fenstermittel sind nicht im Gleichgewicht.

## 4. Bedeutung nach Karte

- Die Karte nennt zwei Bedeutungszeilen:
  - "BT1, BT2 und BT4 treffen ein": Vergroeberung. Nicht ausgeloest, weil BT2 nicht eintrifft.
  - "BT1 oder BT4 trifft nicht ein": Synchronisation ueber das Bad. Nicht ausgeloest, weil beide eintreffen.
- **Der Ausgang liegt in keiner Zeile. Beschreibung (ohne Umdeutung):**
  - Die Spreizung schrumpft nicht. Eine Synchronisation ueber das Bad gibt es bis T = 6000 also nicht, in beiden
    Phasensaetzen.
  - Eine Vergroeberung gibt es aber auch nicht.
    - Der groesste Ball nimmt nicht zu. Der mittlere gewinnt etwas, mit und ohne Bad gleich.
    - Ab dem zweiten Fenster bleiben alle Schwankungen unter 0,14 % in Q und 0,03 % in omega.
  - Das Bad selbst (3,2e-4 der Ladung) hinterlaesst in Takten und Ladungen keine Spur ueber der Kontrolle (L2).
- Die Schreibtisch-Erwartung der Leitung ("das Bad treibt Vergroeberung") ist damit fuer diesen Aufbau nicht
  bestaetigt. Widerlegt ist sie auch nicht: Das Bad ist so duenn, dass bis T = 6000 kein Austausch messbar wird [H].
- Die Vorab-Abschaetzung im Plan [H] traf weitgehend zu: kleine, nicht monotone Aenderungen; BT1 entscheidet ein
  Vorzeichen, das nur knapp ueber der Streuung liegt.

## 5. Bad, Lagen, Atmung, Dreiball-Takt (beschreibend)

- **Bad:**
  - Abgestrahlte Ladung in der Kontrolle (Q_gitter(0) - Q_box): 0,00229 / 0,00310 / 0,00321 / 0,00323 / 0,00324 /
    0,00324 / 0,00324 / 0,00324 je Fenster. Die Abstrahlung endet also nach t ~ 2000.
  - Im Bad-Arm bleibt diese Ladung in der Box: 3,2e-4 der Gesamtladung 9,982, n = 3,6e-5 je Laenge. Der Plan erwartete
    3e-5 bis 4e-5.
  - Q_bad(B1) - Q_bad(K1) ~ 0,0014 in den letzten Fenstern. Erwartet waren 0,0015 fuer den Anteil ausserhalb der
    Ballbereiche (42 von 90 Laengeneinheiten). Das Bad ist also etwa gleichmaessig verteilt.
  - Sonde (x = 31,5), erstes Fenster, B1:
    - |psi|^2 = 2,1e-5.
    - Spektrum: 46 % der Leistung bei omega = +1,005 (knapp ueber der Massenschwelle 1, langsame Wellen), daneben
      1,06 und 1,17. Negative Frequenzen (negative Ladung) 0,3 %.
    - B2 zeigt zusaetzlich eine Linie bei 2,19 (1,6 %).
    - Spaeter misst die Sonde den Schwanz von Ball 3, der auf sie zu wandert (letztes Fenster: Linie bei 0,792 = omega_3).
- **Lagen** (Fenstermittel erstes -> letztes; Randabstand nie unter 19):

  | Lauf | Ball 1 | Ball 2 | Ball 3 | Abstand aussen |
  |---|---|---|---|---|
  | B1 | -18,07 -> -25,01 | 0,02 -> -1,74 | 17,96 -> 22,49 | 36,03 -> 47,50 |
  | B1f | -18,06 -> -25,28 | 0,03 -> -1,62 | 17,97 -> 22,68 | 36,03 -> 47,96 |
  | B2 | -17,64 -> -17,78 | 0,25 -> 0,98 | 17,73 -> 24,24 | 35,37 -> 42,02 |
  | K1 | -18,01 -> -21,55 | -0,01 -> -0,16 | 17,99 -> 21,29 | 36,00 -> 42,84 |

  - Die Baelle stossen sich langsam ab, wie bei D = 18 in SCHWEBUNGSUHR-2.
  - Mit Bad (B1, B1f) geht das deutlich schneller als ohne (K1) [H: Kraefte aus der Badstreuung]. Dadurch wird die
    direkte Kopplung mit der Zeit schwaecher.
- **Atmung** (halbe Spanne der Zentrumsdichte):
  - B1: 0,017 bis 0,024 in allen Fenstern.
  - K1: 0,014 / 0,0022 / 0,0013 / ... / 0,0003, klingt also ab.
  - [H] Im Bad-Arm ist das ueberwiegend Interferenz des Badfelds mit dem Ball, 2 f_0 |psi_Bad| ~ 0,0075 (Effektivwert).
    Nachweis einer neu angeregten Eigenatmung: keiner.
- **Dreiball-Takt** (Nachtrag nach den Laeufen, code/nachtrag_dreier.py, lauf-69/nachtrag_dreier.log; nicht im Plan, keine
  Urteilsgrundlage):
  - Die Kombinationsphase ph_1 - 2 ph_2 + ph_3 dreht mit omega_1 - 2 omega_2 + omega_3 = 0,00184 (A), Periode 3415, bzw.
    0,00166 (B), Periode 3794.
  - Der Prozess "zwei Ladungsquanten vom mittleren Ball, je eines zu den aeusseren" ist damit fast resonant, weil die
    omega fast gleichabstaendig sind [H].
  - Gleitende Q-Mittel (Breite 600) gegen cos und sin dieser Phase:
    - R^2 = 0,09 bis 0,45, Amplitude 8e-5 bis 1,2e-3 (B2 am groessten).
    - Der mittlere Ball schwingt gegenphasig zu den aeusseren (Phase 131 bis 149 Grad gegen -26 bis -70 Grad).
    - In 10 von 12 Faellen erklaert dieser Takt mehr als eine lineare Drift (R^2 der Drift 0,002 bis 0,38). In B1 erklaert
      bei Ball 1 und Ball 3 die Drift mehr.
    - Im Fitbereich [400; 5700] liegen nur etwa 1,5 Perioden; der Fit ist daher schwach bestimmt.
  - Lesart [H]: Ein Teil der Unterschiede "letztes gegen erstes Fenster" ist ein langsames Dreiball-Pendeln, laenger als
    jedes Fenster. Es tritt in der Kontrolle genauso auf, ist also kein Badeffekt. Die Fensterregel des Nachtrags (zwei
    Paarschwebungen) deckt es nicht ab.

## 6. Kontrollen

- **Ladungserhaltung** (Q ueber das ganze Gitter, groesste relative Abweichung von t = 0):
  - B1 2,0e-14, B1f 1,1e-13, B2 4,2e-14 (Leapfrog erhaelt diese Ladung exakt bis auf Rundung).
  - K1 verliert 3,2e-4 durch die Daempfungsschicht, das ist die Abstrahlung.
- **Energie** (alle 10): B1 4,6e-6, B1f 1,2e-6, B2 4,3e-6 relativ. Halber Zeitschritt gibt ein Viertel; der Fehler
  skaliert also mit dt^2.
- **Abschnitte:** B1s (drei Aufrufe bis 2000, 4000, 6000) ist bitgleich zu B1: psi, old, alle Messreihen, Bilder, Energie
  (lauf-69/bitvergleich.log).
- **Gittervergleich B1 (dx 0,1) gegen B1f (dx 0,05, also auch halber Zeitschritt):**
  - Alle vier Urteile gleich; BT1 und BT4 auch mit B1f statt B1.
  - Fenstermittel:
    - omega um 2 bis 3e-5 versetzt. Das ist der Gitterversatz von omega_d (2,2e-5 bei Ball 1).
    - Delta im ersten und letzten Fenster bis auf 2e-6 gleich, in den uebrigen bis auf 1,1e-5.
    - Q um 6,5 bis 8e-4 versetzt, wie der bekannte Gitterversatz der freien Q (SCHWEBUNGSUHR-2: 6,7e-4).
  - L3, Effekt letztes minus erstes Fenster, B1 gegen B1f:
    - Delta +1,71e-5 gegen +1,83e-5 (Faktor 13,5)
    - Q_gross -9,09e-4 gegen -9,89e-4 (Faktor 11,3)
    - Q_klein -3,71e-4 gegen -2,98e-4 (Faktor 5,1, knapp ueber der Schwelle 5)
- **Familienkurve** (Nachtrag, lauf-69/qomega.log, nicht im Plan):
  - Q_i gegen Q(omega_i) = 4 sqrt2 omega atanh(sqrt((1 - s)/(1 + s))), s = sqrt(2 omega^2 - 1), Kontinuum.
  - Abweichung erstes und letztes Fenster in allen Laeufen zwischen -5,3e-4 und +1,7e-4. K1 letztes Fenster: -1,1e-4 /
    -1,9e-4 / -3,2e-4.
  - Der verbleibende Rest liegt in der Groesse des Gitterversatzes und der Schwanzladung jenseits 8.

## 7. Literatur (L4)

Erst nach den Laeufen abgerufen, ab 22:48:53 CEST.
- Gelesen wurden ar5iv-Volltexte ueber Auszuege des Werkzeugs WebFetch. Die Zitate sind nicht Zeile fuer Zeile am PDF
  geprueft.
- Die Websuche war fuer die Sitzung erschoepft. Abgerufen habe ich deshalb nur Arbeiten, deren arXiv-Nummer ich kannte.

- **Laine, Shaposhnikov, "Thermodynamics of nontopological solitons", hep-ph/9804237 (Nucl. Phys. B 532 (1998) 376):**
  - Abschnitt 3: "these solutions are saddle points of the Euclidian finite temperature and finite density path
    integral at μ=ω" [S]. Das ist das chemische Gleichgewicht omega = mu der Karte.
  - Abschnitt 3: "the ground state of the system always contains just one Q-ball at any temperature when V→∞" [S]. Im
    Gleichgewicht bleibt also ein einziger Ball; das passt zur Schreibtisch-Erwartung "der groesste gewinnt", als
    Endzustand.
  - Abstract: "In a system with a finite volume, Q-balls evaporate at a volume dependent temperature." [S]
  - Abschnitt 5: "we completely neglect the process of merging of two Q-balls" [S].
  - Die Arbeit behandelt Thermodynamik (heisses Plasma, flache Potentiale, 3D). Wie schnell ein duennes, nicht
    thermisches klassisches Bad dorthin fuehrt, steht dort nicht [L?].
- **Saffin, Xie, Zhou, "Q-ball Superradiance", arXiv:2212.03269:**
  - Abstract: "the scattering involves two coupled modes" [S].
  - Haupttext: "ω± = ωQ ± ω"; beide Moden laufen nur fuer "|ω| > ωQ + 1" (Gl. 8) [S].
  - Abstract: "despite the fact that the particle number is conserved in the scattering, the mismatch between the
    frequencies of the two modes allows for the enhancement of the energy ..." [S].
  - Laut Auszug gibt es keine 1+1D-Rechnung [L?].
  - Anwendung [H]: Unser Bad liegt bei omega_r ~ 1,0 bis 1,2, also 0,2 bis 0,45 ueber den Balltakten. Das ist weit unter
    omega_Q + 1, und nur eine Mode laeuft. In linearer Ordnung tauschen Bad und Ball also keine Ladung. Das passt zum
    Nullbefund.
- **Smerzi, Fantoni, Giovanazzi, Shenoy, cond-mat/9706221 (PRL 79 (1997) 4950):**
  - "z˙=−√(1−z²)sinφ", und bei grossem Energieunterschied "φ=φ(0)+ΔEt, giving an oscillating z(t) with frequency
    ωac≃E₁⁰−E₂⁰" [S]. Das ist das AC-Josephson-Pendeln mit der Differenzfrequenz.
  - Integriert man z˙ bei kleinem z, haengt der Mittelwert von z an phi(0) [H, eigener Schritt]. Das passt zur
    Phasensatzabhaengigkeit der Startwerte (A gegen B, Fenster 1).
- **Aus SCHWEBUNGSUHR-2 uebernommen** (dort [S], hier nicht neu gelesen): Battye/Sutcliffe 2000 (phasengetriebener
  Ladungstransfer in 1D) und Axenides u. a. 2000 (Schwebung mit der Differenzfrequenz, langsame Drift auseinander).
- **Nicht gefunden [L?]:**
  - ein fast resonanter Dreiball-Takt (omega_1 - 2 omega_2 + omega_3) bei Q-Baellen
  - Ostwald-Reifung von 1D-Q-Baellen durch ein klassisches Strahlungsbad
  - Bei erschoepfter Suche heisst "nicht gefunden" hier nur "nicht gesucht werden koennen".
- **Antwort fuer L4:** teilweise bekannt.
  - Endzustand im Gleichgewicht: ein Ball.
  - Linear keine Ladungsuebergabe Welle <-> Ball.
  - AC-Josephson-Pendeln.
  - Unser Nullbefund bei diesem Bad und T = 6000 ist eine modellspezifische Zahl [H].

## 8. Latten (v3, V3-ENTWURF.md, Abschnitt 2)

- **L1, kann scheitern:** ja. Jede Vorhersage hatte zwei Ausgaenge, BT2 ist gescheitert. Die Karte sagt, was man bei
  Synchronisation saehe.
- **L2, Gegenprobe (Bad an gegen aus, B1 gegen K1):** nein fuer "das Bad treibt die Takte".
  - Effekte letztes minus erstes Fenster:
    - Delta +1,7e-5 gegen +5,2e-5
    - Q_gross -9,1e-4 gegen -1,13e-3
    - Q_klein -3,7e-4 gegen -6,3e-4
  - Die Differenzen (+2,2e-4, +2,6e-4) entsprechen dem Zuwachs des Badanteils im Ballbereich (1,7e-4) und liegen in der
    Streuung.
  - Ueber der Kontrolle wirkt das Bad nur auf Lagen und Zentrumsdichte-Zittern.
- **L3, Numerik:** bestanden (Faktoren 13,5 / 11,3 / 5,1). Die gemessenen "Effekte" sind aber Einschwingschritte, keine
  Baddrift.
- **L4, schon bekannt:** teilweise (Abschnitt 7).
- **L5, Messbezug:** nein (1D-Modell).

## 9. Grenzen, Abweichungen, Selbstanzeigen

**Grenzen:**
- 1D, M1, ein Abstand (D = 18), eine Box (L = 45), eine Anregungsstaerke (x 1,05), T = 6000.
- Das Bad ist duenn (3,2e-4 der Ladung). Das liegt an der schwachen Abstrahlung der Anregung, nicht an der Box.
  - Ein dichteres oder thermisches Bad ist nicht geprueft.
  - Ebenso wenig sind es laengere Zeiten, die an die Gleichgewichtsaussage (ein Ball) heranreichen koennten.
- Das erste Fenster enthaelt noch das Einschwingen; die Abstrahlung endet erst bei t ~ 2000. "Letztes gegen erstes" misst
  deshalb vor allem diesen Schritt (Regel der Karte, nicht geaendert).
- Der Dreiball-Takt (Periode 3400 bis 3800) ist laenger als die Fenster. Sein Phasenversatz geht in die Urteile ein [H].
- Die Sonde misst ab der Mitte des Laufs den Schwanz des wandernden Balls 3. Nur ihre fruehen Werte beschreiben das Bad.

**Abweichungen vom Plan:** keine bei Laeufen, Regeln und Urteilen.
- Nach den Laeufen kamen drei Nachtraege hinzu, alle als solche markiert und keine Urteilsgrundlage:
  - Familienkurve Q(omega), auf der .69 per python -c ueber kleintest.sh
  - Dreiball-Phase, neues Skript code/nachtrag_dreier.py
  - Delta-Streuung, lokal per jq

**Selbstanzeigen:**
1. **Lokaler Interpreterstart:** Um 22:42 CEST stand in einem lokalen grep-Befehl versehentlich `python3 - 2>/dev/null`.
   - Der Interpreter startete mit leerer Eingabe und endete sofort; es lief kein Code.
   - Dem Wortlaut nach verstoesst das gegen "lokal keine Python-Laeufe".
2. **Rauchlauf nahe an den echten Parametern:** 0,57 / 0,61 / 0,65 und D = 17 bei gleicher Box.
   - Er zeigte vor dem Einfrieren die Taktverschiebung durch die Anregung und die schwache Abstrahlung.
   - Damit habe ich die Fensterlaenge und den Hinweis zu BT3/BT4 gegen omega_d festgelegt (im Plan offengelegt). Die
     gewertete Lesart folgt ohnehin dem Nachtrag der Karte.
3. **Codeaenderungen vor dem Einfrieren:** Spektrumsvorzeichen und Badkorrektur (im Plan offengelegt). Nach dem Einfrieren
   blieb badtakt1d.py unveraendert (sha256 unten).
4. **Werkzeugdateien:** Der Warte-Befehl legte eine Ausgabedatei unter /tmp/claude-1000/.../tasks/ an. Ein jq-Filter
   (tab.jq) liegt in meinem Scratchpad.
5. **Websuche:** Ein Suchversuch wurde wegen des erschoepften Sitzungsbudgets abgelehnt. Die Quellen stammen deshalb aus
   meinem Gedaechtnis (arXiv-Nummern) und wurden per WebFetch abgerufen.
6. **Rauchlauf-Ausgaben** liegen nur auf der .69 unter runde23-bad-takt/rauch/ und wurden nicht kopiert.

**Laufzeiten** (Service runtime): B1 15,3 s, B1f 33,9 s, B2 15,6 s, K1 26,1 s, B1s 3 x 5,4 s, je "neu" 0,5 bis 0,8 s;
Auswertung 0,6 s. Wartezeit auf belegte Spuren hoechstens ~10 s.

**sha256** (lokal und auf der .69 gleich, Praefixvergleich):
- code/badtakt1d.py 4a38fcc0d1236769c68f310eff552d91308250ea2b627fcaaca5009f3bd53f0e
- code/nachtrag_dreier.py 3a4df6e723dbf4fb18a9ca2425905b769372a2ee3a05e9e76afa9811c25f1bb7
- PLAN.md und PLAN.md.eingefroren-20261002-224557 3f11a7727a0d7e6a0d27142a36103e2387774fcc549b23ee1a65118f255c56a9
- lauf-69/auswertung.json a27f362c7fb1ed1e4333fb7fa79ba533d1e1836355d9d8b4007281dd9f8b0be7
- lauf-69/B1.npz 5f22da9ac1bd373d197c3a10ae4670736a8d4d22a405f0bfb0b277efed6435c0
- lauf-69/B1f.npz dc363de22b097892955900ef011accb224db96d8660cc253d6d0f8d56ef50ace
- lauf-69/B2.npz 1601211cec7db2ce57721fd9c153a87e16d351407d3e78a11e75f5b0190c37a1
- lauf-69/K1.npz 5db2ffdf1a60f897d7e672fb38dcdf35e9c51b694db074cc52783401ecd9ccde
- lauf-69/B1s.npz 844c58ba12a22594fcfa4050f41e9e4b20755180621a1fd9e974e63082c81420

## 10. Einfach gesagt

Wir haben drei verschieden grosse Wellenpakete, die sich wie Uhren je in ihrem eigenen Takt drehen, in eine Kiste mit
spiegelnden Waenden gesetzt. Ein kleiner Schubs am Anfang laesst sie etwas Wellen abstrahlen, die als gemeinsames "Bad"
in der Kiste bleiben. Die Frage war, ob sich die Uhren ueber dieses Bad angleichen oder ob die grosse Uhr die kleinen
frisst. Bis zum Ende passiert keins von beidem: Jede Uhr findet nach kurzer Zeit ihren eigenen festen Takt und behaelt
ihn. Das Bad ist dafuer einfach zu duenn; es enthaelt nur drei Zehntausendstel der ganzen Ladung.
