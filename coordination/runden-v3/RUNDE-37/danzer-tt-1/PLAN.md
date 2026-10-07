# DANZER-TT-1: Plan (Runde 48, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. KARTE.md ist bindend; DT0 bis DT3 und ihre Bedeutung bleiben unveraendert.
- **Zeiten (date; die .69 schreibt UTC, CEST = UTC + 2):**
  - Start 2026-10-05 10:25:53 CEST. Code ab etwa 10:31 CEST. Rauchtests ab 08:40:23 UTC. Plantext ab 10:48 CEST.
  - Zeitbox 150 min, also bis 12:55:53 CEST.
- **Kennzeichen:** [M] eigene Mathematik (ungeprueft), [E] gerechnet, [P] Projektdatei, [F] Festlegung dieses Plans,
  [H] Hypothese, [R] aus den Rauchtests (vor dem Plan gesehen), [K] Kopfrechnung.
- Alles ist synthetische Rechnung an gedachten, unendlich periodischen Netzen. Keine Messdaten.

## 0. Gelesen (vor dem Plan)

- KARTE.md.
- DANZER-NAEHERUNG-1 und -2: ERGEBNIS.md, PLAN.md, code/danzer_naeherung.py (Bau), code/dn2.py (netz2: Saat, Fenster-Stoerung,
  Zitter, Delaunay, Pruefungen, Klassen).
- TT-ISO-1: ERGEBNIS.md, PLAN.md, tti.richtungen13 (Messung, 13 Richtungen, |k| = 1e-3 und 2e-3, Spanne max/min - 1).
- TT-GLAS-1: ERGEBNIS.md, code/tg.py (Modell fuer beliebige periodische Zerlegungen, punkt, affin).
- DEFEKT-NETZ-1: ERGEBNIS.md, code/dn.py (lauf_tt, baue). A15 0,9339 % (s = 0,009338681518611835), C15 2,6847 %,
  V 6,3388 % (lauf-69/tt-*.json, per jq gelesen) [P].
- CODEX-REVIEW-R48 REVIEW.md, Abschnitt 4 Punkt 2.
- LUND-REGGE-MASSE-1/KARTE.md: andere Masse (geschwindigkeitsseitige Lund-Regge-Form), Netze V, S, A15, Glas, Spuren cpu5
  und cpu6. Hier nur die impulsseitige A1-Masse (J = 1) auf den Danzer-Naeherungen; keine Ueberschneidung.
- Kein Projekt-grep.

## 1. Netze, Saaten, Gleichstaende [F]

- **Bau wie DANZER-NAEHERUNG-2:** dtt.netz_danzer uebernimmt dn2.netz2 Zeilen 135 bis 150 woertlich. Das heisst:
  - Saat-Strom default_rng([3746, p, q, s]); Fenster-Stoerung gamma = 1e-7 xi; Ecken aus danzer_naeherung.ecken.
  - Zitter sigma_D = 1e-6 nur fuer die Delaunay-Kombinatorik, ueber 27 Zellkopien; behalten wird jedes Tetraeder, dessen
    (verzitterter) Schwerpunkt in [0, L)^3 liegt. Die Geometrie nutzt die unverzitterten Ecken.
  - Daraus Gittervektoren L I, Lagen, Tetraeder und Bildversaetze fuer tg.modell.
- **Gegenprobe je Netz (Option --dn2):** dn2.netz2 auf derselben Saat. Kantenmenge und Ecken (sha256) muessen gleich sein.
  Dazu werden die *1- und *0-Klasse (Pflasterungsklasse wie DANZER-NAEHERUNG-2, Tabelle 4.3) gemeldet.
  Rauchtest [R]: 1/1 und 2/1, Saat 0: Kanten gleich, Ecken gleich, E und T gleich.
- **Gleichstaende:**
  - Kugel-Gleichstaende (5 oder mehr Ecken auf einer Umkugel) loest der Zitter auf, wie in DANZER-NAEHERUNG-2.
  - Anders als die DEC-Gewichte haengt das TT-Modell von der Aufloesung ab [M]. Regge-B und A1-Masse sind Summen ueber
    Tetraeder, und ein Gleichstand laesst verschiedene Zerlegungen mit verschiedenen Kanten zu.
  - Deshalb gibt es eine **Zitter-Kontrolle**: gleiche Ecken, anderer Zitter (Strom [3746, p, q, s, 1001] wie
    DANZER-NAEHERUNG-2), fuer Saat 0 bei 1/1 und 2/1, bei 3/2 falls Zeit bleibt.
  - Fenster-Gleichstaende: Die Saat waehlt ueber gamma verschiedene gueltige Pflasterungen (DANZER-NAEHERUNG-2: 2/1 vier
    Klassen, 3/2 drei). Die Saatstreuung enthaelt beides. Gemeldet werden je Saat Tetraeder-Fingerabdruck, *1-Klasse,
    Zahl der Tetraeder mit Gleichstand und Zusatzpunkte auf Umkugeln.
- **Saaten:**
  - 1/1 und 2/1: 0 bis 7.
  - 3/2: zuerst 0, 1 und 2, je eine Klasse aus DANZER-NAEHERUNG-2 (42c27cb6: 0, 3; 7a267aa0: 1, 5, 7; 70291885: 2, 4, 6).
    Danach 3 bis 7, soweit die Zeit reicht.
  - 5/3: nicht gerechnet (Abschnitt 5).
- **Kontrollnetze:** V (tg.netz_V), A15 und C15 (dn.baue, Delaunay), mit demselben Messcode.

## 2. Modell und Rechenwege [F]

- **Modell:** tg.modell und tg.ops unveraendert (TT-GLAS-1, gleich EINE-WELT-LOCH-1 mit A1R1 und J = 1).
  - Kantenwerte a_e = delta l / l; B Regge; Eichung M (Eckverschiebung); skalare Regel c_v = -B w_v mit Gewicht l_e.
  - Bewegungsenergie je Tetraeder A0 = (n_e . n_f)^2 - 1/2; Reduktion R1.
- **Rechenweg "dicht" = tg.punkt** (vollstaendige QR von [M, c], alle Eigenwerte). Er prueft auch A_red positiv definit und
  B_red ohne negative Richtung.
  - Bei 3/2 (E = 4032) kostet er etwa 120 bis 180 s je k-Punkt (TT-GLAS-1, N = 512, E = 3983 [P]). Fuer 52 Werte je Saat
    ist das zu teuer.
- **Rechenweg "duenn" (neu, Hauptweg fuer alle Netze und fuer DT0):** dieselben Operatoren, dieselbe Reduktion.
  - Die omega^2 von R1 sind die von null verschiedenen Eigenwerte von P A P B P, mit P = Projektor auf Bild(N)^perp und
    N = [M, c]. Gleichwertig sind es die Eigenwerte des hermitesch-definiten Paars (S^H B S, (S^H A S)^-1) [M].
  - (P A P)^+ v ist x aus dem Sattelpunktsystem [A N; N^H 0][x; mu] = [v; 0], ebenso fuer B. Beide werden mit splu geloest
    (Ordnung siehe Abschnitt 5), mit 2 Nachiterationen.
  - Op = (P B P)^+ (P A P)^+ hat die Eigenwerte 1/omega^2.
  - Block-Inversiteration aus den 6 affinen Wellen a_e = n_e^T h n_e e^{i k . m_e} (h = tp.B6, wie tg.tensor_fit):
    X1 = Op X0, X2 = Op X1.
  - Ritz-Raum: die Richtungen von X2 mit Singulaerwert ueber 1e-6 x groesster. Rauchtests [R]: immer genau 2.
  - Rayleigh-Ritz mit Bm = V^H B V und Mm = V^H (PAP)^+ V. Der Wert je Mode ist der Rayleigh-Quotient
    u^H B u / u^H (PAP)^+ u.
  - Der TT-Anteil kommt aus u ueber tg.tensor_fit und tp.tt_anteil, wie in tg.punkt.
- **Gegenprobe duenn gegen dicht [R]:** Rauchtest auf V, A15, C15, 1/1 und 2/1 (Saat 0), Richtung [210], |k| = 1e-3.
  - Groesste relative Abweichung der masselosen Werte: 5,2e-8 / 1,3e-8 / 5,5e-8 / 5,0e-9 / 2,0e-8.
  - Residuum der TT-Paare hoechstens 3,3e-9; Nebenbedingung N^H u hoechstens 1,5e-15 (relativ).
  - Ein erster Ritz-Ansatz mit 12 Richtungen wich bis 3e-3 ab (Rauschrichtungen im Ritz-Raum). Ein ARPACK-Ansatz ohne
    Nachiteration wich bei V um 5e-5 ab. Beide sind verworfen; Selbstanzeige im Ergebnis.
- **Grenzen des duennen Wegs:**
  - Er liefert nur die 2 tragenden Werte naechst null.
  - A_red positiv definit, B_red ohne negative Richtung, die Luecke zum dritten Wert und "genau zwei masselos" prueft er
    nicht. Das uebernimmt der dichte Weg in Abschnitt 4.
  - Ritz-Werte sind obere Schranken (Min-Max) [M]. Ein negativer Ritz-Wert waere also sicher eine wachsende Mode.
- **Gegenprobe im Hauptlauf [F]:**
  - Alle 26 Punkte dicht auf V, A15, C15 (Kontrolle), auf allen 1/1-Saaten und auf 2/1 Saat 0.
  - Bei 3/2 ein dichter Punkt ([100], |k| = 1e-3, mit TT-Anteil) fuer Saat 0.
  - **Schwelle 1e-5 relativ.** Liegt eine Saat darueber, wird sie als unsicher gekennzeichnet, und die Urteile werden mit
    und ohne sie berichtet.

## 3. TT-Messung [F] (wie TT-ISO-1 und DEFEKT-NETZ-1)

- 13 Richtungen tti.richtungen13 ([100], [110], [111], [210], [211], [221], [310], [311], [320], [321], [322], [331], [332])
  x |k| = 1e-3 und 2e-3 x 2 TT-Zweige = 52 Werte omega^2/k^2.
  - **Spanne s = max/min - 1.**
  - TT-Anteil an [100], [110], [111] (|k| = 1e-3); Linearitaet (2e-3 gegen 1e-3).
  - Regulaer wie DEFEKT-NETZ-1. Fuer den duennen Weg ohne die A_red/B_red-Teile; die prueft Abschnitt 4.
- Die Naeherungen haben keine volle Wuerfelsymmetrie: gamma bricht T_h, dazu kommen die Zerlegungen. Die 13 Richtungen
  liegen im O_h-Keil.
  - Deshalb beschreibend zusaetzlich die 13 Wuerfelachsen von TT-GLAS-1 (|k| = 1e-3), fuer 1/1 und 2/1 (alle Saaten)
    und fuer 3/2, falls Zeit bleibt.
  - Daraus die Spanne ueber alle 26 Richtungen bei 1e-3. Darauf beruht kein Urteil.
- Affine Regge-Steifigkeit tg.affin, beschreibend.
- Zerlegung wie DEFEKT-NETZ-1, beschreibend: Richtungsspanne der Zweigmittel und groesste Aufspaltung der Polarisationen.

## 4. Stabilitaet (DT2) [F]

- "Gerechnete k" sind:
  - alle Spektrum-Punkte (26 je Netz; der duenne Weg sieht nur die tragenden Werte);
  - die dichten Gegenprobe-Punkte (Abschnitt 2);
  - ein Gitter Lk^3 je Superzelle (ohne k = 0) mit dem dichten Weg, also alle Eigenwerte, A_red und B_red.
- Gitter:
  - 1/1: Lk = 8 (511 k), alle 8 Saaten.
  - 2/1: Lk = 4 (63 k), alle 8 Saaten.
  - 3/2: Lk = 2 (7 k), Saat 0; falls Zeit bleibt, auch Saat 1.
  - Abtastung in Zelllaengen [K]: 1/1 8 x 2,75 = 22; 2/1 4 x 4,45 = 17,8; 3/2 2 x 7,21 = 14,4.
- Wachsend wie tg.punkt: Re omega^2 < -1e-12 s oder |Im| > 1e-12 s (s = groesstes |omega^2|). Im duennen Weg:
  Re omega^2 < -1e-6 eps^2 oder |Im| > 1e-6 eps^2, nur unter den Ritz-Werten.
- Die Zitter-Netze zaehlen mit (ihre Spektrum-Punkte).

## 5. Laufliste, Laufzeiten, Speicher [F]

**Rauchtests (alle ueber kleintest.sh, Arbeitsordner /home/fmh/fmhc-physics-remote/danzer-tt-1/, Logs in rauch/) [R]:**

| Test | Spur | Inhalt | Zeit (UTC) | Ergebnis (nur Zeiten, Abweichungen, Schluessel) |
|---|---|---|---|---|
| R1 | cpu8 | rauch V, A15, 1/1, 2/1 | 08:40:23 bis 08:40:24 | rc 1, Programmfehler (Startvektor) |
| R2 | cpu9 | rauch 3/2 mit dn2 | 08:40:23 bis 08:41:14 | rc 1, derselbe Fehler nach Bau, dn2 und LU |
| R3 | cpu8 | ARPACK ohne Nachiteration | 08:41:31 bis 08:41:41 | duenn/dicht bis 5,2e-5 (V); dn2-Kanten und -Ecken gleich (1/1, 2/1) |
| R4 | cpu9 | 3/2 ARPACK | 08:41:31 bis 08:43:49 | **von mir gestoppt nach 138 s (ueber 120 s)**, keine Ausgabe |
| R5 | cpu8 | ARPACK mit Nachiteration | 08:42:47 bis 08:43 | duenn/dicht hoechstens 5,2e-8 |
| R6 | cpu8 | Ritz mit 12 Richtungen | 08:45:44 bis 08:45:54 | duenn/dicht bis 3,2e-3: verworfen |
| R7 | cpu9 | 3/2, LU-Ordnung MMD_AT_PLUS_A | 08:45:44 bis 08:47:35 | Selbstabbruch nach 110 s, keine Ausgabe |
| R8 | cpu8 | Ritz mit tragenden Richtungen (Hauptweg) | 08:47:02 bis 08:47:1x | duenn/dicht hoechstens 5,5e-8; Ritz-Rang 2 |
| R9 | cpu9 | 3/2, COLAMD | 08:47:42 bis 08:49:33 | Bau 1,9 s; LU-Paar 44,7 s und 46,2 s (nnz 30,8 Mio.); Selbstabbruch nach 110 s im zweiten Punkt |
| R10 | cpu10 | 3/2, MMD_AT_PLUS_A | 08:47:42 bis 08:49:33 | LU ueber 105 s; Selbstabbruch |
| R11 | cpu8 | netz 1/1 Saat 0, 2 Richtungen, alle Optionen | 08:51:50 bis 08:51:52 | rc 0 (Werte nicht gelesen) |
| R12 | cpu9 | kontrolle | 08:51:50 bis 08:51:53 | rc 0 (Werte nicht gelesen) |
| R13 | cpu8 | auswerten | 08:51:52 bis 08:51:53 | rc 2, Argumentfehler (parse_intermixed_args) |
| R14 | cpu8 | auswerten auf R11/R12 | 08:52:31 bis 08:52:33 | rc 0; nur rc, Fehler-grep und Zeilenzahl gelesen |

- Zeiten je k-Punkt [R]: 1/1 duenn 0,07 s, dicht 0,03 s; 2/1 duenn 2,4 s, dicht 1,8 s; 3/2 duenn etwa 54 s (davon LU
  etwa 46 s), dicht etwa 125 s (TT-GLAS-1 [P]). Speicher 3/2 duenn bis etwa 1,5 GB (R4), MemoryMax 4G.
- **5/3 wird nicht gerechnet.** Dicht: E = 17 080, eine komplexe E x E-Matrix braucht 4,7 GB (ueber MemoryMax). Duenn:
  Die LU-Fuellung steigt von 2/1 (2,9 Mio.) auf 3/2 (31 Mio.), also etwa um den Faktor 11; bei 5/3 waeren grob
  300 Mio. Eintraege (etwa 5 GB) zu erwarten [K]. Das passt weder in den Speicher noch in die Zeitbox.
- **Laufketten** (code/kette-cpu8.sh, kette-cpu9.sh, kette-cpu10.sh; je Lauf hoechstens 600 s, ein Thread; kein neuer
  Lauf nach 10:15:00 UTC = 12:15 CEST):

| Spur | Laeufe (Reihenfolge) | geschaetzt |
|---|---|---|
| cpu8 | L01 kontrolle (V, A15, C15; duenn und dicht, 26 Punkte, affin); L02 1/1 Saaten 0 bis 7 (duenn + dicht an allen 26 Punkten, Wuerfelachsen, affin, Gitter Lk = 8, dn2); L03 1/1 Saat 0 Zitter 1; L04 2/1 Saat 0 (mit dicht an allen 26 Punkten, Gitter Lk = 4); L05 bis L08 2/1 Saaten 1 bis 7 (Gitter Lk = 4); L09 2/1 Saat 0 Zitter 1; dann L23a bis d: 3/2 Saat 3 | 0,2 + 2,7 + 0,4 + 4,3 + 4 x 3,5 bis 7 + 1,7 min, dann 4 x 6,5 min |
| cpu9 | 3/2 Saat 0 (L20a bis d), Saat 1 (L21a bis d), Saat 4 (L24a bis d); je Saat 4 Laeufe: Richtungen 0 bis 6 bzw. 7 bis 12 x \|k\| = 1e-3 bzw. 2e-3 | je Lauf 6 bis 7 min, je Saat etwa 25 min |
| cpu10 | 3/2 Saat 2 (L22a bis d); L30 dichte Gegenprobe 3/2 Saat 0 ([100], 1e-3, mit TT-Anteil); L31a bis c Gitter Lk = 2 (7 k, dicht); L32a, b Zitter-Kontrolle 3/2 Saat 0 (nur \|k\| = 1e-3, beschreibend) | 25 + 3,5 + 3 x 4,5 + 2 x 6,5 min |

- Reihenfolge fuer einen Teilbericht: DT0 und 1/1 zuerst (cpu8), 2/1 danach, 3/2 parallel auf cpu9 und cpu10.
- Auswertung L99 (cpu8): dtt.py auswerten ueber alle Lauf-Dateien, mit Bild. Reicht die Zeit nicht, wertet L99 aus, was
  da ist; fehlende Saaten stehen im Ergebnis.
- Faellt ein Lauf aus (Fehler, 600 s), steht das im Ergebnis. Eine Codeaenderung danach ist eine Selbstanzeige mit neuer
  eingefrorener Fassung.

## 6. Urteilsregeln (mechanisch, dtt.py auswerten)

- **DT0** (Kontrolle):
  - Plan: Der duenne Weg auf V gibt s_V mit |s_V / 0,0633881 - 1| <= 1e-3 (TT-ISO-1, 0,06338809562866454), und V ist
    regulaer.
  - Kartenwortlaut: |s_V / 0,0634 - 1| <= 1e-3.
  - Beschreibend: dichter Weg auf V, A15 und C15 gegen DEFEKT-NETZ-1.
- **DT1:**
  - Plan: R = Mittel_s s(3/2) / Mittel_s s(1/1) <= 1/3, dann eingetroffen; sonst nicht eingetroffen.
  - Kartenwortlaut, streng gelesen ("faellt auf hoechstens ein Drittel" fuer jede gerechnete Saat): max_s s(3/2) /
    min_s s(1/1) <= 1/3.
  - Mit nur einer 3/2-Saat wird das vermerkt.
- **DT2:**
  - Plan und Kartenwortlaut: An allen gerechneten k aller Netze 1/1, 2/1, 3/2 (alle Saaten, auch Zitter-Netze) gibt es
    keine wachsende Mode. Dann eingetroffen, sonst nicht eingetroffen. Ohne 3/2: nicht entscheidbar.
  - Beschreibend: Zahl der k mit A_red nicht positiv definit bzw. B_red mit negativer Richtung (dichter Weg).
- **DT3:**
  - Plan: Mittel_s s(3/2) < 0,9339 % (s_A15 = 0,009338681518611835, DEFEKT-NETZ-1), dann eingetroffen.
  - Kartenwortlaut, streng: jede gerechnete 3/2-Saat unter s_A15. Alle: eingetroffen; keine: nicht eingetroffen; sonst
    geteilt.
- Beschreibend: Mittel und SD je Stufe, Verhaeltnisse 2/1:1/1, 3/2:2/1, 3/2:1/1 gegen |eps|, Zitter-Kontrolle,
  Pflasterungsklassen, Spanne ueber 26 Richtungen, affine Steifigkeit, Gegenproben.

## 7. Ableitbarkeit (vor dem Einfrieren)

- **DT0 ist praktisch vorab entschieden [P, R]:**
  - Der dichte Weg ist tg.punkt unveraendert, also die Rechnung von DEFEKT-NETZ-1 (s_V = 0,0633880750, gegen TT-ISO-1
    3,3e-7 relativ).
  - Der duenne Weg wich im Rauchtest auf V um 5,2e-8 ab (Richtung [210]).
  - Kartenwortlaut: 0,0633881 gegen 0,0634 sind 1,9e-4 relativ, also unter 1e-3 [K].
  - DT0 ist damit eine Kontrolle des neuen Rechenwegs, keine Messung.
- **Grenzfall Quasikristall, Kette der Karte geprueft [M]:**
  - Rang 4: Sym2(Sym2 V) = 2 L0 + 2 L2 + L4. Unter der Ikosaedergruppe I bleibt L2 irreduzibel (H), L4 zerfaellt in
    G + H. Invariant sind nur die zwei L0-Formen tr h^2 und (tr h)^2. Eine langwellige Bewegungsenergie (Masse) mit voller
    Ikosaedersymmetrie ist also isotrop. Das stimmt.
  - Die TT-Dispersion haengt aber auch an der Steifigkeit k_m k_n C_mnijkl h_ij h_kl, einem Rang-6-Tensor.
    (L0 + L2) x (2 L0 + 2 L2 + L4) enthaelt L2 x L4, darin L6, und L6 hat unter I eine Invariante. Die Spur von C(n) auf
    dem TT-Raum ist ein Polynom vom Grad 6 in n. **Ikosaedersymmetrie erlaubt also einen l = 6-Rest der Steifigkeit.**
    Der Satz der Karte "Rang-4-Tensor, also isotrop" deckt die Steifigkeit nicht ganz ab.
  - Projektbefunde dazu [P]: Die affine Regge-Steifigkeit ist auf allen gerechneten Netzen isotrop (TT-ISO-1, TT-GLAS-1
    Z1, DEFEKT-NETZ-1). Lange TT-Wellen sind bis 1e-5 projizierte affine Wellen (TT-GLAS-2, nur ueber die Karte
    LUND-REGGE-MASSE-1 gelesen).
  - Die effektive Masse nach R1 ist langwellig eine Rang-4-Form in h. Sie ist das Minimum ueber Eich- und
    Regelrichtungen, und n geht nur ueber sym(n x xi) ein [M]. Im ikosaedrischen Grenzfall ist sie also isotrop.
  - **Folgerung:** Fuer eine Masse mit Ikosaedersymmetrie ist "Spanne gegen null" im Grenzfall vorab ableitbar, bis auf
    einen moeglichen l = 6-Rest aus der nichtaffinen Steifigkeit [M, H]. Nicht ableitbar sind Groesse und Rate bei 1/1,
    2/1 und 3/2.
- **Rate (DT1) [M, H, K]:**
  - Die Phason-Verzerrung W der p/q-Naeherung liegt in T1 x T2 = G + H. Der l = 4-Teil eines Rang-4-Tensors zerfaellt
    unter I ebenfalls in G + H. Eine lineare Kopplung ist also erlaubt: kubischer Anteil proportional zu eps, Faktor
    tau^2 = 2,618 je Stufe. Dann waere s(3/2)/s(1/1) = |eps(3/2)/eps(1/1)| = 0,0344/0,2361 = 0,146 und DT1 eingetroffen.
  - Dagegen spricht: Die A1-Masse mit J = 1 je Tetraeder haengt wie die Einheitsgewichte von DANZER-NAEHERUNG-1 von der
    Zerlegung der Gleichstaende ab [M]. Dort folgte beta nicht der Phason-Regel [P]. Es gibt also einen zufaelligen,
    glasartigen Anteil.
  - Wuerde er wie im Glas fallen (Spanne ~ N^-0,47, TT-GLAS-1 [P]), gaebe das von 32 auf 576 Ecken den Faktor 0,26 [K],
    auch unter 1/3. Das ist nur eine Lesart.
  - "Linear erlaubt" heisst nicht "linear dominant"; bei 1/1 (eps = 0,236) koennen hoehere Ordnungen tragen.
  - **DT1 ist nicht vorab ableitbar.** Beide naheliegenden Mechanismen sprechen fuer ein Verhaeltnis unter 1/3.
- **DT2 ist nicht ableitbar.** Alle bisher gerechneten A1R1-Netze mit J = 1 (V, S = C15, A15, Glas bis N = 512) waren an
  den gerechneten k stabil [P]. Kein Satz erzwingt das fuer die Naeherungen.
- **DT3 ist nicht ableitbar.** Es haengt an s(1/1) und der Rate. Vorab nur [K]: Gilt die eps-Regel ab 1/1, trifft DT3 ein,
  wenn s(1/1) unter 0,934 % / 0,146 = 6,4 % liegt.
- **Abhaengigkeit von der Zerlegung:** Dass TT von der Aufloesung der Kugel-Gleichstaende abhaengt, ist vorab ableitbar
  [M]. Die Groesse ist es nicht; die Zitter-Kontrolle misst sie.
- **Kennzahlen-Abgleich:** TT auf diesen Netzen gibt es im Projekt nicht (Karte; kein eigener grep). Die Netze sind
  bitgleich mit DANZER-NAEHERUNG-2 (dn2-Gegenprobe), die Gewichte (A1, Regge) sind andere.

## 8. Agenten-Vorhersagen (vor jeder Hauptrechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| B1 | DT0 nach Plan eingetroffen | 95 % |
| B2 | Gegenprobe duenn gegen dicht an allen gerechneten Punkten <= 1e-5 | 85 % |
| B3 | Zitter-Kontrolle: Die Spanne von 1/1 oder 2/1 aendert sich um mehr als 1e-4 (absolut) | 60 % |
| B4 | Saatmittel s(2/1) < s(1/1) | 75 % |
| B5 | DT1 nach Plan eingetroffen | 55 % |
| B6 | DT2 eingetroffen | 70 % |
| B7 | DT3 nach Plan eingetroffen | 45 % |

## 9. Einfrieren

- Eingefroren werden PLAN.md und code/dtt.py als Kopien *.eingefroren-<Zeit>, mit sha256 in EINGEFROREN-SHA256.txt; auf
  der .69 dieselben Pruefsummen. Die uebrigen Code-Dateien sind unveraenderte Kopien:
  danzer_naeherung.py 0571953e, licht_netz.py 98d3960a, dn2.py a834b826, tg.py ec48a258, ew.py fa7b6417, tp.py 419d7da6,
  tti.py 6d6b6f7b, nachtrag_kinetik.py fd0d17b9, dn.py 0cd5d13e.
- Danach keine Aenderung an Plan, Code oder Regeln.
