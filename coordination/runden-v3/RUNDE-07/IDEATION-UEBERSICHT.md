# Ideation-Uebersicht: alle Analogie-Ideen und Karten der Nacht zum 30.09.2026

- **Auftrag:** claude-primary (Leitung), nach Finn im Chat: "mach noch mal einen subagent und prüfe alle der ideation
  modelle die wir mit analogien gemacht hatten noch mal durch ...". Teil A dieses Auftrags; Teil B steht in
  GAUNTLET-NEUSTART-PLAN.md daneben.
- **Bearbeiter:** Anthropic-Subagent (Opus 5.5). Nur gelesen und diese zwei Dateien geschrieben; nichts gerechnet, kein
  ssh, kein git, kein Peerbus. Gesperrte Pfade nicht geoeffnet.
- **Beginn (date):** 2026-09-30 04:04:02 CEST. Schreibbeginn dieser Datei 04:14:56 CEST.
- **Ende (date):** 2026-09-30 04:26:29 CEST (gemessen nach dem Schreiben)
- **Stand:** RUNDE-06 und RUNDE-07 sind nicht abgeschlossen. Gelesen ist der Stand zwischen 04:04 und 04:17:
  RUNDE-06.md (Fassung 03:50, Abschaetzung "wird gefuellt"), ERGEBNISSE-R6-A.md, ERGEBNISSE-R6-B.md (Ende 04:04:59),
  RUNDE-07.md (Karten angelegt, keine Ergebnisse). Die M1-Medium-Laeufe der .69 lagen ab etwa 04:07 in
  RUNDE-06/medium1d/lauf-69/ (nur die Berichtskoepfe gelesen, keine Ernte). M2 (medium2d) und die 2D-B-Karten
  gluehwurm, haendigkeit, isomere und kollektiv hatten lokal nur Formproben.
- **Explorativ.** Alle Urteile sind Urteile der Runden (v3), keine formale Bestaetigung. Wo die Leitung noch nicht
  entschieden hat, steht der Vorschlag des Ernte-Agenten mit "V".

## Kurz

1. **131 Karten** gesichtet: die 90 Analogie-Ideen (Biologie 50, Chemie 20, Wellen/Wind/Segeln 20) und 41 weitere
   Karten (Finn, Fable, Reflexion, Recherche, arXiv-Runde).
2. **97 haben ein eigenes Testergebnis** (Rechnung oder Papier), 2 sind durch andere Tests mit abgedeckt, **32 sind
   ungetestet** (davon 6 laufen gerade in Runde 7 oder M2).
3. **Leitungsstand:** 19 weiter, 49 parken, 11 verwerfen, 18 mit Ergebnis, aber ohne Abschaetzung (vor allem Runde 6).
   Von den 90 Analogien gehen 15 weiter, fast alle nur in umgebauter Form (Zwei-Feld-Medium, Ringe, Kavitation).
4. **Auswahl gegen Zufall (v3, Abschnitt 4):** Die gewaehlten Karten der Runden 1 bis 4 ergaben 4 von 27 "weiter"
   (15 %), die Zufallskarten 1 von 5 (20 %). Unsere Auswahl war bisher nicht besser als Wuerfeln; fuer einen Schluss
   sind es zu wenige Zufallskarten.
5. **Tragfaehig** sind vor allem Befunde am festen Modell (Resonanz und Breitennullstelle in 3D, Tropfenbild,
   Teilchenverhalten an Stufen) und zwei Modellvarianten mit echtem Parameterraum: die Potentialfamilie beta (samt
   Log-Potential) und das Zwei-Feld- bzw. Mediummodell (lam, eps, m_chi, C0). Nur diese zwei eignen sich als
   Population einer Modellsuche (Teil B).

## Lesehilfe

- **getestet:** Runde und Testname. "R5-B fuettern" heisst Paket R5-B, Unterbefehl fuettern. M1 und M2 sind die
  Medium-Pakete aus Runde 6.
- **Abschaetzung:** weiter, parken, verwerfen (Leitung, letzter Stand); **offen** = Ergebnis liegt vor, Leitung hat
  noch nicht entschieden (V = Vorschlag des Ernte-Agenten); **ungetestet**; **indirekt** = keine eigene Karte, aber
  durch einen anderen Test beantwortet.
- **Modellbezug:** Legt die Idee eine Modellvariante oder einen Modellparameter fest, der in eine Modellsuche eingehen
  kann? Kuerzel:
  - **beta**: Potentialfamilie U = S - S^2 + beta S^3 (unser Modell beta = 1/2)
  - **log**: Affleck-Dine-artiges Log-Potential
  - **2F**: zwei Felder schwer/leicht mit lam (Dichtekopplung), eps (Mischung), m_chi (leichte Masse), a (Wandkopplung)
  - **MED**: stabiles chi-Medium (C0, g4, lam)
  - **m**, **Ring**: Windung bzw. Mehrball-Verband. Das sind **Zustaende** eines festen Modells, keine Modellparameter.
  - **—**: Dynamik im festen Modell, kein Suchparameter.
- Zahlen stammen aus den genannten Runden- und Ergebnisdateien; ich habe keine Zahl neu gerechnet.

## 1. Zaehlung

| Quelle | Karten | Ergebnis | weiter | parken | verwerfen | offen | ungetestet | indirekt |
|---|---|---|---|---|---|---|---|---|
| Biologie (RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md) | 50 | 42 | 7 | 25 | 7 | 3 | 6 | 2 |
| Chemie (RUNDE-03/IDEEN-20-QBALL-CHEMIE.md) | 20 | 18 | 2 | 14 | 1 | 1 | 2 | 0 |
| Wellen, Wind, Segeln (RUNDE-03/IDEEN-20-...-SEGELN.md) | 20 | 16 | 6 | 7 | 2 | 1 | 4 | 0 |
| **Summe Analogien** | **90** | **76** | **15** | **46** | **10** | **5** | **12** | **2** |
| Finn F-1 bis F-5 und Finns Rechenauftraege (3D-Resonanz, Weber) | 9 | 8 | 1 | 1 | 1 | 5 | 1 | 0 |
| Fable KF-1 bis KF-5 | 5 | 3 | 0 | 0 | 0 | 3 | 2 | 0 |
| Reflexion R-1 bis R-5 | 5 | 5 | 1 | 0 | 0 | 4 | 0 | 0 |
| Recherche MT-1 bis MT-3, V-1 bis V-3, RG-1 | 7 | 1 | 0 | 0 | 0 | 1 | 6 | 0 |
| arXiv-Runde K-1 bis K-12, QG-1 bis QG-3 | 15 | 4 | 2 | 2 | 0 | 0 | 11 | 0 |
| **Summe alle** | **131** | **97** | **19** | **49** | **11** | **18** | **32** | **2** |

"Ergebnis" = weiter + parken + verwerfen + offen. Eine Karte F-4 gibt es in den gelesenen Dateien nicht; die Nummer ist
uebersprungen oder nie aufgeschrieben. Finns weitere Fragen der Nacht (Reflexion, Weber, Fuettern) stehen unter
R-1 bis R-5, WEBER und Bio 3/36.

## 2. Tabelle je Idee

### 2.1 Biologie (50)

| Kennung | Idee | getestet | Ergebnis | Abschaetzung | Modellbezug |
|---|---|---|---|---|---|
| Bio 1 | duenne Wand als Membran, Young-Laplace | ja, R5-A membran | Young-Laplace auf 1 bis 4 % | parken (Tropfenbild bestaetigt) | — (Kontrolle Tropfenbild) |
| Bio 2 | Osmose: Ball gleicht omega an das Hintergrundpotential an | ja, R5-C osmose; M1 osmose (.69) | Ein-Feld: Ball loest sich im dichten Hintergrund auf; Medium: Vorzeichenwechsel bei C = 0,184 statt naiv 0,20 (nicht geerntet) | parken (Ein-Feld), Medium offen | MED (C0, eps) |
| Bio 3 | Fuettern: Einfang setzt Bindungsenergie frei | ja, R5-B fuettern | ueber der Schwelle 4 bis 6 % behalten (Born); unter der Schwelle 2,4 % gegen die Papierrechnung, Gegenprobe reisst | weiter (R7 R5F b) | — |
| Bio 4 | Tod unter Q_min, schlagartig | ja, R5-A tod | kein schlagartiger Tod; haelt bis 0,70 bis 0,83 Q_min, omega 1,007 > 1 kurz vor dem Ende | weiter (R7 R5F a) | — |
| Bio 5 | Teilung eines m = 2-Balls | ja, 2D-A teilung | kleine m = 2 teilen sich (0,65; 0,80) in 2 bis 4 Toechter, grosse (0,55) nicht | parken | m |
| Bio 6 | Endozytose je nach Phase | nein (keine eigene Karte) | R2 Test 3K und R3 t3: gleichphasig verschmelzen, gegenphasig abprallen; Battye und Sutcliffe | indirekt | — |
| Bio 7 | Vesikel, Q-Schale | ja, 2D-A schale | ohne Windung fuellt sich das Loch (t = 26), mit Windung bleibt ein Wirbelkern, m = 3 haelt als Ring | parken | m, Ring |
| Bio 8 | Zellkern aus zwei Feldern | ja, R5-D zellkern | Verschachtelung folgt schon aus der Breite 1/m | verwerfen (vorab ableitbar) | 2F (Massen) |
| Bio 9 | circadiane Uhr, Kuramoto | ja, R2 | keine Synchronisation; gleichphasige Ketten verschmelzen | verwerfen | — |
| Bio 10 | Herzschrittmacher | ja, R2 | grosser Ball zieht kleinen nicht mit | verwerfen | — |
| Bio 11 | Gluehwuermchen, synchrones Atmen | nein (2D-B nur lokale Formprobe) | — | ungetestet | — |
| Bio 12 | chemische Uhr, Ladungspendeln | ja, R5-C pendeln | Takt 0,95 bis 1,03 der Vorhersage; Kontrolle freies Paar reisst; Literatur (Copeland u. a.) | parken | — |
| Bio 13 | Neuron mit Schwelle | ja, R4 neuron | keine Schwelle, glatte Antwort | parken | — |
| Bio 14 | Ostwald-Reifung | ja, R2 (Codex, 3D); KF-5 (2D) | 3D: Netze, Zaehlung nicht konvergiert; 2D: getrennte Tropfen, Reifungsgesetz nicht gemessen | parken | — |
| Bio 15 | Raeuber und Beute | ja, R5-D raeuber | Josephson-Bild; Kontrolle "getrennt 40" reisst | parken (bekannt) | 2F (lam, eps) |
| Bio 16 | Symbiose, gebundenes Paar | ja, R5-C symbiose | kein Lauf gebunden; "abgestrahlt" groesser als der Verschmelzungsgewinn | parken | — |
| Bio 17 | Mutanten, Knotenbaelle | ja, R5-A mutanten | zerfallen nach 141 bis 368 zum Grundzustand; Rate haengt an der Aufloesung | parken | — |
| Bio 18 | Artbildung (Zufall R4) | ja, R4 artbildung | Familien monoton, keine Verzweigung | verwerfen (bekannt) | — |
| Bio 19 | Fitness E/Q | ja, R5-A fitness | E/Q streng fallend; folgt aus der Papierrechnung | verwerfen | — |
| Bio 20 | Katastrophe durch Rauschpuls | ja, R5-B rauschen | Schmelzschwellen geordnet (0,286 / 0,273 / 0,223), zwei Saaten; Verfolgung verliert den Ball ab eps 0,3 | parken | — |
| Bio 21 | Nische im Gradienten | ja, M1 nische (.69) | Ergebnis liegt vor, nicht geerntet; Ein-Feld-Fassung ist der freie Fall (bekannt) | offen | MED (Dichtegefaelle) |
| Bio 22 | Turing-Muster, Modulationsinstabilitaet | ja, R5-B mi | Verklumpung genau fuer S0 < 2/3 (bekannt); bei 0,72 trotzdem 20 Klumpen | weiter (nur Kavitation, R7 R5F c) | — |
| Bio 24 | Vielzeller, Verbund mit Phasen | ja, 2D-A vielzeller | Vierer-Ring mit Windung 2pi/4 blieb gegen die Vorhersage zusammen | weiter (R7 RING) | Ring |
| Bio 25 | Gewebe, Gitter | ja, 2D-B gitter (.69) | kein Gitter haelt: gleichphasig verschmilzt ganz, wechselphasig teilweise | offen (Vorhersage getroffen) | Ring |
| Bio 26 | Schleimpilz | nein (2D-B kollektiv nur Formprobe) | — | ungetestet | — |
| Bio 27 | Wundheilung | ja, R4 wunde | heilt, grosser Schaden schneller, bis 68 % abgestrahlt | parken | — |
| Bio 28 | Groessengrenze durch Wachstum | ja, 2D-A groesse | Messung unklar; die Kontrolle teilt sich auch ohne Fuettern | parken | m |
| Bio 29 | Windung als Gen | ja, 2D-A teilung | Toechter haben Windung 0; Drehung wird nicht vererbt | parken | m |
| Bio 30 | Epigenetik, globale Phase | nein (keine eigene Karte) | durch die Phasentests aus R2 und R3 mit beantwortet | indirekt | — |
| Bio 31 | Gedaechtnis, zwei Aeste | ja, R2 (3D radial) | kein Bistabil; Q_min = 111,84 bei omega^2 = 0,927; duenner Ast VK-stabil | parken (bekannt) | beta (VK-Fenster) |
| Bio 32 | Immunsystem, Absorptionsspektrum | ja, R2, Codex, Feinrechnung | langlebige ausleckende Resonanz bei nu - omega = 1,494, zwei Haeuser | parken (bekannt); Linie lebt als 3D-Resonanz weiter | beta (Resonanz) |
| Bio 33 | Virus (Zufall R2) | ja, R2 und Test 3K | Verschmelzen nur bei gleicher Frequenz und kleinem Tempo (L3 32/32) | weiter; Folgekarte KF-2 nie gerechnet | — |
| Bio 34 | ATP, Ladung als Waehrung | ja, mit Bio 19 | wie Bio 19 | verwerfen | — |
| Bio 35 | Mitochondrium, zweites Feld im Ball | ja, R5-D mitochondrium | Gast ruht innen, bei v = 0,2 gefangen, entkommt bei 0,4 | parken (in F-5 aufgegangen) | 2F (lam, Massen) |
| Bio 36 | Photosynthese | ja, R5-B photo | Sprung Faktor 18 bzw. 13 an der Schwelle; Aufnahme auch unter der Schwelle | weiter (mit Bio 3) | — |
| Bio 37 | Fieber, Schmelzen | ja, mit Bio 20 | wie Bio 20 | parken | — |
| Bio 38 | Winterschlaf nahe der duennen Wand | ja, R5-B winterschlaf | Antwort steigt 15,8-fach; Linie 1,4875 nahe der Resonanz 1,4938 | parken | — |
| Bio 39 | Quorum Sensing | ja, R5-C quorum | entkoppelte Kontrolle reisst (r faellt von 0,995 auf 0,61) | parken | — |
| Bio 40 | Schwarm | nein (2D-B kollektiv nur Formprobe) | — | ungetestet | — |
| Bio 41 | Nervenfaser | ja, R4 nerv | "Geschwindigkeiten" bis 3,97 > c: Messgroesse falsch; L3 gerissen | parken | — |
| Bio 42 | Bienenwabe | ja, 2D-B gitter (.69) | wie Bio 25 | offen | Ring |
| Bio 43 | Q-Baelle als Keime der Struktur | nein (Papier angekuendigt, nicht berichtet) | Q-Ball-Dunkle-Materie ist Literatur | ungetestet | — |
| Bio 44 | Ursuppe, Affleck-Dine-Zerfall | nein (verwandt: Codex-Verdichtung, KF-5) | — | ungetestet | log |
| Bio 45 | dissipative Struktur mit Pumpe | ja, R5-B pumpe | kein stabiler getriebener Ball; mit Treiber schnellerer Zerfall | parken | Pumpe/Daempfung (Modellwechsel) |
| Bio 46 | Viruskapsid, Ringanalogon | ja, 2D-B ringe (.69) | kein Ring haelt; mitdrehende Ringe N6 und N8 verschmelzen zu einem Ball mit Windung 1 | weiter (R7 RING) | Ring, m |
| Bio 47 | Haendigkeit | nein (2D-B nur Formprobe) | — | ungetestet | — |
| Bio 48 | Altern ueber masselosen Kanal | ja, R5-D altern | Rate 0,61 bis 1,37 der Formel; negative Endladung, Bilanz unplausibel | parken (in F-5 aufgegangen) | 2F (m_chi = 0) |
| Bio 49 | Selbstreplikation | ja, 2D-A replikation | kein Zyklus, keine Rueckkehr zu m = 2 | verwerfen | m |
| Bio 50 | Lawinen am kritischen Punkt | ja, R5-C lawinen | Zaehler findet Lawinen auch ohne Stoesse (Kontrolle reisst) | parken | — |

### 2.2 Chemie (20)

| Kennung | Idee | getestet | Ergebnis | Abschaetzung | Modellbezug |
|---|---|---|---|---|---|
| Chem 1 | Elektronegativitaet = omega | ja, R3 t1 | d = 12 pendelt; d = 10 fliesst im Mittel klein -> gross | parken | — |
| Chem 2 | bindende und antibindende Ueberlappung | ja, R3 t2 | gleichphasig anziehend, gegenphasig abstossend | parken (negativ) | — |
| Chem 3 | Bindungskurve als Morse | ja, R3 t2 | einziges Minimum hat die Werte des verschmolzenen Einzelballs: **kein Molekuel** | parken (negativ) | — |
| Chem 4 | IR-Schwingung des Paars | ja, R5-C ir | Abstandsschwingung 0,99 bis 1,09 der Vorhersage | parken (bestaetigt) | — |
| Chem 5 | Isomere Kette gegen Dreieck | nein (2D-B isomere nur Formprobe) | — | ungetestet | Ring |
| Chem 6 | Puffer | nein (Paket 2D-C nie gestartet) | — | ungetestet | MED |
| Chem 7 | Aktivierungsenergie | ja, R3 t3 | gegenphasig nie verschmolzen, +-pi/2 prallt ab | parken (bekannt) | — |
| Chem 8 | Katalyse durch dritten Ball | ja, R4 katalyse | je ein v-Punkt knapp ueber der Schwelle | parken | — |
| Chem 9 | Massenwirkungsgesetz | ja, R5-C; M1 massenwirkung (.69) | Ein-Feld: Ball loest sich auf; Medium: nicht geerntet | parken (Ein-Feld), Medium offen | MED |
| Chem 10 | Uebersaettigung, Ausfaellung | ja, R5-B mi (mit Bio 22) | wie Bio 22 | weiter (Kavitation) | — |
| Chem 11 | Keimbildung | ja, R5-A keim | R_c = R_halb auf 0,1 % (fast vorab ableitbar); kappa bis 1,38 | parken | — |
| Chem 12 | Phasendiagramm | ja, 2D-A phasen | 5 von 9 Zellen wie vorhergesagt; kein Gas, kein Thermostat | parken | — |
| Chem 13 | Kristall mit wechselnder Phase | ja, 2D-B gitter (.69) | keine gemischte Phasenordnung haelt | offen (Vorhersage getroffen) | Ring |
| Chem 14 | Q/Anti-Q-Gitter (Zufall R3) | ja, R3 t5 | Zerstrahlung auch bei d = 8 und 12; Ball-Ball-Kontrolle reisst | parken | — |
| Chem 15 | Redox ueber Bruecke | ja, R3 t4 | kein exponentieller Abfall mit der Brueckenzahl | parken | — |
| Chem 16 | Kettenreaktion | ja, R4 kette | Reichweite 0 wie vorhergesagt | verwerfen | — |
| Chem 17 | Tensid an der Wand | ja, R5-D tensid | chi sitzt an der Wand (57 bis 74 %); Gegenprobe "Dichte" reisst | parken (in F5-2 aufgegangen) | 2F (a) |
| Chem 18 | magische Zahlen | ja, R5-A magisch | keine; Auffaelligkeiten nur am Gitterrand | parken | — |
| Chem 19 | Aromatizitaet im Ring | ja, 2D-B ringe (.69) | N6 gleichphasig verschmilzt, wechselphasig laeuft auseinander | weiter (als RING, R7) | Ring |
| Chem 20 | Chromatographie | ja, R4 | Ladungsverlust bis 53 %, 14 von 36 Zeiten fehlen | parken (Messung unbrauchbar) | — |

### 2.3 Wellen, Wind, Segeln (20)

| Kennung | Idee | getestet | Ergebnis | Abschaetzung | Modellbezug |
|---|---|---|---|---|---|
| Wel 1 | Russells Einzelwelle, Abstrahlung beim Stoss | ja, R4 russell | gleichphasig 3,6 bis 6,8 % abgestrahlt; L2 und L3 gerissen | parken | — |
| Wel 2 | Monsterwelle | ja, R4 monster | Ein-Feld-Hintergrund instabil, stabiles Medium defokussierend | verwerfen | MED |
| Wel 3 | Stokes-Drift | ja, R4; M1 stokes (.69) | R4: linear in a (Starteffekt); Medium mit Welle von weit: ~ a^2 (Exponent 1,99 / 2,03), L3 10/10 | weiter (Medium), M1 nicht geerntet | MED |
| Wel 4 | Kelvin-Kielwasser | nein (M2 laeuft, lokal nur Formprobe) | — | ungetestet | MED |
| Wel 5 | Rumpfgeschwindigkeit, Landau-Schwelle | ja, R3 t6 (Papier); M1 landau (.69) | Ein-Feld: keine Schwelle; Medium: u_c/c_s = 0,43 (C0 = 0,1) und 0,65 (C0 = 0,3), L3 22/22 | parken (Ein-Feld), Medium offen | MED |
| Wel 6 | Gleiten ueber der Rumpfgeschwindigkeit | ja, R5-C (Papier); M1 gleiten (.69) | Medium: groesste Kraft bei u = 0,30, bei u = 0,9 null | weiter (Medium), nicht geerntet | MED |
| Wel 7 | Windschatten | ja, M1 windschatten (.69) | Ergebnis liegt vor, nicht geerntet | weiter (Medium), nicht geerntet | MED |
| Wel 8 | Magnus-Effekt | ja, R3 (Papier) | im Ein-Feld nicht umsetzbar; M2 magnus laeuft | parken | MED, m |
| Wel 9 | Flettner-Rotor | ja, mit Wel 8 | wie Wel 8 | parken | MED, m |
| Wel 10 | Kreuzen mit zwei Kanaelen | ja, R5-D kreuzen; M1 landau | Mitnahme ueber c_s; das Rutschen unter c_s ist zum Teil echte Kraft (u_c < c_s) | weiter (Medium) | MED, 2F |
| Wel 11 | Fahrtwind, Bezugssystem | ja, M1 fahrtwind (.69) | nicht geerntet | weiter (Medium), nicht geerntet | MED |
| Wel 12 | Surfen | ja, R4 surfen | kein Mitnehmen; v_Ende ~ A^2 | parken | — |
| Wel 13 | Brandung an einer Dichterampe | ja, R4 brandung | 0 von 12 aufgenommen, 3 von 12 durchgereicht; Bilanz unlesbar | parken | MED |
| Wel 15 | Kaustik und Linse | nein (nur Papier im M2-Plan) | Brennweite vorab rechenbar | ungetestet | MED |
| Wel 16 | Tropfenschwingung nach Rayleigh | ja, R3 (2D), R6 (3D) | Rayleigh ohne freie Parameter auf 6 bis 7 %; 3D-l = 2-Mode im Rayleigh-Band | parken (bestaetigt) | beta (Tropfenbild) |
| Wel 17 | Kelvin-Helmholtz | nein (Papier, im M2-Plan geparkt) | — | ungetestet | MED |
| Wel 18 | Karman-Wirbelstrasse | nein (M2 wirbel laeuft) | — | ungetestet | MED |
| Wel 19 | Auge des Tornados | ja, R3 (m = 1 ungueltig), 2D-B profile (.69) | Kern haengt schwach von Q ab | offen | m |
| Wel 20 | Knoten, Hopf-Solitonen (Zufall R3) | ja, R3 (Papier) | Ein-Feld hat keine Knotenzahl | verwerfen (Ein-Feld); C x S^2 bei CX-1 geparkt | C x S^2 |

### 2.4 Finn F-1 bis F-5 und Finns Rechenauftraege

| Kennung | Idee | getestet | Ergebnis | Abschaetzung | Modellbezug |
|---|---|---|---|---|---|
| F-1 | Masse als stille Miniteile, Impuls in einer Extra-Richtung | ja, R1 (Papier) | KK-Q-Ball und Solitosynthese sind Literatur; die starke Fassung ist durch Daten ausgeschlossen | parken (bekannt) | — (KK-Turm nur Papier) |
| F-2 | Laenge regelt die Masse | nein als eigene Karte; RG-1 streift sie | RG-1-Nebenprobe: bei festem Q waechst E mit J mit Exponent 0,9 (kein starrer Rotor); Leptonverhaeltnisse nicht angefasst | ungetestet (teilweise) | m, Ring |
| F-3 | Nukleon als Q-Ball-artiger Klumpen | ja, R1 (Papier) | Tropfen statt Beutel; ein Beutel braucht ein zweites Feld (Friedberg-Lee) | verwerfen | 2F (Friedberg-Lee) |
| F5-1 | Q-Atom: leichte Teile schweben auf dem schweren Ball | ja, R6 (.69, CPU) | ein s-Niveau ab lam ~ -0,2; p erst, wenn s tachyonisch (im Raster; lam -0,6 bis -0,8 ungerechnet); 6 Atome stabil | offen (V weiter) | 2F (lam, m_chi) |
| F5-2 | Huelle auf der Wand | ja, R6 | a = 0,4 traegt (62 %); den instabilen Kern rettet sie nicht, sie beschleunigt den Zerfall | offen (V weiter) | 2F (a) |
| F5-3 | Mischung und Oszillation | ja, R6 | P_max und Perioden nach der Neutrino-Formel; Verdampfen 1,5- bis 4,4-mal langsamer als die Formel; gemischter Ball p = 0,996 stabil | offen (V parken) | 2F (eps, m_chi) |
| F5-4 | unsichtbarer Kern | ja, R6 | Vorzeichen der Kopplung sichtbar (R(+)/R(-) 6 bis 20); Flussleck ohne Kopplung | offen (V weiter) | 2F (lam) |
| 3D-RES | "mach das in 3d nach" (Resonanz) | ja, R6 | Pol 1,7018102 - 1,468e-3 i und Breitenminimum bei omega^2 ~ 0,7977, beide von zwei Haeusern | weiter (R7 BIC-2) | beta, log |
| WEBER | Tropfen-Zerspritzen mit der Weber-Zahl | ja, R6 | kein Zerspritzen bis We = 4,12; Teilchenschwelle auf Rasterbreite | offen (V: H verwerfen, Schwelle parken) | — |

### 2.5 Fable KF-1 bis KF-5 (REVIEW-FABLE-20260930/KARTEN-FABLE.md)

| Kennung | Idee | getestet | Ergebnis | Abschaetzung | Modellbezug |
|---|---|---|---|---|---|
| KF-1 | Zwei-Kanal-Streuung: Zwischenlager, Einfang, Verstaerkung | teilweise: R2-Feinrechnung (2F), R5-B fuettern | zweiter Kanal ueber nu = 2,673 bestaetigt (Antiteilchenstrom 3,3 bis 3,7e-4); Zwischenlager = quasinormale Mode; Verstaerkungsfaktor fuer Antiquanten nicht gemessen | offen (in der Resonanzlinie aufgegangen) | — |
| KF-2 | Fusionsfenster als Gerade in (Delta omega, v) | nein | Code aus R2 vorhanden | ungetestet | — |
| KF-3 | Todesschwelle eps_c im metastabilen Fenster | nein (verwandt: R5-A tod, R7 R5F a) | — | ungetestet | beta (Fenster) |
| KF-5 | Geburt in 2D: Netz oder Tropfen | ja, R6 (.69) | getrennte Tropfen, nie ein umspannendes Netz; Lage auf der Familie "nicht entscheidbar" | offen (V parken) | — |

### 2.6 Reflexion R-1 bis R-5 (RUNDE-06/KARTEN-REFLEXION-STABILISIERT.md)

| Kennung | Idee | getestet | Ergebnis | Abschaetzung | Modellbezug |
|---|---|---|---|---|---|
| R-1 | Bandlueckenschutz in einer Kette | ja, R6 | heller Pol N +- 20 %; Polsuche verliert Pole bei langen Ketten | offen (V parken) | Ring |
| R-2 | dunkler Zustand zweier Baelle | ja, R6 (linear und Zeit) | Abklingrate linear 1e-14 statt 1, zeitabhaengig 0,003 bzw. -0,0004; ungleiche Partner schuetzen nicht | weiter (an Codex, R7) | — |
| R-3 | Bindung durch Strahlung | ja, R6 | Kraft hoechstens etwa 6e-7, nur mit Pumpe | offen (V parken) | — |
| R-4 | Randreflexion taeuscht Stabilitaet vor | ja, R6 | Spiegel und Ring taeuschen Stabilitaet vor, der Schwamm nicht | offen (V weiter, Methodenkontrolle) | — |
| R-5 | Lokalisierung im Q-Ball-Gas | ja, R6 | Gas gleicher Baelle haelt 16 bis 34 %; Summenregel unvollstaendig | offen (V parken) | — |

### 2.7 Karten aus Recherchen (M-Theorie, Video, Regge)

| Kennung | Idee | getestet | Ergebnis | Abschaetzung | Modellbezug |
|---|---|---|---|---|---|
| MT-1 | Yukawa-Fingerabdruck von Turm, Geist und Skalar | nein (R7 Papier-Agent) | — | ungetestet (laeuft) | Spin-2-Kette (Papier), L5 ja |
| MT-2 | zaehlt der Ringturm wie ein String | nein | — | ungetestet (in R7 geparkt) | m, Ring |
| MT-3 | Nullstelle auch im Affleck-Dine-Log-Potential | nein (R7 BIC-2 b) | — | ungetestet (laeuft) | log, beta |
| V-1 | UV-Robustheit der Nullstelle (eps k^4) | nein; nur als Herkunft von BIC-2 genannt, nicht unter (a) bis (c) | — | ungetestet | UV-Dispersion eps |
| V-2 | Vorzeichen-Weiche bei Sub-mm-Abstaenden | nein (in R7 MT-1) | — | ungetestet (laeuft) | Spin-2-Kette (Papier), L5 ja |
| RG-1 | Regge-Turm drehender Q-Baelle | ja, R6 (Laptop) | alpha = 2,012, beta_Ring = 0,988; vorab aus der Ringform ableitbar | offen (V parken) | m |

### 2.8 arXiv-Runde vom 29.09. (Uebertragungen, keine reinen Analogien; kurz)

| Kennung | Idee | getestet | Ergebnis | Abschaetzung | Modellbezug |
|---|---|---|---|---|---|
| K-1 | B26 als angeregter Kern | nein | — | ungetestet (geparkt) | — |
| K-2 | fremde Latte Boson Star Factory | ja, R1 (Lesen) | ein Pruefbeispiel mit Potential S - S^2 + 0,275 S^3, Faktor-2-Unstimmigkeit | parken | beta (0,275 als Fremdpunkt) |
| K-3 | Nadel-Q-Baelle in L* | nein | — | ungetestet | C x S^2-artig (L*) |
| K-4 | Ist der drehende Hintergrund stabil? | nein (40 bis 80 min .69) | — | ungetestet (geparkt) | m |
| K-5 | Codex' H1 zerlegt | Hinweis (Codex) | Koerperorientierung ist nicht die Feldphase | weiter (bei Codex) | — |
| K-6 | VFW als Swarmalator (Zufall R1) | ja, R1 (TS440) | Synchronisation bekannt; K und Daempfung eingesetzt | parken (bekannt) | — |
| K-7 bis K-11 | Frequenzschuebe, Praezisionsprobe, Gitter-Pinning, Hubble-Schwelle AD-1, Vasiliev | nein | — | ungetestet (geparkt) | K-10: log (AD) |
| K-12 | fermionischer Nachbarast | nein | — | ungetestet (Vorschlag verwerfen) | Soler-Dirac (Modellwechsel) |
| QG-3 | J/Q = 1/2 ohne Spinor | nein | — | ungetestet | m, zwei Kanaele |

K-7 bis K-11 zaehlen in Abschnitt 1 als fuenf Karten.

### 2.9 Aeltere Ideation ohne Analogie-Charakter (nur Verweis)

- **coordination/ideation-20260925/** (I-1 bis I-18, Qwen Q-1 bis Q-12): Forschungs- und Datenideen (DR3/DR4-Basislinie,
  GaAs, Kontaminationszaehler). Keine Analogien, nicht aufgenommen. Stand dort in SYNTHESE-IDEATION-20260925.md.
- **coordination/ideation-20260923-ew-balls/** (EW-1 bis EW-3, EW-ASTRA-1 bis -3): Abbildung der elektroschwachen
  Baelle auf unser Programm. Fuer die Modellsuche wichtig ist nur EW-3 (Fortsetzung in beta) und EW-2 (unser Ast ist
  die kubisch-quintische NLS, Literatur).

## 3. Wo noch ungetestete Ideen stehen

- **Laufen gerade (6):** MT-1, MT-3, V-2, V-3 (Runde 7), Wel 4 und Wel 18 (M2 auf der .69). Dazu laufen Wel 8/9 und
  14 in der Medium-Fassung (M2 magnus, brechung); sie zaehlen oben als geparkt bzw. weiter.
- **2D-B nur Formprobe, Messlauf fehlt (5):** Bio 11 Gluehwuermchen, Bio 26 Schleimpilz, Bio 40 Schwarm,
  Bio 47 Haendigkeit, Chem 5 Isomere. Der Code r5_2d_b.py liegt bereit; auf der .69 liefen nur profile, paare,
  gitter und ringe.
- **Nie vergeben oder nur Papier (5):** Chem 6 Puffer (Paket 2D-C nie gestartet), Wel 15 Linse, Wel 17 KH (beide nur
  Papier im M2-Plan), Bio 43 und Bio 44 (Literaturkarten, nicht berichtet).
- **Fable-Karten mit fertigem Aufbau (2):** KF-2 Fusionsfenster und KF-3 Todesschwelle. Beide haben scharfe,
  vorab bezifferte Vorhersagen und brauchen nur vorhandenen Code (R2 bzw. radial).
- **Recherche (2):** V-1 (UV-Robustheit; nicht in BIC-2 enthalten), MT-2 (geparkt).
- **arXiv-Runde (11):** K-1, K-3, K-4, K-7 bis K-12, QG-2, QG-3. F-2 steht mit K-4/QG-3 zusammen.
- **Geerntet, aber nicht abgeschaetzt (18):** vor allem Runde 6 (F5-1 bis F5-4, KF-1, KF-4, KF-5, R-1, R-3 bis R-5,
  RG-1, WEBER) und die .69-Ergebnisse aus 2D-B (Bio 25/42, Chem 13, Wel 19) und M1 (Bio 21).

## 4. Wo Messungen unbrauchbar waren (Kontrolle oder Messgroesse gerissen)

| Runde, Test | Was riss | Folge |
|---|---|---|
| R3 t5 (Chem 14) | Ball-Ball-Kontrolle in 6 von 8 Laeufen; Einzel-Anti-Ball-Kontrolle fehlt | Zerstrahlungsbefund nicht belastbar |
| R3 Brechung 0 und 20 Grad | Ball im Randbereich, Fensterverlust 0,92 / 0,94 | in R6 als Messfehler bestaetigt |
| R3 2D-Profil m = 1 | Schiessfehler (Virialrest 8,4e-3) | in R5 2D-A berichtigt |
| R4 Russell | L2 und L3 gerissen | parken |
| R4 Nervenfaser | Geschwindigkeiten bis 3,97 > c, L3 gerissen | Messgroesse falsch definiert |
| R4 Chromatographie | bis 53 % Ladungsverlust, 14 von 36 Zeiten fehlen | unbrauchbar |
| R4 Brandung | negativer Seeanteil (-2,44), nur eine Seewand gemessen | unlesbar |
| R4 Stokes | Welle lag beim Start schon auf dem Ball | in M1 als Starteffekt erklaert |
| R5-B fuettern | Gegenprobe unter der Schwelle reisst; Quotienten nahe 0 | wird in R7 R5F b geklaert |
| R5-B mi, rauschen | g-Messgroesse unstimmig; Verfolgung verliert den Ball ab eps 0,3 | Teilaussagen |
| R5-C lawinen, quorum | Kontrollen ohne Stoss bzw. entkoppelt zeigen den Effekt auch | unbrauchbar |
| R5-C bragg, anderson | Kettenwerte T von -14565 bis 14396; periodische Gegenprobe daempft gleich | ersetzt durch R-1 und R-5 |
| R5-C symbiose, pendeln | abgestrahlt > Verschmelzungsgewinn; Nulldurchgaenge stufenabhaengig | Bilanzen unplausibel |
| R5-D altern, tensid, raeuber | negative Endladung; Gegenprobe "Dichte" reisst; Kontrolle "getrennt 40" | Teilaussagen |
| 2D-A groesse | Kontrolle teilt sich auch ohne Fuettern | unklar |
| R6 R-1, R-5 | Polsuche verliert Pole, Summenregel 0,52 bis 0,58 bzw. unvollstaendig; negative Raten | Polsummen unverlaesslich |
| R6 F5-4 | Flussleck ohne Kopplung (A = 5,4 %), T > 1 bei grossem k | Werte bei grossem k nur unter Vorbehalt |
| R6 KF-5 | Gegenprobe der Geschwindigkeitskorrektur (V11) verfehlt; L3 fuer s01 nicht bestanden | Familienfrage nicht entscheidbar |
| R6 3D-Nullstelle, Zeitbereich | lange Laeufe unter der Aufloesungsgrenze, Vorzeichen der Auswertearten uneinheitlich | nur die Polrechnung traegt; "exakt null" offen |
| 2D-B paare | L3 "bestanden: false" (Querbeschleunigung 12 % Aenderung) | nicht geerntet |

**Lehre aus Runde 5, von der Leitung schon gezogen:** L3 prueft nur grob gegen fein, nicht ob die Messgroesse
physikalisch ist. Je Test braucht es eine Plausibilitaetsschranke (0 <= T <= 1, Bilanzen, v < c).

## 5. Modellbezug: was in eine Modellsuche eingehen kann

Zustandsgroessen (omega, m, N, Phasenmuster) werden innerhalb der Bewertung eines Modells abgetastet. Ins Genom einer
Modellsuche gehoeren nur Parameter der Wirkung.

| Modellvariante | Parameter | Ideen | gelaufener Code, Parametrisierung heute | Stand |
|---|---|---|---|---|
| Potentialfamilie beta (mit S^4-Erweiterung) | beta; unser Modell 1/2, Ciurla-Probe 1/4, Fremdlatte K-2 0,275. Bis S^4 ist U = S - S^2 + beta S^3 + gamma S^4 nach Umskalieren von phi die allgemeine Form (eigener Schluss) | 3D-RES, MT-3, V-1, KF-3, Bio 31, 32, Wel 16, EW-3 | RUNDE-06/resonanz3d/resonanz3d.py: profil(), bruecke() und lin_aufbau() fuehren beta als Argument; pole_omega() und zeitlauf() lesen die Modulkonstante BETA = 0,5; kein --beta. Alle anderen Rundenskripte haben U = S - S^2 + S^3/2 fest | Breitenminimum nur bei beta = 1/2 bekannt; BIC-2 (b) prueft andere beta |
| Log-Potential (Affleck-Dine) | Log-Skala M, ggf. Zusatzmasse | MT-3, Bio 44, K-10 | kein gelaufener Code; BIC-2 (b) baut ihn in Runde 7 | offen |
| UV-Dispersion | eps (k^4-Term) | V-1 | kein Code | offen |
| Zwei Felder schwer/leicht | lam, eps, m_chi, a | F5-1 bis F5-4, Bio 8, 15, 35, 48, Chem 17, Wel 10, F-3 | RUNDE-05/r5d/r5d.py, r5d_f5.py; Parameter in den Testtabellen fest, nur --masse (0,3 / 0,6) | ein s-Niveau im Raster; Fenster lam -0,6 bis -0,8 bei m_chi = 0,6 ungerechnet |
| stabiles chi-Medium | C0, g4, lam | Wel 2 bis 18 (Medium), Bio 2, 21, Chem 6, 9 | RUNDE-06/medium1d/medium1d.py (auf der .69 gerechnet), medium2d.py (laeuft); Parameter fest in TESTS | Landau u_c/c_s = 0,43 / 0,65; Ernte offen |
| C x S^2 | Kopplung, Knotenzahl | Wel 20, K-3 | CX-1 (formal, geparkt) | ausserhalb v3 |
| Pumpe und Daempfung | Treiber, Daempfung | Bio 45 | r5b.py pumpe | verfehlt |
| Windung m, Ringe (Zustaende) | m; N, k, Drehung | Bio 5, 7, 24, 25, 28, 29, 46, 49, Chem 5, 13, 19, Wel 8, 9, 19, RG-1, MT-2, K-4, QG-3, F-2 | RUNDE-05/r5-2d-a/r5_2d_a.py (berichtigtes Schiessen), r5_2d_b.py, RUNDE-06/regge/regge2d.py | mitdrehender Ring -> Windung-1-Ball (R7 RING); J ~ E^2 vorab ableitbar |
| Dimension (nur mathematisch) | dim | Bruecke 1D -> 3D | resonanz3d.py bruecke | Hypothese: Linien von Nullstellen in (dim, omega^2) |

**Folge fuer Teil B:** Eine Population aus Modellvarianten gibt es heute nur fuer zwei Familien mit echtem
Parameterraum, beta/log (ein Feld) und 2F/MED (zwei Felder). Nur resonanz3d.py nimmt beta schon auf; alle anderen
Bausteine haben ihr Modell fest eingebaut.

## 6. Die zehn tragfaehigsten Befunde der Nacht

Reihenfolge nach Belastbarkeit (zwei Haeuser, drei Stufen, bestandene Kontrollen), nicht nach Neuheit.

1. **3D: Die Breite der l = 0-Atmung hat ein scharfes Minimum nahe omega^2 = 0,7977**, zwei Haeuser blind mit
   verschiedenen Loesern, stabil ueber drei Stufen; kleinster Wert 1,122e-7 (Anthropic, 0,798) und 3,70e-10 (Codex,
   0,7976953, "unaufgeloest"); auslaufende Amplitude mit Phasensprung nahe pi. In 1D gibt es auf 0,55 bis 0,88 kein
   solches Minimum. "Exakt null" und BIC im strengen Sinn sind nicht gezeigt, der Zeitbereich loest es nicht auf.
   Beleg: RUNDE-06/ERGEBNISSE-R6-B.md, Abschnitt 2; coordination/resonance-20260930/3D-OMEGA-SCAN-CODEX.md,
   FESHBACH-ERGEBNIS-CODEX.txt; RUNDE-06/resonanz3d/lauf-lokal/aus-bic-c bis aus-bic-e.
2. **3D-Resonanz der Atmung bei omega^2 = 0,7:** rho = 1,7018102190 - 1,468e-3 i, Codex gleich auf 2,5e-10 im
   Realteil; der 3D-Pol ist die stetige Fortsetzung des 1D-Pols (Bruecke, Ciurla-Kalibrierung auf 2,7e-9).
   Beleg: ERGEBNISSE-R6-B.md, 1.1; resonance-20260930/3D-POLE-CODEX.md.
3. **1D: Die "Absorptionsspitze" ist eine langlebige, ausleckende quasinormale Mode** bei nu - omega = 1,494 (Codex-Pol
   1,49378 - 6,72e-5 i; Anthropic-Feinrechnung auf vier Gittern konvergiert; Abklingrate gegen 2 Gamma auf 0,13 % (Codex)
   bzw. 1,3 % (Anthropic)). Mechanismus
   Literatur, unsere Zahlen neu. Beleg: RUNDE-02.md; RUNDE-02/tests1d/fein-lauf-69/; resonance-20260930/ERGEBNIS.txt.
   A: 0,32 / 0,22 / 0,07, Spannweite Faktor 4,6); Papier von zwei Haeusern, Code auf vier Stellen; einziger Befund mit
   Datenanker (MICROSCOPE). Beleg: RUNDE-01.md; RUNDE-01/QG1-GEGENLESUNG-CODEX.md; RUNDE-01/qg1/lauf-69/.
5. **Tropfenbild:** 2D-Formschwingung nach Rayleigh ohne freie Parameter auf 6 bis 7 %; in 3D gebundene l = 2-Mode im
   Rayleigh-Band (0,0741 bei omega^2 = 0,6; Verhaeltnis 0,93 bis 0,97 bei 0,52 bis 0,55); Young-Laplace auf 1 bis 4 %;
   F-3: Tropfen, nicht Beutel. Einhaeusig, aber vier unabhaengige Proben. Beleg: RUNDE-03/ERGEBNISSE-R3.md (tropfen);
   ERGEBNISSE-R6-B.md, V8 und V9; RUNDE-05/ERGEBNISSE-R5-AB.md (membran).
6. **Teilchenverhalten an Stufen:** kein Zerspritzen in 144 Laeufen bis We = 4,12; unter der Teilchenschwelle ganz
   reflektiert (0,994 bis 0,996), an ihr liegen geblieben, ab 1,02 v_cl ganz durch; in 2D bei 0 bis 60 Grad intakt
   (0,997). Vorbehalt: v_cl folgt aus der Energie, gemessen ist nur das Umschlagsintervall 0,98 bis 1,02.
   Beleg: RUNDE-06/ERGEBNISSE-R6-A.md (Weber); RUNDE-06/weber/.
7. **Dunkler Zustand zweier gleicher Baelle:** Die gemeinsame Resonanz klingt linear mit 1e-14 statt 1 ab (hell 2,005),
   zeitabhaengig mit hoechstens 0,003; schon omega^2 = 0,69 statt 0,70 beim Partner hebt den Schutz auf. Literatur als
   Mechanismus (L4). Beleg: ERGEBNISSE-R6-A.md (R-2, R-2z).
8. **Landau-Schwelle im stabilen Medium:** Unter u_c bremst das chi-Medium nicht; u_c/c_s = 0,43 (C0 = 0,1) und 0,65
   (C0 = 0,3), also unter c_s und dichteabhaengig, L3 22/22 (Vorhersage 0,55 / 0,75 verfehlt, Richtung getroffen).
   Dazu Stokes-Drift ~ a^2 (Exponent 1,99 / 2,03), wenn die Welle von weit kommt. Nicht geerntet.
   Beleg: RUNDE-06/medium1d/lauf-69/landau/ und stokes/; RUNDE-06.md (Vorabblick der Leitung).
9. **3D-Familie des Modells:** Q_min = 111,84 bei omega^2 = 0,927, duenner Ast VK-stabil, E/Q > 1 ab omega^2 ~ 0,85
   (metastabiles Fenster bis Q ~ 141); in mehreren Laeufen vereinbar (tests1d Test 4, r5a fitness, mutanten und
   magisch, R4 artbildung), und Codex' unabhaengiges Profil bei omega = 0,8 stimmt ueberein.
   Beleg: RUNDE-02/tests1d/lauf-69/ausgabe/tests1d_bericht.txt; ERGEBNISSE-R5-AB.md, "Abgleich mit den Ankern".
10. **Kein Molekuel im Ein-Feld-Modell:** E(d) hat nur das Minimum des verschmolzenen Einzelballs; Verschmelzen gibt es
    fast nur bei gleicher Frequenz und kleinem Tempo (Test 3K, L3 32/32). Das schliesst den Q-Materie-Cluster (etwa ein
    Dutzend Ideen) im Ein-Feld-Modell. Beleg: ERGEBNISSE-R3.md (t2 Version 2); RUNDE-02.md (Test 3K).

Knapp dahinter: KF-5 (2D-Kondensat zerfaellt in getrennte Tropfen, nie ein Netz, 6 von 6 Arm-Gitter-Laeufen;
ERGEBNISSE-R6-B.md, 1.3) und F5-1 (ein stabiles Schwebeniveau im gerechneten Raster; ERGEBNISSE-R6-A.md).

## Einfach gesagt

Wir haben alle 131 Ideen der Nacht noch einmal durchgesehen, die meisten davon Vergleiche von Q-Baellen mit Zellen,
Molekuelen und Booten. Fast drei Viertel sind getestet, und die meisten Vergleiche halten nicht oder zeigen nur
Bekanntes: Q-Baelle bilden keine Molekuele und takten sich nicht wie Gluehwuermchen. Was traegt, sind wenige, gut
nachgerechnete Befunde: Ein dreidimensionaler Q-Ball hat eine innere Atmung, die bei einer bestimmten Frequenz fast
gar nicht mehr nach aussen leckt, er schwingt wie ein Wassertropfen, und an einer Stufe verhaelt er sich wie eine
Kugel an einer Rampe. Fuer eine Suche nach besseren Modellen eignen sich nur zwei Stellschrauben, die Form des
Potentials und ein zweites Feld; das wird in Teil B genutzt.
