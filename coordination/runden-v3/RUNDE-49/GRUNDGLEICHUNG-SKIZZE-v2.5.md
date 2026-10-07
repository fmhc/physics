# Grundgleichung fuer Finns Netz: gewaehlte Architektur und offene Folgerungen (Fassung 2.5)

- Leitung claude-primary; Fassung 2.3 geschrieben ab 2026-10-05 12:38:10 CEST, Aenderungen zu 2.4 ab 13:00:21 CEST, zu 2.5 ab 13:29:23 CEST (date).
- **Neu in 2.5:** zwei Berichtigungen nach Codex (Peerbus 13:08, IDEATION-4-CLAUDE-ABGLEICH.txt, von einem Nicht-Autor gegengelesen): unimodulare Uhr und K = 0 auf dem leeren Torus (Abschnitt 4); der R-Transfer des Skalars ist nicht kanonisch (Abschnitt 6).
- **Grundlage:**
  - Fassungen 2, 2.1, 2.2 und 2.3 (bleiben als Lesestaende unveraendert)
  - vier frische Leser: zu Fassung 2 (7 A, 13 B, 7 C), zu 2.1 (5 A, 14 B, 9 C), zu 2.2 (3 A, 7 B, 11 C), zu 2.3 (2 A, 3 B, 11 C; Urteil "weitergabefaehig nach den A-Befunden"); Befunde in RUNDE-37/grundgleichung-v2-leser, -v21-leser, -v22-leser, -v23-leser
  - Codex' Gegenblick zu Fassung 2 (codex-ideation-20261005/GRUNDGLEICHUNG-v2-GEGENBLICK.md)
  - Ernten seit Fassung 2 (RUNDE-48.md, RUNDE-49.md), zuletzt GIELEN-RIED-TIEF-L
- **Status:** Schreibtisch [ES]. Die Aenderungen von 2.3 auf 2.4 (A1, A2 und B1 bis B3 des vierten Lesers; dazu der Stand von REGIME-K-1 und GIELEN-RIED-TIEF-L in 2.3 (ii), 4, 7, 8 und 9) hat kein Leser mehr gesehen. Nichts hier ist ein Ergebnis; was "entstehen soll", ist eine Pruefliste. Alle Projektbezuege sind Modellrechnungen, keine Messdaten.
- Kennzeichen: [M] Mathematik, [P] Projektbefund, [S] Literatur an der Quelle, [S Treffer] nur Suchtreffer, [L] Gedaechtnis (ungeprueft), [ES] Schreibtisch, [H] Hypothese, **[W]** Modellentscheidung (gesetzt, nicht hergeleitet).
- **Begriffe und Zeichen:**
  - "Takt-Operator" T = 8 d0ᵀ *1 d0; "maximale Scheibung" K = 0 (K Spur der aeusseren Kruemmung); "globaler Lapse" ein N fuer alle Zellen. Das Wort "Takt" allein wird nicht benutzt.
  - Sh = Shift-Operator auf die Kantenraten; S = |phi|^2 (Argument des Potentials U); S_T = g^ij T_ij (Spannungsspur der Materie); "Netz S" = C15.
  - Lesart R: beim Umklappen Laengen und Raten stetig, danach orthogonale Projektion auf die neue Zwangsflaeche (Skalar: dphi/dt stetig). Lesart P: Impulse stetig, Null-Fortsetzung (Skalar: pi stetig).

## 0. Stand der Einarbeitung

- **Codex zu Fassung 1 (fuenf Punkte):** alle angenommen. Eingearbeitet sind 2, 3, 4 und 5. Punkt 1 teilweise: Shift-Interpolation ja (Abschnitt 1); Spurbindung als Kette benannt, am Code offen (2.2); D_v nur benannt (2.4).
- **Codex zu Fassung 2:** Punkte 1, 2, 3 und 5 umgesetzt. Bei Punkt 4 offen: globale Impulsrekonstruktion, volle Variation mit Bewegungstermen (Abschnitt 5), Vorzeichen von rho + S_T dort, wo es zaehlt (Abschnitt 4).
- **Leser:** alle A-Befunde der drei Leser eingearbeitet; B- und C-Befunde des dritten Lesers weitgehend (unten ohne Einzelvermerk).
- **Wichtigste Berichtigungen seit Fassung 2:**
  - Die zwei "nur" zur Lapse-Linearitaet waren falsch (2.3).
  - K = 0 ist auf dem geschlossenen Torus nur in linearer Naeherung zulaessig. Mit Lambda = 0 und rho >= 0 schliesst der T^3-Satz maximale Daten mit Materie ganz aus (Abschnitt 4).
  - "Kruemmung = Spannung" gilt in dieser Form nur statisch und bei gleichem N. Im Kontinuum (Lambda = 0, rho >= 0) gibt es auf dem Torus keine statischen Lagen mit Materie; ob das auf dem Netz gilt, ist offen [H] (Abschnitt 5).
  - Die Zahlen belegen keinen Gegensatz "Zwangsstruktur gegen Isotropie". Ohne wachsende Moden in den gerechneten Spektren sind bisher die zwei Paarungen A1R1 und A2R1, nicht eine Reduktion; die Positivitaet auf der Eichung fehlt auch dort (2.3, 4).

## 1. Zustand (feste Topologie, festes Netz)

- Raum: 3-Torus (periodisch), feste Zerlegung T, alle Tetraeder nicht entartet, Delaunay [W]. Umklappen kommt erst in Abschnitt 6 dazu.
- Kanonische Paare:
  - Geometrie: q_e = l_e^2 und p^e (Kanten)
  - Licht: A_e und E^e (Kanten; A reell und nicht kompakt [W])
  - Materie: phi_v und pi_v (Ecken, komplex; Normierung in 3.2)
- Multiplikatoren an den Ecken: Lapse N_v, Shift s_v, A0_v (Gauss).
- **Interpolation [W]:** N_t, N_e, N_f sind Mittel der Ecken von t, e bzw. f. Der Shift ist das stueckweise lineare Vektorfeld aus den Eckwerten s_v (ein je Zelle konstanter Wert gaebe L_s g = 0).

## 2. Eine kanonische Konvention (Phasenraumform)

### 2.1 Wirkung

S = Integral dt [ Summe_e p^e dq_e/dt + Summe_e E^e dA_e/dt + Summe_v (pi_v dphi_v/dt + c.c.) - H_tot ]

H_tot = Summe_v N_v H_v + Summe_v s_v . D_v + Summe_v A0_v G_v

- H_v und G_v sind unten definiert, D_v nur als Anforderung (2.4). Das Schema loest die Algebra der Zwangsbedingungen nicht (Abschnitt 4).

### 2.2 Geometrie in H_v (ADM-Vorzeichen)

- **Kontinuum [L, Standard-ADM; vom ersten Leser nachgerechnet]:** H = (16 pi G/sqrt g)(pi:pi - (1/2)(tr pi)^2) - (sqrt g/16 pi G)(R - 2 Lambda).
- **Netz:** Integral sqrt(g) R = 2 Summe_e l_e eps_e (Regge), Integral sqrt(g) = Summe_t V_t.
- **Bewegungsanteil, Form A [W]:** 16 pi G Summe_t w_vt (1/V_t) [pi_t:pi_t - (1/2)(tr pi_t)^2]
  - Eine **Setzung**, keine Uebersetzung. Im Kontinuum steht in jeder Zelle ihr Anteil am Impuls. Form A setzt in jede Zelle den vollen Kantenimpuls p^e (Zellimpuls aus den sechs Kantenimpulsen der Zelle).
  - Je Zelle ist Form A die Umkehrung der geschwindigkeitsseitigen Form h:h - (tr h)^2, global nicht: Die Summe lokaler Inversen ist nicht die Inverse der Assemblierung.
  - **Spurkoeffizient 1/2** = lambda/(d lambda - 1) bei lambda = 1, d = 3 [M].
    - Kette zur Bindung im Code [P, mit Vorbehalt]: HODGE-MASSE-1 meldet A2_t K_t = 1 auf 1,6e-9 mit der lambda = 1-Form K_t. Dann ist A2 je Zelle deren Inverse mit Spurkoeffizient 1/2. Am Code nicht bestaetigt.
  - Masse ~ Volumen ist die Projektvariante A2; A1 ist dieselbe Zellform ohne Volumengewicht.
  - Bei gleichmaessiger Rate verfehlt A2 den Kontinuumswert (HM0: 1,02 bis 1,36, spurfrei 0,019 bis 0,039 des Kontinuumswerts; Lesart Verhaeltnis oder Abweichung in der Quelle offen). Die Lund-Regge-Form trifft ihn auf hoechstens 1,2e-13 [P, HODGE-MASSE-1].
- **Kruemmungsanteil:** -(1/8 pi G) Summe_e w_ve l_e eps_e + (Lambda/8 pi G) Summe_t w_vt V_t. Die positiv benannte Regge-Summe steht mit **Minus** in H, wie -sqrt(g) R.
- **Gewichte [W]:** w_vt = 1/4, w_ve = 1/2 fuer die Ecken von t bzw. e; Summe_v N_v w_vt = N_t.

### 2.3 Lapse-Abhaengigkeit der Traegheit [M, ES]

- **Form A** ist linear in N. Ihre N-Variation liefert N-freie Zwangsfunktionen H_v. Ob diese erster Klasse sind, ist offen (Abschnitt 4); auch Form A kann am Ende N festlegen.
- **Form B** (geschwindigkeitsseitig nach Lund-Regge, Literaturstandard; im Projekt A2L):
  - L_kin = Summe_t (1/(2 N_t)) vᵀ M_t v mit v = qdot - Sh s. Die Legendre-Umkehr gibt (1/2) pᵀ M(N)^-1 p + pᵀ Sh s mit M(N) = Summe_t M_t/N_t [M].
  - **Bedingungen:**
    - M(N) invertierbar fuer alle zugelassenen N. M_t ist indefinit (DeWitt mit lambda = 1 in 3D: Signatur (5,1)); bei entartetem M erst der Dirac-Algorithmus.
    - Der Shift wirkt als gemeinsame Kantengeschwindigkeit Sh s. Bei zellweise verschiedenen Shift-Operatoren Sh_t wird H quadratisch in s.
  - **Homogen vom Grad 1 [M]:** Fuer den Lapse-Teil H_N (Bewegung plus Potential, ohne Shift- und Gaussterm) gilt M(aN) = M(N)/a, also H_N(aN) = a H_N(N). H_N ist damit linear entlang jedes Strahls N = a(t) N̂, mit beliebigem festen Profil N̂; der globale Lapse ist der Sonderfall N̂ = 1.
  - **Nichtlinear bei gemeinsamen Freiheitsgraden:**
    - Spielzeugbeispiel [M]: ein gemeinsamer Freiheitsgrad zweier Zellen mit Massen m1, m2 gibt H = p^2 N1 N2/(2 (m1 N2 + m2 N1)), fuer m1 = m2 = 1 also p^2 N1 N2/(2 (N1 + N2)). Unabhaengige Bloecke ohne gemeinsame Kante sind dagegen linear (Codex 1).
    - Fuer echte Regge-Zellen (je sechs Kanten, indefinite M_t) ist "generisch nichtlinear" bis zur Zwei-Tetraeder-Probe (Abschnitt 9) [H].
  - **Zwangsbedingungen bei B [M, H]:**
    - C_v = dH_N/dN_v ist homogen vom Grad 0, haengt also nur von den Verhaeltnissen N_v/N_w ab.
    - Nach Euler gilt Summe_v N_v C_v = H_N. Eine globale Bedingung bleibt; generisch legen die Gleichungen die V - 1 Verhaeltnisse fest [H, zu pruefen].
    - Friedman/Jack 1986: Lapse und Shift je Simplex koennen durch Konsistenz bestimmt werden, wenn vorab gewaehlte Multiplikatoren die Bedingungen nicht erhalten [P, REGGE-KINETIK-L, nur Abstract]. Gambini/Pullin, "consistent discretizations" [L].
- **Weitere lineare Formen:**
  - **Nichtlokal [M]:** (1/2) Summe_e N_e p^e (M(1)^-1 p)_e mit dem festen M(1) = Summe_t M_t ist linear in N und bei gleichem N gleich B.
    - Preis: M(1)^-1 ist dicht; wie schnell es abfaellt, ist offen (M indefinit).
    - Gleiche Werte bei gleichem N heissen nicht gleiche Zwangsbedingungen: Die Ableitungen nach N_v unterscheiden sich. Gleiche Stabilitaet wie B ist nur in linearer Ordnung um p = 0 gezeigt.
  - **Gemischte Form [M, Codex 2]:** L = Summe_t [P_tᵀ R_t v - (N_t/2) P_tᵀ G_t^-1 P_t] mit unabhaengigen Zellimpulsen P_t, Rekonstruktionsmatrizen R_t und der Kopplung p = Summe_t R_tᵀ P_t. Vor der Elimination linear in N; sie macht die fehlenden Abgleichbedingungen sichtbar. Erst deren Dirac-Analyse kann einen Ausweg zeigen oder ausschliessen.
- **Was die Rechnungen zeigen [P; HODGE-MASSE-1 Tab. 4.2, LUND-REGGE-MASSE-1]:**
  - Ohne wachsende Moden auf allen sieben gerechneten Netzen und im Umklapp-Kasten sind nur die Paarungen A1R1 und A2R1. Sie sind richtungsabhaengig (V: 6,34 % bzw. 5,92 %).
  - B mit RH ist bis auf ~1e-7 TT-isotrop (S, A15; V nicht trennbar, Ritz 3,16 %; Glas Ritz 3,5e-6 bis 7,7e-6). Es hat wachsende Moden: je 1 auf V, S und A15, 46 bis 50 auf Glas.
  - B mit R1 ist auf den Kristallen bei kleinem k regulaer, aber anisotrop (V 10,6 %, S 0,74 %, A15 4,7 %). Bei grossem k waechst es: an 142 (V), 28 (S) und 12 (A15) von 511 k, erst ab kl ~ 0,94 / 2,17 / 2,02. Auf Glas waechst es an jedem gerechneten k (27 bis 33 Moden).
    - Die Anisotropie sitzt dort in der Partnerbedingung c^+ p = 0 der skalaren Regel, nicht in der Masse (Masse bei gleichmaessiger Rate kontinuumsgleich) [P, LUND-REGGE-MASSE-1].
  - B mit R2 hat eine wachsende Mode auf einem von vier Glasnetzen.
  - Auf Glas wachsen Moden mit RH (A1, A2, A2L) und mit A2LR1 in jedem Netz. Einzelne Splitter sind nicht die Ursache: Auf splitterarmem Glas bleiben A1RH 4 bis 7 und A2RH 4 bis 6 wachsende Moden je k, und die Moden sitzen nicht an den schlechtesten Zellen. Gleichgueltig ist die Zellform aber nicht: Strengere Formschranken im ganzen Netz senken die Zahl (A1RH von 9 bis 10 auf 4 bis 7) [P, SPLITTER-FREI-1].
- **Was daraus folgt [H, eingeschraenkt]:**
  - Gerechnet ist nur: Isotropie ohne Abstimmung gab es bisher nur mit B und RH, und dort wachsen Moden. Mit B wachsen Moden auch unter R1.
  - "B ist nicht linear in N" ist eine Strukturaussage, die keine dieser Rechnungen beruehrt. Um p = 0, N = 1 geht die N-Abhaengigkeit des Bewegungsterms erst in dritter Ordnung ein.
  - Die Spektren belegen einen Konflikt der getesteten Paarungen, keinen allgemeinen Ausschluss. R1 und RH gehoeren zu verschiedenen Constraintpaaren (Codex 3).
- **Auswege und Pruefwege [H]:**
  - (i) Form A als Geruest, Isotropie aus Symmetrie oder Vergroebern. DANZER-TT-1 (geerntet, A1R1): Auf den Ikosaeder-Naeherungen faellt die Spanne (12,2 / 6,2 / 2,6 %), bleibt aber ueber A15 (0,934 %). 41 bis 42 % der Tetraeder haben dort weitere Ecken auf der Umkugel; der Zufall waehlt die Zerlegung, und die Spanne haengt daran. Ein Symmetrie-Grund ist nicht gezeigt.
  - (ii) Regime K: Die Bewegungsenergie folgt aus der 4D-Regge-Wirkung. Auf dem Kuhn-Gitter laufen Schwerewellen so schon mit c, mit genau zwei Polarisationen (REGGE-WELLE-1, RUNDE-37) [P]; auf der B1-Kopie ohne Fuellung ist die euklidische Wirkung langwellig exakt einsteinsch (REGIME-K-1: TT-Spanne 9,7e-10) [P]. Fuer das gefuellte Netz V, um das es geht, ist das offen (REGIME-K-2 laeuft). Die Gleichungen legen die Zeltstangen (den diskreten Lapse) abseits flacher Loesungen in der Regel fest [L, Bahr/Dittrich; Dittrich/Hoehn]. (ii) ersetzt die gesetzte Bewegungsenergie, beantwortet aber die Frage nach einem freien Lapse nicht.
  - (iii) nichtlokale lineare Kopplung (oben), konstruierbar.
  - (iv) gemischte Form mit Zellimpulsen: Pruefweg, kein Ausweg.

### 2.4 Verschiebung und Gauss

- **D_v [ES, offen]:** D_v soll die Verschiebung der Ecke v erzeugen und auf **alle** Variablen wirken (q ueber die Kantenvektoren, phi und A ueber ihren Transport). Die Form steht aus. Linear am flachen Netz ist sie die Impulsregel aus IMPULS-NETZ-1 [P]. Abseits von flach bricht Regge die Verschiebungssymmetrie (Bahr/Dittrich) [S].
- **G_v** = (d0ᵀ E)_v - rho_v, im neutralen Arm rho = 0. {G_v, G_w} = 0, und H haengt von A nur ueber d1 A ab (d1 d0 = 0) [M].

## 3. Materie und Licht

### 3.1 Eine Zeiteinheit fuer alle Sektoren [W]

- **Setzung:** Die 8 aus dem Takt-Operator ist ein gleichmaessiger Lapse-Faktor N0 = Wurzel 8 fuer alle Sektoren. Ein konstanter Lapse-Faktor skaliert alle omega^2 gleich mit N0^2 [M].
  - Im ungefixten Modell laesst sich N0 in N_v aufnehmen; die Setzung ist dann reine Konvention. Physikalisch zaehlt nur das Verhaeltnis der Tempi zwischen den Sektoren.
- **Die zwei anderen Wege aendern Physik [M]:** Kommt die 8 allein in den Skalar, ueber Z_s oder ueber Z_t, laeuft der Skalar mit Tempo Wurzel 8 und das Licht mit 1. Die zwei Wege unterscheiden sich nur in der Compton-Laenge: Ueber Z_s aendert sich k_C^2 = U'(0)/Z_s in Netzeinheiten, ueber Z_t nicht.
- **Skalar:** Z_s/Z_t = 1 [W]. Dann gilt Z_t *0 phi'' = -N0^2 Z_t d0ᵀ *1 d0 phi - ... = -Z_t T phi - ...
- **Licht:** Y_s/Y_t = 1 [W] (in H^EM unten stillschweigend Y_s = Y_t = 1). Mit N0 gilt *1 A'' = -N0^2 d1ᵀ *2 d1 A, langwellig omega^2 = N0^2 k^2.
- **Geometrie:** N0 steht vor H_v. Im ADM-Kontinuum kuerzt sich G, also omega^2 = N0^2 k^2. Fuer Form A ist selbst das unsicher (2.2).
- **Folge [M]:** Langwellig haben Skalar und Licht mit diesen Setzungen dieselbe Grundgeschwindigkeit N0 (Netzeinheiten), richtungsgleich auf jedem periodischen, strikt Delaunay-Netz (*1 > 0).
  - Skalar und elektrischer Teil: Mit umkreisbasierten Dualzellen sind lineare Funktionen diskret harmonisch (geschlossene Dualzellen), und es gilt Summe *1 l lᵀ = Vol I [M; P DANZER-NAEHERUNG-2].
  - Magnetischer Teil: Summe_f *2_f |f|^2 n_f n_fᵀ = Vol I, und konstante Felder sind ohne Korrektor stationaer [M, von zwei Lesern unabhaengig von Hand gezeigt].
  - Die Gleichheit **zwischen** den Sektoren folgt aus der gemeinsamen Setzung, nicht aus der Hodge-Struktur.
  - Rang 2 erzwingt nicht Rang 4. Fuer Schwerewellen ist die Richtungsgleichheit damit offen (2.3).

### 3.2 Erster Arm: neutral [W]

- **Skalar (Q-Ball, globale U(1)):** komplexes Feld mit L = Z_t *0 |phidot|^2 - Z_s Summe_e *1_e |phi_a - phi_b|^2 - *0 U(S), S = |phi|^2.
  - pi = Z_t *0 phidot* (konjugiert), H^phi = Summe_v N_v [ |pi_v|^2/(Z_t *0_v) + *0_v U(S_v) ] + Summe_e N_e Z_s *1_e |phi_a - phi_b|^2.
  - Mit phi = (phi1 + i phi2)/Wurzel 2 ist das dasselbe wie das reelle Schema L = (Z_t/2) *0 (phi1dot^2 + phi2dot^2) - ... [M; Codex 4].
- **Licht:** H^EM = Summe_e N_e (E^e)^2/(2 *1_e) + Summe_f N_f *2_f (d1 A)_f^2/2. Der elektrische Term braucht *1_e > 0 (Abschnitt 6).
- **Kopplung an die Geometrie:**
  - ueber die l-Abhaengigkeit von *0, *1, *2 und V; eine gesetzte metrische Kopplung [W], kein hergeleitetes Aequivalenzprinzip
  - Die Materiespannung an einer Kante ist die Ableitung des Materieteils nach q_e, aus demselben H [ES].
  - Gleiche schwere und traege Masse einschliesslich Bindungsenergie ist ein eigener Test (Codex-Vorschlag "Rang 8" aus der Ideation 3).

### 3.3 Zweiter Arm: geladen (anderes Modell)

- Linktransport |phi_a - U_ab phi_b|^2 mit U_ab = exp(i e A_e), zeitliche kovariante Ableitung mit A0; rho_v aus den kanonischen Materieimpulsen derselben Wirkung.
- Profile, Ladungsbereiche, Stabilitaet und Bindungsbefunde des Q-Balls gelten dort nicht ohne neuen Nachweis [Codex].

## 4. Zwangsbedingungen und Zeitscheibung

- **Wahl [W]: ungefixtes Eichmodell.** N_v, s_v und A0_v sind freie Multiplikatoren.
- **Zu berechnen:** Poisson-Matrix von {H_v, D_v, G_v}, Erhaltung unter H_tot, Null- und Randmoden auf dem Torus. Erster Klasse: gut. Zweiter Klasse: Dirac-Klammer, Freiheitsgrade zaehlen.
- **Bekannt:** Gauss ist abelsch und mit eichinvariantem H vertraeglich [M]. Die Impulsregel ist linear am flachen Hintergrund erster Klasse [P, IMPULS-NETZ-1]; "linear" ist ein Zwischenziel. Die skalare Regel ist offen.
- **Maximale Scheibung K = 0 auf dem Torus [M]:**
  - Lapse-Gleichung: Laplace N = N W mit W = K:K + 4 pi G (rho + S_T) - Lambda (vom ersten Leser nachgerechnet).
  - Auf dem geschlossenen Torus folgt durch Multiplizieren mit N und Integrieren: -Integral |grad N|^2 = Integral W N^2. Bei W >= 0, nicht ueberall null, bleibt nur N = 0; die Zeit stuende still.
  - **T^3-Satz [L, Schoen/Yau 1979; Gromov/Lawson 1980]:** T^3 traegt ausser der flachen keine Metrik mit R >= 0. Mit Lambda = 0, rho >= 0 und K = 0 gibt die Hamilton-Bedingung R = K:K + 16 pi G rho >= 0; maximale Daten auf T^3 sind dann flach, ruhend und leer, gleich welches Vorzeichen rho + S_T hat. Bei Lambda > 0 und rho >= 0 gibt es auf T^3 gar keine maximalen Daten (R >= 2 Lambda > 0).
  - **Wo das Vorzeichen von rho + S_T zaehlt [M]:** bei Lambda < 0, bei U < 0 und fuer die CMC-Alternative unten. Fuer das komplexe Feld gilt rho + S_T = 4 |phidot|^2 - 2 U; das ist negativ fuer jede statische Lage mit U > 0 und im Q-Ball-Schwanz (U ~ m^2 |phi|^2), wenn omega^2 < m^2/2.
  - Diskret [H]: Dasselbe gilt, wenn die diskrete Lapse-Gleichung die Form d0ᵀ *1 d0 N = -*0 W N mit W >= 0 hat. Der Operator kommt aus {K_v, H_w}, also aus dem gewichteten Schlaefli-Term; dass er d0ᵀ *1 d0 ist, ist nicht gezeigt.
  - Am flachen Hintergrund ist W = 0. Dort hat {K, H} die Nullmode "konstantes N": Die globale Zeitumparametrisierung bleibt erster Klasse.
  - **Folge:** K = 0 ist auf dem Torus nur in der Naeherung kleiner Wellen eine zulaessige Eichung. In der vollen Theorie erzwingt schon eine kleine Welle N = 0. Der flache 3-Torus ist zudem linearisierungsinstabil [L, Moncrief 1975; Fischer/Marsden/Moncrief].
- **K = 0 als eigenes Gesetz (tr pi = 0, Horava-Ecke alpha = beta = 0):**
  - Die Horava-Ecke ist auf geschlossenen Raeumen nach SKALAR-SEKTOR-L der CMC-Fall K = K(T); dort wirkt lambda, und die Gleichheit mit der ART ist nicht belegt. Belastbar ist die Gleichheit nur bei asymptotisch flachem Rand [P].
  - Fuer das woertliche Gesetz tr pi = 0 gilt randfrei [M, Rechnung des dritten Lesers, nicht gegengelesen]: Der Unterschied zur ART ist c (tr pi)^2/sqrt g mit c = (lambda - 1)/(2 (3 lambda - 1)). Seine Klammer mit tr pi verschwindet auf tr pi = 0, und {tr pi(x), tr pi(y)} = 0. Der Erhalt von tr pi = 0 gibt damit die Lapse-Gleichung der ART, und das Torus-Argument greift ohne Rand.
  - Offen: die Nullmoden (konstantes N, Multiplikator der Spurbedingung).
- **Alternative 1: konstante mittlere Kruemmung K = tau(t) (CMC, York-Zeit) [L]:**
  - tau ist nur dann eine Zeit, wenn es sich von Scheibe zu Scheibe monoton aendert; dafuer muss sich das Volumen aendern. Auf dem ruhenden flachen Torus, dem Hintergrund der Rechnungen in 2.3 und 6, ist tau konstant null und keine Zeit.
  - Die Lapse-Gleichung -Laplace N + W N = d tau/dt hat bei d tau/dt > 0 eine positive Loesung, wenn der kleinste Eigenwert von -Laplace + W positiv ist; W >= 0, nicht ueberall null, reicht dafuer [L]. Wo W < 0 ist (rho + S_T < 0, siehe oben), ist das eine Pruefaufgabe.
  - Dass es eine CMC-Blaetterung gibt, ist auf geschlossenen Raeumen ein Satz mit Voraussetzungen [L, Marsden/Tipler; Gerhardt; Andersson/Moncrief]. Shape Dynamics (Gomes/Gryb/Koslowski 2011) ist dual zur ART in CMC-Eichung [L, ungeprueft].
- **Daneben: unimodulare Zeit als Zaehler, keine Scheibung (Henneaux/Teitelboim) [M, S]:**
  - Sie ist zu Lambda konjugiert; ihr Zuwachs zwischen zwei Scheiben ist das eingeschlossene 4-Volumen (Gielen/Ried 2026, 2610.03479, Gl. 36: dT = Summe der 4-Simplex-Volumina [S, GIELEN-RIED-TIEF-L]). Sie waechst bei jeder Blaetterung mit N > 0, auch auf dem ruhenden Torus (Zuwachs Volumen mal Eigenzeit) [M].
  - Sie ist aber nur ein Zaehler: Sie kennzeichnet Klassen von Scheiben gleichen 4-Volumens und legt nicht fest, welche Scheibe "jetzt" ist; der Lapse bleibt oertlich frei (Kuchar 1991 [S, ueber GIELEN-RIED-TIEF-L]). Eine Scheibung ersetzt sie deshalb nicht.
  - Als globaler Zaehler mit gleich hohen Zeltstangen rechnet REGIME-K-1 schon so [P]. Die oertliche Regel "jeder Zeltzug fuegt dasselbe 4-Volumen hinzu" macht die Zeitscheiben nach einer Rechnung des Agenten instabil (Bona-Masso f = -1; an der Quelle nur das Kriterium f > 0) [ES, H].
  - Preis: Lambda wird eine Integrationskonstante statt eines festen Werts (Abschnitt 7). Auf dem leeren, flachen Torus laufen K = 0 und die unimodulare Uhr zusammen: Bei Lambda = 0, N = 1 und Shift 0 ist K_ij = 0, das Volumen V konstant und T(t) - T(0) = V t [M, Codex]. Ausgeschlossen sind unter Lambda = 0 und W >= 0 nur nichttriviale maximale Daten mit Materie oder Wellen (dann N = 0); der Zaehler selbst ist dort nicht das Hindernis.
  - "Finns Takt zaehlt Volumen" ist eine Schreibtisch-Lesart aus WELTKRISTALL-L im gleichmaessigen 600-Zellen-Modell [M, ES], kein Rechenbefund.
- **Fuer Finns Uhren-Bild [H]:** Als Scheibung kommt die York-Zeit auf sich aenderndem Volumen in Frage; als Zaehler die unimodulare Zeit (global, mit Lambda als Integrationskonstante), die die Scheibung offen laesst. Eine globale Zeit in diesen Formen widerspraeche der ART nicht, anders als der projizierbare Horava-Fall aus SKALAR-SEKTOR-L. Pruefen (ZELT-KOMMUTATOR-2 laeuft).
- Welche Lesart der bisherige Code rechnet (er setzt H und K = 0 zusammen), muss die Algebra zeigen.
- **Energie:**
  - kein Positiv-Energie-Import
  - Auf dem Torus ist H_tot auf den Loesungen null (Form A: Summe von Zwangsbedingungen; Form B: nach Euler) [M].
  - **Stabilitaet haengt an der Paarung, nicht an der Reduktion:** Ohne wachsende Moden in den gerechneten Spektren sind bisher die zwei Paarungen A1R1 und A2R1. Mit B wachsen Moden unter R1 und unter RH, unter R2 eine Mode auf einem von vier Glasnetzen (drei Reduktionen gerechnet). Auch fuer A1R1 und A2R1 fehlt die Positivitaet auf der Eichung (1 bis 88 negative Richtungen von K auf der Eichung, HODGE-MASSE-1).
  - **Volumenmode [P, LUND-REGGE-MASSE-1]:** Fuer B mit R1 ist auf den Kristallen die globale konforme Richtung die einzige negative bei k = 0 und waechst nicht; die wachsenden Richtungen liegen am Nullkegel der lambda = 1-Form (Spuranteil 0,334 bis 0,337, von Hand 1/3). Auf Glas wachsen 28 bis 33 von 29 bis 34 negativen Richtungen.
    - Eine einzige globale Mode erklaert die negativen Richtungen im Kasten nicht (A1RH 9, A2RH 5, A2LR1 28, A2LRH 46 von 481). Lokale Spurrichtungen haben nach DeWitt ebenfalls negative Bewegungsenergie; die Pruefung ist auf sie zu erweitern.

## 5. Kruemmung und Spannung (Finn, 05.10.)

- **Schlaefli [M]:** Fuer die ungewichtete Summe gilt d(Summe_e l_e eps_e) = Summe_e eps_e dl_e, weil sich die Aenderungen der Fehlwinkel aufheben.
  - Bei raeumlich gleichem N (N = 1) gilt dH/dq_e = -eps_e/(16 pi G l_e) + (Lambda/8 pi G)(dV/dl_e)/(2 l_e). Die Kraft auf die Kante ist pdot_e = -dH/dq_e = +eps_e/(16 pi G l_e) - (Lambda/8 pi G)(dV/dl_e)/(2 l_e).
- **Bei ungleichem N** bleibt in der Ableitung von Summe_e N_e l_e eps_e der Term Summe_e' (N_e' - N_ref) l_e' d eps_e'/d l_e stehen, die diskrete Form von D_i D_j N - g Laplace N. Im Newton-Fall ist er von derselben Ordnung wie der Fehlwinkel.
- **Statischer Fall (p = 0, pdot = 0):** Die Kantengleichung bilanziert Fehlwinkel, Lapse-Term, Lambda-Term und Materiespannung. Das ist der ij-Teil der diskreten Einsteingleichung; die Hamilton-Bedingung H_v = 0 (Kruemmung gegen Energiedichte) ist eine eigene Gleichung.
- **Mit Bewegung** kommen der Bewegungsanteil (quadratisch in p), bei s ungleich 0 der Shiftterm und pdot selbst hinzu.
- **Beispiele, nur im offenen, asymptotisch flachen Raum bzw. als oertliche Bilanz:**
  - Vakuum um eine ruhende Masse (raeumliche Kruemmung ungleich null, Materiespannung null) schliesst ueber den Lapse-Term (bei Lambda ungleich 0 auch ueber den Lambda-Term).
  - Momentan ruhender Staub hat Kruemmung ohne Spannung. Er ist nicht statisch; die Kantengleichung schliesst ueber pdot ungleich 0, weil der Staub zu fallen beginnt.
  - Im Kontinuum (Lambda = 0, rho >= 0) gibt es auf T^3 nach dem T^3-Satz (Abschnitt 4) keine statische oder momentan ruhende Lage mit Materie. Fuer das Regge-Netz folgt das nicht direkt, weil dort nur eine gewichtete Fehlwinkelsumme je Ecke nicht negativ sein muss [H].
- **Lesart [L]:** Im Newton-Grenzfall steckt die Schwerkraft im ungleichen Gang der Uhren (Lapse). Abschnitt 5 leitet das nicht her.
- Eine Regel "Fehlwinkel ueber einer Schwelle wird an die Nachbarn verteilt" (Kruemmungs-Sandhaufen) waere eine **zusaetzliche** Regel und gehoert in einen eigenen SOC-Arm.
  - KRUEMMUNGS-SANDHAUFEN-2D-1 (geerntet, ohne frischen Leser): Auf der geschlossenen Kugel sind die Lawinen breiter als auf der Scheibe; das Potenzgesetz ist knapp verfehlt. Eine grobe Verzweigungszahl ~1 im Endzustand ist ein Nachtrag nach Sicht.
  - Die Folgekarte -2D-2 laeuft. Pflichtkontrolle: Schwerewellen duerfen nicht gedaempft werden.

## 6. Umklappen (erst nach den Abschnitten 2 bis 4)

- **Klasse:** periodisches Delaunay-Netz ohne Rand.
  - Das umkreisbasierte Dual einer Kante ist die Voronoi-Facette zwischen ihren Endpunkten. Ihre Flaeche ist >= 0 und = 0 bei Kosphaerizitaet, also am Zug [M; L, Hirani/Kalyanaraman/VanderZee 2013 "pairwise Delaunay"].
  - Der elektrische Term E^2/(2 *1) wird dort singulaer. Stetigkeit von M heisst nicht Stetigkeit von M^-1 [Codex].
- **Uebergabe:**
  - A, E, phi, pi und p auf das neue Kokettennetz abbilden; d respektieren; Gauss nach dem Zug erhalten, ohne Ladung zu erzeugen. Energie, symplektische Struktur und Zwangsbedingungen sind drei getrennte Bedingungen.
  - **R gegen P [P, UEBERGABE-KONFLUENZ-1, TAKT-DYNAMIK-1]:**
    - Geometrie: R ist reihenfolgefest (bis 1,6e-13), verliert aber Energie (-2,4 bis -12,7 % ueber 10 Perioden). P traegt im Impuls eine kleine Reihenfolgespur (bei disjunkten Zuegen bis 2,8e-7, insgesamt bis 1,3e-5) und gewinnt Energie (+15 bis +20 %). Statisch umkehrbar sind beide.
    - Skalar: phi bleibt bei 2-3- und 3-2-Zuegen am selben Ort, weil keine Ecke wegfaellt [M]. In R wird pi_v mit D = *0'_v/*0_v umskaliert (phi' = phi, pi' = D pi).
      - **Nicht kanonisch [M, Codex, gegengelesen]:** Fuer D ungleich I ist diese Abbildung auf dem ungekuerzten Feldraum keine kanonische Abbildung (im Feldblock {x'_i, p'_j} = D_ji), auch bei positivem diagonalem D und exakt umkehrbarer Rueckkehr. Eine Verschiebung nur der geometrischen Impulse repariert das nicht.
      - Ein kanonischer Vergleich x' = F(q) x verlangt den Kotangential-Lift p'_x = F^-T p_x und einen Rueckstoss im geometrischen Impuls, p'_q,a = p_q,a - p_xᵀ F^-1 (d_a F) x [M, Codex].
      - R aendert ausserdem die globale U(1)-Ladung und verletzt beim geladenen Skalar Gauss nach dem Zug; das verschwindet, wenn der Zug genau an der Kosphaerizitaet erfolgt (Effekt des endlichen Zeitschritts) [M, Rechnung des vierten Lesers, nicht gegengelesen]. P erhaelt Ladung und Gauss.
      - Weil 2-3-Zuege die Zahl der Kanten aendern, ist ein symplektischer Diffeomorphismus des ganzen ungekuerzten Phasenraums nicht moeglich; der Transfer im gekuerzten (physikalischen) Raum ist gesondert zu pruefen.
    - Gueltigkeit: nur Form A, nur 2-3-Startzuege, statische Paarprobe, linear um flach, N = 128, ohne Licht.
    - **Abwaegung der Leitung [H]:** Keine der beiden Lesarten erfuellt bisher alle Bedingungen; die Wahl ist offen.
  - Offen: Reihenfolge in Kaskaden (im Code entscheidet eine Sperre), Licht.
  - Drei Regime nach LAMBDA-TURING-L [ES]: kinetisch eindeutige Normalform; bei grossen Schritten in 3D kann monotones Umklappen scheitern (Joe [S Treffer]); auf dem symmetrischen Netz nur modulo Diagonalwahl.
- **Zaehlung:** Die 9 Freiheitsgrade der flachen Bipyramide (5 . 3 - 6) zaehlen weder den ganzen Regge-Phasenraum noch Materie und Licht.
- **Energiesprung:** Gerechnet (nicht gemessen): Mittel von abs(dH)/H0 je 2-3-Zug je Lauf 1,26e-3 / 3,93e-3 / 1,17e-3, hoechstens 3,1e-2; Glas N = 128, Amplitude 1e-3, Saaten s1 bis s3 (s4 ohne Zug), A2R1 [P, HODGE-MASSE-1 Tab. 4.4]. Dass allein die fehlende Uebergabe die Ursache ist, bleibt Hypothese.
- **Zugarten:** 1-4- und 4-1-Zuege aendern die Eckenzahl; Zwangsbedingungen kommen hinzu oder fallen weg. In diskreter Zeit senken 3-2- und 4-1-Zuege den Rang der Symplektik (Dittrich/Hoehn 2013, Satz 4.1) [P, REGGE-KINETIK-L]. Umkehrbare Graphdynamik erhaelt die Eckenzahl (Arrighi u. a. 2026, nur Abstract) [P, LAMBDA-TURING-L].
- **Topologie:** Pachner-Zuege tauschen eine Kugel gegen eine Kugel mit gleichem Rand und aendern die Topologie nicht [M]. Fuer Spin 1/2 aus reiner Geometrie braeuchte es spinorielle Raeume; Henkel und RP^3 sind es nicht [S, KRUEMMUNG-SPANNUNG-SPIN-L].

## 7. Bewusst draussen (spaetere, eigene Entscheidungen)

- **Unimodulares Lambda:** braucht zusaetzliche Variablen, Zwangsbedingungen und Randdaten; eine Integrationskonstante ist keine vorhergesagte kleine Zahl. Als globaler Zaehler ist die unimodulare Zeit Kandidat (Abschnitt 4); den Reihenfolgetest auf dem Netz rechnet ZELT-KOMMUTATOR-2.
- **SOC-Auswahl eines kleinen Lambda bzw. Kruemmungs-Sandhaufen:** eigener Arm (Abschnitt 5).
- **Kaehler-Dirac:** eine weitere Feld- und Quantisierungsentscheidung, kein hergeleiteter Spin-1/2-Sektor.
- **Quantisierung:** exp(iS/hbar) setzt Wirkungseinheit, Mass, Eichbehandlung und eine Messdeutung voraus; das i allein erzeugt keine Quantenmechanik.
- **Einheiten:** Eine Kantenlaenge setzt G nicht ohne Wirkungs-, Zeit- und Energienormierung.

## 8. Gesetzt gegen zu pruefen

**Gesetzt [W]:**
- Torus-Topologie, festes Delaunay-Netz (Umklappen spaeter)
- q_e als Variablen, umkreisbasierte Hodge-Sterne
- Form A mit Spurkoeffizient 1/2 als Arbeitsgeruest, lambda = 1; Alternativen B, nichtlokal, gemischt (2.3)
- Gewichte w_vt = 1/4, w_ve = 1/2; Interpolation von N (Mittel) und s (stueckweise linear)
- Zeitkonvention: gleichmaessiger Lapse-Faktor N0 = Wurzel 8 fuer alle Sektoren; Z_s/Z_t = 1, Y_s/Y_t = 1
- metrische Kopplung, neutraler Q-Ball, A nicht kompakt, G und Lambda fest

**Offen (Pruefliste, nicht geliefert):**
1. Definition von D_v, dann Algebra der Zwangsbedingungen und Zahl der Freiheitsgrade
2. globale Impulsrekonstruktion (meinen Form A und gemischte Form dieselben Kantenimpulse?)
3. Spurbindung am Code bestaetigen
4. stabile reduzierte Energie, mit Volumenmode und lokalen Spurrichtungen
5. TT-Isotropie: mit Form A ueber Symmetrie oder Vergroebern? Regime K? (REGIME-K-1)
6. Zeitscheibung jenseits linearer Ordnung: York-Zeit auf sich aenderndem Volumen; dazu die unimodulare Zeit als globaler Zaehler (ersetzt keine Scheibung); Vorzeichen von rho + S_T bei Lambda < 0, U < 0 und fuer CMC
7. Newton-Grenzfall und Lichtablenkung im selben H, mit Lapse-Term (Abschnitt 5), auf offenem bzw. sich aenderndem Hintergrund
8. Mitfuehrung (bisher IMPULS-NETZ-1, linear) und Doppelpulsar mit vollstaendiger Quelle (V1-AUFHEBUNG-1: auf V mit abgestimmten Gewichten vertraeglich)
9. gleiche schwere Masse einschliesslich Bindungsenergie; kleines Lambda
10. Uebergaberegel beim Umklappen: R gegen P je Sektor, Kaskaden, Licht

## 9. Reihenfolge (Vorschlag)

1. Die letzte Schicht (2.3 auf 2.4) bei der naechsten Fassung mit lesen lassen.
2. Ergebnisse von REGIME-K-2 (gefuelltes V in 4D-Zeit) und ZELT-KOMMUTATOR-2 (Reihenfolge, unimodulare Uhr) abwarten.
3. Algebra-Karte mit drei Vorbedingungen: D_v zuerst definieren; {H_v, H_w} mindestens in erster Ordnung in p oder um einen Hintergrund mit p ungleich 0 (die lineare Ordnung ist blind fuer A gegen B); Nullmoden auf dem Torus gesondert. Dazu Codex' Zwei-Tetraeder-Probe (relative Lapse, Lapse-Hesse) und eine Probe des gewichteten Schlaefli-Terms.
4. Neutraler Q-Ball plus Maxwell im selben H auf festem Netz: Spannungskopplung, schwere Masse, Vorzeichen von rho + S_T.
5. Uebergaberegel beim Umklappen (Abwaegung R gegen P je Sektor), Kaskaden-Reihenfolge.
6. Danach SOC-Arm (nach KRUEMMUNGS-SANDHAUFEN-2D-2), Kaehler-Dirac, Quantisierung.

## Einfach gesagt

Fassung 2.3 schreibt auf, was in die Grundgleichung gehoert und was noch fehlt, bevor man sie ganz nachrechnen kann, vor allem die Regel fuer das Verschieben der Ecken. Mit der Traegheit aus der Literatur liefen Schwerewellen in unseren Rechnungen bisher nur unter einer bestimmten Eckenregel richtungsgleich; Stoerungen wuchsen dabei unter zwei von drei gerechneten Eckenregeln, unter der dritten nur vereinzelt. Deshalb wird jetzt geprueft, ob die Bewegungsenergie aus einer vierdimensionalen Wirkung folgen kann. In einer ruhenden Lage im offenen Raum halten sich Kruemmung, das Gefaelle im Gang der Uhren, Lambda und die Spannung der Materie die Waage. Fuer die Uhr gibt es zwei Ansaetze: Zeitscheiben, in denen der Raum gleichmaessig waechst oder schrumpft, oder einen Zaehler, der das vierdimensionale Volumen addiert. Der Zaehler laeuft auch in einem ruhenden, geschlossenen Raum weiter, legt aber nicht fest, welche Raumscheibe gerade "jetzt" ist.
