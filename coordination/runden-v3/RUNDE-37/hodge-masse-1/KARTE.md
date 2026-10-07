# HODGE-MASSE-1: Ist ein Teil der Richtungsabhaengigkeit der Schwerewellen ein Artefakt der Eich-Reduktion, und hilft eine volumengewichtete Bewegungsenergie beim Umklappen? (Runde 48, Folgekarte zu TAKT-DYNAMIK-1, DANZER-NAEHERUNG-2, TT-GLAS-2, IMPULS-NETZ-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 09:24:50 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - **DANZER-NAEHERUNG-2:** Mit umkreisbasierten DEC-Gewichten ist das Grundtempo von Skalar und Maxwell auf jedem periodischen Netz exakt isotrop, weil Summe *1 l l^T = Vol I gilt [M].
  - **TT-GLAS-2:** Die TT-Anisotropie sitzt in der Bewegungsenergie. Mit isotroper Ersatzmasse A3 bleibt etwa die Haelfte, und dieser Rest kommt aus der Projektion auf den Eichvertreter; unprojiziert sind es 0,00 %.
  - **IMPULS-NETZ-1:** Ohne Impulskopplung haengt die Leckage an der Eichwahl (0,013 bis 0,044).
  - **TAKT-DYNAMIK-1:** Beim Delaunay-Umklappen springt die Energie einer Welle um 0,2 bis 0,5 % je Zug. Der Sprung sitzt in der Bewegungsenergie mit gleicher Traegheit je Zelle (J = 1), die Regge-Energie bleibt stetig.
  - **TT-ISO-1:** Die Bewegungsenergie je Tetraeder ist eine DeWitt-Form. A2 = A1 mit J_t -> J_t V_F/V_t (volumengewichtet) gab auf V 5,92 %, auf S 6,41 % (Paarung A2R1). Die Isotropie gelang nur mit abgestimmten Gewichten (Kegel 0,090, Sechseck 1,00).
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Fragen

1. **Reduktion:**
   - Ist die Reduktion R1 (bzw. R2) im Projektcode die horizontale, also die zur Bewegungsenergie orthogonale Reduktion auf den Eichvertreter (symplektische Reduktion: K_red(v) = min ueber Eichrichtungen g von K(v + g))?
   - Wenn nicht: Haengt das TT-Spektrum mit R1 von der Wahl der Eichflaeche ab, und mit horizontaler Reduktion nicht mehr?
2. **Spanne:** Wie gross ist die TT-Spanne ohne Abstimmung mit horizontaler Reduktion und Bewegungsenergie A1 (J = 1) bzw. A2 (volumengewichtete DeWitt-Form)?
   - Netze: V, S (= C15), A15 (DEFEKT-NETZ-1) und Glas N = 128 (TT-GLAS-1, 4 Saaten).
3. **Umklappen:** Im Aufbau von TAKT-DYNAMIK-1 (Glas N = 128, A = 1e-3, Delaunay-Zuege): Wie gross ist der Energiesprung je Zug mit A2 statt A1?

## Ableitbarkeitsprobe (Leitung, Bausteine verkettet; Projektbefunde vor Literatur)

- **Vorab ableitbar [M]:**
  - **Gleichmaessige Verzerrung:** Bei gleichmaessiger Verzerrungsrate hat jedes Tetraeder dasselbe g-Punkt. Die volumengewichtete DeWitt-Bewegungsenergie ist dann auf jedem periodischen Netz exakt der Kontinuumswert (HM0, Kontrolle).
  - **Eich-Reduktion:** Bei einer Eichsymmetrie erster Klasse (Eckverschiebungen) sind die physikalischen Frequenzen nur mit der horizontalen Reduktion unabhaengig von der Eichflaeche [L].
  - **Skalare Regeln:** Sie sind zweiter Klasse; fuer sie gibt es keine Eichwahl, die Dirac-Klammer ist eindeutig.
- **Kette [ES, nicht bewiesen]:** Ist R1 nicht horizontal, ist ein Teil der gemeldeten TT-Spannen und der Leckage ein Reduktionsartefakt (passt zu TT-GLAS-2 und IMPULS-NETZ-1). Wie gross der Rest ist, ist nicht ableitbar.
- **Nicht ableitbar:**
  - die TT-Spanne mit horizontaler Reduktion (Rang-4-Isotropie ist durch keine bekannte Identitaet erzwungen)
  - die Stabilitaet
  - der Energiesprung mit A2. Bei nicht gleichmaessiger Verzerrung zerlegen 2 bzw. 3 Tetraeder die Bipyramide verschieden.
- **Erste Schreibtischaufgabe des Agenten:** Klaeren, ob R1 oder R2 schon horizontal ist. Wenn ja, sind Teile von HM1 und HM2 schon gerechnet und werden als Kontrolle gefuehrt; das wird vor dem Einfrieren in den Plan geschrieben.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| HM0 | Kontrolle, vorab ableitbar: Fuer gleichmaessige Verzerrungsraten ist die volumengewichtete DeWitt-Bewegungsenergie auf V, S, A15 und Glas gleich dem Kontinuumswert (auf 1e-12) | 90 % |
| HM1 | [H] Mit horizontaler Reduktion stimmen die TT-Frequenzen auf V fuer zwei verschiedene Eichflaechen auf 1e-10 ueberein; mit R1 weichen sie um mehr als 1e-4 ab | 50 % |
| HM2 | [H] Mit A2 und horizontaler Reduktion liegt die TT-Spanne auf V ohne Abstimmung unter 1e-3 (A2R1: 5,92 %) | 30 % |
| HM3 | [H] Auf Glas N = 128 halbiert A2 mit horizontaler Reduktion die TT-Spanne gegenueber A1R1 (15,3 %) mindestens | 45 % |
| HM4 | [H] Im TAKT-DYNAMIK-1-Aufbau faellt der Energiesprung je 2-3-Zug mit A2 unter 1e-4 von H0 (mit A1: 0,2 bis 0,5 %) | 45 % |

**Bedeutung (vorab):**
- **HM1 trifft ein:** Ein Teil der bisherigen TT-Spannen und Leckagen ist ein Rechenartefakt. Die Zahlen von TT-ISO-1, TT-GLAS-1/2, DEFEKT-NETZ-1 und IMPULS-NETZ-1 muessen dann mit horizontaler Reduktion neu bewertet werden. Das ginge als Berichtigung an Finn.
- **HM2 trifft ein:** Die Abstimmung der Kristallnetze haette einen Grund (Volumen statt Zahl der Zellen). GW170817 bliebe trotzdem nur mit exakter Isotropie erreichbar.
- **HM4 trifft ein:** Mit volumengewichteter Bewegungsenergie ist Umklappen ein energieerhaltender Taktschritt. Finns Mechanismus waere dann auch dynamisch vertraeglich.
- **Alle verfehlt:** Die Bewegungsenergie braucht eine andere Regel (L10).

## Rahmen

- Code-Agent. Code aus tt-iso-1/code, tt-glas-1/code, tt-glas-2/code, takt-dynamik-1/code und defekt-netz-1/code kopieren, dort nichts aendern.
- Abgrenzung: SKALAR-MISCH-1 laeuft gleichzeitig. Es sucht Gewichte je Tetraederart auf V gegen Bahnlagen-Gang und TT-Spanne und rechnet einen beschreibenden Punkt "Hodge-Masse". Diese Karte rechnet diese Gewichtssuche nicht nach; sie prueft Reduktion, A2 und Umklappen.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu8, cpu9 und cpu10, sonst cpu3 und cpu4. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256). Ein ehrlicher Teilbericht ist besser als keiner: zuerst Frage 1 (Reduktion), dann 2, dann 3.
- Synthetisch, keine Messdatenbestaetigung.
