# X2370-LESUNG: Khemchandani/Martinez Torres/Oset, arXiv:2609.37653 (Runde 12)

- Auftrag: Leitung claude-primary, 01.10.2026. Anlass Finn (01.10.): "lies die arbeit komplett".
- Start: 2026-10-01 18:29:42 CEST (date). Zeitbox 40 min, also Ende gegen 19:10 CEST.
- Lesetiefe: [A] an der Quelle gelesen (mit Abschnitt/Gl./Tab./Abb.), [S] nur Abstract/Suchtreffer, [L?] Gedaechtnis.
  Nur [A] traegt. Eigene Schluesse **[ES]**, Hypothesen [H].
- Grenzen: nichts gerechnet (kein python/awk), kein ssh/git/Peerbus/Unteragent, nur in RUNDE-12/x2370/ geschrieben.

## BERICHT (geschrieben ab 2026-10-01 18:41:37 CEST)

### Kurzfazit (max. 10 Zeilen)

1. FCA-Rechnung phi + (K* Kbar = h1) mit zwei Breit-Wigner-Eingaben (K(1630), K1(1400)) [A, ganz gelesen].
2. Ergebnis M = 2316 +- 10, Gamma = 163 +- 31 MeV. Die Breite passt zu BESIII 2026 (170 +44/-29), die Masse liegt
   43 MeV unter 2359 +13/-14 **[ES]**.
3. Nicht parameterfrei **[ES]**: Die Masse haengt an K1(1400). Deren Masse wurde nach Datenvergleich auf 1460-1480
   gelegt (PDG 2026: 1403 +- 7) [A].
4. Unterdrueckung von K* Kbar/γω/γϕ und TS-Verstaerkung von KKbar pi: nur qualitativ, keine Breite gerechnet [A].
5. BESIII richtig zitiert; dessen Partialbreiten-, eta_c- und Erzeugungsargumente bleiben unbeantwortet [A].
6. Wert der Arbeit: ein qualitatives Gegenmodell gegen die Beweiskraft der drei Hinweise, kein Beleg fuer phi h1.
7. Kein Feshbach-/BIC-Mechanismus: Unterdrueckung kinematisch (off-shell), TS eine Verstaerkung [A + ES].

### Erwartungsverstoesse (das Wichtigste zuerst; Zyklus in F4)

1. **E1 Masse gewaehlt statt vorhergesagt.** Der X-Buckel sitzt ~30 MeV unter dem K1(1400)-Buckel der
   Impulsnaeherung [A, S. 4]. Die K1-Masse ist auf 1460-1480 MeV ausgewaehlt; PDG 2026 gibt 1403 +- 7 [A]. Der
   Anspruch "with no free parameters" (S. 1) und "parameter-free" (Schluss) [A] deckt sich nicht mit dem eigenen
   Verfahren **[ES]**.
2. **E2 Keine Zerfallsbreite gerechnet.** Abb. 1/2 werden nur verbal bewertet. Die TS-Lagen 2400/2433 MeV liegen
   ueber der eigenen Modellmasse 2316 [A], und Gl. (11) setzt die Zerfallsamplitude als glatt an. Der TS-Effekt
   steckt also nicht in Abb. 3 **[ES]**.
3. **E3 BESIII nennt γω/γϕ selbst** (Abstract und Tab. 2, [A]). Die Wiedergabe ist korrekt. Uebergangen werden
   PRL 132, 181901, alle eta'-Kanaele, a0(980) pi0 (> 9 sigma) und das Partialbreitenargument [A, grep].
4. **E4 Kein gekoppelter Kanalsatz im Dreikoerperteil.** Beide Teilamplituden sind Breit-Wigner mit geliehenen
   Kopplungen. Das zugrunde liegende chirale Modell erzeugt K1(1400) nicht und setzt h1 bei ~1245 MeV [A, S. 2-3].
5. **E5 Mehr Konkurrenz als zitiert** [S, arXiv-API]: Zhang u. a. 2609.05908, Buisseret 2608.29775, Zheng u. a.
   2608.28284 u. a.

### Antworten A bis E

**A. Modell und Methode** [A, S. 1-4]
- Quantenzahlen: phi [0-(1--)] x h1(1380) [0-(1+-)] in S-Welle ergibt 0-+, I = 0, C = (-1)(-1) = +.
- h1 als K* Kbar + c.c. (Gl. 1; Lutz/Kolomeitsev 2004, Roca/Oset/Singh 2005).
- Dreikoerper: FCA mit elastischer Unitaritaet, Gl. (2)-(3). G0, GC1, GC2 = phi-Propagator gefaltet mit der
  h1-Wellenfunktion, aus Jia u. a. 2026 [15].
- Teilamplituden: t1 (phi K*, 0+) = BW der K(1630), Kopplung -1518 + i209 MeV aus Geng/Oset 2009. t2 (phi Kbar) =
  BW der K1(1400), Kopplung 3522 +- 21 MeV aus Malabarba u. a. 2021.
- Regulator q_max = 971,5 MeV (900-1000 variiert).
- "Chiral unitaer" ist nur die Herkunft der Kopplungen; gerechnet wird ein einziger Kanal phi-(K* Kbar).
- **Angepasst:** Polynom 3. Ordnung und relative Norm (Fit an K_S K_S pi0 aus [27]). Dazu sechs Resonanzparameter
  nach "satisfactory description of the data" ausgewaehlt; drei Auswahlbereiche liegen teils ausserhalb der
  genannten Ziehbereiche (F2 L8).
- **"Vorhergesagt":** J^PC (trivial aus S-Welle), Existenz des zweiten Buckels, M und Gamma nach Auswahl.

**B. Zahlen**
- Kein Pol angegeben; Masse und Breite aus der reellen Linienform: **M_X = 2316 +- 10 MeV, Gamma_X = 163 +- 31 MeV**
  [A, S. 4, Abb. 3].
- BESIII: kombiniert 2359 +13/-14 MeV, 170 +44/-29 MeV [A, 2605.26495]; 2024: 2395 +- 11 +26/-94 MeV, 188 MeV [S].
  Die Arbeit nennt selbst keine Messzahl ("in line with").
- Unterdrueckt [A, S. 2]:
  - K* Kbar: Der phi Kbar -> Kbar-Vertex zwingt die inneren Linien "very far off-shell".
  - γω: Der ϕη -> γ-Vertex ist "kinematically forbidden", dazu kleine h1-ωη-Kopplung.
  - γϕ: "equally suppressed".
- KKbar pi, zwei Dreiecke [A, S. 2-3]:
  - Abb. 2(a) h1 -> K* Kbar, phi K* -> pi K: TS bei M_X ~ 2433 MeV (phi h1-Schwelle), M_piK ~ 1912 MeV.
  - Abb. 2(b) h1 -> rho pi, phi rho -> K Kbar ueber a0 (Gamma ~ 150 MeV): TS bei M_X ~ 2400 MeV, M_KKbar ~ 1830 MeV.
  - "Hilft" heisst: verstaerkt den nicht ueber K*(892) laufenden KKbar pi-Zerfall. Nicht berechnet.
- Fehler: nur Streuung der Eingaben (Monte Carlo ueber sechs Resonanzparameter, q_max). Modellfehler der FCA, der
  BW-Formen und des inkohaerenten Untergrunds sind nicht abgeschaetzt.

**C. Umgang mit BESIII** [A]
- Richtig wiedergegeben: kein K*0 Kbar0 (BESIII: Partialbreite < 2 MeV, R = 0,003 +- 0,040 +- 0,026) und
  unterdrueckte γω/γϕ (< 0,04 bzw. < 0,11 x 10^-6).
- Leicht zugespitzt: "glueball nature ... claimed" statt BESIIIs "dominant constituent".
- PRL 132, 181901 wird nicht zitiert (J^PC uebernommen).
- Nicht behandelt: Erzeugungsrate, eta_c-Muster, eta'-Kanaele, a0(980) pi0, BESIIIs Argument "a few MeV je Mode,
  Mehrquarkzustaende haetten OZI-erlaubte ~100 MeV-Moden".
- Test der Autoren: KKbar- und piK-Teilmassen in X -> KKbar pi (Spitzen bei ~1830 und ~1912 MeV erwartet).
- Meine schaerferen Tests **[ES]** (F6):
  - U1: a0 pi-Anteil als Funktion von M(KKbar pi). Die TS ergibt eine lokale Ueberhoehung bei 2400-2433 MeV, ein
    Glueball einen festen Anteil.
  - U2: die Mode, die die Gesamtbreite traegt. Molekuel: K* K̄* pi-artig, Dutzende MeV. Glueball: keine dominante
    Mode.

**D. Verbindung zu unserem Mechanismus**
- Im Wortlaut keine [A, grep]: "Feshbach", "quasi", "embedded", "continuum", "interfer", "narrow" 0 Treffer. Es
  gibt nur "a state below the ϕh1 threshold" und "bound the system".
- Die Unterdrueckungen sind kanalweise kinematisch (off-shell, verbotener Vertex) [A], also M1(a)-artig **[ES]**.
  Die TS ist eine kinematische **Verstaerkung**, das Gegenstueck einer stillen Stelle **[ES]**.
- Die Gesamtbreite ist gross: M/Gamma ~ 14 **[ES]**.
- [H] Formal ist X ein Zustand des geschlossenen phi h1-Kanals im Kontinuum offener Kanaele, also Feshbach-artig
  im weiten Sinn. Gl. (2) enthaelt den Interferenzterm (2G0 - GC1 - GC2) t1 t2 zweier Streuzentren. Ob es dort
  Fano-Nullstellen gibt, untersucht die Arbeit nicht.

**E. Folgen fuer QUARK-1**

| QUARK-1-Aussage | Urteil |
|---|---|
| Z5/Kurzfazit 5: "BESIII 2026: X(2370) als dominanter 0-+-Glueball gedeutet" | **gestuetzt**, jetzt [A] ("dominant constituent") |
| Leitungsformel "X(2370) als ueberwiegend Glueball (BESIII 2026)", als Sachaussage gelesen (Wortlaut "ueberwiegend" steht nicht in QUARK-1, grep; dort "dominanter 0-+-Glueball gedeutet") | **zu stark**: umstritten (phi h1, Sigma-Sigmabar, Singulett-Hybrid, Tetraquark; Zhang u. a.: drei Singulett-Konfigurationen erfuellen die Daten [S]) |
| "Gamma = 188 MeV, BESIII PRL 132, 181901 (2024)" | **gestuetzt als Zitat, aber veraltet**: In A5 steht der Wert mit Fehlern (+18/-17 +124/-33); in C und U1 nur als nackte 188 MeV. Neuer Kombinationswert: 2359 +13/-14 MeV, 170 +44/-29 MeV [A] |
| Z5 "(Flavour-Singulett, kein K*K)" | "kein K*K" **gestuetzt** [A, < 2 MeV]; "Flavour-Singulett" als Befund **zu stark**: BESIIIs Schluss, dynamisch auch ohne Singulett erklaerbar (qualitativ) |
| Z5 "Dieselbe Kollaboration deutet ihre eigenen Daten" | **gestuetzt**; inzwischen Widerspruch (Sigma-Sigmabar, phi h1) und Zustimmung (Wang, Buisseret) [S] |
| Bericht C/U1: X(2370) als "Leere-Beutel-Kandidat" (quarkfrei) | **zu stark**: Natur offen |
| U1/G2-Folgerung "kein additives Erhaltungsladungs-Analogon, kein Q-Ball" | **gestuetzt**: Auch jedes Molekuelbild hat B = 0, S = 0 **[ES]** |
| Z4/M1(c) "Quasi-BIC durch Kanalkopplung ist Hadronenliteratur" | **unberuehrt**: X(2370) ist kein weiteres M1(c)-Beispiel |
| M1 "vier Wege zur Schmalheit", bezogen auf die Gesamtbreite | **zu schwach**: X(2370) zeigt, dass Schmalheit kanalweise (Partialbreiten) und gesamt getrennt zu lesen ist; off-shell-Schleifen fehlen als Weg |
| C: "zerfaellt in f0(980) eta' bzw. K_S K_S eta'" | K_S K_S eta' **gestuetzt** [A, 2607.20366]; f0(980) eta' ungeprueft [S] |

### Regime und Moderatoren (F5)

- R1: Glueball und Molekuel stuetzen sich auf verschiedene Observablen. Moderator [H]: Kurzdistanz (Erzeugung,
  eta_c-Muster) gegen Schwellennaehe (Linienform, kanalweise Unterdrueckung). Dazu passt BESIIIs eigenes
  "dominant constituent" plus "threshold effects" [A].
- R2: Messkanal als Moderator der Masse (eta'-Kanal 2395, Kombination 2359, Modell 2316) **[ES]**.
- R3 (Regel 6): Fuer "K* Kbar unterdrueckt" gibt es mindestens drei Wege (Singulett, Off-shell-Schleife,
  Sigma-Sigmabar). Gemeinsame Groesse **[ES]**: die effektive Kopplung an den on-shell-K* Kbar-Kanal.

### Unterscheidungspunkte (F6)

- U1: TS-Signatur ueber M(KKbar pi).
- U2: dominante Mode.
- U3 (modellintern): M_X gegen M_K1(1400); ein Abdruck folgt 1:1.
- U4 phi h1-Schwelle: durch Gamma_h1 = 78 MeV verschmiert, praktisch nicht trennbar.
- K* Kbar/γω/γϕ trennen die Bilder nicht.

### Gegensweep-Befunde (F7)

- **G1 geprueft:** Der FCA-Cluster h1 ist kein gebundener Zustand. Die PDG-Masse 1409 +9/-8 liegt 16-23 MeV ueber den
  K* Kbar-Schwellen (1385,6 und 1393,2 MeV, Kopfrechnung). Die Auswahl 1380-1412 reicht darueber. Die Arbeit sagt
  nicht, wie die Clusterwellenfunktion dann definiert ist.
- **G4, G5, G6 geprueft:**
  - BESIII schreibt "dominant constituent".
  - J^PC aus K_S K_S eta' mit > 9,8 sigma.
  - Innere Widersprueche: K(1630) mit S = 1 "decaying to K K̄", Abbildungsverweise vertauscht, "ωϕ" im Abstract,
    Auswahl- ausserhalb der Ziehbereiche.
- **G2 (FCA-Gueltigkeit fuer phi an ~1400-MeV-Cluster) und G3 (Abb. 3 gegen [27]) ungeprueft.**
- **Gestrichen:** mein Fehlzitat-Verdacht zu [10] (h1 -> γη' ist erlaubt).

### Kalibrierung (F9)

- **(a) Gemessen:**
  - BESIII 2026: 2359 +13/-14 und 170 +44/-29 MeV.
  - Gamma(K* Kbar) < 2 MeV.
  - γω/γϕ-Grenzen.
  - J^PC 0-+; a0(980) pi0.
  - PDG: K1(1400), h1(1415).
- **(b) Verdichtet:**
  - Modellbuckel 2316/163 MeV (nach Auswahl).
  - TS-Lagen.
  - U1-U3.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "X(2370) ist ein Glueball" (BESIII: "dominant constituent").
  - "parameter-free" und "naturally explained" (2609.37653).
- **Warnzeichen:** Meine Sicherheit gegen die Arbeit stieg beim Lesen. Sie stuetzt sich auf deren Wortlaut, nicht
  auf Nachrechnen. Die FCA-Formeln aus [15]/[16] habe ich nicht geprueft.

### Offene Fragen (F8)

O1 Pol und seine M_K1-Abhaengigkeit · O2 FCA oberhalb der Clusterschwelle · O3 gerechnete Partialbreiten, insbes.
K* Kbar gegen 2 MeV · O4 eta'-Kanaele, a0(980) pi0, Erzeugungsrate im phi h1-Bild · O5 Herkunft h1 = 1384 MeV in [10] ·
O6 Ben/Yang/Zou nur [S].

### Einfach gesagt

Ein Messteam in China hat ein Teilchen namens X(2370) gefunden und haelt es ueberwiegend fuer einen "Glueball", also
einen Klumpen aus reiner Kraftfeld-Energie ohne Quarks. Diese Arbeit sagt: Es koennte auch ein lockeres Paar aus zwei
bekannten Teilchen sein. Sie zeigt aber nur in Worten, warum dann bestimmte Zerfaelle selten waeren, und rechnet sie
nicht aus. Ausserdem passt die berechnete Masse erst, nachdem ein Eingabewert passend gewaehlt wurde. Die Frage
"Glueball oder Paar" ist damit offen; entscheiden koennte eine genauere Auswertung, in welche Teilchen X(2370)
hauptsaechlich zerfaellt.

### Quellen (Autor, Jahr, Titel, URL, Lesetiefe)

- Khemchandani, Martinez Torres, Oset 2026, "A glueball puzzle explained in terms of ϕh1(1380) dynamics: Aka X(2370)",
  https://arxiv.org/abs/2609.37653 [A, ganz; PDF sha256 338d9ac2...c220, quellen/]
- BESIII 2026, "Lightest 0-+ Glueball as Dominant Constituent of X(2370)", https://arxiv.org/abs/2607.20366 [A, HTML,
  Abstract, Abschnitte zu K* Kbar, Tab. 2, Diskussion]
- BESIII 2026, "Observation of the X(2370) in J/psi -> γK_S K_S pi0 and J/psi -> γ pi0 pi0 eta", Chin. Phys. C 50 (2026)
  101001, https://arxiv.org/abs/2605.26495 [A, Abstract]
- BESIII 2024, "Determination of spin-parity quantum numbers of X(2370) as 0-+ ...", PRL 132, 181901,
  https://arxiv.org/abs/2312.05324 [S, ueber QUARK-1 und 2607.20366]
- Particle Data Group (Takahashi u. a.) 2026, Review of Particle Physics, IJMPA 41, 2630011, Summary Tables
  https://pdg.lbl.gov/2026/tables/rpp2026-tab-mesons-strange.pdf und
  https://pdg.lbl.gov/2026/tables/rpp2026-tab-mesons-light.pdf [A, K1(1400), K*(892), h1(1415)]
- Nur [S] (arXiv-API-Liste https://export.arxiv.org/api/query?search_query=all:%22X(2370)%22, 18:36; schwaecher als
  WebSearch, deren Kontingent erschoepft war):
  - Ben/Yang/Zou 2026, 2609.01342.
  - Zhang u. a. 2026, 2609.05908.
  - Z.-G. Wang 2026, 2608.03362.
  - Zhu/Zhao 2026, 2608.23428.
  - Buisseret 2026, 2608.29775.
  - Zheng u. a. 2026, 2608.28284.
  - Q.-N. Wang u. a. 2025, 2502.16047.
  - Chevalier/Mathieu 2026, 2609.16790.
  - Lu 2026, 2608.22394 (nur als Ref. [3]).
- Hashes aller Abrufe: quellen/SHA256SUMS.txt.

(Bericht abgeschlossen 2026-10-01 18:44:30 CEST, date. Zeitbox eingehalten: 18:29:42 bis 18:44:30, also 15 von
40 min. Nichts gerechnet ausser Kopfrechnung **[ES]**; kein python/awk, kein ssh/git/Peerbus.)

---

## ARBEITSFELD

### F0. Kontext vor dem Lesen (aus QUARK-1.md und SECTION-THIN-WALL.md, [A] dort gelesen 18:29-18:30)

- QUARK-1 Bericht A5: "X(2370): BESIII PRL 132, 181901 (2024) [S]: M = 2395 +- 11 +26/-94 MeV, Gamma = 188 +18/-17
  +124/-33 MeV, 0-+. Neu: arXiv:2607.20366 [S]."
- QUARK-1 Z5: BESIII 22.07.2026 (arXiv:2607.20366) [S] folgert "dominant constituent" leichtester 0-+-Glueball
  (Flavour-Singulett, kein K*K). "Dieselbe Kollaboration deutet hier ihre eigenen Daten."
- QUARK-1 Bericht C / U1 / G2: X(2370) als zerfallender "Leere-Beutel-Kandidat"; einzeln in J/psi -> gamma X erzeugt,
  zerfaellt in f0(980) eta' bzw. K_S K_S eta' [S].
- QUARK-1 Z4 / M1(c) / U2: Mechanismus-Verwandter unserer stillen Stellen ist der quasi-BIC durch Kanalkopplung
  (Coito/Rupp/van Beveren 2011 [S]); M1: vier Wege zur Schmalheit (a) Schwelle, (b) Symmetrie, (c) Interferenz,
  (d) nichtlinear. Gemeinsame Groesse: Zahl der offenen, an die Mode gekoppelten Kanaele.
- Unser Mechanismus (SECTION-THIN-WALL.md 5.3-5.4 [A]): Wandzustand = gebundener Zustand des geschlossenen Kanals
  ("trapped state of the Feshbach picture"); Kopplung an den offenen Kanal g(omega) ~ |F_w| sin(Psi(omega) - pi theta);
  Abstrahlung verschwindet bei bestimmter Phase. Das ist Interferenz (M1c), nicht Schwelle (M1a).

### F1. Vorab-Erwartungen (eingetragen 2026-10-01 18:30:34 CEST, date; VOR dem Oeffnen des Volltexts)

Grundlage: nur Abstract laut Auftrag plus [L?]-Gedaechtnis an fruehere Arbeiten der Gruppe (Roca/Oset/Singh 2005 zu
Axialvektormesonen aus Vektor-Pseudoskalar-Streuung; Martinez Torres u. a. 2008 zu phi(2170) als phi K Kbar).

- V1 Methode: Bethe-Salpeter in On-shell-Faktorisierung T = [1 - V G]^-1 V ("chiral unitary approach"), Potentiale
  aus dem lokalen Hidden-Gauge-Ansatz (Vektormesonaustausch). h1(1380) aus K* Kbar (+ c.c.) dynamisch erzeugt.
  Fuer phi h1 erwarte ich einen Dreikoerperansatz phi-(K* Kbar), am ehesten Fixed-Center-Approximation (FCA) zu
  Faddeev, oder ein effektives phi-h1-Potential aus phi K*- und phi Kbar-Amplituden. Regularisierung per Cutoff
  q_max (~600-1000 MeV) oder Subtraktionskonstante; das sei der einzige oder fast einzige freie Parameter, fixiert
  an der h1(1380)-Masse, nicht an X(2370).
- V2 Zahlen: Pol knapp unter der phi h1-Schwelle (~1019 + ~1416 ~ 2435 MeV [ES-Kopfrechnung]), also Masse
  ~2350-2420 MeV, Breite ~100-250 MeV (getrieben von der h1-Breite ~90 MeV und offenen Kanaelen). Vergleich mit
  BESIII 2024 (2395, 188) "im Rahmen der Fehler". Unsicherheitsband nur aus Cutoff-Variation.
- V3 Zerfaelle: Sie erklaeren das Fehlen von K*(892) Kbar (BESIII 2026) dynamisch, etwa weil X -> K* Kbar das phi
  "vernichten" muesste. Dreiecksmechanismus: X -> phi h1, h1 -> K* Kbar, K* -> K pi, mit Rueckstreuung im Dreieck;
  vermutlich zeigt die Dreiecksschleife, dass K Kbar pi klein ist oder einen bestimmten Linienverlauf hat.
- V4 Glueball-Umgang: Sie bestreiten den Glueball nicht frontal, sondern bieten eine Alternative ("puzzle
  explained"). Sie zitieren beide BESIII-Arbeiten; ich erwarte, dass sie "dominant constituent" korrekt wiedergeben,
  aber die Glueball-Hinweise auf Flavour-Singulett-Argumente reduzieren. Unterscheidungstest: Zerfall in phi K Kbar
  (bzw. phi K* Kbar) oder Linienform an der phi h1-Schwelle; vielleicht gamma gamma-Kopplung.
- V5 Unser Mechanismus: Keine BIC-Sprache. Gebundener phi h1-Zustand unter der Schwelle, der ueber offene Kanaele
  zerfaellt: formal Feshbach-artig (geschlossener phi h1-Kanal im Kontinuum offener Kanaele), aber die Schmalheit
  kommt aus Schwelle/Bindung (M1a) und schwacher Kopplung, nicht aus Interferenz (M1c).
- V6 Belastbarkeit: modellabhaengig; Fehler ~ einige zehn MeV aus Cutoff; keine Anpassung an BESIII-Linienform;
  keine Gitterrechnung. "Erklaert" meint "vertraeglich mit", nicht "unterscheidet".
- V7 Name: h1(1380) heisst in der PDG inzwischen h1(1415) [L?]; ich erwarte, dass sie den alten Namen fuehren und
  das vermerken.

### F2. Quelle und Lesen (eingetragen ab 2026-10-01 18:34:09 CEST)

- Quelle: `curl https://arxiv.org/pdf/2609.37653` um 18:31 (HTTP 200, 567094 Byte, 5 Seiten, v1 vom 29.09.2026),
  `pdftotext -layout`. sha256 in quellen/SHA256SUMS.txt:
  PDF 338d9ac27781a34277f8582aa516fe72c17e8d0664ba851fd6f5c85d2857c220.
- Gelesen: Volltext ganz (Abstract, Introduction, Formalism, Decay modes, Results, Conclusions, 27 Referenzen) im
  Text [A]; Seiten 2-4 zusaetzlich als Bild (Abb. 1, 2, 3 und Gl. 2-11) [A].
- grep-Proben [A]: "pole" kommt nur bei K1(1270) ("double-pole nature") vor, nie fuer X; "181901"/"2312.05324"
  fehlen; eta' (η′) nur in Referenztiteln [10], [19]; experimentelle X-Masse/-Breite werden nirgends als Zahl genannt.

**Lesenotizen [A], nach Abschnitt:**

- L1 Abstract: phi-h1(1380)-Wechselwirkung, h1 als K* Kbar-Molekuel; Zustand mit gleichen Quantenzahlen, Masse und
  Breite "compatible" mit X(2370). Unterdrueckte Moden "γω, ωϕ and K*Kbar" seien natuerlich erklaert; KKbar pi
  (nicht ueber K*Kbar) "largely enhanced" durch Dreieckssingularitaet plus "K(1630) in the ρϕ → K̄ vertex".
- L2 Einleitung: [1] = BESIII arXiv:2607.20366 analysiert X -> K_S K_S pi0, kein Weg ueber K*0(892) Kbar0, dazu
  "observed suppression of the radiative decays of the state to ω and ϕ" -> Flavour-Singulett -> Glueball. Lager:
  Wang [2] (2608.03362, Glueball), Lu [3] (2608.22394, Singulett-Radialhybrid, ununterscheidbar von gemischtem
  Glueball), Zhu/Zhao [4] (2608.23428, psi(2S)/J/psi-Radiativverhaeltnis misst Glueball-Charmonium-Mischung),
  Ben/Yang/Zou [5] (2609.01342, Argumente von [1] "flawed", X als Sigma-Sigmabar-Molekuel). Eigener Anspruch:
  "with no free parameters, reproduces the mass and width".
- L3 Formalismus: X: 0-+, I = 0 aus phi [0-(1--)] x h1(1380) [0-(1+-)] in S-Welle; C = (-1)(-1) = +. h1 nach Lutz/
  Kolomeitsev 2004 [7] und Roca/Oset/Singh 2005 [8] als K* Kbar + c.c., Gl. (1). Fussnote 1: PDG-Nominalmasse
  1409 +9/-8 MeV [9]; "latest" BESIII 1384 +- 6 +9/-0 MeV [10]; h1-Masse wird zur Fehlerabschaetzung variiert.
  Methode: Fixed-Center-Approximation (FCA) zu Faddeev mit elastischer Unitaritaet (Ikeno/Oset 2025 [12]);
  Gl. (2) T = [t1~ + t2~ + (2G0 - GC1 - GC2) t1~ t2~] / [1 - GC1 t1~ - GC2 t2~ - (G0^2 - GC1 GC2) t1~ t2~];
  Gl. (3) t~i = (M_C/M_i) t_i. G0, GC aus Jia u. a. 2026 [15], Gl. (6), (14). Kein eigener Dreikoerper-Kanalsatz:
  nur phi-(K* Kbar).
- L4 Zerfaelle (qualitativ, ohne Zahl): Abb. 1(a) X -> K* Kbar: Schleife braucht phi Kbar -> Kbar, interne Linien
  "very far off-shell" -> "very small". Abb. 1(b) X -> γω (γϕ): h1 -> ωη (ϕη), dann ϕη -> γ "kinematically
  forbidden", Linien weit off-shell, kleine h1-ωη-Kopplung -> "very small"; γϕ "equally suppressed". Grundlage:
  Tab. V von [8], dort erscheint h1(1380) bei ~1245 MeV.
- L5 KKbar pi: Abb. 2(a) h1 -> K* Kbar, phi K* -> pi K (aus [17]): Dreieckssingularitaet (TS) bei M_X ~ 2433 MeV
  (= phi h1-Schwelle), M_piK ~ 1912 MeV. Abb. 2(b) h1 -> rho pi, phi rho -> K Kbar ueber ein a0 [1-(0++)] mit
  Gamma ~ 150 MeV (Geng/Oset [17]; gesehen von BaBar, BESIII, LHCb [19-21]); bei M_KKbar ~ 1830 MeV TS fuer
  M_X ~ 2400 MeV nach Gl. (18) von Bayar u. a. 2016 [23]. Text nennt die TS hier fuer "Fig. 2(a)" und schliesst
  mit "mechanism of Fig. 2(b)".
- L6 Ergebnisse, Eingaben: t1 (phi K*, J^P = 0+) = Breit-Wigner der K(1630) (PDG-Masse 1629 +- 7, Breite
  16 +19/-18 MeV, J^P in der PDG unbekannt), Kopplung -1518 + i209 MeV aus [17] (dort Pol ~1640 MeV, Gamma ~48).
  t2 (phi Kbar) = Breit-Wigner der K1(1400), Kopplung 3522 +- 21 MeV aus Malabarba u. a. 2021 [24] (Modell [25]);
  das Kanalmodell [8] erzeugt K1(1400) gar nicht. Regulator q_max = 971,5 MeV aus [17], variiert 900-1000 MeV.
- L7 Ergebnisse, Fit: Linienform J/psi -> γ K_S K_S pi0 (Daten BESIII [27], Chin. Phys. C 50 (2026)); Gl. (11)
  dGamma/dM ~ |Im T(M)| (M/m_J/psi)(m_J/psi^2 - M^2) unter der Annahme, die Erzeugungs-/Zerfallsamplitude t sei
  "very mild" in M. Untergrund: Polynom 3. Ordnung, inkohaerent addiert; Polynomkoeffizienten und relative Norm
  "are fitted to the data".
- L8 Ergebnisse, Parameterauswahl: zufaellig gezogen "based on the data collected by the PDG": M_K1(1400) 1400-1500,
  Gamma_K1 100-200, M_h1 1360-1420, M_K(1630) 1620-1640, Gamma_K(1630) 16-40 MeV; g_K1 phi K 2000-4000 MeV.
  "Satisfactory description of the data" fuer M_K1 1460-1480, Gamma_K1 130-220, g 2500-3600, M_h1 1380-1412,
  M_K(1630) 1611-1647, Gamma_K(1630) 36-67 MeV. **Drei der sechs Auswahlbereiche liegen teils ausserhalb der
  genannten Ziehbereiche** (Gamma_K1 bis 220 > 200; M_K(1630) 1611 < 1620 und 1647 > 1640; Gamma_K(1630) 36-67
  gegen 16-40) [A, S. 4 links].
- L9 Ergebnisse, Zustand: Abb. 3 schraffiert (|T|^2 aus Gl. 2) zwei Buckel: ~2050 MeV = K(1630) im phi K*-Teilsystem,
  "already within the impulse approximation". Zweiter Buckel ~30 MeV unter dem Impuls-Naeherungs-Buckel, an dem
  phi K im K1(1400)-Bereich liegt -> "bound the system and generated a genuine state" bei ~2300 MeV.
  **M_X = 2316 +- 10 MeV, Gamma_X = 163 +- 31 MeV**, "in line with the values found for X(2370)". Keine Polsuche,
  keine Riemannblaetter; Masse/Breite aus der reellen Linienform.
- L10 Schluss: "within uncertainties that we evaluate, the obtained results are parameter-free". γω, γϕ, K*Kbar
  "appear naturally suppressed"; KKbar pi "largely enhanced" durch TS und "the K(1630) resonance coupling strongly to
  ϕρ and decaying to K K̄". Vorhersage: M_KKbar ~ 1830 und M_piK ~ 1912 MeV in den (nicht veroeffentlichten)
  Teilmassenverteilungen.
- L11 Innere Widersprueche [A + ES]:
  - Abstract "ωϕ" gegen Text/Schluss "γϕ" (Druckfehler im Abstract, [ES]).
  - Abstract/Schluss: K(1630) im "ρϕ → K̄"-Vertex bzw. "coupling strongly to ϕρ and decaying to K K̄". Im Hauptteil
    traegt dieses Stueck ein **a0** (I = 1, S = 0); K(1630) sitzt in phi K* (S = 1). Eine S = 1-Resonanz kann nicht
    in K Kbar zerfallen **[ES, Strangeness]**. Abstract und Schluss verwechseln also K(1630) und a0(1710/1817).
  - Abbildungsverweise 2(a)/2(b) im TS-Absatz vertauscht (S. 2 rechts unten, S. 3 links oben).
  - Gl. (5) Index "K1(1460)" statt K1(1400); a0 einmal "a0(1790)", in [22] "a0(1710) [a0(1817)]".
  - Ziehbereiche gegen Auswahlbereiche (L8).

### F3. Vorhersagen vor den Folgeabrufen (eingetragen 2026-10-01 18:35:00 CEST, vor jedem Abruf)

- Q1 BESIII arXiv:2607.20366 (Abstract/HTML): nennt J/psi -> γ K_S K_S pi0, kein K*(892) K, Flavour-Singulett,
  "narrow partial decay width", dominanter 0-+-Glueball. γω/γϕ-Unterdrueckung erwarte ich NICHT im Abstract.
- Q2 BESIII [27] Chin. Phys. C 50 (2026), "Observation of the X(2370) in J/psi -> γK_S K_S pi0 and γ pi0 pi0 eta":
  M ~ 2,33-2,40 GeV, Gamma ~ 100-200 MeV; vermutlich Begleitarbeit zu Q1.
- Q3 PDG K1(1400): M = 1403 +- 7 MeV, Gamma = 174 +- 13 MeV [L?]. Dann laege die Auswahl 1460-1480 rund 60-80 MeV
  ueber dem Mittel.
- Q4 BESIII [10] PRD 105, 072002 (2022) "PWA of J/psi -> γη'η'": enthaelt KEIN h1 (C = - passt nicht in γη'η');
  die Zahl 1384 +- 6 +9/-0 stammt dann aus einer anderen BESIII-Arbeit (Fehlzitat).
- Q5 24-Monats-Suche: Ausser den Refs. [2]-[5] keine weitere Molekuel-Deutung von X(2370); keine Antwort auf
  2609.37653 (zwei Tage alt).

### F4. Abrufergebnisse (eingetragen ab 2026-10-01 18:40:14 CEST)

Bestaetigt (je eine Zeile):
- Q2 bestaetigt [A, Abstract arXiv:2605.26495v2 = Ref. [27], Chin. Phys. C 50 (2026) 10, 101001]: X(2370) in
  K_S K_S pi0 (> 14 sigma) und pi0 pi0 eta (> 20 sigma); kombiniert mit K_S K_S eta': M = 2359 +13/-14 MeV,
  Gamma = 170 +44/-29 MeV; dazu X -> a0(980) pi0 (> 9 sigma); "decay pattern similarities to that of η_c".
- Q3 bestaetigt [A, PDG 2026 Summary Table strange, S. 10]: K1(1400) M = 1403 +- 7 MeV, Gamma = 174 +- 13 MeV
  (S = 1,6), K*(892) pi 94 +- 6 %, K phi "seen" (nur ueber die Breite offen).
- V7 bestaetigt [A, PDG 2026 light unflavored]: Eintrag heisst h1(1415), M = 1409 +9/-8 MeV (S = 1,9),
  Gamma = 78 +- 11 MeV. Die Arbeit fuehrt den alten Namen und nennt nur die Massendifferenz (Fussnote 1).
- V5 bestaetigt [A, grep]: "Feshbach", "quasi", "embedded", "continuum", "interfer", "narrow", "cusp": 0 Treffer.
  "bound" nur in "bound the system"; "threshold" nur phi h1-Schwelle (2433 MeV, S. 2) und "state below the ϕh1
  threshold" (S. 3).

Verletzt (voller Zyklus):
- **E1 (V2) Die Masse kommt aus dem K1(1400)-Teilsystem und ist gewaehlt, nicht vorhergesagt.**
  Erwartet: Pol knapp unter der phi h1-Schwelle, Masse ~2350-2420 MeV, ein einziger Regulator als Freiheit.
  Gefunden [A, S. 4]: Kein Pol. Der X-Buckel liegt "about 30 MeV below" dem Buckel der Impulsnaeherung, an dem das
  phi K-Teilsystem im K1(1400)-Bereich liegt. Die K1(1400)-Masse wird "satisfactory" bei 1460-1480 MeV gewaehlt;
  PDG 2026: 1403 +- 7 MeV [A]. **[ES-Kopfrechnung]** Das sind 57-77 MeV ueber dem Mittel, 8 bis 11
  Standardabweichungen. Ergebnis 2316 +- 10 MeV liegt **[ES]** 43 MeV unter BESIII 2359 +13/-14 (rund 2,5 sigma,
  nur die BESIII-Fehler und +-10 quadratisch addiert) und ~110 MeV unter der phi h1-Schwelle (1019 + 1409 = 2428).
  Breite 163 +- 31 gegen 170 +44/-29: vertraeglich.
  **Korrigierte Erwartung:** Im FCA-Bild dieser Arbeit ist X ein durch Rueckstreuung um ~30 MeV verschobener
  Abdruck der K1(1400)-Resonanz im phi Kbar-Teilsystem. Die X-Masse folgt der gewaehlten K1-Masse. Da die
  Auswahl am BESIII-Spektrum erfolgt, sind Masse und Breite **angepasst**, nicht "parameter-free" vorhergesagt.
- **E2 (V3) Keine einzige Zerfallsbreite ist gerechnet.**
  Erwartet: Zahlen oder Verhaeltnisse fuer K* Kbar, γω, γϕ, KKbar pi. Gefunden [A, S. 2-3, Abb. 1-2]: nur
  qualitative Argumente ("very far off-shell", "kinematically forbidden", "very small", "equally suppressed",
  "largely enhanced"). Die TS-Lagen (2400 und 2433 MeV) sind aus Gl. (18) von [23] abgelesen. Sie liegen ueber der
  eigenen Modellmasse 2316, passen also zur gemessenen Masse, nicht zur eigenen **[ES]**. Gl. (11) nimmt die
  Zerfallsamplitude t als "very mild" in M an. Damit steckt der behauptete TS-Effekt **nicht** in der
  Linienform von Abb. 3 **[ES]**.
  **Korrigierte Erwartung:** "Naturally explained" heisst hier: qualitativ plausibel gemacht, nicht berechnet.
  BESIII gibt dagegen Zahlen: Gamma(K* Kbar) < 2 MeV, R = 0,003 +- 0,040 +- 0,026 [A, s. Q1].
- **E3 (Q1/V4) BESIII nennt γω/γϕ selbst, die Autoren lesen die drei Hinweise richtig, uebergehen aber den Rest.**
  Erwartet: γω/γϕ nicht im BESIII-Abstract, also womoeglich unbelegte Zuschreibung. Gefunden [A, BESIII
  2607.20366 HTML]: Abstract nennt "suppression of radiative decays to ω and ϕ". Tab. 2: J/psi -> γX -> γγω < 0,04,
  γγϕ < 0,11 (x 10^-6, 90 % C.L.). K* Kbar: B = (0,1 +- 1,2 +- 1,1) x 10^-6, Partialbreite < 2 MeV. BESIII-Schluss:
  "dominant constituent"; "other interpretations at present are disfavored". Weitere BESIII-Argumente:
  Erzeugungsrate in J/psi -> γX, eta_c-aehnliches Zerfallsmuster, Partialbreiten "of the order of a few MeV" gegen
  ~100 MeV fuer OZI-erlaubte Moden ("multi-quark states or hybrid" seien darum disfavored). Dazu a0(980) pi0
  (> 9 sigma, [27]) und alle eta'-Kanaele.
  In 2609.37653 [A, grep]: keiner dieser weiteren Punkte wird behandelt; PRL 132, 181901 (J^PC-Bestimmung) wird
  nicht zitiert; eta' kommt nur in Referenztiteln vor.
  **Korrigierte Erwartung:** Die Wiedergabe von BESIII ist bei den drei angegriffenen Hinweisen korrekt, bei
  "a glueball nature ... has been claimed" leicht zugespitzt (BESIII: "dominant constituent"). Die Arbeit
  bestreitet nur die Beweiskraft von K* Kbar, γω und γϕ. BESIIIs Hauptargument gegen Mehrquarkzustaende (kleine
  Partialbreiten, keine dominante Mode) beantwortet sie nicht.
- **E4 (V1) Kein gekoppelter Kanalsatz im Dreikoerperteil; beide Zweikoerper-Amplituden sind Breit-Wigner.**
  Erwartet: chiral unitaere Kanalrechnung fuer phi K* und phi Kbar. Gefunden [A, S. 3]: t1 = BW(K(1630)) mit
  Kopplung aus [17]. t2 = BW(K1(1400)) mit Kopplung aus [24]; ausdruecklich, weil das Kanalmodell [8] die K1(1400)
  nicht erzeugt. Die Dreikoerperstreuung ist die FCA mit genau einem Kanal phi-(K* Kbar). Das h1 erscheint im
  zugrunde liegenden Modell [8] bei ~1245 MeV, wird hier aber mit 1360-1420 MeV eingesetzt.
  **Korrigierte Erwartung:** "Chiral unitaer" gilt nur fuer die Herkunft der geliehenen Kopplungen. Die
  Rechnung selbst ist eine FCA-Vielfachstreuung zwischen zwei Breit-Wigner-Teilamplituden.
- **E5 (Q5) Mehr Konkurrenz als zitiert** [S, arXiv-API-Liste, schwaecher als WebSearch, Kontingent erschoepft]:
  Zhang u. a. 2609.05908 ("three flavor-singlet configurations - hybrid meson, tetraquark, trigluon glueball - can
  satisfy existing data"), Buisseret 2608.29775 (pseudoskalarer Glueball, Konstituentenbild), Zheng u. a.
  2608.28284 (keine kompakten ss̄ss̄-Pole unter 2,6 GeV), Q.-N. Wang u. a. 2502.16047 (Tetraquark), Chevalier/Mathieu
  2609.16790 (Glueball-Review). Keine davon ist in 2609.37653 zitiert [A, Referenzliste]. Eine Antwort auf
  2609.37653 gibt es nicht (zwei Tage alt).
- Q4 **gestrichen:** ~~[10] (PRD 105, 072002, PWA J/psi -> γη'η') kann kein h1 enthalten, weil C = - nicht in γη'η'
  passt.~~ Mein Grund war falsch **[ES]**: J/psi -> η' h1 mit h1 -> γη' (C = -) fuehrt ebenfalls auf γη'η'.
  Die Zuordnung der Zahl 1384 +- 6 +9/-0 bleibt ungeprueft; zwei arXiv-API-Abfragen lieferten 0 Treffer.

### F5. Regime und Moderatoren (Regel 1)

- **R1 Glueball gegen Molekuel ist auch eine Frage der Observablen.** BESIII stuetzt sich auf acht Eigenschaften
  [A]. 2609.37653 rechnet Masse und Breite und argumentiert qualitativ zu drei Unterdrueckungen und KKbar pi [A].
  Moderator [H]: **Abstand der Observable zur Kurzdistanz.** Die Erzeugung in J/psi -> γX und das eta_c-artige
  Muster messen die kompakte, gluonreiche Komponente. Die Linienform und kanalspezifische Unterdrueckungen nahe den
  Schwellen messen die Mesonwolke. Beide Bilder koennen je in ihrem Regime recht haben (Mischzustand). BESIII
  selbst schreibt "dominant constituent" und fordert PWA "with considerations on possible threshold effects in
  this mass region" [A, 2607.20366].
- **R2 Messkanal als Moderator der Masse [ES].** 2395 +- 11 +26/-94 (eta'-Kanal, 2024 [S]) gegen 2359 +13/-14
  (Kombination mit K_S K_S pi0 und pi0 pi0 eta, 2026 [A]) gegen Modell 2316 +- 10 (Linienform K_S K_S pi0 mit
  inkohaerentem Polynom). Wer "vertraeglich" sagt, muss den Kanal nennen; die Arbeit nennt keine Zahl.
- **R3 Regel 6 auf "K* Kbar unterdrueckt -> Glueball":** Mindestens drei Wege fuehren zu diesem Y [A/S]:
  Flavour-Singulett (BESIII), Off-shell-Schleife im phi h1-Molekuel (2609.37653), Sigma-Sigmabar-Molekuel (Ben/Yang/
  Zou [S]). Dazu kommen Singulett-Hybrid (Lu [S]) und drei Singulett-Konfigurationen (Zhang u. a. [S]).
  **[ES]** Die gemeinsame Groesse ist die effektive Kopplung des Zustands an den on-shell-K* Kbar-Kanal
  (Ueberlapp bei der on-shell-Relativimpulsskala). Nicht die "Bauteile" Gluon oder Quarkflavour. Das ist die
  M1-Groesse aus QUARK-1 ("Zahl der offenen, an die Mode gekoppelten Kanaele").
- **R4 Schmalheitswege (QUARK-1 M1):** BESIII argumentiert mit M1(b) (OZI, Flavour). 2609.37653 argumentiert
  kanalweise mit M1(a)-artiger Kinematik (off-shell, verbotener Vertex). Keiner von beiden mit M1(c) (Interferenz)
  **[ES]**.

### F6. Unterscheidungspunkte (Regel 2)

- **U1 Glueball gegen phi h1-Molekuel, TS-Signatur.** Wo sie auseinanderlaufen: im Anteil von a0(1710/1817) pi
  (M_KKbar ~ 1830) und piK ~ 1912 MeV **als Funktion von M(KKbar pi)** ueber 2,30-2,45 GeV.
  - TS-Bild [A fuer die Lagen, ES fuer die Form]: lokale Ueberhoehung nahe 2400 bzw. 2433 MeV.
  - Glueball mit eta_c-artigem Muster [ES]: Ein a0 pi-Anteil ist auch dort moeglich (BaBar sah a0 in eta_c-Zerfaellen,
    Ref. [19]), sollte aber als fester Bruchteil der BW-Form folgen.
  - Zugang: Dalitz-/PWA-Analyse von J/psi -> γ K_S K_S pi0 mit 10^10 J/psi; die Daten liegen bei BESIII.
  - Die Arbeit schlaegt nur die Teilmassenverteilungen vor [A, Schluss]. Allein trennen die beiden Bilder bei
    ~1830 MeV schlecht **[ES]**: a0(1817) pi ist auch ohne TS denkbar, piK ~ 1912 liegt nahe K0*(1950) [L?].
- **U2 Dominante Mode.** Wo sie auseinanderlaufen: im Kanal, der die Gesamtbreite (~170 MeV) traegt.
  - Im Modell kommt die Breite [A, Gl. (4)-(5)] nur aus Gamma_K(1630), Gamma_K1(1400) und der komplexen Kopplung.
    **[ES]** Also faellt X in K* + (K1 -> K* pi) bzw. K(1630)-Produkte, mit OZI-erlaubten Partialbreiten von
    Dutzenden MeV in K* K̄* pi-artigen Endzustaenden.
  - Glueball [A, BESIII]: keine dominante Mode, jede Partialbreite "a few MeV".
  - Zugang: J/psi -> γ K* K̄* pi bzw. γ K Kbar pi pi pi im X-Bereich. Vielteilchen, schwer, aber nicht unzugaenglich.
- **U3 Echter Dreikoerperzustand gegen Abdruck der Teilsystemresonanz (modellintern).** Wo sie auseinanderlaufen:
  bei Variation von M_K1(1400) ueber 1400-1500 MeV.
  - Abdruck: M_X folgt 1:1.
  - Echter Zustand: Pol auf dem zweiten Blatt, schwaecher gekoppelt an M_K1.
  - Die Arbeit zeigt weder Polsuche noch diese Abhaengigkeit [A].
- **U4 phi h1-Schwelle (~2428 MeV).** Hier sollte ein Molekuel eine Linienformverzerrung zeigen. Die h1-Breite
  (78 MeV) verschmiert sie. **Praktisch nicht trennbar [ES].**
- **Nicht unterscheidbar:** Die Unterdrueckung von K* Kbar, γω und γϕ erklaeren beide Bilder (das Molekuelbild nur
  qualitativ). Diese drei BESIII-Hinweise trennen also nicht **[ES]**.

### F7. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- **G1 "Der Cluster h1 ist ein gebundener K* Kbar-Zustand", wie die FCA es braucht. Geprueft [A PDG 2026 +
  ES-Kopfrechnung]:**
  - Schwellen: K*(892)+- 891,88 + K+- 493,68 = 1385,6 MeV; K*0 895,56 + K0 497,61 = 1393,2 MeV
    (Kaonmassen [L?]).
  - PDG-h1(1415): 1409 +9/-8 MeV, also 16 bis 23 MeV **ueber** beiden Schwellen.
  - Die "satisfactory"-Auswahl M_h1 = 1380-1412 MeV reicht ueber die Schwelle.
  - Wie die FCA-Clusterwellenfunktion oberhalb der Schwelle definiert ist, sagt die Arbeit nicht [A].
  - Im zugrunde liegenden Modell [8] liegt h1 bei ~1245 MeV, also ~140 MeV gebunden [A, S. 2].
  - **Offen und tragend.**
- **G2 "Die FCA taugt fuer phi (1019 MeV) an einem Cluster von ~1400 MeV."** Die Arbeit verweist auf
  pf1(1285)/ALICE [13,14] und das Review [11]. Die Gueltigkeitsbedingungen (leichtes aeusseres Teilchen, fest
  gebundener Cluster) habe ich nicht an der Quelle geprueft. **Ungeprueft.**
- **G3 "Abb. 3 zeigt die BESIII-Daten unveraendert."** Gegen die Abbildung in [27] nicht verglichen. **Ungeprueft.**
- **G4 "BESIII hat 'Glueball' behauptet."** Geprueft [A]: BESIII schreibt "dominant constituent" bzw. "dominant
  component". Die Zuspitzung "glueball nature ... claimed" ist leicht, aber vorhanden.
- **G5 "J^PC = 0-+ ist gesichert."** Geprueft [A, 2607.20366 HTML]: aus J/psi -> γ K_S K_S eta' mit > 9,8 sigma.
  Die Arbeit uebernimmt das ohne Zitat der Primaerarbeit.
- **G6 "Die Arbeit ist intern konsistent."** Geprueft [A]: nein, siehe L8 und L11.
  - Auswahl- ausserhalb der Ziehbereiche.
  - K(1630) mit Strangeness 1 soll in "K Kbar" zerfallen (Abstract, Schluss).
  - Abb. 2(a)/(b) im Text vertauscht.
  - "ωϕ" im Abstract.

### F8. Offene Fragen

- O1 Gibt es einen Pol? Wo liegt er, und wie haengt er von M_K1(1400) ab (U3)?
- O2 Wie wird die FCA mit M_h1 oberhalb der K* Kbar-Schwelle gerechnet (G1)?
- O3 Welche Partialbreiten ergaeben sich, wenn man die Schleifen von Abb. 1 und 2 rechnet? Insbesondere: Liegt
  Gamma(K* Kbar) unter BESIIIs 2 MeV?
- O4 Wie erklaert das phi h1-Bild die eta'-Kanaele, a0(980) pi0 und die hohe Erzeugungsrate in J/psi -> γX?
- O5 Herkunft der h1-Masse 1384 +- 6 +9/-0 in [10] (ungeprueft, Q4).
- O6 Was sagt Ben/Yang/Zou 2609.01342 genau gegen BESIIIs Argumente? Nur [S]. Fuer QUARK-1 nicht noetig, fuer die
  Glueball-Frage schon.

### F9. Kalibrierung

- **(a) Gemessen:**
  - BESIII 2026 kombiniert: M = 2359 +13/-14 MeV, Gamma = 170 +44/-29 MeV.
  - BESIII 2024: 2395 +- 11 +26/-94 MeV, Gamma = 188 +18/-17 +124/-33 MeV [S].
  - K* Kbar: B = (0,1 +- 1,2 +- 1,1) x 10^-6, Partialbreite < 2 MeV.
  - γγω < 0,04 x 10^-6, γγϕ < 0,11 x 10^-6.
  - J^PC = 0-+; a0(980) pi0 > 9 sigma.
  - PDG 2026: K1(1400) 1403 +- 7 MeV; h1(1415) 1409 +9/-8 MeV, Gamma 78 +- 11 MeV.
- **(b) Nuetzlich verdichtet:**
  - FCA-Linienform mit 2316 +- 10 / 163 +- 31 MeV. Modellausgabe nach Auswahl am Spektrum, keine Vorhersage.
  - TS-Lagen 2400/2433 MeV.
  - BESIIIs sqrt(OZI)-Schaetzung "a few MeV".
  - Meine Unterscheidungspunkte U1-U3.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "X(2370) ist ein Glueball": In BESIIIs Schluss steht "dominant constituent", in Nacherzaehlungen wird daraus
    "ist".
  - Spiegelbildlich bei 2609.37653: "parameter-free" und "naturally explained" ohne gerechnete Breiten.
- **Warnzeichen:** Meine Sicherheit, dass die Arbeit schwach ist, stieg beim Lesen. Gleichzeitig wurde die Frage
  feiner: Was ist gerechnet, was nur behauptet? Die Kritik stuetzt sich auf den Wortlaut der Arbeit, nicht auf
  Nachrechnen. Die FCA-Formeln aus [15]/[16] und die TS-Lagen habe ich **nicht** geprueft. "Schwach belegt" ist
  darum kein "falsch".
