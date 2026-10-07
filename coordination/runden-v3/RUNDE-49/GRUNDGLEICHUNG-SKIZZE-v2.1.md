# Grundgleichung fuer Finns Netz: gewaehlte Architektur und offene Folgerungen (Fassung 2.1)

- Leitung claude-primary, geschrieben ab 2026-10-05 11:45:21 CEST (date).
- **Grundlage:**
  - Fassung 2 (RUNDE-48/GRUNDGLEICHUNG-SKIZZE-v2.md; bleibt unveraendert als Lesestand)
  - frischer Leser zu Fassung 2 (RUNDE-37/grundgleichung-v2-leser/BEFUNDE.md: 7 A, 13 B, 7 C)
  - Codex' Gegenblick zu Fassung 2 (codex-ideation-20261005/GRUNDGLEICHUNG-v2-GEGENBLICK.md: 5 Punkte)
  - Ernten seit Fassung 2: LUND-REGGE-MASSE-1, V1-AUFHEBUNG-1, KRUEMMUNG-SPANNUNG-SPIN-L, LAMBDA-TURING-L (RUNDE-48.md)
- **Status:** Schreibtisch [ES], noch kein frischer Leser. Nichts hier ist ein Ergebnis. Was "entstehen soll", ist eine Pruefliste, nicht geliefert. Alle Projektbezuege sind Modellrechnungen, keine Messdaten.
- Kennzeichen: [M] Mathematik, [P] Projektbefund, [S] Literatur an der Quelle, [L] Gedaechtnis (ungeprueft), [ES] Schreibtisch, [H] Hypothese, **[W]** Modellentscheidung (gesetzt, nicht hergeleitet).
- **Begriffe (Leser C1):** "Takt-Operator" T = 8 d0ᵀ *1 d0; "maximale Scheibung" K = 0; "globaler Lapse" ein N fuer alle Zellen. Das Wort "Takt" allein wird hier nicht mehr benutzt.

## 0. Stand der Einarbeitung

- **Codex zu Fassung 1 (fuenf Punkte):** alle angenommen.
  - Punkte 3, 4 und 5 sind eingearbeitet.
  - Punkt 2 (gemeinsame Zeiteinheit) ist jetzt in den Formeln (Abschnitt 3.1).
  - Punkt 1 ist teilweise eingearbeitet: Shift-Interpolation (Abschnitt 1) und Spurbindung (2.2) ja. **D_v ist weiter nur benannt** (2.4).
- **Leser und Codex zu Fassung 2:** alle sieben A-Befunde eingearbeitet; die fuenf Codex-Punkte aufgenommen, offen bleiben D_v und die globale Impulsrekonstruktion (Codex 4); B- und C-Befunde soweit unten vermerkt.
  - Wichtigste Berichtigungen:
    - Die zwei "nur" in 2.3 waren falsch.
    - K = 0 ist auf dem geschlossenen Torus nur linear zulaessig.
    - "Kruemmung = Spannung" gilt nur bei gleichem N.
    - Die Zahlen belegen keinen Gegensatz "Zwangsstruktur gegen Isotropie".

## 1. Zustand (feste Topologie, festes Netz)

- Raum: 3-Torus (periodisch), feste Zerlegung T, alle Tetraeder nicht entartet, Delaunay [W]. Umklappen kommt erst in Abschnitt 6 dazu.
- Kanonische Paare:
  - Geometrie: q_e = l_e^2 und p^e (Kanten)
  - Licht: A_e und E^e (Kanten; A reell und nicht kompakt [W])
  - Materie: phi_v und pi_v (Ecken, komplex; Normierung in 3.2)
- Multiplikatoren an den Ecken: Lapse N_v, Shift s_v, A0_v (Gauss).
- **Interpolation [W]:**
  - N_t, N_e, N_f sind Mittel der Ecken von t, e bzw. f.
  - Der Shift ist das stueckweise lineare Vektorfeld aus den Eckwerten s_v. Ein je Zelle konstanter Wert gaebe L_s g = 0 (Leser A6).

## 2. Eine kanonische Konvention (Phasenraumform)

### 2.1 Wirkung

S = Integral dt [ Summe_e p^e dq_e/dt + Summe_e E^e dA_e/dt + Summe_v (pi_v dphi_v/dt + c.c.) - H_tot ]

H_tot = Summe_v N_v H_v + Summe_v s_v . D_v + Summe_v A0_v G_v

- H_v und G_v sind unten definiert, D_v nur als Anforderung (2.4).
- Das Schema loest die Algebra der Zwangsbedingungen nicht (Abschnitt 4).

### 2.2 Geometrie in H_v (ADM-Vorzeichen)

- **Kontinuum [L, Standard-ADM; vom Leser nachgerechnet, R1]:** H = (16 pi G/sqrt g)(pi:pi - (1/2)(tr pi)^2) - (sqrt g/16 pi G)(R - 2 Lambda).
- **Netz:** Integral sqrt(g) R = 2 Summe_e l_e eps_e (Regge), Integral sqrt(g) = Summe_t V_t.
- **Bewegungsanteil, Form A [W]:** 16 pi G Summe_t w_vt (1/V_t) [pi_t:pi_t - (1/2)(tr pi_t)^2]
  - Das ist eine **Setzung**, keine Uebersetzung (Leser B1, Codex 2).
    - Im Kontinuum steht in jeder Zelle ihr **Anteil** Pi_t am Impuls.
    - Ein Kantenimpuls p^e ist aber die Summe der Beitraege aller Zellen um e. Form A setzt in jede Zelle den vollen p^e (Zellimpuls aus den sechs Kantenimpulsen der Zelle).
    - Je Zelle ist Form A die Umkehrung der geschwindigkeitsseitigen Form h:h - (tr h)^2. Global nicht: Die Summe lokaler Inversen ist nicht die Inverse der Assemblierung.
  - **Spurkoeffizient 1/2** = lambda/(d lambda - 1) bei lambda = 1, d = 3 [M].
    - Bindung im Code [P, mit Vorbehalt]: HODGE-MASSE-1 meldet A2_t K_t = 1 auf 1,6e-9 mit der lambda = 1-Form K_t. Dann ist A2 je Zelle deren Inverse mit Spurkoeffizient 1/2.
    - Am Code zu bestaetigen (Leser B8).
  - Masse ~ Volumen ist die Projektvariante A2; A1 ist dieselbe Zellform ohne Volumengewicht.
  - Bei gleichmaessiger Rate trifft A2 den Kontinuumswert nicht (1,02 bis 1,36, spurfrei 0,019 bis 0,039), die Lund-Regge-Form schon (1,2e-13) [P, HODGE-MASSE-1 HM0].
- **Kruemmungsanteil:** -(1/8 pi G) Summe_e w_ve l_e eps_e + (Lambda/8 pi G) Summe_t w_vt V_t
  - Die positiv benannte Regge-Summe steht mit **Minus** in H, wie -sqrt(g) R.
- **Gewichte [W]:** w_vt = 1/4, w_ve = 1/2 fuer die Ecken von t bzw. e. Summe_v N_v w_vt = N_t.

### 2.3 Lapse-Abhaengigkeit der Traegheit [M, ES; mit Leser und Codex berichtigt]

- **Form A** ist linear in N. Ihre N-Variation liefert N-freie Zwangsfunktionen H_v.
  - Ob diese erster Klasse sind, ist offen (Abschnitt 4). Auch Form A kann am Ende N festlegen (Leser B6, Codex 2).
- **Form B** (geschwindigkeitsseitig nach Lund-Regge, Literaturstandard; im Projekt A2L):
  - L_kin = Summe_t (1/(2 N_t)) vᵀ M_t v mit v = qdot - B s. Die Legendre-Umkehr gibt (1/2) pᵀ M(N)^-1 p + pᵀ B s mit M(N) = Summe_t M_t/N_t [M].
  - **Bedingungen** (Leser B2, B3):
    - M(N) muss fuer alle zugelassenen N invertierbar sein. M_t ist indefinit (DeWitt mit lambda = 1 in 3D: Signatur (5,1)); bei entartetem M erst der Dirac-Algorithmus.
    - Der Shift wirkt als gemeinsame Kantengeschwindigkeit B s. Bei zellweise verschiedenen B_t wird H quadratisch in s.
  - **Homogen vom Grad 1 [M]:** M(sN) = M(N)/s, also H(sN) = s H(N). B ist damit linear entlang jedes Strahls N = s(t) N̂, mit beliebigem festen Profil N̂. Der globale Lapse ist nur der Sonderfall N̂ = 1 (Leser A1).
  - **Generisch nichtlinear [M]:** Zwei Zellen mit einer gemeinsamen Kante geben H = p^2 N1 N2/(2 (N1 + N2)). Unabhaengige Bloecke ohne gemeinsame Kante sind dagegen linear (Codex 1). Im zusammenhaengenden Regge-Netz teilen Zellen Kanten.
  - **Zwangsbedingungen bei B [M, H]:**
    - C_v = dH/dN_v ist homogen vom Grad 0, haengt also nur von den Verhaeltnissen N_v/N_w ab.
    - Nach Euler gilt Summe_v N_v C_v = H. Eine globale Bedingung bleibt; generisch legen die Gleichungen die V - 1 Verhaeltnisse fest (Leser B5) [H, zu pruefen].
    - Friedman/Jack 1986: Lapse und Shift je Simplex werden durch Konsistenz bestimmt, wenn vorab gewaehlte Multiplikatoren die Bedingungen nicht erhalten [P, REGGE-KINETIK-L, nur Abstract]. Gambini/Pullin ("consistent discretizations") [L].
- **Weitere lineare Formen:**
  - **Nichtlokal [M, Leser A1]:** (1/2) Summe_e N_e p^e (M^-1 p)_e ist linear in N und bei gleichem N gleich B. Der Preis ist Nichtlokalitaet: M^-1 ist dicht, und wie schnell es abfaellt, ist offen (M indefinit). Die Stabilitaet ist bei gleichem N die von B.
  - **Gemischte Form [M, Codex 2]:** L = Summe_t [P_tᵀ B_t v - (N_t/2) P_tᵀ G_t^-1 P_t] mit unabhaengigen Zellimpulsen P_t und der Kopplung p = Summe_t B_tᵀ P_t. Sie ist vor der Elimination linear in N und macht die fehlenden Abgleichbedingungen sichtbar. Ein Trick fuer erste Klasse ist das nicht.
- **Was die Rechnungen zeigen [P; HODGE-MASSE-1 Tab. 4.2, LUND-REGGE-MASSE-1]:**
  - Ohne wachsende Moden auf allen sieben gerechneten Netzen und im Umklapp-Kasten sind nur A1R1 und A2R1. Sie sind richtungsabhaengig (V: 6,34 % bzw. 5,92 %).
  - B mit RH ist bis auf ~1e-7 TT-isotrop (S, A15; V nicht trennbar, Ritz 3,16 %; Glas Ritz 3,5e-6 bis 7,7e-6). Es hat aber wachsende Moden: je 1 auf V, S und A15, 46 bis 50 auf Glas.
  - B mit R1 ist auf den Kristallen bei kleinem k regulaer, aber anisotrop (V 10,6 %, S 0,74 %, A15 4,7 %). Bei grossem k waechst es (V an 142 von 511 k), auf Glas an jedem k (27 bis 33 Moden).
    - Die Anisotropie sitzt dort in der Partnerbedingung c^+ p = 0 der skalaren Regel, nicht in der Masse (Masse bei gleichmaessiger Rate exakt kontinuumsgleich) [P, LUND-REGGE-MASSE-1].
  - Auf Glas wachsen Moden mit RH (A1, A2, A2L) und mit A2LR1 in jedem Netz, mit A2LR2 in einem von vier (Leser A2). Ob Splitter die Ursache sind, prueft SPLITTER-FREI-1 (laeuft).
- **Was daraus folgt [H, eingeschraenkt]:**
  - Gerechnet ist nur: Isotropie ohne Abstimmung gab es bisher nur mit B und RH, und dort wachsen Moden.
  - "B ist nicht linear in N" ist eine Strukturaussage, die keine dieser Rechnungen beruehrt. Um p = 0, N = 1 geht die N-Abhaengigkeit des Bewegungsterms erst in dritter Ordnung ein (Leser B4, R4).
  - Die Spektren belegen einen Konflikt der getesteten Paarungen, keinen allgemeinen Ausschluss. R1 und RH gehoeren zu verschiedenen Constraintpaaren (Codex 3).
- **Auswege [H]:**
  - (i) Form A als Geruest, Isotropie aus Symmetrie (DANZER-TT-1 laeuft) oder aus Vergroebern.
  - (ii) Regime K (REGIME-K-1 laeuft): Die Bewegungsenergie folgt aus der 4D-Regge-Wirkung. In 4D-Regge legen die Gleichungen die Zeltstangen (den diskreten Lapse) abseits flacher Loesungen in der Regel fest [L, Bahr/Dittrich; Dittrich/Hoehn]. (ii) ersetzt die gesetzte Bewegungsenergie, beantwortet aber die Frage nach einem freien Lapse nicht (Leser B11).
  - (iii) nichtlokale lineare Kopplung (oben), konstruierbar.
  - (iv) gemischte Form mit Zellimpulsen (Codex 2).

### 2.4 Verschiebung und Gauss

- **D_v [ES, offen]:** D_v soll die Verschiebung der Ecke v erzeugen und auf **alle** Variablen wirken (q ueber die Kantenvektoren, phi und A ueber ihren Transport). Die Form steht aus. Linear am flachen Netz ist sie die Impulsregel aus IMPULS-NETZ-1 [P].
  - Abseits von flach bricht Regge die Verschiebungssymmetrie (Bahr/Dittrich) [S].
- **G_v** = (d0ᵀ E)_v - rho_v, im neutralen Arm rho = 0. {G_v, G_w} = 0, und H haengt von A nur ueber d1 A ab (d1 d0 = 0) [M].

## 3. Materie und Licht

### 3.1 Eine Zeiteinheit fuer alle Sektoren [W; Leser A3]

- **Setzung:** Die 8 aus dem Takt-Operator ist ein **gleichmaessiger Lapse-Faktor N0 = Wurzel 8 fuer alle Sektoren**.
  - Ein konstanter Lapse-Faktor ist eine Zeiteinheit: Er skaliert alle omega^2 gleich mit N0^2 [M].
  - Kaeme die 8 dagegen ueber das Verhaeltnis Z_s/Z_t allein in den Skalar, aenderte sie mit einem Potential die Compton-Laenge in Netzeinheiten, also Physik (omega^2 = (Z_s/Z_t) k^2 + U'(0)/Z_t).
- **Skalar:** Z_s/Z_t = 1 [W]. Dann gilt Z_t *0 phi'' = -N0^2 Z_t d0ᵀ *1 d0 phi - ... = -Z_t T phi - ...
- **Licht:** dieselbe Konvention, Y_s/Y_t = 1 [W]. Mit N0 gilt *1 A'' = -N0^2 d1ᵀ *2 d1 A, langwellig omega^2 = N0^2 k^2.
- **Geometrie:** N0 steht vor H_v. Im ADM-Kontinuum kuerzt sich G, also omega^2 = N0^2 k^2. Fuer Form A ist selbst das unsicher, weil sie den Kontinuumswert der Bewegungsenergie verfehlt (2.2).
- **Folge [M, P]:** Langwellig haben Skalar und Licht mit diesen Setzungen dieselbe Grundgeschwindigkeit N0 (Netzeinheiten), richtungsgleich auf jedem periodischen Delaunay-Netz.
  - Grund fuer die Richtungsgleichheit: Mit umkreisbasierten Dualzellen sind lineare Funktionen diskret harmonisch (geschlossene Dualzellen), und es gilt Summe *1 l lᵀ = Vol I [M; Leser R5; P DANZER-NAEHERUNG-2].
  - Die Gleichheit **zwischen** den Sektoren folgt aus der gemeinsamen Setzung, nicht aus der Hodge-Struktur.
  - Rang 2 erzwingt nicht Rang 4. Fuer Schwerewellen ist die Richtungsgleichheit damit offen (2.3).

### 3.2 Erster Arm: neutral [W]

- **Skalar (Q-Ball, globale U(1)):** komplexes Feld mit L = Z_t *0 |phidot|^2 - Z_s Summe_e *1_e |phi_a - phi_b|^2 - *0 U(S), S = |phi|^2.
  - pi = Z_t *0 phidot* (konjugiert), H^phi = Summe_v N_v [ |pi_v|^2/(Z_t *0_v) + *0_v U(S_v) ] + Summe_e N_e Z_s *1_e |phi_a - phi_b|^2.
  - Das ist dieselbe Normierung wie das reelle 1/2-Schema fuer phi = (phi1 + i phi2)/Wurzel 2 [M; Codex 4].
- **Licht:** H^EM = Summe_e N_e (E^e)^2/(2 *1_e) + Summe_f N_f *2_f (d1 A)_f^2/2. Der elektrische Term braucht *1_e > 0 (Abschnitt 6).
- **Kopplung an die Geometrie:**
  - ueber die l-Abhaengigkeit von *0, *1, *2 und V; das ist eine gesetzte metrische Kopplung [W], kein hergeleitetes Aequivalenzprinzip
  - Die Materiespannung an einer Kante ist die Ableitung des Materieteils nach q_e, aus demselben H [ES].
  - Gleiche schwere und traege Masse einschliesslich Bindungsenergie ist ein eigener Test (Codex Rang 8).

### 3.3 Zweiter Arm: geladen (anderes Modell)

- Linktransport |phi_a - U_ab phi_b|^2 mit U_ab = exp(i e A_e), zeitliche kovariante Ableitung mit A0; rho_v aus den kanonischen Materieimpulsen derselben Wirkung.
- Profile, Ladungsbereiche, Stabilitaet und Bindungsbefunde des Q-Balls gelten dort nicht ohne neuen Nachweis [Codex].

## 4. Zwangsbedingungen

- **Wahl [W]: ungefixtes Eichmodell.** N_v, s_v und A0_v sind freie Multiplikatoren.
- **Zu berechnen:** Poisson-Matrix von {H_v, D_v, G_v}, Erhaltung unter H_tot, Null- und Randmoden auf dem Torus. Erster Klasse: gut. Zweiter Klasse: Dirac-Klammer, Freiheitsgrade zaehlen.
- **Bekannt:**
  - Gauss ist abelsch und mit eichinvariantem H vertraeglich [M].
  - Die Impulsregel ist linear am flachen Hintergrund erster Klasse [P, IMPULS-NETZ-1]. "Linear" ist ein Zwischenziel.
  - Die skalare Regel ist offen.
- **Maximale Scheibung K = 0 auf dem Torus [M; Leser A4, Codex 4]:**
  - Die Lapse-Gleichung lautet Laplace N = N W mit W = K:K + 4 pi G (rho + S) - Lambda (Form und Vorzeichen vom Leser nachgerechnet).
  - Auf dem geschlossenen Torus folgt durch Multiplizieren mit N und Integrieren: -Integral |grad N|^2 = Integral W N^2.
    - Bei Lambda = 0 und W >= 0, nicht ueberall null (eine Schwerewelle genuegt), bleibt nur N = 0. Die Zeit stuende still.
    - Diskret gilt dasselbe, solange d0ᵀ *1 d0 positiv semidefinit ist (*1 >= 0).
    - Bei Lambda ungleich 0 gibt es N ungleich 0 nur, wenn 0 Eigenwert von Laplace - W ist, also nicht generisch. Der flache ruhende Torus ist dann zudem keine Loesung.
  - Am flachen Hintergrund ist W = 0. Dort hat {K, H} die Nullmode "konstantes N": Die globale Zeitumparametrisierung bleibt erster Klasse.
  - **Folge:** K = 0 ist auf dem Torus nur linear um den ruhenden flachen Hintergrund eine zulaessige Eichung. Der flache 3-Torus ist zudem linearisierungsinstabil [L, Moncrief 1975; Fischer/Marsden/Moncrief].
  - Die uebliche Wahl auf geschlossenen Raeumen ist konstante mittlere Kruemmung K = tau(t) (CMC, York-Zeit) mit inhomogener Lapse-Gleichung [L].
  - **Fuer Finns Takt-Bild [H]:** Als maximale Scheibung traegt er auf dem Torus nur kleine Wellen. Kandidat fuer mehr ist die York-Zeit, eine globale Zeitfunktion auf geschlossenen Raeumen. Shape Dynamics (Gomes/Gryb/Koslowski 2011) ist dual zur ART in CMC-Eichung [L]. Eine globale Zeit in dieser Form widerspraeche der ART dann nicht, anders als der projizierbare Horava-Fall aus SKALAR-SEKTOR-L [L, ungeprueft]. Pruefen.
- **K = 0 als eigenes Gesetz (Horava-Ecke alpha = beta = 0, SKALAR-SEKTOR-L):** formal ein anderes Zwangssystem. Mit asymptotisch flachem Rand ist es nach SKALAR-SEKTOR-L loesungsgleich mit der ART in maximaler Scheibung (Jacobson/Pulakkat 2025) [P]. Auf dem Torus ist das offen (Leser B9).
- Welche Lesart der bisherige Code rechnet (er setzt H und K = 0 zusammen), muss die Algebra zeigen.
- **Energie [Leser B10]:**
  - kein Positiv-Energie-Import
  - Auf dem Torus ist H_tot auf den Loesungen null (Form A: Summe von Zwangsbedingungen; Form B: nach Euler) [M].
  - Die Stabilitaetstests pruefen das Vorzeichen der quadratischen reduzierten Energie fuer zwei Reduktionen. Sie widersprechen sich (R1 stabil, RH nicht). "Die" reduzierte Energie ist damit noch nicht bestimmt.
  - Die globale Volumenmode hat nach DeWitt negative Bewegungsenergie; in der ART ist sie der Skalenfaktor [L, Moncrief]. Negative Richtungen bei k = 0 sind vor der Deutung "Instabilitaet" auf sie zu pruefen.

## 5. Kruemmung und Spannung (Finn, 05.10.) [M; Leser A5, Codex 4]

- **Schlaefli:** Fuer die ungewichtete Summe gilt d(Summe_e l_e eps_e) = Summe_e eps_e dl_e, weil sich die Aenderungen der Fehlwinkel aufheben.
  - Bei raeumlich gleichem N ist die Kantenkraft des Kruemmungsanteils deshalb proportional zum Fehlwinkel: nach q_e = l_e^2 gleich -eps_e/(16 pi G l_e). Dazu kommt der Lambda-Beitrag (Lambda/8 pi G) dV/dl_e.
- **Bei ruhender Materie ist N nicht gleich** (etwa 1 + Newton-Potential). Dann bleibt in der Ableitung von Summe_e N_e l_e eps_e der Term Summe_e' (N_e' - N_ref) l_e' d eps_e'/d l_e stehen. Das ist die diskrete Form von D_i D_j N - g Laplace N, gleich gross wie der Fehlwinkel.
  - Beispiele: Vakuum um eine ruhende Masse (raeumliche Kruemmung ungleich null, Materiespannung null) schliesst nur ueber diesen Lapse-Term; ruhender Staub hat Kruemmung ohne Spannung.
- **Folge:** Erst Fehlwinkel, Lapse-Term (Uhrengefaelle) und Materiespannung zusammen ergeben die diskrete Einsteingleichung. Der Schwerkraft-Anteil steckt also im ungleichen Gang der Uhren.
- Eine Regel "Fehlwinkel ueber einer Schwelle wird an die Nachbarn verteilt" (Kruemmungs-Sandhaufen) waere eine zusaetzliche Regel. Sie gehoert in einen eigenen SOC-Arm (KRUEMMUNGS-SANDHAUFEN-2D-1 laeuft, 2D-Vorstufe). Pflichtkontrolle: Schwerewellen duerfen nicht gedaempft werden.

## 6. Umklappen (erst nach den Abschnitten 2 bis 4)

- **Klasse:** periodisches Delaunay-Netz ohne Rand.
  - Das umkreisbasierte Dual einer Kante ist die Voronoi-Facette zwischen ihren Endpunkten. Ihre Flaeche ist >= 0 und = 0 bei Kosphaerizitaet, also am Zug [M, Leser R8; L, HKV 2013 "pairwise Delaunay"].
  - Der elektrische Term E^2/(2 *1) wird dort singulaer. Stetigkeit von M heisst nicht Stetigkeit von M^-1 [Codex].
- **Uebergabe:**
  - A, E, phi, pi und p auf das neue Kokettennetz abbilden; d respektieren; Gauss nach dem Zug erhalten, ohne Ladung zu erzeugen.
  - Energie, symplektische Struktur und Zwangsbedingungen sind drei getrennte Bedingungen.
  - Reihenfolge zweier gleichzeitiger Zuege: UEBERGABE-KONFLUENZ-1 laeuft. Bekannt sind drei Regime (LAMBDA-TURING-L): kinetisch eindeutige Normalform; bei grossen Schritten in 3D nicht eindeutig (Joe); auf dem symmetrischen Netz nur modulo Diagonalwahl.
- **Zaehlung:** Die 9 Freiheitsgrade der flachen Bipyramide (5 . 3 - 6) zaehlen weder den ganzen Regge-Phasenraum noch Materie und Licht.
- **Energiesprung:**
  - Gerechnet (nicht gemessen): Mittel von abs(dH)/H0 je 2-3-Zug je Lauf 1,26e-3 / 3,93e-3 / 1,17e-3, hoechstens 3,1e-2. Glas N = 128, Amplitude 1e-3, Saaten s1 bis s3 (s4 ohne Zug), A2R1 [P, HODGE-MASSE-1 Tab. 4.4; Leser B12].
  - Dass allein die fehlende Uebergabe die Ursache ist, bleibt Hypothese.
- **Zugarten:** 1-4- und 4-1-Zuege aendern die Eckenzahl; Zwangsbedingungen kommen hinzu oder fallen weg. In diskreter Zeit senken 3-2- und 4-1-Zuege den Rang der Symplektik (Dittrich/Hoehn 2013, Satz 4.1) [P, REGGE-KINETIK-L; Leser C6]. Umkehrbare Graphdynamik erhaelt die Eckenzahl (Arrighi u. a. 2026, nur Abstract) [P, LAMBDA-TURING-L].
- **Topologie:** Pachner-Zuege tauschen eine Kugel gegen eine Kugel mit gleichem Rand und aendern die Topologie nicht [M]. Topologieaenderung braucht eine weitere Zugart.
  - Fuer Spin 1/2 aus reiner Geometrie braeuchte es spinorielle Raeume; Henkel und RP^3 sind es nicht [S, KRUEMMUNG-SPANNUNG-SPIN-L].

## 7. Bewusst draussen (spaetere, eigene Entscheidungen)

- **Unimodulares Lambda:** braucht zusaetzliche Variablen, Zwangsbedingungen und Randdaten; eine Integrationskonstante ist keine vorhergesagte kleine Zahl.
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
- Zeiteinheit: gleichmaessiger Lapse-Faktor N0 = Wurzel 8 fuer alle Sektoren; Z_s/Z_t = 1, Y_s/Y_t = 1
- metrische Kopplung, neutraler Q-Ball, A nicht kompakt, G und Lambda fest

**Offen (Pruefliste, nicht geliefert):**
1. Definition von D_v, dann Algebra der Zwangsbedingungen und Zahl der Freiheitsgrade
2. Spurbindung am Code bestaetigen
3. stabile reduzierte Energie (globale Volumenmode gesondert)
4. TT-Isotropie: mit Form A nur ueber Symmetrie oder Vergroebern? Regime K? (DANZER-TT-1, REGIME-K-1)
5. Zeitscheibung auf dem Torus jenseits linearer Ordnung (CMC bzw. York-Zeit statt K = 0)
6. Newton-Grenzfall und Lichtablenkung im selben H, mit Lapse-Term (Abschnitt 5)
7. Mitfuehrung (bisher IMPULS-NETZ-1, linear) und Doppelpulsar mit vollstaendiger Quelle (V1-AUFHEBUNG-1: auf V mit abgestimmten Gewichten vertraeglich)
8. gleiche schwere Masse einschliesslich Bindungsenergie; kleines Lambda

## 9. Reihenfolge (Vorschlag)

1. Frischer Leser fuer Fassung 2.1.
2. Ergebnisse von REGIME-K-1 und DANZER-TT-1 abwarten.
3. Algebra-Karte mit drei Vorbedingungen (Leser B13):
   - D_v zuerst definieren.
   - Die lineare Ordnung ist blind fuer A gegen B: {H_v, H_w} mindestens in erster Ordnung in p oder um einen Hintergrund mit p ungleich 0.
   - Nullmoden auf dem Torus (konstantes N, globale Verschiebung) gesondert fuehren.
   - Dazu Codex' Zwei-Tetraeder-Probe (relative Lapse, Lapse-Hesse) und eine Probe des gewichteten Schlaefli-Terms.
4. Neutraler Q-Ball plus Maxwell im selben H auf festem Netz: Spannungskopplung und schwere Masse.
5. Uebergaberegel beim Umklappen (nach UEBERGABE-KONFLUENZ-1).
6. Danach SOC-Arm (nach KRUEMMUNGS-SANDHAUFEN-2D-1), Kaehler-Dirac, Quantisierung.

## Einfach gesagt

Fassung 2.1 schreibt auf, was in die Grundgleichung gehoert und was noch fehlt, bevor man sie ganz nachrechnen kann, vor allem die Regel fuer das Verschieben der Ecken. Die Traegheit aus der Literatur macht Schwerewellen nur zusammen mit einer bestimmten Eckenregel richtungsgleich, und genau dann schaukeln sich Stoerungen auf. Deshalb wird jetzt eine echte vierdimensionale Zeit geprueft. Kruemmung und Spannung halten sich in der Feldgleichung die Waage; bei ruhender Materie gehoert der unterschiedliche Gang der Uhren dazu. Finns Takt als "maximale Zeitscheiben" traegt auf einem geschlossenen Raum nur kleine Wellen; fuer mehr braucht es eine Zeit, in der der Raum ueberall gleich schnell waechst oder schrumpft.
