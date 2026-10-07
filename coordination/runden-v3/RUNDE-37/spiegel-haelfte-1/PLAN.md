# SPIEGEL-HAELFTE-1: Plan (Runde 42)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date):** Start 2026-10-04 17:35:36 CEST; Code ab etwa 17:50; Plantext ab 17:57:24 CEST.
- **Kennzeichen:** [M] eigene Mathematik; [E] Messung im Modell; [P] Projektdatei; [S] Quelle (FJ = Foster/Jacobson,
  arXiv:1610.01142, lokale Kopie dunkel-flip-l/quellen/F11-FosterJacobson-1610.01142.txt, Zeilen dieser Kopie);
  [H] Hypothese; [R] im Rauchlauf gesehen.
- **Art:** Synthetische Rechnung an einem selbst gebauten Modell. Keine Messdaten.
- **Vorhersagen und Wahrscheinlichkeiten:** aus der Karte, unveraendert (SH0 75 %, SH1 45 %, SH2 60 %).

## 1. Teil A: Schreibtischpruefung der Herleitung (vor jeder Rechnung)

Geprueft: DOSSIER 6.2 und ARBEITSFELD 9 ("FJ = Kompression der Einbahn-Regel W = C S_+ auf Komponente 2").
Bezeichnungen: Verschiebungsbasis |a⟩, a = 1..4; Komponente a springt um h_a (Tetraeder-Satz T+ des BCC);
n_a = h_a/|h_a|; P_a = |n_a⟩⟨n_a| = (1 + n_a·σ)/2; V = (1/√2) Σ_a |n_a⟩⟨a| : C^4 → C^2.

| Schritt | Aussage im Dossier | Pruefung | Ausgang |
|---|---|---|---|
| A1 | V V^† = 1 | (1/2) Σ_a P_a = 1, weil Σ_a n_a = 0; steht so bei FJ ("Note in particular that (1/2) Σ_i P_i = I", [S] Z. 212-213) | haelt [M] |
| A2 | V^†V ist ein Rang-2-Projektor mit Diagonale 1/2 und Nebenbetrag² 1/12 | folgt aus A1; ⟨a|V^†V|b⟩ = (1/2)⟨n_a|n_b⟩, Betrag² (1/4)(1 + n_a·n_b)/2 = 1/12 | haelt [M] |
| A3 | "genau die Matrixelemente von P_2" → V^†V = P_2 | **Luecke.** Die Betraege legen den Projektor nicht fest: P_2' = 1 − P_2 hat dieselben Betraege (Diagonale 1/2, Nebenelemente −⟨a|P_2|b⟩), ebenso das komplex Konjugierte. Eichinvariant sind die Bargmann-Produkte ⟨a|P|b⟩⟨b|P|c⟩⟨c|P|a⟩. Fuer die FJ-Spinoren gilt Tr(P_a P_b P_c) = (i/4) n_a·(n_b × n_c) = ±i/(3√3), mit V^†V also ±i/(24√3); das Vorzeichen ist die Haendigkeit des Tetraeders und kippt bei n → −n (P-quer = (1 − n·σ)/2). Richtig ist: V^†V ist bis auf eine diagonale Phaseneichung D (vertauscht mit S_+, also dieselbe Regel) entweder P_2 oder P_2'. Welche Haelfte die FJ-Haendigkeit "Spin parallel zum Schritt" traegt, haengt an der Darstellung (2+2' oder 2+2'') und an der Richtungskonvention; der Projektcode von QCA-DIAMANT-4 arbeitet nur im k-Raum und legt die Realraum-Richtung nicht fest [P] | berichtigt: Die Kompression auf **jede** Haelfte ist ein FJ-Schachbrett, auf der einen mit P_a, auf der anderen mit P-quer_a (FJ: "To treat left-handed Weyl spinors we need only replace the spin projections P_i by the orthogonal projections", [S] Z. 405-406). Zahlenpruefung an der Projekt-Loesung im Rauchlauf R1 |
| A4 | V S_+(k) V^† = (1/2) Σ_a e^{ik·h_a} P_a = FJ Gl. (15) | direkt: V diag(z_a) V^† = Σ_a z_a (1/2)|n_a⟩⟨n_a|; unabhaengig von der Phasenwahl der Spinoren (P_a ist phasenfrei; FJ: "The amplitude matrix (18) is independent of the choice of phases", [S] Z. 365). Eine andere Phasenwahl ist die Eichung D = diag(e^{iδ_a}); die Haendigkeit ist durch keine Phasenwahl zu aendern ([S] Z. 409-412) | haelt [M] |
| A5 | P_2 W P_2 = e^{iα} V^† A V; FJ iteriert die Kompression, 2' wirkt als vollkommene Senke | P_2 C = e^{iα} P_2 (Muenze im Kommutanten); (P_2 W P_2)^t = e^{iαt} V^† A^t V. Realraum: Ψ_t = e^{−iαt} V φ_t mit φ_{t+1} = e^{iα} P_2 S_+ φ_t erfuellt FJ Gl. (11) Ψ(x) = (1/2) Σ_a P_a Ψ(x − h_a) exakt (V P_2 = V, v_a^† V = (V^†V)_{a·}) | haelt [M]; FJ ist nicht P_2 W^t P_2 (die unitaere Regel gibt zurueck) |
| A6 | Vereinigung der vier zeitversetzten FCC-Gitter von FJ = BCC, Schritte = T+-Satz | Nebenklassen des FCC-Untergitters {2Z³, Summe ≡ 0 mod 4} im BCC: 0, t_1, 2t_1 ≡ (0,0,2), 3t_1; Index 4; je Schritt ein Nebenklassenwechsel. Unter S_+ zerfaellt das BCC-Gitter in vier entkoppelte Familien; jede ist das FJ-Raumzeitgitter | haelt [M] |

**Zusaetze aus der Pruefung (neu, [M], nicht gegengelesen):**

- **A7 Verdoppler an H, P, P' sind die vier Familien.** An k_H = (π,0,0), k_P = (π/2)(1,1,1), k_P' = −k_P
  (ganzzahlige Koordinaten) ist e^{ik·t_a} fuer alle a gleich (−1, −i, +i). Also W(k_X + q) = λ_X W(q): Die Kegel an
  H, P, P' aus QCA-DIAMANT-4 Teil B [P] sind die k = 0-Kegel, um π, 3π/2, π/2 in der Eigenphase gedreht. FJ hat dieselbe
  Vierfach-Symmetrie ("θj → θj + π/2 ... just multiplies the eigenvalue by e^{iπ/2}", [S] Z. 297-300) und identifiziert
  diese Punkte im Raumzeitgitter mit k = 0. **Der Unterschied FJ gegen Einbahn-Regel liegt deshalb nicht bei H, P, P',
  sondern beim Partner in 2' (bei k = 0, Eigenphase β) und bei der Unitaritaet.** Das berichtigt die Zeile "FJ gegen
  unitaere Einbahn-Regel" in DOSSIER Abschnitt 8 teilweise. Innerhalb einer Familie hat W = C S_+ genau zwei Kegel,
  beide bei k = 0 (auf 2 bei α, auf 2' bei β, entgegengesetzte Haendigkeit).
- **A8 Mittelwert ueber die Unordnung bei W = 2π ist exakt FJ.** Entwickelt man jeden Schritt nach
  C_x = e^{iα}P_2 + e^{iβ_x}P_2', traegt jeder Term mit mindestens einem 2'-Schritt ein Produkt Π_x e^{i m_x β_x} mit
  m_x ≥ 1 an mindestens einem Knoten (auch bei Wiederbesuchen, die alle 4 Schritte moeglich sind). Fuer β_x gleichverteilt
  auf dem ganzen Kreis ist ⟨e^{imβ}⟩ = 0 fuer m ≥ 1. Also ⟨ψ(t)⟩ = e^{iαt} (P_2 S_+)^t ψ_0 = FJ, und
  ⟨w_2⟩ = N_FJ + ⟨|δψ_2|²⟩ ≥ N_FJ. **SH1 prueft damit genau, ob der inkohaerente Anteil aus 2' nach 2 zurueckkommt.**
- **A9 Schreibtisch-Erwartung, heuristisch ([M] fuer die Einzelschritte, [H] fuer das Ratenbild):** Die Zufallsphasen
  machen die nach 2' abgeflossene Amplitude weiss (in k gleichverteilt). Fuer eine weisse 2'-Amplitude gilt im Mittel
  ueber k: E_k[S^† P_2 S] = diag(⟨a|P_2|a⟩) = 1/2. Im naechsten Schritt geht also die Haelfte ihres Gewichts nach 2
  zurueck. Ratenbild: Das inkohaerente Gewicht 1 − N_FJ teilt sich etwa 1:1 auf 2 und 2', also ⟨w_2⟩ ≈ (1 + N_FJ)/2
  und Rueckgabequote r = (⟨w_2⟩ − N_FJ)/(1 − N_FJ) ≈ 1/2. Dann haelt SH1 nur, solange N_FJ ≥ ~0,83. Nicht erfasst:
  Lokalisierung in 2', Korrelationen durch Wiederbesuche. Diese Erwartung aendert die Karten-Wahrscheinlichkeiten nicht.
  **Selbstanzeige vorab:** Mit A8 und A9 ist SH1 naeher an "vorab ableitbar", als die Ableitbarkeitsprobe der Karte
  annahm. Die Messung prueft die Rueckgabequote r.

**Teil-A-Urteil (Schreibtisch):** Die Herleitung haelt in der Sache: Die Kompression der unitaeren Einbahn-Regel auf
eine Haelfte ist ein FJ-Schachbrett, und 2' wirkt dort als vollkommene Senke. Berichtigt werden A3 (Betraege reichen
nicht; welche Haelfte P_a und welche P-quer_a traegt, ist eine Darstellungs- und Konventionsfrage) und die
Verdoppler-Lesart (A7). **Teil B wird gerechnet, nicht nur beschrieben.** Zahlenpruefung im Rauchlauf R1.

## 2. Bau (Teil B)

1. **Gitter und Verschiebung:** BCC in ganzzahligen Koordinaten (alle Koordinaten gleicher Paritaet), Sprungvektoren
   h_a = t_a = (1,1,1), (1,−1,−1), (−1,1,−1), (−1,−1,1), Laenge √3 = 1 Hop. Komponente a springt je Schritt um +h_a
   (Realraum-Konvention; im k-Raum diag(e^{−ik·h_a})). Richtung S_+ wie die Projekt-Loesung (repr von T:2+2' in
   qca-diamant-4/lauf-69/haupt_Bb.json, per jq kopiert nach code/qcad4_repr_2p2s.json; Gewicht S_+ ≈ 4, S_− ≈ 3e−12).
2. **Muenze:** C_x = e^{iα}P_2 + e^{iβ_x}(1 − P_2) mit α = 0 und mittlerer Phase β = π (Gegentakt; dieselbe Regel wie
   A = (P_2 − P_2')S_+ in QCA-DIRAC-T-1 [P]). P_2 ist der exakte Gram-Projektor (1/2)⟨n_a|n_b⟩ der FJ-Spinoren mit der
   Haendigkeit, die die Bargmann-Invariante der Projekt-Loesung ergibt. Er ist mit dem P_2 der Projekt-Loesung
   eichverwandt (D diagonal; Pruefung R1). Grund: exakte Algebra (Projektor auf ~1e−15) statt der Genauigkeit der
   gespeicherten repr-Koeffizienten (~1e−7). Gewichte, Ortsmomente und |ψ(k)|² sind unter D invariant.
3. **Unordnung ("dark tick"):** β_x je BCC-Knoten fest und unabhaengig, gleichverteilt in [β − W/2, β + W/2].
   W ∈ {0, π/8, π/4, π/2, π, 3π/2, 2π}. Saaten: W = 0 eine (deterministisch), W = 2π sechs, sonst drei.
   Saat = 42000 + 100·i_W + s (i_W = Index in der Liste des jeweiligen Laufs, s = 0, 1, ...); Rauchlaeufe mit Saatbasis
   4200.
4. **Rechengitter:** eine FCC-Familie (A6), n ∈ Z_N³ periodisch, Basis b_i = h_i − h_0. Bezugssystem mit zyklischem
   Versatz o_t = h_{t mod 4} (Summe ueber vier Schritte null): Komponente a springt im n-Gitter um E4[a] − E4[t mod 4]
   mit E4 = (0, e_1, e_2, e_3). Paket und Unordnung ruhen im Rechengitter; die Unordnung je Nebenklasse r = t mod 4 ist
   ein eigenes Feld β_r[n] (jeder BCC-Knoten genau einmal). N = 96: Inkugel der Wigner-Seitz-Zelle des Uebergitters
   R_in = 0,8165·N Hop = 78 Hop. Pruefgroesse Randgewicht (Anteil jenseits 0,75 R_in und 0,9 R_in).
5. **Paket:** ψ_0(y) = g(y) V^†χ, χ = Spin +z (Laborrahmen), g = exp(−|y|²/(4σ²)), normiert. Ortsbreite σ je Achse
   (Hop), k-Breite 1/(2σ). P_2 ψ_0 = ψ_0 exakt (ganz in Komponente 2, um k = 0).
6. **Regel fuer σ (vor dem Rauchlauf festgelegt):** Kandidaten σ ∈ {3, 4, 5, 6, 8} Hop. Gewaehlt wird der Kandidat mit
   N_FJ(100) am naechsten bei 0,5. Grund: SH1 muss scheitern und bestehen koennen. Bei N_FJ(100) ≥ 0,83 waere SH1 nach
   A9 fast sicher erfuellt; bei N_FJ(100) = 0,5 haelt SH1 nur, wenn hoechstens etwa ein Zehntel des abgeflossenen
   Gewichts zurueckkommt. Die FJ-Kurve ist vorab ableitbar und verraet nichts ueber die Unordnungslaeufe.
7. **Zeitentwicklung:** 100 Schritte. FJ-Referenz: iterierte Kompression φ_{t+1} = e^{iα} P_2 S_+ φ_t, dasselbe Paket,
   dasselbe Gitter; im Rauchlauf zusaetzlich die C²-Regel FJ Gl. (11) gegen V φ_t.

## 3. Messgroessen

- w_2(t) = Σ_x |P_2 ψ(x,t)|² in jedem Schritt; Saatmittel ⟨w_2⟩(t). N_FJ(t) = |φ_t|² in jedem Schritt.
- d_rel(t) = |⟨w_2⟩(t) − N_FJ(t)| / N_FJ(t); D_rel = max ueber t = 1..100. Je Saat ebenso.
- Rueckgabequote r(t) = (⟨w_2⟩(t) − N_FJ(t)) / (1 − N_FJ(t)) bei t = 10, 25, 50, 100 (beschreibend; bei W < 2π nur
  normierter Ueberschuss, weil der Mittelwert dort nicht FJ ist).
- Ausbreitung: R_2²(t) = Ortsvarianz des 2-Anteils (Gewicht |P_2ψ|², minimales Bild, Hop-Einheiten), alle 5 Schritte.
  v_eff = sqrt(⟨R_2²⟩(100) − R_2²(0)) / 100 mit dem Saatmittel ⟨R_2²⟩. Beschreibend: v_steig = (R_2(100) − R_2(50))/50,
  dieselben Groessen fuer FJ, Radialprofil des 2-Anteils bei t = 100, Schwerpunktdrift.
- Grosse Wellenvektoren: f_gross(t) = Anteil des 2-Gewichts mit |k| > k_c, k_c = 4·1/(2σ) = 2/σ Hop^−1, im k-Raum der
  Familie (Brillouin-Zone des FCC-Untergitters, minimales Bild), alle 10 Schritte; Vergleich mit FJ. Die H/P/P'-Punkte
  des BCC-Bilds fallen in der Familie auf k = 0 (A7).
- Kohaerenzpruefung zu A8 (beschreibend): c(t) = ⟨φ_FJ(t)|ψ_2(t)⟩ bei t = 10, 25, 50, 100; erwartet ⟨c⟩ = N_FJ(t).
- Normerhalt Σ|ψ|² (alle 5 Schritte), Randgewicht des 2-Anteils und des Gesamtzustands.
- Bloch-Kontrolle bei W = 0: (i) w_2(t) aus der schrittweisen k-Raum-Entwicklung; (ii) Endzustand t = 100 aus dem
  Zyklusoperator U(q)^25 (wiederholtes Quadrieren); (iii) zweite Realraum-Fassung mit voller 4×4-Muenze.
- Kegelanalyse (R1, ohne Gitter): Eigenphasen von W(0); Steigungen bei |k| = 1e−5 in 60 Richtungen; P_2-Gewicht der
  Kegelzweige; Chiralitaet det M mit M_ij = (1/4) Σ_a h_ai m_aj (m_a Spinrichtung der Haelfte).

## 4. Urteilsregeln (Zahlen vor dem Rauchlauf festgelegt)

- **SH0 Plan:** eingetroffen genau dann, wenn (a), (b) und (c) gelten.
  - (a) Teil A haelt am Schreibtisch (Abschnitt 1), und die Zahlen bestaetigen ihn: V V^† = 1 und V^†V = P_2,
    Kompression = FJ (mit P oder P-quer) ≤ 1e−12 (saubere Fassung) bzw. ≤ 1e−6 (Projekt-Loesung); die
    Bargmann-Invariante der Projekt-Loesung T:2+2' passt zu genau einer Haendigkeit (Abstand ≤ 1e−6, zur anderen
    ≥ 1e−2); C²-Regel gegen Kompression im Gitter ≤ 1e−12; T-Kovarianz der sauberen Muenze ≤ 1e−12.
  - (b) W = 0: |w_2^Gitter(t) − w_2^Bloch(t)| ≤ 1e−8 fuer alle t ≤ 100 und relative Zustandsabweichung bei t = 100
    (Gitter gegen Zyklusoperator) ≤ 1e−8.
  - (c) Bloch: Eigenphasen von W(0) = {α, α, β, β} auf 1e−12; Kegelsteigungen auf 2 und auf 2' je 1/3 ± 1e−4;
    P_2-Gewicht der α-Zweige und P_2'-Gewicht der β-Zweige je ≥ 1 − 1e−6 bei |k| = 1e−5; det M auf 2 und auf 2' mit
    entgegengesetztem Vorzeichen.
  - "Kohaerente Rueckkehr" ist mit (b) abgedeckt (die Bloch-Kurve ist die Vorhersage). Beschreibend: min w_2 und
    Mittel ueber t = 51..100 minus Mittel ueber t = 1..50.
- **SH0 Kartenwortlaut:** wie Plan. "Teil-A-Herleitung haelt" gilt als erfuellt, wenn die Schlussfolgerung haelt
  (Kompression auf eine Haelfte = FJ einer Haendigkeit, 2' = Senke), auch mit Berichtigungen an Einzelschritten; die
  Berichtigungen werden vermerkt.
- **SH1 Plan:** W = 2π, Saatmittel: D_rel ≤ 0,10 → eingetroffen, sonst nicht eingetroffen. Vorbedingung: SH0 (b)
  erfuellt und 0,3 ≤ N_FJ(100) ≤ 0,7; sonst "nicht auswertbar".
- **SH1 Kartenwortlaut:** jede einzelne Saat bei W = 2π mit D_rel ≤ 0,10.
- **SH2 Plan:** W = 2π: v_eff (Saatmittel von R_2²) in [0,30; 0,3667] (1/3 ± 10 %) → eingetroffen, sonst nicht
  eingetroffen. Vorbedingung: v_eff bei W = 0 im selben Band (das Mass gibt ohne Unordnung 1/3); sonst "nicht
  auswertbar".
- **SH2 Kartenwortlaut:** Die Karte nennt kein W ("bleibt"). Eingetroffen, wenn v_eff (Saatmittel) fuer jedes
  gerechnete W > 0 im Band liegt; Vermerk je Saat.
- **Beschreibend, ohne Urteil:** r(t); f_gross(t) gegen FJ; Kohaerenzpruefung c(t); Zusatzverlust bei π/8 und π/4 mit
  Verhaeltnis ≈ 4 (W²-Skalierung, vorab ableitbar, nur Kontrolle); v_steig; Radialprofil; Randgewicht.

## 5. Ablauf und Rechnen

- Nur auf der .69 ueber kleintest.sh, Spur cpu11, je Lauf ≤ 10 min, 1 Thread, 4 GB. Ordner
  /home/fmh/fmhc-physics-remote/runde42-spiegel-haelfte/ (code/, rauch/, lauf/).
- **Rauchlauf:** R1 Teil A (alle Zahlenpruefungen, Kegelanalyse); R2 FJ-Kandidaten σ (N = 96, 100 Schritte) → σ nach
  2.6; R3 W = 0 mit Bloch-Kontrolle und C²-Pruefung (N = 96, 100 Schritte; SH0 (b)); R4 W = 2π, eine Saat, **blind**
  (schreibt nur Laufzeit, Speicher, Normerhalt und Randgewicht des Gesamtzustands, keine SH1-/SH2-Groessen).
- **Hauptlaeufe nach dem Einfrieren:** H1 W = 0 (Bloch-Kontrolle) und W = π/8, π/4; H2 W = π/2, π, 3π/2; H3 W = 2π
  (sechs Saaten). Aufteilung nach Rauchlauf-Laufzeit, je Lauf ≤ 10 min. Danach auswertung.py (ebenfalls ueber den
  Starter).
- Faellt ein Lauf aus (rc ≠ 0 oder Zeitabbruch), sind die betroffenen Urteile "nicht auswertbar"; ein zweiter Versuch
  nur mit unveraendertem Code und Vermerk.

## 6. Grenzen

- Modellintern; das Ergebnis sagt nichts ueber die Natur.
- Eine FCC-Familie statt vier: exakt gleichwertig fuer ein Paket in einer Familie (A6).
- Endliches periodisches Gitter (N = 96), Randgewicht als Pruefgroesse.
- Die σ-Wahl beeinflusst SH1 (2.6). Die Rueckgabequote r ist das von σ weniger abhaengige Mass.
- 3 bis 6 Saaten je W.

## 7. Rauchlauf (Eintrag nach dem Rauchlauf, vor dem Einfrieren; Text ab 18:07:04 CEST)

Alle Laeufe auf der .69 ueber kleintest.sh, Spur cpu11, rc = 0 ausser der ersten R5-Auswertung (UTC = CEST − 2 h). Dateien in
rauch-69/.

| Lauf | Inhalt | Start (UTC) | Dauer | Speicher |
|---|---|---|---|---|
| R1 | Teil A (Zahlenpruefung, Kegel) | 16:00:07 | 0,3 s | 39 MB |
| R2 | FJ-Kandidaten σ = 3, 4, 5, 6, 8; N = 96; 100 Schritte | 16:00:31 | 79 s (je σ ~15 s) | 357 MB |
| R3 | W = 0, Bloch-Kontrolle, C²-Pruefung; σ = 4; N = 96 | 16:02:07 | 79 s (Lauf 17 s) | 1,8 GB (Zyklusoperator) |
| R4 | W = 2π, eine Saat, blind | 16:03:47 | 39 s (Lauf 19,5 s) | 581 MB |
| R5 | Codepfad-Probe N = 24 (W = 0 und 2π, 2 Saaten) und auswertung.py; nur rc und Schluessel angesehen | 16:06:05; Auswertung 16:06:14 (rc = 1, JSON-Fehler), 16:06:41 (rc = 0) | 9 s; 7 s | |

- **R1 (Teil A) [R]:** Die gespeicherte Projekt-Loesung T:2+2' ist genau (C unitaer auf 7,6e−13, Rest S_− 3e−12).
  - V V^† = 1 (1,8e−15), V^†V = P_2 (0), Diagonale 1/2, Nebenbetrag² 1/12 auf 1e−15.
  - **Spinrichtung der Haelfte 2 ist antiparallel zum Frequenzvektor h_a** (m_a·h_a = −1 bei allen a), die von 2'
    parallel. Bargmann-Invariante passt zu "−h" auf 1,2e−16, zu "+h" nicht (4,8e−2).
  - Kompression auf 2 = FJ mit P-quer auf 1,7e−15 (mit P: Abstand 1,56). Bei T:2+2'' umgekehrt: 2 parallel,
    Kompression = FJ mit P auf 7,8e−16. Das ist die Karte "2 gegen 2''".
  - Iterierte Kompression gegen e^{iαt} V^† A^t V: 2,4e−14 (t ≤ 10). T-Kovarianz der Projekt-Loesung ≤ 2,1e−15,
    der sauberen Fassung ≤ 5,3e−16. Phasenwahl: A gleich auf 1,1e−16, P_2 eichverwandt auf 6e−17. Saubere Fassung gegen
    Projekt-Loesung nach Eichung D: 1,0e−15.
  - Kegel (saubere Fassung): Eigenphasen W(0) = {0, 0, π, π} auf 1,1e−16; Steigungen 1/3 auf 3e−11 (2 und 2');
    P_2-Gewicht der α-Zweige ≥ 1 − 1,1e−11; det M_2 = −1/27, det M_2' = +1/27.
- **R2 (FJ-Referenz, vorab ableitbar):** N_FJ(100) = 0,357 / 0,496 / 0,605 / 0,687 / 0,795 fuer σ = 3 / 4 / 5 / 6 / 8.
  **Nach Regel 2.6 gilt σ = 4** (N_FJ(100) = 0,4956), k_c = 0,5 Hop^−1. Randgewicht FJ jenseits 0,75 R_in 5e−5.
- **R3 (SH0-Kontrolle, σ = 4) [R]:** C²-Regel gegen Kompression 2,6e−17; Bloch w_2-Kurve 1,0e−13; Endzustand gegen
  Zyklusoperator 2,7e−14 relativ; zwei Realraum-Fassungen 3,6e−17; Normerhalt 4e−14. Bei W = 0: w_2 ≥ 0,9897,
  w_2(100) = 0,9979 (kohaerente Rueckkehr). Vorbedingung SH2: v_eff(W = 0) = 0,3237 im Band (gesehen, Kontrollgroesse);
  v_eff(FJ) = 0,336.
- **R4 (blind):** 19,5 s je Saat, 581 MB, Normerhalt 4e−14, Randgewicht des Gesamtzustands jenseits 0,75 R_in 3,8e−5.
  N = 96 genuegt.
- **Nicht angesehen:** w_2, R_2, f_gross und Ueberlapp bei W > 0 (R4 schreibt sie nicht; R5-Werte nur als Schluessel).
- **Festlegungen nach dem Rauchlauf (vor dem Einfrieren):**
  - σ = 4 (Regel 2.6), N = 96, 100 Schritte.
  - Hauptlaeufe mit getrennten Saatbasen: H0 Teil A; H1 W = 0 (Bloch, C²) und π/8, π/4, Saatbasis 42000; H2 W = π/2,
    π, 3π/2, Saatbasis 43000; H3 W = 2π, sechs Saaten, Saatbasis 44000; dann auswertung.py. Geschaetzt je Lauf 2 bis
    5 min.
  - auswertung.py: Urteilsregeln wie Abschnitt 4; R5 hat nur den Codepfad geprueft (ein Fehler bei der JSON-Ausgabe
    von numpy-Wahrheitswerten wurde vor dem Einfrieren behoben).
