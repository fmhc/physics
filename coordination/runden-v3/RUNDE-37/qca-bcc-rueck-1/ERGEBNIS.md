# QCA-BCC-RUECK-1: Ergebnis (Runde 38/39)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date):**
  - Start 2026-10-04 09:24:34 CEST; Literatur ab 09:29 (1 Abruf); Code bis 09:41:35; Plantext ab 09:43:25; Text dieser
    Datei ab 09:54:27 CEST.
  - Rauchlaeufe 07:41:39 bis 07:53:45 UTC (PLAN.md Abschnitt 7). Plan und Code eingefroren 09:50:59 CEST
    (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe auf der .69 ueber kleintest.sh, je ein ssh-Aufruf (UTC = CEST − 2 h):

    | Lauf | Spur | Inhalt | Aufruf bis Ende (UTC) | Rechenzeit |
    |---|---|---|---|---|
    | H-0 | cpu5 | Teil 0: QR0-Suche (40 Starts je Variante), Weyl-Referenz, Konstruktionen | 07:51:13 bis 07:52:26 | 12,7 s |
    | H-4N | p4000b | Teil 4, Form N, frei/r50/r20/r05, 40 Starts | 07:51:17 bis 07:55:34 | 109,3 s |
    | H-4O | cpu5 | Teil 4, Form O, frei/r50/r20/r05, 40 Starts | 07:52:27 bis 07:57:06 | 279,2 s |
    | H-8Oa | p4000b | Teil 8, Form O, frei, 12 Starts | 07:55:34 bis 08:04:31 | 187,1 s |
    | H-8Na | cpu5 | Teil 8, Form N, frei/r50, 12 Starts, maxit 600 | 07:57:06 bis 08:06:33 | 332,6 s |
    | H-8Nb | cpu5 | Teil 8, Form N, r20, 12 Starts, maxit 600 | 08:06:33 bis 08:14:05 | 82,5 s |
    | H-8Ob | p4000b | Teil 8, Form O, r50/r20, 12 Starts | 08:04:31 bis 08:18:09 | 333,3 s |
    | Auswertung | cpu5 | auswertung.py | 08:18:24 bis 08:19:12 | 0,2 s |
    | Bilder | p4000b | bild.py | 08:19:12 bis 08:23:24 | 9,2 s |

  - Alle rc = 0. Die Differenz zwischen Aufruf-Spanne und Rechenzeit ist Wartezeit am Lock (fremde Laeufe auf meinen
    Spuren, Selbstanzeige 6).

- **Kennzeichen:** [S] an der Quelle gelesen (D'Ariano/Erba/Perinotti 2017, arXiv:1708.00826v2, als Bild; Quelle 2014
  ueber die Lesungen in qca-tetra-1 und qca-gegenlesen); [L] Literatur aus dem Gedaechtnis; [L?] unsicher; [M] eigene
  Mathematik; [H] Hypothese; [R] im Rauchlauf gesehen.
- **Art des Ergebnisses:**
  - Synthetische Rechnung an selbst gebauten Modellen und am Literaturmodell, keine Messdatenbestaetigung.
  - QR0 war aus der Literatur ableitbar (Prop. 5c der Arbeit von 2017), QR2 am Schreibtisch bis auf die Isotropie bei
    |k| = 0,05 (Konstruktion R3). QR1 war offen; es stuetzt sich auf die Suche und einen Teilbeweis (R4).
  - Alle drei Ausgaenge waren in den Rauchlaeufen vor dem Einfrieren zu sehen (PLAN.md Abschnitt 7).

## Ergebnis zuerst

1. **Mit 4 Zustaenden: kein Automat mit Rueckspruengen unter der vollen Gruppe T [Suche; Teilbeweis M].**
   - 3200 Starts (alle zehn Darstellungsklassen, Formen N und O, frei und mit erzwungenem Rueck-Anteil 50, 20 und
     5 %): 353 gueltige Treffer, jeder springt nur in S_+ oder nur in S_− (116) oder gar nicht (237, nur Vor-Ort-Term).
   - Mit erzwungenen Rueckspruengen kein Treffer; das kleinste Minimum ist 1,16e−4 (bei 5 % Rueck-Anteil).
   - Bewiesen ist nur ein Teil: Die Trennung "S_+ wirkt auf eine Irrep, S_− auf die andere" ist unmoeglich (R4).
   - Deshalb QR1 eingetroffen.
2. **Mit 8 Zustaenden: ja, mit isotropen Weyl-Kegeln und 360 Grad = −1 [M, numerisch; Bau vorab, R3].**
   - Bauart (Konstruktion R3): ein Hin-Sektor (springt nur in S_+), ein Rueck-Sektor (nur S_−) und eine Muenze, die
     zwischen beiden umschaltet. Ein Teilchen kann so um h springen und danach um −h zurueck.
   - Die Suche fand 17 Automaten mit Rueckspruengen, alle in K4 = 2+2+2'+2', auch mit Vor-Ort-Term. Sie haben
     J_+ = J_− wie die Konstruktion, sind aber zum Teil allgemeiner (v bis 0,37, die Konstruktion hat bei K4 v ≤ 1/3
     [M, nachtraeglich, nicht gegengelesen]). Jeder hat bei k = 0 vier
     Weyl-Kegel (v = 0,007 bis 0,37), in erster Ordnung isotrop. 12 haben einen Kegel mit Streuung ≤ 1e−2 bei
     |k| = 0,05, der beste alle vier bei 2e−4 bis 2,1e−3.
   - 360 Grad wirken in allen als −1 (am Treffer selbst bestimmt). Masse gibt es ohne Inversion keine; an H, P und P'
     sitzen je vier weitere Kegel (Verdoppler).
   - Deshalb QR2 eingetroffen.
3. **Kontrolle:** Dieselbe Suche findet unter L_2 mit 2 Zustaenden die Weyl-Automaten der Quelle (20 von 40, Spektrum
   auf 5e−16, v = 1/√3). Erzwingt man 20 % Rueck-Anteil, findet sie nichts, wie Prop. 5c der Arbeit von 2017 verlangt.
   Deshalb QR0 eingetroffen.
4. **Kartenluecke:** Als reine Matrixbedingung erfuellt schon die direkte Summe zweier Einbahn-Automaten die
   Rueckspruung-Bedingung. Geurteilt habe ich je unzerlegbarem Block; nach Kartenwortlaut (Matrix) sind alle drei
   Urteile gleich.
5. **Literatur:** D'Ariano/Erba/Perinotti 2017 klassifizieren nur 2 Zustaende. Rueckspruenge gehoeren dort zur
   Definition, und Z_3 (also T) ist bei 2 Zustaenden ausgeschlossen. Zu 4 und 8 Zustaenden sagt die Arbeit nichts:
   QR1 und QR2 sind nicht aus ihr ableitbar, QR0 schon.

## Urteile (lauf-69/auswertung.json, Vorbedingungen erfuellt)

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil |
|---|---|---|---|
| QR0 | Kontrolle: Die Suche findet unter L_2 mit 2 Zustaenden den Weyl-Automaten der Quelle (mit Rueckspruengen) | 90 % | eingetroffen |
| QR1 | [H] Mit 4 Zustaenden gibt es unter T keinen nichttrivialen Automaten mit Rueckspruengen und Kegel | 55 % | eingetroffen |
| QR2 | [H] Mit 8 Zustaenden gibt es unter T einen nichttrivialen Automaten mit Rueckspruengen und isotropem Kegel, mit 360 Grad = −1 | 35 % | eingetroffen |

- **QR0:** r50: 20 Treffer von 40, alle Weyl (Abweichung ≤ 5,0e−16), J_+ = J_− = 1, v = 0,577350. Vermerk Variante
  frei: eingetroffen (21 Treffer). r20: 0 Treffer (Minimum 0,16514).
- **QR1:** 0 Gegenbeispiele. Vermerke: Matrix-Lesart (Kartenwortlaut) eingetroffen (0); nur Form N eingetroffen (0);
  ohne Gueltigkeitsschwelle 1e−20 eingetroffen (0). Rueck-Treffer ohne Kegel: 0.
- **QR2:** 12 Kandidaten (K4: N frei 6, N r50 1, O frei 2, O r50 3). Vermerke: Matrix-Lesart eingetroffen (12);
  Isotropie streng 1e−3 bei 0,05 eingetroffen (3); nur Form N eingetroffen (7); 360 Grad nur ueber die Darstellung
  eingetroffen (12); alle Kegel des Automaten isotrop eingetroffen (2); Konstruktionen aus Teil 0: 2 von 5 gemischten
  (K4 gemischt 2, K5 gemischt 1).
- **Woran die Urteile haengen:**
  - QR1 an der Suche: Bewiesen ist nur die Sektortrennung (R4). Ein Rueck-Automat mit 4 Zustaenden und gebrochenen
    Anteilen ist nicht ausgeschlossen, aber in 3200 Starts nicht aufgetaucht.
  - QR2 an meiner Isotropieschwelle 1e−2 bei 0,05 (geeicht an der Quelle). Mit 1e−3 bleiben 3 Kandidaten; der Ausgang
    aendert sich nicht.

## Literatur [S]

- **Abruf:** 1 von 3 (WebFetch auf arxiv.org/pdf/1708.00826, nur die PDF abgelegt, kein Text). Gelesen als Bild: alle
  7 Seiten. Kopie quelle/dariano-erba-perinotti-2017-arXiv-1708.00826.pdf (sha256 dc410794...7bb91c81).
- G. M. D'Ariano, M. Erba, P. Perinotti, "Isotropic quantum walks on lattices and the Weyl equation",
  arXiv:1708.00826v2 [quant-ph] (30. Nov. 2017), PRA 96, 062101 (2017).
- **Was die Arbeit beantwortet:**
  - Nur s = 2 (S. 1, Abstract: "with a coin system of dimension s = 2"; S. 4: "From now on we will restrict to s = 2").
  - Rueckspruenge sind Teil der Definition: S. 2 "we will assume A_h ≠ 0 for all h ∈ S_+ ∪ S_−"; S. 4 "By definition
    the transition matrices are nonnull".
  - Z_3 in der Isotropiegruppe ist bei s = 2 ausgeschlossen (S. 5: "The case K ≅ Z_3 is not consistent with Eqs.
    (17) and (18)"); fuer BCC ist "the only possible isotropy group ... U_L = {I, iσ_X, iσ_Y, iσ_Z}" (S. 6, Fig. 1).
  - Prop. 5c (S. 7): die zwei Weyl-Automaten, A_e = 0; S. 6: α_+² = α_−² = 1/4.
- **Was sie nicht beantwortet:** s = 4 und s = 8, die Gruppe T mit mehr Zustaenden, Blockzerlegung. QR1 und QR2 sind
  daraus nicht vorab ableitbar; QR0 schon. Andere Arbeiten dazu kenne ich nicht [L?].

## Schreibtisch [M] (PLAN.md Abschnitt 3)

- **R1:** Unter T haben alle A_h in S_+ dieselbe Norm a_+, alle in S_− dieselbe Norm a_−. Die Rueckspruung-Bedingung
  heisst dann a_+ > 0 und a_− > 0; das ist zugleich "alle acht A_h ≠ 0" (Arbeit von 2017).
- **R2 (Kartenluecke):** Die Bedingung als Matrixbedingung erfuellt schon eine direkte Summe aus einem Automaten, der nur
  in S_+ springt, und einem, der nur in S_− springt. Deshalb urteile ich je unzerlegbarem Block (Block-Lesart).
- **R3 (8 Zustaende, Konstruktion):** W(k) = X·(C_1 S_+(k) ⊕ C_2 S_−(k)), X eine Muenze, die beide Sektoren mischt. Sie
  ist unitaer, T-kovariant, hat J_+ = J_− = 4 und erfuellt die Block-Lesart. Bei k = 0 liegen Zweifach-Cluster auf den
  2T-Irreps 2, 2' (bzw. 2''); dort erzwingt T in erster Ordnung c k·σ (isotrop), 360 Grad = −1.
- **R4 (4 Zustaende, Teilbeweis):** Es bleiben nur 1+3 und 2+2' (D1, S2, gemischte Klassen zerfallen). Ausgeschlossen
  ist die Sektortrennung (S_+ wirkt nur auf eine Irrep, S_− nur auf die andere): Dann muessten acht orthonormale Vektoren
  in C^4 liegen. Nicht bewiesen ist der Fall mit gebrochenen Anteilen.
- **R5 (Kontrolle):** Unter L_2 mit s = 2 erzwingt Prop. 5c J_+ = J_− = 1; Variante r20 muss leer bleiben.

## Tabellen

### Teil 0: Kontrolle QR0 (L_2, Pauli, s = 2, Form N, 40 Starts je Variante)

| Variante | Treffer | Weyl (Spektrum) | J_+ / J_− | v bei k = 0 | Streuung bei 0,05 | Kleinster Defekt |
|---|---|---|---|---|---|---|
| frei | 21 | 21 (11 + 10 in den zwei Spektralklassen), Abw. ≤ 3,9e−16 | 1 / 1 | 0,577350 | 2,817e−3 | 9,5e−32 |
| r50 | 20 | 20 (6 + 14), Abw. ≤ 5,0e−16 | 1 / 1 | 0,577350 | 2,817e−3 | 1,2e−31 |
| r20 | 0 | | | | | 0,16514 (= 18/109) |

- Alle 41 Treffer: gueltig (voller Defekt ≤ 5,4e−31), unzerlegbar (Kommutant 1), alle acht Normen gleich (Verhaeltnis
  1,0), Wirkung am Treffer projektiv, Kegel auch an H, P, P' (Verdoppler wie in der Quelle).
- Weyl-Referenz A^± (Eq. 24 der Quelle 2014): Defekt 0, L_2-Kovarianz 0, Block-Lesart erfuellt, v = 0,577350, Streuung
  5,6e−7 bei |k| = 1e−5 und 2,817e−3 bei 0,05 (wie QCA-TETRA-1).
- r20 ohne Treffer, wie Prop. 5c verlangt (α_+² = α_−²).

### Teil 0: Konstruktion Muenze × (S_+ ⊕ S_−), 8 Zustaende (beschreibend, Vermerk zu QR2)

| Konstruktion | Kategorie | Kommutant | v der vier Kegel (je zweifach) | Streuung bei 0,05 | 360 Grad |
|---|---|---|---|---|---|
| K4 gemischt 0 | Rueck + Kegel | 1 | 0,2715 (2×), 0,0390 (2×) | 0,023 bis 0,24 | projektiv |
| K4 gemischt 1 | Rueck + Kegel | 1 | 0,2378 (2×), 0,0681 (2×) | 0,028 bis 0,155 | projektiv |
| K4 gemischt 2 | Rueck + Kegel, isotrop | 1 | 0,2477 (2×), 0,2185 (2×) | 0,0016 bis 0,0103 | projektiv |
| K4 direkte Summe (X = I) | Rueck nur Matrix | 2 (zwei Einbahn-Bloecke) | 1/3 (4×) | 0,0009 bis 0,033 | mehrdeutig |
| K5 gemischt 0 | Rueck + Kegel | 1 | 1/3 (4×) | 0,030 bis 0,046 | projektiv |
| K5 gemischt 1 | Rueck + Kegel, isotrop | 1 | 1/3 (4×) | 0,0035 bis 0,027 | projektiv |

- Alle unitaer (Defekt ≤ 2,7e−30) und T-kovariant (≤ 5,4e−16), J_+ = J_− = 4, C3 am Treffer implementierbar, keine
  Inversion. An H, P und P' liegen je vier lineare Zweifach-Cluster: 16 Weyl-Kegel in der Zone.
- Die direkte Summe zeigt die Kartenluecke (R2): Als Matrix sind alle acht Spruenge besetzt, jeder Block springt aber
  nur in eine Richtungsgruppe.
- Bei K5 bleibt v = 1/3 trotz Mischung; bei K4 sinkt v mit der Mischung (0,039 bis 0,27) [M, nachtraeglich, nicht
  gegengelesen: In der Konstruktion ist W(0)^†∂W = ∂S_+(0) ⊕ ∂S_−(0), unabhaengig von X und C; auf einem Cluster mit Anteilen
  |a|², |b|² in den beiden Sektoren gilt c = (|a|² c_+ + |b|² c_−). Im K5-Bau haben die beiden 2-Kopien gleiches c,
  im K4-Bau entgegengesetztes, also v = |(|a|² − |b|²)|/3 ≤ 1/3]. Die Suchtreffer erreichen v = 0,37 und sind deshalb
  nicht alle von dieser Bauart.

### Teil 4: 4 Zustaende, volle Gruppe T (40 Starts je Fall, Form, Variante)

Form N (acht Spruenge):

| Fall | dim | frei: Treffer | r50: kleinster Defekt | r20 | r05 |
|---|---|---|---|---|---|
| fuenf eindimensionale Summen | 12 bis 32 | 0 (12/7) | 12/7 | 1,72339 | 1,72727 (= 19/11) |
| T:1+3 | 12 | 19, alle einseitig | 0,088889 (4/45) | 0,0084581 | 1,1607e−4 |
| T:1'+3 | 12 | 22, alle einseitig | 0,088889 | 0,0084581 | 1,1607e−4 |
| T:2+2 | 16 | 0 (4/45) | 4/45 | 0,49893 | 0,90096 |
| T:2+2' | 12 | 17, alle einseitig | 0,0015294 | 0,0084581 | 1,1607e−4 |
| T:2+2'' | 12 | 14, alle einseitig | 0,0015294 | 0,0084581 | 1,1607e−4 |

Form O (dazu Vor-Ort-Term; bei r50, r20, r05 zusaetzlich J_+ + J_− = 2):

| Fall | dim | frei: Treffer | r50: kleinster Defekt | r20 | r05 |
|---|---|---|---|---|---|
| fuenf eindimensionale Summen | 18 bis 48 | 34 bis 39, alle trivial | 0,632 bis 0,672 | 0,816 bis 0,826 | 0,92794 |
| T:1+3 | 14 | 26 (10 trivial, 16 einseitig) | 0,13187 | 0,31861 | 0,53536 |
| T:1'+3 | 14 | 18 (5 trivial, 13 einseitig) | 0,13187 | 0,31861 | 0,53536 |
| T:2+2 | 20 | 21, alle trivial | 0,022599 | 0,21728 | 0,41822 |
| T:2+2' | 14 | 16 (8 trivial, 8 einseitig) | 0,041787 | 0,21728 | 0,41822 |
| T:2+2'' | 14 | 17 (10 trivial, 7 einseitig) | 0,041787 | 0,21728 | 0,41822 |

- 3200 Starts, 353 Treffer, alle gueltig (voller Defekt ≤ 9,7e−29), **kein einziger mit Rueckspruengen**: 116
  einseitig (J_+, J_−) = (4, 0) oder (0, 4), die Gegenrichtung hoechstens 2,1e−6 der groessten Norm; 237 trivial (nur
  Vor-Ort-Term, J = 0).
- Mit fester Rueckspruung-Bedingung gibt es keinen Treffer; die Minima sind in allen 60 Faellen mit Bedingung ≥ 1,16e−4
  und gleich fuer die gleichwertigen Darstellungen (1'+3 wie 1+3, 2+2'' wie 2+2', auf 6 bis 15 Stellen).
- Fuer kleine erzwungene Anteile w sinkt das Minimum (Form N: 0,0085 bei w = 0,2, 1,2e−4 bei w = 0,05, fuer 1+3 und
  2+2' gleich): Der Defekt geht gegen 0, wenn die Gegenrichtung verschwindet. Das ist der einseitige Automat mit kleiner
  Beimischung, keine versteckte Loesung [H, aus dem Verlauf]. Bei 2+2' gibt es bei w = 0,5 ein eigenes, kleineres
  lokales Minimum 0,0015294 (nicht monoton in w).
- Rauchlauf 2 (25 Starts) gab dieselben Minima: bei 2+2' und bei r20, r05 auf 12 bis 15 Stellen, bei 1+3 r50 auf 6
  Stellen (langsame Konvergenz gegen 4/45).

### Teil 8: 8 Zustaende, volle Gruppe T (12 Starts je Fall, Form, Variante; Form N mit maxit 600)

Treffer (Kategorien) bzw. kleinster Defekt; "Rueck" = Block-Lesart erfuellt; "iso" = isotroper Kegel mit Spin −1,
am Treffer projektiv (QR2-Kandidat).

| Fall | dim N/O | N frei | N r50 | N r20 | O frei | O r50 | O r20 |
|---|---|---|---|---|---|---|---|
| K1 = 2+2+2+2 | 64/80 | 0 (8/45) | 0 (8/45) | 0 (1,139) | 3 trivial | 0 (0,0453) | 0 (0,553) |
| K2 = 2+2+2+2' | 52/62 | 0 (4/45) | 0 (0,0904) | 0 (0,1286) | 2 einseitig, 2 trivial | 0 (0,0589) | 0 (0,00826) |
| K3 = 2+2+2+2'' | 52/62 | 0 (4/45) | 0 (0,0904) | 0 (0,1286) | 2 einseitig, 1 trivial | 0 (0,00153) | 0 (0,00826) |
| K4 = 2+2+2'+2' | 48/56 | **7 Rueck (6 iso)** | **2 Rueck (1 iso)** | 0 (0,0172) | **3 Rueck (2 iso)** | **5 Rueck (3 iso)** | 0 (0,00826) |
| K5 = 2+2+2'+2'' | 44/50 | 2 einseitig | 0 (0,00199) | 0 (2,1e−4) | 2 trivial | 0 (0,00153) | 0 (0,00826) |

- **17 Rueck-Treffer, alle in K4**, alle gueltig (voller Defekt ≤ 8,0e−23), unzerlegbar (Kommutant 1), alle acht
  Spruenge gleich stark besetzt, J_+ = J_− (Abweichung ≤ 4,1e−9): Form N J_± = 4; Form O frei J_± = 4; 3,80 und 0,107
  (Vor-Ort-Gewicht 0 bis 7,79); Form O r50 J_± = 2.
- **Kegel:** Jeder Rueck-Treffer hat bei k = 0 vier Zweifach-Cluster, alle linear (Weyl-Kegel), Geschwindigkeiten
  0,0070 bis 0,3696; in erster Ordnung isotrop (Streuung bei |k| = 1e−5 ≤ 3,9e−4). Die Chiralitaeten der vier Kegel
  heben sich auf (Summe ≤ 2,9e−5). Keine Masse: kein Treffer mit Luecke ohne lineare Aufspaltung.
- **Isotropie bei |k| = 0,05:** 2,5e−4 bis 0,39 je Kegel. 12 der 17 Rueck-Treffer haben mindestens einen Kegel mit
  Streuung ≤ 1e−2 (QR2-Kandidaten), 2 davon alle vier Kegel, 3 mindestens einen ≤ 1e−3. Bester Treffer (K4, N, frei):
  v = 0,3696 und 0,3553 (je zweimal), Streuung 2e−4 bis 2,1e−3.
- **360 Grad:** In allen Rueck-Treffern am Treffer projektiv (C2x, C2y eindeutig, K = −I), C3 implementierbar, keine
  Inversion; in jedem Kegel-Cluster P V(C2x)² P = −P usw.
- **Verdoppler:** An H, P und P' liegen in jedem Rueck-Treffer je vier lineare Zweifach-Cluster.
- **Homogenitaet Eq. (2) der Arbeit von 2017:** In den Rueck-Treffern ist ||A_h − A_h'|| ≥ √2·||A|| (kleinster Wert
  1,41421) fuer alle Paare einer Richtungsgruppe; verschiedene Richtungen haben verschiedene Matrizen, Eq. (2) ist
  erfuellt.
- **K5:** Die Suche fand keinen Rueck-Treffer; Nicht-Treffer endeten bis 5,0e−7 (langsame Konvergenz wie in
  QCA-DIRAC-T-1). Die Konstruktion zeigt, dass es K5-Automaten mit Rueckspruengen gibt (Teil 0).
- **r20 (J_+ : J_− = 1 : 4):** in keinem Fall ein Treffer, auch nicht in K4 (Minimum 0,0172 bzw. 0,00826).

## Schreibtisch gegen Rechnung

- **R1:** In jedem Treffer haben alle vier A_h in S_+ dieselbe Norm, ebenso in S_−; Rueck-Treffer haben alle acht
  gleich stark (Normverhaeltnis 1,0).
- **R2:** Die direkte Summe (X = I) ist als Matrix "besetzt", zerfaellt aber in zwei Einbahn-Bloecke der Dimension 4
  (Kommutant 2, Wirkung am Treffer mehrdeutig).
- **R3:** Alle fuenf gemischten Konstruktionen sind unitaer, T-kovariant, unzerlegbar und erfuellen die Block-Lesart;
  ihre Kegel sind in erster Ordnung isotrop (Streuung bei |k| = 1e−5 ≤ 5,3e−5), ausser "K4 gemischt 1" mit 3,1e−3.
  Dort liegen zwei Cluster bei k = 0 nur 0,0034 auseinander (gemessen); die Kopplung zwischen ihnen, relativ etwa
  v|k|/Abstand ≈ 7e−4, ist die naheliegende Ursache [H]. Die Suche findet dieselbe Art Automat selbst (K4, Form N und O).
- **R4:** Bei 4 Zustaenden kein Treffer mit Rueckspruengen; alle einseitigen Treffer haben (J_+, J_−) = (4, 0) oder
  (0, 4), keinen Zwischenwert. Das ist mehr, als R4 beweist (R4 schliesst nur die Sektortrennung aus).
- **R5:** L_2 mit r20 leer (Minimum 18/109), mit r50 nur Weyl.
- **D1, S2 (Vorgaenger):** eindimensionale Summen und T:2+2 ohne nichttriviale Treffer, mit und ohne Vor-Ort-Term;
  K1 (2+2+2+2) ebenso.
- **Nachtraeglich [H]:** Alle Rueck-Treffer haben J_+ = J_−, auch mit Vor-Ort-Term (dort J_± bis hinab zu 0,107).
  Unter L_2 erzwingt das Prop. 5c; unter T habe ich es nicht bewiesen.

## Kontrollen

- **Positivkontrolle QR0:** derselbe Suchcode (Nebenbedingung r50) findet unter L_2 die Weyl-Automaten der Quelle,
  20 von 40 Starts, beide Spektralklassen, Spektrum auf 5e−16.
- **Gegenprobe Blockzerlegung:** direkte Summe "nur Matrix", gemischte Konstruktionen unzerlegbar.
- **Gleichwertige Darstellungen:** 1'+3 und 1+3, 2+2'' und 2+2' mit denselben Minima (6 bis 15 Stellen) und denselben
  Trefferarten; K3 und K2 mit denselben Minima in Form N (4/45 frei, 0,090418 bei r50).
- **Codepruefung je Lauf:** Bahn-Defekt gegen vollen Defekt ≤ 3e−16 relativ, J_+ aus der Gram-Matrix ≤ 2,1e−16,
  Jacobi-Matrix gegen Differenzenquotient ≤ 1,5e−7.
- **Gruppen und Darstellungen:** T 12, 2T 24, Kern ±I; alle 16 Darstellungen unitaer und projektiv geschlossen
  (≤ 1e−15), Kommutator −I genau bei den projektiven, +I bei den linearen.
- **Trefferabstand:** gueltige Treffer ≤ 8,0e−23 (voller Defekt, die meisten ≤ 1e−28), Nicht-Treffer ≥ 5,0e−7 (K5 frei, langsame Konvergenz), mit erzwungenen Rueckspruengen bei 4 Zustaenden ≥ 1,16e−4.

## Kartenberichtigungen und Festlegungen (vor dem Einfrieren, PLAN.md Abschnitt 1)

1. **Matrix- gegen Block-Lesart (Kartenluecke):** Die woertliche Bedingung (A_h ≠ 0 ⇒ A_−h ≠ 0 als Matrizen) erfuellt
   schon die direkte Summe zweier Einbahn-Automaten (Konstruktion "K4 direkte Summe"). Haupturteil je unzerlegbarem
   Block; die Matrix-Lesart (Kartenwortlaut) steht bei QR1 und QR2 als Vermerk.
2. **Mindestnorm** 1e−3 der Frobenius-Norm relativ zur groessten (im Block: der komprimierten Matrizen). Gemessen: Die
   Gegenrichtung einseitiger Treffer liegt bei ≤ 2,1e−6 (s = 4) bzw. ≤ 1,5e−6 (s = 8), Rueck-Treffer bei 1 (alle acht
   gleich stark).
3. **Gueltig** heisst voller Defekt nach der Nachpolitur ≤ 1e−20 (Treffer: < 1e−10 wie auf der Karte). Gemessen haben
   alle 425 Treffer ≤ 8,0e−23; die Schwelle hat nichts aussortiert.
4. **Nebenbedingung** als feste Anteile w = 0,5; 0,2; 0,05 plus Variante frei; Form O mit J_+ + J_− = s/2.
5. **Formen** N und O; die Eichung W(0) = I (Eq. 9) nicht gerechnet, weil sie die Normen der A_h nicht aendert.
6. **Kegel** bei k = 0 (lineare Aufspaltung in allen 126 Richtungen und echte Kopplung).
7. **Isotropie:** Streuung ≤ 1e−3 bei |k| = 1e−5 und ≤ 1e−2 bei 0,05 (geeicht am Weyl-Automaten der Quelle, 2,8e−3);
   Vermerk streng 1e−3.
8. **360 Grad** am Treffer (implementierende Unitaere, K = −I) und im Kegel-Cluster ueber die 2T-Lifts.
9. **Darstellungen:** Dimension 4 vollstaendig gerechnet (ausser den gemischten, die nach R4 zerfallen); Dimension 8
   die fuenf Spinorklassen; gemischte am Schreibtisch auf s = 4 und s = 2 zurueckgefuehrt; die 24 rein linearen
   8-dim Klassen nicht gerechnet (koennen 360 Grad = −1 nicht tragen).
10. **Urteil nach Kartenwortlaut** = Matrix-Lesart: QR0 eingetroffen (bei 2 Zustaenden fallen beide Lesarten zusammen), QR1
    eingetroffen (kein 4-Zustands-Treffer ist auch nur als Matrix beidseitig besetzt), QR2 eingetroffen (12 Kandidaten).

## Latten (v3)

- **L1 kann scheitern:** teilweise.
  - QR1 war offen: Ein einziger gueltiger 4-Zustands-Treffer mit Rueckspruengen und Kegel haette es gekippt (3200
    Starts, vier Varianten, zwei Formen), ebenso den Teilbeweis R4.
  - QR0 (Literatur) und QR2 (Konstruktion) konnten nur am Code, an der Konstruktion (Unitaritaet, Kovarianz) und an der
    Isotropie bei 0,05 scheitern; die letzte war offen.
- **L2 Gegenprobe:**
  - direkte Summe (X = I): Matrix-Lesart erfuellt, Block-Lesart nicht; die Blockzerlegung trennt also, was sie soll
  - L_2 mit r20: keine Loesung, wie Prop. 5c verlangt
  - gleichwertige Darstellungen (1'+3 gegen 1+3, 2+2'' gegen 2+2', K3 gegen K2) mit gleichen Minima bzw. Klassen
  - Weyl-Referenz der Quelle (Streuung 2,817e−3) als Eichung der Isotropie
  - Konstruktion gegen Suche in K4 und K5
- **L3 Numerik:** Treffer ≤ 8,0e−23 (421 von 425 ≤ 1e−28) gegen Nicht-Treffer ≥ 5,0e−7; Weyl-Spektrum auf 5e−16;
  Gegenrichtung einseitiger Treffer ≤ 2,1e−6 gegen Normverhaeltnis 1 bei Rueck-Treffern; J_+ − J_− ≤ 4,1e−9;
  Codepruefung ≤ 3e−16 (Defekt), ≤ 1,5e−7 (Jacobi).
- **L4 schon bekannt:**
  - Klassifikation fuer s = 2, Rueckspruenge als Definition, Ausschluss von Z_3 bei s = 2, Weyl-Automaten [S, 2017].
  - Dirac-Automat als Kopplung zweier Weyl-Automaten [S, Quelle 2014, Lesung QCA-DIRAC-T-1].
  - Muenze mal Verschiebung (Grover-, Hadamard-Laeufe) ist Standard der Quantenlauf-Literatur [L].
  - Ob T-kovariante BCC-Automaten mit 8 Zustaenden und Rueckspruengen oder ein Ausschluss fuer 4 Zustaende
    veroeffentlicht sind, weiss ich nicht [L?].
- **L5 Messbezug:** keiner.
  - Die Richtungsabhaengigkeit der Geschwindigkeit bei endlichem k waere bei Planck-Maschenweite unmessbar klein
    [H, nicht geprueft].
  - Die Verdoppler (16 Weyl-Kegel in der Zone bei den Konstruktionen) waeren fuer jede physikalische Lesart ein Problem:
    zusaetzliche masselose Sorten.

## Bedeutung fuer Finns Bild

- **Belegt im Modell [M, numerisch; QR1 nur durch Suche und Teilbeweis]:**
  - Auf BCC mit voller Tetraeder-Drehgruppe T und Rueckspruengen (jede Richtung auch rueckwaerts, wie die Quelle es
    verlangt) gibt es mit 4 inneren Zustaenden keinen Automaten; jede 4-Zustands-Loesung springt nur in S_+ oder nur in
    S_−. Der Befund A4 des Gegenlesers ist damit keine Luecke der damaligen Suche, sondern (soweit gesucht) die Regel.
  - Mit 8 Zustaenden geht es: Ein Hin-Sektor (S_+), ein Rueck-Sektor (S_−) und eine Muenze, die zwischen ihnen
    umschaltet. Das Teilchen hat bei k = 0 Weyl-Kegel mit Spin-1/2-Verhalten (360 Grad = −1), in erster Ordnung exakt
    isotrop, bei |k| = 0,05 je nach Muenze bis auf 2e−4 isotrop.
  - Das passt zur Bedeutung, die die Karte fuer "QR1 und QR2 treffen ein" vorab notiert hat: Fuer die volle Tetraeder-
    Symmetrie mit Rueckspruengen braucht ein Fermion (im Modell) 8 innere Zustaende, viermal so viel wie der
    Weyl-Automat der Quelle unter der kleinen Gruppe L_2.
  - Die 4-Zustands-Aussage "BCC als Fermionen-Netz mit voller Tetraeder-Symmetrie" aus QCA-DIAMANT-4 laesst sich mit
    Rueckspruengen nicht retten (der Fall "QR1 verfehlt durch einen Treffer" der Karte trat nicht ein); mit 8 Zustaenden
    gilt eine entsprechende Aussage.
- **Nicht gezeigt:**
  - dass 4 Zustaende nie reichen (nur Teilbeweis R4 plus Suche)
  - Masse: Ohne Inversion fand die Suche nur Kegel, keine Luecke (wie QCA-DIRAC-T-1 S4)
  - Verdoppler: Jeder nichttriviale 8-Zustands-Treffer hat auch an H, P und P' je vier Weyl-Kegel
  - Wechselwirkung, Messbezug
- **Vorschlag [H, nicht gerechnet]:** pruefen, ob unter T mit Rueckspruengen J_+ = J_− erzwungen ist (alle Rueck-Treffer
  haben es, auch mit Vor-Ort-Term), und ob die Rueck-Treffer mit Inversion (wie Form P in QCA-DIRAC-T-1) eine
  isotrope Masse tragen.

## Selbstanzeigen

1. **Ausgaenge vor dem Einfrieren gesehen.** Rauchlauf 1 und 2 zeigten QR0, QR1 und QR2 so, wie sie ausgingen
   (PLAN.md Abschnitt 7). QR0 und QR2 waren ausserdem am Schreibtisch ableitbar.
2. **Vor dem Plan gelesen:** die Gewichte S_+/S_− der Treffer aus qca-dirac-t-1/lauf-69 (jq). Sie haben die
   Konstruktion R3 angeregt.
3. **Festlegungen mit Wirkung auf die Urteile:** Block-Lesart als Haupturteil (Kartenwortlaut als Vermerk), Isotropie-
   schwelle 1e−2 bei 0,05 (geeicht an der Quelle), Gueltigkeit 1e−20. Die Schwellen standen im Code vor Rauchlauf 1
   (qca_rueck.py unveraendert seit dem scp um 09:41:35, sha256 a42239a2...).
4. **Nach den Rauchlaeufen geaendert (vor dem Einfrieren):** auswertung.py rechnet die Urteile auch bei verletzten
   Vorbedingungen (nur Diagnose) und hat den Vermerk "alle Kegel isotrop". Keine Schwelle, keine Regel.
5. **Teilbeweis, nicht gegengelesen:** R4 (Sektortrennung bei 4 Zustaenden unmoeglich) ist meine eigene Herleitung;
   kein frischer Leser hat sie geprueft. Der allgemeine 4-Zustands-Fall ist nicht bewiesen.
6. **Fremde Laeufe auf meinen Spuren:** Ein anderer Agent (runde39-spin-zufall) hat cpu5 und p4000b zwischen meinen
   Laeufen belegt; meine Laeufe warteten am Lock (bis etwa 8 min je Lauf). Keine fremden Prozesse angefasst.
7. **Teil 8 mit nur 12 Starts je Fall** (Zeitbox; QCA-DIRAC-T-1 hatte 40). In K5 fand die Suche keinen Rueck-Treffer,
   obwohl es welche gibt (Konstruktion). Die Suche ist dort also unvollstaendig; QR2 haengt nicht daran (K4).
8. **Nicht gerechnet:** die 24 rein linearen 8-dim Darstellungsklassen (koennen 360 Grad = −1 nicht tragen) und die
   gemischten Klassen (nur Schreibtisch, PLAN.md 1.10). Die Variante W(0) = I (Eichung) nicht gerechnet.
9. **Literatur:** Fundstellen nur aus den selbst gelesenen Seitenbildern; das Abrufwerkzeug lieferte keinen Text.
   1 von 3 Abrufen.
10. **Werkzeuge:**
    - Lokal: jq, ssh, scp, sha256sum, date, grep, sed, dazu mkdir, cp, ls, cat, tail, cut, wc und Warteschleifen
      "until grep ...; do sleep 5; done" (teils im Hintergrund), einmal "sleep 20" im Vordergrund; ein "sleep 25" lehnte
      das Werkzeug ab. Kein Interpreter lokal.
    - Auf der .69 ausserhalb des Starters: mkdir, ls, mv (atomarer Austausch von auswertung.py vor dem Einfrieren),
      sha256sum, cat (kleintest.sh), uptime, lesend systemctl --user list-units und ps (Lock-Halter). Kein Python
      ausserhalb des Starters.
11. **Laufbuchhaltung:** Nach dem Einfrieren keine Aenderung an Plan, Code oder Regeln; jeder Hauptlauf einmal, rc = 0.
    Je ssh-Aufruf ein Starteraufruf; die Folge je Spur lief als lokale Kette getrennter ssh-Aufrufe, nichts davon im
    Hintergrund auf der .69. Hoechstens zwei meiner Laeufe zugleich, nur cpu5 und p4000b. Der Rauchlauf 3 (bild.py)
    lief erst nach dem Einfrieren zu Ende (07:53:45 UTC, rc = 0) und hat nichts mehr veraendert.
12. **Gegenlesen dieser Datei (beide Richtungen, gegen die JSON-Dateien):** acht Stellen berichtigt: "40 Faelle" statt
    60 mit Bedingung; "5 bis 7 Stellen" statt 6 bis 15 (zweimal); Streuung "bis 0,15" statt 0,155; eine falsche
    Monotonie in w; "13 Stellen" fuer Rauchlauf 2 (bei 1+3 nur 6); "alle Suchtreffer sind Muenze mal Verschiebung"
    (v bis 0,37 widerspricht); "= √2 fuer alle Paare" statt ≥ √2; die Gegenrichtung einseitiger Treffer bei s = 8 fehlte.
    Die Urteile sind nicht betroffen.
13. **Bild:** In omega_treffer.png ist je Darstellung der beste Treffer gezeigt; bei vielen Faellen ist das ein
    trivialer oder einseitiger Treffer, und nur ein K4-Rueck-Treffer ist abgebildet (nur Darstellung).
14. **Zeitbox:** 120 min ab 09:24:34 CEST; Text abgeschlossen um 10:24:18 CEST (date).

## Dateien

- **Plan:** PLAN.md und PLAN.md.eingefroren-20261004-095059; Pruefsummen in EINGEFROREN-SHA256.txt.
- **Quelle:** quelle/dariano-erba-perinotti-2017-arXiv-1708.00826.pdf.
- **Code:** code/qca_rueck.py, code/auswertung.py, code/bild.py, je mit .eingefroren-20261004-095059.
- **Rauchlaeufe:** rauch-69/ (rauch1, rauch2: json, log; rauch3: auswertung, Bilder).
- **Hauptlaeufe:** lauf-69/haupt_{0,4N,4O,8Na,8Nb,8Oa,8Ob}.json/.log, auswertung.json/.log, bild.log,
  treffer_je_fall.png, omega_treffer.png, PRUEFSUMMEN.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/runde39-qca-rueck/ (code/, rauch/, lauf/).

## Einfach gesagt

Wir wollten wissen, ob eine Quanten-Spielregel auf dem Netz mit acht Tetraederrichtungen je Knoten alle Drehungen des
Tetraeders respektieren kann, wenn jeder Sprung auch rueckwaerts moeglich sein muss, und ob sie dann Teilchen mit
halbem Spin traegt. Mit vier inneren Zustaenden je Knoten fanden wir in 3200 Versuchen keine einzige solche Regel:
Jede Loesung springt nur in eine der beiden Richtungsgruppen, wie eine Einbahnstrasse. Mit acht Zustaenden geht es,
indem man einen Hin-Teil und einen Rueck-Teil durch eine Art Muenzwurf verbindet; dann entstehen Teilchen mit halbem
Spin (nach einer vollen Drehung tragen sie ein Minuszeichen), die bei kleinen Impulsen in alle Richtungen fast gleich
schnell laufen, aber keine Masse haben. Die volle Tetraeder-Symmetrie mit Rueckspruengen kostet also viermal so viele
innere Zustaende wie die kleine Symmetrie der Quelle; das ist eine Rechnung an einem Modell, keine Messung, und dass
vier Zustaende nie reichen, ist nur teilweise bewiesen.
