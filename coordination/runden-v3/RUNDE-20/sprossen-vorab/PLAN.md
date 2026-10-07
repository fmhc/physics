# PLAN SPROSSEN-VORAB (Runde 20)

- Code-Agent. Start 2026-10-02 17:07:55 CEST (date). Plan geschrieben ab 17:16:21 CEST (date), vor jedem Lauf dieser
  Karte (bis dahin nur py_compile auf der .69).
- Gelesen: KARTE.md, KARTE-NACHTRAG-1.md (Leitung, 17:09:55); HUELLEN-LEITER-3: KARTE, PLAN (eingefroren), beide
  Nachtraege, ERGEBNIS, FREMDSTIMME, code/, aus/ (test-auswertung.json, aus/test/*.json nur Laufzeiten und Lagen,
  diag/ nur Dateinamen); HUELLEN-LEITER-2: ERGEBNIS, aus/diag/umlauf-st1-0-13.json (genaue Lage der Stelle bei
  R = 40,49); Runde 18: ERGEBNIS, aus/laeufe/stellen.json, aus/zeilen.json. Nichts aus Sperrbereichen.
- Verbindlich (Karte): Annahmekriterium (Kurvenzuordnung nur ueber Stetigkeit und Rang), Pflichtpruefung L4 vor dem
  Einfrieren, Vorhersagetabelle, V0 bis V3, Bedeutung. Nichts davon wird nach dem Ergebnis geaendert.
  **[Lesart]**-Stellen sind markiert. Die Zusatzvorgabe der Leitung (Kartennachtrag 1) steht getrennt in Abschnitt 7.
- Code: code/huellen_leiter3.py, huellen_leiter2.py, stille3.py, beutel.py unveraendert aus HUELLEN-LEITER-3
  (sha256 f67e1375..., 2755359c..., 1d15a38c..., f831e818..., verglichen). Neu: code/sprossen_vorab.py (Befehle test,
  ausw, fortfehler; importiert huellen_leiter3.py unveraendert). Hilfsdateien: hilfs/zeilen-126.json (erste 126 Zeilen
  der Zeilenliste der Runde 18), hilfs/bekannte.json (88 Stellen der Runde 18, Stufe 1 und 2, mit gap; 8 Sprossen aus
  HUELLEN-LEITER-3, S-Wurzeln; die Stelle bei R = 40,487 aus HUELLEN-LEITER-2 getrennt, keiner Kurve zugeordnet).

## 1 Verfahren (Code wie HUELLEN-LEITER-3)

- Profile Stufe 1 (hp 0,01) und Stufe 2 (hp 0,005), Zeilen 0 bis 125 (R bis 46,48), aus der Saat bei Q = 200 wie die
  Vorlaeufer (Befehl profile von huellen_leiter3.py). Vergleich mit profile-info.json von HUELLEN-LEITER-3 (Erwartung
  bitgleich in w2, Q, E, Rchi).
- **Lagen aus Variante S** (chi < 1e-12 -> 0), **Umlauf aus Variante F** (chi im Inneren analytisch fortgesetzt), wie
  HUELLEN-LEITER-3 Plan 1. Newton auf W = m_ac + i m_bc gedaempft (newton_W, unveraendert: Schritt < 1e-10, hoechstens 30
  Schritte, |d omega^2| <= 2e-4, |d rho| <= 2e-3). Ankerprofil = naechste Zeile mit omega^2 <= Start.
- Start: omega^2 = lineare Interpolation in der Tabelle (Rchi, omega^2) der Stufe 1 beim Ziel-R (beide Stufen gleich);
  rho = Kurvenfortsetzung (Abschnitt 3) beim Ziel-R. Nachstarts bei Ziel-R - 0,25 und + 0,25 (Karte), in dieser
  Reihenfolge, Abbruch beim ersten lokal angenommenen Versuch.
- Rechteck-Umlauf von W wie HUELLEN-LEITER-3 (umlauf_mit_rueckfall, 16 Punkte je Kante, Verfeinerung bis Sprung
  < 0,4 rad, Halbbreite min(1e-3, 0,4 Abstand zum E1-Rand, 0,25 gap, 0,5 dw2_zeile), Rueckfall 1e-4): mit F um die
  F-Wurzel (Newton F ab der S-Wurzel). Dazu mit S um die S-Wurzel, nur berichtet.

## 2 Annahme einer Sprosse (Testcode, derselbe fuer L4 und Test)

Je Ziel (k, R_ziel) und Stufe, an der S-Wurzel (alle Pflicht):

1. **konv:** Newton konvergiert und |W| <= 1e-9 (Karte). |W| < 1e-10 wird berichtet.
2. **Rangabfall:** sigma2/sigma1 von G <= 1e-6 (wie HUELLEN-LEITER-3) und Bereich E1.
3. **Rang [Lesart wie HUELLEN-LEITER-3]:** In der Zeile bei omega^2 der Wurzel (zeile_k, Variante S) hat die naechste
   Nullstelle von m_bc den Rang k von unten und liegt auf <= 1e-6 bei rho der Wurzel.
4. **Stetigkeit:** |rho_Wurzel - rho_fort(R_Wurzel)| < 0,1 d_nb (Abschnitt 3).
5. **Fenster:** |R_Wurzel - R_ziel| <= 0,5 (R = Rchi des Profils an der Wurzel). "Gefunden" = angenommen in diesem
   Fenster (Karte).
6. Dann (nur fuer lokal angenommene Versuche): F-Newton ab der S-Wurzel und F-Rechteck; S-Rechteck.

Ueber beide Stufen: angenommen, wenn auf beiden Stufen 1 bis 5 erfuellt sind, der F-Rechteck-Umlauf auf beiden Stufen
aufgeloest und +-1 ist und die S-Wurzeln beider Stufen in omega^2 und rho auf <= 1e-6 uebereinstimmen.
Delta R = R_Wurzel (Stufe 1) - R_ziel. **Keine Knotenzahl** (Karte; Fremdstimme L4). Die Knotenzahl wird nur berichtet.

## 3 Fortsetzung, Nachbarabstand, Schwelle (vorab festgelegt)

- **Fortsetzungsformel:** rho_fort(R) = quadratisches Polynom in x = 1/R (Lagrange) durch die letzten drei bekannten
  Stellen der Kurve k mit R < R_ziel - 1 (Stufe-1-Werte R, rho aus hilfs/bekannte.json), ausgewertet bei 1/R.
  - Bekannte Stellen: die 88 Stellen der Runde 18 und die 8 Sprossen aus HUELLEN-LEITER-3 (auch die zwei k = 3-Stellen,
    die dort formal nur an der Knotenzahl scheiterten). Neu gefundene Sprossen dieses Tests werden **nicht** verwendet
    (keine Verkettung); fuer die zweite Sprosse von k = 4 bis 7 reicht die Fortsetzung also zwei Sprossen weit.
  - Die Bedingung R < R_ziel - 1 schliesst die Zielstelle selbst aus, wenn sie (bei L4) bekannt ist. Sprossenabstaende
    sind >= 2,1, also bleibt die Vorgaengerstelle drin.
  - Damit (Test): k = 0: Nr 81, 39,594, 42,004; k = 1: Nr 88, 40,506, 42,613; k = 2: Nr 85, 40,229, 42,351; k = 3:
    Nr 83, 39,765, 41,912; k = 4: Nr 63, 71, 80; k = 5: Nr 67, 77, 86; k = 6: Nr 64, 73, 82; k = 7: Nr 66, 75, 87.
  - Startwert rho = rho_fort(R_Start); Pruefwert rho_fort(R_Wurzel).
- **Abstand zur Nachbarkurve d_nb:** In derselben Zeile (zeile_k bei omega^2 der Wurzel) der kleinere Abstand der
  Nullstelle mit Rang j (naechste zur Wurzel) zu den Nullstellen mit Rang j - 1 und j + 1; fuer j = 0 nur j + 1.
- **Schwelle:** Fortsetzungsfehler < 0,1 d_nb (Karte: "kleiner als ein Zehntel").
- Berichtet: Fehler, d_nb, Verhaeltnis Fehler/d_nb je Stelle und Stufe; dazu (Befehl fortfehler, reine Datenrechnung)
  die Fortsetzungsfehler an allen bekannten Stellen fuer einen und zwei Sprossenschritte, im Verhaeltnis zum
  Nachbarabstand gap der Runde 18 (Hinweis der Leitung: fuer k = 4 bis 7 reicht die Fortsetzung weiter als die Daten).

## 4 Pflichtpruefung L4 (vor dem Einfrieren)

- **Ziele (bekannte Stellen, R wie in der Karte):** k = 0: 39,594 / 42,004; k = 1: 40,506 / 42,613; k = 2: 40,229 /
  42,351; k = 3: 39,765 / 41,912; k = 4: 36,92 (Nr 80); k = 5: 38,26 (Nr 86); k = 6: 37,19 (Nr 82); k = 7: 38,27
  (Nr 87). Beide Stufen. Genau der Testcode von Abschnitt 2 und 3 (Befehl test, Modus l4), danach ausw l4.
- **Bestanden, wenn alle 12 angenommen sind.** Berichtet: Abstand der Wurzel zur bekannten Lage, F-Umlauf gegen den
  bekannten Umlauf (Runde 18 bzw. HUELLEN-LEITER-3), Fortsetzungsfehler.
- Nicht bestanden: Kriterium berichtigen (nur am Kriterium, nicht an Zielen, Vorhersagen oder Wertung), erneut pruefen,
  jeden Durchgang unten in Abschnitt 4a dokumentieren. Erst nach einem bestandenen Durchgang einfrieren.
- **[Lesart] V0** wird am ersten Durchgang mit dem unveraenderten Entwurf gewertet (sonst waere V0 durch Nachbessern
  immer erfuellt); spaetere Durchgaenge werden berichtet.
- Die F-Umlaeufe aus L4 an der letzten bekannten Stelle jeder Kurve sind die Anfangsglieder fuer V3.

### 4a Durchgaenge

- **Durchgang 1 (Entwurf unveraendert, code/sprossen_vorab.py sha256 b06fbb8a...): bestanden, 12 von 12 angenommen.**
  Laeufe 15:18:24 bis 15:24:45 UTC (6 Teile, rc 0), formale Auswertung ausw l4 15:24:55 UTC
  (aus/l4-d1/l4-auswertung.json). Alle im ersten Start (Versuch 0), beide Stufen.

| k | R Karte | R gefunden | Abstand zur bekannten Lage (omega^2 / rho) | F-Umlauf St1/St2 (bekannt) | S-Umlauf | Stufenabstand | Fortsetzungsfehler / d_nb | max abs(W) |
|---|---|---|---|---|---|---|---|---|
| 0 | 39,594 | 39,59426 | 1,2e-14 / 4,0e-15 | +1/+1 (+1) | +1/+1 | 2,9e-10 | 3,1e-9 / 0,1617 = 1,9e-8 | 4,6e-11 |
| 0 | 42,004 | 42,00367 | 8,7e-14 / 3,3e-15 | -1/-1 (-1) | -1/-1 | 2,9e-10 | 1,9e-9 / 0,1613 = 1,2e-8 | 6,8e-11 |
| 1 | 40,506 | 40,50636 | 1,4e-14 / 5,2e-14 | +1/+1 (+1) | +1/+1 | 2,5e-10 | 4,9e-8 / 0,00797 = 6,1e-6 | 2,0e-10 |
| 1 | 42,613 | 42,61313 | 3,6e-13 / 2,7e-13 | -1/-1 (-1) | -1/-1 | 2,4e-10 | 3,7e-8 / 0,00720 = 5,2e-6 | 3,1e-10 |
| 2 | 40,229 | 40,22944 | 3,8e-14 / 2,2e-14 | -1/-1 (-1) | -1/-1 | 3,0e-10 | 4,2e-7 / 0,00809 = 5,2e-5 | 8,4e-11 |
| 2 | 42,351 | 42,35113 | 3,5e-14 / 1,3e-14 | +1/+1 (+1) | +1/+1 | 2,8e-10 | 2,5e-7 / 0,00729 = 3,4e-5 | 1,1e-10 |
| 3 | 39,765 | 39,76541 | 2,2e-15 / 1,0e-14 | +1/+1 (D2: +1) | -1/-1 | 5,5e-10 | 3,4e-6 / 0,01357 = 2,5e-4 | 8,9e-11 |
| 3 | 41,912 | 41,91233 | 6,9e-15 / 4,9e-14 | -1/-1 (D2: -1) | +1/+1 | 4,9e-10 | 2,2e-6 / 0,01223 = 1,8e-4 | 5,3e-11 |
| 4 | 36,92 | 36,91656 | 4,3e-9 / 1,5e-8 (Nr 80) | +1/+1 (+1) | -1/-1 | 1,1e-9 | 2,2e-5 / 0,02137 = 1,0e-3 | 2,0e-11 |
| 5 | 38,26 | 38,25564 | 2,0e-9 / 7,2e-9 (Nr 86) | +1/+1 (+1) | +1/+1 | 1,6e-9 | 4,2e-5 / 0,02484 = 1,7e-3 | 1,1e-10 |
| 6 | 37,19 | 37,19029 | 1,4e-9 / 7,2e-9 (Nr 82) | -1/-1 (-1) | -1/-1 | 2,5e-9 | 1,5e-4 / 0,03063 = 4,8e-3 | 4,1e-11 |
| 7 | 38,27 | 38,27163 | 8,9e-10 / 7,2e-9 (Nr 87) | -1/-1 (-1) | -1/-1 | 3,4e-9 | 3,7e-4 / 0,03285 = 1,1e-2 | 7,8e-11 |

  - Bekannte Lage: HL3-Sprossen als S-Wurzel (Abstand ~1e-13), Runde-18-Stellen als Halbierungslage (auf ~1e-8 genau).
  - F-Umlauf gleich dem bekannten Umlauf an allen 12, auch auf k = 4 bis 7 (Runde 18), dort erstmals geprueft. S dreht
    k = 3 (beide) und k = 4 (Nr 80), wie in HUELLEN-LEITER-2 und -3 gesehen.
  - Rang an allen 12 = k auf beiden Stufen; sigma2/sigma1 <= 3,1e-10; |W| <= 1e-10 an 9 von 12 (k = 1 und 2 / 42,351
    bis 3,1e-10).
- **Zusatzpruefung vor dem Einfrieren (keine Aenderung am Kriterium):** Befehl fortfehler (aus/fortfehler.json): Bei zwei
  Sprossenschritten liegt der Fehler auf k = 4 bis 7 an den reifen Stellen bei 0,0056 (Nr 80), 0,0096 (Nr 86) und 0,034
  (Nr 82) des Nachbarabstands, an der fruehen Stelle Nr 87 (k = 7, aus Nr 49, 57, 66) aber bei 0,124, also ueber der
  Schwelle. Deshalb geprueft, wie weit die tatsaechliche Fortsetzung des Tests (letzte drei Stellen der Runde 18) die
  Kurve trifft: gegen die Zeilennullstellen mit Rang k an den 8 HL3-Wurzeln (R 39,59 bis 42,61, nur Lagen, keine
  Vorzeichen; hilfs/fort-zeilen.jq, Ausgabe hilfs/fort-zeilen-ausgabe.tsv): Fehler / d_nb hoechstens 0,0044 (k = 4),
  0,0040 (k = 5), 0,0141 (k = 6), 0,0158 (k = 7, bei R = 42,61). Erwartung fuer k = 7 bei 43,03: ~0,02. Die Schwelle 0,1
  bleibt also mit Faktor >= 5 frei. Kein zweiter Durchgang noetig.
- Nebenbefund dieser Pruefung: Die Kurve k = 5 liegt bei R = 40,506 bei rho = 1,24835; die bekannte Stelle aus
  HUELLEN-LEITER-2 (R = 40,487, rho = 1,24841) liegt also auf k = 5 (Erwartung Abschnitt 8). Die Vorhersage k = 5 / 40,51
  ist damit nicht blind (Kartennachtrag 1); die Wertung folgt Abschnitt 7.

## 5 Test (nach dem Einfrieren)

- Ziele (Karte, woertlich): k = 0: 44,414; k = 1: 44,720; k = 2: 44,473; k = 3: 44,059 (Toleranz +-0,06); k = 4: 39,13 /
  41,33; k = 5: 40,51 / 42,76; k = 6: 39,51 / 41,83; k = 7: 40,65 / 43,03 (Toleranz +-0,12). Beide Stufen, Befehl test
  (Modus test), danach ausw test.

## 6 Wertung

- **V0:** L4 bestanden (erster Durchgang, Abschnitt 4).
- **V1:** eingetroffen, wenn alle 4 Sprossen k = 0 bis 3 angenommen sind und je |Delta R| <= 0,06. Sonst nicht.
- **V2:** eingetroffen, wenn mindestens 7 der 8 Sprossen k = 4 bis 7 angenommen sind mit |Delta R| <= 0,12. Sonst nicht.
- **V3 [Lesart wie HUELLEN-LEITER-3 P2']:** Folge je Kurve: k = 0 bis 3: zweite Sprosse aus HUELLEN-LEITER-3 (F-Umlauf
  aus L4), dann die neue; k = 4 bis 7: letzte Stelle der Runde 18 (F-Umlauf aus L4), dann die zwei neuen nach R.
  Gewertet werden Schritte zu einer neuen Sprosse zwischen direkt aufeinander folgenden angenommenen Gliedern (ein nicht
  angenommenes Glied unterbricht). Ein Schritt ist erfuellt, wenn der F-Umlauf auf beiden Stufen gleich ist und das
  Vorzeichen wechselt. Eingetroffen, wenn alle gewerteten Schritte erfuellt sind und es mindestens einen gibt; nicht
  eingetroffen, wenn einer nicht erfuellt ist; offen ohne gewerteten Schritt. Berichtet wird je Kurve.
- **Bedeutung (Karte, woertlich):** V1 bis V3 eingetroffen (und L4 bestanden) -> "Die Sprossenregel sagt neue stille
  Stellen vorab gewertet voraus [H, im Modell gestuetzt]." **[Lesart]** "Abweichungen > 0,3" = mindestens eine der 12
  Sprossen angenommen mit |Delta R| > 0,3 oder nicht gefunden -> "Die Regel bricht jenseits R ~ 42 zusammen; Grund
  suchen." Der Ausloeser (welche Sprosse, angenommen oder nicht) steht immer dabei (Fremdstimme L3). Sonst
  Zwischenausgang ohne diese Aussagen.

## 7 Zusatzvorgabe der Leitung (KARTE-NACHTRAG-1, 17:09:55, vor jedem Lauf; getrennt gekennzeichnet)

- Bekannte Stelle aus HUELLEN-LEITER-2: omega^2 = 0,7621818033, rho = 1,2484145323, R = 40,48736 (Stufe 1), Kurve
  unbestimmt. Faellt eine angenommene Sprosse mit ihr zusammen (|R - 40,48736| <= 0,01 und |rho - 1,24841| <= 0,005),
  wird sie als "nicht blind" markiert. Die Kurve folgt aus demselben Annahmekriterium (Abschnitt 2).
- V2 dann zusaetzlich ohne diese Sprosse: "mindestens 6 von 7". Nur Nebenlesart; das formale V2 bleibt.
- Formal V0 bis V3 unveraendert.

## 8 Erwartung vorab (Schreibtisch, [H], nicht gerechnet)

- Die Stelle bei R = 40,487, rho = 1,2484 liegt nach Augenmass auf k = 5 (letzte k = 5-Abstaende in rho -0,0118,
  -0,0099, naechster ~ -0,0084 -> rho ~ 1,2484 bei R ~ 40,5). Erwartung: die k = 5-Sprosse 40,51 wird "nicht blind".
- Fortsetzungsfehler (Handrechnung k = 4, zwei Schritte bis R = 41,9 gegen die Zeilennullstelle mit Rang 4 aus
  HUELLEN-LEITER-3): ~5e-5 bei d_nb ~0,017, also ~3 % der Schwelle. Fuer k = 1/2 (d_nb ~0,007) ein Schritt, ~3e-5.
- Risiko: k = 4 bis 7 sind unter S schon im K0-Bereich umlaufgedreht (HUELLEN-LEITER-2); F sollte die Konvention der
  Runde 18 haben, geprueft war das nur fuer k = 0 bis 3. L4 zeigt es fuer k = 4 bis 7 an Nr 80, 86, 82, 87.
- Risiko: Die dritten Sprossen k = 0 bis 3 (R 44,06 bis 44,72) liegen jenseits aller bisher mit F gerechneten Stellen
  (bis 42,61). Die F-Saat aus der Mitte waechst dort um weitere ~2 Groessenordnungen; die c-Loesung bleibt nach meiner
  Lesart exakt (ihre a/b-Anteile entstehen nur aus der Saat, ohne Rundungsbeimischung), ungeprueft.
- Nachtrag nach Durchgang 1 (vor dem Einfrieren): V0 eingetroffen (Abschnitt 4a).

## 9 Laeufe (.69, kleintest.sh, Spuren cpu bis cpu4, je <= 600 s)

- Ordner /home/fmh/fmhc-physics-remote/runde20-sprossen-vorab/ (code/, hilfs/, aus/, logs/, prof-st1/, prof-st2/), alle
  Pfade absolut.
- V0: py_compile. V1: Profile beider Stufen; Vergleich mit HUELLEN-LEITER-3. V2: L4 in Teilen je Stufe, ausw l4,
  fortfehler. Einfrieren. V3: Test in Teilen je Stufe, ausw test.
- Programmfehler werden behoben und mit sha256 dokumentiert; Verfahren bleibt. Nachtraege nur eingefroren
  (PLAN-NACHTRAG-n.md.eingefroren-*), als nachtraeglich markiert.
