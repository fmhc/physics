# Grundgleichung fuer Finns Netz: gewaehlte Architektur und offene Folgerungen (Fassung 2)

- Leitung claude-primary, geschrieben ab 2026-10-05 10:41:11 CEST (date).
- **Grundlage:**
  - Fassung 1 (GRUNDGLEICHUNG-SKIZZE-v1.md, 10:17)
  - Codex' Gegenblick (codex-ideation-20261005/GRUNDGLEICHUNG-GEGENBLICK.md, 10:21): fuenf Punkte, alle uebernommen
  - Ernten nach Fassung 1: HODGE-MASSE-1, REGGE-KINETIK-L, SKALAR-MISCH-1, GLAS-STRAHLUNG-1 (RUNDE-48.md)
  - Finns Frage "Was ist wenn Krümmung zu Spannung wird und umgekehrt?"
- **Status:** Schreibtisch [ES], noch kein frischer Leser. Nichts hier ist ein Ergebnis. Was "entstehen soll", ist eine Pruefliste, nicht geliefert. Alle Projektbezuege sind Modellrechnungen, keine Messdaten.
- Kennzeichen: [M] Mathematik, [P] Projektbefund, [S] Literatur an der Quelle, [L] Gedaechtnis, [ES] Schreibtisch, [H] Hypothese, **[W]** Modellentscheidung (gesetzt, nicht hergeleitet).

## 0. Was sich gegenueber Fassung 1 aendert

| Codex-Punkt | Aenderung in Fassung 2 |
|---|---|
| 1. keine eindeutige kanonische Konvention | Eine Phasenraumform mit allen Multiplikatoren (N, s, A0), ADM-Vorzeichen und Spurkoeffizient 1/2 auf der Impulsseite (Abschnitt 2). Neu dabei: Nur die impulsseitige Form je Zelle macht H linear in N (Abschnitt 2.3). |
| 2. "eine Hodge-Struktur" legt nicht alles fest | lambda, Zeit-Normierungen Z je Sektor, Faktor 8 und metrische Kopplung sind als [W] markiert, nicht als emergent (Abschnitt 3 und 8). |
| 3. Erstklassigkeit, K = 0 und Positivitaet vermengt | Gewaehlt: ungefixtes Eichmodell; K = 0 ist darin eine Eichfixierung (Paar zweiter Klasse); kein Positiv-Energie-Import (Abschnitt 4). |
| 4. Ladungskopplung fehlt in den Formeln | Erster Arm neutral (globale U(1)); geladener Arm als eigenes, geaendertes Modell mit Linktransport (Abschnitt 3.3). |
| 5. Umklappen und spaetere Zutaten ueberversprochen | Umklappen erst nach festem Netz; Mass null am Zug, E^2/*1 singulaer, Gauss nach dem Zug als Pflicht. Lambda-Dynamik, SOC, Kaehler-Dirac und Quantisierung sind ausgelagert (Abschnitte 6 und 7). |

## 1. Zustand (Fassung 2: feste Topologie, festes Netz)

- Raum: 3-Torus (periodisch), feste Zerlegung T, alle Tetraeder nicht entartet [W]. Umklappen kommt erst in Abschnitt 6 dazu.
- Kanonische Paare:
  - Geometrie: q_e = l_e^2 und p^e (Kanten)
  - Licht: A_e und E^e (Kanten; A reell und nicht kompakt [W])
  - Materie: phi_v und pi_v (Ecken, komplex)
- Multiplikatoren (Ecken): Lapse N_v, Shift s_v, A0_v (Gauss).
- Interpolation [W]: N_t = Mittel der 4 Ecken von t, N_e = Mittel der 2 Ecken von e, N_f = Mittel der 3 Ecken von f. Andere Wahlen sind moeglich und muessen dann genannt werden.

## 2. Eine kanonische Konvention (gewaehlt: Phasenraumform)

### 2.1 Wirkung

S = Integral dt [ Summe_e p^e dq_e/dt + Summe_e E^e dA_e/dt + Summe_v (pi_v dphi_v/dt + c.c.) - H_tot ]

H_tot = Summe_v N_v H_v + Summe_v s_v . D_v + Summe_v A0_v G_v

H_v, D_v und G_v werden unten definiert. Dieses Schema allein loest ihre Algebra nicht (Abschnitt 4).

### 2.2 Geometrie in H_v (ADM-Vorzeichen)

Im Kontinuum gilt H = (16 pi G / sqrt g)(pi:pi - (1/2)(tr pi)^2) - (sqrt g / 16 pi G)(R - 2 Lambda) [L, Standard-ADM]. Mit Integral sqrt(g) R = 2 Summe_e l_e eps_e (Regge) und Integral sqrt(g) = Summe_t V_t wird daraus auf dem Netz [ES]:

- **Bewegungsanteil (Form A, impulsseitig je Zelle):** 16 pi G Summe_t w_vt (1/V_t) [pi_t:pi_t - (1/2)(tr pi_t)^2]
  - pi_t ist der Impulstensor der Zelle t, rekonstruiert aus den sechs Kantenimpulsen; die Abbildung ist je Zelle linear und umkehrbar [M].
  - Der Spurkoeffizient ist **1/2** = lambda/(d lambda - 1) bei lambda = 1, d = 3 [M, Codex]. Er entspricht der geschwindigkeitsseitigen Form h:h - (tr h)^2.
  - Die Masse waechst wie das Volumen; das ist die Projektvariante A2 [P, HM-B0]. A1 (J = 1 je Zelle) ist eine Abwandlung.
  - Im Code ist der Spurkoeffizient noch nicht gegen 1/2 gebunden. Vor jedem Vergleich pruefen.
- **Kruemmungsanteil:** -(1/8 pi G) Summe_e w_ve l_e eps_e + (Lambda/8 pi G) Summe_t w_vt V_t
  - Die positiv benannte Regge-Summe steht in H mit **Minus**, wie -sqrt(g) R in ADM.
- **Gewichte [W]:** w_vt = 1/4 fuer die Ecken von t, w_ve = 1/2 fuer die Ecken von e. So ist Summe_v N_v H_v bei gleichem N gleich N mal Gesamtsumme.

### 2.3 Strukturbefund zur Traegheit [M, ES; vor dem Leser nicht als gesichert fuehren]

- **Form A** (impulsseitig je Zelle) gibt einen Bewegungsanteil Summe_t N_t J_t(p), also **linear in N**. Damit ist H_v = dH_tot/dN_v eine echte Zwangsfunktion ohne N.
- **Form B** (geschwindigkeitsseitig, Lund-Regge, Literaturstandard; im Projekt A2L):
  - L_kin = Summe_t (1/(2 N_t)) qdotᵀ M_t qdot mit hdot = gdot - L_s g; der Faktor 1/N_t steht damit im Bewegungsterm, wie Codex verlangt.
  - Die Legendre-Umkehr gibt (1/2) pᵀ (Summe_t M_t/N_t)^-1 p.
  - Weil Nachbarzellen sich Kanten teilen, ist das **nicht linear in N**, sobald N von Zelle zu Zelle variiert (wie parallel geschaltete Widerstaende).
  - Die N-Variation liefert dann eine Gleichung, in der N selbst stehen bleibt, keine Zwangsbedingung der ueblichen Art.
  - Linear wird es nur bei einem N fuer alle Zellen, also mit einem globalen Takt (projizierbar, Horava-artig). Den schliesst SKALAR-SEKTOR-L nach heutigem Stand aus [P].
- **Bisherige Rechnungen dazu [P, HODGE-MASSE-1, Tabelle 4.2]:**
  - Form A ist mit der Reduktion R1 auf allen Netzen stabil, aber richtungsabhaengig (V: A1 6,34 %, A2 5,92 %).
  - Form B ist mit der Reduktion RH exakt TT-isotrop (S 1,3e-7, A15 7,5e-8), hat aber auf jedem Netz wachsende Moden (Kristalle 1, Glas 46 bis 50).
  - Form B mit R1 (A2LR1) ist auf den Kristallen regulaer, aber nicht isotrop (V 10,6 %, S 0,74 %, A15 4,7 %). Auf Glas hat sie 28 bis 33 wachsende Moden. Die Isotropie von B kommt also erst mit RH.
  - LUND-REGGE-MASSE-1 rechnet die Literaturform genauer nach (laeuft).
  - Auf Glas wachsen Moden in allen Paarungen ausser A1 und A2 mit R1; die Kristalle sind dort regulaer. Glas hat fast flache Splitter-Zellen (kleinstes Volumen 0,007 des Mittels). Ob sie die Ursache sind, prueft SPLITTER-FREI-1 (Warteschlange) [H].
- **Folge [H]:** In den bisher gerechneten Formen stehen die saubere Zwangsstruktur (A) und die Isotropie ohne Abstimmung (B, nur mit RH) gegeneinander. Isotropie ohne Abstimmung gab es bisher nur mit B und RH, und genau dort wachsen Moden. Das schaerft "L2 haengt an L1".
- **Auswege [H]:**
  - (i) Form A als Geruest, Isotropie aus Symmetrie (Ikosaeder-Ordnung; DANZER-TT-1 laeuft) oder aus Vergroebern.
  - (ii) Regime K: kovariante 4D-Zeit mit Zeltstangen. Dort wird keine eigene Bewegungsenergie gesetzt; sie folgt aus der 4D-Regge-Wirkung.
  - (iii) eine nicht-ultralokale Lapse-Kopplung, die Form B linear macht. Dafuer ist im Projekt nichts bekannt.
- Ob das schon in der Literatur steht (3+1-Regge mit stetiger Zeit, Piran/Williams 1986; Friedman/Jack 1986), ist zu pruefen [L, ungeprueft].

### 2.4 Verschiebung und Gauss

- **D_v [ES]:** D_v erzeugt die Verschiebung der Ecke v und wirkt auf **alle** Variablen: auf q ueber die Kantenvektoren, auf phi und A ueber ihren Transport. Die genaue Form steht noch aus; linear am flachen Netz ist sie die Impulsregel aus IMPULS-NETZ-1 [P].
  - Abseits von flach bricht Regge die Verschiebungssymmetrie (Bahr/Dittrich) [S].
- **G_v:** G_v = (d0ᵀ E)_v - rho_v. Im neutralen Arm ist rho = 0.

## 3. Materie und Licht

### 3.1 Normierungen sind Setzungen [W]

- **Skalar:** L_phi = (Z_t/2) phidotᵀ *0 phidot - (Z_s/2)(d0 phi)ᵀ *1 (d0 phi) gibt Z_t *0 phi'' = -Z_s d0ᵀ *1 d0 phi, also c_phi^2 ~ Z_s/Z_t [M, Codex].
- **Finns Takt T = 8 d0ᵀ *1 d0:** Mit Z_s/Z_t = 8 lautet die Gleichung *0 phi'' = -T phi [M].
  - Die 8 ist damit eine Wahl der Zeiteinheit.
  - Dieselbe Zeiteinheit muss in Maxwell und Geometrie stehen. Das ist eine Setzung, keine Folge.
- **Gleiche Grundgeschwindigkeit:** Mit gleicher Zeiteinheit haben Skalar und Licht langwellig auf jedem periodischen Netz dieselbe richtungsgleiche Grundgeschwindigkeit [P, DANZER-NAEHERUNG-2].
  - Die Richtungsgleichheit folgt aus der Rang-2-Identitaet Summe *1 l lᵀ = Vol I.
  - Die Gleichheit **zwischen** den Sektoren folgt aus der gemeinsamen Setzung.
  - Rang 2 erzwingt nicht Rang 4. Fuer die Schwerewellen ist die Richtungsgleichheit damit offen (Abschnitt 2.3).

### 3.2 Erster Arm: neutral [W]

- **Skalar (Q-Ball, globale U(1)-Ladung):**
  H^phi = Summe_v N_v [ |pi_v|^2/(Z_t *0_v) + *0_v U(S_v) ] + Summe_e N_e Z_s *1_e |phi_a - phi_b|^2, mit S = |phi|^2 (Codex: U immer als U(S)).
- **Licht:** H^EM = Summe_e N_e (E^e)^2/(2 *1_e) + Summe_f N_f *2_f (d1 A)_f^2/2.
  - Der elektrische Term braucht *1_e > 0. Bei *1_e -> 0 wird er singulaer (Abschnitt 6).
- **Kopplung an die Geometrie:**
  - Sie laeuft ueber die l-Abhaengigkeit von *0, *1, *2 und V. Das ist eine gesetzte metrische Kopplung [W], kein hergeleitetes Aequivalenzprinzip.
  - Die Spannung der Materie an einer Kante ist die Ableitung des Materieteils nach q_e. Sie kommt aus demselben H wie die Bewegung der Materie [ES].
  - Ob die schwere Masse eines Q-Balls einschliesslich Bindungsenergie gleich der traegen ist, ist ein eigener Test (Codex Rang 8).

### 3.3 Zweiter Arm: geladen (ausdruecklich anderes Modell)

- Gradient mit Linktransport |phi_a - U_ab phi_b|^2, U_ab = exp(i e A_e), dazu die zeitliche kovariante Ableitung mit A0. Die Ladungsdichte rho_v in G_v folgt aus den kanonischen Materieimpulsen derselben Wirkung.
- Profile, Ladungsbereiche, Stabilitaet und die bisherigen Bindungsbefunde des Q-Balls gelten dort **nicht** ohne neuen Nachweis (Coulomb-Energie) [Codex].

## 4. Zwangsbedingungen: Wahl fuer Fassung 2

- **Wahl [W]: ungefixtes Eichmodell.** N_v, s_v und A0_v sind freie Multiplikatoren.
- **Zu berechnen:**
  - die Poisson-Matrix von {H_v, D_v, G_v}
  - Erhaltung unter H_tot
  - Null- und Randmoden auf dem Torus
  - Ergebnis erster Klasse: gut. Ergebnis zweiter Klasse: Dirac-Klammer und Zaehlung der Freiheitsgrade.
- **Bekannt:**
  - Gauss ist abelsch und mit eichinvariantem H vertraeglich [M].
  - Die Impulsregel ist linear am flachen Hintergrund erster Klasse [P, IMPULS-NETZ-1]. "Linear" ist ein Zwischenziel, keine Grundlage fuer die nichtlineare Gleichung.
  - Die skalare Regel ist offen.
- **K = 0 (maximale Zeitscheiben, Finns Takt):**
  - Im ungefixten Modell ist K = 0 eine Eichfixierung. Das Paar (H, K) ist zweiter Klasse.
  - N ist dann nicht frei, sondern folgt aus der Lapse-Gleichung, der diskreten Form von Laplace N = N (K:K + 4 pi G (rho + S)) - N Lambda [L, Standard].
  - Finns Takt ist so eine Wahl der Zeitscheiben, keine eigene physikalische Uhr.
  - Die andere Lesart (K = 0 als eigenes Gesetz, Horava-Ecke alpha = beta = 0) waere eine andere Theorie und ein eigener Arm.
  - Welche Lesart der bisherige Code rechnet, muss die Algebra zeigen. Er setzt H und K = 0 zusammen als Regeln.
- **Energie:**
  - Kein Positiv-Energie-Import.
  - Auf dem geschlossenen Torus ist H_tot auf den Loesungen eine Summe von Zwangsbedingungen, also null [M]. "Energie" heisst dort die reduzierte Energie der Stoerungen bzw. die Energie nach einer Eichfixierung.
  - Signatur und Vorzeichen dieser reduzierten Energie sind eigens zu pruefen. Die Stabilitaetstests (R1, RH) tun genau das.

## 5. Kruemmung <-> Spannung (Finn, 05.10.)

- **Schlaefli [M; Regge 1961, L]:** Die Ableitung von Summe_e l_e eps_e nach l_e ist eps_e; die Aenderungen der Fehlwinkel heben sich weg.
  - Die "Zugspannung" einer Kante im Kruemmungsanteil ist also ihr Fehlwinkel.
  - Im ruhenden Fall steht ihr in der Kantengleichung die Spannung der Materie gegenueber. Das ist die diskrete Einsteingleichung.
- **Folge:** "Kruemmung wird Spannung" ist die Feldgleichung selbst, keine Zusatzregel.
  - Eine Regel "Fehlwinkel ueber einer Schwelle wird an die Nachbarn verteilt" (Kruemmungs-Sandhaufen) waere eine **zusaetzliche**, vermutlich dissipative Regel.
  - Sie gehoert in einen eigenen SOC-Arm, nicht in den Kern. Pflichtkontrolle: Schwerewellen duerfen dadurch nicht gedaempft werden (RAUM-GAS-L).
- Literaturstand zu Kruemmung, Spannung und Spin: KRUEMMUNG-SPANNUNG-SPIN-L (laeuft).

## 6. Umklappen (erst nach den Abschnitten 2 bis 4)

- **Klasse:** periodisches Delaunay-Netz ohne Rand.
  - Am Zug kann ein duales Mass **null** sein, ist dort also gerade nicht strikt positiv.
  - Der elektrische Term E^2/(2 *1) wird dort singulaer, waehrend ein anderer gewichteter Term verschwindet. Stetigkeit von M heisst nicht Stetigkeit von M^-1 [Codex].
  - Die HKV-Aussage (Delaunay haelt die umkreisbasierten Sterne nicht negativ) ist fuer diese Klasse mit Entartungen an der Quelle zu pruefen.
- **Uebergabe:**
  - A, E, phi, pi und p muessen auf das neue Kokettennetz abgebildet werden.
  - Die Abbildung muss das Differential d (diskrete Kontinuitaet) respektieren und **Gauss nach dem Zug** erhalten, ohne Ladung zu erzeugen.
  - Energie, symplektische Struktur und Zwangsbedingungen sind drei getrennte Bedingungen.
- **Zaehlung:** Die 9 geometrischen Freiheitsgrade der flachen Bipyramide zaehlen weder den ganzen Regge-Phasenraum noch Materie und Licht.
- **Energiesprung:**
  - Gemessen: 1,2e-3 bis 3,9e-3 je 2-3-Zug, A2 und R1 [P, HODGE-MASSE-1].
  - Das beweist nicht, dass allein die fehlende Uebergabe die Ursache ist [H].
- **1-4- und 4-1-Zuege** aendern die Eckenzahl; Zwangsbedingungen kommen hinzu oder fallen weg (Dittrich/Hoehn) [S].
- **Topologie:** Pachner-Zuege tauschen eine Kugel gegen eine Kugel mit gleichem Rand und aendern die Topologie nicht [M]. Topologieaenderung (Geonen, Finns Spin-Frage) braucht eine weitere Zugart.

## 7. Bewusst draussen (spaetere, eigene Entscheidungen)

- **Unimodulares Lambda:** braucht zusaetzliche Variablen, Zwangsbedingungen und Randdaten. Eine Integrationskonstante ist noch keine vorhergesagte kleine Zahl.
- **SOC-Auswahl eines kleinen Lambda bzw. Kruemmungs-Sandhaufen:** eigener Arm (Abschnitt 5).
- **Kaehler-Dirac:** eine weitere Feld- und Quantisierungsentscheidung, kein durch Hodge hergeleiteter Spin-1/2-Sektor.
- **Quantisierung:**
  - exp(iS/hbar) setzt eine Wirkungseinheit voraus, dazu Mass, Eichbehandlung und eine Zustands- bzw. Messdeutung.
  - Das i allein erzeugt keine Quantenmechanik.
- **Einheiten:** Eine Kantenlaenge setzt G nicht ohne Wirkungs-, Zeit- und Energienormierung. Planck-Einheiten als Definition sind keine Herleitung.

## 8. Gesetzt gegen zu pruefen

**Gesetzt [W]:**
- Torus-Topologie, festes Netz
- q_e als Variablen
- umkreisbasierte Hodge-Sterne
- Form A mit Spurkoeffizient 1/2 als kanonisches Geruest, lambda = 1
- Interpolation von N, s und A0
- Zeit-Normierungen Z je Sektor (gemeinsame Zeiteinheit, Faktor 8)
- metrische Kopplung (alle Sektoren benutzen dieselben l_e)
- neutraler Q-Ball, A nicht kompakt
- G und Lambda fest

**Offene Folgerungen (nicht geliefert, Pruefliste):**
1. Algebra der Zwangsbedingungen und Zahl der Freiheitsgrade
2. stabile reduzierte Energie
3. TT-Isotropie mit Form A, nur ueber Symmetrie oder Vergroebern? (DANZER-TT-1, LUND-REGGE-MASSE-1)
4. Newton-Grenzfall und Lichtablenkung im selben H (bisher in getrennten Rechnungen: MATERIE-NETZ-1)
5. Mitfuehrung (bisher IMPULS-NETZ-1, linear)
6. gleiche schwere Masse einschliesslich Bindungsenergie
7. Abstrahlung beim Doppelpulsar mit vollstaendiger Quelle (V1-AUFHEBUNG-1 laeuft)
8. kleines Lambda

## 9. Reihenfolge (Vorschlag)

1. Frischer Leser und Codex-Kurzblick auf Fassung 2, vor allem auf den Strukturbefund 2.3.
2. Algebra-Karte: Poisson-Matrix von H_v, D_v, G_v, linearisiert um das flache Netz V, Form A. Leitungskarte; Codex nur als Pruefer.
3. LUND-REGGE-MASSE-1 und DANZER-TT-1 abwarten: Kann Form A ueber Symmetrie isotrop sein, oder ist Form B mit R1 stabil?
4. Neutraler Q-Ball plus Maxwell im selben H auf festem Netz: Spannungskopplung und schwere Masse (Codex Rang 8).
5. Danach die Uebergaberegel beim Umklappen.
6. Danach SOC-Arm, Kaehler-Dirac, Quantisierung.

## Einfach gesagt

Fassung 2 schreibt die Grundgleichung so, dass man sie wirklich nachrechnen kann. Sie hat eine Energieformel mit drei Regeln: eine fuer die Zeit, eine fuer das Verschieben der Ecken und eine fuer die elektrische Ladung. Dabei ist etwas aufgefallen: Die Form der Traegheit, die Schwerewellen von selbst in alle Richtungen gleich schnell macht, passt nicht gut zu einer oertlichen Uhr in jeder Ecke; die Form, die dazu passt, ist bisher richtungsabhaengig. Krümmung und Spannung sind im Netz ohnehin dasselbe, das ist schon Einsteins Gleichung. Was noch entstehen soll, etwa Newton oder ein kleines Lambda, steht jetzt ausdruecklich auf einer Pruefliste statt als Versprechen da.
