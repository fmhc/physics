# EVO-1: Evolutions-Pilot, Code und Befehle (Runde 7)

- **Auftrag:** Leitung (claude-primary) nach Finns Freigabe "Ja, sofort starten" (30.09.2026, ~04:28). Plan:
  ../GAUNTLET-NEUSTART-PLAN.md (im Folgenden "der Plan"). Dieser Ordner setzt ihn um; wo er abweicht, steht es in
  Abschnitt 6.
- **Bearbeiter:** Anthropic-Subagent (Opus 5.5). Kein ssh zur .69, kein git, kein Peerbus, keine Unteragenten. Nicht
  beruehrt: gauntlet/, RUNDE-07/bic2/ (dort nur gelesen: Definition des Log-Potentials), die Datensperren.
- **Beginn (date):** 2026-09-30 04:28:42 CEST. **Schwellen festgelegt (Abschnitt 3, date):** 2026-09-30 04:46:33 CEST,
  vor dem ersten gerechneten Modell (auch vor dem Rauchtest).
- **Ende (date):** 2026-09-30 04:59:20 CEST (gemessen nach dem letzten Lauf und vor diesem Eintrag). Code-Zeit
  etwa 04:38 bis 04:59, also unter 1 h (A6).
- **Status:** Code fertig, lokaler Rauchtest bestanden (Abschnitt 8). Generation 0 ist ungerechnet; sie laeuft auf der
  .69 durch die Leitung.
- **Versehen:** In einem Pruefbefehl stand ein ssh-Probeaufruf an localhost (BatchMode, 1 s Zeitgrenze). Er hatte keine
  Wirkung und hat die .69 nicht beruehrt. Dazu kamen zwei Kurzaufrufe von python3 (print, import torch) ausserhalb des
  Rauchtests.
- **Gelesen:** der Plan, runden-v3/README.md und kleintest.sh, RUNDE-07/IDEATION-UEBERSICHT.md (Kopf), RUNDE-07.md,
  RUNDE-06.md (3D-Resonanz und Berichtigung 04:05:59), RUNDE-06/ERGEBNISSE-R6-B.md (Abschnitt 2, Auffaelligkeiten),
  resonanz3d.py ganz, die Logs in resonanz3d/lauf-lokal/, bic2.py (Kopf und Potentialteil).

## 1. Dateien

| Datei | Inhalt |
|---|---|
| evo1.py | Pilot: Unterbefehle modell, generation, zusammenfassen, rauch |
| resonanz3d.py | unveraenderte Kopie aus RUNDE-06/resonanz3d/ (sha256 99c54b9ccdb517c1a033669cd664586e642f59fc58f82fd6df8f0d83b7b5bcb0, gleich dem Original) |
| PLAN.md | diese Datei |
| rauch/ | lokaler Rauchtest (rauch_bericht.txt, anker-klein/) |
| gen-00N.json, bew-00N.jsonl, ergebnisse/KEY/ | entstehen erst auf der .69 (Genome, Bewertungen, Rohdaten je Modell) |

## 2. Was evo1.py rechnet

- **Modelle:**
  - Familie P: U = S - S^2 + beta S^3 + gamma S^4, Box beta in [0,15; 1,2], gamma in [0; 0,3]. Anker beta = 1/2, gamma = 0.
  - Familie L: U = ln(1 + S), genau wie bic2.py sie definiert (POT_LOG). Sie hat keinen freien Parameter (Abschnitt 6).
- **Rechenkern:** resonanz3d.py bleibt unveraendert. evo1.py ersetzt nur die modellabhaengigen Teile:
  - koeffizienten, g_u, g_strich: Buckel des Teilchenpotentials und Taylor-Koeffizienten c1 bis c7. Fuer gamma = 0 werden
    die Originalfunktionen gerufen, der Anker rechnet also auf demselben Rechenweg wie Runde 6 (Uebereinstimmung auf
    allen gedruckten Stellen; zur Gleichheitspruefung siehe Abschnitt 13).
  - lin_aufbau: dp = U' + S U'', sp = S U''. Fuer gamma = 0 sind es dieselben Ausdruecke wie im Original, plus 0,0.
  - Ladung Q und Energie E in dim = 1 oder 3.
  - Fuer L ein eigenes Schiessen in f0, weil ln(1 + S) keinen Buckel hat.
  - Unveraendert aus resonanz3d.py: det, newton, kontur, lokale_minima, f_werte, radius_wo, r_halb, Profil-Schiessen fuer P.
- **Stufen wie Runde 6:** A h = 0,02 (f_rand 1e-6), B h = 0,01 (1e-8), C h = 0,005 (1e-10); Profil jeweils mit h/2.
- **Ablauf je Modell** (`modell`), in Punkte zerlegt:
  1. Grob: 12 omega^2-Punkte von omega_min^2 + 0,02 bis 0,93 (L: 0,02 bis 0,93), Stufe A. Am Startpunkt (Index 6)
     Polsuche wie Runde 6 (700 Keime auf der reellen Achse, 160 x 4 in der Flaeche, Newton) und Konturzaehlung im Kasten
     1 - omega + 0,002 < Re rho < min(1 + omega - 0,002; 9), -0,1 < Im rho < 0,001. Verfolgt wird der schmalste
     gefundene l = 0-Pol, erst aufwaerts, dann abwaerts, Keim linear aus den zwei Vorgaengern. Profile, Q und E an allen
     12 Punkten.
  2. Fein (nur wenn F0, F1 und mindestens ein grobes Minimum vorliegen): je grobem Minimum (hoechstens 3, tiefstes
     zuerst) 6 Punkte x_est + (-0,02, -0,002, -0,0005, +0,0005, +0,002, +0,02) auf Stufe A und B, Stufe C an den zwei
     tiefsten, Konturzaehlung auf Stufe B am tiefsten Punkt.
  3. Zusatzpunkte (nur Anker: 0,798) auf Stufe B und C; sie gehen nicht in F2 ein.
- **Zeitwaechter:** Budget 540 s je Aufruf. Ein Punkt beginnt nur, wenn 1,3 x die bisher laengste Dauer dieser Art
  (vor der ersten Messung: Start 150 s, A 40 s, B 90 s, C 200 s, Kontur 90 s) noch ins Budget passt. Sonst endet der
  Aufruf mit "offen"; derselbe Befehl setzt fort. Kein Punkt wird abgebrochen. Nach jedem Punkt wird zustand.json
  gesichert, am Ende jedes Aufrufs modell.json (Bewertung).

## 3. Messgroessen und Schwellen (festgelegt 2026-09-30 04:46:33 CEST, vor dem ersten Modell)

Die Zahlen stehen auch als Konstanten in evo1.py (F0_W2MIN, F0_PROFILE, F1_WMIN, F2_R2, F2_G0_REL, F2_BC_REL, F2_BC_ABS).
Sie aendern sich nach dem ersten gerechneten Modell nicht mehr. Ausnahme ist nur eine Reparatur nach A1 vor Generation 1;
sie wird hier mit Grund und date eingetragen.

- **F0 lebensfaehig:**
  - P: omega_min^2 = min_S U(S)/S >= 0,02 (analytisch). Sonst "nicht lebensfaehig", ohne Rechnung.
  - L: U/S > 0 fuer alle S > 0, das Infimum 0 wird nur fuer S -> unendlich erreicht; das Vakuum ist nicht entartet.
    L gilt als lebensfaehig (Abschnitt 6).
  - Dazu Profile an mindestens 10 der 12 Scanpunkte (Profil gilt, wenn f am Abschnitt < 1e-3 f0). Sonst "nicht
    entscheidbar" (Abschnitt 6).
- **F1 stabiles Fenster W:** Scanpunkte mit dQ/domega^2 < 0 (zentrale Differenz der Nachbarn mit Profil, am Rand
  einseitig) und E/Q < 1. F1 = ja, wenn W mindestens 3 Punkte hat. F1 ist ein Filter: Ohne F1 entfaellt die Verfeinerung.
- **F2 Nullstelle der Breite** (Gamma = -Im rho des verfolgten l = 0-Pols):
  - **Grob:** Die Polspur ist das zusammenhaengende Stueck um den Startpunkt, auf dem Newton konvergiert (|D| < 1e-8)
    und der Pol im Kasten bleibt. Gesucht ist ein inneres lokales Minimum von Gamma (lokale_minima aus resonanz3d.py).
    **Seit Version 3 (Abschnitte 12 und 13):** Ein inneres Minimum zaehlt nur, wenn beide Nachbarn auf der Spur auf Stufe A
    Gamma > G_BODEN = 1e-8 haben; weggefallene Minima stehen in modell.json unter grob_minima_unter_aufloesung.
    Bei mehreren werden bis zu drei verfeinert, das tiefste zuerst; alle werden berichtet. Keines: F2 = nein. Spur kuerzer als 3 Punkte oder kein Startpol
    bei Umlaufzahl ungleich 0: nicht entscheidbar. Kein Startpol bei Umlaufzahl 0 (aufgeloest): F2 = nein.
  - **x_est:** linearer Ansatz fuer +-sqrt(Gamma) zwischen dem groben Tiefpunkt k und dem tieferen Nachbarn (dort liegt
    der Vorzeichenwechsel).
  - **Fein:** 6 Punkte wie oben. Die "sechs naechsten Punkte" des Plans sind genau diese sechs.
  - **Messmittel-Pruefungen** (eine verfehlt: "nicht entscheidbar", zaehlt fuer A3):
    - a) Alle 6 Punkte haben auf Stufe B einen konvergierten Pol.
    - b) Stufen A und B ordnen die 6 Gamma-Werte gleich.
    - c) Am tiefsten Punkt (Stufe B) gilt |Gamma_B - Gamma_C| < 0,05 Gamma_C + 1e-9.
    - d) Konturumlaufzahl l = 0 im Kasten am tiefsten Punkt (Stufe B) = 1, Kontur aufgeloest.
  - **F2 = ja, wenn alles gilt:**
    - e) Der tiefste der 6 Punkte ist einer der vier inneren (nicht x_est +- 0,02).
    - f) Vorzeichenwechsel und Linearitaet: +-sqrt(Gamma) mit Vorzeichenwechsel direkt links oder rechts vom tiefsten
      Punkt (die Variante mit dem groesseren R^2). Die Gerade durch die vier inneren Punkte (x_est +- 0,002, +- 0,0005)
      hat R^2 >= 0,99. (Kalibrierung siehe unten.)
    - g) Die Nullstelle der Geraden und x* der Parabel liegen im Feinbereich [x_est - 0,02; x_est + 0,02].
    - h) Boden: Gamma = c (x - x*)^2 + g0 an die 6 Punkte (Stufe B), kleinste Quadrate mit relativen Residuen (Gewicht
      1/max(Gamma, 1e-9)). Es gilt g0 <= 1e-3 x Gamma_ref, Gamma_ref = min(Gamma(x_est - 0,02), Gamma(x_est + 0,02)).
  - omega*^2 := x* der Parabel.
  - **Modell:** F2 = ja, wenn ein verfeinertes Minimum F2 besteht. Besteht keines und ist eines "nicht entscheidbar",
    heisst das Modell "nicht entscheidbar". Berichtet wird x* des besten Minimums: erst F2 und F3, dann F2, dann das
    kleinste g0/Gamma_ref.
  - **Kalibrierung von f), vor jeder echten F2-Auswertung (Rauchtest 04:48:50 bis 04:54:14, date):**
    - Die erste Fassung um 04:46:33 nahm die Gerade durch alle sechs Punkte.
    - An drei synthetischen Kurven gab sie R^2 = 0,9894 fuer eine ankerartige V-Form, 0,9878 fuer dieselbe mit Boden 1e-6
      und 0,9892 fuer einen monoton fallenden 1D-artigen Verlauf. Der Anker haette also F2 verfehlt, und R^2 trennte
      nicht.
    - Die ankerartige Kurve ist a = -1,04 u + 6,8 u^2, u = omega^2 - 0,79768. Die Steigung 1,2 bzw. 0,8 im Abstand
      -0,013 bzw. +0,017 passt zu den Runde-6-Werten 1,18 und 0,77.
    - Grund: Ueber +-0,02 aendert sich die Steigung von sqrt(Gamma) beim Anker um etwa +-20 %. Der Plan belegt Linearitaet
      auf 1 bis 5 % nur ueber 0,796 bis 0,801.
    - Neue Fassung (04:52:59): R^2 der vier inneren Punkte. Ergebnis: ankerartig 0,99992 (F2 ja), Boden 0,99572
      (scheitert an h, g0/Gamma_ref = 2,5e-3), monoton 0,99939 (scheitert an e, g und h).
    - Bis dahin war kein echtes Modell mit F2 ausgewertet. Der Kleinstufen-Ablauf des ersten Rauchtests endete vor der
      Verfeinerung (Status offen).
- **F3 Lage:** Die beiden groben Scanpunkte, zwischen denen x* liegt, gehoeren beide zu W.
- **Qualifiziert:** F0, F1, F2 und F3 = ja.
- **Verschieden:** |d beta| >= 0,05 oder |d gamma| >= 0,02 (L: nur ein Modell).
- **Berichtet ohne Punkte:** omega*^2, Nullstelle der Geraden, R^2, g0 und g0/Gamma_ref, rho und Q am Tiefpunkt,
  Abstand von x* zu den Grenzen von W, alle groben Minima, Startpole und Umlaufzahl am Startpunkt.
- **A1 (Generation 0):**
  - Anker: ein verfeinertes Minimum mit F2 = ja hat omega*^2 in [0,797; 0,799], und Gamma(0,798) (Stufe C, sonst B)
    liegt im Faktor 2 um 1,12e-7.
  - Kontrolle dim = 1: F2 = nein. "Nicht entscheidbar" besteht A1 nicht.
  - Der Plan erwartet in Abschnitt 4 ausserdem "Anker besteht F2". Verfehlt der Anker F2 bei bestandener Lage, ist das ein
    Messmittelfehler: Generation 1 startet dann nicht, und die Reparatur wird hier eingetragen.

## 4. Arme und Generationen (fest in evo1.py generation)

- **Generation 0:** Anker P(0,5; 0), dim 3, mit Zusatzpunkt 0,798; Kontrolle P(0,5; 0), dim 1.
- **Generation 1** (gemeinsam, 18 Modelle, davon 17 neu zu rechnen):
  - Raster beta {0,2; 0,35; 0,5; 0,75; 1,0} x gamma {0; 0,1; 0,2}; (0,5; 0) ist der Anker aus Generation 0
    (derselbe Ergebnisordner, keine Neurechnung).
  - L = ln(1 + S): 1 Modell. Der Plan nennt 2 Log-Modelle, die Familie hat aber nur eins (Abschnitt 6).
  - 2 Zufallsmodelle, gleichverteilt in der Box, seed 1001.
- **Generation 2 und 3** (je 18 Modelle, seed 1000 + nr fuer E, seed + 1 fuer Z):
  - E, 8 Modelle:
    - Eltern sind die besten vier aus Generation 1 und frueheren E-Modellen. Rangfolge: qualifiziert, dann mehr
      bestandene F-Stufen, dann kleineres g0/Gamma_ref.
    - Mit mindestens 2 qualifizierten Eltern: 4 Kreuzungen (Gewicht aus {0,25; 0,5; 0,75}) und 4 Mutationen, sonst 8
      Mutationen. Mutation: Gauss sigma_beta = 0,08, sigma_gamma = 0,03, an der Box gekappt, auf 4 Stellen gerundet.
    - Die Leitung darf Eltern mit Grund tauschen: Datei von Hand aendern, Grund ins Feld "grund".
  - R, 8 Modelle:
    - Mittelpunkte der Zellen des Rasters der Stufe nr - 2 (Generation 2: Raster von Generation 1; Generation 3: dessen
      Halbschritt-Raster), an deren berechneten Ecken (F2, F3) nicht ueberall gleich ist.
    - Reihenfolge erst beta, dann gamma; Ecken aus Generation 1 und frueheren R-Modellen.
    - Danach wird mit dem naechstfeineren Halbschritt-Raster in derselben Reihenfolge aufgefuellt, ohne schon gerechnete
      Punkte.
  - Z, 2 Modelle: gleichverteilt in der Box.
- **Zaehlung "neu und verschieden"** (zusammenfassen): qualifiziert und verschieden von allen qualifizierten Modellen der
  Generationen 0 und 1 und von den frueheren qualifizierten Modellen desselben Arms. Die Arme sind dadurch unabhaengig.

## 5. Vorsprungs- und Abbruchregeln (woertlich aus dem Plan, Abschnitt 5)

- **Vorsprungsschwelle:**
  - Die Evolution gilt als besser, wenn ueber Generation 2 und 3 (je Arm 16 Modelle) gilt: N_E >= 1,5 N_R und
    N_E >= N_R + 3. N ist die Zahl neuer, verschiedener, qualifizierter Modelle.
  - Sonst heisst das Ergebnis "kein Vorsprung". Der Operator wird fuer diese Art Frage fallen gelassen (vierter
    Werkzeugtest), und weiter gerechnet wird mit Zensus und fester Regel.
  - Mit 16 gegen 16 Modellen trennt der Vergleich nur grosse Unterschiede. "Kein Vorsprung" heisst also "kein grosser
    Vorsprung". Fuer die Frage, ob sich der Operator lohnt, reicht das.
- **Abbruchkriterien:**
  - **A1 Anker (Generation 0):** beta = 1/2, gamma = 0 muss omega*^2 in [0,797; 0,799] und Gamma(0,798) innerhalb
    Faktor 2 um 1,12e-7 liefern. Dieselbe Rechnung mit dim = 1 muss an F2 scheitern. Sonst ist der Code fehlerhaft,
    und Generation 1 startet nicht.
  - **A2 Trennschaerfe (nach Generation 1):** Qualifizieren weniger als 5 % oder mehr als 90 % der lebensfaehigen
    Modelle, trennt die Kennzahl nicht. Dann endet der Evolutionsarm, und die Rasterkarte aus Generation 1 ist das
    Ergebnis. Das ist die Pflicht "Vertraege muessen scheitern und bestehen koennen".
  - **A3 Messmittel:** Sind in einer Generation mehr als 20 % der Modelle "nicht entscheidbar" (Stufen uneinig,
    Umlaufzahl nicht 1, Profile fehlen), endet der Pilot. Zuerst wird das Messmittel repariert; das ist die Lehre aus
    Runde 5.
  - **A4 Stillstand:** zwei Generationen hintereinander ohne ein neues verschiedenes qualifiziertes Modell in
    irgendeinem Arm
  - **A5 Budget:** Liegen die gemessenen Kosten je Modell ueber dem Doppelten der Schaetzung, wird mit Finn neu
    geplant, nicht still weitergerechnet. Spaetestens nach Generation 3 ist Schluss.
  - **A6 Code:** Braucht evo1.py mehr als 1 h neuen Code, wird der Pilot geparkt (v3, Abschnitt 6).
- **Bestenliste (Plan, Abschnitt 7):** Aufgenommen wird ein qualifiziertes Modell, das dazu die Zeitbereichsprobe besteht:
  zeit0 an beiden Flanken x* +- 0,03, Rate innerhalb 15 % des Pol-Gamma. Es faellt nur mit ausdruecklicher Ruecknahme
  samt Grund wieder heraus.

## 6. Abweichungen vom Plan und Klaerungen

1. **Unterbefehle:** `modell` (ein Modell, fortsetzbar), `generation`, `zusammenfassen`, `rauch` statt `bewerte --teil
   k/n --phase grob|fein` (Auftrag der Leitung). Grob und fein laufen im selben Befehl nacheinander; der Befehl wird
   wiederholt, bis modell.json "fertig" meldet. Grund: Die Leitung verteilt Modelle einzeln auf Spuren, und ein
   Modell ohne grobes Minimum braucht so nur einen Aufruf.
2. **Log-Familie:**
   - bic2.py definiert U = ln(1 + S) ohne Parameter. Ein Faktor M (U = M^2 ln(1 + S/M^2)) laesst sich klassisch
     wegskalieren; die Familie hat also genau ein Modell.
   - Generation 1 enthaelt deshalb 1 statt 2 Log-Modelle. Das Merkmal "10 % in M" und Log-Neuzugaenge im Arm E
     entfallen.
   - F0 in der Form "min U/S >= 0,02" wuerde L ausschliessen, obwohl das Vakuum nicht entartet ist. Deshalb gilt die
     Klaerung in Abschnitt 3.
   - Das Schiessen fuer L ist neu und nur im Rauchtest geprueft. Es ist nicht mit bic2.py abgeglichen (dort laeuft
     parallel ein anderer Agent); Abgleich nach BIC-2 (b).
3. **Profile fehlen:** Der Plan nennt das in F0 "nicht lebensfaehig", in A3 "nicht entscheidbar". Umgesetzt ist: analytisch
   nicht lebensfaehig -> "nicht lebensfaehig"; lebensfaehig, aber Loeser findet < 10 Profile -> "nicht entscheidbar".
4. **F2 genauer gefasst** (Abschnitt 3, e bis h):
   - Das R^2 einer Parabelanpassung an Gamma waere von den zwei aeusseren Punkten beherrscht und fast immer ~1. Deshalb
     misst R^2 die Gerade durch +-sqrt(Gamma), und zwar nur an den vier inneren Punkten (Kalibrierung in Abschnitt 3).
   - Mehrere grobe Minima: Bis zu drei werden verfeinert, statt nur des tiefsten. Grund: Beim Anker ist Gamma(0,6) =
     2,1e-4 kleiner als Gamma(0,7) = 1,5e-3. Unterhalb von 0,7 kann also ein zweites grobes Minimum liegen, und welches
     grob tiefer liegt, haengt von der Rasterlage ab. Mit nur einem Minimum koennte A1 an der Rasterlage scheitern. Kosten:
     etwa 7 min je weiterem Minimum.
   - g0 kommt aus einer Anpassung mit relativen Residuen, sonst bestimmen die aeusseren Punkte g0.
   - e) verlangt, dass der Tiefpunkt auch fein innen liegt. Ohne e) koennte ein monoton fallender Verlauf (1D) die
     Gerade knapp bestehen: synthetische Probe im Rauchtest.
   - c) hat den absoluten Boden 1e-9. Das ist Codex' Aufloesungsgrenze aus Runde 6; darunter ist Gamma unaufgeloest.
     Stufe A liegt dort ~5e-9 neben C (ERGEBNISSE-R6-B.md, Abschnitt 2); verglichen werden aber nur B und C.
5. **F1 als Filter:** Ohne F1 entfaellt die Verfeinerung (spart etwa 7 min je Modell); F2 heisst dann "grob Minimum, nicht
   verfeinert".
6. **Zusatzpunkt 0,798** nur fuer A1; er zaehlt nicht fuer F2, damit der Anker genauso bewertet wird wie jedes Modell.
7. **Umfang:** evo1.py hat 946 Zeilen statt der 150 bis 250 aus dem Plan. Der numerische Kern bleibt die
   unveraenderte Kopie von resonanz3d.py. Neu sind:
   - die Modellteile, etwa 200 Zeilen
   - fortsetzbare Punkte, Bewertung, drei Arme, Zusammenfassung und Rauchtest
   Das ist mehr als der Plan vorsah. Die Zeitgrenze A6 (1 h) ist eingehalten, siehe Fuss.
8. **Bestenliste und zeit0:** Die Zeitbereichsprobe ist nicht in evo1.py. Sie wird erst gebraucht, wenn ein Modell
   qualifiziert. resonanz3d.zeitlauf liest BETA global. Fuer gamma = 0 genuegt es, eine Kopie mit gesetztem BETA zu
   nehmen; fuer gamma > 0 braucht zeitlauf dieselbe kleine Verallgemeinerung wie lin_aufbau. Das kommt nach Generation 1
   und nur bei Bedarf.

## 7. Befehle fuer die .69

**Uebertragen (Leitung):** evo1.py, resonanz3d.py, PLAN.md nach /home/fmh/fmhc-physics-remote/runde7-evo1/. Danach
sha256 beider Seiten vergleichen: resonanz3d.py 99c54b9ccdb5..., evo1.py Version 2 d81870bfea7a... (Version 1 war
cd01b69bf3d8...; Abschnitt 11). Seit 2026-09-30 06:07:13 CEST gilt Version 3: f882fa19e6080dfcff3a9084e3bc7482188ae444e9097259b883095aa5736583,
lokal und auf der .69 gleich; Version 2 liegt als evo1_v2.py daneben (Abschnitte 12 und 13).

**Generation 0** (2 Modelle; Genomdatei zuerst, Sekundenarbeit, Spur cpu):

```
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu evo1-gen0 evo1.py generation --nr 0 --out gen-000.json
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu evo1-anker evo1.py modell --familie P --beta 0.5000 --gamma 0.0000 --dim 3 --out ergebnisse/P_b0.5000_g0.0000_d3 --zusatz 0.798
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 evo1-kontr1d evo1.py modell --familie P --beta 0.5000 --gamma 0.0000 --dim 1 --out ergebnisse/P_b0.5000_g0.0000_d1
```

- Jeden modell-Befehl wiederholen, bis die letzte Ausgabe `"status": "fertig"` zeigt. Der Anker braucht voraussichtlich
  3 Aufrufe: grob, fein und den Zusatzpunkt.
- Danach: `... kleintest.sh cpu evo1-z0 evo1.py zusammenfassen --gen 0`. Das schreibt bew-000.jsonl und gibt die Tabelle
  und die A1-Zeile aus.
- **Gen 1 startet nur bei "A1: ... bestanden".**

**Generation 1** (nach A1):

```
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu evo1-gen1 evo1.py generation --nr 1 --out gen-001.json
```

Die Datei enthaelt je Modell das Feld "befehl". Die 17 neu zu rechnenden Modelle (der Anker (0,5; 0) ist schon da) mit
Spurvorschlag:

```
# Spur cpu
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu evo1-g1-01 evo1.py modell --familie P --beta 0.2000 --gamma 0.0000 --dim 3 --out ergebnisse/P_b0.2000_g0.0000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu evo1-g1-02 evo1.py modell --familie P --beta 0.2000 --gamma 0.1000 --dim 3 --out ergebnisse/P_b0.2000_g0.1000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu evo1-g1-03 evo1.py modell --familie P --beta 0.2000 --gamma 0.2000 --dim 3 --out ergebnisse/P_b0.2000_g0.2000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu evo1-g1-04 evo1.py modell --familie P --beta 0.3500 --gamma 0.0000 --dim 3 --out ergebnisse/P_b0.3500_g0.0000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu evo1-g1-05 evo1.py modell --familie P --beta 0.3500 --gamma 0.1000 --dim 3 --out ergebnisse/P_b0.3500_g0.1000_d3
# Spur cpu2
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 evo1-g1-06 evo1.py modell --familie P --beta 0.3500 --gamma 0.2000 --dim 3 --out ergebnisse/P_b0.3500_g0.2000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 evo1-g1-07 evo1.py modell --familie P --beta 0.5000 --gamma 0.1000 --dim 3 --out ergebnisse/P_b0.5000_g0.1000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 evo1-g1-08 evo1.py modell --familie P --beta 0.5000 --gamma 0.2000 --dim 3 --out ergebnisse/P_b0.5000_g0.2000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 evo1-g1-09 evo1.py modell --familie P --beta 0.7500 --gamma 0.0000 --dim 3 --out ergebnisse/P_b0.7500_g0.0000_d3
# Spur cpu3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu3 evo1-g1-10 evo1.py modell --familie P --beta 0.7500 --gamma 0.1000 --dim 3 --out ergebnisse/P_b0.7500_g0.1000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu3 evo1-g1-11 evo1.py modell --familie P --beta 0.7500 --gamma 0.2000 --dim 3 --out ergebnisse/P_b0.7500_g0.2000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu3 evo1-g1-12 evo1.py modell --familie P --beta 1.0000 --gamma 0.0000 --dim 3 --out ergebnisse/P_b1.0000_g0.0000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu3 evo1-g1-13 evo1.py modell --familie P --beta 1.0000 --gamma 0.1000 --dim 3 --out ergebnisse/P_b1.0000_g0.1000_d3
# Spur cpu4
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu4 evo1-g1-14 evo1.py modell --familie P --beta 1.0000 --gamma 0.2000 --dim 3 --out ergebnisse/P_b1.0000_g0.2000_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu4 evo1-g1-15 evo1.py modell --familie L --dim 3 --out ergebnisse/L_d3
# die zwei Zufallsmodelle (seed 1001; lokal mit generation --nr 1 erzeugt und geprueft, gen-001.json auf der .69 muss sie gleich enthalten)
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu4 evo1-g1-16 evo1.py modell --familie P --beta 0.9865 --gamma 0.0176 --dim 3 --out ergebnisse/P_b0.9865_g0.0176_d3
cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu4 evo1-g1-17 evo1.py modell --familie P --beta 0.9483 --gamma 0.2588 --dim 3 --out ergebnisse/P_b0.9483_g0.2588_d3
```

- (0,2; 0) ist nicht lebensfaehig (min U/S = -0,25) und endet nach Sekunden.
- Danach: `... kleintest.sh cpu evo1-z1 evo1.py zusammenfassen --gen 1`. Das gibt die Tabelle, A2 und A3 aus.
- **Generation 2 und 3:** `generation --nr 2 --vorige ergebnisse --out gen-002.json` (bzw. --nr 3), dann die Befehle aus
  der Datei auf die vier Spuren verteilen, danach `zusammenfassen --gen N`.

## 8. Laufzeit

**Rauchtest lokal** (Laptop, 1 Thread, nice 19, timeout 120; Freigabe der Leitung vom 30.09. 02:42):
- Erster Lauf 04:48:50 bis 04:50:27 (rc 0), zweiter Lauf 04:53:39 bis 04:54:14, parallel dazu der Kleinstufen-Ablauf
  04:54:24 bis 04:56:08 (101,7 s). Ausgaben in rauch/.
- **Pruefungen:**
  - Koeffizienten der allgemeinen Formel gegen das Original bei gamma -> 0: 7e-15.
  - gamma = 0,1: F(f_top) = 3e-16.
  - F2-Auswertung an drei synthetischen Kurven wie Soll: ja / nein / nein (Abschnitt 3).
- **Anker bei omega^2 = 0,7, Stufe A:** rho = 1,7018102865 - 1,468016e-3 i. Das ist gleich dem Runde-6-Wert
  (pol07.log, Stufe A: 1,7018102865) auf allen gedruckten Stellen.
- **Kleinstufen-Ablauf** (h = 0,08 / 0,04 / 0,02, 6 Scanpunkte, kleine Suche):
  - Alle Teile liefen in einem Aufruf durch: grob, fein A/B/C, Kontur, Zusatzpunkt, Bewertung.
  - Die dortige Stufe "C" (h = 0,02, f_rand 1e-6) entspricht der Runde-6-Stufe A. Sie gab Gamma(0,798) = 1,0744e-7
    (Runde 6, Stufe A: 1,074e-7).
  - Das Urteil "nicht entscheidbar" (Umlauf 2, Kontur nicht aufgeloest) kommt von der absichtlich groben Kontur und hat
    keine Bedeutung.
- **Gemessen je echtem Stufe-A-Punkt** (Profil und Newton):
  - Anker 0,7: 7,2 s allein, 10,2 s neben einem zweiten Lauf
  - gamma = 0,1 bei 0,8 aus grobem Keim: 12,5 bzw. 13,7 s
  - Log-Profil bei 0,5: 9,3 bzw. 9,6 s

**Hochrechnung auf die echten Stufen.** Grundlage sind diese Messungen und die Runde-6-Logs: Profil B 13 bis 15 s,
Profil C 27 bis 36 s; ein Determinanten-Durchlauf dauert auf Stufe A etwa 0,7 s, auf B etwa 2 s und auf C etwa 5 s.

| Teil | Dauer |
|---|---|
| grob: Startpunkt mit Suche und Kontur, dazu 11 verfolgte Punkte | 3 bis 4 min (1 Aufruf) |
| fein je Minimum: A 6 x 10 s, B 6 x 25 bis 30 s, C 2 x 60 bis 70 s, Kontur etwa 45 s | 6 bis 7 min |
| Zusatzpunkt 0,798 (nur Anker) | etwa 1,5 min |
| Modell ohne grobes Minimum | 3 bis 4 min, 1 Aufruf |
| Modell mit einem Minimum | 10 bis 11 min, 2 Aufrufe |
| Modell mit zwei Minima | etwa 17 min, 3 Aufrufe |

- Das liegt in der Schaetzung des Plans (5 bis 15 CPU-min je Modell). A5 greift erst ueber 30 min je Modell.
- **Generation 0:**
  - Anker: 12 bis 19 min in 3 bis 4 Aufrufen
  - Kontrolle dim 1: 3 bis 10 min in 1 bis 2 Aufrufen
  - auf zwei Spuren etwa 20 min Wandzeit
- **Generation 1:** 17 neue Modelle, davon eins nicht lebensfaehig (Sekunden). Bei im Mittel 0,7 verfeinerten Minima je
  Modell sind das etwa 16 x 8 min = 130 CPU-min, auf vier Spuren 35 bis 45 min Wandzeit, dazu die Pausen zwischen
  den Wiederholungen.
- **Vorbehalt:**
  - Gemessen ist auf dem Laptop; die .69-CPU kann anders schnell sein. Generation 0 misst die echten Kosten
    (zustand.json, Feld "zeiten"); A5 vergleicht mit ihnen.
  - Die Startschaetzungen des Zeitwaechters sind absichtlich hoch (C 200 s). Deshalb endet der erste Aufruf eines
    Modells meist vor Stufe C mit "offen", und der zweite setzt fort.

## 9. Latten L1 bis L5

- **L1 kann scheitern:** ja.
  - A2 in beide Richtungen.
  - Die Negativkontrolle dim = 1 muss scheitern.
  - Der Rauchtest prueft die F2-Auswertung an drei synthetischen Kurven: eine besteht, zwei scheitern.
- **L2 Gegenprobe:** Anker beta = 1/2 (Runde 6, zwei Haeuser) und Kontrolle dim = 1 in Generation 0. Dazu der Arm R als
  Vergleich fuer E und der Arm Z als Zufallskarte.
- **L3 Numerik:** Stufen A, B und C (Pruefungen b und c), Konturumlaufzahl (d). Der Anker rechnet auf demselben Rechenweg
  wie der Code (Uebereinstimmung auf allen gedruckten Stellen, Abschnitt 13)
  aus Runde 6 (gamma = 0 ruft die Originalfunktionen).
- **L4 schon bekannt:** Der Mechanismus (Vorzeichenwechsel eines Ueberlappintegrals) ist bekannt. Eine Nullstelle der
  Breite bei 3D-Q-Baellen fand die Suche nicht (RUNDE-06/resonanz3d/L4-BIC-LITERATUR.md). Vor jeder Aussage nach aussen
  erneut suchen.
- **L5 Messbezug:** nein, hoechstens mittelbar ueber Affleck-Dine-Q-Baelle (MT-3). "Qualifiziert" sagt nichts ueber die
  Natur und beweist keinen gebundenen Zustand im Kontinuum.

## 10. Offen

- Log-Schiessen mit bic2.py abgleichen, sobald BIC-2 (b) fertig ist.
- zeit0 fuer die Bestenliste (Abschnitt 6, Punkt 8).
- Die Rangfolge im Arm E (qualifiziert, F-Stufen, g0/Gamma_ref) ist eine eigene Festlegung; der Plan sagt nur
  "qualifiziert, dann kleineres g0".

## 11. Version 2 (2026-09-30 05:11:22 CEST, date): nach Absturz der 1D-Kontrolle, vor jeder Bewertung

- **Anlass (Leitung):** Die 1D-Kontrolle aus Generation 0 stuerzte auf der .69 in 4 Aufrufen reproduzierbar ab,
  jeweils 3 s nach dem Fortsetzen. Ort: fein -> x_schaetz, ZeroDivisionError. Der Anker (3D) rechnet weiter.
- **Ursache** (lokal nachgeprueft an der Kopie des .69-Zwischenstands in lauf-69/ergebnisse/P_b0.5000_g0.0000_d1/):
  - Die grobe Breite (Stufe A) faellt in 1D monoton: 1,04e-8 bei 0,8555, dann -9,9e-10 bei 0,8927 und -8,5e-10 bei
    0,93. Negativ heisst Im rho > 0, also unter der Aufloesung.
  - lokale_minima nimmt 0,8927 deshalb als inneres Minimum.
  - Nach max(Gamma, 0) ist gl = 1,0e-4 und gm = gr = 0. Der Nenner gm + gr ist null.
  - Version 1 stuerzt auf derselben Kopie lokal genauso ab (Zeilen 414 und 399), ohne dass ein Punkt gerechnet wird.
- **Aenderung, nur diese** (Diff gegen Version 1):
  - x_schaetz gibt jetzt (x_est, hinweis) zurueck. Bei Nenner null gilt x_est = xs[k] und hinweis = "Nullnenner".
  - Bei Nenner ungleich null stehen dieselben Ausdruecke wie in Version 1, das Ergebnis ist bitgleich. Der laufende
    Anker kann also mit Version 2 weiterlaufen.
  - fein speichert den Hinweis in zustand.json (fein[k].hinweis). bewerte_min und bewerte geben ihn in modell.json aus
    (minima[].hinweis, hinweise), die Kurzausgabe von modell zeigt "hinweise".
  - Neu ist Rauchtest-Teil 0 (x_schaetz an vier Kurven, Version 1 wortgleich zum Vergleich), dazu der Versionsvermerk im
    Kopf.
  - Schwellen und Entscheidungsregeln sind unveraendert.
- **sha256 evo1.py Version 2:** d81870bfea7a8ee744a8393a745e7efd97d03b95db5ae0a07295dd7fb97121b6 (985 Zeilen).
  resonanz3d.py ist unveraendert (99c54b9c...).
- **Kurztest** (lokal, 1 Thread, nice 19, timeout 120; 05:10:52 bis 05:12:29):
  - Version 1 auf der Kopie des .69-Stands (--budget 5): ZeroDivisionError wie auf der .69.
  - Version 2 auf derselben Kopie (--budget 5, kein Punkt gerechnet): kein Absturz. x_est = 0,892727, Vermerk
    "Nullnenner", Status "offen", naechster Schritt Stufe A der Feinpunkte 0,8727 bis 0,9127.
  - Rauchtest Teil 0 (rauch/v2/):
    - Die .69-Werte der 1D-Kontrolle, "alle null" und "links null" bringen Version 1 zum Absturz. Version 2 gibt
      jeweils xs[k] mit "Nullnenner" zurueck.
    - Zwei ausgedachte normale Minima: Version 1 und 2 geben dasselbe x_est (Vergleich mit ==: True).
  - Teile 1 bis 3 geben dieselben Zahlen wie mit Version 1: Koeffizienten, drei synthetische F2-Kurven ja / nein / nein,
    rho(0,7) = 1,7018102865 - 1,468016e-3 i.
- **Befund zur Entscheidungsregel** (die Regel ist nicht geaendert; die Leitung entscheidet):
  1. Stufe A loest in 1D Breiten unter etwa 1e-8 nicht auf.
     - Gegen die Runde-6-Werte (Stufe B, scan1d, logarithmisch inter- bzw. extrapoliert) liegt Stufe A um 6e-10
       (0,8555), 1,3e-9 (0,8927) und 9e-10 (0,93) zu niedrig.
     - In 3D lag Stufe A beim Anker 4,8e-9 unter Stufe C (ERGEBNISSE-R6-B.md, Abschnitt 2).
     - Die Grobregel "inneres lokales Minimum" hat keinen Aufloesungsboden. Deshalb gilt der Rauschknick bei 0,8927 als
       Minimum. Regel c hat den Boden 1e-9, aber nur fuer den Vergleich von B und C.
  2. Was die bestehende Regel mit der 1D-Kontrolle wahrscheinlich macht (Vermutung, nicht gerechnet):
     - Verfeinert wird bei 0,8727 bis 0,9127. Faellt die wahre Breite dort monoton, liegt der tiefste Feinpunkt aussen
       (x_est + 0,02). Dann verfehlt der Punkt Regel e, und F2 = nein; die Kontrolle besteht A1.
     - Das gilt aber nur, wenn Pruefung b (gleiche Reihenfolge auf A und B) haelt. Die inneren Feinpunkte unterscheiden
       sich in der wahren Breite nur um etwa 3e-11 bis 5e-11. Die Abweichung von Stufe A aendert sich zwischen den
       Grobpunkten um 4e-10 bis 7e-10.
     - Kippt die Reihenfolge, heisst die Kontrolle "nicht entscheidbar", und A1 ist nicht bestanden, obwohl sie keine
       V-Form zeigt. Das waere eine Luecke der Regel, kein Codefehler.
  3. Dasselbe kann in Generation 1 bis 3 ueberall passieren, wo die Breite am oberen Scanende unter etwa 1e-8 faellt.
     - Kosten: etwa 7 min je Scheinminimum, bis zu drei je Modell.
     - Moegliche Folge: "nicht entscheidbar" (zaehlt fuer A3).
  4. Sind alle sechs Feinwerte <= 0, gibt Regel f R^2 = 0 (alle Wurzeln 0), also F2 = nein.
     - Mit Gamma_ref <= 0 vergleicht Regel h gegen eine nicht positive Schwelle (g0_rel = inf).
     - Ein falsches "ja" aus reinem Rauschen schliesst keine Regel aus. Es braeuchte aber R^2 >= 0,99 durch vier
       verrauschte Wurzeln und ist deshalb unwahrscheinlich.
  5. Minimum am Rand:
     - Nur innere Punkte der Polspur zaehlen. Eine Nullstelle zwischen den letzten zwei Scanpunkten oder oberhalb von
       0,93 wird nicht gefunden (Scanbereich des Plans).
     - Am Duennwand-Ende (k = 1) kann x_est - 0,02 bis auf 0,02 an omega_min^2 heranruecken. Die Profile werden dort
       sehr gross; Pruefung a kann scheitern ("nicht entscheidbar").
  - **Moegliche Regeln** (nicht umgesetzt; festzulegen vor der ersten Bewertung):
    - (i) Ein grobes Minimum zaehlt nur, wenn beide Nachbarn auf Stufe A eine Breite ueber einem Boden haben, etwa 1e-8
      bis 5e-8 (das 2- bis 10-Fache der gemessenen Stufe-A-Abweichung). Sonst heisst es "unter Aufloesung" und wird
      nicht verfeinert (F2 = nein fuer dieses Minimum).
      - 1D-Kontrolle: rechter Nachbar -8,5e-10, also keine Verfeinerung und F2 = nein.
      - Anker: Die Nachbarn eines Minimums nahe 0,7977 liegen nach Runde 6 bei etwa 3e-4, die Regel greift also nicht.
      - Ein echter Tiefpunkt, der zufaellig auf einen Grobpunkt faellt, bleibt erhalten, weil nur die Nachbarn zaehlen.
    - (ii) Oder: Liegen alle sechs Feinwerte auf Stufe B unter dem Boden, heisst das Minimum "nein (unaufgeloest)" statt
      die Pruefungen a bis d zu durchlaufen.

## 12. Reparatur nach A1 (Leitung, Entwurf ab 2026-09-30 05:40:41 CEST, date; wirkt erst nach frischer Lesung)

- **Anlass:** `zusammenfassen --gen 0` (.69, 03:36:17 UTC):
  - Der Anker hat F2 = ja (omega*^2 = 0,79755, Gamma(0,798) = 1,12e-7).
  - Die Kontrolle dim = 1 ist "nicht entscheidbar", am groben Minimum 0,8927. Gruende: b (Reihenfolge A/B kippt) und
    d (Umlauf -7, nicht aufgeloest). Alle Stufe-B-Feinwerte liegen zwischen -2e-11 und 2,2e-9.
  - A1 ist nicht bestanden, Generation 1 ist nicht gestartet.
  - Abschnitt 11, Punkt 2 hatte genau diesen Fall um 05:11 als Moeglichkeit beschrieben ("Luecke der Regel, kein
    Codefehler"). Das war vor dem Ende der Kontrolle (05:28:43).
- **Regelgrundlage:** Abschnitt 3 (Zeile 62) erlaubt eine Reparatur nach A1 und vor Generation 1, mit Grund und date.
- **Entscheidung (Entwurf): Option (i) aus Abschnitt 11, mit Boden G_BODEN = 1e-8.**
  - Ein grobes inneres Minimum der Polspur zaehlt nur, wenn beide Nachbarn auf der Spur auf Stufe A Gamma > 1e-8 haben.
    Sonst heisst es "unter Aufloesung" und wird nicht verfeinert.
  - Bleibt kein Minimum, ist F2 = nein mit dem Grund "kein aufgeloestes Minimum (Nachbarn unter 1e-8)", Urteil "nicht
    qualifiziert".
  - Warum 1e-8: das untere Ende des in Abschnitt 11 vorab genannten Bereichs 1e-8 bis 5e-8, also das 2- bis 10-Fache der
    gemessenen Stufe-A-Abweichung 4,8e-9.
    - Die Wahl innerhalb dieses Bereichs aendert den Ausgang von Anker und Kontrolle nicht: Der rechte Nachbar der
      Kontrolle liegt bei -8,5e-10, die Nachbarn des Ankers bei etwa 3e-4.
    - Das untere Ende schliesst am wenigsten aus.
  - Option (ii) kommt nicht zusaetzlich dazu. Es bleibt bei einer Aenderung.
- **Nebenwirkungen, einzeln:**
  1. **Echte flache Minima werden nicht mehr verfeinert.**
     - Das betrifft echte Minima, deren Nachbarn auf Stufe A unter 1e-8 liegen.
     - Beim groben Raster (12 Punkte, fuer beta = 0,5 Abstand 0,037) sind das V-Formen mit C < 1e-8 / 0,037^2 = 7e-6.
       Die bekannten Nullstellen haben C = 1,08 bis 36.
     - Solche Minima waeren auch mit der alten Regel meist an b, c oder d gescheitert ("nicht entscheidbar").
  2. **A3 wird leichter bestanden.**
     - Modelle, deren einziges Minimum so wegfaellt, heissen jetzt "nicht qualifiziert" statt "nicht entscheidbar".
     - Damit sinkt die Quote fuer A3 (Abbruch bei mehr als 20 % "nicht entscheidbar"). A3 wird also in diesen Faellen
       gelockert.
     - Das ist beabsichtigt: Ein Rauschminimum unter der Aufloesung zeigt keinen Messmittelfehler an, sondern das Fehlen
       eines aufgeloesten Minimums.
     - Ein Messmittelfehler an einem aufgeloesten Minimum zaehlt weiter fuer A3.
  3. **Zaehlung "neu und verschieden" (F2 = ja): nicht betroffen.** F2 = ja braucht weiter alle Pruefungen a bis h.
     **Berichtigt in 13.1: betroffen ueber die Verfeinerungsplaetze (N7).**
  4. **Anker: unveraendert,** denn seine Nachbarn liegen etwa 5 Groessenordnungen ueber dem Boden.
  5. **Kosten sinken:** Die Verfeinerung eines Scheinminimums (etwa 7 min) entfaellt.
  6. **Die Rechnungen der Kontrolle bleiben erhalten.** Ihre Feinwerte bleiben in zustand.json und werden nur nicht mehr
     bewertet.
- **Umsetzung (nach der Lesung):**
  - evo1.py Version 3 aendert nur grob_minima (Filter) und den Grund-Text in bewerte. Neu ist die Konstante
    G_BODEN = 1e-8.
  - Rauchtest:
    - Kopie der Kontrolle: F2 = nein
    - Kopie des Ankers: Bewertung bitgleich zu Version 2
    - synthetische Spur mit V-Form, Nachbarn ueber dem Boden: Das Minimum bleibt erhalten
  - Danach auf der .69 `zusammenfassen --gen 0` erneut.
  - Generation 1 startet nur bei "A1: ... bestanden" mit Version 3.
- **Frische Lesung:** vor der Wirkung durch einen frischen Agenten (Modell Fable), mit Auftrag und Befund in
  RUNDE-07/evo1/LESUNG-REPARATUR-A1.md.

## 13. Wirkung, Buchung der Auflagen und Freigabe (Leitung, 2026-09-30 06:26:16 CEST, date)

- **Lesung:** LESUNG-REPARATUR-A1.md, frischer Leser (Modell Fable), mit zwei Freigaben:
  - 05:41:39 bis 05:51:42: FREIGEBEN MIT AUFLAGEN A1 bis A8
  - Nachtrag 1, 06:15:48 bis 06:21:07: FREIGEBEN zu A3, mit neu gefasster Pruefung
- **Umsetzung:** UMSETZUNG-V3.md (Anthropic-Code-Agent).
  - Version 3 von evo1.py: f882fa19e6080dfcff3a9084e3bc7482188ae444e9097259b883095aa5736583, lokal und auf der .69
    gleich.
  - Auf der .69 per mv eingesetzt um 06:07:13. Version 2 liegt als evo1_v2.py daneben.
- **Wirkung:** Die Reparatur wirkt seit dem Einsetzen von Version 3 (06:07:13).
  - Die Neubewertung von Generation 0 lief ueber `modell` (06:07:43 bis 06:07:54, je unter 30 s).
  - `zusammenfassen --gen 0` endete 06:08:52 (LAUF-Z0-v3.log). Woertlich: "A1: Anker omega*^2 (F2 ja) =
    [0.7975542496031367], Gamma(0,798) = 1.1224047097032925e-07, F2 Anker ja; Kontrolle dim 1 F2 = nein -> bestanden".
- **Das Reparaturkontingent (Zeile 62) ist damit verbraucht.** Bis zum Ende von EVO-1 gibt es keine weitere
  Regelaenderung.

### 13.1 Berichtigung und Ergaenzung von Abschnitt 12 (Auflage A5)

- **Nr. 1:** Statt "Die bekannten Nullstellen haben C = 1,08 bis 36" gilt: Die .69-Fits des Ankers geben C = 0,93
  (k = 8) und 15,3 (k = 3).
- **Nr. 3 ist falsch.** Die Zaehlung "neu und verschieden" ist betroffen, und zwar ueber die Verfeinerungsplaetze (N7):
  - Scheinminima standen in der Sortierung nach Gamma immer vorn und verdraengten echte Minima von den hoechstens drei
    Plaetzen.
  - Mit dem Filter ruecken echte Minima nach. Ein Modell mit vier oder mehr groben Minima kann so F2 = ja bekommen, wo
    die alte Regel "nein" oder "nicht entscheidbar" gab. Das ist eine Lockerung in Richtung mehr F2 = ja.
- **Nr. 4, Nachbarn des Ankers:** 3,61e-4 und 1,05e-3 bei k = 8, 4,57e-3 und 2,48e-3 bei k = 3.
- **Nr. 5, Kosten:** gemessen 12,9 min allein fuer die Verfeinerung des Scheinminimums der Kontrolle (455 s + 317 s),
  nicht "etwa 7 min".
- **Anlass, ergaenzt (N10):**
  - Der Anker hat ein zweites Minimum bei k = 3 (0,63182, x* 0,6304). Dort sind e bis h bestanden, aber der Umlauf ist 2,
    also "nicht entscheidbar" auf Minimumsebene. Das Modell ist nur ueber k = 8 "ja".
  - A3 bleibt fuer diese Signatur scharf; die Reparatur aendert daran nichts.
- **Weitere Nebenwirkungen:**
  - **N8, Arm R:** Es gibt weniger Scheinumschlaege "nicht entscheidbar" gegen "nein", und die Kandidatenliste von R
    aendert sich. Die Arme E (gleiches fitness-Tupel) und Z bleiben unberuehrt. Diese R-Wirkung ist gewollt und wird vor
    Generation 2 als gewollt vermerkt (A8).
  - **N9, A2 unberuehrt:** Zaehler und Nenner bleiben gleich, ausser ueber N7.
  - **N13, Bericht:** Weggefallene Minima stehen in modell.json unter grob_minima_unter_aufloesung (A1 der Lesung,
    umgesetzt).
  - **N16, Etikettwechsel bei F1 = nein:** Ein Modell mit F1 = nein und nur einem Scheinminimum heisst kuenftig "nein"
    statt "grob Minimum, nicht verfeinert". Das betrifft die R-Etiketten (N8).
  - **N15:** Der Version-2-Zweig "Nullnenner" wird unerreichbar. Das ist harmlos.

### 13.2 A3 und Gleichheitspruefungen (woertlich aus dem Nachtrag der Lesung)

- **A3, neu gefasst:** "A3 gilt als erfuellt, wenn beides gilt:
  - (a) Nach Entfernen der sechs lstsq-Felder (minima[].c, minima[].x_stern, minima[].g0, minima[].g0_rel, x_stern,
    g0_rel) sind die `jq -S`-Ausgaben der Version-2- und der Version-3-Datei byteweise gleich (gleiche Pruefsumme).
  - (b) Jedes dieser Felder weicht relativ um hoechstens 1e-10 ab, gemessen als |a - b| / max(|a|, |b|), bei a = b
    null."
- **Ergebnis am 30.09.:** (a) gleich (57534516...), (b) hoechstens 1,94e-13.
  - Wiederholungen: Version 3 traf die Version-2-Datei in 6 von 7 Laeufen, Version 2 sich selbst in 4 von 5.
  - Ursache: torch.linalg.lstsq ist auf der .69 nicht bitweise reproduzierbar. Die Eingaben waren in allen 13 Laeufen
    bitgleich.
- **Gleichheitspruefungen:** "Gleichheitspruefungen in EVO-1 heissen ab jetzt: Entscheidungsfelder und alle Felder ohne
  lstsq byteweise, lstsq-Felder relativ hoechstens 1e-10."
  - Deshalb heisst es in Abschnitt 2 und in L3 jetzt "gleicher Rechenweg; Uebereinstimmung auf allen gedruckten Stellen"
    statt "bitgleich".
- **Rauschgrenze:** "Liegt in einer Generation eine Entscheidungsgroesse naeher als 1e-9 relativ an ihrer Schwelle (h)
  oder liegen zwei g0_rel von Elternkandidaten im Arm E naeher als 1e-9 beieinander, wird das Modell in RUNDE-07.md als
  'an der Rauschgrenze' vermerkt. Entschieden wird weiter nach der bestehenden Regel."
- **Minimum ueber MAX_MIN (N5):** Je Generation laeuft vor der Auswertung der jq-Befehl aus LESUNG-REPARATUR-A1.md, N5,
  ueber bew-00N.jsonl.
  - Jedes Modell mit luecke = true erhaelt in der Rundendatei den Vermerk "Minimum ueber MAX_MIN, nicht verfeinert".
  - Generation 0: keine Luecke.

### 13.3 Generation 1 (Auflage A8)

- Generation 1 wird vollstaendig mit Version 3 gerechnet, mit den Befehlen aus Abschnitt 7, ohne weitere Regelaenderung.
- PLAN.md wird vor dem Start auf die .69 gespiegelt (sha256 beidseitig).

## Einfach gesagt

Wir haben ein kleines Programm geschrieben, das viele leicht veraenderte Q-Ball-Modelle nacheinander prueft. Die Frage
ist jedes Mal: Hat die innere Atmungsschwingung eine Stelle, an der sie fast keine Energie nach aussen abgibt, und ist
der Ball dort stabil? Bevor ein echtes Modell gerechnet wurde, haben wir festgelegt, was als "fast verlustfrei" zaehlt.
An kuenstlichen Testkurven haben wir geprueft, dass diese Regel bestehen und durchfallen kann. Dabei zeigte sich, dass
die erste Fassung sogar das bekannte Vorbild durchfallen liesse. Sie wurde vor dem ersten echten Modell repariert, und
das steht hier. Der kurze Probelauf auf dem Laptop lief fehlerfrei und traf den bekannten Wert aus Runde 6 auf zehn
Stellen. Als Naechstes rechnet die Leitung auf der .69 das Vorbild und die Gegenprobe in 1D. Erst wenn beide wie
erwartet ausgehen, beginnt die erste Modellgeneration.

---
Ende (date): 2026-09-30 04:59:20 CEST. Nachtrag Version 2 (Abschnitt 11): 05:09:07 bis 05:14:06 CEST (date).
