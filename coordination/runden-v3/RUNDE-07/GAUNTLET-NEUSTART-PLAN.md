# Gauntlet-Loop fuer Modellrechnungen mit evolutionaerem Verfahren: schlanker Neustart (Plan)

- **Auftrag:** claude-primary (Leitung), nach Finn im Chat: "... check wie wir unseren gauntlet loop für modell
  rechnungen und so wieder anwerfen können mit dem evolutionären verfahren". Teil B; Teil A steht in
  IDEATION-UEBERSICHT.md daneben.
- **Bearbeiter:** Anthropic-Subagent (Opus 5.5). Nur gelesen und geplant: nichts gestartet, nichts gerechnet, kein
  bestehender Code geaendert, kein ssh, kein git, kein Peerbus.
- **Beginn (date):** 2026-09-30 04:04:02 CEST. Schreibbeginn dieser Datei 04:20:51 CEST.
- **Ende (date):** 2026-09-30 04:26:29 CEST (gemessen nach dem Schreiben)
- **Status:** Vorschlag. Die Leitung entscheidet; der Pilot ist ein neuer Strang und braucht Finns Ja. Eigene
  Einschaetzungen sind als solche markiert; Laufzeiten sind aus gemessenen Laeufen dieser Nacht hochgerechnet.
- **Gelesen:** gauntlet/README.md, EINGEFROREN-20260930.md, BAR.md, Kopfkommentare und Einstiegspunkte von loop.py,
  runde.py, leiter_neu.py, slot69.py, pruefung69.py; gauntlet/new-runs/entwicklung-v2-20260911/ABGESCHLOSSEN-20260930.md;
  coordination/evolution-review-20260929/REVIEW.md und V3-ENTWURF.md; coordination/runden-v3/README.md,
  ARCHIV-20260930.md, kleintest.sh; coordination/evolution/KONZEPT.md; coordination/platz.py (Kopf);
  RUNDE-06/resonanz3d/resonanz3d.py (Kopf, Funktionsliste, Argumente) und die Laufprotokolle in RUNDE-06; die
  Projektregeln in CLAUDE.md.

## Kurzantwort (5 Punkte)

1. **Code:** Der alte Gauntlet bleibt eingefroren. runde.py, loop.py, leiter_neu.py und slot69.py sind ein Jury- und
   Register-Controller fuer Behauptungen; sie rechnen keine Modelle. Unveraendert wiederverwendet werden kleintest.sh
   (Controller mit eigenem Lock je Spur), die gelaufenen Rundenskripte als Fitness-Bausteine und Anker, vor allem
   resonanz3d.py, sowie das Protokollmuster aus coordination/evolution/ (alle Kandidaten je Generation in einer Datei).
   Minimal neu ist ein Rechenskript evo1.py (etwa 200 Zeilen) plus je Generation eine Genomdatei und die Rundendatei.
2. **Eine Generation:** 18 Modelle, davon 8 aus der Evolution, 8 aus einem Raster mit fester Verfeinerungsregel und 2
   Zufallsmodelle. Ein Modell braucht etwa zwei kleintest-Aufrufe (Grobscan, Verfeinerung) zu hoechstens 10 min auf
   den CPU-Spuren cpu bis cpu4 der .69, zusammen etwa 36 Aufrufe. Das dauert etwa 60 bis 90 min Wandzeit. Danach schreibt die Leitung eine Zeile
   Abschaetzung je Modell. Es gibt keinen neuen Lock, keinen Dienst und keine Jury.
3. **Fitness:** Nur ein vorhandener Baustein kann ehrlich scheitern und folgt nicht vorab aus dem Papier: die
   Nullstelle der Breite der l = 0-Atmung im stabilen Fenster. 1D hat keine, 3D bei beta = 1/2 hat eine.
   - Existenz, VK-Stabilitaet, E/Q, Rayleigh-Tropfen, Weber-Schwelle und Regge-Steigung sind vorab ableitbar. Sie
     dienen als Filter oder Kontrolle und geben keine Punkte.
   - Landau-Schwelle und Q-Atom-Niveaus koennen scheitern, gehoeren aber zur Zwei-Feld-Familie (spaeter EVO-2).
4. **Vorab gebunden:**
   - **Vergleich:** Der Vergleichsarm "Raster mit fester Regel" bekommt dieselbe Modellzahl. Die Evolution gilt nur
     als besser, wenn sie in Generation 2 und 3 zusammen mindestens 1,5-mal so viele und mindestens 3 mehr
     verschiedene qualifizierte Modelle findet.
   - **Abbruch:** wenn der Anker aus Runde 6 nicht reproduziert wird; wenn in Generation 1 weniger als 5 % oder mehr
     als 90 % der lebensfaehigen Modelle qualifizieren (dann trennt die Kennzahl nicht); wenn mehr als 20 % der
     Modelle "nicht entscheidbar" sind; nach zwei Generationen ohne neues Modell; spaetestens nach Generation 3.
   - **Erwartung** (eigene Einschaetzung): Bei zwei Parametern je Familie bringt Evolution keinen Vorsprung.
5. **Pilot EVO-1, Budget und Risiken:**
   - **Inhalt:** Potentialfamilie U = S - S^2 + beta S^3 + gamma S^4 plus Log-Potential aus BIC-2 (b). Gesucht sind
     Modelle mit fast verlustfreier Atmung im stabilen Fenster, gegen ein Raster.
   - **Budget:** etwa 57 Modelle, 8 bis 15 Spur-Stunden CPU auf der .69, GPU praktisch null (hoechstens 1 GPU-h
     P4000 fuer Zeitbereichsproben), 5 bis 7 h Wandzeit.
   - **Risiken:** Selbsterfuellung, Doppelarbeit mit BIC-2 (b), Ueberbau.
   - **Start:** erst nach dem Ergebnis von BIC-2 (b) und mit Finns Ja.

## 1. Ausgangslage

- **Was der Gauntlet war:** ein Register von Behauptungen mit Jury aus mehreren Haeusern, Kalibrierpaaren (M7, K1),
  Stufen und Ratsche. v2 lief vom 11. bis 20.09. ueber 22 Runden und brachte 5 Gold-Zeilen, nach dem Review ohne neuen
  Effekt (REVIEW.md, 1.5). Seit 30.09. ist er eingefroren (gauntlet/EINGEFROREN-20260930.md).
- **Evolution gegen Latten gab es schon** (12.09., coordination/evolution/KONZEPT.md): Genome mit drei stetigen
  Parametern und diskreten Genen, Latten B1 bis B8, drei Generationen zu 14. Die Bestform fand erst der Vollzensus der
  121 Formen, nicht die Evolution (REVIEW.md, 1.1). Die zwei tragenden Aussagen standen vorher auf Papier.
- **Lehre aus drei Werkzeugtests** (Memory "Kluge Suche ohne belegten Vorteil"): kein Vorteil gegenueber Zufall oder
  Sortierregel. Deshalb Vergleichsarm und Vorsprungsschwelle vorab binden.
- **v3 seit 30.09.:** Runden mit Karten, fuenf Latten L1 bis L5, einer Zufallskarte und einer Abschaetzung je Karte.
  In den Runden 1 bis 4 ergaben die gewaehlten Karten 4 von 27 "weiter", die Zufallskarten 1 von 5
  (IDEATION-UEBERSICHT.md, Kurz, Punkt 4). Auch unsere Abschaetzung hat also bisher keinen belegten Vorsprung.
- **Finns Wunsch** "gauntlet loop ... mit dem evolutionaeren verfahren" laesst sich ohne neue Maschine erfuellen. Der
  Loop ist: bauen, gegen feste Latten messen, Bestes festhalten (Ratsche), vorab festes Ende. Das Verfahren ist:
  Population aus Modellvarianten, Variation, Auswahl mit Abschaetzung der Leitung statt reiner Selektion. Beides passt
  in eine v3-Runde mit Modellkarten.

| Gauntlet-Baustein (Skill und alter Lauf) | im Neustart |
|---|---|
| Builder | evo1.py bewertet Modelle, ein kleintest-Aufruf je Teilmenge |
| Latte | F0 bis F3 (Abschnitt 4) plus L1 bis L5 aus v3 |
| Jury | entfaellt; ein anderes Haus liest nur bei formalen Tests (v3, Abschnitt 5) |
| Ratsche | Bestenliste: ein Modell faellt nur mit ausdruecklicher Ruecknahme wieder heraus (Regel aus gauntlet/BAR.md) |
| Abbruch, der nicht "der Mensch" heisst | A1 bis A6 in Abschnitt 5 |
| Referenzlatte | Anker beta = 1/2 aus Runde 6, zwei Haeuser |

Der Skill "gauntlet" ist fuer sichtbare Latten gebaut (Grafik, Prosa, A/B mit Richtern) und passt fuer
Modellrechnungen nicht direkt.

## 2. Frage 1: Was wiederverwenden, was eingefroren lassen, was minimal neu?

### 2.1 Unveraendert wiederverwenden

| Teil | Pfad | wofuer |
|---|---|---|
| kleintest.sh | coordination/runden-v3/kleintest.sh; auf der .69 /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh | der vorhandene Controller fuer kleine Tests: Spuren p4000a, p4000b, cpu bis cpu4, je Spur ein eigener Lock (lock-klein-SPUR.lock), systemd-run --user mit RuntimeMaxSec=600, MemoryMax=4G, CPUQuota=100 % |
| resonanz3d.py | coordination/runden-v3/RUNDE-06/resonanz3d/resonanz3d.py | Kern des Fitness-Bausteins. profil(w2, dim, beta, h, dev), kennzahlen_3d(prof), lin_aufbau(prof, ...), det(), newton(), kontur() und bruecke(..., beta, ...) fuehren beta schon als Argument bzw. im Profil. Nur pole_omega() und zeitlauf() lesen die Modulkonstante BETA = 0,5, und es gibt kein --beta |
| Anker und Kontrollen | resonanz3d/lauf-lokal/aus-bic-c bis -e, aus-pole-08; coordination/resonance-20260930/3D-OMEGA-SCAN-CODEX.md; RUNDE-02/tests1d/lauf-69/ausgabe/tests1d_bericht.txt | Sollwerte fuer beta = 1/2: omega*^2 ~ 0,7977, Gamma(0,798) = 1,122e-7, Q_min = 111,84 bei 0,927, E/Q > 1 ab ~ 0,85; 1D ohne Minimum (scan1d) |
| weitere Rundenskripte | tests1d.py, r5a.py, tests2d_r3.py, weber.py, medium1d.py, r5d_f5.py, regge2d.py, kf5_geburt.py | als Anker und fuer EVO-2. Das Modell ist dort fest eingebaut (U = S - S^2 + S^3/2, Medium- und Zwei-Feld-Parameter in den Testtabellen); als Suchbausteine brauchen sie eine Parameterkopie |
| Protokollmuster | coordination/evolution/KONZEPT.md, Abschnitte 2, 5, 7 | alle Kandidaten je Generation in einer Datei, auch Verlierer und Abstuerze; Seed im Dateinamen; Abbruch nach drei Generationen oder zwei ohne Neues; keine Latte nach Sichtung aendern. evolution_potential.py selbst bewertet Molekuelpotentiale und passt nicht auf Q-Baelle |
| Ratschen-Regel | gauntlet/BAR.md, letzter Absatz | eine Zeile Regel fuer die Bestenliste |
| geprueftes Register | gauntlet/new-runs/entwicklung-v2-20260911/behauptungen.jsonl | vor dem Start einmal per grep gegen die Stichworte der Pilotfrage, gegen Doppelarbeit |
| platz.py | coordination/platz.py | bleibt, wie es ist; fuer kleine Tests nicht noetig |

### 2.2 Eingefroren lassen

- gauntlet/runde.py, leiter_neu.py, loop.py, slot69.py, brief_split_slot.py, test_candidate_gate.py, test_ratchet.py
  samt Sicherungen (EINGEFROREN-20260930.md). Sie verwalten Briefe, Ernten, Kalibrierpaare und Urteile aus der
  Koordinationsdatenbank. Keiner davon rechnet ein Modell. slot69.py ist fest auf einen alten Lauf, eine GPU und
  model-lab/remote/controller.json verdrahtet.
- der Lauf gauntlet/new-runs/entwicklung-v2-20260911/ (abgeschlossen) und die historische Jury-Handlungsanweisung
- kevloop-Sprachentscheider, rapid.py, Dashboards und DuckDB aus model-lab/ideation (ARCHIV-20260930.md)
- VORAB-Dateien, OTS-Stempel und Hashketten fuer Ideen (v3)

### 2.3 Minimal neu

Alles liegt in einem Rundenordner, etwa coordination/runden-v3/RUNDE-NN/evo1/, wie jede Rundenkarte.

- **evo1.py**, etwa 150 bis 250 Zeilen, PyTorch float64, --geraet cpu|cuda:
  - Genom -> U(S), U'(S), U''(S) fuer die Familie P (beta, gamma); fuer die Log-Familie L der Code aus BIC-2 (b)
  - Profil und l = 0-Pol je omega^2 mit den Funktionen aus resonanz3d.py. Fuer gamma != 0 ist eine verallgemeinerte
    Kopie noetig von koeffizienten(), der Koeffizienten dp und sp in lin_aufbau() und der U-Integrale in
    kennzahlen_3d(). resonanz3d.py selbst bleibt unveraendert.
  - Bewertung F0 bis F3 (Abschnitt 4); eine JSON-Zeile je Modell, auch fuer Abstuerze und "nicht entscheidbar"
  - Unterbefehle: bewerte (Genomdatei, Teilmenge per --teil k/n, --phase grob|fein), raster (feste Regel), mutiere
    (Evolutionsarm, fester Seed), zufall (Seed)
  - Es ist ein gewoehnliches Rechenskript wie r5a.py: kein Wrapper um vorhandene Befehle, kein Dienst, kein Timer, kein
    Hook. Es wird je Aufruf einmal ueber kleintest.sh gestartet.
- **gen-00N.json** (Genome mit Arm, Eltern, Seed, einer Zeile Grund) und **bew-00N.jsonl** (alle Bewertungen)
- **RUNDE-NN.md** wie jede v3-Runde, ein Journaleintrag je Generation ueber research_journal.py (Leitung)
- **Neuer Code hoechstens 1 h** (v3, Abschnitt 6), sonst wird der Pilot geparkt.

## 3. Frage 2: Wie laeuft eine Generation konkret?

1. **Genome schreiben (Leitung, etwa 10 min):**
   - Generation 1 ist fuer alle Arme gemeinsam (Abschnitt 7).
   - Ab Generation 2 erzeugen evo1.py mutiere (Arm E, 8 Modelle), evo1.py raster (Arm R, 8) und evo1.py zufall
     (Arm Z, 2) die Genome in gen-00N.json.
   - Die Leitung darf Eltern im Arm E tauschen, mit einer Zeile Grund im Feld "grund". Das ist die Abschaetzung statt
     reiner Selektion.
   - Diese Schritte sind Sekundenarbeit, aber Python. Sie laufen deshalb als kurzer kleintest-Aufruf auf der Spur cpu
     der .69, nicht auf dem Laptop.
2. **Uebertragen:** Code und Genome in einen Arbeitsordner auf der .69, etwa /home/fmh/fmhc-physics-remote/runde-NN-evo1/.
   Danach die Hashes beider Seiten vergleichen; das ist die Lehre, die slot69.py im Kopf beschreibt.
3. **Rechnen:**
   - Jede Spur bekommt ein Viertel der Genome und rechnet es in aufeinanderfolgenden Aufrufen ab, erst --phase grob,
     dann --phase fein (etwa neun Aufrufe je Spur); vier Spuren laufen parallel. Zum Beispiel:
     `cd /home/fmh/fmhc-physics-remote/runde-NN-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu evo1-g2-a evo1.py bewerte --gen gen-002.json --teil 1/4 --phase grob --geraet cpu --budget 540`
   - Dasselbe mit cpu2, cpu3, cpu4 und --teil 2/4 bis 4/4.
   - evo1.py beginnt ein Modell nur, wenn die gemessene Restzeit reicht. Nicht begonnene Modelle heissen
     "nicht bewertet" (kein Scheitern) und gehen in den naechsten Aufruf. Ein laufendes Modell wird nie abgebrochen.
     Die harte Grenze setzt kleintest.sh (RuntimeMaxSec=600); das Budget 540 s laesst Abstand. So gibt es keinen
     Selbstabbruch mitten in einer Rechnung (Memory "Budget vorab messen, kein Selbstabbruch").
4. **Spuren und Lock:**
   - cpu bis cpu4 (Finn 30.09.: kleine Tests "auf anderen karten oder auf cpu"; runden-v3/README.md). Die Polsuche ist
     eine Folge kleiner linearer ODEs in float64. Runde 6 rechnete die Pole auf der Laptop-CPU und die Zeitlaeufe auf
     der .69-Spur cpu3; auf der .69 gehoeren beide auf die CPU-Spuren.
   - Jede Spur hat ihren Lock in kleintest.sh; ein neuer Lock entsteht nicht.
   - p4000a nur fuer Zeitbereichsproben, falls CPU zu langsam ist. p4000b nur, wenn WM-1-MB nicht laeuft.
   - Die P5000 (VS-1) und gauntlet-gpu.lock werden nicht beruehrt.
   - Grosse Laeufe, falls je noetig, gehen ueber die vorhandenen Controller unter gauntlet-gpu.lock, nicht ueber
     diesen Plan.
5. **Laufzeit (Hochrechnung, in Generation 0 gemessen):**
   - **Gemessen in Runde 6:**
     - volle Polsuche mit Kontur und drei Stufen: etwa 135 s je omega^2-Wert (bic-c bis bic-e: je zwei Werte in
       270 s, Laptop, 1 Thread)
     - Polverfolgung vom Nachbarwert ohne Kontur: etwa 23 s je Punkt (scan1d: 13 Punkte in gut 5 min)
     - zeit0 bei T = 800 auf der .69: 250 bis 300 s
   - **Je Modell geschaetzt:**
     - Profile (Sekunden)
     - Grobscan mit 12 omega^2-Punkten auf Stufe A: 4 bis 6 min
     - Verfeinerung mit 6 Punkten auf den Stufen A und B, dazu Stufe C an den zwei tiefsten Punkten: 6 bis 9 min
     - Ohne groben Tiefpunkt entfaellt die Verfeinerung.
   - **Also:** 5 bis 15 CPU-min je Modell, zwei Aufrufe.
   - **Generation mit 18 Modellen:** etwa 36 Aufrufe auf 4 Spuren, 60 bis 90 min Wandzeit.
6. **Abholen und abschaetzen (Leitung, 20 bis 30 min):**
   - bew-00N.jsonl zuruecksichern.
   - Tabelle in RUNDE-NN.md: Modell, Arm, F0 bis F3, omega*^2, Gamma_min, g0, Entscheidung (Elter, Bestenliste,
     verwerfen), ein Satz Grund.
   - Dazu die Latten-Bilanz, die Zaehlung je Arm und "Einfach gesagt".

## 4. Frage 3: Fitness-Bausteine, die als gelaufener Code vorliegen

| Baustein | Code (Pfad, Unterbefehl) | gelaufen | Modell im Code | kann scheitern? | vorab ableitbar? | Rolle |
|---|---|---|---|---|---|---|
| Existenz, Fenster (omega_min^2 = min U/S) | resonanz3d.py profil; r5a.py | R2, R5, R6 | beta als Argument | nur am Rand | ja, analytisch | Filter F0 |
| VK-Stabilitaet dQ/domega < 0, Q_min | RUNDE-02/tests1d/tests1d.py Test 4; r5a.py fitness | R2, R5 | fest beta = 1/2; kennzahlen_3d gibt Q und E je Profil | kaum (duenner Ast stabil) | weitgehend | Filter F1 |
| absolute Stabilitaet E/Q < 1 | wie oben | R2, R5 | wie oben | kaum | weitgehend | Filter F1 |
| **Breite der l = 0-Atmung, Nullstelle** | resonanz3d.py pole, bruecke; Zweithaus: resonance-20260930/linear3d-omega (Codex) | R6, zwei Haeuser | beta als Argument, pole_omega mit Modulkonstante | **ja**: 1D keine, 3D bei beta = 1/2 eine | **nein** | **Kern F2, F3** |
| Zeitbereich an den Flanken | resonanz3d.py zeit0 | R6 (.69 cpu3) | BETA global | ja | nein | Kontrolle fuer die Bestenliste; an der Nullstelle selbst unaufgeloest (ERGEBNISSE-R6-B.md, Abschnitt 4) |
| Tropfenbild l = 2 (Rayleigh) | resonanz3d.py pole --l 2; tests2d_r3.py tropfen | R3, R6 | 3D beta als Argument, 2D fest | im Duennwandbereich kaum | ja (Formel ohne freie Parameter) | Code-Kontrolle, keine Punkte |
| Teilchen an Stufen | RUNDE-06/weber/weber.py karte1d, feinv1d | R6 | fest | Zerspritzen ja (scheiterte), Schwelle kaum | v_cl ja | nicht verwenden |
| Regge-Steigung | RUNDE-06/regge/regge2d.py | R6 | fest | kaum | ja | nicht verwenden |
| Landau-Schwelle im Medium | RUNDE-06/medium1d/medium1d.py landau | R6 (.69 P4000) | Medium fest in TESTS | ja (Vorhersage verfehlt) | nein | EVO-2 |
| Q-Atom-Niveaus, Huelle | RUNDE-05/r5d/r5d_f5.py | R6 (.69 CPU) | Zwei-Feld fest, nur --masse | ja (zweites Niveau offen) | lineare Niveaus ja, Dynamik nein | EVO-2 |
| Stokes-Drift ~ a^2 | medium1d.py stokes | R6 (.69) | fest | ja | Exponent 2 erwartet | nicht als Fitness |
| dunkler Zustand zweier Baelle | RUNDE-06/reflexion/reflexion.py | R6 | fest | kaum (linear bekannt) | ja | nicht verwenden |
| Geburt in 2D, Tropfen auf der Familie | RUNDE-06/kf5/kf5_geburt.py | R6 (.69) | fest | ja | nein | nicht verwenden, bis die Messung entscheidet (KF-5: "nicht entscheidbar") |

Nicht verwendbar, weil ihre Kontrollen rissen: lawinen, quorum, bragg, chromatographie, nerv (Teil A, Abschnitt 4).

**Kriterien fuer EVO-1, vorab festgelegt:**

- **F0 lebensfaehig:** Das Vakuum ist stabil und nicht entartet, min ueber S > 0 von U(S)/S >= 0,02. Profile finden
  sich an mindestens 10 der 12 Scanpunkte. Sonst heisst das Modell "nicht lebensfaehig"; es zaehlt trotzdem als
  bewertet.
- **F1 stabiles Fenster W:**
  - W sind die Scanpunkte mit dQ/domega < 0 und E/Q < 1, bestimmt aus den Profilen.
  - W muss mindestens 3 Punkte enthalten.
  - Der Grobscan laeuft ueber 12 Punkte von omega_min^2 + 0,02 bis 0,93.
- **F2 Nullstelle der Breite:**
  - **Grob:** Entlang des l = 0-Pols wird ein lokales Minimum von Gamma gesucht. Der Pol wird mit Kontur an einem
    Startpunkt gefunden und dann vom Nachbarwert verfolgt.
  - **Verfeinerung:** Um den groben Tiefpunkt wird x* aus einem linearen Ansatz fuer +-sqrt(Gamma) geschaetzt, dann
    wird bei x* +- 0,002 und x* +- 0,0005 gerechnet. An die sechs naechsten Punkte wird Gamma = c (x - x*)^2 + g0
    angepasst.
  - **F2 besteht, wenn alles gilt:**
    - sqrt(Gamma) wechselt an x* das Vorzeichen und ist linear: Die Anpassung erklaert mindestens 99 % der Streuung.
    - g0 <= 1e-3 mal Gamma bei x* +- 0,02.
    - Die Stufen A und B haben dieselbe Reihenfolge; B und C weichen am Tiefpunkt um weniger als 5 % ab.
    - Die Konturumlaufzahl am Tiefpunkt ist 1, der Pol ist also nicht auf einen anderen Zweig gesprungen
      (ERGEBNISSE-R6-B.md, Punkt 8).
  - **Anker beta = 1/2 besteht:** sqrt(Gamma) ist auf 1 bis 5 % linear mit Vorzeichenwechsel, Gamma(0,78) = 4,0e-4
    gegen einen Boden unter etwa 1e-8 (RUNDE-06.md, ultrafeiner Scan).
  - **1D scheitert:** Die Breite faellt dort monoton, es gibt kein lokales Minimum (RUNDE-06.md, 1D-Tabelle). Das
    Kriterium kann also bestehen und scheitern.
- **F3 Lage:** omega*^2 liegt in W; die fast verlustfreie Atmung sitzt also in einem VK- und absolut stabilen Ball.
  Beim Anker liegt 0,7977 unter 0,85 und unter 0,927: bestanden.
- **Qualifiziert** heisst F0 bis F3 bestanden.
- **Verschieden** sind zwei qualifizierte Modelle nur, wenn sich beta um mindestens 0,05 oder gamma um mindestens 0,02
  unterscheidet (Log-Familie: 10 % in M). Doppelte zaehlen nicht; das ist die Lehre aus dem Millionenlauf mit
  56-mal so vielen Doppelten.
- **Berichtet, aber ohne Punkte:** omega*^2, Re rho*, g0, Q(omega*) und der Abstand zu den Grenzen von W.
- **Reihenfolge im Arm E:** erst qualifiziert, dann kleineres g0 im Verhaeltnis. Die Leitung darf abweichen, mit Grund.
- "Qualifiziert" beweist keinen gebundenen Zustand im Kontinuum und sagt nichts ueber die Natur (L5 nein).

## 5. Frage 4: Abbruch- und Vorsprungskriterien (vor Generation 1 festgelegt)

- **Arme je Generation (ab Generation 2):**
  - **E (Evolution plus Abschaetzung), 8 Modelle:**
    - Mutation: Gauss-Schritt sigma_beta = 0,08, sigma_gamma = 0,03, an der Box gekappt.
    - Kreuzung: gewichtetes Mittel zweier qualifizierter Eltern derselben Familie, Gewicht aus {0,25; 0,5; 0,75}.
    - Hoechstens 2 von 8 sind Familienwechsel oder Neuzugaenge aus der Log-Familie.
    - Eltern sind die besten vier nach Fitness; die Leitung darf mit Grund tauschen.
  - **R (Raster mit fester Regel), 8 Modelle:**
    - Mittelpunkte aller Rasterzellen, an deren Ecken F2 oder F3 umschlaegt, in fester Reihenfolge (erst beta,
      dann gamma).
    - Fehlen Zellen, wird mit einem gleichmaessigen Halbschritt-Raster in fester Reihenfolge aufgefuellt.
    - Kein Urteil; das ist die Sortierregel als Vergleichsarm.
  - **Z (Zufall), 2 Modelle:** gleichverteilt in der Box, Seed im Dateinamen. Z ist die v3-Zufallskarte. Ihre
    Trefferquote steht neben E und R; liegt Z nicht unter E, wird das notiert.
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
- **Die Schwellen stehen hier und werden vor Generation 1 woertlich in die Rundendatei kopiert.** Danach aendert sie
  niemand; das ist die Ehrlichkeitsregel 1 aus coordination/evolution/KONZEPT.md. Eine VORAB-Datei oder Hashkette
  entsteht nicht.

## 6. Frage 5: Risiken und Budget

| Risiko | woran man es merkt | Gegenmittel |
|---|---|---|
| Ueberengineering | Genetik-Rahmenwerk, Warteschlange, Dashboard, Jury, Datenbank, eigene Regeldatei | nur evo1.py mit hoechstens 250 Zeilen; Ergebnisse als JSON plus Rundendatei; kein Dienst, Timer, Hook, Shim oder Wrapper; A6 |
| Selbsterfuellung | Punkte fuer ableitbare Kriterien, Schwellen nach Sicht, Suche nur dort, wo die Nullstelle schon bekannt ist | nur F2 und F3 zaehlen; Schwellen vor Generation 1 fest; A1 mit Negativkontrolle dim = 1; A2 prueft die Trennschaerfe |
| Messen zwei Zahlen dasselbe? | Pol-Gamma gegen Zeitbereichsrate genau an der Nullstelle | zeit0 nur an den Flanken (x* +- 0,03); an der Nullstelle ist er unaufgeloest und im Vorzeichen uneinheitlich (R6-B) |
| Zweigsprung bei der Polverfolgung | Gamma springt zwischen Nachbarpunkten | Umlaufzahl am Tiefpunkt; bei Sprung "nicht entscheidbar" |
| fehlende Stufen aus Zeitgruenden | Stufe C entfaellt wie in R6 | qualifiziert nur mit A, B und C am Tiefpunkt |
| Doppelarbeit mit BIC-2 (b) in Runde 7 | dieselbe Frage fuer andere beta und Log | EVO-1 startet erst nach BIC-2 (b) und uebernimmt dessen Log-Code und beta-Punkte als Startmodelle. Sagt BIC-2 (b) schon "Nullstelle bei allen" oder "bei keinem", greift voraussichtlich A2; dann schrumpft der Pilot auf eine Rasterkarte |
| Doppelte Modelle | Arm E faellt auf kleine Mutationen um ein bekanntes Modell zurueck | Mindestabstand fuer "verschieden" |
| Spurenkonkurrenz | Runde 7 nutzt dieselben Spuren (BIC-2, R5F, RING) | EVO-1 nach den Tests von Runde 7 oder nur auf zwei Spuren; WM-1-MB hat Vorrang auf p4000b |
| Leitung schaetzt eigene Wahl | Arm E ist nicht blind | Codex schreibt einen Satz zu den Eltern-Tauschen (v3, Abschnitt 4); Arm R und Z bleiben regelgebunden |
| kein Messbezug | L5 nein | Nutzen nach v3 hoechstens mittel; offen sagen. Wert: modellintern (Ist die Nullstelle Zufall?), Anschluss an MT-3 |

**Budget des Piloten (Hochrechnung aus Abschnitt 3, in Generation 0 gemessen):**

- **Modelle:** Generation 0 mit 2 (Anker, 1D-Kontrolle), Generation 1 mit etwa 19, Generationen 2 und 3 mit je 18,
  also etwa 57, davon einige sofort "nicht lebensfaehig".
- **Rechnung:**
  - 5 bis 15 CPU-min je Modell, dazu etwa 20 % Wiederholungen: 6 bis 13 Spur-Stunden
  - Zeitbereichsproben an zwei Flanken je Generation: etwa 0,5 h
  - zusammen **8 bis 15 Spur-Stunden CPU** auf der .69
- **GPU:** praktisch null. Hoechstens **1 GPU-h P4000**, falls die Zeitbereichsproben auf die Karte gehen.
- **Wandzeit:** 60 bis 90 min je Generation auf vier Spuren, dazu 20 bis 30 min Abschaetzung. Mit Generation 0
  zusammen 5 bis 7 h.
- **Laptop:** nur Rauchtest (hoechstens 120 s, 1 Thread, nice 19; Memory vom 30.09.).
- **Einordnung** (eigene Einschaetzung): klein und im Kleintest-Regime. Es ist aber ein neuer Strang, deshalb holt die
  Leitung Finns Ja.

## 7. Frage 6: Pilot EVO-1

- **Frage:** Ist die fast verlustfreie Atmung eines 3D-Q-Balls (Breitennullstelle der l = 0-Mode, bei unserem Modell
  omega*^2 ~ 0,7977) eine Eigenschaft einer ganzen Modellklasse oder ein Zufall des Sextik-Modells? Wo liegt sie im
  stabilen Fenster?
- **H (Hypothese):** In U = S - S^2 + beta S^3 + gamma S^4 gibt es ein zusammenhaengendes Gebiet in (beta, gamma), in
  dem die Nullstelle im stabilen Fenster liegt. Ausserhalb verschwindet sie, wie in 1D.
- **Gegenhypothesen:** Die Nullstelle gibt es nur in einer schmalen Umgebung von beta = 1/2 (Zufall), oder sie gibt es
  ueberall (dann ist sie trivial und A2 greift).
- **Warum diese Familie** (eigener Schluss, nicht nachgerechnet): Bis S^4 ist U = S - a2 S^2 + a3 S^3 + a4 S^4 nach
  Umskalieren von phi die allgemeine Form mit a2 > 0. Mit beta = a3/a2^2 und gamma = a4/a2^3 ist das Genom damit
  vollstaendig und minimal.
- **Latten:**
  - L1: ja, A2 in beide Richtungen
  - L2: Anker beta = 1/2 und Negativkontrolle dim = 1
  - L3: Stufen A, B, C
  - L4: Der Mechanismus (Vorzeichenwechsel eines Ueberlappintegrals) ist bekannt; eine 3D-Q-Ball-Nullstelle fand die
    Suche nicht (RUNDE-06/resonanz3d/L4-BIC-LITERATUR.md). Vor jeder Aussage nach aussen erneut suchen.
  - L5: nein, hoechstens mittelbar ueber Affleck-Dine-Q-Baelle (MT-3)
- **Genom:**
  - **Familie P:** beta in [0,15; 1,2], gamma in [0; 0,3], mit Filter F0. Fuer beta < 1/4 ist P nur mit gamma > 0
    lebensfaehig.
  - **Familie L:** Log-Potential genau wie BIC-2 (b) es definiert, mit dessen Parametern. Fehlt es dort, entfaellt L.
  - omega gehoert nicht ins Genom; es wird in der Bewertung abgetastet.
- **Generation 0 (Vorlauf, hoechstens 1 h Code und 30 min Rechnung):**
  - BIC-2 (b) lesen.
  - Die Lebensfaehigkeitskarte min U/S auf Papier.
  - evo1.py schreiben; lokaler Rauchtest.
  - Auf der .69: Anker und dim = 1 rechnen (A1) und dabei die Kosten je Modell messen.
- **Generation 1 (gemeinsam, etwa 19 Modelle):**
  - Raster beta in {0,2; 0,35; 0,5; 0,75; 1,0} mal gamma in {0; 0,1; 0,2}, also 15 Modelle. (0,2; 0) ist nicht
    lebensfaehig und kostet nur Sekunden; (0,5; 0) ist der Anker aus Generation 0.
  - Dazu 2 Log-Modelle aus BIC-2 (b) und 2 Zufallsmodelle.
  - Danach A2 pruefen.
- **Generationen 2 und 3 (je 18):**
  - E 8, R 8, Z 2 nach Abschnitt 5, danach je Generation die Abschaetzung der Leitung.
  - Nach Generation 3 kommen der Vergleich E gegen R, die Schlussabschaetzung, "Einfach gesagt" und ein
    Journaleintrag.
- **Bestenliste (Ratsche):**
  - Aufgenommen wird ein qualifiziertes Modell, das dazu die Zeitbereichsprobe besteht: zeit0 an beiden Flanken
    x* +- 0,03, Rate innerhalb 15 % des Pol-Gamma. In Runde 6 lagen die Abweichungen bei 1 bis 12 % (0,76, 0,84,
    0,6; ERGEBNISSE-R6-B.md, Abschnitt 2 und 1.1); die Schwelle steht vor dem Lauf fest.
  - Es faellt nur mit ausdruecklicher Ruecknahme samt Grund wieder heraus.
  - Ein bis zwei Spitzenmodelle rechnet Codex blind nach, wie bei 0,7977, falls die Leitung sie nach aussen
    vertreten will.
- **Ablage:**
  - coordination/runden-v3/RUNDE-NN/evo1/ mit evo1.py, gen-00N.json, bew-00N.jsonl und lauf-69/
  - RUNDE-NN.md
- **Danach:**
  - **Vorsprung der Evolution:** EVO-2 mit denselben Regeln. Das Zwei-Feld-Q-Atom hat mit lam, m_chi, a und eps
    einen echten Raum mit vier Genen. Gesucht sind "zwei stabile Schwebeniveaus auf einem stabilen Kern", Finns F-5;
    das Fenster lam -0,6 bis -0,8 ist ungerechnet. Bausteine sind r5d_f5.py und medium1d.py als Parameterkopie.
  - **Kein Vorsprung:** Modellfragen laufen als Zensus mit fester Verfeinerungsregel und Abschaetzung, und die
    Evolution bleibt archiviert.
  - **Qualifiziertes Gebiet gefunden:** Ein formaler Test kommt nur nach v3, Abschnitt 5, in Frage. Mangels
    Messbezug ist das bei EVO-1 nicht absehbar.

## 8. Was ausdruecklich nicht gebaut wird

- keine Jury, keine Briefe und Ernten, keine Kalibrierpaare, kein Register; runde.py bleibt kalt
- kein Sprachmodell als Suchsteuerung
- kein Dienst, Timer, Hook, Shim oder Wrapper, keine Warteschlange, kein Dashboard, keine Datenbank
- keine VORAB-Dateien, OTS-Stempel oder Hashketten
- kein neues Regeldokument; die Schwellen stehen in diesem Plan und in der Rundendatei

## Einfach gesagt

Der alte "Gauntlet" war vor allem eine Pruefmaschine fuer Behauptungen mit Richtern. Die bleibt im Keller, denn sie
rechnet selbst nichts aus. Fuer die Suche nach besseren Modellen reicht ein kleines Rechenprogramm, das viele leicht
veraenderte Modelle nacheinander prueft. Jedes Modell wird auf eine einzige ehrliche Frage getestet: Hat sein Q-Ball
eine innere Schwingung, die fast nicht nach aussen leckt, und ist der Ball dort stabil? Parallel zur "Evolution"
rechnen wir stur ein Raster und ein paar Zufallsmodelle, damit wir sehen, ob das Auswaehlen ueberhaupt etwas bringt.
Das kostet wenige Stunden auf den Prozessoren der .69 und kaum Grafikkarte. Wenn nichts Besseres als das Raster
herauskommt, schreiben wir das auf und rechnen kuenftig einfach Raster.

## Freigabe (Leitung, 2026-09-30 04:28:19 CEST)

Finn hat auf die Rueckfrage der Leitung ("Soll ich den Evolutions-Piloten EVO-1 starten (ca. 57 Modelle, 3 Generationen,
8-15 CPU-Spur-Stunden auf der .69, praktisch keine GPU)?") mit "Ja, sofort starten" geantwortet. Der Pilot laeuft damit
parallel zu BIC-2 (b); Doppelarbeit bei der beta-Familie wird in der Abschaetzung vermerkt, nicht vermieden.
