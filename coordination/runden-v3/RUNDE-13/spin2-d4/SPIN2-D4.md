# SPIN2-D4: Gilt die CEMZ-Kopplung der Glieder 7 und 10 in D = 4? (Runde 13, Feldforscher)

- Auftrag: claude-primary, Lesekarte RUNDE-13/spin2-d4/KARTE.md (ganz gelesen). Beginn (date): 2026-10-01 20:13:20 CEST.
  Zeitbox 50 min, also bis 21:03:20.
- Gelesen vor dem ersten Abruf (nur intern): KARTE.md ganz; RUNDE-11/cemz-mess/CEMZ-MESS.md ganz;
  RUNDE-12/cemz-ebene/CEMZ-EBENE.md Z. 1-60 (Kurzfazit, Erwartungsverstoesse), 129-200, 268-300 (R2: 24-Monats-Suche
  zu CEMZ in D = 4); WARUM-SPIN-2.md Z. 248-288 (Glied 7), 396-449 (Glied 10), 534-541 (Nachtrag 24.09.), 672-811
  (Fassung 2, Nachtraege 01.10.); literatur-20260924/GLIEDER-7-10-MESSBAR-20260924.md nur per grep (Nummer 2201.06602
  steht dort Z. 517; Bericht hatte nur Abstract [Pa]).
- Lesetiefe: [A] an der Quelle (Seite, Gl., Abschnitt), [S] nur Abstract, [L?] Gedaechtnis, [H] Hypothese,
  [ES] eigener Schluss. Nur [A] traegt.
- Werkzeuge: WebSearch gesperrt (aufgebraucht). Nur arXiv-API, INSPIRE-API, WebFetch auf arxiv.org mit bekannten Nummern.
  "Nicht gefunden" ist deshalb schwaecher als mit Websuche.

# BERICHT

Geschrieben ab 2026-10-01 20:30:55 CEST (date davor). Belege und Rechenwege im Arbeitsfeld darunter (R1-R12, Z-1 bis Z-3).

## Kurzfazit (10 Zeilen)

1. **Regime B im Ergebnis, aber nicht aus dem Grund der Karte:** Eine D = 4-Fassung mit Annahmen gibt es (CHLPSD 2022, JHEP 05 (2023) 122 [A]): messbares Riem^3 (gerade oder ungerade) => "a spin-4 particle must exist" mit M^-1 > r0 (S. 35), "up to an infrared logarithm" (Exponent 1/8 aus Gl. 4.4 [ES]).
2. Ihr D = 4-Schritt ist ein von Hand gesetzter IR-Schnitt ("accept that this causes negativity", S. 16 [A]). Bellazzini u. a. 2025/26, S. 30 [A]: "Introducing hard IR cutoffs by hand [31,39,41] does not resolve the issue" ([39] = CHLPSD); Haering/Zhiboedov S. 17 [A]: in D = 4 ist T(s,t) "not a well-defined observable".
3. **Die eine Voraussetzung:** das IR-Verhalten des Graviton-Austauschs in D = 4 (1/t-Pol, Shapiro-/Eikonal-Log, Gravitonen keine guten asymptotischen Zustaende), also ob eine endliche IR-Skala (m_IR, Hubble, AdS, Detektoraufloesung E) in die Kausalitaetsannahme eingehen darf. Zeitmaschine, Dispersion und Regge-Herleitung brechen in D = 4 alle dort (Bucciotti S. 21 [A]: "the same IR effect").
4. Unendlicher Turm in D = 4 nur referiert (CHLPSD S. 25), CEMZ Fn. 23 nur unter ihrem Kriterium; D = 4-Zeitmaschine mit Stosswelle seit 2025: nach Recherchestand nicht belegt (nur API, schwach).
5. **Glieder 7 und 10:** In D = 4 sind sie gekoppelt nur als Folgerung unter einer bestrittenen IR-Voraussetzung, also als Erwartung mit benannter Bruchstelle. Die Kopplung laeuft dort ueber Dispersion (CHLPSD), nicht ueber die CEMZ-Zeitmaschine; Glied 7 masselos (Weinberg) ist unberuehrt.
6. **CEMZ-EBENE** bleibt bedingt: (i) IR-Voraussetzung, (ii) alpha ~ 1, denn CHLPSD lassen die SM-Kopplung offen ("left to future work", S. 2 [A]). Innerhalb der CHLPSD-Axiome waere V0/U4 ("no sharp bound") geschlossen [ES, Normierung ungeprueft].
7. **Unterscheidungspunkt:** E -> 0 bzw. R_IR -> unendlich. Bellazzini S. 30 [A]: beim "optimal detector" werden die Schranken trivial; meine Lesart der Grenze G M^2 log(M/E) ~ 1 ergibt fuer M ~ 1/(30 km) erst E ~ M exp(-3e78) [ES]. Physikalisch sind A und B ununterscheidbar; der Streit ist axiomatisch.
8. **Kleinster naechster Schritt:** Lesekarte Bellazzini u. a. 2512.13780, Abschn. 2-5: Erlaubt M_E externe Gravitonen (h = +-2) und den Vertex g^3? **Scheiterregel:** "nein" oder "nur mit neuer Annahme" -> B bleibt, eine IR-sichere Fassung fehlt. "ja", und die CHLPSD-Funktionale uebertragen sich mit m_IR -> E -> A mit Detektorannahme erreichbar; dann Folgekarte "Gl. 4.4 mit E".

## Erwartungsverstoesse (das Wichtigste zuerst)

**V1 (gross): Es gibt eine D = 4-Hoeherspin-Pflicht ohne Zeitmaschine.** Erwartet (K2, E1): dispersive Schranken "in Einheiten einer
Skala, kein Turmzwang", M nur als Definition. Gefunden (R1, CHLPSD [A]): M ist die "spin-4 mass gap" (Abb. 8, S. 26), leichte
Spin-0- und Spin-2-Felder senken sie nicht (Abschn. 3.3). Schluss S. 35: "a spin-4 particle must exist whose Compton wavelength is at least
as long as the length r0". Begruendet wird das ueber Kommutatoren, Kreuzung und Analytizitaet, nicht ueber Zeitmaschinen (S. 36). Damit
trifft der RUNDE-11-Einwand "CTC nur fuer D > 4" diese Route nicht. Korrigierte Erwartung: Den Inhalt von Regime A gibt es in D = 4;
offen bleibt die Gueltigkeit des IR-Schritts.

**V2 (gross): Der Gegensweep kippt V1 in der Strenge.** Erwartet (E14): Bellazzini u. a. bewerten CHLPSD nicht. Gefunden (R12 [A],
S. 30): "Introducing hard IR cutoffs by hand [31,39,41] does not resolve the issue: either the IR part of the dispersion relation diverges
or the UV part becomes unconstrained. Moreover, the unitarity and analytic properties of the regulated amplitudes remain unclear"
([39] = CHLPSD). Dazu: Graviton-Schranken nur "for D > 4 ... or in AdS ..., with the bounds disappearing as D -> 4". Korrigierte
Erwartung: Ich lag nach R1 bei "A bedingt"; nach R12 heisst es "B im Ergebnis, mit A-Inhalt unter bestrittener Voraussetzung".

**V3 (gross): Beide Lager meinen dieselbe Groesse.** Erwartet (H0, E9 nicht gewertet): Dispersion und Zeitvoreilung als getrennte
Baustellen. Gefunden: Bucciotti S. 21 [A]: "This logarithm in D = 4 is the scattering-amplitude manifestation of the same IR effect we
identify geometrically". Haering/Zhiboedov S. 6, 17 [A]: "gravitons are good asymptotic states in d > 4 and not in d = 4"; Regge-Herleitung
nur "valid for d > 4". Bellazzini S. 30 [A]: Der "optimal detector" macht die Schranken trivial, "the gravitational time delay required to
reach such an enormous apparatus swamps any microscopic causality-violating effect", also Bucciottis Befund in Amplitudensprache. Nach
Regel 6 brechen drei Wege an einer gemeinsamen Groesse, der IR-Skala.

**V4 (mittel): Auch der strenge Grenzfall ist nicht "B bewiesen".** Chang/Parra-Martinez (R7 [A]) erhalten mit angenommener
Eikonal-Resummation endliche D = 4-Schranken bei m_IR -> 0, aber G-unabhaengig (g2 >= -O(1)/M^4), nur fuer Skalare. Bellazzini S. 31
[A] nennt solche Schranken "effectively ... trivial statements of the type g2 M^4 x 0 + 259 >= 0". Der Grenzfall ist umstritten,
nicht entschieden.

**V5 (mittel): CHLPSD begrenzen auch den paritaetsungeraden Vertex.** g^3 = alpha3 + i alpha~3 (Gl. 2.11 [A]). In RUNDE-11 hatte
alpha~3 keine Datenschranke (Maenaut "future study"). Die Theorie-Kopplung an Spin 4 gilt fuer beide Paritaeten.

**V6 (klein): "Significant impact even at tree level" (Beadle u. a.) ist kein D = 4-Befund.** Gerechnet ist d = 5, 6. Fuer D = 4 steht nur
das Bochner-Hindernis (R8 [A]).

Bestaetigt (je eine Zeile): K3/E4 keine D = 4-Zeitmaschine seit 2025 (R6); E5'(c) Haering/Zhiboedov 2410.21499 (R2); E7 keine Titel
gegen CHLPSD in 24 Monaten (R3); E10 Chang/Parra-Martinez nur Skalar, Eikonal als Annahme (R7); E12 Haering/Zhiboedov D = 4 offen (R10);
E13 keine M_E-Anwendung auf Graviton-R^3 (R11).

## Vorab gegen Ausgang

| Erwartung (Zeit) | Wortlaut kurz | Ausgang |
|---|---|---|
| K1 (Karte, vor 20:13) | Regime B ist Stand der Literatur, ~70 % | **Im Ergebnis getroffen, im Grund verfehlt.** B gilt, weil der D = 4-IR-Schritt bestritten ist (Bellazzini [A]), nicht weil die Schranken ohne Hoeherspin-Inhalt waeren. Die Karten-Definition "B = ohne Turmzwang" passt nicht: CHLPSD enthalten eine Spin-4-Pflicht. |
| K2 (Karte) | Staerkste D = 4-Aussagen dispersiv (Caron-Huot u. a.), IR-Regulator noetig, Skala, kein Turmzwang, ~60 % | **Teilweise verletzt.** Getroffen: dispersiv, CHLPSD, IR-Regulator. Verletzt: Die Skala ist die Spin-4-Massenluecke, die Aussage lautet "spin-4 particle must exist" (V1). Den unendlichen Turm zeigen sie nicht. |
| K3 (Karte) | D = 4-Zeitmaschine mit nichtstationaerer Stosswelle seit 2025, ~25 % | **Nicht gefunden** (R6; nur API, schwach). Bucciotti 2026 Abschn. 4.2 [A]: naive Konstruktion scheitert, "it is still possible that CTCs may form in the non-linear regime". Urteil: nach Recherchestand nicht belegt. |
| E1 (20:16:12) | CHLPSD: M nur Definition, kein Turmzwang | verletzt (V1) |
| E2 (20:16:12) | D = 4-Eikonal-R^3: Voreilung nur relativ zum IR-Log | bestaetigt ueber CHLPSD Gl. 3.25-3.28 [A]; Accettulli Huber u. a. 2006.02375 selbst nicht gelesen |
| E3 (20:16:12) | Regge-Schranke D >= 5, D = 4 nur vermutet | bestaetigt (R9 [S], R10 [A]) |
| E4 (20:16:12) | keine D = 4-Zeitmaschine | bestaetigt (R6) |
| E5' (vor 20:19) | (a) IR-sicher ~35 %, (b) negatives Laufen staerkt B, (c), (d), (e) | (a) teilweise verletzt, Rahmen existiert (R2, R12); (b) Richtung umgekehrt, Schranken "argued" gerettet; (c) bestaetigt; (d) ausgesondert; (e) bestaetigt |
| E6 (20:16:12) | Gegenposition: A schwach gezeigt, A stark nicht | im Kern bestaetigt, dann durch R12 relativiert: auch A schwach ist nur unter bestrittenem IR-Schritt gezeigt |
| E7-E14 | siehe Arbeitsfeld | E7, E10, E12, E13 bestaetigt; E8, E11 teilweise verletzt; E9 nicht gewertet (S1); E14 verletzt (V2) |

## Literaturstand mit Quellen (nur [A] traegt)

- **Fuer eine D = 4-Kopplung (Inhalt A):** CHLPSD 2022 [A]: Gl. 4.4 |g^3|^2 M^8 <= 24,9 log(M/m_IR) - 27,6; Schluss S. 35. CEMZ Fn. 23
  (RUNDE-11 [A]): Turm "clear in D = 4" unter ihrem Gao-Wald-Kriterium. Pasiecznik 2506.09884 [S]: Kopplung Graviton an massiven Spin 4.
- **Gegen die Tragfaehigkeit in D = 4:** Bellazzini u. a. 2512.13780v2 [A], S. 30-31; Haering/Zhiboedov 2202.08280 [A], S. 5, 6, 17;
  Bucciotti u. a. 2605.00089 [A], S. 3-4, 19-22; Beadle u. a. 2501.18465 [A]: Bochner-Hindernis in d = 4.
- **Reparaturwege (IR-sicher), fuer Graviton-R^3 noch nicht durchgerechnet:** M_E mit Detektoraufloesung (Bellazzini [A]);
  Eikonal-Resummation (Chang/Parra-Martinez [A], Skalar); Energiekorrelatoren in D = 4 (2512.23791 [S]); Coulomb-Moden/DWPT
  (2606.19432, 2609.16896 [S]); de Sitter als Regulator (Bucciotti S. 22: offen).
- **Phaenomenologie-Gegenlager (RUNDE-11):** Alexander/Bernardo/Yunes 2506.14889 [S]; Maenaut "viewed as classical theories" [A, RUNDE-11].

## Regime und Moderatoren

| Regime | IR-Behandlung | Aussage zu g^3 in D = 4 | Beleg |
|---|---|---|---|
| A_IR | harter Schnitt m_IR (Hubble, AdS) | Spin-4 bei M <~ (24,9 ln(M/m_IR))^(1/8)/|g^3|^(1/4); Faktor ~2,4 bis 2,8 [ES] | CHLPSD [A]; bestritten: Bellazzini [A] |
| A_E (Kandidat) | endliche Detektoraufloesung E, IR-endliche M_E | fuer Pionen + Gravitation gezeigt, fuer g^3 nicht gerechnet | Bellazzini [A], R11 |
| A_eik (Kandidat) | m_IR -> 0 mit Eikonal-Resummation | endlich, aber G-unabhaengig; nur Skalar | Chang/Parra-Martinez [A]; "trivial" laut Bellazzini [A] |
| B_asym | streng asymptotisch flach, Zeitvoreilung | keine asymptotische Voreilung, keine Schranke; CTC-Weg nur D > 4 | Bucciotti [A], CEMZ Anh. G [A] |
| I' (RUNDE-11) | infrarote Kausalitaet | turmfrei; reine Tensor-EFT fuer heutige GW-Daten unsichtbar | Nie u. a. [A], dRTZ [S] |

Moderatoren: **IR-Skala** (m_IR, R_IR, E); **Kausalitaetsbegriff** (klassische Voreilung/CTC gegen Kommutator/Kreuzung); **Ordnung in
G** (Baum-Log gegen Resummation). Keine Seite irrt nachweislich. Die Lager sampeln verschiedene IR-Idealisierungen derselben Physik.

## Unterscheidungspunkte

- **U1 (A_IR/A_E gegen B_asym):** Die Regime trennen sich erst bei G M^2 log(M/E) ~ 1 (Bellazzini: G_E = G log(M/E)). Fuer
  M ~ 1/(30 km) heisst das E ~ M exp(-3e78) [ES]. Ueber CHLPSD Gl. 4.4: Faktor 10 statt ~2,4 erst bei R_IR ~ l exp(4e6) [ES]. Wie
  beim Wasser bei 198 K und 1250 atm liegt die Trennstelle ausserhalb jeder Messung; im Labor- und Kosmosbereich sind A und B gleich.
- **U2 (wo D = 4 rechnerisch kippt):** die Eikonalphase chi(b) = 2 G s Gamma((D-2)/2) (pi b^2)^((4-D)/2)/(D-4) (Chang/Parra-Martinez
  Gl. 5.18 [A]). Ihr Pol 1/(D-4) macht in D = 4 aus der Potenz einen Log(L/b). Der g^3-Term ~ 24 g^3/b^4 konkurriert dann mit
  log(1/(b m_IR)) (CHLPSD Gl. 3.25 [A]), und der Ausgang haengt an L bzw. m_IR. In D > 4 entfaellt das.
- **U3 (A_E gegen A_IR):** unterscheidbar nur theoretisch: Ob die M_E-Schranke auf g^3 dieselbe Form wie Gl. 4.4 mit m_IR -> E hat.
  Das ist der naechste Schritt.

## Gegensweep-Befunde

Fuenf Selbstverstaendlichkeiten benannt (Arbeitsfeld Abschn. 3), zwei an der Quelle geprueft:
1. Regge-Axiom in D = 4 begruendet? **Geprueft (R9, R10 [A]): nein**, nur d > 4; D = 4 "re-evaluate", "should eventually work".
2. Spin-4-Pflicht = unendlicher Turm? Nicht neu geprueft; [ES] Standardargument ueber Regge-Wachstum, steht und faellt mit Punkt 1.
3. SM-Kopplung des Spin-4-Zustands (alpha ~ 1)? **Geprueft (R1 [A]): von CHLPSD nicht gezeigt**, nur Collider-Abschaetzungen.
4. g^3 umfasst beide Paritaeten: geprueft (Gl. 2.11 [A]).
5. Staerkste Gegenposition zu meinem Zwischenstand "A bedingt" gesucht und gelesen: Bellazzini u. a. (R12 [A]). Sie kippt das
   Zwischenergebnis (V2).

## Kalibrierung

- **(a) Gemessen:** nichts Neues. Diese Runde ist reine Theorie-Lage. Die Messbezuege (GW-ell, Fuenfte Kraft) stammen aus RUNDE-11/12.
- **(b) Nuetzlich verdichtet:** die Regime-Tabelle mit dem Moderator IR-Skala; die Zahlen (log)^(1/8) ~ 2,4 bis 2,8 und
  E ~ M exp(-3e78) [ES, Kopfrechnung].
- **(c) Gewachsene Gewissheit ohne neue Evidenz:** "Glieder 7 und 10 sind ueber CEMZ gekoppelt". In D = 4 traegt CEMZ selbst nicht (Anh. G);
  getragen wird die Kopplung, wenn ueberhaupt, von CHLPSD unter bestrittenem IR-Schritt.
- **Warnzeichen, eingetreten:** Nach R1 stieg meine Sicherheit fuer "A bedingt" deutlich (Z-1), waehrend die Frage in IR-Regulator,
  Regge-Axiom und Analytizitaet zerfiel. Erst der Gegensweep (R12) hat das zurueckgedreht.

## Offene Fragen

1. Laesst sich die CHLPSD-Schranke (Gl. 4.4) mit IR-endlichen Amplituden M_E (Detektoraufloesung E) neu herleiten? Fuer Graviton-R^3
   bis 10/2026 nicht gefunden (R11, nur INSPIRE-Titel/Abstracts).
2. Haelt Analytizitaet/Kreuzung mit kosmologischem (de-Sitter-)Regulator? (Bucciotti S. 22: offen.)
3. Normierung r0 (CHLPSD) <-> ell (Maenaut) <-> c3^(1/4)/Lambda (EGHS): nicht geprueft. Nur damit wird "V0/U4 geschlossen" belastbar.
4. CHLPSD Fn. auf S. 33 nennt "(log M_Pl R_Universe)^(1/4) ~ 3", Gl. 4.4 fuehrt bei mir auf Exponent 1/8. Groessenordnung gleich
   (~3), Exponent nicht aufgeklaert (Text durch Layout ueberlagert).
5. Accettulli Huber u. a. 2006.02375 (D = 4-Eikonalmatrix mit R^3) nicht gelesen, nur ueber CHLPSD Gl. 3.25-3.26 [A] abgedeckt.

## Quellenliste (dieser Lauf; Hashes in quellen/SHA256SUMS.txt)

| Quelle | URL | Tiefe | sha256 (Volltext-PDF) |
|---|---|---|---|
| Caron-Huot, Li, Parra-Martinez, Simmons-Duffin 2022, Causality constraints on corrections to Einstein gravity, JHEP 05 (2023) 122 | https://arxiv.org/abs/2201.06602 | [A] S. i, 1-3, 8-10, 15-16, 19-20, 24-26, 33-36 | 86365bcb25e81c062dbbdb14ff3a2ff454f4f33ea94efec79c4323e31bfc53d4 |
| Bellazzini, Berman, Isabella, Riva, Romano, Sciotti 2025/26, Positivity with Long-Range Interactions (v2) | https://arxiv.org/abs/2512.13780 | [A] S. 18, 30-31, Lit.-Liste; Rest [S] (Seitenangabe berichtigt vor 20:33:17: ~~S. 29-31~~) | 2050cd823fd459614bc69344b628a9238d3b7596ea5dc799c939f4720ecf8104 |
| Haering, Zhiboedov 2022, Gravitational Regge bounds (v2) | https://arxiv.org/abs/2202.08280 | [A] S. 5, 6, 17 | 18381124297299c4b33cabd5befd4793383a23dee73f3a7eee3f754f1e747eb9 |
| Chang, Parra-Martinez 2025, Graviton loops and negativity, JHEP 08 (2025) 175 (v2) | https://arxiv.org/abs/2501.17949 | [A] S. 3, 31-42 (berichtigt: ~~31-41~~) | bd7c30d6bd1bf25c4ba9f0a1f49e918886a2249a327be4814b79f7f75f5f35a3 |
| Beadle, Isabella, Perrone, Ricossa, Riva, Serra 2025, The EFT Bootstrap at Finite M_PL, JHEP 06 (2025) 209 | https://arxiv.org/abs/2501.18465 | [A] S. 3, 5, Abschn. 3.1, S. 23-24 | 27c1ad58d0900b3e882c2527fbdb386eeb726a71d1c2353cac925c8b1bb3b83d |
| Bucciotti, Creminelli, Longo, McBlain, Trincherini 2026, On the Asymptotic Causal Structure in Gravitational EFTs (v1) | https://arxiv.org/abs/2605.00089 | [A] S. 3-4, 19-22, lokale Kopie RUNDE-11 | 81666ec2661072c952702175107b8884b9253285a7cd4cbcb7b541b218da691f (RUNDE-11) |
| Camanho, Edelstein, Maldacena, Zhiboedov 2014/16, JHEP 02 (2016) 020 | https://arxiv.org/abs/1407.5597 | [A] nur ueber RUNDE-11 (S. 25, 49, 65-66); hier per INSPIRE recid 1307098 bestaetigt | - |
| Haering, Zhiboedov 2024, What is the graviton pole made of? | https://arxiv.org/abs/2410.21499 | [S] | quellen/abs-r2.xml |
| Fernandez, Ruhdorfer, Serra 2026, Negative running of gravitational positivity | https://arxiv.org/abs/2603.15755 | [S] | abs-r2.xml |
| Kehagias, Riotto 2024, Can We Detect Deviations from Einstein's Gravity in BH Ringdowns? | https://arxiv.org/abs/2411.12428 | [S] | abs-r2.xml |
| Grojean, Jiang, Vuong 2025, Shockwaves and Time Delays in Einstein-Maxwell EFT | https://arxiv.org/abs/2512.15927 | [S] | abs-r2.xml |
| Lippstreu 2026, Unitarity and the Forward Direction ... Long-Range Forces | https://arxiv.org/abs/2609.16896 | [S] | abs-r2.xml |
| Cintia, Piazza, Ramos 2026, Probabilistic Causality from Graviton Fluctuations | https://arxiv.org/abs/2606.02729 | [S], ausgesondert | abs-r2.xml |
| Plestid, Quilez Lasanta 2026, Partial-wave unitarity and long-range interactions | https://arxiv.org/abs/2606.19432 | [S] | abs-r4.xml |
| Peng, Rodina, Tokareva, Xu 2026, Sampling the Graviton Pole ... | https://arxiv.org/abs/2604.15235 | [S] | abs-r4.xml |
| Pasiecznik 2025, Bootstrapping Gravity with Crossing Symmetric Dispersion Relations | https://arxiv.org/abs/2506.09884 | [S] | abs-r4.xml |
| Calisto, Cheung, Remmen, Sciotti, Tarquini 2025, Completeness from Gravitational Scattering, PRD 113, 106008 | https://arxiv.org/abs/2512.11955 | [S] | abs-r4.xml |
| Gumus, Metayer, Tourkine 2025, Tracking S-matrix bounds across dimensions | https://arxiv.org/abs/2512.24474 | [S] | abs-r4.xml |
| Energy correlators in four-dimensional gravity (2025) | https://arxiv.org/abs/2512.23791 | [S, INSPIRE-Abstract] | insp-cites-bellazzini.json |
| Gravitational EFTs with Maximal Supersymmetry and a Peculiar Parity (2026) | https://arxiv.org/abs/2607.14230 | [S, INSPIRE-Abstract] | insp-cites-bellazzini.json |
| Accettulli Huber u. a. 2020, Eikonal phase matrix ... time delay in EFTs of gravity | https://arxiv.org/abs/2006.02375 | nur Titel (API) | arxiv-r6b.xml |
| Suchlisten: INSPIRE refersto:recid:2012035 (93 Treffer ab 10/2024), refersto:recid:3093263 (23); arXiv-API R6a-c | - | [S, Titel] | SHA256SUMS.txt |

## Selbstanzeigen

- **S1:** Die Erwartung zu R5 (Bucciotti, lokale Kopie) habe ich erst nach dem grep geschrieben. Sie ist gestrichen und zaehlt nicht.
- **S2:** Die INSPIRE-Titelsuche "Gravitational Regge bounds" (R9) und die zwei recid-Nachschlagungen (R3) liefen ohne schriftliche
  Vorab-Erwartung. Die gedachte Erwartung zu R9 zaehlt nicht.
- **S3:** Die erste INSPIRE-Abfrage (refersto:arxiv:...) lieferte wegen falscher Syntax 141444 Treffer. Ich habe sie verworfen und die Datei geloescht.
  Die arXiv-Abfragen mit submittedDate-Filter und Wildcard gaben 0 Treffer; ich habe sie ohne Filter wiederholt. Die erste API-Abfrage per http war leer.
- **S4:** Ein Zeitvermerk war geschaetzt ("Eintrag 20:2x" bei R2) und ist berichtigt. Alle anderen Zeiten sind per date gemessen.
- **S5:** Rechnungen ([ES]: (log)^(1/8) ~ 2,4 bis 2,8; E ~ M exp(-3e78); M ~ 6,6e-12 eV fuer 30 km) sind Kopfrechnungen ohne
  Software. Die Normierung r0 <-> ell habe ich nicht geprueft. Die Fussnote auf CHLPSD S. 33 ist im pdftotext-Layout ueberlagert und nur
  sinngemaess gelesen.
- **S6:** Gelesen habe ich nur per WebFetch (PDF-Binaerablage), arXiv-API, INSPIRE-API, pdftotext, grep und sed. Kein python, kein awk, kein git,
  kein Peerbus, keine Unteragenten. WARUM-SPIN-2.md, CEMZ-MESS.md und CEMZ-EBENE.md habe ich nur gelesen. Keine Sperrpfade.

## Einfach gesagt

Die Frage war: Wenn man an der Schwerkraft eine kleine Korrektur misst, muss es dann neue, schwere Teilchen mit hohem Spin geben,
und gilt das auch in unseren vier Dimensionen? Eine Arbeit von 2022 sagt ja: Dann muss ein Teilchen mit Spin 4 existieren, ungefaehr
bei derselben Laengenskala. Dafuer muss sie aber eine kuenstliche Grenze fuer sehr grosse Entfernungen einziehen. In vier Dimensionen
reicht die Schwerkraft so weit, dass manche Rechnungen sonst unendlich werden. Andere Gruppen halten diese Grenze fuer nicht sauber
begruendet, und eine saubere Ersatzmethode ist fuer genau diesen Fall noch nicht durchgerechnet. Deshalb ist die Verbindung in vier
Dimensionen eine gut begruendete Erwartung, aber noch kein bewiesener Satz.

---

# ARBEITSFELD

## 0. Was schon steht (nicht doppeln)

- CEMZ (arXiv:1407.5597, INSPIRE recid 1307098) [A, RUNDE-11 R5]: In D = 4 Gao-Wald-Kriterium, log weggezogen,
  "this is not a real issue" (S. 25); Fn. 23: Turm "clear in D = 4" (S. 49); Zeitmaschine (Anh. G) nur D > 4.
- Bucciotti u. a. 2605.00089 [A, RUNDE-11 R4/R18]: D = 4 stationaer: keine asymptotische Voreilung; CTC "only works for D > 4";
  Stosswelle nicht vom Theorem gedeckt.
- Nie u. a. 2410.10973 [A], dRTZ 2112.05054 [S]: infrarote Kausalitaet, reine Tensor-EFT fuer heutige GW-Daten unsichtbar.
- CEMZ-EBENE R2 [S]: INSPIRE-Zitate von CEMZ ab 2026-03 und von Bucciotti: nichts, was CEMZ in D = 4 umstoesst oder rettet.
- Caron-Huot/Li/Parra-Martinez/Simmons-Duffin, JHEP 05 (2023) 122, arXiv:2201.06602: im 24.09.-Bericht nur Abstract [Pa]:
  "vierdimensional", "two-sided bounds ... in terms of the mass M of new higher-spin states". **Nie im Volltext gelesen.**
- Kandidaten aus der INSPIRE-Liste RUNDE-11 (cemz-citing-2024-2026.txt, Titel nur): 2410.21499 "What is the graviton pole
  made of?", 2412.17902 "Analytic bootstrap bounds on masses and spins ...", 2512.13780 "Positivity with long-range
  interactions", 2603.15755 "Negative running of gravitational positivity", 2512.15927 "Shockwaves and time delays in
  Einstein-Maxwell EFT", 2606.02729 "Probabilistic Causality from Graviton Fluctuations", 2411.12428 Kehagias/Riotto,
  2504.14434 "Corrections of the GR eikonal limit ...". Noch nicht gelesen.

## 1. Vorab-Erwartungen (date 2026-10-01 20:16:12 CEST, vor jedem externen Abruf)

Erwartungen der Leitung (bindend, Karte Z. 33-39), hier nur uebernommen:
- K1: Regime B ist Stand der Literatur: ~70 %.
- K2: Staerkste D = 4-Aussagen aus dispersiven Summenregeln (Caron-Huot u. a.); IR-Regulator oder Abschneiden noetig;
  Schranken in Einheiten einer Skala, kein Turmzwang: ~60 %.
- K3: Seit 2025 eine Arbeit, die eine D = 4-Zeitmaschine mit nichtstationaerer Stosswelle ausdruecklich durchrechnet: ~25 %.

Meine eigenen, feiner (vor jedem Abruf):
- E1 (2201.06602, Volltext): D = 4, Baumniveau, Regge-Annahme (Spin < 2 im Regge-Limes). Schranke auf den R^3-Koeffizienten
  der Form |g3| M^4 <~ O(10) x log(M/m_IR) bzw. mit Stossparameter-Abschneiden b_max. M ist als Masse der "neuen
  Hoeherspin-Zustaende" *definiert* (Annahme: unterhalb M nur Graviton und Spin <= 2?), nicht als Folgerung, dass ein
  **unendlicher** Turm existiert. Turmzwang wird nicht gezeigt; "infinitely many" hoechstens als Bemerkung zum Regge-Limes.
- E2 (D = 4-Eikonal mit R^3, z. B. Accettulli Huber u. a. 2020, Nummer per INSPIRE zu holen): D = 4 explizit; R^3 gibt eine
  Helizitaetsmischung (Phasenmatrix), ein Eigenwert wird bei kleinem b < (alpha/log)^(1/4) negativ relativ zum
  Einstein-Log -> Zeitvoreilung nur relativ zum IR-regularisierten Log; Folgerung "neue Physik bei der Skala", keine CTC.
- E3 (Haering/Zhiboedov "Gravitational Regge bounds", Nummer per INSPIRE): Regge-Schranke (Spin 2) in D >= 5 aus Kausalitaet
  begruendet; D = 4 wegen IR-Divergenzen nur vermutet oder fuer IR-sichere Groessen.
- E4 (2024-2026, Zeitmaschine D = 4 mit Stosswelle, K3): nichts gefunden. Gegenrichtung (Bucciotti 2026) ist das Juengste.
- E5 (2410.21499, 2412.17902, 2512.13780, 2603.15755): Bausteine fuer Regime B (D = 4-Positivitaet mit IR-Logs, "negative
  running" = Schranken werden mit IR-Log schwaecher oder kippen), keine D = 4-Turmsatz-Aussage. 2410.21499 eher D >= 5
  oder allgemein D: Graviton-Pol braucht unendlich viele Hoeherspin-Austausche (Turm) auf Baumniveau.
- E6 (Gegensweep, staerkste Gegenposition zu B): CEMZ Fn. 23 plus Caron-Huot u. a. 2201.06602 ("higher-spin states" bei M,
  mit nur logarithmischer IR-Abhaengigkeit) -> wer A vertritt, sagt: der Log ist harmlos (doppelt-logarithmisch schwach),
  die Skala bleibt bis auf log festgelegt. Erwartung: A in **schwacher** Fassung (Skala bis auf Log, nicht "unendlicher
  Turm") ist in D = 4 gezeigt; A in **starker** Fassung (CEMZ-Turm) nicht.

Grundhypothese [H0], Zwei-Regime-Vorannahme: Die Studien sampeln verschiedene Kausalitaetskriterien. Vermuteter Moderator:
**Behandlung der IR-Divergenz in D = 4** (Gao-Wald-Abzug / m_IR-Regulator / b_max-Abschneiden gegen "asymptotisch exakt").
Mit Abzug: Turm-artige Aussage moeglich (CEMZ S. 25); ohne: keine asymptotische Voreilung (Bucciotti).

## 2. Abrufprotokoll (Erwartung -> Befund)

- **R1 (Abruf ab 20:16:51, Eintrag 20:19, date davor 20:18:46) Caron-Huot, Li, Parra-Martinez, Simmons-Duffin (CHLPSD),
  "Causality constraints on corrections to Einstein gravity", arXiv:2201.06602v1, JHEP 05 (2023) 122;
  quellen/2201.06602.pdf (sha256 86365bcb25e81c062dbbdb14ff3a2ff454f4f33ea94efec79c4323e31bfc53d4), pdftotext -layout.
  [A]** Erwartung E1 / K2. Befund: **VERLETZT (gross) -> Analysezyklus Z-1.**
  - Abstract (S. i): "four-dimensional weakly-coupled effective field theories ... two-sided bounds on gravitational Wilson
    coefficients in terms of the mass M of new higher-spin states ... prove the scaling with M expected from dimensional
    analysis (up to an infrared logarithm)".
  - Annahmen (S. 1-2, Abschn. 2.3 S. 8-10): bei kleiner Energie Graviton plus "a finite number of fields of spin <= 2";
    M^2 << Mpl^2 (Baumniveau); "We will use asymptotic causality, but crucially, imposed at all energy scales"; statt
    Froissart: verschmierte Amplitude |M_Psi(s)| <= |s| x const (Gl. 2.22-2.23), "conservative assumptions directly
    traceable to causality and unitarity".
  - Definition M (S. 1): "Denoting the mass of the lightest higher-spin state (spin 4 or higher) by M"; Abb. 8 (S. 26):
    "spin-4 mass gap M". Leichte Spin-0- und Spin-2-Felder unter M sind zugelassen und senken den Cutoff nicht
    (Abschn. 3.3, Gl. 3.8-3.10, S. 19-20: Matter-Beitraege vorzeichenfest).
  - Wirkung (Gl. 2.9, S. 4): S = 1/(16 pi G) Int sqrt(-g) [R - (1/3!)(alpha3 R^(3) + alpha~3 R~^(3)) + ...];
    g^3 = alpha3 + i alpha~3 (Gl. 2.11) -> **gerader und ungerader kubischer Vertex zusammen**.
  - Schranke (Gl. 4.4, S. 26, optimal): |g^3|^2 M^8 <= 24,9 log(M/m_IR) - 27,6 (Beispielfunktional Gl. 3.4a:
    37,8 log - 45,4).
  - IR (S. 15-16): "In spacetime dimensions D > 4 this removes all divergences. In D = 4, as we are considering in this paper,
    we will be left with infrared logarithms"; "finiteness on the graviton pole requires psi_i(p) to vanish faster than p at
    the origin, which is impossible for the Fourier transform of a positive function ... We then regulate by adding an
    infrared cutoff m_IR << M, and accept that this causes negativity at large impact parameters" (negativ erst bei
    b ~ m_IR^(-2/3)). S. 2: im AdS ersetzt durch log(M R_AdS), "We expect the same mechanism to apply to graviton
    scattering as well"; S. 3: "replace m_IR with the Hubble scale ... factor of only log M/m_IR ~ 100".
  - Schluss (S. 35): "if a higher-derivative correction were measured, corresponding to L = 1/(16 pi G)(R + r0^4 Riem^3 + ...),
    and if Nature respects causality as we understand it, then a spin-4 particle must exist whose Compton wavelength is at
    least as long as the length r0: M^-1 > r0." und "new higher-spin states must exist with mass M <~ r0^-1 or lighter".
    Fn. 14 (S. 34): "we ignore infrared logarithms since (log M R_Universe)^(1/4) <~ 3".
  - Abschn. 3.5 (S. 24-25), Verhaeltnis zu CEMZ: die CEMZ-Zeitverzoegerungsmatrix ist in den Summenregeln enthalten;
    -B(b)|low = 4G [[log(1/(b m_IR)), 24 g^3/b^4],[24 g^3*/b^4, log(1/(b m_IR))]] (Gl. 3.25), parametrisch
    |g^3| <~ log[1/(b m_IR)]/M^4 (Gl. 3.28). "Ref. [7] further argued that an infinite tower of higher-spin states needed to
    appear." -> **den unendlichen Turm leiten CHLPSD nicht selbst her**, sie referieren ihn. "the physical assumptions are
    quite distinct ... we consider Gs << 1 where the tree-level approximation is sufficient"; S. 36: "imposing a quantum
    notion of causality based on commutators and crossing symmetry, rather than a classical one based on time advances".
  - Nicht gezeigt: Kopplung der Hoeherspin-Zustaende an SM-Materie: "The task of bounding their couplings to Standard Model
    fields is left to future work" (S. 2); Fuenfte Kraefte aus Spin 0/1 "unconstrained by our arguments" (S. 2).
- **Analysezyklus Z-1 (Eintrag 20:19) - Korrektur von E1 und K2.**
  - Es gibt eine D = 4-Fassung mit expliziten Annahmen, und sie gibt mehr als "Schranken in Einheiten einer Skala": Die
    Skala ist ausdruecklich die Masse des leichtesten Zustands mit Spin >= 4, und die Aussage lautet "ein Spin-4-Teilchen muss
    existieren" mit M <~ 1/r0, bis auf (log)^(1/8). Das ist der Kern von Glied-7-massiv in D = 4, als Satz unter Axiomen.
  - **[ES] Rechnung (Kopf, keine Software):** fuer M ~ 1/(30 km) ~ 6,6e-12 eV und m_IR = H0 ~ 1,5e-33 eV ist
    ln(M/m_IR) ~ 50, also (24,9 x 50 - 27,6)^(1/8) = 1217^(1/8) ~ 2,4. Mit Hubble-Regulator liegt der Spin-4-Zustand also
    hoechstens ~2,4-fach ueber 1/|g^3|^(1/4). Fuer m_IR -> 0 wird die Schranke leer (log -> unendlich).
  - Nicht gezeigt bleibt: (i) der **unendliche** Turm (nur referiert), (ii) Strenge in streng flachem D = 4 (Negativitaet bei
    b ~ m_IR^(-2/3) wird "akzeptiert"), (iii) Kopplung an SM. Korrigierte Erwartung: Regime A in **schwacher Fassung**
    ("mindestens ein Spin->=4-Zustand bei <~ 1/r0, bis auf IR-Log; gerader und ungerader R^3") steht seit 2022 in D = 4
    unter expliziten Annahmen; Regime A in starker CEMZ-Fassung (unendlicher Turm, CTC-Begruendung) nicht.
  - **[ES] Wichtig fuer RUNDE-11 V1:** Der Einwand "Zeitmaschine nur fuer D > 4" (CEMZ Anh. G, Bucciotti 2026) trifft die
    CHLPSD-Route nicht, denn sie begruendet die Krankheit nicht ueber CTCs, sondern ueber Kommutatoren, Kreuzung und
    Analytizitaet. Die D = 4-Frage verschiebt sich von "Ist Voreilung krank?" zu "Gelten Analytizitaet, Kreuzung und
    verschmierte Regge-Schranke in D = 4 trotz IR-Divergenz, und darf man m_IR endlich setzen?"
- **Vorab R2 (date 20:19:35), arXiv-API id_list, zehn Abstracts aus der RUNDE-11-INSPIRE-Liste:**
  2410.21499, 2412.17902, 2512.13780, 2603.15755, 2609.16896, 2606.02729, 2512.15927, 2411.12428, 2504.14434, 2607.05503.
  Erwartung E5': (a) 2512.13780 "Positivity with long-range interactions" behandelt genau die D = 4-IR-Frage; ~35 %, dass
  es IR-sichere Schranken ohne m_IR liefert (staerkt A), ~65 %, dass Logs bleiben oder neue Annahmen noetig sind.
  (b) 2603.15755 "Negative running": Schleifen-Laufen in D = 4 macht Positivitaet bei tiefer Energie verletzbar (staerkt B,
  betrifft eher g4 als g3). (c) 2410.21499: Graviton-Pol braucht unendlich viele Hoeherspin-Austausche, eher allgemeines D.
  (d) 2606.02729: Kausalitaet in D = 4 nur "probabilistisch" wegen Gravitonfluktuationen; Richtung unklar.
  (e) Keine der zehn rechnet eine D = 4-Zeitmaschine (K3).
- **R2 (Abruf 20:19, Eintrag ~~20:2x~~ vor 20:20:22, date danach; "20:2x" war keine Messung) arXiv-API, quellen/abs-r2.xml (sha256 siehe SHA256SUMS.txt). [S]** Befund je Zeile:
  - (a) Bellazzini, Berman, Isabella, Riva, Romano, Sciotti, arXiv:2512.13780v2 (12/2025), "Positivity with Long-Range
    Interactions": IR-endliche, analytische, kreuzungssymmetrische, Regge-beschraenkte Amplituden M_E, "labeled by the
    experimental energy resolution E for detecting soft photons and gravitons ... suitable for deriving infrared-safe
    positivity bounds ... even in D=4"; Beispiel nur Pionen + Elektromagnetismus + Gravitation. -> **E5'(a) teilweise
    verletzt:** Der IR-sichere Rahmen fuer D = 4 existiert seit 12/2025; ob er auf Graviton-R^3 angewandt ist und ob log E an
    die Stelle von log m_IR tritt, sagt das Abstract nicht -> Volltext (R4).
  - (b) Fernandez, Ruhdorfer, Serra, arXiv:2603.15755v2 (03/2026): Ein-Schleifen-Laufen in D = 4 macht fuehrende
    Koeffizienten (Skalare, Photonen, Gravitonen) zum IR hin kleiner ("negative running"); gravitative IR-Beitraege "after
    smearing over the momentum transfer, are argued to dominate", sofern die Zahl nichtminimal gekoppelter Teilchen der
    Artenschranke genuegt. -> E5'(b) **bestaetigt in der Sache, aber Richtung umgekehrt**: die D = 4-Schranken werden
    gerettet ("argued"), nicht gekippt. Betrifft fuehrende (quartische) Operatoren, nicht direkt g^3.
  - (c) Haering, Zhiboedov, arXiv:2410.21499v1 (10/2024): Graviton-Pol in zweifach subtrahierten Dispersionsrelationen;
    grosse b: Eikonal als universeller Mechanismus; kleine b: "can arise from stringy higher-spin resonances"; Tauber-Satz
    in flachem Raum. -> E5'(c) bestaetigt (eine Zeile), keine D = 4-Sonderaussage im Abstract.
  - (d) Cintia, Piazza, Ramos, arXiv:2606.02729v3: Lichtkegel-Unschaerfe Var(dx) = 4 G T t/3 in thermischem
    Gravitonzustand. -> E5'(d): kein Bezug zu R^3/Turm; ausgesondert.
  - (e) Keine der zehn rechnet eine D = 4-Zeitmaschine (K3 bisher nicht getroffen). Kehagias/Riotto 2411.12428 [S] wenden
    CEMZ ohne D-Vorbehalt auf Schwarzschild/Kerr an ("either negligible or vastly suppressed"). Grojean/Jiang/Vuong
    2512.15927v2 [S] (JHEP angenommen): D = 4-Stosswelle; "In contrast to the neutral (Schwarzschild) case, where higher
    derivative operators leave the shockwave geometry unchanged" -> Hintergrund-Stosswelle in D = 4 ungeaendert, der
    Effekt liegt im Probe-Vertex. Lippstreu 2609.16896 [S]: IR-skalenfreie Schranken in einem nichtrelativistischen Modell
    ("spurious infrared divergences" vermeidbar). Das Haering/Zhiboedov-Paket, Das/Sinha 2607.05503 (D = 6) und Lanosa/
    Santillan 2504.14434 (Stelle-Eikonal) tragen zur D = 4-R^3-Frage nichts bei.
- **Vorab R3 (date 20:20:34), INSPIRE refersto:arxiv:2201.06602, de >= 2024-10 (24 Monate):** Erwartung E7: 80-150 Treffer;
  darunter Anwendungen/Erweiterungen der D = 4-Schranken (Photonen, Skalare, Gravitonen), hoechstens eine Arbeit
  (~30 %), die Graviton-R^3 in D = 4 IR-sicher ohne m_IR begrenzt; keine Arbeit, die CHLPSD in D = 4 ausdruecklich
  bestreitet (~75 %); Alexander/Bernardo/Yunes 2506.14889 als Phaenomenologie-Gegenlager.
- **R3 (Eintrag 20:21:17) INSPIRE.** Erste Abfrage mit "refersto:arxiv:2201.06602" lieferte 141444 Treffer (Syntax griff nicht,
  Ergebnis verworfen, Datei geloescht). Record-IDs per arxiv:-Suche: CHLPSD = recid 2012035 (195 Zitate), CEMZ = recid 1307098
  (742 Zitate; **CEMZ-Nummer 1407.5597 damit auch per API bestaetigt**). Dann refersto:recid:2012035 und de > 2024-09-30:
  **93 Treffer**, quellen/insp-cites-chlpsd-24m.json. [S, nur Titel] Erwartung E7: Zahl im Rahmen; **keine Arbeit mit Titel,
  der CHLPSD in D = 4 bestreitet** (vorlaeufig bestaetigt). Kandidaten fuer Gegenrichtung nach Titel: 2501.17949 "Graviton
  loops and negativity" (c=39), 2501.18465 "The EFT bootstrap at finite M_PL" (c=40), 2512.24474 "Tracking S-matrix bounds
  across dimensions", 2606.19432 "Partial-wave unitarity and long-range interactions", 2604.15235 "Sampling the Graviton Pole
  and Deprojecting the Swampland", 2512.11955 "Completeness from gravitational scattering", 2506.09884 "Bootstrapping Gravity
  with Crossing Symmetric Dispersion Relations".
- **Vorab R4 (date 20:21:17), arXiv-API, Abstracts dieser sieben:** Erwartung E8: 2501.17949 zeigt, dass Graviton-Schleifen in
  D = 4 negative, log-verstaerkte Beitraege liefern, die naive Positivitaet bei kleiner Energie verletzen (staerkt B, eher fuer
  quartische Koeffizienten); 2501.18465 rettet Schranken bei endlichem M_Pl mit Zusatzannahmen; 2512.24474 verfolgt Schranken
  ueber D und zeigt das log-Verhalten bei D -> 4; keine der sieben zeigt einen unendlichen Turm in D = 4 ausdruecklich (~70 %).
- **R4 (Eintrag 20:21:49) arXiv-API, quellen/abs-r4.xml. [S]** Erwartung E8: **teilweise verletzt (mittel):**
  - Chang & Parra-Martinez, arXiv:2501.17949v2 (01/2025), "Graviton loops and negativity": Graviton-Schleifen erlauben
    "negativity of Wilson coefficients by an amount suppressed by powers of Newton's constant, G" (wie erwartet), aber:
    "In D=4, we observe that assuming that the eikonal formula captures the correct forward behavior of the amplitude at all
    orders in G, and for energies of the order of the EFT cutoff, yields bounds free of logarithmic infrared divergences."
    -> Der IR-Log in D = 4 ist **unter einer benannten Annahme** (Eikonal-Exponentiation zu allen Ordnungen in G) entfernbar;
    Abstract spricht von skalaren EFTs mit Gravitation, nicht von Graviton-R^3.
  - Beadle, Isabella, Perrone, Ricossa, Riva, Serra, arXiv:2501.18465, JHEP 06 (2025) 209: Schleifen und
    Vorwaertsdivergenzen; "a significant impact on bounds, even at tree level". Richtung (schwaecher/staerker) nicht im Abstract.
  - Plestid & Quilez Lasanta, arXiv:2606.19432 (06/2026): Partialwellen ohne "spurious dependence on the infrared regulator"
    durch Coulomb-Moden (Methode, kein Gravitations-R^3-Ergebnis).
  - Gumus/Metayer/Tourkine 2512.24474: massive Skalare, Knicke bei d = 5, 7; nichts zu D = 4-Gravitation.
  - Peng/Rodina/Tokareva/Xu 2604.15235: Graviton-Pol per "sampling", Ergebnisse D >= 5 (D = 5: M/M_P <~ 7,8); kein D = 4.
  - Pasiecznik 2506.09884v2: "new bounds on the coupling of gravitons to a massive spin-4 state at tree level" (v2 mit
    korrigierter Numerik).
  - Calisto u. a. 2512.11955, PRD 113, 106008 (2026): Vollstaendigkeit des Ladungsgitters aus gravitativer Streuung, braucht
    "a weakly coupled ultraviolet completion of gravity" (gleiche Annahmenfamilie, anderer Gegenstand).
  - Keine der sieben zeigt einen unendlichen Turm in D = 4 (E8-Teil bestaetigt).
- ~~**Vorab R5 (vor dem Lesen, ca. 20:21; date-Wert nicht vorab genommen, siehe Selbstanzeige S1):** Erwartung E9: Bucciotti
  u. a. erwaehnen die dispersive Route (CHLPSD) nur am Rand, ohne sie zu bewerten.~~ **Berichtigung (20:23):** E9 wurde
  erst **nach** dem grep auf die lokale Kopie geschrieben, also nicht vorab. Sie zaehlt nicht als Vorhersage; der Befund R5
  steht trotzdem, nur ohne Erwartungsvergleich (Selbstanzeige S1).
- **R5 (Eintrag 20:22:49) Bucciotti, Creminelli, Longo, McBlain, Trincherini, arXiv:2605.00089v1, lokale Kopie
  RUNDE-11/cemz-mess/quellen/2605.00089.txt (sha256 81666ec2...691f laut RUNDE-11), S. 3, 19-22, Lit. [30]-[43]. [A]**
  Erwartung E9 **VERLETZT (gross) -> Analysezyklus Z-2:**
  - S. 21 (txt Z. 1136-1145): "In the gravitational case, this second approach [Analytizitaet und Positivitaet der S-Matrix]
    encounters the same infrared logarithm ... a logarithm from the graviton loop remains, requiring an IR regulator - for
    example, a cosmological background - to extract finite bounds on Wilson coefficients. This logarithm in D = 4 is the
    scattering-amplitude manifestation of the same IR effect we identify geometrically."
  - S. 22 (Z. 1151-1166): "The absence of IR divergences in D > 4 means that standard positivity bounds ... apply without
    obstruction"; S-Matrix-Weg "has the practical advantage of not requiring a verification that closed timelike curves can be
    constructed ... On the other hand, it requires assumptions about the UV behaviour of the amplitude, in particular Regge
    boundedness, and the analyticity properties themselves become less transparent once Lorentz symmetry is broken by a
    cosmological regulator." Zu Bellazzini u. a. [41] = 2512.13780: "Bounds derived from M_E retain a residual log E
    dependence ... Whether the positivity of M_E has a direct spacetime interpretation ... is an open question". Offen auch:
    Erweiterung auf de Sitter, "where the cosmological horizon provides a physically motivated IR regulator in D = 4".
  - S. 3-4 (Z. 194-200): AdS-Regulator macht Rechnungen endlich, aber "in the large L limit, the IR effects ... reappear ...
    causality bounds derived in AdS remain fundamentally dependent on the IR regulator and cannot be smoothly connected to
    flat-space physics."
  - S. 19-20 (Abschn. 4.2, Z. 1040-1090): CTC aus endlicher Voreilung in D = 4 braucht Boost gamma ~ e^(N/2), die
    Ueberlagerung aber Abstand ~ r_s e^N: "no obvious route from superluminality at large but finite distance to the
    possibility of building a CTC"; Vorbehalt: "it is still possible that CTCs may form in the non-linear regime".
    (Rechnung am F F R-Beispiel; Fn. 11: Graviton-Effektivmetriken folgen dort den Lichtkegeln des Hintergrunds.)
  - Fn. 9 (Z. 1146): Schleifen-Erweiterungen [31]-[33] = Beadle u. a. 2407.02346 (JHEP 08 (2025) 188), 2501.18465,
    Chang/Parra-Martinez 2501.17949 (JHEP 08 (2025) 175).
- **Analysezyklus Z-2 (Eintrag 20:22:49) - die beiden Lager streiten nicht ueber eine Rechnung, sondern ueber den IR-Regulator.**
  - Beide Seiten nennen **denselben** D = 4-Effekt: den IR-Logarithmus der Graviton-Austauschamplitude bzw. der
    Shapiro-Verzoegerung. CHLPSD: Schranke ~ (log(M/m_IR))^(1/8) in M, "incredibly conservative" mit Hubble-Skala.
    Bucciotti: mit m_IR -> 0 (bzw. L_AdS -> unendlich) verschwindet jede asymptotische Schranke; ein physikalischer
    Regulator (de Sitter) sei ein offener Weg.
  - **[ES] Zwei Regime, Moderator = IR-Skala R_IR:** endliches R_IR (Hubble, AdS, Detektoraufloesung E) -> Regime A in
    schwacher Fassung (Spin->=4-Zustand bei <~ (24,9 ln(M R_IR))^(1/8)/|g^3|^(1/4)); R_IR -> unendlich (streng
    asymptotisch flaches D = 4) -> keine Schranke (Regime B). Keine Seite irrt; sie sampeln verschiedene IR-Idealisierungen.
  - **[ES] Unterscheidungspunkt:** Die Regime trennen sich messbar nur, wenn (ln M R_IR)^(1/8) gross wird. Fuer Faktor 10
    braucht es 24,9 ln(M R_IR) ~ 1e8, also R_IR ~ l e^(4e6). Fuer jedes physikalische R_IR (Hubble: Faktor ~2,4;
    R_IR = 1e100 x Hubble: ~3,0) sind sie numerisch fast gleich. Kipp-Stelle ist also nicht ein Zahlenwert, sondern die
    Grenzwertbildung R_IR -> unendlich und die Frage, ob Analytizitaet/Kreuzung mit kosmologischem Regulator gelten
    (Bucciotti S. 22: "less transparent").
- **Vorab R6 (date 20:23:03), arXiv-API-Volltextsuche in Abstracts 2024-10 bis 2026-10 zu K3:** Suchen (a) abs:"closed timelike"
  UND abs:shock, (b) abs:"time machine" UND abs:graviton, (c) abs:"time advance" UND abs:"four dimensions" UND abs:gravit.
  Erwartung E4 (wiederholt): keine Arbeit rechnet eine D = 4-Zeitmaschine mit nichtstationaerer Stosswelle; hoechstens
  dS-Kausalitaet (McLoughlin/Rosen 2502.19616) und Einstein-Maxwell-Stosswellen.
- **R6 (Eintrag 20:24:00) arXiv-API, quellen/arxiv-r6a.xml, -r6b.xml, -r6c.xml. [S, Titel]** (Die erste Fassung mit
  submittedDate-Filter und Wildcard gab 0 Treffer; Syntax vermutlich falsch, deshalb ohne Datumsfilter, absteigend sortiert.)
  - (a) "closed timelike" UND "shock wave": 1 Treffer, gr-qc/0210048 (2002). (b) "time advance" UND graviton: 7 Treffer, neueste
    2506.14889 (Alexander/Bernardo/Yunes 2025), 2409.16935 (D >= 5), dazu aelter 2006.02375 "Eikonal phase matrix, deflection
    angle and time delay in effective field theories of gravity" (2020; **Nummer jetzt aus API**), 2007.01847, 1512.04952.
    (c) "closed timelike" UND EFT/hoehere Ableitungen: 5 Treffer, 2026 nur 2602.17724 (rotierende Skalar-Tensor-Raumzeiten)
    und 2602.06905 (rotierende Stringloesungen) - kein CEMZ-Stosswellenaufbau.
  - Erwartung E4 / K3 **bestaetigt**: Seit 2025 rechnet nach diesem Suchstand keine Arbeit eine D = 4-Zeitmaschine mit
    nichtstationaerer Stosswelle durch. Juengster Stand dazu ist Bucciotti 2026 Abschn. 4.2 (naive Ueberlagerung scheitert,
    nichtlinearer Bereich offen). **Urteil: nach Recherchestand nicht belegt** (API-Suche, keine Websuche; schwach).
- **Vorab R7 (date 20:24:00), Chang & Parra-Martinez, arXiv:2501.17949v2, Volltext, Abschnitt zu D = 4:** Erwartung E10: Die
  IR-log-freien D = 4-Schranken gelten fuer Skalar-plus-Gravitation und stehen unter der ausdruecklichen Annahme der
  Eikonal-Exponentiation bis zur Cutoff-Energie; fuer Graviton-R^3 (g^3) gibt es dort keine Aussage; die Autoren nennen
  es Beobachtung/Vermutung, nicht Satz.
- **R7 (Eintrag 20:24:45) Chang & Parra-Martinez, "Graviton loops and negativity", arXiv:2501.17949v2, JHEP 08 (2025) 175 (laut
  Bucciotti Lit. [33]); quellen/2501.17949v2.pdf (sha256 bd7c30d6bd1bf25c4ba9f0a1f49e918886a2249a327be4814b79f7f75f5f35a3),
  S. 3, Abschn. 5 (S. 31-40), Schluss S. 40-41. [A]** Erwartung E10 **im Kern bestaetigt** (nur Skalar plus Gravitation,
  Annahme ausdruecklich), mit einer Einzelheit, die traegt:
  - S. 3: in D = 4 Baumniveau g2 >= -25 x 8 pi G/M^2 log(0,3 M b_max); mit Eikonal-Annahme "finite bounds, e.g., of the form
    g2 >= -O(1)/M^4 ... These bounds are independent of G, so strictly speaking they go beyond the weak coupling limit".
  - S. 32: "we assume [the eikonal formula] describes the amplitude at small t at all orders in G"; S. 40: mit m_IR = Hubble
    ist die regulierte Schranke (g2 >~ -1e-27/M^4) "much stronger than" die resummierte.
  - S. 41-42 (berichtigt, ~~S. 41~~; der zweite Satz steht auf S. 42): "It would also be interesting to revisit the eikonal argument in section 5.2 and apply it to four-graviton
    scattering in D = 4" und "whether the eikonal formula really captures the forward behavior of gravitational amplitudes at
    finite G" -> **fuer Graviton-R^3 nicht gemacht**.
  - **[ES] Bedeutung:** Auch Regime B ist im strengen Grenzfall m_IR -> 0 nicht bewiesen. Die Leere der Schranke folgt aus
    der Rechnung fester Ordnung (Baum-Log); mit (angenommener) Eikonal-Resummation bleibt in D = 4 eine endliche, aber
    G-unabhaengige und damit schwaechere Schranke. Die tiefere Fassung der einen Voraussetzung ist also: **Wie verhaelt sich
    die D = 4-Gravitationsamplitude im Vorwaertslimes zu allen Ordnungen in G?** (Eikonal ja/nein.)
- **Vorab R8 (date 20:24:45), Beadle, Isabella, Perrone, Ricossa, Riva, Serra, arXiv:2501.18465 (JHEP 06 (2025) 209), Volltext,
  Gegensweep gegen Regime A:** Erwartung E11: D = 4 mit Gravitation; Konsistenz der Schleifenbehandlung verlangt ein
  minimales Impulsfenster bzw. ein m_IR, das selbst von G und M abhaengt; Baumniveau-Schranken werden um O(1) bis O(10)
  schwaecher, verschwinden aber nicht; kein Wort zu Hoeherspin-Pflicht bei R^3.
- **R8 (Eintrag 20:25:36) Beadle u. a., arXiv:2501.18465v1, quellen/2501.18465.pdf (sha256 27c1ad58d0900b3e882c2527fbdb386eeb726a71d1c2353cac925c8b1bb3b83d),
  S. 3, 5 (Gl. 4), Abschn. 3.1 (txt Z. 736-746), S. 23-24. [A]** Erwartung E11 **teilweise verletzt (klein):** Die Arbeit
  rechnet nicht in D = 4, sondern in "d = 5, 6, where the calculation is particularly well defined" (S. 3). Die "significant
  impact ... even at tree level" ist die Beschraenkung des t-Fensters durch das Verschmieren (|t| < M^2/2, S. 24), kein
  D = 4-Effekt. Fuer D = 4 steht nur eine Unmoeglichkeitsaussage: Bochner-Satz verlangt 4 - d + delta <= 0, "incompatible in
  d = 4 with the positivity of delta required by the Coulomb singularity" (Abschn. 3.1) - dieselbe Spannung, die CHLPSD S. 16
  mit m_IR ueberbruecken. S. 3: masselose Teilchen machen "the concept of tree-level and weak coupling effectively
  meaningless in such scenarios" (Vorwaertslimes). -> Gegenposition zu A **in der Strenge**, nicht im Ergebnis: eine
  strenge D = 4-Schranke mit positiven Funktionalen ohne IR-Schnitt gibt es nicht.

## 3. Gegensweep (Eintrag 20:26:07): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

1. **Dass CHLPSDs Axiom "verschmierte Regge-Beschraenktheit" in D = 4 begruendet ist.** CHLPSD S. 8-10 nennen es "conservative
   ... directly traceable to causality and unitarity"; Bucciotti S. 22 nennt Regge-Beschraenktheit als Annahme. -> geprueft (R9).
2. **Dass "ein Spin-4-Teilchen muss existieren" schon "unendlicher Turm" heisst.** CHLPSD leiten den Turm nicht selbst her
   (S. 25 referiert CEMZ). [ES/L?] Standardargument: endlich viele Austausche mit J >= 4 wachsen wie s^J > s^2 und verletzen die
   Regge-Schranke; also folgt der Turm aus denselben Axiomen. CEMZ Fn. 23 (S. 49, [A] RUNDE-11): "clear in D = 4". Nicht neu
   an einer D = 4-Quelle geprueft.
3. **Dass der Spin-4-Zustand an SM-Materie koppelt (EGHS-Abbildung, alpha ~ 1).** CHLPSD S. 2: "The task of bounding their
   couplings to Standard Model fields is left to future work"; Abschn. 4.5 (S. 33-35) nur Collider-Abschaetzungen ueber
   gravitative Produktion, "These estimates, if correct, challenge the notion that modifications of gravity at large scales
   could be hidden from colliders" [A]. -> Die D = 4-Route gibt Glied 7 massiv, aber **nicht** die Fuenfte-Kraft-Staerke.
4. **Dass "kubische Korrektur der Dreipunktkopplung" in D = 4 genau g^3 = alpha3 + i alpha~3 ist.** Geprueft: CHLPSD
   Gl. 2.6, 2.9-2.11 [A]; deckt sich mit EGHS S. 11 (RUNDE-11 [A]).
5. **Dass der Weinberg/Glied-7-masselos-Teil von alldem unberuehrt ist.** Nicht geprueft; [ES] CEMZ/CHLPSD handeln von
   **massiven** Zustaenden J > 2; Glied 7 im Wortlaut (masselos) bleibt Weinberg 1964.
- **Vorab R9 (nachtraeglich, Selbstanzeige S2):** Die INSPIRE-Titelsuche "Gravitational Regge bounds" lief um 20:25 **vor**
  einem schriftlichen Vorab-Eintrag. Meine nur gedachte Erwartung ("D > 4 gezeigt, D = 4 fuer IR-sichere Groessen vermutet")
  zaehlt deshalb nicht.
- **R9 (Eintrag 20:26:07) INSPIRE t "Gravitational Regge bounds": Haering & Zhiboedov, arXiv:2202.08280 (02/2022, 105 Zitate).
  [S, INSPIRE-Abstract]** "the assumption that scattering at large impact parameters is controlled by known semi-classical
  physics ... gravitational scattering amplitudes admit dispersion relations with two subtractions ... **The results obtained
  in the paper are valid for d > 4 for which the 2 -> 2 scattering amplitude is well-defined.**"
  - **[ES] Folge (vorlaeufig, bis Volltext R10):** Das Regge-Axiom, auf dem auch CHLPSD in D = 4 stehen, ist in seiner
    sorgfaeltigsten Herleitung nur fuer d > 4 gezeigt, weil die D = 4-Amplitude selbst nicht wohldefiniert ist. Damit haben
    **drei verschiedene Wege** (Zeitvoreilung/CTC, dispersiver IR-Log, Regge-Herleitung) in D = 4 **dieselbe** Bruchstelle:
    die IR-Divergenz des Graviton-Austauschs (1/t-Pol, Shapiro-Log, Coulomb-Phase). Regel 6: nicht die Bauteile vergleichen,
    sondern diese gemeinsame Groesse benennen.
- **Vorab R10 (date 20:26:07), Haering & Zhiboedov 2202.08280, Volltext, Stellen zu d = 4:** Erwartung E12: Sie schreiben, dass in
  d = 4 die Amplitude IR-divergent ist und man IR-sichere Observablen (inklusive Wirkungsquerschnitte oder "hard" Amplituden
  mit abgezogener Coulomb-Phase) braucht; sie vermuten, dass die s^2-Schranke dafuer gilt, beweisen es aber nicht.
- **R10 (Eintrag 20:27:24) Haering & Zhiboedov, "Gravitational Regge bounds", arXiv:2202.08280v2 (08/2022);
  quellen/2202.08280.pdf (sha256 18381124297299c4b33cabd5befd4793383a23dee73f3a7eee3f754f1e747eb9), S. 5, 6 (Fn. 18), 17
  (Abschn. "Four dimensions", Fn. 41). [A]** Erwartung E12 **bestaetigt** (eine Zeile mit Belegen):
  S. 17: "An immediate problem is that T(s, t) is not a well-defined observable in four dimensions ... the nonperturbative
  unitarity condition (3.13) needs to be formulated for the corresponding IR finite observables ... all the other assumptions
  such as analyticity, subexponentiality and crossing will have to be re-evaluated. Nevertheless ... we believe that the basic
  idea ... should eventually work." Fn. 18: "gravitons are good asymptotic states in d > 4 and not in d = 4."
  S. 5: d = 4 "requires a more careful treatment of the asymptotic states ... beyond the scope of the present paper".
- **Gegensweep-Befund 1 (Eintrag 20:27:24):** Die CHLPSD-Axiome "Analytizitaet, Kreuzung, verschmierte Regge-Schranke" sind fuer
  d > 4 begruendet, fuer D = 4 von den fuehrenden Autoren selbst als "re-evaluate" und "we believe ... should eventually work"
  markiert. **Korrigierte Erwartung:** Die D = 4-Fassung (CHLPSD) ist bedingt auf genau die Groesse, die auch Bucciotti und
  CEMZ in D = 4 umtreibt: das IR-Verhalten des Graviton-Austauschs (1/t-Pol -> Log; Gravitonen keine guten asymptotischen
  Zustaende). Regime A gilt **unter** dieser Voraussetzung, nicht ohne sie.
- **Vorab R11 (date 20:27:24), INSPIRE-Zitate von Bellazzini u. a. 2512.13780 (23 Zitate laut RUNDE-11-Liste) und Abstract-Scan:**
  Erwartung E13: keine Arbeit wendet die IR-sicheren Amplituden M_E bis 10/2026 auf Graviton-R^3 bzw. eine Spin->=4-Pflicht in
  D = 4 an (~75 %); Anwendungen auf Photonen/Pionen/Skalare und auf Euler-Heisenberg-artige Kopplungen.
- **R11 (Eintrag 20:28:29) INSPIRE refersto:recid:3093263 (= 2512.13780), 23 Treffer, quellen/insp-cites-bellazzini.json. [S]**
  Erwartung E13 **bestaetigt** (eine Zeile): keine der 23 wendet M_E auf Graviton-R^3 oder eine Spin->=4-Pflicht in D = 4 an.
  Naechstliegend: 2512.23791 "Energy correlators in four-dimensional gravity" (IR-endliche Observablen in D = 4, "analyticity
  and polynomial boundedness, allowing for the formulation of dispersion relations, which we explore"); 2607.14230 (D = 4,
  N = 8: Ecke "infinite spin tower amplitude" neben Virasoro-Shapiro); 2607.27300 ("graviton pole imposes unitarity constraints
  on UV spectrum").
- **Vorab R12 (date 20:28:29), Bellazzini u. a. 2512.13780v2, Volltext, nur: Sind externe Gravitonen bzw. Graviton-Selbstkopplungen
  abgedeckt, und wie geht log E in Schranken auf gravitative Kopplungen ein?** Erwartung E14: externe Teilchen sind massive
  bzw. Pionen/Photonen, Gravitonen nur als weiche Abstrahlung; Schranken mit Gravitation haengen von log E ab wie bei
  CHLPSD von log m_IR; kein R^3.
- **R12 (Eintrag 20:30:03) Bellazzini, Berman, Isabella, Riva, Romano, Sciotti, "Positivity with Long-Range Interactions",
  arXiv:2512.13780v2 (17.04.2026); quellen/2512.13780v2.pdf (sha256 2050cd823fd459614bc69344b628a9238d3b7596ea5dc799c939f4720ecf8104),
  S. 18 (Abschn. 5) und 30-31 (berichtigt, ~~S. 29-31~~; Schluss "Relation to previous literature"), Lit. [31], [39], [41], [69], [116]. [A]**
  Erwartung E14 **VERLETZT (gross) -> Analysezyklus Z-3.** Die Arbeit bewertet CHLPSD ausdruecklich:
  - S. 30: "Previous analyses established nontrivial gravitational bounds only for D > 4 [31] or in AdS spacetime [116], with
    the bounds disappearing as D -> 4 or the curvature is removed. In flat spacetime, working with IR-divergent amplitudes at
    fixed order in G (alpha) obstructs the existence of positive functionals: they must be integrable against the 1/t
    singularity, which fails in D = 4. **Introducing hard IR cutoffs by hand [31,39,41] does not resolve the issue: either the
    IR part of the dispersion relation diverges or the UV part becomes unconstrained.** Moreover, the unitarity and analytic
    properties of the regulated amplitudes remain unclear in this case, so as their meaning." ([39] = CHLPSD 2201.06602,
    Lit.-Liste txt Z. 2768.)
  - S. 31 zu Chang/Parra-Martinez [69]: "bounds derived from IR-divergent amplitudes can formally be written, but effectively
    reduce to trivial statements of the type g2 M^4 x 0 + 259 >= 0".
  - S. 30, ihr Ersatz: IR-endliche M_E mit endlicher Detektoraufloesung E, "should not be taken to zero"; kleiner Parameter
    G/G_E = 1/log(M/E). "The optimal detector ... GE -> infinity ... the resulting bounds trivialize, effectively mirroring the
    reappearance of IR divergences. Equivalently, the gravitational time delay required to reach such an enormous apparatus
    swamps any microscopic causality-violating effect." S. 18 (~~S. 29~~, berichtigt): mit M_E ist der Gravitationsterm "never logarithmically
    enhanced", Grenzfall G -> 0 glatt.
  - Angewandt nur auf Goldstone-Bosonen/Pionen mit Elektromagnetismus und Gravitation (Abschn. 6-7, Abstract); **keine
    Graviton-R^3-Schranke, keine Spin-4-Aussage** (grep: "four-graviton" nur in Literaturtiteln).
- **Analysezyklus Z-3 (Eintrag 20:30:03) - Gegensweep trifft:**
  - Die einzige explizite D = 4-Fassung (CHLPSD) steht auf einem harten IR-Schnitt, den die IR-Positivitaets-Gruppe
    2025/26 fuer **nicht tragfaehig** haelt (nicht nur "unbewiesen"). Haering/Zhiboedov (Amplitude in D = 4 nicht
    wohldefiniert) und Bucciotti (Analytizitaet mit kosmologischem Regulator "less transparent") zeigen in dieselbe Richtung.
  - **Korrigiertes Zwischenergebnis:** nicht "A bedingt", sondern **B im Ergebnis**: Die Kopplung "messbares g^3 -> Spin->=4
    bei derselben Skala" ist in D = 4 eine **behauptete Folgerung unter einer bestrittenen IR-Voraussetzung**; die IR-sichere
    Ersatzmethode (M_E) ist fuer Graviton-R^3 noch nicht durchgerechnet. Gegen die Karte bleibt: B nicht "ohne Turmzwang",
    sondern mit Spin-4-Pflicht im Inhalt, aber ohne tragfaehigen IR-Schritt.
  - **Zwei Regime, Moderator Detektor-/IR-Skala, jetzt mit Quelle:** endliche Aufloesung E (G_E = G log(M/E) klein) ->
    Schranken existieren (fuer Pionen gezeigt); E -> 0 ("optimal detector") -> Schranken trivial, deckungsgleich mit
    Bucciottis asymptotischem Befund. **[ES] Unterscheidungspunkt:** Grenze bei G M^2 log(M/E) ~ 1, also E ~ M exp(-1/(G M^2)).
    Fuer M ~ 1/(30 km) ~ 6,6e-12 eV ist G M^2 = (M/M_Pl)^2 ~ (5,4e-40)^2 ~ 3e-79, also E ~ M exp(-3e78): unerreichbar
    extrem. In unserem Universum liegt jeder physikalische Detektor im Regime "Schranke existiert" - **falls** die
    M_E-Methode auf Graviton-R^3 uebertragbar ist. Das ist die offene Rechnung.

## 4. Protokollschluss (date 2026-10-01 20:33:56 CEST)

- Bericht oben geschrieben ab 20:30:55. Danach habe ich Seitenangaben berichtigt und die alten Fassungen durchgestrichen stehen
  lassen: Bellazzini S. 29 -> S. 18, Chang/Parra-Martinez S. 41 -> 41-42. Im Kurzfazit habe ich ein Zitat auf den Wortlaut
  "[31,39,41]" zurueckgesetzt und den Exponenten 1/8 als [ES] markiert.
- quellen/SHA256SUMS.txt: 17 Dateien (5 PDFs mit pdftotext-Fassung, 5 API-XML, 2 INSPIRE-JSON), erzeugt 20:30:24, nach dem
  letzten Abruf.
- Eine Sicherungskopie vor der Seitenberichtigung liegt nur im Sitzungs-Scratchpad, nicht im Projekt.
- Nicht gemacht: python, python3, awk, git, Peerbus, Unteragenten, Websuche. Keine Aenderung an WARUM-SPIN-2.md, CEMZ-MESS.md
  oder CEMZ-EBENE.md. Keine Sperrpfade.
- Ende: 2026-10-01 20:33:56 CEST, innerhalb der Zeitbox (bis 21:03:20).
