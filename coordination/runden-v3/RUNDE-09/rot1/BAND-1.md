# BAND-1 (Runde 10): Reissprobe des Bands zwischen zwei Wirbeln

- Bearbeiter: Anthropic-Code-Agent (Opus 5.5), Fortsetzung von ROT-1 und REGGE-1. Explorativ (v3).
- Karte der Leitung 2026-09-30 10:26 CEST. Beginn 10:30:41 (date). Diese Vorab-Datei ist vor jedem BAND-1-Lauf
  geschrieben; Kopie BAND-1.md.eingefroren-<Zeit>.
- Frage [H]: Reisst das Band zwischen einem psi_1-Wirbel (A) und einem psi_2-Wirbel (B) bei grossem Abstand?
  - Denkbar: Ein neues Wirbel-/Antiwirbelpaar entsteht aus der Bandenergie (Analogon zum Stringbrechen, kein QCD-Anspruch).
  - Oder das Band zerschneidet den Ball.

## 1. Vorwissen (offengelegt)

- Band bei g = 0,5:
  - frei (paardyn, REGGE-1) eine Linse aus zwei Ising-Waenden, Kraft F = 1,5 bis 1,8
  - statisch mit Phasenklammer ein leerer Schlitz, Steigung 0,97; bei g = 0,2 statisch 0,61
- Intakte Baender bisher bis d = 9,5 (statisch) bzw. mittlerem d = 7,4 (frei), im Ball Q = 700 (R_halb ~ 12,3).
- REGGE-1, Q = 700: Bei d_0 = 11 (g = 0,5) ging das Paar verloren, der Ball wurde zerlegt (Q_w 196 von 700, 401
  geschluckt). Bei g = 0 und d_0 = 11 blieb alles ganz (Q_w 675). Bei g = 0,2, d_0 = 9 fehlte das Paar in 69 % der
  Analysen (Q_w 606).
- Energie eines einkomponentigen Wirbels (g = 0, S ~ 1, radial_ergebnis.json, E_v1 - E_b):
  10,25 / 10,86 / 11,61 / 12,63 bei Ballradius ~5 bis 7.

## 2. Schaetzung der Reisslaenge L_b (vor jeder Rechnung)

- Ein Paar (Wirbel + Antiwirbel) in einer Komponente des gemischten Balls (S_a = S_0/2 ~ 0,58 bei g = 0,5):
  - aus den Daten: je Wirbel etwa 0,58 x (10,3 bis 12,6) = 6,0 bis 7,3, als Paar E_pair ~ 12 bis 15
  - von Hand: E_pair(l) = 4 pi S_a ln(l/xi) + 2 c_1 = 7,24 ln(l/1,1) + 1,2 (xi ~ 1,1 aus der Anpassung der
    Wirbelenergie oben, Kern c_1 ~ 0,6)
- Reissbedingung sigma L_b = E_pair (QCD-Lesart: Die Bandenergie bezahlt das neue Paar):
  - freies Band (sigma = F ~ 1,6): L_b ~ 7,5 bis 9,5 (Datenschaetzung) bzw. ~11,5 (Handformel mit l = L_b)
  - statischer Schlitz (sigma = 0,97): L_b ~ 12 bis 15 bzw. ~25
  - **Arbeitswert: L_b(frei) ~ 8 bis 12, L_b(statisch) ~ 12 bis 25.**
- Zweite Reissart, geometrisch [Hand]:
  - Liegen A und B auf einem Durchmesser, kostet ein Band aus zwei Waenden 2 sigma d.
  - Eine Wand quer durch den ganzen Ball (Rand - A - B - Rand) kostet 2 R sigma. Die Waende koennen am Ballrand kostenlos
    enden.
  - Fuer d > R ist das Zerschneiden des Balls billiger: d_cut ~ R. Das passt zum Befund bei d_0 = 11, R ~ 12
    (Abschnitt 1).
- Vorbehalt: In der klassischen Rechnung (Temperatur null) braucht ein neues Paar eine Keimbildung ueber eine Schwelle.
  Energetisch erlaubtes Reissen muss also nicht eintreten. Die Anfangsabstrahlung des eingepraegten Starts ist die
  einzige "Unruhe".

## 3. Laeufe (vor der Rechnung festgelegt)

- **Groesserer Ball:** Q = 3600 (R ~ 28), Box L = 48 (n = 320 bei dx 0,3), Randschicht wie immer.
- **Frei** (bandfrei, Unterbefehl band, T = 300, g von Anfang an):
  - g = 0,5: d = 8, 14, 20, 26
  - g = 0: d = 14, 26 (ohne Band)
  - g = -0,5 mit psi_2 -> i psi_2: d = 20 (K4)
  - Fein (dx 0,2, dt 0,025): g = 0,5, d = 20
- **Festgehalten** (bandstat, Phasenklammer 0,5 < r < 2 um A und B, Q_1 = Q_2 = Q/2, 6000 Iterationen):
  - g = 0,5 und 0,2: d = 8, 14, 20, 26
  - dazu g = -0,5 mit psi_2 -> i psi_2 bei d = 20
- Messung frei, je 5 Zeiteinheiten:
  - Wirbelzahl je Komponente und Vorzeichen als Zahl zusammenhaengender Achter-Umlauf-Bloecke in r < 0,85 R
  - Lage von A und B
  - Wandkreuzungen auf einem Kreis um die Paarmitte (Radius d/2 + 3) und auf dem Randkreis r = 0,85 R
  - Klumpenzahl, Fensterladung, Bilanz
- Messung statisch: E(d), Wandkreuzungen auf dem Kreis um beide, Windung um A und B (r = 2,4).

## 4. Vorab-Erwartung (p)

| Nr. | Erwartung | p |
|---|---|---|
| B1 | frei, g = 0,5, d = 8 (< L_b): Band bleibt, keine neuen Wirbel bis T = 300 | 0,7 |
| B2 | frei, g = 0,5, d = 14 / 20 / 26 (> L_b): neue Wirbelpaare im Bandbereich (Reissen) in mindestens einem der drei Laeufe | 0,35 |
| B3 | frei, g = 0,5, d = 14 bis 26: Band bleibt in allen drei Laeufen verbunden, ohne neue Wirbel ("reisst nicht", metastabil) | 0,45 |
| B4 | frei, g = 0,5: Ball zerfaellt oder wird zerschnitten (>= 2 Klumpen oder Waende am Randkreis) in mindestens einem Lauf mit d >= 14 | 0,2 |
| B5 | frei, g = 0: keine neuen Wirbel, keine Waende | 0,8 |
| B6 | statisch g = 0,5 und 0,2: E(d) waechst linear bis d = 26 (Steigung d = 20 bis 26 mindestens 0,5 x Steigung d = 8 bis 14), keine Wandkreuzung auf dem Kreis um beide | 0,65 |
| B7 | K4: frei d = 20, Dichten -g (i psi_2) = +g auf <= 1e-9; statisch Energie gleich auf <= 1e-9 relativ | 0,95 |
| B8 | fein gegen grob (frei, g = 0,5, d = 20): gleiche Einordnung (reisst / reisst nicht / zerschnitten); Zeitpunkt des ersten Ereignisses auf 20 % | 0,6 |

## 5. Scheiterregel (vorab)

- **"Reisst nicht" (frei)**, wenn fuer alle d >= 14 bei g = 0,5 bis T = 300 gilt:
  - in r < 0,85 R genau ein psi_1- und ein psi_2-Wirbel (keine zusaetzliche Blockgruppe in >= 3 aufeinanderfolgenden
    Analysen)
  - der Kreis um die Paarmitte hat in >= 80 % der Analysen keine Wandkreuzung
  - der Ball bleibt ein Klumpen
- **"Reisst"**, wenn zusaetzliche Wirbelgruppen (beider Vorzeichen) in >= 3 aufeinanderfolgenden Analysen auftreten,
  waehrend A und B noch bestehen, oder wenn der Kreis um die Paarmitte in >= 3 aufeinanderfolgenden Analysen >= 2
  Wandkreuzungen zeigt (Band zum Rand umgelegt).
- **"Zerschnitten"**, wenn >= 2 Klumpen in >= 3 aufeinanderfolgenden Analysen oder der Randkreis Wandkreuzungen zeigt
  und die Fensterladung unter 80 % faellt.
- **Statisch:** "reisst nicht", wenn B6 erfuellt ist; "reisst", wenn die Steigung d = 20 bis 26 unter 0,3 x Steigung
  d = 8 bis 14 faellt oder der Kreis um beide Wandkreuzungen zeigt.
- Die Einordnung ist vor dem Ergebnis festgelegt. Bei Grenzfaellen gilt der Wortlaut.

## 6. Nachtrag vor weiteren Laeufen (10:43:42, date; nach bandstat, bandstat2, band grob und band fein)

- Beobachtet, aber noch nicht ausgewertet:
  - Frei: Der eingepraegte Dipol der relativen Phase bildet zuerst Waende entlang grosser Kreisboegen durch A und B
    (Radius d/sqrt 2, Mitte bei (0, +-d/2)).
    - Fuer d > R/(1/2 + 1/sqrt 2) = 0,83 R erreichen sie den Ballrand [Hand, nachtr.]. So zerfaellt der Ball bei d = 26
      (R 28,6). Ebenso zerfiel er in REGGE-1 bei d_0 = 11 (R 12,3; 0,83 R = 10,2).
    - Die Anfangsstoerung erzeugt Wirbeltruemmer im ganzen Ball.
  - Statisch: Bei grossem d verschiebt der Fluss den ganzen Ball, bis ein geklammerter Wirbel draussen im Vakuum liegt
    (Bild bandstat2_felder.png). Die Translation ist bei festem Q frei. Das ist kein neues Paar.
- Deshalb **ein weiterer freier Lauf "band2" mit duenner Anfangslinse**, gleiche Regeln (Abschnitt 5), gleiche Messung:
  - Delta_start = f(Delta_dipol) mit f(D) = 2 atan(sign(D) (\|tan(D/2)\|/cot(delta/2))^3). f ist monoton und behaelt
    die Windung. Delta ist ~0 ausser in einer Linse der halben Breite ~1,5 um die Strecke AB, delta = 4 x 1,5/d.
  - psi_1 = F/sqrt 2 v_A e^{i (D - f(D))/2}, psi_2 = F/sqrt 2 v_B e^{-i (D - f(D))/2}
  - g = 0,5: d = 8, 14, 20, 26; g = -0,5 mit psi_2 -> i psi_2 bei d = 20 (K4); fein: g = 0,5, d = 20
- Vorab zu band2 (vor dem Lauf):

| Nr. | Erwartung | p |
|---|---|---|
| B9 | band2, d = 26: der Ball bleibt ganz (kein Zerschneiden durch Anfangsboegen) | 0,6 |
| B10 | band2, d = 14 / 20 / 26: keine zusaetzlichen Wirbelgruppen im Bandbereich in >= 3 aufeinanderfolgenden Analysen ("reisst nicht" im Sinn des Paarbruchs) | 0,55 |
| B11 | band2: weniger Wirbeltruemmer ausserhalb des Bands als band (Hoechstzahl "sonst" kleiner) | 0,7 |

## 7. Nachtrag vor band3 (10:53:25 laut date, Lauf gestartet, Ergebnis noch nicht gesehen)

- band2 (duenne Anfangslinse) zeigt ab d = 14 zusaetzliche Blockgruppen im Bandbereich. Nach dem Bild (d = 26) duennt das
  Band dort zu einem Schlitz aus, in dem beide Komponenten verschwinden.
- Umlaeufe ueber einen Strich verschwindender Dichte mit Phasensprung pi sind mehrdeutig, wie die Plakette in ROT-1.
  Die Blockzaehlung trennt dort echte neue Wirbel nicht von Zaehlartefakten.
- **Diagnose band3** (nachtraeglich, nicht Teil der Scheiterregel; Physik identisch zu band2): zusaetzlich zaehlen nur
  Bloecke mit Gesamtdichte S > 0,3 S_max.
  - Ein echter neuer Einkomponenten-Wirbel im gemischten Ball hat einen gefuellten Kern (S gross) und wird gezaehlt.
  - Ein Artefakt auf dem Schlitz (S ~ 0) nicht.
- Erwartung vor dem Ergebnis:
  - Wenn das Band durch neue Wirbelpaare reisst, zeigt die strenge Zaehlung ab d = 14 zusaetzliche Gruppen (p = 0,4).
  - Wenn es nur zum Schlitz ausduennt, bleibt sie bei 0 (p = 0,6).

## 8. Ergebnis (eingetragen ab 10:56:02 laut date)

Quellen: lauf-69/ausgabe/band_grob_ergebnis.json, band_fein_ergebnis.json, band2_grob_ergebnis.json,
band2_fein_ergebnis.json, band3_grob_ergebnis.json, bandstat_ergebnis.json, bandstat2_ergebnis.json; Berichte
*_bericht.txt, Bilder *_g0.5_d*.png und bandstat2_felder.png; Logs LAUF11 bis LAUF17 (alle rc = 0).

### 8.1 Kurz

1. **Mit sauberem Start (duenne Linse, band2/band3) haelt das Band bei d = 8 und wirft ab d = 14 neue Wirbelpaare ab.**
   - Das ist ein Analogon zum Stringbrechen. Reisslaenge zwischen 8 und 14, Vorab-Schaetzung 8 bis 12.
   - d = 8: keine zusaetzliche Wirbelgruppe bis T = 300. Das Paar zieht sich zusammen (d 7,8 -> 1,3 bis 4,4), der Ball
     bleibt ganz (Q_w 0,997) [num].
   - d = 14 / 20 / 26: zusaetzliche Gruppen im Bandbereich, zuerst dauerhaft (>= 3 Analysen) bei t = 105 / 25 / 115
     [band2_grob: laeufe[].t_extra, band_bloecke_max 14 / 16 / 16].
   - Die strenge Zaehlung (nur S > 0,3 S_max) findet sie ebenfalls (4 / 4 / 2) [band3_grob: extra_streng_max]. Es sind
     also echte Einkomponenten-Wirbel mit gefuelltem Kern, keine Zaehlartefakte des Schlitzes.
   - Beispiel d = 14, t = 105 bis 115: gleichzeitig ein psi_1-Paar (+1/-1) und ein psi_2-Paar (+1/-1); danach wieder
     genau ein psi_1- und ein psi_2-Wirbel.
   - Ob die neuen Wirbel einander oder die alten Enden vernichten, zeigt die Zaehlung nicht.
   - Bis T = 300 bleibt ein durchgehender Strang (Schlitz mit Linse, Bild band2_grob_g0.5_d26.png). Zwei getrennte
     Stuecke ("zwei Mesonen") sieht man nicht. Das Band "flackert" durch Paarbildung, statt dauerhaft zu zerfallen [Bild].
2. **Mit dem Dipol-Start (band) dominiert die Anfangsstoerung.**
   - Wirbeltruemmer im ganzen Ball ab t = 10 fuer d >= 14; ausserhalb des Bands bis 64 Bloecke, im Bandbereich bis 24
     [band_grob: sonst_bloecke_max, band_bloecke_max].
   - d = 26 wird der Ball zerschnitten (bis 5 Klumpen, Q_w 0,52). Grund: Die ersten Waende laufen entlang der
     Dipolboegen, die fuer d > 0,83 R den Rand erreichen (R 28,6: Grenze 23,7) [Hand, nachtr.].
   - Dieselbe Grenze erklaert REGGE-1, d_0 = 11 im kleinen Ball (0,83 x 12,3 = 10,2).
   - Mit duenner Startlinse bleibt der Ball bei d = 26 ganz (1 Klumpen, Q_w 0,989): Das Zerschneiden ist eine Folge des
     Starts, nicht des Bands.
3. **Statisch (festgehaltene Enden, Klammer) haelt das Band bis d = 14; laengere Baender loest der Fluss, indem er den
   ganzen Ball von einer Klammer wegschiebt.** Kein neues Paar.
   - g = 0,5: E(14) - E(8) = 6,28, Spannung 1,05 (Q = 700: 0,97); konvergiert, Drift <= 5e-5 [bandstat2:
     konf[].E, dE_letzte1000].
   - d = 20 / 26: Ball verschoben, ein Wirbel draussen im Vakuum (Bild bandstat2_felder.png). E = 2284,3 / 2285,4, also
     11,8 unter dem Band bei d = 8, flach. Drift 0,09 / 0,93.
   - g = 0,2: schon ab d = 14 verschoben (E 2497,2 / 2495,0 / 2496,1 gegen 2510,8 bei d = 8).
   - Das ist ein Klammer-Artefakt (Translation bei festem Q frei) [num].
   - Der erste Lauf mit 6000 Iterationen war nicht konvergiert (Drift bis 4,8) und wird nicht gewertet.
4. **Kontrollen:**
   - K4 frei: Dichte -g (i psi_2) = +g auf 1,8e-13 (band) bzw. 3,5e-14 (band2); statisch E gleich auf 2,6e-11 absolut
     (1e-14 relativ).
   - Fein gegen grob (d = 20): band 10 / 10 (erstes Ereignis); band2 25 / 25 und 230 / 230, d(t) auf 0,3 gleich.
   - band3 reproduziert band2 in allen Standardspalten.
   - Bilanz: Q <= 8e-5 (band2), E <= 1,1e-3.
   - g = 0 (ohne Band): keine zusaetzlichen Wirbel (extra 0) bei d = 14 und 26.
5. **Belegstufe:**
   - Paarbildung ab d = 14 bei sauberem Start: [num+K] (fein fuer d = 20, K4, zweite Zaehlung). Ihr Verlauf (Vernichtung
     oder Ersatz der Enden) ist offen.
   - Reisslaenge 8 bis 14: [num], zwei Stuetzstellen.
   - Zerschneiden bei d > 0,83 R: [num] mit nachtraeglicher Handbegruendung.
   - Statischer Befund: [num], Klammer-Artefakt.

### 8.2 Scheiterregel (Abschnitt 5) nach Wortlaut

- Frei, Dipol-Start (band): d = 14 "zerschnitten" (2 Klumpen ab t = 95 fuer 3 Analysen), d = 20 "reisst", d = 26
  "zerschnitten"; d = 8 "reisst" (Truemmer t = 45 bis 55).
- Frei, sauberer Start (band2, band3; Nachtrag 10:43:42, gleiche Regel): d = 8 "reisst nicht"; d = 14, 20, 26 "reisst".
- Also ist "reisst nicht" fuer d >= 14 in beiden Startarten nicht erfuellt: **das Band reisst** im Sinn der Regel.
- g = 0: Die Regel meldet "reisst" ueber Wandkreuzungen auf dem Paarkreis (t = 255 bzw. 55). Ohne Kopplung gibt es aber
  keine Waende; n_e wechselt dort auch ohne Wand das Vorzeichen. Die Wirbelzahl bleibt 1 + 1. Das Wandkriterium ist bei
  g = 0 nicht anwendbar.
- Statisch:
  - g = 0,5: "reisst" (Steigung d = 20 bis 26 0,18 < 0,3 x 1,05); Ursache Ballverschiebung, nicht Paarbildung
  - g = 0,2: E faellt schon von d = 8 nach 14. Die Verhaeltnisklausel ist mit negativer Anfangssteigung nicht
    anwendbar. B6 ("E waechst linear") ist verletzt.

### 8.3 Vorab gegen Ausgang

| Nr. | Vorab | Ausgang | Bewertung |
|---|---|---|---|
| B1 | band, d = 8: Band bleibt, keine neuen Wirbel | Truemmer t = 45 bis 55 (Dipol-Start); mit Linse (band2) erfuellt | verfehlt (Startart) |
| B2 | neue Paare im Bandbereich bei d >= 14 in mindestens einem Lauf | band: d = 26 ab t = 20, d = 20 ab 155; band2: d = 14 ab 105 | getroffen |
| B3 | Band bleibt fuer d = 14 bis 26 ohne neue Wirbel | nein | verfehlt |
| B4 | Ball zerfaellt / zerschnitten in mindestens einem Lauf d >= 14 | band d = 26 (5 Klumpen, Q_w 0,52), d = 14 (2 Klumpen t = 95) | getroffen |
| B5 | g = 0: keine neuen Wirbel, keine Waende | keine neuen Wirbel; Wandkriterium nicht anwendbar | teilweise |
| B6 | statisch E linear bis d = 26 | Ballverschiebung ab d = 20 (0,5) bzw. 14 (0,2) | verfehlt |
| B7 | K4 <= 1e-9 | 1,8e-13 / 3,5e-14 / 1e-14 rel. | getroffen |
| B8 | fein = grob in Klasse, erstes Ereignis +-20 % | band 10/10, band2 25/25 | getroffen |
| B9 | band2 d = 26: Ball bleibt ganz | 1 Klumpen, Q_w 0,989 | getroffen |
| B10 | band2: keine neuen Gruppen im Bandbereich bei d = 14 bis 26 | in allen drei | verfehlt |
| B11 | band2: weniger Truemmer ausserhalb | sonst 0 / 12 / 16 / 8 gegen 18 / 38 / 50 / 64 | getroffen |
| band3 | Paarbruch: strenge Zaehlung > 0 (p 0,4); nur Schlitz: 0 (p 0,6) | 4 / 4 / 2 | Paarbruch-Zweig |

- Summe B1 bis B11: 6 getroffen, 1 teilweise, 4 verfehlt.

### 8.4 Einordnung [H]

- Das Band zwischen einem psi_1- und einem psi_2-Wirbel verhaelt sich wie ein Strang mit fester Spannung:
  - Spannung frei ~1,6, statisch ~1,0
  - Ab einer Laenge zwischen 8 und 14 bildet es neue Wirbelpaare. Die Groessenordnung passt zu E_pair/sigma
    (12 bis 15 / 1,6).
- Das aehnelt dem Stringbrechen, aber nur als Bild: kein Eichfeld, keine Farbladung; die neuen "Enden" sind Wirbel mit
  gefuelltem Kern.
- Dauerhaft getrennte Paare ("zwei Mesonen") sind bis T = 300 nicht gezeigt.
- Offen: Verfolgung der einzelnen Wirbel nach der Paarbildung, laengere Zeiten, groesserer Ball und g = 0,2 frei.

### 8.5 Verstoesse und Verfahren (Selbstanzeige)

- Zwei weitere lokale Interpreterstarts ohne Zweck, beide vor einer Bearbeitung, gerechnet wurde nichts:
  - kurz vor 10:33:36: leerer `python3 -` mit gequotetem Heredoc
  - zwischen 10:43:42 und 10:44:17: `python3 -c 1` am Ende eines sed-Befehls
  - Zusammen mit ROT-1 (08:11) sind es drei; bitte ins Arbeitsfeld.
- Laeufe: bandstat (6000 Iterationen, nicht konvergiert, nicht gewertet), bandstat2 (16000), band (Dipol-Start),
  band fein, band2 und band2 fein (Linse), band3 (Linse, strenge Zaehlung). Je Aufruf unter 4 min, Spuren p4000a und
  p4000b.
- Skript jeweils per neue Datei + mv ersetzt; kein git, keine Journaleintraege, keine Hooks.
- Y-1 nicht begonnen (Anweisung der Leitung).
