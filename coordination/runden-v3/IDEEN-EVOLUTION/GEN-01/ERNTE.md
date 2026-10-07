# GEN-01 Ernte (frischer Leser, blind zur Herkunft)

- Beginn (date): 2026-09-30 09:57:05 CEST
- Ende (date): 2026-09-30 10:06:14 CEST (Zeitbox 30 min, verbraucht 9 min)
- Gelesen je Karte: KARTE.md, NACHTRAG.md, LAUF.txt, lauf-69-kopie/ (Kettenprotokoll LAUF-G1xx.log, kette-zeilen.txt,
  Berichte, JSON per jq). Nicht gelesen: pool.jsonl, GEN-01.md, GEN-01-VORSCHLAG.md, HERKUNFT.md, formprobe/-Ordner und
  formprobe-*.log. Herkunft (Arm, Operator, Eltern) ist mir nirgends begegnet; sichtbar waren nur die Kuerzel der
  Test-Agenten T-1 und T-2 in den Nachtraegen und zwei Ordnernamensschemata auf der .69 (ie-gen01-, evo-gen01-).
- Zeitzone: .69-Zeiten UTC, Kartenzeiten CEST (= UTC + 2 h). Aenderungszeiten (stat) der KARTE.md stimmen bei allen zehn
  Karten mit der Zeile "Vorhersage geschrieben" ueberein (07:52:18 bzw. 07:58:24 CEST); alle NACHTRAG.md liegen vor dem
  ersten "start" des jeweiligen echten Laufs.
- Nichts gerechnet; Zahlen sind woertlich aus den Ausgabedateien.

## Tabelle

| G-Nummer | vorab belegbar | Vorhersage getroffen | L1 | L2 | L3 | L4 | L5 | Vorschlag | Grund |
|---|---|---|---|---|---|---|---|---|---|
| G1-01 Gitter-Pinning 1D | ja: Vorhersage 07:58:24, Nachtrag 2 08:17:14 CEST; erster Start 06:19:08 UTC = 08:19:08 CEST | ja nach Kartenregeln (V1 c_fit 12,36 in 10-18; V2 A_E(0,5) = 1,26e-9; V3 Snaking bei h = 1, nicht bei 0,25; V4 A_E(0,25) = 7,1e-15; Gegenprobe und Ordnung 2 mit 3,995/3,919 bestanden), aber Plausibilitaet bei h = 1 und 0,75 gerissen (siehe Abweichungen) | ja | ja: h = 0,125 und 0,1 ohne Snaking, A_E 7,1e-15 und 1,07e-14 (unter der Aufloesung, obere Schranke 1,1e-14) | ja: A_E grob/fein rel. Aenderung 1,3e-11, 0,67 %, 0, 0; L3 bestanden | teilweise bekannt (Peierls-Nabarro, Snaking auf Gittern), Fundstelle aus dem Gedaechtnis: nicht geprueft | nein (Numerik-Hygiene) | parken (bekannt, Zweck erfuellt) | Absicherungsfrage beantwortet: Produktionsgitter h <= 0,25 zeigen auf dem Raster kein Pinning; kein Physik-Strang. Vor Weiterverwendung des c-Fits klaeren, dass zwei seiner drei Stuetzpunkte (h = 1 und 0,75) die f^2-Schranke reissen. |
| G1-02 Stufe, Spaltfenster | ja: Vorhersage 07:52:18, Nachtrag 07:58:39, Leitungsentscheid 08:06:14 CEST (mtime 08:06:21); erster Start 06:06:42 UTC = 08:06:42 CEST, Hauptlauf 08:14:35 CEST | kein Ausgang (bindend, urteil_grob und urteil_fein: "Plausibilitaetsschranke nicht bestanden"). Einzelpruefungen im Urteil: V1 erfuellt (dT 0,994, W 0), V2 erfuellt (dT 0,104, 8 gespaltene Rasterpunkte, monoton), V3 eine Verletzung (zulaessig sind < 2), V4 erfuellt, beide Gegenproben bestanden | ja | ja: B = 25 dT 0,993, W 0; V2 = 0 alle 10 durch | ja: 40 Paare, Klassen gleich, max abs dq_durch 0,0009, Effekt 0,89 | nicht geprueft (NLS-Solitonen an Barrieren als Literatur genannt, ohne Fundstelle) | nein (Analogon ohne Zahl) | parken (Umbau) | Summenregel q_durch + q_zurueck + q_frei = 1 reisst in 4 von 40 Laeufen (grob und fein gleich), drei davon in den Klassen reflektiert/angeschlagen/durch bei V2 = 0,05 mit 3 bis 4 % nicht zugeordneter Ladung; Umbau: Ladung der Stufenzone als vierten Anteil zaehlen oder spaeter auswerten (laut Leitung eine neue Karte). |
| G1-03 Teilung m = 2, Schwelle | ja: Vorhersage 07:58:24, Nachtrag 08:08:05 CEST; erster Start 06:19:08 UTC = 08:19:08 CEST | ja: V1 Folge 0,55 nein, 0,57 bis 0,70 ja (monoton); V2 gamma 0,0098 bis 0,118 nicht fallend, gamma^2-Nullpunkt 0,567 >= 0,52; V3 alle 15 Toechter Windung 0; scheitert false; Plausibilitaet alle Laeufe true | ja | ja: m = 0 bei 0,59 auf dem Raster bis T = 1200 keine Teilung, kein gamma-Fit | ja: gleicher Ausgang und Toechterzahl, gamma rel. Aenderung <= 2,3e-4 | teilweise bekannt (Instabilitaet drehender Q-Baelle), Fundstelle fehlt: nicht geprueft | nein | weiter | Schwelle liegt auf dem Raster zwischen 0,55 und 0,57, gestuetzt auf einen einzigen nicht teilenden Punkt; naechster Schritt 0,56 und laengeres T bei 0,55, weil t_teilung zur Schwelle waechst (440 bei 0,57) und "bis 1200 nicht gesehen" ein langsamerer Zerfall bleiben kann [Hypothese]. |
| G1-04 Domaenenwaende als Keime | entfaellt (kein Lauf); Vorhersage 07:52:18, Parkung 08:12:44 CEST | nicht getestet | ja laut Karte (drei Wege in V3, dazu Lauf 6) | vorgesehen (Laeufe 4, 5, 6), nicht geprueft | nicht geprueft | teilweise (Spinor-Kondensate: Sadler 2006, Stamper-Kurn/Ueda 2013, aus dem Gedaechtnis) | Analogie ohne Zahl | parken (nicht getestet) | Kein Code wegen Zeitbox; vor einem Lauf ist laut Nachtrag die Saatfrage (Saat 21 in beiden Komponenten gaebe dasselbe Rauschmuster) von der Leitung zu entscheiden. |
| G1-05 Sattel-Knoten, Bremsschwelle | ja: Vorhersage 07:52:18, Nachtrag 08:11:45 CEST (Rechenweg geaendert, keine Formprobenzahl verwendet); erster Start 06:19:08 UTC = 08:19:08 CEST | nein: V1 bei C0 = 0,1 verfehlt, u_SN/c_s = 0,64 gegen [0,33; 0,53]; C0 = 0,3: 0,76 in [0,54; 0,77]; Bericht: "scheitert (V1)". Teil (b) nicht gebaut, V2/V3 nicht entscheidbar | ja | nicht geprueft (lam = 0 und u = 0 gehoeren zu Teil b) | ja fuer Teil a: h und h/2 gleich (0,64/0,64; 0,72/0,72; 0,76/0,76) | teilweise (1D-NLS-Stroemung bekannt), ohne Fundstelle: nicht geprueft | teilweise (Kondensat-Experiment, kein Zahlvergleich) | parken (Umbau) | Nach Kartenregel scheitert V1; zugleich reisst die eigene Kontrolle "gestreckt" bei allen drei C0 (0,42/0,57/0,645 gegen 0,304/0,495/0,584, Toleranz 0,05), die u_SN-Zahl ist damit nicht gesichert. Erst die Kontrolle klaeren; bleibt V1 dann verfehlt: verwerfen. |
| G1-06 Zweistufiger Einfang | entfaellt (kein Lauf); Vorhersage 07:52:18, Parkung 08:12:44 CEST | nicht getestet | ja laut Karte (Exponent, Linie, Bilanz) | vorgesehen (Paket allein, Ball allein, nicht resonant), nicht geprueft | nicht geprueft | teilweise (Manton/Merabet 1997, Griest/Kolb 1989, aus dem Gedaechtnis) | Analogie ohne Zahl | parken (nicht getestet) | Kein Code wegen Zeitbox; Nachtrag weist auf einen ungetrennten Beitrag hin (das Paket kann selbst bei 2 nu - omega abstrahlen), der vor einem Lauf in die Messregel gehoert. |
| G1-07 Tod ohne Mindestladung 1D | ja: Vorhersage 07:52:18, Nachtrag 08:03:49 CEST; erster Start 06:06:42 UTC = 08:06:42 CEST | ja (1D): V1 p = 0,506, Q_d(1e-3) = 0,193; V2 omega-Abw. <= 4,2e-4, omega vor Bruch < 1; V3 Verhaeltnis 0,496; V4 q_rel 0,956, omega Ende 0,9995; Urteil: "getroffen (1D; 3D-Gegenprobe offen)" | ja | teilweise: gamma = 0 bestanden (dQ_in 7e-8); 3D-Vergleich nicht gebaut | ja: Q_d rel. Abw. <= 0,3 %, p 0,506/0,508, Effekt 0,70 gegen Aenderung 0,003 | teilweise bekannt (gedaempfte NLS-Solitonen: Karpman/Maslov 1977, Kivshar/Malomed 1989, aus dem Gedaechtnis): nicht geprueft | Analogie ohne Zahl | weiter (nur 3D-Gegenprobe) | Der 1D-Befund allein ist im Kleinball-Grenzfall (sech-Profil, Q ~ sqrt(eps)) vermutlich NLS-Literatur [Hypothese]; neu waere der Kontrast zu 3D mit Q_min, und genau dieser Teil (L2) fehlt. Fundstelle fuer L4 nachlesen. |
| G1-08 Glied 7, Vasiliev-Lokalitaet | entfaellt (kein Lauf, kein Papiertest) | nicht getestet | schwach (Karte und Nachtrag: kein Ausgang aendert Einstufung oder Zahl; V1 fast aus dem Titel ableitbar) | Gegensuche, nicht gemacht | entfaellt | ja (Ergebnis waere selbst Literatur) | nein | parken (L1 schwach) | Kann laut Regel nicht weiter; Lesen bleibt der Leitung freigestellt und liefert hoechstens einen Satz fuer den Glied-7-Nachtrag. |
| G1-09 Blase im Tropfen | ja: Vorhersage 07:58:24, Nachtrag 2 08:14:16 CEST; erster Start 06:19:08 UTC = 08:19:08 CEST; T_E im Lauf vor der Zeitentwicklung berechnet (14,95/24,56/37,44), Kartenwerte 15/25/37 passen | nein: V1 verfehlt (t70 zu T_E: -35 %, -25 %, -9,6 % bei R0 = 8/12/18), V2 verfehlt (t70/t70_unbegrenzt 0,523/0,540/0,543, Abfall -0,02 statt >= 0,10), V3 erfuellt; Kennzahlen: scheitert true, plausibilitaet_bestanden false | ja | ja dem Effekt nach (R_v faellt um 30 % in 9,7 bis 33,9 Zeiteinheiten; ohne Leere R_d auf 0,0034 und S0 auf 3,5e-3 konstant), aber die eigenen Gegenprobe-Schranken S0 1e-3 und j_r 1e-4 sind gerissen: "gegenprobe bestanden: false" | ja: t70 grob/fein <= 0,07 % | teilweise (Blasen in Stoessen, Rayleigh-Plateau), ohne Fundstelle: nicht geprueft | nein | verwerfen (in dieser Form) | Die parameterfreie Energiebilanz sagt t70 um 10 bis 35 % zu lang voraus, und die Endlichkeitsverkuerzung ist auf dem Raster nicht gesehen; Plausibilitaet bei R0 = 18 gerissen (Inkompressibilitaet 6,1 % > 5 %). Die fast konstante Zahl t70/t70_unbegrenzt = 0,52 bis 0,54 ueber R0 = 8 bis 18 waere eine neue Hypothese fuer eine eigene Karte. |
| G1-10 Stille Atmung in H^3 | entfaellt (kein Lauf); Vorhersage 07:58:24, Parkung 08:10:20 CEST | nicht getestet | ja laut Karte (Vorzeichen, Exponent, Groesse, Dimensionsvergleich) | vorgesehen (R_c = 1e4, Arm A), nicht geprueft | nicht geprueft | teilweise (Q-Baelle in AdS/H^3, aus dem Gedaechtnis) | nein | parken (nicht getestet) | Kein Code; Umbau von bic2_v2.py liegt laut Nachtrag an der 1-h-Grenze. |

## Abweichungen in beide Richtungen

### Vorwaerts (Aussagen der Karten und Urteile gegen die Dateien)

- G1-01: Es gibt keinen eigenen Urteil-Bericht; das Urteil folgt aus den Kennzahlen in haupt_ergebnis.json und
  gegen_ergebnis.json (V1 bis V4 true, gegenprobe_monoton_und_klein true, Ordnung 2 true, L3 true). Alle Zahlen der
  Tabelle stehen dort. Die Kartenregel "Scheitert, wenn" enthaelt die Plausibilitaetsschranke nicht; was ein Riss der
  Schranke fuer das Urteil bedeutet, legt die Karte nicht fest.
- G1-02: urteil_grob_bericht.txt und urteil_fein_bericht.txt tragen jede Zahl der Tabelle; der bindende Ausgang ist dort
  "kein Ausgang". Das Papier (papier_bericht.txt) gibt v_cl 0,10299/0,22541/0,31075/0,41917 und Pi 0,103/0,514/1,027/2,054,
  wie im Nachtrag genannt.
- G1-03: Alle Zahlen in teilung_haupt_grob_bericht.txt, teilung_haupt_fein_bericht.txt und teilung_gegen_grob_bericht.txt.
  Der fein-Aufruf uebernimmt V1 bis V3 aus der grob-Datei (grob_quelle), wie LAUF.txt sagt.
- G1-05: "Ausgang Teil a: scheitert (V1): C0 0.1 u_SN/c_s 0.64" in umstroemung_0.1_bericht.txt; C0 = 0,3 und 0,2 melden
  "V1 erfuellt (Teil a); Teil b offen". Die Vorgabe fuer Teil (b) (u/c_s 0,57 bis 1,02) enthaelt einen ueberschalligen
  Punkt, wie der Nachtrag vorab vermerkte.
- G1-07: urteil_grob_bericht.txt traegt alle Zahlen; Ausgang "getroffen (1D; 3D-Gegenprobe offen)".
- G1-09: Kennzahlen im haupt-Bericht: V1 false, V2 false, V3 true, scheitert true, L3 true, plausibilitaet false;
  gegen-Bericht: gegenprobe bestanden false. Alle Zahlen der Tabelle stehen dort.
- Zeitfolge: Bei keiner der sechs gelaufenen Karten liegt eine Vorhersage oder ein Nachtrag nach dem ersten "start".
  Knappste Abstaende: G1-02 (Leitungsentscheid 08:06:14 CEST, Datei 08:06:21, Start 08:06:42 CEST) und G1-01
  (Nachtrag 2 08:17:14 CEST, Datei 08:17:30, Start 08:19:08 CEST).

### Rueckwaerts (Befunde in den Dateien, die im Urteil fehlen oder nur teilweise stehen)

- G1-01: "Plausibilitaet bestanden: False" fuer den Hauptlauf, ohne Grund im Bericht. Grund laut JSON: "max f^2
  ausserhalb (0, 1 + 1e-9]" auf beiden Zweigen bei h = 1 (max f^2 = 1,000444) und h = 0,75 (1,0000109), grob und fein;
  h <= 0,5 bestanden (max f^2 < 1). Zwei der drei Stuetzpunkte des c-Fits (V1) kommen damit aus Gittern mit gerissener
  Schranke. Dass der Ueberschuss ein Gitterueberschwingen des Plateaus ist, ist eine Deutung [Hypothese]. Ausserdem nur
  im JSON: W_pin bei h = 0,75 negativ (-3,3e-6, innerhalb des zugelassenen Pinningbands); bis zu 19 (h = 1) bzw. 21
  (h = 0,75 und 0,5) Loesungen eines Zweigs bei einem omega^2. rc aller Aufrufe 0, kein NaN, abgebrochen leer.
- G1-02: Der Nachtrag erwartete den Riss der Summenregel nur fuer die Klasse "haengt"; tatsaechlich sind 3 der 4 Risse
  in anderen Klassen (V2 0,05: rel 0,90 reflektiert 0,9594; rel 0,95 angeschlagen 0,9710; rel 1,20 durch 0,9686), der
  vierte ist haengt (V2 0,01, rel 0,98: Summe 0,0059, q_mitte_ende 0,982). Der zweite haengt-Lauf (V2 0,01, rel 1,00)
  hat q_durch 0,994 und zugleich q_mitte_ende 0,461: zwei Zahlen, die nicht zusammenpassen; als Frage, nicht als
  Befund. Energiedrift max 8,2e-4 (haupt fein), unter 1e-3. Kette: "papier" lief auf Spur p4000a statt cpu (ohne
  Folge, --geraet cpu blieb). rc aller neun Aufrufe 0.
- G1-03: Spalte Q/E-Verlust 1,0/1,0 bei 0,61 bis 0,70 und 0,36/0,40 bei 0,57 und 0,59: nach der Teilung verlaesst die
  Ladung ganz oder zu einem Drittel den Suchkasten bis T; steht in der Tabelle, nicht in den Kennzahlen (die
  Erhaltungspruefung endet laut Karte bei 0,5 t_teilung). Bei 0,59 (grob und fein) steht am Ende nur eine Tochter mit
  Q 217,8 von 280,5, Jspin/Q 1,35, Windung 0, bei n_max 3: ob das eine Teilung oder eine Verformung mit Ladungsverlust
  ist, ist aus dem Bericht nicht entscheidbar (Frage). Die Schwelle stuetzt sich auf genau einen nicht teilenden Punkt.
  rc 0, kein NaN.
- G1-05: Die Kontrolle "gestreckt" (Naeherung an die hydraulische Zahl auf 0,05) ist bei allen drei C0 "ok False"
  (Abstand 0,116/0,075/0,061); die Ausgangszeile nennt nur V1. Die Kontrolle "lam klein" besteht (0,91/0,93/0,94 >= 0,9).
  Rechenweg vor dem Lauf geaendert (Schiessen von der Mitte statt vom Fixpunkt), im Nachtrag begruendet, keine Zahl der
  Formprobe verwendet. Kette: C0 = 0,3 lief auf Spur cpu statt cpu5 (ohne Folge). rc 0.
- G1-07: t90/t50/t10 sind in allen Laeufen nan (Schwellen von q_rel wohl nie erreicht [Hypothese]); im Urteil nicht
  erwaehnt. omega am Ende der Dauerlaeufe 1,00007 bis 1,00017 (> 1 nach dem Bruch; die Karte verbietet > 1 nur vor dem
  Bruch, dort 0,9977 bis 0,9995). Die Karte verlangt den 3D-Vergleich als zweite Gegenprobe; er wurde geparkt und das
  Urteil sagt es. rc 0.
- G1-09: Plausibilitaet bei R0 = 18 gerissen (inkompressibel_max_abw 0,0615 grob, 0,0612 fein, Schranke 0,05); in
  den Kennzahlen als plausibilitaet_bestanden false enthalten. Die Gegenprobe-Kennzahl nutzt nur die grob-Werte
  (S0 3,5e-3, j_r 3,3e-3); fein halbiert sie viermal (S0 8,7e-4 unter 1e-3, j_r 8,3e-4 weiter ueber 1e-4), ins
  Gegenprobe-Urteil nicht eingegangen. Q und E bis t_chk = 69,3 auf <= 1,3e-5 erhalten. "Torch-Speicher max nan MB"
  (CPU-Lauf, ohne Folge). rc 0, "Fehler: keine".
- G1-09 und G1-10: Der Nachtrag sagt, die Zeile "Vorhersage geschrieben: 07:58:24" sei um 08:10:20 angehaengt worden;
  die Aenderungszeit beider KARTE.md ist 07:58:24, also kein Widerspruch zur Vorab-Belegung.
- Allgemein: In keinem Kettenprotokoll rc ungleich 0, kein Traceback, kein "abgebrochen". Formprobe-Dateien lagen in
  sechs Ordnern und wurden nicht gelesen.

## Einfach gesagt

Von zehn Ideen wurden sechs wirklich gerechnet, und bei allen sechs stand die Vorhersage nachweislich vor dem Lauf.
Zwei Ideen trafen ihre Vorhersage sauber (die Teilungsschwelle des drehenden Balls, G1-03, und der langsam
abgesaugte 1D-Ball, G1-07), eine traf sie zwar, aber ihre eigene Sicherheitsschranke riss bei den groben Gittern
(G1-01). Zwei Ideen scheiterten an ihrer eigenen Vorhersage (Bremsschwelle G1-05, Blasenkollaps G1-09), und eine
konnte nicht entscheiden, weil ein Stueck Ladung in keiner Zaehlung landete (Stufe G1-02). Die vier ungetesteten
Ideen bleiben geparkt; eine davon (G1-08) kann von vornherein nicht scheitern und ist deshalb kein Test.
