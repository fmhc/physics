# Runde 16 (v3): Theoriekarte M_E-G3 bei Codex, blinder Nachbau der Log-Stelle

Leitung: claude-primary. Angelegt: 2026-10-02 07:45:25 CEST (date). Explorativ. Runde 15 ist abgeschlossen (Journal nr 552).

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| M_E-G3 | R13 SPIN2-D4-2, Finn 02.10. "gib die Theoriekarte an Codex" | IR-endliche Schranke fuer die Graviton-Dreipunktkorrektur in D = 4? Vorabklassen A bis D | Codex (Auftrag per Peerbus 32b70561, 07:46) |
| LOG-NACHBAU | R13 B-BALL | Findet ein unabhaengig geschriebener Code im Log-Potential blind dieselbe stille Stelle (0,9256 nur nachtraeglich gefunden)? | Code-Agent, frisch, ohne Einsicht in die bball-Ergebnisse |

- Vorhersage M_E-G3 (Leitung): A ~10 %, B ~35 %, C ~45 %, D ~10 %.

## Laufend (eingetragen 2026-10-02 07:46:33 CEST)

- **M_E-G3:** Auftrag an Codex per Peerbus (32b70561, kind task, zugestellt).
- **LOG-NACHBAU:** frischer Code-Agent ab ~07:47, Karte RUNDE-16/log-nachbau/KARTE.md (07:45:25).
  - Die Vorhersage der Leitung ist versiegelt (VORHERSAGE.sha256 d1a8b067...). Der Klartext liegt im Scratchpad der Leitung
    und wird nach dem Lauf hier offengelegt.
  - Lesesperren gegen die bball-Ergebnisse und -Codes stehen in der Karte.

### TETRA-SCHNITTE (Finn: "analysieren einordnen codex geben"; eingetragen 2026-10-02 07:49:04 CEST)

- Buendel aus Finns Downloads in RUNDE-16/tetra-chain/ kopiert und entpackt, mit Pruefsummen. Kein Code, nichts
  ausgefuehrt.
- Einordnung: RUNDE-16/tetra-chain/EINORDNUNG.md.
  - Die Zaehlregel P = T3 + 2 T4 + 2 C stimmt, unter einer Konvexitaetsbedingung.
  - Die Tabellen sind in sich stimmig (von Hand nachgerechnet).
    Strang Dimensionsbildung/Grundbewegung bei Codex.
- An Codex als Auftrag (Peerbus, kind task): unabhaengiger Nachbau, Beweis mit Bedingung, Anschluss an den
  Tetraeder-Strang, offene Fragen an Finn.

### Check ChatGPT-Rahmen (Finn: "check mal ..."; eingetragen 2026-10-02 08:10:56 CEST)

- Der Link war nicht lesbar (nur JavaScript-Huelle, Chrome-Erweiterung nicht verbunden); geprueft ist der eingefuegte
  Text. Check: RUNDE-16/tetra-chain/CHECK-CHATGPT-RAHMEN.md.
- Urteil: ein vernuenftiger, ehrlich gekennzeichneter Spielzeugmodell-Rahmen. Der Kasten "-> Raumzeit" wird nicht
  geliefert, weil Zeit und 3D-Einbettung eingesetzt sind.
- Korrekturen:
  - Die Stabilitaet rotierender Zustaende braucht das mitrotierende Bild bzw. Floquet und Erhaltungsgroessen.
  - Die Kantenenergie mit positiven Koeffizienten kollabiert ohne Ruhelaengen.
  - Die Tickrate haengt an der Wahl der Schnitte.
- Widerspruch: "11+1/19+1" ist im Rahmen ein ebener Ring plus Zentrum, im Buendel eine Tetraederkette.
- Bekannt [L?]: Ring plus Zentrum unter Gravitation ist Maxwells Ringproblem, stabil nur fuer N >= 7 (Moeckel 1994).
- An Codex als Nachtrag zum Tetra-Auftrag (kind status, zur Kenntnis).

### Zwei Seiten des Feldes: Review, v2 und Ausprobieren (Finn: "review das mal", "improve", "probier in einem subagent einfach mal aus die sachen"; eingetragen 2026-10-02 08:16:19 CEST)

- Finns Datei (Downloads, sha256 0edb86c3...) liegt als RUNDE-16/zwei-seiten/v1-original.md vor.
- **v2 der Leitung:** RUNDE-16/zwei-seiten/ZWEI-SEITEN-DES-FELDES-v2.md, Kopie in Finns Downloads als
  zwei_seiten_des_feldes_formeln_arbeitsmodell_v2.md (das Original bleibt unveraendert). Hauptaenderungen:
  - kinetischer Term fuer komplexes Feld, Existenzfenster omega_min^2 = m^2 - lambda^2/(4g), Ladung Q, Bezug zum
    Projektmodell
  - diskrete Gleichung als echte Diskretisierung mit geometrieabhaengiger Kopplung
  - Symbolkonflikt lambda (dreifach) aufgeloest
  - Schnitte unterschieden (Sonde gegen intrinsisch); Ticks als Ereignisse der Kodimension 1, ereignisgenau ueber
    Orientierungsdeterminanten
  - Energie mit Ruhegroessen statt Kollaps; glatte Schnittenergie statt Punktzahlen
  - relative Gleichgewichte und gyroskopische Stabilitaet, Krein, feste Ladung
  - Maxwell-Ring als Positivkontrolle
  - Namenskonflikt 11+1 (Ring gegen Tetraederkette) als zwei Varianten R und T
  - Bruecke: stille Q-Ball-Stelle auf dem Gitter
  - Leitidee ehrlich: Raumzeit ist im Modell vorausgesetzt
- **AUSPROBIEREN:** Code-Agent ab ~08:16, Karte RUNDE-16/zwei-seiten/ausprobieren/KARTE.md (08:15:23), fuenf Versuche:
  - V1 Federtetraeder
  - V2 Maxwell-Ring
  - V3 Federring N = 4 bis 32
  - V4 ereignisgenaue Ticks
  - V5 diskreter Q-Ball auf dem Ring-Graphen
  Die Vorhersagen stehen in der Karte.
- Aktive Agenten: LOG-NACHBAU, AUSPROBIEREN (zwei). Codex: M_E-G3, TETRA.

### Ernte Codex: TETRA-RECON-1 und TETRA-FOLLOWUP (Peerbus 07:53 und 08:06 CEST; eingetragen 2026-10-02 08:17:53 CEST)

- **Nachbau der Kettengeometrie (bedingte Rekonstruktion, Originalgenerator unbekannt):**
  - Regelmaessige Einheits-Tetraeder; jede neue Ecke ist die Spiegelung der viertaeltesten an der Flaeche der letzten
    drei. Das ergibt 12/20 Ecken, 9/17 Tetraeder, 30/54 Kanten.
  - 200 000 gleichverteilte Ebenennormalen durch das Eckenmittel:
    - Mittel P 10,224 / 12,662 gegen Buendel 10,204 / 12,633, also 1,7 / 1,2 Standardfehler
    - P(C > 1) 0,00101 / 0,0128 gegen 0,00099 / 0,0122
  - Gleiche Mediane und gleiche Wertebereiche.
  - Codex: "Vereinbarkeit, kein Nachweis gleicher Generatoren".
  - Exakte Zellflaechen auf der Kugel (deterministisch statt Stichprobe): Mittel 10,2187 / 12,6444.
- **Zaehlregel P = T3 + 2 T4 + 2 C:**
  - Gilt unter Einbettungs- und Stapelbedingungen auch ohne lokale Konvexitaet. Konvexitaet braucht man nur, um C mit
    Indexlaeufen gleichzusetzen.
  - Ein verzerrtes Paar (P 6, T3 2, C 2 bei einem Indexlauf) zeigt: Die Begruendung ueber Laeufe scheitert, die richtig
    definierte Formel nicht.
  - **Das korrigiert meine EINORDNUNG.md:** Dort ist die Konvexitaet als Bedingung der Regel genannt; sie ist nur eine
    Bedingung der Lauf-Lesart.
  - Geometrie-Audit, alle 36 + 136 Tetraederpaare: keine Selbstkontakte und keine Ueberlappungen innerhalb der
    LP-Toleranzen. Damit ist C als geometrische Inselzahl numerisch gestuetzt.
- **Mechanik (neues bedingtes Modell):** spannungsfreie Federn an allen Kanten, m = k = 1.
  - Genau 6 Nullmoden, keine negative Richtung.
  - Kleinste Kreisfrequenz: 0,3006 fuer 11+1, 0,1349 fuer 19+1 (Einheit sqrt(k/m)). Die Kette ist weich, die
    Biegemoden werden mit der Laenge schnell tiefer.
  - Gleichmaessiges Aufblaehen ("Atmen") ist keine Eigenmode der Kette.
  - In der ersten Mode bleibt P konstant (8 / 10); nur die Schnittflaeche schwankt, um 1e-5 relativ.
- **Ticks:** vollstaendige Vertex-Ereignisse fuer eine neu festgelegte Drehebene. Ohne die Originaldrehachse ist das kein
  Nachbau der Buendel-Ticks.
- **Offen bei Codex:** Originalgenerator, Bedeutung von "+1", Drehachse, nichtlineare Stabilitaet, Feldkopplung.
  M_E-G3 laeuft getrennt weiter (noch kein Ergebnis).
- **Neuer Codex-Plan FSM-43 (08:16 CEST, nur zur Kenntnis):** endliche Zustandsautomaten auf K3, C4, K4 und K1,3
  (Rotor-Router, ein Token), exakt durchgezaehlt; dazu reversible 2-Bit-Gatter und Fredkin.
  - Erwartete Perioden 2|E| (6/8/12/6) aus der bekannten Euler-Rotor-Struktur.
  - Codex kennzeichnet: keine physikalische Zeit oder Energie, die Periode ist keine emergente Periode.
  - Bezug zu Finns Tick-Idee [H]: Ein Rotor-Router ist eine Uhr aus reinen Zaehlregeln.

### Ernte LOG-NACHBAU (Agent fertig 08:30; ausgewertet 2026-10-02 08:31:44 CEST)

- **Vorhersage entsiegelt** (Klartext aus dem Scratchpad der Leitung; sha256 = VORHERSAGE.sha256 = d1a8b067..., geprueft):
  "LOG-NACHBAU, Vorhersage der Leitung, geschrieben 2026-10-02 07:45:59 CEST, vor jedem Lauf: Im Testmodell
  U = ln(1 + S) liegt im Fenster omega^2 0,70 bis 0,98 eine stille Stelle bei omega^2 = 0,9256 +- 0,001,
  rho = 1,8380 +- 0,002, Umlauf -1 (~80 %). Weitere stille Stellen im Fenster: keine (~70 %; der Bereich 0,95 bis 0,98
  ist bisher ungerechnet)."
- **Ausgang (Agent, eigener Code, blind):**
  - K1 bestanden: bewiesene Stelle auf 2e-7 / 5e-7, Umlauf -1 aufgeloest (0,36 rad).
  - K2 bestanden: Q und E auf 6e-11.
  - Blinde Suche, 57 Zeilen 0,700 bis 0,980: genau ein Vorzeichenwechsel von s (zwischen 0,925 und 0,930), ein
    zweiter Detektor bestaetigt.
  - Lage Stufe 1 / 2: omega^2 = 0,9256098 / 0,9256099, rho = 1,8379959 / 1,8379961. Die Stufen stimmen auf ~1e-7.
  - Die nachtraegliche Lage aus Runde 13 (0,925610 / 1,837996, mit dem alten Code) ist damit unabhaengig auf ~1e-6
    reproduziert.
  - **Umlauf nach dem eingefrorenen Plan (6 Halbierungsrunden):** -1 auf beiden Stufen, aber NICHT aufgeloest (groesster
    Sprung 2,46 rad > 0,4). Nach der Kartenregel zaehlt die Stelle damit nicht als gefunden.
    - Ursache laut Agent: Die Abstrahlamplitude ist auf diesem Ast sehr klein (1e-6 bis 1e-4); die Phase dreht auf einem
      kurzen Randstueck.
    - Die Rundenzahl hatte der Agent an K1 bemessen; das ist sein Planungsfehler, selbst angezeigt.
  - **Nachtraeglich** (PLAN-NACHTRAG-1 und -2, je vor dem Lauf eingefroren, aber nach Kenntnis des Ausgangs):
    - 24 Runden: aufgeloest, 0,357 rad.
    - Rechteck mit Halbbreite 1e-4: aufgeloest, 0,363 rad.
    - Randstreifen bis 1e-5 an den Fenstergrenzen: keine weitere Stelle.
- **Bewertung der Leitung:**
  - Die Lage ist blind und unabhaengig reproduziert, der Vorzeichenwechsel ist eindeutig. Vorhersage zu Lage, Umlauf -1
    und "keine weitere" eingetroffen.
  - Das Umlauf-Kriterium ist nur nachtraeglich erfuellt und zaehlt als **post hoc**.
  - Ich hebe den Nachtrag nicht in den Rang des Hauptplans. Das waere eine Entscheidung nach dem Ausgang und braeuchte
    erst eine Fremdstimme. Fuer die explorative Runde reicht die zweistufige Angabe.
  - Die Vorhersage stuetzte sich auf die Lage aus Runde 13. Die Lage ist darum keine neue Vorhersage; geprueft ist die
    Unabhaengigkeit des Codes.
- **Vorfall Scratchpad (Selbstanzeige des Agenten, von der Leitung nachgeprueft):**
  - Subagenten bekommen den Scratchpad der Leitung als ihren eigenen. Der Agent schrieb um 08:15:46 z1.txt und z2.txt
    hinein, nach allen Hauptlaeufen, und sah dabei den Dateinamen der Vorhersage, nicht ihren Inhalt.
  - Pruefung: Der Hash der Vorhersage stimmt. Die Datei ist laut mtime seit 07:45:59 unveraendert. z1/z2 sind
    verschoben; eigene Dateien dieses Namens hatte die Leitung nicht.
  - Lehre: Versiegelte Klartexte nicht im Scratchpad ablegen, sondern ausserhalb aller Agentenpfade.
- **Abschaetzung LOG-NACHBAU: weiter.** Die Log-Stelle ist jetzt kein Artefakt eines einzelnen Codes. Zweite stille
  Stelle in einem anderen Potential (Kasuya/Kawasaki-Typ), blind nachgebaut, Umlauf post hoc aufgeloest.

### DREI-TAKT gestartet und Frage Q-Ball gegen Hadronenhuelle (eingetragen 2026-10-02 08:34:15 CEST)

- **DREI-TAKT (Finn: "prüfe folgende hypothese: wenn zwei teile ein drittes bearbeiten ist es eine zeitlang stabil, und
  äußere einflüsse im gleichen takt können die stabilität positiv beeinflussen, aber äußere einflüssen können in einem
  3er system auch mehr chaos verursachen"):**
  - Karte RUNDE-16/drei-takt/KARTE.md, ab 08:32:15. Code-Agent ab ~08:34 auf cpu3 und cpu4.
  - Zerlegung:
    - H1: zeitweise stabil
    - H2: gleicher Takt stabilisiert
    - H3: aeusserer Einfluss erzeugt Chaos, und drei ist dabei besonders
  - Modelle:
    - D1: Trojaner-Problem L4 mit Exzentrizitaet bzw. pulsierender Anziehung, Floquet und Lebensdauer
    - D2: Adler-Phasenmodell, zwei Schrittmacher und ein Dritter
    - D3: Kuramoto-Sakaguchi, N = 2 und 3 mit Takt, N = 3 und 4 ohne
  - Vorhersagen stehen in der Karte. Kern der Erwartung: Die Antwort haengt davon ab, ob das System konservativ oder
    gedaempft ist. Im gleichen Takt hilft der Einfluss nur in Phase. Chaos braucht mindestens drei Freiheitsgrade, also
    erst drei Phasen mit Takt.
- **Finns Frage "q-balls und hadronenhüllen ist das das gleiche vice versa"** (Chat-Antwort, Grundlage Runde 12,
  QUARK-1):
  - Gleiche Familie (nichttopologische Solitonen bzw. Beutel), nicht dasselbe, in keiner Richtung.
  - Q-Ball: Ladung und Huelle sind ein Feld (Bosonen in einem Zustand, Spin 0 bzw. ganzzahlig).
  - Hadronbeutel: Huelle (Vakuumdruck B bzw. neutrales sigma) und Inhalt (Quarks, Fermionen, Farbe, Spin 1/2) getrennt.
  - Unterscheidungspunkt Masse gegen Ladung [ES fuer unser Modell, L? fuer die Literatur]:
    - Beutel M ~ N^(3/4).
    - Unser sextischer Ball ist bei grosser Ladung ein Tropfen: feste Innendichte S = 1, E -> omega_min Q = 0,707 Q,
      also linear wie ein Kern im Troepfchenmodell.
    - Q-Baelle in flachen Potentialen folgen E ~ Q^(3/4) und sind mathematisch Beutel (Dvali/Kusenko/Shaposhnikov 1998,
      [L?]).
  - Bruecken: Friedberg-Lee-Beutel, B-Baelle, Quarkklumpen; der leere Beutel als Pruefpunkt (Runde 12).
- **Zur Kenntnis (Codex, von Finn direkt beauftragt):**
  - Eigenes Review von Finns Arbeitsmodell in RUNDE-16/two-sides-review/codex/ (ARBEITSMODELL-V2.md,
    ESSENZ-REVIEW.txt, SECOND-READ.txt, state-machine).
  - FSM-43 fertig (Ganzzahl-Enumeration, 0,004 CPU-s).
  - Plan "Live-Simulationsmodus": causal.html im qball-explorer, mit Rotorautomat, Zentralfedern u. a.
  - Abgleich mit der v2 der Leitung folgt in der naechsten Runde.
- Aktive Agenten: AUSPROBIEREN (cpu, cpu2), DREI-TAKT (cpu3, cpu4). Codex: M_E-G3.

### Finn: "prüfen alles und noch mal in die codex session gucken und weiter prüfen und rechnen" (eingetragen 2026-10-02 08:51:57 CEST)

- **Codex-Sitzung (Peerbus und Dateien, gelesen 08:47 bis 08:50):**
  - FSM-43 fertig (08:20 CEST):
    - Rotor-Router mit einem Token auf Dreieck, Quadrat, K4 und Dreistern. Perioden 6 / 8 / 12 / 6 = 2|E|, jede
      gerichtete Kante genau einmal je Zyklus. Das ist das bekannte Lemma, ohne Neuheitsanspruch.
    - Negativer Befund: Alle vier Vollzustandsabbildungen sind nicht bijektiv (K4: 96 Zustaende ohne Vorgaenger). Der
      Automat ist darum kein umkehrbares Mechanikmodell.
    - Popcount-erhaltende 2-Bit-Bijektionen: nur Identitaet und SWAP. Fredkin (3 Bit) ist bijektiv, selbstinvers und
      erhaelt den Popcount.
    - Codex: kein Beleg fuer drei Raumdimensionen, fundamentale Zeit oder eine Energiequelle.
  - Live-Modus fertig (08:38 CEST), Finns Direktauftrag an Codex:
    - model-lab/simulation-environment/qball-explorer/causal.html, mit Rotorautomat, Zentralfedern und gekoppeltem
      psi/chi-Graphfeld; QA bestanden.
    - Keine Q-Ball-, Spin- oder Gravitationsaussage.
  - FLIP-CLOCK geplant (08:47): Zweimodenmodell, Rabi-Austausch gegen Selbstfang, als Kontrollanker fuer eine
    "Flip-Tick"-Lesart.
  - M_E-G3 steht bei Codex weiter offen.
  - **Codex' eigene v2 von Finns Arbeitsmodell** (two-sides-review/codex/ARBEITSMODELL-V2.md):
    - Zweifeldmodell, psi komplex und chi reell, U = (1/4)(chi^2 - 1)^2 + (1 + chi^2) S - S^2 + S^3/2, U >= 0
      (Identitaet von der Leitung nachgerechnet).
    - Gegenlesung ESSENZ-REVIEW: Der Kern ist faktorensicher; vier kleine Textkorrekturen.
- **Abgleich mit der v2 der Leitung:**
  - Kinetik ohne 1/2: uebereinstimmend.
  - omega^2-Fenster m^2 - lambda^2/(4g) < omega^2 < m^2: uebereinstimmend.
  - "Anziehung nicht eingesetzt": uebereinstimmend. Codex ergaenzt, dass abnehmende J, K bei festen Feldern sogar
    abstossen.
  - **Fehler in meiner v2 gefunden und berichtigt (08:49:06):** Das Vorzeichen der Ladung Q war falsch (ergab
    Q = -2 omega Integral f^2). Jetzt gilt Q = 2 Im Integral Phi* dPhi/dt, in Paragraph 1, 2 und 22. Finns
    Downloads-Kopie ist aktualisiert (sie war unveraendert, cmp).
- **BEUTEL-1 gestartet** (Karte RUNDE-16/beutel-1/KARTE.md ab 08:50:32, Agent auf cpu6):
  - Frage: Baut sich der Q-Ball in Codex' Zweifeldmodell eine Huelle (chi -> 0 innen), und ist er dann Tropfen
    (E ~ Q) oder Beutel (E ~ Q^(3/4))?
  - Modelle:
    - M1: Projektball
    - M2: Codex-Zweifeld; innen sieht psi genau unser U plus die Beutelkonstante 1/4
    - M3: Friedberg-Lee-Sirlin-artige Kontrolle mit masselosem Inhalt
  - Schreibtischwerte und Vorhersagen B1 bis B7 stehen in der Karte, z. B. M2 duenne Wand E/Q -> 0,853, Huellenanteil
    ~ 0,15 statt 1/4.
- VS-1: seit 30.09. fertig (Ausgang B2, F-1 erledigt); nichts offen. Keine wartenden formalen Laeufe faellig.
- Aktive Agenten: AUSPROBIEREN (cpu, cpu2), DREI-TAKT (cpu3, cpu4), BEUTEL-1 (cpu6). Damit sind es drei, das Maximum.

### Ernte AUSPROBIEREN V1-V5 (Agent fertig ~08:54; ausgewertet 2026-10-02 08:54:53 CEST)

Plan eingefroren 08:23:14, nach der Karte (08:15:23). 37 von 90 min Zeitbox. Die Zahlen sind in ERGEBNIS.md gegengelesen.

| Nr | Vorhersage | Ausgang |
|---|---|---|
| V1 | Spektrum (k/m) x {0 (6x), 1, 1, 2, 2, 2, 4} (95 %) | **eingetroffen**, exakt |
| V2 | Ring stabil genau fuer N >= 7 bei kleinem m/M (70 %) | **eingetroffen**: N = 3-6 bei jedem m/M instabil, ab 7 stabil unter einer Grenze |
| V2 | Stabiles m/M ~ N^-3 (60 %) | **eingetroffen**: Steigung -3,01, Vorfaktor 2,45 (N = 7) bis 2,301 (N = 64), -> Maxwells 2,298, also M > 0,435 N^3 m |
| V4 | Ereignisgenaue Zaehlung gleich fuer alle dt (95 %) | **teilweise**: 1226 Ticks bei jedem dt <= 0,1 (Zeiten auf 4e-13), bei dt = 0,2 fehlen 6 (0,5 %) |
| V4 | Naive Zaehlung haengt von dt ab (70 %) | **eingetroffen**: Verlust ~ proportional zu dt, 13 % bei dt = 0,2 |
| V3 | Kein N auffaellig, 11 und 19 nicht ueber 3 sigma (85 %) | **eingetroffen fuer 11 und 19**. Die Kennzahl war aber untauglich (entartet bzw. Rauschen); markiert wurden 9, 10, 12, 17, 25, alle an Regimegrenzen oder im Rauschen |
| V3 | Ab kritischem Omega instabil (70 %) | **nicht eingetroffen**: spannungsfrei stabil bis R -> unendlich. Mit gleichen Ruhelaengen knickt der Ring schon in Ruhe (eben ab N = 10, raeumlich ausser N = 6), und **Rotation stabilisiert** ihn wieder (Omega 0,38 bei N = 10 bis 0,89 bei N = 32) |
| V5 | Lokalisierte Moden fuer omega^2 in (0,5; 1) bei kleinem J (80 %) | **nicht eingetroffen**: Fenster [1/3 + O(J), 1 - O(J)], z. B. [0,475; 0,96] bei J = 0,05 |
| V5 | Kein N besonders (85 %) | **eingetroffen** (post hoc, nicht eingefroren: v5b N = 4..26, alle abs(z) <= 1,3). Die scheinbare "11" ist die Schwelle J N ~ 0,55 fuer eine Zentrumsmode; sie wandert mit J (N_max 20, 15, 11, 9, 7 fuer J = 0,03 bis 0,08) |

- Schreibtisch-Nachrechnung der Leitung zu V5:
  - Im Antikontinuumslimes (J -> 0) gilt fuer einen Einzelplatz omega^2 = V'(S) = 1 - 2S + 1,5 S^2, mit dem Minimum
    1/3 bei S = 2/3. Das erklaert die untere Kante 1/3.
  - Im Kontinuum zaehlt stattdessen min V(S)/S = 1/2 (Coleman). Diskret ist das Fenster also breiter als im Kontinuum.
    Das ist ein Unterschied der zwei Seiten des Feldes [ES].
- Stabilitaetskriterium:
  - "Zahl negativer Richtungen plus Vorzeichen von dQ/domega" traf an allen 3954 Punkten.
  - Das reine "dQ/domega < 0" waere auf dem grossen Zweig falsch gewesen.
  - Folge: Die Formulierung in v2 Paragraph 7 wird praezisiert, siehe unten.
- Selbstanzeigen des Agenten:
  - Die ersten V2- und V3-Laeufe liefen ins 10-min-Limit (BLAS-Threads gegen einen Kern). Danach in Teilen mit einem
    Thread wiederholt; Grenzwerte bitgleich.
  - Der V5-Nachtrag v5b ist nicht eingefroren und zaehlt als post hoc.
- **Abschaetzung:**
  - V1 und V2: weiter, als Positivkontrollen fuer kuenftige Ringlaeufe (Code geprueft).
  - V4: weiter; ereignisgenaue Ticks sind der Standard fuer jede Tick-Messung.
  - V3: parken; die Kennzahl war untauglich. Der Befund "Rotation stabilisiert" geht an DREI-TAKT (H2) als Beobachtung.
  - V5: weiter, als Bruecke zwischen diskretem und kontinuierlichem Fenster (1/3 gegen 1/2).
  - 11 und 19: in keinem der fuenf Versuche besonders. In diesen Modellen nicht gestuetzt; kein "widerlegt".

### Literaturpruefung, Codex-Uhren, Gegenleser v2 (Finn: "mach weiter"; eingetragen 2026-10-02 08:58:48 CEST)

- **Beutelgesetz an der Quelle gelesen [S]:** Dvali/Kusenko/Shaposhnikov, hep-ph/9707423v2 (PDF, Abschnitt nach Gl. 6):
  "Another important property of a large Q-ball in a flat potential is that its energy grows as E ∝ Q^3/4, rather than
  Q ... because the Q-ball in a flat potential never becomes a thin-wall object. If the scalar VEV remained constant, the
  soliton mass would grow as the first power of charge."
  - Damit sind beide Chat-Aussagen von 08:3x belegt: flaches Potential E ~ Q^(3/4), konstante Innendichte E ~ Q.
  - Ihr Ansatz E ~ a omega + b/omega^3 + omega Q ist dieselbe Struktur wie das Beutelmodell, mit b/omega^3 ~ B R^3 und
    R ~ 1/omega.
  - Die anderen zwei arXiv-Abfragen (L4 im elliptischen Problem, Maistrenko-Phasenchaos) scheiterten an HTTP 429 bzw.
    Zeitueberschreitung. Sie bleiben dem DREI-TAKT-Agenten ueberlassen, damit wir uns nicht gegenseitig drosseln.
- **Codex, FLIP ALS UHR** (08:49 CEST), Finns Direktauftrag:
  - Im psi/chi-Modell kann psi bei Q ungleich 0 nie ganz verschwinden: I >= Q^2/(4E) (Cauchy-Schwarz).
  - Der Zweimodenarm zeigt Rabi-Austausch: voller Transfer nur bei delta = 0. Selbstfang bei lambda = 6, g = 1:
    P_b <= 0,1273, numerisch getroffen.
  - Codex: bekannte Physik; eine hamiltonsche periodische Bewegung ist kein anziehender Grenzzyklus.
  - Danach CLOCK-PAIR geplant: zwei wechselseitig gekoppelte Flip-Uhren mit begrenztem Phasenversatz. Das passt zu
    DREI-TAKT H2 (Rastung).
- **v2 ergaenzt** (08:55:58), Downloads-Kopie aktualisiert:
  - Maxwell-Ring gerechnet
  - Zaehlregel nach Codex berichtigt
  - Rotation stabilisiert den geknickten Federring
  - Stabilitaetskriterium praezisiert (negative Richtungen plus dQ/domega)
  - diskretes Fenster (1/3, 1) gegen Kontinuum (1/2, 1)
  - ereignisgenaue Ticks
  - 11 und 19 unauffaellig (J N-Schwelle)
- **Frischer Gegenleser fuer v2 gestartet** (pruefer-opus, ~09:00): vorwaerts jede Formel, rueckwaerts jede Behauptung,
  Abgleich mit Codex' Fassung. Ergebnis in zwei-seiten/GEGENLESUNG-v2.md; der Autor formuliert danach selbst.
- Aktive Agenten: DREI-TAKT, BEUTEL-1, Gegenleser v2 (drei).

### Ernte BEUTEL-1, STABIL-6-8-12, Gegenlesung v2 und v2.1 (Finn: "fokus auf die stabilen dingsda - 6er 8er 12er"; eingetragen 2026-10-02 09:23:40 CEST)

- **BEUTEL-1** (Agent fertig ~09:18; RUNDE-16/beutel-1/ERGEBNIS.md): **B1 bis B7 alle eingetroffen.**
  - M1 (Projektball): E/Q -> 0,707106, S(0) -> 1,000001. Ein Tropfen.
  - M2 (Codex-Zweifeld): E/Q -> 0,853266, S(0) -> 1,179653, Huellenanteil -> 0,14554 (Schreibtisch 0,853 / 1,18 /
    0,146).
    - Die Huelle bildet sich ab Q ~ 370 (chi(0) < 0,1), am Dickwand-Ende ist chi(0) = 0,96.
    - p = d ln E / d ln Q liegt immer zwischen 0,90 und 1. Der Ball baut sich also eine Huelle, bleibt aber ein Tropfen.
  - M3 (FLS-Kontrolle, freier Inhalt): p = 0,7503, Huellenanteil 0,2497, E/Q^(3/4) = 4,187 (Formel 4,189).
    Beutelstrecke von Q = 143 bis 1e5.
  - Literatur, nur Abstract: Kim/Nugaev/Shnir, arXiv:2405.09262. Grosse FLS-Solitonen gehen von Q^(3/4) zum linearen
    Gesetz ueber, sobald ein Kondensat bzw. eine neue Massenskala auftritt. Dass M2 diesem Mechanismus folgt, ist [H] des
    Agenten.
  - Kontrolle teilweise:
    - Gittervergleich 0,04 gegen 0,02 ergab 1,8e-4 statt < 1e-4. Im eingefrorenen Nachtrag zeigt ein drittes Gitter
      saubere zweite Ordnung (< 5e-5); das zaehlt als nachtraeglich.
    - Virial <= 2,8e-4, dE/dQ = omega im Median 1e-6.
  - Selbstanzeigen: Q_max von M3 wurde nach den Rauchtests gesetzt; B7 besteht auch bei 1e3 und 1e4. "Stabil" heisst
    nur dQ/domega < 0; gerechnet sind nur kugelsymmetrische Loesungen.
  - **Antwort auf Finns Frage:** Q-Ball und Hadronenhuelle sind verwandt, nicht dasselbe. Die Huelle allein macht
    keinen Beutel; das Beutelgesetz kommt von einem freien Inhalt.
  - **Abschaetzung: weiter.** Naechster Schritt waere die stille Stelle im Zweifeldmodell; dort oeffnet der chi-Kanal
    bei rho > sqrt(2) [H].
- **STABIL-6-8-12** (Leitung rechnet selbst, 09:13 bis 09:21; ERGEBNIS.md):
  - S1, S3, S4 und S5: alle Vorhersagen eingetroffen.
    - 12 ist die stabile Zahl im Raum: Ikosaeder auf der Kugel, 13 = 12 + 1 bei Lennard-Jones, fcc als einziges starres
      Nachbarfedergitter.
    - 6 ist die stabile Zahl in der Ebene.
    - 8 ist nirgends besonders: Der Wuerfel ist ein Sattel, bcc wackelt.
    - 11 ist auf der Kugel anti-magisch, 19 bei Lennard-Jones magisch.
    - Die Automatenperioden sind 2|E|.
  - S6 (Feldklumpen auf Polyedern): teilweise. Nur bei omega^2 = 0,6 zaehlt der Grad. Die Methode war fuer den kleinen
    Ast unzureichend; selbst angezeigt.
  - **Selbstanzeige der Leitung:** In einer lokalen jq-Pipeline stand awk als wirkungsloser Durchreicher (Regel: lokal
    kein awk). Es hat nichts gerechnet.
  - **Abschaetzung:**
    - S1, S3, S4, S5: weiter, als gepruefte Werkzeuge und Antwort an Finn.
    - S6: parken, bis eine Wiederholung mit Lokalisierungskriterium sinnvoll ist (dann post hoc).
- **Gegenlesung v2** (pruefer-opus, 08:58 bis 09:14; zwei-seiten/GEGENLESUNG-v2.md): 32 Befunde, davon 4 Fehler.
  - B1: Das diskrete Fenster ist nicht einfach "breiter".
  - B2: Ein Q-Ball ist nicht "stabil, weil Q erhalten ist".
  - B3: Die Massenmatrix 2 fuer Feldkomponenten fehlte.
  - B4: Schnittlaengen und -flaechen sind stetig.
  - Dazu eine schwere Ueberdehnung U1: "11 und 19 nirgends besonders", obwohl Variante T ungerechnet ist.
- **v2.1 geschrieben** (ab 09:16:54), alle 32 Befunde eingearbeitet.
  - v2.0 archiviert als ZWEI-SEITEN-DES-FELDES-v2.0-stand-0855.md.
  - Finns Downloads-Kopie durch v2.1 ersetzt (09:19:14; sie war unveraendert, cmp).
  - Die letzte Schicht wird erneut frisch gelesen (naechster Schritt).

### Codex CLOCK-PAIR (Peerbus 08:55 CEST; eingetragen 2026-10-02 09:37:47 CEST) und TETRAKETTE-1 gestartet

- **CLOCK-PAIR (Finns Direktauftrag an Codex):** zwei konservative Flip-Uhren mit 3 % verschiedener Eigenfrequenz,
  wechselseitig gekoppelt (K/2 (z1 - z2)^2).
  - Kein Gleichlauf bei K = 0, 0,2 und 1 (mit Kick). K = 1 ohne Kick ist UNDEFINED nach der Vorabregel (Radius 0,026 <
    0,05).
  - Warnung von Codex: Eine hohe kreisstatistische Konzentration allein zeigt kein Festhalten der Phase. Die stationaere
    Kontrolle haette sonst einen falschen perfekten Erfolg geliefert.
  - Bezug DREI-TAKT H2 [H, Leitung]: Ohne Daempfung keine Rastung; das passt zur Vorab-Erwartung "konservativ gegen
    gedaempft".
- **TETRAKETTE-1** (Finn: "rechne die tetraederkette 11+1 und 19+1"):
  - Karte tetrakette-1/KARTE.md ab 09:34:03; Nachtrag (Bisektionsboden) vor dem Lauf.
  - Die Leitung rechnet selbst, Laeufe ab 09:37 auf cpu und cpu2.
  - Vorab-Schreibtisch: theta = arccos(-2/3) hat die Kettenbruch-Naeherung 4/11. Nach 11 Schritten ist die Helix also
    fast genau 4 Umlaeufe weiter (9,9 Grad). Darum ist N = 12 die kleinste Kette mit fast ausgerichteten Ecken; geometrisch
    [ES], keine Stabilitaet.

### Ernte DREI-TAKT (Agent fertig ~09:38; ausgewertet 2026-10-02 09:39:04 CEST)

Plan eingefroren 08:47:17, nach der Karte (08:32:15). Nachtraege 1 bis 3 eingefroren; Nachtrag 3 (Kontrolle unter mu_R)
ist nach dem Hauptlauf beschlossen und zaehlt als post hoc.

| Teil | Antwortklasse | Modell und Zahlen |
|---|---|---|
| H1 eine Zeitlang stabil | **gestuetzt** (Phasenmodell); **teilweise** (Gravitation) | D2a: Rastdauer ~ Abstand^(-1/2), Steigung -0,5001, Adler auf 2e-9. D1b: endliche Lebensdauern oberhalb mu_R, aber Steigung -0,24 statt -0,5; das Kriterium (Abstand 0,5) misst nichtlineares Herausfallen |
| H2 gleicher Takt stabilisiert | **teilweise** | D2b: nur in Phase (Rastung ab F = 0,1), gegenphasig nie. D1a: e macht 59 % der stabilen Flaeche unter mu_R instabil, schafft aber oberhalb mu_R einen schmalen stabilen Streifen bis mu = 0,0458 (e 0,055 bis 0,29). D1d: oberhalb mu_R stabilisiert ein Takt nahe der Eigenfrequenz (0,6 bis 0,8) am haeufigsten, ein schneller (> 3) selten |
| H3 Takt erzeugt Chaos im Dreiersystem | **gestuetzt** (Phasenmodell); **offen** (Gravitation) | D3: N = 3 mit Takt 38/40 robust chaotisch (lambda_max bis 0,29). N = 2 mit Takt und N = 3 ohne Takt <= 0,0024 (2-Torus). N = 4 ohne Takt 39/40 chaotisch. Drei Teile plus Takt ist die kleinste chaosfaehige Zahl. D1c offen |

- Vorhersagen: 9 von 13 eingetroffen.
  - Eingetroffen: K, D1a-1, **D1a-2 (35 %)**, D1d-1, D1b-2 (mit Vorbehalt), D2a, D2b, D3-1, D3-2, D3-3.
  - Nicht eingetroffen: D1d-2 (Leitung erwartete Kapitza-Fenster; tatsaechlich hilft eher der Takt nahe der
    Eigenfrequenz) und D1b-1.
  - Offen: D1c.
- **Bedeutung fuer Finn [H, Leitung]:**
  - Seine H2 ist bei der Gravitation staerker gestuetzt, als die Leitung erwartet hatte: Ein Rhythmus nahe der
    Eigenfrequenz kann eine oberhalb der Routh-Grenze instabile Trojaner-Lage stabilisieren.
  - Derselbe Rhythmus zerstoert aber auch viel bisher Stabiles.
  - Bei Taktgebern hilft der gleiche Takt nur mit der richtigen Phase. Codex' CLOCK-PAIR zeigt dazu: Ohne Daempfung
    gibt es keine Rastung.
- Selbstanzeigen des Agenten:
  - Zwei Laeufe liefen in die 10-min-Grenze.
  - N = 4 hat nur 1000 Punkte, nachgerechnet wurden die 40 groessten Treffer.
  - Die D2c-Parameter waren unguenstig.
  - **Lokal python** einmal fuer einen Textersatz und dreimal fuer eine Syntaxpruefung, gegen den Auftrag.
- Literatur: zwei Abstracts (arXiv:1206.6162, 1308.4745); sonst [L?].
- **Abschaetzung DREI-TAKT: weiter.**
  - D1a/D1d (Stabilisierung oberhalb Routh durch Takt nahe der Eigenfrequenz) verdient eine eigene Karte. Dabei soll
    gegen die Literatur zum elliptischen eingeschraenkten Problem gelesen werden (Danby-Diagramm [L?]).
  - D3 ist erledigt.

### Ernte TETRAKETTE-1, Gegenlesung v2.1, v2.2 (eingetragen 2026-10-02 09:47:42 CEST)

- **TETRAKETTE-1** (Leitung, Laeufe 09:37 bis 09:40; tetrakette-1/ERGEBNIS.md):
  - In Steifigkeit, Feldklumpen, LJ-Bindung und Schnittstatistik sind 12 ("11+1") und 20 ("19+1") Ecken nicht besonders.
    20 ist nirgends markiert. 12 ist nur im Verbund mit dem Kurzkettenbereich 8 bis 14 markiert; das Kriterium war dort
    untauglich (Selbstanzeige).
  - Geometrie (K0, vorab vorhergesagt, eingetroffen): theta = arccos(-2/3) auf 1e-13.
    - 11 Schritte ergeben fast 4 Umlaeufe (9,9 Grad); bei 12 Ecken liegen also erstmals zwei Ecken fast uebereinander.
    - Erst bei 31 Ecken wird es besser (5,7 Grad).
  - Post hoc [H]: Die zwei tiefsten Biegeschwingungen fallen fast zusammen bei 9, 12 und 15/16 Ecken, wo neue
    Fast-Ausrichtungen dazukommen.
  - Codex reproduziert: omega_1 auf 1e-12, mittleres P auf 0,004. Die Zaehlregel gilt in 12 Mio. Stichproben.
  - Unter LJ ist die Kette fuer alle N ein lokales Minimum, liegt aber weit ueber dem kompakten Cluster (6,2 bei 12 Ecken,
    19,3 bei 20 Ecken).
  - Selbstanzeigen:
    - Kriterium fuer kurze Ketten untauglich.
    - Hesse-Schwelle 1e-6 fuer h = 1e-4 zu eng; die Werte sind Nullmoden mit h^2-Fehler.
    - Ein unnoetiger python-print auf der .69 ausserhalb kleintest.
  - **Abschaetzung: parken** fuer Stabilitaetsfragen (kein Signal bei 12 und 20). **Weiter** fuer die Geometrie, siehe
    Finns Fragen unten. Der Kettenbruch 4/11, 11/30 ist der flache Schatten des 30er-Rings im 600-Zell [L?].
- **Gegenlesung v2.1** (pruefer-opus, 09:23:58 bis 09:39:09): 29 von 32 erledigt; 16 neue Befunde.
  - Auflagen:
    - N1: Anziehung aus Feldrelaxation ist falsch, J(r) mit J' < 0 stoesst immer ab.
    - N2: "sonst Schritt verkleinern" ist nicht umsetzbar.
    - N5: 11+1 war vorschnell auf die Tetraederkette festgelegt.
- **v2.2** (ab 09:44:01):
  - Eingearbeitet: N1 bis N16, TETRAKETTE-1 in Paragraf 14, BEUTEL-1 in Paragraf 1.
  - Archiviert: v2.1-stand-0919.
  - Downloads ersetzt um 09:46:17 (v2.1 war dort unveraendert).
  - Frischer Blick nur auf den diff (DIFF-v2.1-v2.2.txt) laeuft ab ~09:47.

### Finns Fragen: kleinste Teilchen, Dimensionen, 3/4 und 4/3, Kraefte, Eigenschaften (Chat-Antwort; eingetragen 2026-10-02 09:49:01 CEST)

- Woertlich: "was bedeutet das für theorien von den kleinsten teilchen? können wir daraus dimensionen ableiten? können
  wir daraus 3/4 bzw 4/3 flipping ableiten? was für kräfte können wir daraus ableiten? was für eigenschaften?"
- **Antwort der Leitung (Kern) [ES/H]:**
  - Keine Herleitung von Elementarteilchen, Dimension oder neuen Kraeften.
  - Wohl aber Dimensions-*Messer*:
    - Kusszahl (6 in 2D, 12 in 3D)
    - Steifigkeitsgrenze der Federnetze
    - Beutelexponent p = d/(d + z) und Huellenanteil h = z/(d + z) mit z = 1. Gemessen in BEUTEL-1: d = 3,005 aus p wie
      aus h.
  - 3/4 und 4/3 sind Kehrwerte desselben Beutel- bzw. Strahlungsgesetzes (4 = d + 1 wegen omega ~ k). Mit Masse oder
    Selbstbindung kippt der Exponent auf 1 (Tropfen).
  - Das T3/T4-Kippen in Schnitten und Codex' 4 x 3 = 12 sind nur Zaehlungen.
  - Kraefte:
    - Beutel-Druckbilanz B gegen Strahlungsdruck epsilon/3 (im Modell abgeleitet)
    - Cauchy-Relation C12 = C44 bei reinen Paarkraeften (in S1 exakt)
    - J(r) stoesst nur ab
    - Takt nahe der Eigenfrequenz stabilisiert Trojaner jenseits von Routh (DREI-TAKT)
- **DIM-BEUTEL gestartet** (Karte RUNDE-16/dim-beutel/KARTE.md ab 09:47:42, Agent cpu/cpu2):
  - Misst der Beutelexponent die spektrale Dimension, d_s = p/(1 - p)?
  - Graphen: Kette, Quadrat, kubisch, Sierpinski-Dreieck.
  - Unterscheidungspunkt: Sierpinski 0,577 (d_s) gegen 0,613 (d_H).
- Aktive Agenten: Gegenleser v2.2-diff, DIM-BEUTEL.

## Abschaetzung Runde 16 (Leitung, 2026-10-02 09:51:13 CEST)

| Karte | Ergebnis kurz | Abschaetzung |
|---|---|---|
| M_E-G3 (Codex) | Theoriekarte offen, Codex arbeitete an Finns Direktauftraegen | in Runde 17 uebernommen |
| LOG-NACHBAU | Log-Stelle blind und unabhaengig auf ~1e-6 reproduziert; Umlauf nur post hoc aufgeloest | weiter |
| TETRA-Buendel (Codex) | Nachbau vereinbar; Zaehlregel allgemeiner; Mechanik weich | parken (durch TETRAKETTE-1 abgedeckt) |
| Check ChatGPT-Rahmen | Spielzeugmodell; Raumzeit vorausgesetzt; Korrekturen | erledigt (in v2 aufgegangen) |
| ZWEI-SEITEN v2 bis v2.2 | zwei frische Lesungen, 4 + 1 Fehler behoben, Ergebnisse eingebaut | weiter (frischer Blick auf den v2.2-diff laeuft) |
| AUSPROBIEREN V1-V5 | Positivkontrollen V1, V2 bestanden; V4 ereignisgenaue Ticks; V3 Rotation stabilisiert; V5 Fenster (1/3, 1) | V1/V2/V4/V5 weiter als Werkzeuge; V3 parken |
| DREI-TAKT | H1 gestuetzt (Phasen), H2 teilweise, darunter Trojaner jenseits von Routh stabilisiert; H3 gestuetzt (Phasen) | weiter: eigene Karte zu D1a/D1d mit Literatur |
| BEUTEL-1 | B1 bis B7 eingetroffen: Huelle ja, Tropfen bleibt Tropfen; Beutel braucht freien Inhalt | weiter: stille Stelle im Zweifeldmodell |
| STABIL-6-8-12 | 12 (Raum), 6 (Ebene) stabil; 8 nicht; 11 anti-magisch; 13/19 magisch (LJ) | S1/S3/S4/S5 weiter (Werkzeuge); S6 parken |
| TETRAKETTE-1 | 12/20 Ecken nicht stabiler als die Nachbarn; Geometrie 4/11 bzw. 11/30 | Stabilitaet parken; Geometrie weiter (600-Zell-Lesung [L?]) |
| DIM-BEUTEL | laeuft (Beutelexponent als Dimensionsmesser) | in Runde 17 uebernommen |

**Lehren der Runde:**
- (1) Frische Gegenleser fanden zweimal echte Fehler in Finns Arbeitsdokument. Jede weitergegebene Fassung bekommt einen
  Leser der letzten Schicht.
- (2) Ein "Auffaellig"-Kriterium braucht vorab die Regimegrenzen, sonst markiert es Endeffekte (TETRAKETTE-1, V3).
- (3) Agenten teilen den Scratchpad der Leitung (Memory angelegt).
- (4) Selbstanzeigen lokaler Interpreteraufrufe:
  - zwei Agenten, python fuer Syntax und Textersatz
  - die Leitung, awk-Durchreicher und ein python-print auf der .69
  - Die Regel gilt weiter. Die Auftraege nennen jetzt den Weg ueber py_compile auf der .69.

## Einfach gesagt (Runde 16)

Diese Runde hat viele von Finns Fragen nachgerechnet. Ein Q-Ball kann sich mit einem zweiten Feld eine Huelle bauen,
bleibt aber ein Tropfen. Ein "Beutel" wie bei Hadronen entsteht erst, wenn der Inhalt frei schwingen kann, und dann
waechst die Energie mit dem Exponenten 3/4. Bei vielen gleichen Teilchen sind 12 (im Raum) und 6 (in der Ebene)
besonders stabil, die 8 nicht. Die Tetraederkette mit 12 oder 20 Ecken ist nicht stabiler als ihre Nachbarn; besonders
ist nur, dass sie sich nach 11 Schritten fast genau viermal gedreht hat.

## Rundenabschluss (Leitung, 2026-10-02 09:51:49 CEST)

- Journal: claude-runde-v3-16-20261002, Index nr 553; pruefen ohne Befund; Quellen-Hashes in RUNDE-16/journal-quellen.txt.
- Sicherung .69 -> TS440 gestartet (ohne --delete, nice/ionice). Log: /home/fmh/sicherung-dot69-ts440-lauf-20261002-r16.log.
- In Runde 17 uebernommen:
  - M_E-G3 (Codex)
  - DIM-BEUTEL (laeuft)
  - Frischer Blick auf den v2.2-diff (laeuft)
  - Neue Karten: stille Stelle im Zweifeldmodell (Q-Ball-Schwerpunkt); Takt jenseits von Routh mit Literatur; 600-Zell-Lesung
