# ARBEITSFELD fls-stille (Runde 21, Literatur-Agent)

- Angelegt 2026-10-02 18:32:12 CEST (date). Start der Zeitbox 18:31:08 CEST, Ende spaetestens 19:31.
- Eine Datei fuer alles (Regel 5). Gestrichenes wird ~~gestrichen~~, nicht geloescht. Offene Rueckfragen stehen unten.
- Marken: [S] gelesen (Volltext/Abschnitt), [L?] nur Abstract oder Zitat, [H] eigene Schlussfolgerung.

## 0. Frage 4 zuerst (lokal gelesen, 18:31)

LITERATURE.tex (89 Zeilen) zitiert: Coleman1985, BattyeSutcliffe2000, Kovtun2018 (Kovtun/Nugaev/Shkerin), Azatov2024,
Ciurla2024 (Ciurla/Dorey/Romanczukiewicz/Shnir), Evslin2026, FriedrichWintgen1985, YuLu2025, Malomed2005,
SofferWeinstein1999.
- Das Wort Friedberg, Lee, Sirlin, FLS, Beutel/bag, zwei Felder kommt nicht vor [S, Z. 1-89].
- Stille Stellen in Q-Baellen: Abschnitt grenzt nur ab (Ciurla2024: kleiner, nicht verschwindender Schwanz, Z. 37-40;
  Malomed2005: Haeufung eingebetteter Solitonen in optischem Modell, Z. 65-72). Keine Q-Ball-BIC-Vorarbeit genannt.
- Folgerung fuer die Suche: Nichts aus dieser Liste erneut suchen. Neu zu suchen ist der ganze FLS-/Zweifeld-Strang
  und die Hadronenbeutel-Seite.

## 1. Suchstrategie (vor dem ersten Abruf, 18:32)

Begriffe (englisch):
- Kern: "Friedberg-Lee-Sirlin", "Friedberg-Lee", "FLS model", "two-component Q-ball", "two-field Q-ball",
  "Q-balls with scalar charges", "Wick-Cutkosky" (Zweifeld-Verwandter), "soliton bag", "nontopological soliton bag".
- Moden: "linear perturbations", "normal modes", "quasinormal", "vibrational modes", "excitations", "breathing",
  "radial oscillations", "stability" (lineare Stabilitaetsanalysen enthalten oft Moden).
- Abstrahlung/still: "radiation", "bound states in the continuum", "embedded eigenvalue", "embedded mode",
  "radiationless", "non-radiating", "trapped mode", "half-wavelength", "resonance".
- Hadronen: "Friedberg-Lee soliton bag model" + "Roper", "breathing mode", "monopole vibration", "sigma radiation",
  "glueball emission", "excited states of the soliton bag".

Quellen:
- export.arxiv.org/api/query (abs:/all:, AND-Kombinationen), Volltext arxiv.org/abs|pdf|html.
- api.openalex.org/works?search= (auch vor 1991, also Friedberg/Lee/Sirlin 1976-1978, Goldflam/Wilets 1982 u. a.).
- api.semanticscholar.org/graph/v1/paper/search (Zitationen, Abstracts).
- Zitierende Arbeiten von Friedberg/Lee/Sirlin 1976 ueber OpenAlex cites:-Filter, falls die Schlagwortsuche duenn bleibt.

Zeitraum: 1976 bis heute (FLS 1976); Pflichtfenster der letzten 24 Monate (Oktober 2024 bis Oktober 2026) eigens
pruefen, bevor eine Fehlanzeige ausgesprochen wird (Regel 7).

Reihenfolge:
1. arXiv-Abfragen FLS (Kern), Zweikomponenten, Q-Ball x BIC/quasinormal/embedded/radiationless.
2. OpenAlex fuer Altbestand (vor arXiv) und Hadronenbeutel.
3. Semantic Scholar als Gegenprobe.
4. Volltexte der Treffer, die Fragen 1 bis 3 beruehren.
5. Gegensweep (Regel 4).

Abbruchkriterium: Zeitbox 19:31; ab 19:15 nur noch Schreiben von ERGEBNIS.md.

## 2. Erwartungen der Leitung (fest, Karte) und eigene Vorhersagen je Abruf

Leitung: F1 80 % (mind. eine Arbeit zu Moden/Abstrahlung FLS/Zweikomponente), F2 75 % (keine BIC in FLS),
F3 85 % (keine Leiter), F4 70 % (keine strahlungsfreien Hadronenbeutel-Schwingungen).

Eigene Vorwegnahme (vor dem ersten Abruf, aus Gedaechtnis, nicht gemessen):
- Moden/Stabilitaet von FLS-Q-Baellen: Friedberg/Lee/Sirlin 1976 (Stabilitaet ueber Q), Lee/Pang 1992 (Review),
  Loiko/Shnir ab 2018 (geeichte, rotierende, gravitierende FLS-Q-Baelle; vermutlich Profile, kaum Moden),
  Nugaev/Shkerin 2019 (Review), Levin/Rubakov 2011 (Q-Baelle mit Skalarladung). Erwartung: Lineare Moden mit
  Abstrahlkanal sind fuer FLS kaum untersucht; wenn, dann Stabilitaet (Vakhitov-Kolokolov-artig), nicht Abstrahlung.
- BIC in Q-Baellen: erwartet keine Arbeit ausserhalb des Leiterpapier-Kontexts.
- Hadronenbeutel: Atmungsmoden/Roper als Beutelschwingung (Goldflam/Wilets-Umfeld), ohne Strahlungsfreiheit.

## 3. Abruflog (Vorhersage vor Abruf, Ergebnis danach)

**BERICHTIGUNG 18:42:41 (date):** Die Uhrzeiten in den Bloecken A bis H (18:33 ... 18:57) waren GESCHAETZT, nicht
gemessen, und sind zu spaet. Gemessen sind nur: Start 18:31:08, Anlage 18:32:12, und 18:42:41 nach Block H.
Alle Abrufe A bis H liegen also zwischen 18:32:12 und 18:42:41. Die Reihenfolge Vorhersage -> Abruf ist davon
unberuehrt (jede Vorhersage wurde vor dem jeweiligen Abruf in diese Datei geschrieben). Ab Block I nur date-Werte.

### Block A (arXiv-API), Vorhersagen notiert 18:33 vor dem Abruf
- A1 abs:"Friedberg-Lee-Sirlin": 15-40 Treffer, ueberwiegend Profile (Loiko/Shnir/Kunz: geeicht, rotierend,
  gravitierend), keine Arbeit zu Moden mit Abstrahlung.
- A2 all:"two-component Q-ball" bzw. "two-field Q-ball": wenige Treffer (Brihaye/Hartmann-Umfeld), keine Moden.
- A3 all:"Q-ball" AND all:"bound states in the continuum": 0-2 Treffer, keiner zu FLS.
- A4 all:"Q-ball" AND all:quasinormal: Ciurla 2024, Boson-Stern-QNM, nichts zu FLS.
- A5 all:"soliton bag" AND all:radiation: 0-3 Treffer, keine strahlungsfreie Beutelschwingung.

Ergebnis Block A (abgerufen 18:33-18:35):
- A1: 19 Treffer [L?]. Bestaetigt im Kern (Profile dominieren), ABER vier Mode-/Streunahe Kandidaten, die die Vorhersage
  "keine Arbeit zu Moden mit Abstrahlung" gefaehrden: 2503.04657 (Zhang/Li 2025, Superradianz an FLS-Solitonen:
  Streumoden, Verstaerkungsfaktoren), 2604.04494 (Murai/Ogawa 2026, Mehrfeld-Oszillonen/I-Baelle im FLS-Modell),
  2605.25243 (Su/Xie 2026, Quantenkorrekturen, Hartree, Stabilitaetsuebergaenge), 2411.08985 (Jaramillo/Zhou 2024,
  Dipole und Ketten, Instabilitaet). Dazu Kim/Nugaev 2309.09661, 2405.09262 ("Kim" der Karte = Eduard Kim),
  Loiko/Perapechka 1805.11929 (klassische Stabilitaet), Levin/Rubakov 1010.0030, Loiko/Shnir 1906.01943.
  -> Volltexte noetig: 2503.04657, 2604.04494, 2605.25243, 2411.08985, 1805.11929 (Stabilitaetsteil).
- A2: 3 Treffer (hep-ph/0309298, 1807.03695, 1612.00737), keine Moden. Bestaetigt.
- A3: 0 Treffer. Bestaetigt.
- A4: 2 Treffer: 2604.07713 (Evslin/Liu 2026, "Linearized Q-Ball Perturbations", Feshbach-artige QNM),
  2604.25223 (Cheng/Guo 2026, Schwarzes Loch mit Q-Ball-Haar). Ciurla 2024 fehlt (Schreibweise "quasi-normal"?).
  Kleine Abweichung, kein Verstoss. Pruefen, ob 2604.07713 = "Evslin2026" des Leiterpapiers.
- A5: 0 Treffer. Bestaetigt.

### Block B (arXiv-API), Vorhersagen notiert 18:36 vor dem Abruf
- B1 all:"Friedberg-Lee" AND (mode|oscillation|excitation|perturbation): einige zusaetzliche Treffer aus dem
  Hadronen-Beutelumfeld (Friedberg-Lee-Solitonbeutel, Nukleon), keine BIC.
- B2 all:"Q-ball" AND all:embedded: 0-3 Treffer, keine eingebetteten Moden in Zweifeld-Q-Baellen.
- B3 all:"Q-ball" AND (radiationless|non-radiating|nonradiating|"trapped mode"): 0-2 Treffer.
- B4 all:"soliton bag" (alle): 5-20 Treffer, Hadronenmodelle 1990er, Atmungsmode/Roper evtl. erwaehnt.
- B5 all:"nontopological soliton" AND (vibration|breathing|"normal modes"): wenige Treffer, Stabilitaet.

Ergebnis Block B (abgerufen 18:36-18:38):
- B1: 17 Treffer, meist Neutrino-"Friedberg-Lee-Symmetrie" (irrelevant). Neu und relevant fuer Frage 5:
  nucl-th/0101019 Kowata/Arima 2001 "Excitation Spectrum in the Friedberg-Lee Model" (erste angeregte Zustaende
  positiver Paritaet aus Skalarmeson-Anregungen) [L?]. Su/Xie 2605.25243: Ladungsaustausch Mittelfeld <-> Fluktuationsmoden.
  Bestaetigt (Hadronenumfeld, keine BIC im Abstract).
- B2: 4 Treffer, keine eingebetteten Moden. Bestaetigt.
- B3: 1 Treffer, Radu/Volkov 0804.1357 (Vortonen, "do not radiate" = vermutlich Frequenz unter Massenschwelle). Bestaetigt;
  im Gegensweep kurz pruefen, ob "non-radiating" dort mehr als omega < m meint.
- B4: 7 Treffer (Le Treust 1207.1017 variationell, angeregte Loesungen; Song Shu 1607.01815 Ein-Schleifen-Fluktuationen
  am FL-Solitonbeutel). Keine Roper/Atmung im arXiv-Bestand (Altbestand vor 1991 fehlt dort). Weitgehend bestaetigt.
- B5: 3 Treffer, irrelevant. Bestaetigt.

### Block C (Volltexte arXiv), Vorhersagen notiert 18:39 vor dem Abruf
- C1 2503.04657 Zhang/Li (Superradianz FLS): Streuung an rotierenden FLS-Solitonen, Verstaerkungsfaktor mit
  Resonanzspitzen (quasigebundene Zustaende), Zahl der Spitzen waechst mit Ballgroesse; keine exakten BIC, keine stillen
  Groessen.
- C2 2604.04494 Murai/Ogawa (Oszillonen FLS): Felder schwingen bei ihren Massen, Lebensdauer numerisch; moeglicherweise
  Abstrahlungsunterdrueckung bei bestimmten Parametern. Falls ja: naher Verwandter der stillen Stellen.
- C3 2605.25243 Su/Xie: Hartree-Dynamik mit Fluktuationsmoden; klassische Moden nur als Basis, keine BIC.
- C4 nucl-th/0101019 Kowata/Arima: Sigma-Anregung (Monopol/Atmung) als erster angeregter Zustand positiver Paritaet
  (Roper-Kandidat), behandelt als diskrete Mode ohne Abstrahlungsanalyse.
- C5 2411.08985 Jaramillo/Zhou: Instabilitaet per Zeitentwicklung; keine Abstrahlungsnullstellen.

Ergebnis Block C, Teil 1 (18:40-18:43):
- C1 2503.04657 (Zhang, Li, Xie, Zhou 2025) [S ueber HTML-Volltext, per Abrufmodell gelesen]: FLS mit
  U = e^2 chi^2 |Phi|^2 + g^2/8 (chi^2 - chi_vac^2)^2 (Gl. 1-2), Massenverhaeltnis gamma = m_chi^2/m_Phi^2 (Gl. 5).
  Linearisierung mit eta_+-, rho_+- (Gl. 32-35), drei ein- und drei auslaufende Kanaele, Relaxationsverfahren.
  Spitzen im Verstaerkungsfaktor: "Larger FLS solitons result in more peaks" (Abb. 8). Deutung ausdruecklich vertagt:
  "will be analyzed in detail in our following paper" (Abschn. IV.1.2). Keine BIC, keine Nullstellen, keine
  Normalmoden. Vorhersage bestaetigt. NEUE SPUR: Folgearbeit der Zhou-Gruppe suchen (D1).
- C2 2604.04494 (Murai, Ogawa, Takahashi 2026, PRD 114, 036019) [L?]: reelle FLS-Variante, Mehrfeld-Oszillonen,
  Abstract ohne Abstrahlung/Lebensdauer. Vorhersage "Abstrahlungsunterdrueckung" nicht gestuetzt, Arbeit randstaendig.
- C4 nucl-th/0101019 (Kowata/Arima 2001, PTP 105, 449) [L?]: erster angeregter Zustand positiver Paritaet aus der
  0s-Anregung des Skalarmesons; keine Abstrahlung/Breite im Abstract. Vorhersage bestaetigt.

### Block D, Vorhersagen notiert 18:43 vor dem Abruf
- D1 Folgearbeit Zhou-Gruppe (au:Zhou/Xie + soliton/Q-ball/superradiance): Es gibt eine Arbeit 2025/26, die die Spitzen
  als quasigebundene Zustaende/Resonanzen grosser FLS-Solitonen deutet (Fabry-Perot-artig); keine exakten BIC.
- D2 2605.25243 Su/Xie Abstract: Hartree, Fluktuationsmoden nur als Basis; keine Abstrahlungsnullstellen.
- D3 2411.08985 Jaramillo/Zhou Abstract: Instabilitaet von Ketten, keine Moden mit Abstrahlung.

Ergebnis Block D (18:44-18:45):
- D1: Autorensuche au:Zhou_Shuang_Yong / au:Xie_Qi_Xin liefert 0 (Syntaxfehlschlag, kein Befund). Weiter ueber
  Semantic-Scholar-Zitationen von 2503.04657 (E1) und arXiv all:superradiance (E2).
- D2 2605.25243 (Su, Xie, Zhou 2026) [L?]: Hartree, Ladungsaustausch mit Fluktuationsmoden, Fenster klassisch stabil ->
  quantenmechanisch instabil; keine Normalmoden/Abstrahlung im Abstract. Bestaetigt.
- D3 2411.08985 (Jaramillo/Zhou 2024) [L?]: Einstein-FLS-Multisolitonen, Stabilitaet per numerischer Relativitaet;
  keine Moden/Abstrahlung im Abstract. Bestaetigt.

### Block E, Vorhersagen notiert 18:45 vor dem Abruf
- E1 Semantic Scholar: Zitationen von arXiv:2503.04657: 3-10 Zitate; darunter evtl. die angekuendigte Folgearbeit
  (Deutung der Spitzen als quasigebundene Zustaende/Resonanzen); keine exakten BIC.
- E2 arXiv all:superradiance AND (Q-ball|soliton), neueste zuerst: Saffin/Xie/Zhou 2023 (PRL) und Folgearbeiten; eine
  davon deutet Spitzen als Resonanzen grosser Solitonen.
- E3 OpenAlex: Friedberg/Lee/Sirlin 1976 finden (ID fuer zitierende Arbeiten), Zitierzahl einige Hundert.

Ergebnis Block E (18:46-18:48):
- E1: 3 zitierende Arbeiten (S2). Darunter 2510.27064 Zhang/Zhou/Zhu 2025 "Q-ball superradiance: Analytical approach",
  Abstract: erklaert "multi-peak structure of the spectrum" [L?]. Vorhersage bestaetigt (Folgearbeit existiert).
- E2: 43 Treffer; einschlaegig: 2212.03269 (Saffin/Xie/Zhou 2022, Q-Ball-Superradianz), 2306.01868 (Boson-Stern-
  Superradianz), 2307.13734 (Cardoso/Vicente/Zhong 2023, Energieentnahme an Q-Baellen), 2402.03193 (rotierende Q-Baelle
  3+1D), 2503.04657, 2510.27064. Bestaetigt.
- E3: FLS 1976 = OpenAlex W1999778725, DOI 10.1103/PhysRevD.13.2739, 499 Zitate. Bestaetigt.

### Block F, Vorhersagen notiert 18:48 vor dem Abruf
- F-a 2510.27064 Volltext: analytisches Stufen-/Duennwandmodell; Spitzen = Resonanzen der Innenwelle mit einer
  Quantisierungs-(Halbwellen-)Bedingung k_in R ~ n pi; keine exakten BIC, keine Nullstellen der Abstrahlung einer
  Normalmode; Modell eher Einfeld (evtl. FLS als Anwendung).
- F-b OpenAlex cites:W1999778725 + search modes/oscillation/excitation/radiation: 10-40 Treffer, Hadronen-
  und Stabilitaetsarbeiten, keine BIC.

Ergebnis F-a (18:49-18:51), 2510.27064 Zhang/Zhou/Zhu 2025 [S ueber HTML, zwei Abrufe, per Abrufmodell gelesen]:
- Modell: Einfeld-Sextik V = |Phi|^2 - |Phi|^4 + g|Phi|^6, g > 1/4 (Abschn. II.1, Gl. 3), also UNSERE Einfeld-Familie;
  FLS nur zitiert. Hintergrund als (n+1)-Stufenfunktion (Gl. 18-19), Duennwand = n = 1.
- Mechanismus der Mehrfachspitzen: Verstaerkungsfaktoren werden im Duennwandfall "simple sinusoidal functions"
  (Abstract) von sigma_+- r_*, sigma_+- = sqrt(-rho_1) +- sqrt(-rho_2) (Abschn. IV.2, Gl. 108);
  -rho_1,2 = omega_Q^2 + omega^2 +- sqrt(W^2 + 4 omega_Q^2 omega^2) - (1+U) = Quadrate der beiden Innen-
  Wellenzahlen der gekoppelten Kanaele; hohe Frequenzen: "peak spacing is simply the inverse of the Q-ball size"
  (Abstract; Gl. 114-115 mit sin(2 r_* omega_Q + phi_-), cos(2 r_* omega + phi_+)).
- Keine Nullstellen, keine strahlungsfreien Konfigurationen, keine BIC, keine Normalmoden des Balls. Keine ausdrueckliche
  Halbwellen-Aussage, keine Deutung als Resonanz/Stehwelle (laut Abrufmodell).
- ERWARTUNGSVERSTOSS (teilweise): Erwartet war eine Resonanz-Quantisierung k_in R ~ n pi. Tatsaechlich: Interferenz-/
  Schwebungsstruktur in den SUMMEN und DIFFERENZEN der zwei Innenwellenzahlen, periodisch im Wandradius r_*, ohne
  Resonanzdeutung. Korrigierte Erwartung: Die Periodizitaet besonderer Merkmale im Ballradius ist in der Q-Ball-
  Streuliteratur (Einfeld-Sextik, analytisch; FLS numerisch "mehr Spitzen bei groesseren Solitonen") bereits angelegt.
  Was dort fehlt, ist eine NULLSTELLE der Abstrahlung einer Normalmode. [H] Damit ist der Leiterabstand als solcher
  vermutlich generische Innenwellen-Interferenz; neu bleibt nach Recherchestand die exakte Stille.
- Konsequenz fuer F3: nicht verletzt im Wortlaut (keine Arbeit nennt besondere Groessen in festem Radiusabstand), aber
  die Halbwellen-/Interferenzstruktur ist Literatur. Im Ergebnis so zuschneiden.
- Fuer Frage 4: Die Superradianz-Reihe (2212.03269, 2402.03193, 2503.04657, 2510.27064) fehlt in LITERATURE.tex.

Ergebnis F-b (18:51-18:52): OpenAlex cites:W1999778725 + Modenbegriffe: 198 Treffer (Seite 1 = 100 gelesen, Titel).
Bestaetigt im Kern, aber mehr Mode-Arbeiten als erwartet. Kandidaten zur Pruefung (Titel [L?]):
- "Relativistic (3+1)-dimensional nontopological solitons under perturbations" (1997, PRD 55, 7749)
- "Q-ball perturbations with more details: Linear analysis vs lattice" (2025, PRD 111, 096010)
- "Stability analysis for Q-balls with spectral method" (2026, JHEP 02(2026)078)
- "Non-topological solitons and quasi-solitons" (2025, Rep. Prog. Phys., Review)
- "Excited Q-balls" (2022, EPJC); "Oscillons and bubbles in Q-ball dynamics" (2025, JHEP 12(2025)154)
- "Perturbations of Q-balls: from spectral structure to radiation pressure" (2024, JHEP 07(2024)196) = vermutlich Ciurla2024
- Hadronen: "Spectrum of P-wave baryonic excitations in a model with field confinement" (1976, PRD 14, 2362);
  "Stability of a scalar soliton" (1982, PRD 26, 520); Lee/Pang "Nontopological solitons" (1992, Phys. Rep.).
OpenAlex Hadronen-Suche (Beutel + Atmung/Roper): 5 Treffer, darunter DeTar/Donoghue "Bag Models of Hadrons" (1983,
Annu. Rev.) [L?]. Keine Beutel-Atmung mit Abstrahlung im Titel.

### Block G, Vorhersagen notiert 18:53 vor dem Abruf
- G1 OpenAlex Seite 2 (cites FLS + Modenbegriffe): ueberwiegend Kosmologie/Boson-Sterne, 0-3 weitere Kandidaten.
- G2 PRD 55, 7749 (1997): Zeitentwicklung gestoerter nichttopologischer Solitonen (vermutlich FLS-artig, Zweifeld),
  Stabilitaet/Zerfall, keine stillen Groessen.
- G3 PRD 111, 096010 (2025): Einfeld-Q-Baelle, lineare Moden vs Gitter, keine FLS-BIC.
- G4 JHEP 02(2026)078: Spektralverfahren fuer Q-Ball-Stabilitaet; evtl. FLS als Beispiel; keine BIC.
- G5 Review 2025 Rep. Prog. Phys.: FLS-Abschnitt, Superradianz erwaehnt, keine BIC.

Ergebnis Block G (18:54-18:56):
- G1 Seite 2 (98 Titel): weitere Kandidaten [L?]: "Classical behaviour of Q-balls in the Wick-Cutkosky model" (2019,
  EPJC), "Q-balls in the Wick-Cutkosky model" (2017), "Study of Stability of a Charged Topological Soliton in the System
  of Two Interacting Scalar Fields" (2007, 0710.2975), "Revisiting the fermion-field nontopological solitons" (2024,
  JHEP 09(2024)077; Frage 5), T. D. Lee "Nontopological Solitons and Applications to Hadrons" (1979, Phys. Scr.),
  "Q-balls and charged Q-balls in a two-scalar field theory with generalized Henon-Heiles potential" (2024).
  Bestaetigt (0-3 neue Kandidaten erwartet; es sind etwa 3 einschlaegige).
- G2 Elphick 1997 (PRD 55, 7749) [L?]: allgemeine Methode (dynamische Symmetriegruppen, singulaere Stoerungstheorie,
  kollektive Koordinaten), nicht FLS-spezifisch, keine Abstrahlungsnullstellen. Im Kern bestaetigt.
- G3 Azatov/Ho/Khalil 2025 (PRD 111, 096010) [L?]: Abstract nennt ausdruecklich FLS-Q-Baelle und die Grenze der linearen
  Analyse gegen Gitter. ERWARTUNGSVERSTOSS: erwartet Einfeld ohne FLS. -> Volltext lesen (H1).
- G4 Chen/Andersson/Li 2026 (JHEP 02(2026)078) [L?]: Einfeld, Spektralverfahren, angeregte Q-Baelle verletzen das
  Stabilitaetskriterium, Oszillationsmoden werden imaginaer; kein FLS, keine BIC. Bestaetigt.
- G5 Zhou 2025 Review (Rep. Prog. Phys., arXiv 2411.16604) [L?]: Abstract allgemein. Volltextsuche nach
  continuum/embedded/Friedberg spaeter, falls Zeit.

### Block H, Vorhersagen notiert 18:57 vor dem Abruf
- H1 Azatov/Ho/Khalil 2025 Volltext: Streuung von Wellen an FLS-Q-Baellen (Reflexion, Strahlungsdruck), lineare
  Analyse gegen Gitter; Modenspektrum ggf. gestreift; keine stillen Groessen, keine Leiter.
- H2 "Revisiting the fermion-field nontopological solitons" (2024): fermionisches FL-Soliton, Profile/Stabilitaet,
  keine Beutelschwingungen mit Abstrahlung.

Ergebnis Block H (vor 18:42:41):
- arXiv-API und Semantic Scholar melden HTTP 429 (Ratenbegrenzung), S2-DOI-Abfrage HTTP 404. Ausweg OpenAlex:
  Azatov/Ho/Khalil = arXiv:2412.13885 (OpenAlex W4405626810, Zeitschrift W4410207500).
- H1 2412.13885 [S ueber HTML-Volltext, per Abrufmodell]: Abschnitt 3 "Two-field Q-balls" = FLS:
  V = g_chiPhi chi^2|Phi|^2 + g_chi (chi^2 - v^2)^2 + m_Phi^2|Phi|^2 + g_Phi|Phi|^4 (Gl. 48-49), Werte g_chiPhi = 4,
  g_chi = 1, g_Phi = 0.04, v = 1, m_Phi = 0. Drei Kanaele eta_+, eta_-, eta_chi (Mischterm Gl. 55), Streumatrix
  (Gl. 55-60), Verstaerkungsfaktoren Z_Q, Z_E, Modenumwandlung (Abb. 15-19), Wirkungsquerschnitte (Anh. B.1);
  Abschn. 3.1.1 "Propagating and bounded modes": sechs Regime nach offenen/geschlossenen Kanaelen. Spitzen in Z_E, Z_Q
  (Abb. 9-10). Keine BIC, keine eingebetteten/strahlungsfreien Moden, keine Periodizitaet im Radius. Bestaetigt.
- H2 Ke-Pan Xie 2024 (JHEP 09(2024)077) [L?]: fermionische Solitonprofile (relativistische Mittelfeldtheorie), keine
  Schwingungen/Abstrahlung im Abstract. Bestaetigt.

**FUND ZU FRAGE 4 (lokal, 18:42:47 date):** bibliography.tex des Leiterpapiers: Azatov2024 = arXiv:2412.13885v1, also
GENAU die Arbeit mit dem FLS-Abschnitt 3. LITERATURE.tex Z. 24-31 nennt sie nur fuer die Einfeld-Sextik.
Evslin2026 = 2604.07713 (Evslin, Liu, Romanczukiewicz, Shnir, Wereszczynski, Ziobro). Ciurla2024 = JHEP 07(2024)196.
Kein Eintrag zu Friedberg/Sirlin/Superradianz/Zhou/bag (grep, 15 bibitems). [S]
-> ERWARTUNGSVERSTOSS (Regel 4, Schluessel vor der Nase): Das Papier zitiert bereits eine lineare FLS-Analyse, ohne es
   zu sagen.

### Block I, Vorhersagen notiert 18:43:29 (date) vor dem Abruf
- I1 2412.13885 Abschn. 3 gezielt: keine lokalisierten Loesungen (Normalmoden) des linearisierten FLS-Problems bei
  offenem Kanal; "bounded modes" meint geschlossene Kanaele, nicht gebundene Zustaende des Balls.
- I2 Zhou-Review 2411.16604 (HTML): FLS-Abschnitt und Superradianz-Abschnitt; keine BIC/eingebetteten Moden.
- I3 OpenAlex Hadronen (Friedberg-Lee/soliton bag + Roper/breathing/excited/vibration): Treffer aus 1980-2005
  (Goldflam/Wilets-Umfeld, Kowata/Arima), Atmungsmode als Roper-Kandidat, keine strahlungsfreien Beutelschwingungen.
- I4 OpenAlex Kurzabstracts (Levin/Rubakov 2011, Loiko/Perapechka 2018, Wick-Cutkosky 2019, Kim/Nugaev 2023):
  Profile und Stabilitaet (Ladungs-/Energiekriterien), keine Modenrechnung mit Abstrahlung.

Ergebnis Block I (18:43:29-18:44:17 date):
- I1 2412.13885 gezielt [S per Abrufmodell]: "bounded" = evaneszenter Kanal (k^2 < 0), nicht Eigenmode des Balls
  (Abschn. 3.1.1, Abb. 11; eta_chi geschlossen fuer omega^2 < 8 g_chi v^2). Keine inneren Moden, keine Resonanzdeutung.
  Kein systematisches Variieren des Radius (nur verschiedene omega_Q, Abb. 7, 15-19). Z_E und Z_Q fallen nahe der
  Schwelle zweier offener geladener Kanaele auf null (Abschn. 3.1 nach Abb. 9) = Schwelleneffekt, keine BIC.
  Prioritaetsanspruch der Autoren: "for the first time we have analyzed the perturbations of the FLS Q-ball" (Summary).
  Bestaetigt.
- I2 Zhou-Review 2411.16604 [L?, Abrufmodell sah nur Teile]: FLS-Abschnitt II.6.1 (Profile/Stabilitaet), Schwingungsmoden
  nur im Duennwandabschnitt II.1.5, keine BIC/Halbwelle. Bestaetigt, Teilbefund.
- I3 Hadronen: OpenAlex "soliton bag"+Anregung 219 Treffer (50 Titel), Friedberg-Lee+Anregung 71 (50 Titel).
  Kandidaten: "Excited states in the soliton bag model" (1984, PRD 29, 525); "Surface collective motion in the soliton
  bag model" (1987, PLB); "Excited states of the nucleon within the Friedberg-Lee model" (1993, DOI 10.1007/BF02771449);
  "Bifurcation in the Friedberg-Lee model" (1991, J. Phys. A 24); Birse "Soliton models for nuclear physics" (1990,
  PPNP); Goldflam/Wilets "Soliton bag model" (1982, PRD 25, 1951); Kowata/Arima 2001. Titel bestaetigen die Vorhersage
  (Anregungen ja, Abstrahlung kein Titelthema); Abstracts pruefen (Block J).

### Block J, Vorhersagen notiert 18:44:17 (date) vor dem Abruf
- J1 PRD 29, 525 (1984) "Excited states in the soliton bag model": Quarkanregungen und evtl. Sigma-Atmung im Beutel,
  diskrete Zustaende, keine Abstrahlungsnullstellen.
- J2 PLB 1987 "Surface collective motion": Oberflaechenschwingungen (Vibrationen des Beutels), Frequenzen/Rotation,
  ohne Strahlungsbreite oder mit Breite > 0.
- J3 BF02771449 (1993) "Excited states of the nucleon within the Friedberg-Lee model": Roper als Monopol-/Atmungsmode,
  ohne strahlungsfreie Bedingung.
- J4 Levin/Rubakov 1010.0030, Loiko/Perapechka 1805.11929, Wick-Cutkosky 2019 (EPJC), Kim/Nugaev 2309.09661:
  Profile/Stabilitaet ohne Abstrahlungsrechnung.

Ergebnis Block J (18:44:17-18:45:29 date):
- J1 Saly/Sundaresan 1984 (PRD 29, 525) [L?]: numerische Loesungen des Friedberg-Lee-Solitonbeutels, Erweiterung von
  Goldflam/Wilets auf radial angeregte Zustaende gerader und ungerader Paritaet; diese "restrict severely" den
  Parameterbereich. Statische angeregte Loesungen, keine Abstrahlung. Bestaetigt.
- J2 Iwasaki/Kondo 1987 (PLB 199, 437) [nur Titel/Schlagworte, kein Abstract in OpenAlex]: Oberflaechen-Kollektiv-
  bewegung im Solitonbeutel, semiklassische Quantisierung, P11 (Roper) und P33. Nicht pruefbar, ob Abstrahlung behandelt.
- J3 Haider 1993 (Nuovo Cim. A 106, 335) [nur Titel/Schlagworte]: radial angeregte Nukleonzustaende im FL-Modell.
  Nicht pruefbar.
- J4 Levin/Rubakov 2011 (MPLA 26, 409) [L?]: FLS-Q-Baelle mit verschwindendem Potential eines Feldes, Skalarladung;
  keine Moden. Loiko/Perapechka/Shnir 2018 (PRD 98, 045018) [L?]: haarige FLS-Q-Baelle "classically stable for all
  range of values of angular frequency", Methode im Abstract nicht genannt; rotierende FLS-Q-Baelle. Bestaetigt.
  (Wick-Cutkosky 2019, Kim/Nugaev 2023 nicht mehr abgerufen; Titel/Abstract aus Block A ohne Modenbezug.)

## 3b. Gegensweep (Regel 4), angesetzt 18:45:29 (date)

Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
1. Dass "still" in der Literatur "bound state in the continuum"/"embedded" heisst. Andere Namen: Fano-Null,
   reflexionsfrei/transparent, Ramsauer-Townsend, "zero-width resonance", "radiationless", Anapol (Optik),
   "dark state". Besonders: Nullstellen der Abstrahlung von OSZILLONEN (Fourier-Nullstellen einer flachen Quelle,
   j_1(kR)/(kR)) liefern ebenfalls Leitern besonderer Radien im Abstand ~ pi/k. -> PRUEFEN (K1, K2).
2. Dass M2 dasselbe wie das FLS-Modell der Literatur ist. M2 hat zusaetzlich psi-Masse und -Selbstwechselwirkung
   (-S^2 + S^3/2); Azatov 2024 und Zhang 2025 rechnen reines FLS (m_Phi = 0 bzw. ohne Sextik). Nicht geprueft, ob genau
   diese Hybridform anderswo vorkommt.
3. Dass die 24-Monats-Front (Okt 2024 bis Okt 2026) durch arXiv-Abfragen mit "Q-ball" abgedeckt ist. Arbeiten, die
   "nontopological soliton", "boson star" oder "two-field soliton" sagen, fallen durch. -> PRUEFEN (K3).
4. Dass der Hadronen-Altbestand (1976-1995) ueber OpenAlex auffindbar ist: viele Abstracts fehlen (J2, J3); Lee/Pang 1992
   und Wilets' Buch (1989) sind nicht im Volltext lesbar.
5. Dass "Leiter" nur in Radius-Richtung gesucht werden muss: In Streuarbeiten erscheint dieselbe Struktur in der Frequenz
   ("peak spacing ... inverse of the Q-ball size", 2510.27064).

### Block K (Gegensweep-Pruefungen), Vorhersagen notiert 18:45:29 (date) vor dem Abruf
- K1 Oszillonen: Abstrahlrate mit Nullstellen/Einbruechen bei bestimmten Frequenzen/Radien (Fourier-Nullstellen) ist
  bekannt (Zhang/Amin/Copeland/Saffin/Lozanov 2020 o. ae.), aber fuer reelle Einzel-Oszillonen, nicht fuer Normalmoden von
  Q-Baellen. Falls gefunden: wichtigster Vergleich fuer die Leiter.
- K2 Q-Ball + Ramsauer/reflexionsfrei/transparent/Fano: 0-2 Treffer, keine stillen Moden.
- K3 OpenAlex, ab 2024-10-01, "bound states in the continuum" + soliton/Q-ball/boson star: Treffer aus Optik/Photonik
  (Solitonen in BIC-Gittern), kein Q-Ball/FLS.

Ergebnis Block K (18:45:29-18:46:29 date):
- K1 OpenAlex Oszillonen-Abstrahlung: 607 Treffer (40 Titel). Kandidaten: "Classical decay rates of oscillons" (2020,
  JCAP 07(2020)055), "Flat-top oscillons in an expanding universe" (2010, PRD 81, 085045), "Decay rates of Gaussian-type
  I-balls" (2014, JCAP). Inhalt noch offen -> K1b (Volltext).
- K2 Q-Ball + reflexionsfrei/transparent/Ramsauer/Fano/strahlungsfrei: 4094 Treffer, Spitze von MRT-"q-ball imaging"
  ueberlagert, nichts Einschlaegiges unter 40 Titeln. Zusammen mit B3 (arXiv, 1 irrelevanter Treffer) bestaetigt.
- K3 (24-Monats-Fenster, Regel 7): 3626 Treffer, alle 50 gezeigten aus Photonik/Metamaterial; kein Feldtheorie-Soliton.
  Bestaetigt; Einschraenkung: OpenAlex-Rangfolge, daher gezielte arXiv-Gegenprobe K4.

### Block K', Vorhersagen notiert 18:46:29 (date) vor dem Abruf
- K1b arXiv 2004.01202 (Zhang/Amin/Copeland/Saffin/Lozanov): Zerfallsrate reeller Oszillonen; Einbrueche/Nullstellen
  der Rate bei bestimmten Frequenzen, erklaert ueber Nullstellen der Fourier-Transformierten der Quelle. Keine Q-Baelle,
  keine Normalmoden.
- K4 arXiv-API all:"bound states in the continuum" AND (soliton|kink|oscillon|"boson star"|nontopological): 5-30
  Treffer, fast alle Optik/BEC; evtl. 1-2 Kink-Arbeiten; nichts zu Q-Baellen/FLS.

Ergebnis Block K' (18:46:29-18:47:27 date):
- K1b 2004.01202 (Zhang, Amin, Copeland, Saffin, Lozanov 2020, JCAP 07(2020)055) [L?]: reelle Oszillonen koennen
  "(one or more) exceptionally stable field configurations" durchlaufen, in denen die Zerfallsrate "highly suppressed" ist;
  Ursache laut Abstract die raumzeitabhaengige effektive Masse in der Strahlungsgleichung (zusaetzlich zur Quelle).
  TEILWEISER ERWARTUNGSVERSTOSS: erwartet Fourier-Nullstellen der Quelle; tatsaechlich betont: effektiver Massenterm.
  Sachlich naechster Verwandter einer "stillen Stelle" in skalaren Feldtheorie-Solitonen (nichtlinear, Einfeld, reell,
  Strahlung der 3. Harmonischen), aber keine Normalmode eines Q-Balls. -> Volltext K1c.
- K4 arXiv: 20 Treffer, Optik/BEC/Polaritonen; einzige Feldtheorie 2207.01161 (Toda-Modell, Majorana-Nullmode);
  Kirr/Weinstein nlin/0012021 (parametrisch angeregte Hamilton-PDEs, eingebettete Eigenwerte, mathematisch).
  Kein Q-Ball/FLS/Beutel. Bestaetigt.

### Block L, Vorhersagen notiert 18:47:27 (date) vor dem Abruf
- K1c 2004.01202 Volltext: Rate als Funktion der Oszillonfrequenz mit einer oder zwei scharfen Nullstellen (Vorzeichen-
  wechsel der Strahlungsamplitude), keine regelmaessige Leiter, kein Halbwellenbezug.
- L1 Wick-Cutkosky (Nugaev/Smolyakov 2017 EPJC 77, 2019 EPJC 79): klassische Stabilitaet ueber Q(omega), keine
  Abstrahlungsrechnung.

Ergebnis Block L (18:47:27-18:48:41 date):
- K1c 2004.01202v2 [S, PDF selbst gelesen, S. 1-4, 12-19, 23-24]: Gl. (7.4) Gamma_(3) proportional zu
  [S~(kappa_3)]^2, S~ = raeumliche Fourier-Transformierte der Quelle S_j inkl. effektiver Masse (Gl. 4.5);
  "if S~(kappa_3) vanishes for some omega, then Gamma_(3) also vanishes" (S. 13); tanh^2-Potential: S~_3(kappa_3) = 0 bei
  omega_* ~ 0.82 m (Abb. 4, S. 15), Rest durch 5 omega-Strahlung (Gamma_5 ungleich 0). Abschn. 7.5, phi^6-Potential
  V = m^2 phi^2/2 - lambda phi^4/4 + g phi^6/6 (Gl. 7.9): "multiple dips indicating the existing of multiple, long-lived
  oscillon configurations" (S. 18), dort Verweis auf [50] Mukaida/Takimoto/Yamada 2017 (1612.07750) und [51] Ibe/Kawasaki/
  Nakano/Sonomoto 2019 (1901.06130). Abschn. 8: Lebensdauer-"spikes" ueber dem Anfangsradius ([59, 60], "resonant"
  Konfigurationen, ~10 % laenger).
  -> Vorhersage K1c BESTAETIGT (Nullstelle einer Fourier-Transformierten, wenige Stellen, kein Halbwellenbezug genannt).
  -> ~~K1b-Verstoss "statt Fourier-Nullstelle effektive Masse"~~ GESTRICHEN 18:48: Die effektive Masse steckt in S_j,
     der Mechanismus bleibt die Fourier-Nullstelle. Abstract hatte nur die Verbesserung betont.
  -> ABER Erwartungsverstoss gegen die Grundannahme der Karte (Regel 4, Punkt 1): Eine FOLGE besonderer Groessen mit
     unterdrueckter Abstrahlung ("multiple dips") ist fuer reelle phi^6-Oszillonen Literatur (2017-2020). Kein FLS, keine
     lineare Normalmode, nur fuehrende Harmonische unterdrueckt (naechste strahlt). [H] Fuer F3 relevant als Vergleich,
     nicht als Widerlegung.
- L1 Panin/Smolyakov 2019 (EPJC 79, "Classical behaviour of Q-balls in the Wick-Cutkosky model") [L?]: klassische
  Stabilitaet analytisch und numerisch, nichtlineare Entwicklung instabiler Q-Baelle, aeussere Felder; keine Abstrahlungs-
  nullstellen im Abstract. Bestaetigt.

### Block M, Vorhersagen notiert 18:48:41 (date) vor dem Abruf
- M1 1612.07750 Mukaida/Takimoto/Yamada Abstract: I-Ball-Zerfallsrate ueber die ungefaehr erhaltene adiabatische
  Invariante, nicht monotones Verhalten/Stufen; Nullstellen bei bestimmten Groessen nur implizit.
- M2 Lee/Pang 1992 (Phys. Rep. 221, 251) Abstract: Uebersicht FLS/Solitonsterne/Hadronen; keine Moden mit Abstrahlung.
- M3 hep-ph/0110065 Honda/Choptuik 2002 Abstract: Resonanzen der Oszillon-Lebensdauer ueber dem Anfangsradius (phi^4,
  3D), viele Resonanzen, Vermutung unendlich langer Lebensdauer.

Ergebnis Block M (18:48:41-18:49:25 date):
- M1 Mukaida/Takimoto/Yamada 2017 (JHEP 03(2017)122) [L?]: Langlebigkeit ueber effektive Theorie mit naeherungsweiser
  U(1), Zerfall exponentiell unterdrueckt, "attractor behaviors" verlaengern die Lebensdauer. Keine Dips im Abstract.
  Im Kern bestaetigt.
- M2 Lee/Pang 1992 (Phys. Rep. 221, 251-350): kein Abstract in OpenAlex, nicht pruefbar. Grenze.
- M3 Honda/Choptuik 2002 (PRD 65, 084037) [L?]: "resonant (and critical) behavior" mit Zeitskalengesetz im r_0-Raum
  (phi^4, 3D, reell); Zahl der Resonanzen im Abstract nicht genannt. Bestaetigt.

### Block N, Vorhersagen notiert 18:49:25 (date) vor dem Abruf
- N1 arXiv all:Friedberg AND all:Sirlin (Schreibvarianten, Gegensweep Punkt 3): 20-40 Treffer, gegenueber A1 nur
  wenige neue; keine Moden-/Abstrahlungsarbeit ausser den bekannten (2412.13885, 2503.04657).
- N2 OpenAlex "breathing mode" + "soliton bag"/Friedberg-Lee: 0-5 Treffer, Roper als Atmungsmode in chiralen
  Modellen, nicht im FL-Beutel mit Strahlungsfreiheit.
- N3 2405.09262 Kim/Nugaev 2024: Quantenkorrekturen flachen grosse FLS-Solitonen ab; Fluktuationsspektrum nur fuer
  Ein-Schleifen-Energie; keine Abstrahlung.

Ergebnis Block N (18:49:25-18:50:23 date):
- N1 arXiv all:Friedberg AND all:Sirlin: 21 Treffer; gegenueber A1 neu: 2303.09566 Heeck/Sokhashvili 2023 "Revisiting
  the Friedberg-Lee-Sirlin soliton model", 2012.01052 Loiko/Perapechka 2020 "Q-chains in the U(1) gauged FLS model".
  Mode-/Streuarbeiten nur die bekannten (2503.04657; 2412.13885 nennt FLS offenbar nicht im Abstract, daher hier nicht
  gelistet). Bestaetigt. -> Heeck/Sokhashvili-Abstract pruefen (O1).
- N2 OpenAlex Atmungsmode: 23536 Treffer, von Festkoerper/Kernphysik ueberlagert; einschlaegig nur Birse 1990 (PPNP,
  Solitonmodelle) und "Phase Shifts of the Skyrmion Breathing Mode" (1984, PRL 53, 889: Skyrmion, nicht FL-Beutel).
  Bestaetigt (keine strahlungsfreie Beutelschwingung).
- N3 Kim/Nugaev/Shnir 2024 (2405.09262) [L?]: UV-vervollstaendigtes FLS, Ein-Schleifen-Potential, Duennwand, E ~ Q
  statt Q^(3/4); keine Moden/Abstrahlung. Bestaetigt. ("Kim" der Karte = Eduard Kim, mit Nugaev und Shnir.)

### Block O, Vorhersage notiert 18:50:23 (date) vor dem Abruf
- O1 2303.09566 Heeck/Sokhashvili: Profile, Duennwand/Dickwand, Stabilitaet ueber Q(omega); keine Moden mit
  Abstrahlung.

Ergebnis O1 (18:50:23-18:51:43 date): Heeck/Sokhashvili 2023 (EPJC 83, 526) [L?]: FLS neu betrachtet, Gemeinsamkeiten
und Unterschiede zu Q-Baellen, analytische Naeherungen; keine Moden/Abstrahlung. Bestaetigt.

### Block P (Primaerquellenpruefung des wichtigsten Fundes), Vorhersage notiert 18:51:43 (date)
- P1 PDF 2412.13885 selbst lesen (Abschn. 3 und Summary): Die Abrufmodell-Aussagen bestaetigen sich (FLS-Potential
  Gl. 49, drei Kanaele, "for the first time" im Summary, keine inneren Moden). Grund: Gedaechtnisregel "Suchtreffer-Zitat
  vor Vertrag an der Quelle lesen" - die Kernaussage zu Frage 4 haengt an dieser Quelle.

Ergebnis P1 (18:51:43-18:52:17 date) [S, PDF 2412.13885v1 selbst gelesen, S. 1-2, 13-14, 18-20]:
- Abstract: "as well discussion of the FLS Q-balls". Abschn. 3 (S. 13): Modelle "first studied by Friedberg, Lee and
  Sirlin (FLS)"; Lagrangedichte Gl. (46), Potential Gl. (47) (Abrufmodell hatte "Gl. 48-49" gesagt: BERICHTIGT auf 46-47;
  Gl. 48 Bewegungsgleichungen, Gl. 49 Ansatz, Gl. 50 lineare Stoerungen). Abb. 7 (S. 14): FLS-Profile bei g_chiPhi = 4,
  g_chi = 1, g_Phi = 0.04, v_chi = 1, m_Phi = 0, omega_Q = 1.0 bis 1.6; chi_Q geht im Inneren gegen 0 (Beutel).
- S. 18: Z_E, Z_Q fallen nahe der Schwelle zweier offener geladener Kanaele auf null; Abb. 10: Energieverstaerkung bei
  einlaufendem eta_chi wechselt mehrfach das Vorzeichen ("sign of Z is not fixed"), also Nullstellen des Energie-
  AUSTAUSCHS, nicht der Abstrahlung. Abschn. 3.1.1: sechs Kanalregime (Bedingungen omega^2 gegen 8 g_chi v^2 und
  (omega +- omega_Q)^2 gegen g_chiPhi v^2 + m_Phi^2), "bounded" = geschlossener Kanal. Abb. 11: Kanal-Landkarte.
- Summary (S. 20): "for the first time we have analyzed the perturbations of the FLS Q-ball solution".
- Keine inneren Moden, keine BIC, kein Radiusscan. Vorhersage P1 bestaetigt (mit Gleichungsnummer-Korrektur).

### Block P2, Vorhersage notiert 18:52:17 (date) vor dem Abruf
- P2 PDF 2510.27064 selbst lesen (Abschn. IV.1-IV.3): Duennwand-Verstaerkung als Sinusfunktion von sigma_+- r_*,
  sigma_+- = Summe/Differenz der Innenwellenzahlen; Periode im Radius pi/sigma; keine Nullstellen der Abstrahlung.

Ergebnis P2 (18:52:17-18:53:04 date) [S, PDF 2510.27064v1 selbst gelesen, S. 11-14]:
- Gl. (101)-(102) -rho_1,2 wie oben; Gl. (108) N_+^out rationale Funktion von cos(sigma_- r), sin(sigma_+ r) bei r = r_*;
  Gl. (109) sigma_+- = sqrt(-rho_1) +- sqrt(-rho_2).
- S. 11: "thin-wall location r_* plays the central role in controlling the number of peaks".
- S. 12, Abb. 3: Karten der Verstaerkungsfaktoren ueber (omega, r_*) (omega_Q = 0.52, f_0 = 1.20, g = 1/3, n = 1):
  Maxima/Minima liegen auf Baendern, die sich in r_* periodisch wiederholen -> faktisch eine Radius-Leiter von EXTREMA
  der Streuverstaerkung (nicht von Nullstellen einer Normalmoden-Abstrahlung).
- S. 13: "sigma_+ ~ 2 omega and sigma_- ~ 2 omega_Q" (grosses omega); Oszillation schneller fuer groessere Q-Baelle.
- S. 14, Gl. (114)-(118): N ~ 1 - W^2/(4 omega_Q^2 omega^2) sin(2 r_* omega_Q + phi_-)^2 + ...; Periode im Radius
  pi/sigma_- (Grundterm) bzw. pi/sigma_+ (schneller Term) = halbe Wellenlaenge der Differenz- bzw. Summenwelle der zwei
  Innenkanaele. Vorhersage P2 bestaetigt.
- [H] Damit ist eine Halbwellen-Periodizitaet besonderer Merkmale im Wandradius in der Q-Ball-Streuliteratur explizit
  (Einfeld-Sextik, Duennwand). Fuer F3 wichtig: kein FLS, keine stillen Stellen, aber derselbe Leitertyp.

## 4. Erwartungsverstoesse (Stand 18:53:04 date, Reihenfolge nach Gewicht)

1. Frage 4/Regel 4: Das Leiterpapier zitiert mit Azatov2024 (= 2412.13885v1) bereits die nach eigener Aussage erste
   lineare FLS-Stoerungsanalyse (Abschn. 3, S. 13-20), beschreibt sie aber nur als Einfeld-Sextik (LITERATURE.tex Z. 24-31).
2. Frage 3: Halbwellen-Periodizitaet im Wandradius ist Q-Ball-Literatur (2510.27064, Gl. 108-118, Abb. 3), dort fuer
   Streuverstaerkung (Extrema), Einfeld-Sextik; FLS numerisch nur "more peaks" fuer groessere Solitonen (2503.04657).
   Erwartet war "keine Halbwellen-Bedingung" bzw. eine reine Resonanz-Quantisierung.
3. Frage 2/3 (Nachbarfeld): Eine Folge besonderer Groessen mit unterdrueckter Abstrahlung ("multiple dips") ist fuer
   reelle phi^6-Oszillonen belegt (2004.01202 Abschn. 7.5; Mechanismus Gl. 7.4: Fourier-Nullstelle der Quelle).
4. ~~Oszillonen: effektive Masse statt Fourier-Nullstelle~~ (gestrichen 18:48, siehe Block L).
5. Kleiner: Lineare FLS-Analyse existiert erst seit Dez. 2024; 1976-2024 nur Profile/Stabilitaet (passt zur eigenen
   Vorwegnahme, kein Verstoss, aber bemerkenswert fuer "Neuheit").

## 5. Fundliste

Siehe ERGEBNIS.md Abschnitt 4 (dort vollstaendig mit Marken).

## 6. Offene Rueckfragen

- An die Leitung: Soll das Leiterpapier Azatov2024 auch fuer den FLS-Abschnitt 3 zitieren und die Superradianz-Reihe
  sowie die Oszillon-Dips als Vergleich aufnehmen? (Entscheidung Finn/Leitung, nicht Literatur-Agent.)
- Offen (nicht pruefbar ohne Volltext): Iwasaki/Kondo 1987, Haider 1993, Lee/Pang 1992, Wilets 1989 (Buch),
  Goldflam/Wilets 1982 - Beutelschwingungen mit Breite?
- Offen [H]: Liegt die M2-Leiterperiode bei pi/k_in einer Kanalwelle oder bei pi/(k_1 -+ k_2) wie in 2510.27064?
  (Projektrechnung, nicht Literatur.)
- Nicht erledigt: Radu/Volkov 0804.1357 ("non-radiating") nicht geprueft (Gegensweep Punkt 6 in ERGEBNIS.md).

## 7. Abschluss

- ERGEBNIS.md geschrieben 18:55:26-18:58:52 (date). Danach keine weiteren Abrufe. Zeitbox eingehalten (Ende vor 19:31).
- Gegenlesen rueckwaerts (Zahlen, Gleichungs- und Seitenangaben gegen dieses Protokoll) vor Abgabe durchgefuehrt; zwei
  Stellen berichtigt (Honda/Choptuik: r_0-Bezug nicht aus dem Abstract belegt; Interferenz-Deutung als [H] markiert).
