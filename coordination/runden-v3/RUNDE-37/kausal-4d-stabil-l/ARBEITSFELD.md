# ARBEITSFELD KAUSAL-4D-STABIL-L (Feldforscher, Runde 38)

- Start 2026-10-04 08:11:06 CEST (date). Zeitbox 75 min, also bis ~09:26 CEST.
- Eine Datei fuer alle Zwischenstaende. Gestrichenes bleibt stehen (~~so~~). Offene Rueckfragen unten, sie wandern mit.
- Kennzeichen: [S] an der Quelle gelesen; [L] Gedaechtnis; [L?] unsicher; [ES] eigener Schluss; [H] Hypothese.
- Gelesen (lokal): KARTE.md; kausal-welle-4d/ERGEBNIS.md, PLAN.md, code/kontinuum4d.py (ganz), kausal4d.py (Kopf),
  lauf-69/kont/kontinuum.json (Pole), auswertung.json (Urteile); kausal-welle-1/ERGEBNIS.md; RUNDE-38/WEICHE-STAND.

## 0. Erwartungen der Karte (vor jedem Abruf, unveraendert)

| Nr | Erwartung (Kurz) | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | Polformel 1. Ordnung richtig; Hochrechnung ~ m^3 l_P^2 | **eingetroffen** | Schritt C/E; Johnston 2014 (100), (101) bitgleich; ASS (3.7), (3.10) fuer Formel und Zweig. Zusatz: 1-%-Treffer bei rho = 16 teils Zufall; l = l_P ist Annahme (Surya 2019, Lambda-Abschnitt) |
| E2 | Instabilitaet 4D-Operatoren bekannt (ASS 2014) [L?] | **teilweise** | Wortlaut ja: ASS 2014 Abstract, S. 8, 17; Surya 2019 Z. 7403; BBL 2015. Sache nein: anderes Regime (UV, masselos), siehe V2 |
| E3 | Glaettung macht stabil; Preis neue Laengenskala >> l_P | **nicht eingetroffen** | ASS S. 17 ("not able to find any"); Surya 2019 ("open question"); A6/A12 nichts Neueres. Fuer Johnstons Mittel verschlimmert Glaettung (2b). Literatur-Abhilfen sind andere (V4) |
| E4 | Fuer Johnstons Pfadsumme selbst nicht beschrieben | **eingetroffen** (nach Recherchestand) | Johnston 2010 S. 48, 2014 (101)-(102) und Schluss; Shuman 2023; Hinrichsen/Kastrati 2026; A6/A12. Aber: Korrekturterme erster Ordnung stehen bei Johnston 2014 (V5) |
| E5 | Mittel nicht die ganze Physik; Literatur meist Mittel | **teilweise** | Literatur meist Mittel: ja (ASS S. 10 "exclusively with the continuum operator"; BBL). Fuer Johnstons Propagator meldet die Literatur aber fallende Varianz (Johnston 2010 S. 46; 2014 Schluss), also naehert sich die Einzelrealisierung dem Mittel; im 4D-Lauf ist G je Saat (Median 1,69-2,09) so gross wie G des Mittels (1,63-1,98). Das Mittel ist hier vermutlich die relevante Groesse; Langzeit-Selbstmittelung offen [H] |

## 1. Gegensweep zuerst (Projekt-grep, 08:11-08:17 date-Fenster)

- grep aslanbeigi|saravani|benincasa|nichtlokal|nonlocal: 109 Dateien. Meist Code-Variablen ("nonlocal") oder
  arXiv-Rohdaten. Inhaltlich zaehlen:
  - **RUNDE-22/geometrie-stand/hilfs/surya-1903.11544.txt** = Suryas Living Review 2019 als Text, seit Runde 22 im
    Projekt. Dort [S, lokal]:
    - Z. 7403-7409: "There are indications that while the evolution in d = 2 is stable, it is unstable in d = 4 as
      suggested by Aslanbeigi et al (2014)." ... "still an open question whether there is a subfamily of these operators
      that lead to a stable evolution."
    - Z. 9065-9070: Belenchia et al (2015): QFT "contain critical instabilities. These can be removed by modifying the
      d'Alembertian, but the relationship to CST is unclear."
    - Z. 8020-8030: Johnstons 4D-Propagator (65), (66): nur lim rho -> inf von sqrt(rho) <K_M> = G_m. Kein Wort zu
      Anwachsen bei endlicher Dichte.
    - Z. 7496-7520: Sorkins Mesoskala l_k > l_c, eps = rho_k/rho_c, Glaettungsfunktion f(n, eps) (36), (37).
    - Literaturliste bestaetigt die Nummern: 0806.3083, 1010.5514, 1403.1622 (JHEP 06:024), 1411.6513 (JHEP 03:036),
      gr-qc/0703099, 1512.02083 (PRL 116:161303), 1510.04656, 1701.07212, 1403.6429; Dowker/Glaser CQG 30:195016
      (arXiv-Nummer dort nicht genannt).
  - RUNDE-37/UEBERLEITUNGEN-EMERGENZ.md Z. 111-124 und kausal-welle-1: nur Verweise [L], keine Pruefung.
  - RUNDE-38.md Z. 105: "Kein Benincasa-Dowker-Vergleich (Zeitbox)".
- **Folge [ES]:** E2 ist schon vor jedem Abruf im Projekt belegt (Surya, lokal). Neu zu klaeren: welches Regime die
  4D-Instabilitaet der BD-Operatoren hat (an der Nichtlokalitaetsskala oder an der Massenschale) und ob es seit 2019 eine
  stabile 4D-Familie gibt. E3 ist durch Surya 2019 schon angekratzt ("open question").

## 2. Teil 1, Nachrechnung am Schreibtisch (vor 08:21, Kopfrechnung ohne Rechner)

Schritt A, Erwartungswert der Pfadsumme [ES]:
- Pfad x = z0 < z1 < ... < zn = y aus n Links. Die offenen Intervalle I(z_{i-1}, z_i) einer Kette sind paarweise
  disjunkt (ein w in zwei Intervallen muesste vor und nach demselben z_i liegen). Also faktorisiert die
  Leer-Wahrscheinlichkeit exakt: prod exp(-rho V_i).
- Mit der Mecke-Formel (Poisson): E[#Pfade] = rho^(n-1) mu^(*n). Damit K_P = sum a^n b^(n-1) rho^(n-1) mu^(*n),
  K_P~ = a mu~/(1 - a b rho mu~). Mit b = -m^2/rho: K_P~ = k~/(1 + m^2 k~), k~ = a mu~. **Folgt.**
- E[phi(x)] = (1/rho) E[sum_y K(y,x) J(y)] = int K_P J (Campbell). **Folgt.**

Schritt B, Fouriertransformierte retardierter lorentzinvarianter Funktionen [ES]:
- Bei k = 0, omega = i Omega: F = 4 pi int tau^3 f(tau) dtau int sinh^2(chi) exp(-Omega tau cosh chi) dchi.
- Inneres Integral = K1(z)/z (Integraldarstellung von K_nu mit nu = 1). Also F(Z) = (4 pi/Z) int tau^2 f K1(Z tau)
  dtau mit Z = Omega; Lorentzinvarianz und Analytizitaet in Im omega > 0 setzen fort auf Z^2 = |k|^2 - omega^2.
  **Folgt, gleich wie im Code (amu).**
- Probe: fuehrender Term K1(x) ~ 1/x gibt pi a sqrt(pi/c)/Z^2 mit c = pi rho/24; mit a = sqrt(rho)/(2 pi sqrt 6)
  ist pi a sqrt(pi/c) = 1 exakt. Also k~ -> 1/Z^2 und K_P~ -> 1/(Z^2 + m^2). **Folgt.**

Schritt C, Polformel [ES]:
- Naechste Ordnung aus K1(x) = 1/x + (x/2) ln(x/2) + (x/4)(2 gamma - 1) + O(x^3 ln x):
  k~ = 1/Z^2 + eps [ln(Z^2/sqrt c) + C'] + O(eps Z^2/sqrt c), eps = pi a/(4c) = sqrt 6/(2 pi sqrt rho),
  C' = (3/2) gamma - 1 - 2 ln 2 = -1,5205.
- 1 + m^2 k~ = 0 mit Z^2 = -m^2 + delta: delta = m^4 eps [ln(-m^2/sqrt c) + C'].
- Zweig: omega = omega_r + i Gamma, omega_r > 0, Gamma > 0 gibt Im Z^2 < 0, also ln(-m^2) = ln m^2 - i pi.
- omega = omega0 - delta/(2 omega0) gibt **Im omega = pi m^4 eps/(2 omega0) = (sqrt 6/4) m^4/(omega0 sqrt rho).**
  Genau die Formel des Code-Agenten. Vorzeichen: e^{-i omega t} waechst fuer Im omega > 0. **Folgt.**
- Selbstkonsistenz: Im delta < 0 heisst Im Z^2 < 0, also liegt die Nullstelle wirklich auf dem physikalischen Blatt
  (Im omega > 0, Re Z > 0). Der Code erzwingt Re Z > 0 ebenfalls.
- **Lorentz-Probe [ES]:** Im omega = (sqrt 6/4) m^3/(gamma sqrt rho) fuer omega0 = gamma m. Das ist die Ruherate
  geteilt durch gamma, also Zeitdilatation. Die Rate je Eigenzeit ist invariant: (sqrt 6/4) m^3 l^2, l = rho^(-1/4).
- Masselos: K_P~ = k~ selbst, ohne Nenner. k~ ist in Im omega > 0 analytisch (beschraenkter Kern im Kegel), also
  **keine Pole fuer m = 0**. Das Anwachsen ist ein reiner Masseneffekt.

Schritt D, Gueltigkeit fuer m^2/sqrt(rho) -> 0 [ES]:
- Die Reihe in Z^2/sqrt(c) konvergiert (K1 minus Pol- und Logteil ist ganz; Momente von e^{-c tau^4} wachsen nur wie
  Gamma-Funktionen). Jede weitere Ordnung bringt m^2/sqrt(rho) (mit Log). Relativer Fehler der Polformel:
  O((m^2/sqrt rho) ln(sqrt rho/m^2)). Bei Planckdichte und Elektron ~1e-45, also exakt fuer alle Zwecke.
- Weitere Nullstellen (Luecke des Code-Agenten, "oberhalb Im omega = 1,4 nicht ausgeschlossen"):
  - |Z| >> c^(1/4): k~ ~ 8 pi a/Z^4 (int u^2 K1 = 2), also |m^2 k~| <~ 12,5 m^2/sqrt(rho) << 1.
  - |Z| ~ c^(1/4): |k~| = O(1/sqrt rho), also |m^2 k~| << 1.
  - m << |Z| << c^(1/4): k~ ~ 1/Z^2, |m^2 k~| << 1.
  - **Fuer m^2/sqrt(rho) << 1 gibt es nur die eine Nullstelle an der Massenschale [ES, Groessenordnung, nicht
    streng].** Bei rho = 4 bis 16 (m^2/sqrt rho = 0,5 bis 0,25) ist das nicht gezeigt.
- **Die 1-%-Treffer bei rho = 16 sind teils Zufall [ES]:**
  - Erste Ordnung: Re omega = 1,092, Im omega = 0,153. Numerisch: 1,0545 + 0,1523 i.
  - Mit zweiter Ordnung der Gleichung (delta (1 + eps) + delta^2 = eps L0): 1,073 + 0,170 i. Der naechste K1-Term
    schiebt grob um -0,01 je Teil. Die Korrekturen sind einzeln ~10 % und heben sich im Imaginaerteil zufaellig weg.
  - Bei rho = 4 / 8 liegt die erste Ordnung 25 % / 9 % ueber der Numerik (0,306 / 0,217 gegen 0,246 / 0,198).
  - Fuer die Hochrechnung ist das gleichgueltig (Korrekturen ~1e-45), fuer "trifft auf 1 %" als Guetebeleg nicht.

Schritt E, Hochrechnung (Kopfrechnung) [ES]:
- Gamma = 0,612 (m c^2/hbar) (m/m_P)^2 mit m l_P = m/m_P und l = l_P (rho = l_P^-4). Einheiten: 1/s. **Stimmt.**
- Elektron: m c^2/hbar = 7,76e20 /s; (m/m_P)^2 = (4,19e-23)^2 = 1,75e-45; Gamma = 8,3e-25 /s; 1/Gamma = 1,2e24 s =
  2,8e6 Weltalter (4,35e17 s). **Stimmt (~3e6).**
- Top (172,7 GeV): 2,63e26 /s; (1,41e-17)^2 = 2,0e-34; Gamma = 3,2e-8 /s; 1/Gamma = 3,1e7 s = 0,98 Jahre. **Stimmt.**
- Gegenprobe Messlauf [ES]: Norm ~ e^(2 Gamma Delta t), Delta t = 1,5 (Scheibenmitten 2,25 bis 3,75):
  rho = 16: e^(0,457) = 1,58 gegen G = 1,63 / 1,68; rho = 4: e^(0,738) = 2,09 gegen 1,87 / 1,98. Passt grob.
- **Was die Hochrechnung nicht sagt [ES]:**
  - Sie gilt fuer einen freien Skalar mit Johnstons unveraenderten Amplituden. Elektron und Top sind keine Skalare;
    fuer Fermionen gibt es keinen 4D-Johnston-Propagator. Das einzige elementare Skalarfeld ist das Higgs.
  - **Higgs (125,1 GeV):** 1/Gamma = 1 Jahr x (172,7/125,1)^3 = 2,6 Jahre. Ueber das Weltalter ~5e9 e-Faltungen.
    W/Z (als Skalare gerechnet): ~10 / ~7 Jahre. Myon 0,3 Weltalter, Tau ~0,9 Mio. Jahre.
  - Woertlich genommen haette die linearisierte Higgs-Dynamik um das Vakuum dann wachsende Moden, das Vakuum waere
    instabil. **Damit ist der Einwand fuer schwere Skalare staerker als im ERGEBNIS formuliert [ES/H]**, sofern das
    Ensemble-Mittel die wirksame Dynamik ist (Schritt F) und rho ~ l_P^-4.
  - Planck-Konvention: l = rho^(-1/4) ist nicht festgelegt. Gamma ~ l^2; Faktor 2 in l gibt Faktor 4 in der Rate.

Schritt F, Lesart Mittel gegen Einzelrealisierung [ES/H]:
- E[phi] ist das "koharente Feld" einer Welle im Zufallsmedium. Seine Gleichung hat die Form 1/(Z^2 + m^2 + Sigma)
  mit Sigma = -eps Z^4 [ln(Z^2/sqrt c) + C'] (Dyson-Form). Im Sigma auf der Schale hat das "falsche" Vorzeichen:
  Anti-Daempfung statt Extinktion. In gewoehnlichen Zufallsmedien daempft der Imaginaerteil, weil Energie in den
  diffusen Anteil streut; Johnstons Gewichte haben keinen Erhaltungssatz, der das erzwingt.
- Jensen: E|phi|^2 >= |E phi|^2. Waechst das Mittel, waechst die mittlere Leistung mindestens doppelt so schnell.
  Eine typische Einzelrealisierung (E ln|phi|) kann langsamer wachsen als das Mittel (geglueht gegen gequencht),
  aber die Korrektur je Schwingung (~1e-34 beim Top) stammt aus der mittleren Linkdichte am Lichtkegel, also aus
  sehr vielen Elementen. **[H] Sie mittelt sich wahrscheinlich selbst; eine Einzelrealisierung waechst dann mit
  derselben Rate plus Rauschen.** Nicht gezeigt.
- Fuer eine endliche Kausalmenge ist K = Phi (I - b Phi)^-1 eine endliche Summe (Phi nilpotent). "Instabil" heisst
  dort nur: Anwachsen ueber lange Laufstrecken, keine Divergenz.

Luecken, denen ich nicht folgen kann bzw. die ich nicht geprueft habe:
- L-a: Johnstons Gl. (3.13) bis (3.15), (3.32) habe ich nicht an der Quelle gelesen; Schritt A ist eine unabhaengige
  Herleitung derselben Formel.
- L-b: Zweite Ordnung nur skizziert (Groessenordnung), nicht sauber.
- L-c: Die Numerik von pol_k (Newton mit Differenzenquotient, 96 Knoten) nicht nachgerechnet; nur Plausibilitaet.
- L-d: Ob das Mittel die wirksame Dynamik ist, ist eine Modellfrage, keine Rechenfrage (Schritt F).

## 3. Abrufprotokoll (Vorhersage vor Abruf; Ausgang danach)

| Nr | Zeit | Quelle | Vorhersage (vor Abruf) | Ausgang | Verstoss? |
|---|---|---|---|---|---|
| A12 | 08:40-08:42 (date-Fenster) | arXiv-API all:"causal set" UND (stability ODER unstable ODER instability ODER instabilities), neueste zuerst, 30 | Keine Arbeit der letzten 24 Monate mit stabiler 4D-Familie oder Wachstum von Johnstons Mittel; Treffer eher zu Wachstumsmodellen (CSG), Mannigfaltigkeitsnaehe, Entropie | Eingetroffen. Nur 9 Treffer; einschlaegig nur BBL 2015 und ASS 2014; in 24 Monaten nur fachfremde bzw. allgemeine (2512.00933 Dispersionsrelationen). Daneben Kaloper/Mattingly astro-ph/0607485 (Schranken auf Swerves) und 1210.2589 (Lambda). | nein |
| A11 | 08:40-08:42 (date-Fenster) | arXiv-API id_list gr-qc/0703099 (Sorkin 2007), 1305.2588 (Dowker/Glaser 2013), Abstracts woertlich | Sorkin: 2D-Operator aus der Kausalmenge, Fluktuationen, Nichtlokalitaetsskala zwischen Planck- und Kernskala; Dowker/Glaser: Operatoren fuer alle Dimensionen mit Glaettung; **beide ohne Stabilitaetsaussage** | Eingetroffen. Sorkin: Nichtlokalitaet "survives at much lower energies", nichtlokale Bewegungsgleichung fuer Skalar. Dowker/Glaser: Operator fuer jede Dimension, daraus Kruemmungsschaetzer und Wirkung. Keine Stabilitaetsaussage im Abstract. Nummern und Titel stimmen. | nein |
| A10 | 08:38-08:40 (date-Fenster) | arXiv 2604.24812v1 (Hinrichsen, Kastrati 2026, "Link-based causal set propagators in 1+1"), PDF, pdftotext | 1+1, Linkkern exp(L), Masse ueber Streureihe (wie Johnston); Rauschen und Kontinuumsgrenzfall numerisch; **kein** Anwachsen bzw. keine Polverschiebung in Im omega > 0 besprochen; nichts zu 3+1 | Eingetroffen. Nur 1+1; Masse "via the usual mass-scattering series"; rho = 5000, m = 5, 30 Laeufe "very good agreement"; 3+1 nur Motivation ("trivially true" fuer Potenzreihe in L). grep unstab/grow/pole/imaginary: nichts Einschlaegiges. **Achtung: die WebFetch-Zusammenfassung behauptete Pole, Daempfung und Wachstumsinstabilitaeten; das steht nicht im Text (Halluzination des Zusammenfassers).** | Methode (siehe Gegensweep G4) |
| A9 | 08:33-08:38 (date-Fenster) | arXiv 1512.02083 (Belenchia u. a., PRL 116 (2016) 161303), PDF, pdftotext | Schranke aus bisherigen Daten (LHC) l_k <~ 1e-19 bis 1e-18 m; vorgeschlagene Optomechanik reicht tiefer; keine Schranke auf Johnston-artiges Massenschalen-Wachstum | Eingetroffen. LHC 8 TeV (deren Ref. 18): "lk <= 10^-19 m"; Optomechanik Grundzustand: "lk < 2 x 10^-15 m"; erste Schaetzungen aus Ref. 26 (thermische koharente Zustaende, schlimmster Fall): 2e-22 m bis 1e-29 m, "best forecast falls short by roughly six orders" von l_P. Nur fuer BD-artige Nichtlokalitaet, nicht fuer Massenschalen-Wachstum. | nein |
| A8 | 08:33-08:38 (date-Fenster) | arXiv 2307.08864 (Shuman 2023, "Path Sums for Propagators in Causal Sets"), PDF, pdftotext | Allgemeine Sprung-/Haltamplituden, Bedingungen fuer den Kontinuumsgrenzfall, auch 3+1 ueber Links; **keine** Analyse endlicher Dichte mit Polen in Im omega > 0; vielleicht Mehrschicht-Spruenge | Eingetroffen. Allgemeine Gleichung "average jump amplitudes" gegen mittleren Propagator; numerisch nur 2D retardiert; "at small proper times they may differ greatly". Kein Wort zu Stabilitaet, Wachstum, Polen (grep leer). | nein |
| A7 | 08:33-08:38 (date-Fenster) | arXiv-API id_list: 2606.00311, 2604.24812, 2608.18753, 2506.18745, 2307.08864, 2305.07595, 1512.02083, 1512.08485, 1801.02582 (Abstracts) | 2604/2608: Johnston-Pfadsummen in 1+1, ohne Instabilitaet; 2606.00311: Pauli-Jordan/SJ, nicht Johnstons 4D-Mittel; 2506.18745: lokaler Operator ohne Stabilitaetsaussage in 4D; 2307.08864: Familie von Pfadsummen (Amplituden), ohne 4D-Wachstum; 2305.07595: nichtlokale Higgs-QFT, Landau-Pol; 1512.02083: Optomechanik, Schranke l_k im Bereich 1e-18 m oder schwaecher | (folgt) | |
| A6 | 08:33-08:38 (date-Fenster) | arXiv-API export.arxiv.org: abs "causal set" UND (propagator ODER Alembertian ODER nonlocal), neueste zuerst, 40 | wie A5 | Eingetroffen, soweit Titel reichen: 40 Treffer 2014-11 bis 2026-08; in 24 Monaten (ab 2024-10) nur 1+1-Propagatoren (2604.24812, 2608.18753), 2D-AdS (2504.12919), lokaler Operator (2506.18745), Spektraldichte (2606.00311); kein Titel zu 4D-Stabilitaet. Aelter, aber einschlaegig: 2307.08864 "Path Sums for Propagators", 2305.07595 Higgs-Schranke | nein (Titel), Abstracts in A7 |
| A5 | 08:33-08:38 (date-Fenster) | INSPIRE-API: Arbeiten, die ASS 2014 zitieren, neueste zuerst (Titel, Datum) | Juengste Zitate (2024-2026) zu Kausalmengen-QFT, Verschraenkung, Spektraldimension, Phaenomenologie; **keine** bewiesen stabile 4D-Familie; keine Arbeit zum Anwachsen von Johnstons 4D-Mittel | **Fehlschlag:** Abfrage nicht als refersto ausgewertet, 25 113 fachfremde Treffer (Quantenrechnen, Astro). Abruf verbraucht, kein Inhalt. | Methode, nicht Inhalt |
| A4 | 08:30-08:33 (date-Fenster) | arXiv 1411.2614v2 (Johnston, "Correction terms for propagators and d'Alembertians due to spacetime discreteness", 2014/2015), PDF lokal S. 15-16 als Bild, Rest per pdftotext | Rechnet die Korrekturen endlicher Dichte fuer 2D/4D-Propagatoren und d'Alembert-Operatoren als Reihe in rho^(-1/2) mit ln-Termen; behandelt sie als kleine Korrekturen (m^2 << sqrt rho); **erwaehnt kein Anwachsen bzw. keine Pole in Im omega > 0** (E4 bliebe stehen); hoechstens "Masse/Dispersion verschoben" | Eingetroffen. (100), (101): A1 = (3/(2 pi sqrt 6))[3 gamma - 2 - ln(2 pi rho/(3 s^2))], **bitgleich mit meinem eps [ln(Z^2/sqrt c) + C'] (s = Z^2)**. Massiv nur als formale Reihe in 1/sqrt(rho); (102) enthaelt box G_m * box G_m, einen saekularen (linear wachsenden) Term; kein Wort zu Polverschiebung oder Wachstum. Schluss: Varianz der Propagatoren faellt laut Simulation mit rho ("cancellations of random fluctuations"). | nein; Bestaetigung von Schritt C an der Quelle |

A4-Notiz [S]: (111) L{B-quer} = s^2 L{K0} (Kasten/Exponent im pdftotext verloren, aus (103) und (98)-(99) erschlossen),
also wieder B~ = Z^4 k~. (109) 2D: L{B-quer} = s - (s^2/(2 rho))(ln(2 rho/s) - gamma): Koeffizient von s^2 ln s ist
+1/(2 rho), wie aus ASS S. 6 (gesund). 4D: B~ = s + s^2 A1/sqrt(rho), Koeffizient von s^2 ln s: +eps (gesund);
Johnstons 1/k~: -eps. **Vorzeichenbefund an zwei Quellen gegengeprueft.**
- [ES] Johnstons Reihe (101) ist die Entwicklung eines verschobenen Pols nach delta: 1/(s + m^2 - delta) =
  1/(s + m^2) + delta/(s + m^2)^2 + ... Die abgebrochene Reihe ist nur fuer t << sqrt(rho)/m^3 gleichmaessig gueltig;
  die Resummation gibt das exponentielle Anwachsen. Johnston hat das Material, aber nicht die Folgerung.
| A3 | 08:30-08:33 (date-Fenster) | arXiv 1411.6513 (Belenchia, Benincasa, Liberati 2015), PDF, per pdftotext durchsucht | IR-Entwicklung des 4D-Operators mit p^4 ln p^2 und Imaginaerteil fuer zeitartige p; Feynman-Propagator/Spektraldarstellung mit Kontinuum; "critical instabilities" = die ASS-UV-Nullstellen, Abhilfe durch geaenderte Koeffizienten bzw. Glaettungsfunktion; Johnstons Propagator nicht behandelt; zu massiven Polen hoechstens eine Breite | Teils. Instabile 4D-Moden = komplexe Massen (ASS), "Abhilfe" durch **Quantisierung mit Wheeler-Propagator** (halb retardiert, halb avanciert), nicht durch neue Koeffizienten; Deutung "open issue". **Massive Erweiterung: naive (f(box) - m^2) hat keine reelle Massenschale, deshalb f(box + m^2)**; wie das auf der Kausalmenge aussieht, "open issue". Fussnote 7 verweist auf Johnston 1411.2614 mit denselben Korrekturtermen. | ja (V4: Massenterm-Abhilfe im Argument; V5: Johnston 2014 existiert) |
| A2 | 08:24-08:30 (date-Fenster) | arXiv 1010.5514 (Johnston, Doktorarbeit 2010), PDF 172 S., per pdftotext auf stdout durchsucht (keine Datei angelegt) | Wiederholt 2008: 3+1-Mittel nur fuer rho -> inf das Kontinuum, Bedingung m^2 << sqrt(rho); hoechstens kleine 4D-Simulationen; **keine** Pole in Im omega > 0, kein Anwachsen des Mittels erwaehnt | Eingetroffen. **Zusatzfund Anhang A.3.2: box^2 K_R = B-quer** (siehe A2-Notiz) | ja, Zusatzfund (Verstoss V3) |

A2-Notiz [S, Johnston 2010, arXiv:1010.5514; Seitenzahlen der Arbeit]:
- (3.45) K_P~ = a P~/(1 - a b rho P~); (3.57) a = sqrt(rho)/(2 pi sqrt 6), b = -m^2/rho; nur Grenzwert (3.55) gerechnet.
- S. 48, 3.8.2: Mittel = Kontinuum "only ... in the infinite density limit"; Planckdichte "large but finite";
  "good agreement only for very large sprinkling densities". Simulation rho = 480625, m = 10, kleines Intervall: "We do
  not yet see the Bessel function behaviour". Kein Wort zu Polen, Wachstum, Instabilitaet (grep: unstable, instabilit,
  grow, exponential, upper half: keine Treffer zur 4D-Pfadsumme).
- Andere bekannte 4D-Maengel der Pfadsumme (S. 69-71): auf R x T^3 sterben die Links in der fernen Zukunft aus, der
  masselose Propagator ist dann exponentiell unterdrueckt; in gekruemmter Raumzeit keine "tails" (Huygens).
  "the 3+1 dimensional model would require modification if it were to reproduce a Green's function with a tail."
- S. 80: BD-Fluktuationen "large and grow with the sprinkling density"; Ausweg Mesoskala (Sorkin 2007).
- **Anhang A.3.2, (A.58)-(A.62): box^2 C = 8 pi delta; box^2 K_R = B-quer**, mit K_R = Mittel des masselosen
  4D-Propagators (= Johnstons k) und B-quer = Kern des gemittelten Benincasa-Dowker-Operators. (pdftotext verliert
  das Kastensymbol; "2 KR = B" ist box^2 K_R = B-quer. Gegenprobe siehe naechster Punkt.)
- **Gegenprobe [ES]:** Daraus folgt B~(Z) = Z^4 k~(Z) (Johnstons Vorzeichenkonvention, B~ -> Z^2).
  - UV: k~ ~ (4 pi a/Z^4)(2 - 384 c/Z^4) (int u^2 K1 = 2, int u^6 K1 = 384) gibt Z^4 k~ = 4 sqrt(rho)/sqrt 6 -
    32 pi rho^(3/2)/(sqrt 6 Z^4). ASS (2.17): rho^(-1/2) g -> -4/sqrt 6 + 32 pi/(sqrt 6 Z_A^2), mit g = -B~ und
    Z_A = Z^2/sqrt(rho) **genau dasselbe, beide Ordnungen**. IR: Z^4/Z^2 = Z^2. **Identitaet bestaetigt.**
- **Folgen [ES]:**
  - BD-Operator = Z^4 k~, Johnstons wirksamer Operator = 1/k~. IR: B~ = Z^2 + eps Z^4 [ln(Z^2/sqrt c) + C'],
    1/k~ = Z^2 - eps Z^4 [...]. **Gleicher Term, entgegengesetztes Vorzeichen.**
  - Massiver Skalar mit 4D-BD-Mittel: Pol bei Im omega = -(sqrt 6/4) m^4/(omega sqrt rho) auf dem zweiten Blatt, also
    **Zerfall mit genau der Rate, mit der Johnstons Mittel waechst**. Johnston: negative Spektraldichte; BD: positive.
  - Die UV-Instabilitaet von BD (ASS Abb. 3a) sind Nullstellen von k~. Fuer Johnston sind das Nullstellen des
    Propagators, harmlos. BD und Johnston haben also je eine Instabilitaet, an verschiedenen Stellen: BD im UV
    (masselos), Johnston im IR (nur massiv).
| A1 | 08:21 | arXiv 1403.1622 (ASS 2014), PDF (WebFetch speicherte das PDF, lokal gelesen S. 1-21) | Enthaelt Fourierformel mit K-Bessel fuer retardierte LI-Funktionen; Stabilitaetskriterium = keine Nullstelle von B~(+m^2) in Im omega > 0; urspruengliche 4D-Operatoren instabil mit Polen an der Nichtlokalitaetsskala (auch masselos); keine sicher stabile 4D-Familie (Surya: "open question"); IR-Entwicklung mit Z^4 ln Z^2 | Alles eingetroffen, Einzelheiten unten (A1-Notiz). Zusatz: Fussnote 3 (Mittel gegen Einzelstreuung) und Fussnote 7 (langsame Instabilitaet waere "irrelevant physically") | nein, aber Fussnote 7 traegt mehr als erwartet |

A1-Notiz [S, ASS 2014 = Aslanbeigi, Saravani, Sorkin, JHEP 06 (2014) 024, arXiv:1403.1622v1]:
- (3.7) mit Verweis auf Dominguez/Trione 1979: chi(p) = 2 (2 pi)^(D/2-1) (p.p)^((2-D)/4) int s^(D/2) e^(-rho C_D s^D)
  K_(D/2-1)(sqrt(p.p) s) ds. Fuer D = 4 genau die Formel des Code-Agenten (amu). Hauptzweig, Schnitt auf der negativen
  Achse; (3.10): zukunftsgerichtet = Z - i eps. **Damit ist Schritt B an der Quelle bestaetigt, Zweig wie in Schritt C.**
- (2.14): der b0-Term (Links) des 4D-BD-Operators ist dasselbe Integral wie Johnstons k~. Johnstons Linkkern ist also
  der Linkanteil des BD-Operators.
- S. 8, Abb. 3a: "g(4) does in fact have unstable modes"; Nullstelle bei Z = rho^(-1/2) p.p ~ 3,8 - 25,4 i, also
  |p| ~ 5 rho^(1/4). Meine Umrechnung (k = 0): omega ~ rho^(1/4) (3,3 + 3,85 i) [ES]. **UV-Regime, masselos.**
- (3.30): Stabil genau dann, wenn g~(Z) != 0 fuer alle Z != 0. (3.32): Wachstumsrate nach oben beschraenkt.
- S. 17: "we have not been able to find any choice that would make [the 4D operator] stable." Abschnitt 4: "Are any
  of the continuum-averaged GCB operators stable in 3+1 dimensions? We were not able to find any".
- S. 18: Ebene Wellen sind ein schwaches Kriterium; besser "late-time behavior of the Green function" pruefen. Genau das
  hat KAUSAL-WELLE-4D getan.
- Fussnote 7 (S. 18): Instabilitaet mit "very large (cosmological)" Wachstumszeit waere "irrelevant physically"; mit
  Planck-Zeit evtl. vertraeglich mit stabiler diskreter Entwicklung; "We were not able to find any such operator in 4D".
- Fussnote 3 (S. 2): Einzelstreuung gegen Mittel; Fluktuationen des ungeglaetteten B wachsen mit rho; "Which behavior
  is relevant physically?" Ausweg: Nichtlokalitaetsskala, so dass die Mittelung in jeder einzelnen Kausalmenge passiert.
- S. 9-10: GCB-Operatoren mit eigener Nichtlokalitaetsskala (Anhang D), Preis "a second, independent length scale".
- S. 6 (2D): rho^-1 g(2) = -Z f(Z), Im f = -(Im Z/2) x (positiv). Zukunftsgerichtet zeitartig: Im g > 0.
- Anhang A: In der IR-Entwicklung wird der Z ln Z-Term per b_n weggestellt; Z^2 ln Z (= p^4 ln p^2) bleibt frei.

A1-Folgerungen [ES]:
- **Zwei Regime (Regel 1).** BD/GCB in 4D: Instabilitaet an der Nichtlokalitaetsskala, auch masselos, Rate ~ 4 rho^(1/4).
  Johnstons Mittel: masselos stabil (k~ ohne Nenner, analytisch), massiv eine Polverschiebung an der Massenschale, Rate
  ~ m^3 l^2. Moderatoren: Masse und Bauart (geometrische Reihe im Linkkern gegen alternierende Schichtsumme).
- **Johnstons Mittel im ASS-Kriterium:** g_J = -1/k~ - m^2. Masselos keine Nullstelle (k~ endlich), also nach (3.30)
  stabil. Massiv: genau die Nullstelle aus Schritt C. Das ist der in Fussnote 7 gesuchte Typ "sehr lange Wachstumszeit",
  aber nur fuer leichte Felder; fuer schwere (Top, Higgs) Jahre, nicht kosmologisch.
- **Vorzeichen-Lesart:** Johnston, IR: rho^(-1/2) g_J = -Z + (sqrt 6/2 pi) Z^2 [ln Z + const] (ASS-Einheiten).
  Zukunftsgerichtet zeitartig: Im g_J = -(sqrt 6/2) |Z|^2 < 0. 2D-BD hat Im g > 0 (S. 6). Ich rechne fuer 2D-BD plus
  Masse eine Daempfung (Im omega < 0) statt Anwachsen. Johnstons Mittel hat also im Kontinuum eine negative
  Spektraldichte (sigma = -eps), geisterartig; daran haengt das Anwachsen. [ES, nur 2D-BD an der Quelle verglichen;
  Vorzeichen fuer 4D-BD aus Abb. 3b nicht sicher ablesbar.]

## 2b. Abhilfen am Schreibtisch (zwischen den Abrufen A1 und A3, vor 08:30) [ES]

- **Reelle Aenderung von a und b hilft nicht.** Mit a = lambda a0 und reellem b lautet die Polbedingung
  k0~(Z) = -1/M^2 mit reellem M^2. Erste Ordnung: Im Z^2 = -pi eps M^4 != 0 fuer jedes reelle M^2 > 0. Man kann
  die Masse (Re omega) richtigstellen, das Anwachsen nicht. Komplexes b macht den Kern komplex (reelles Feld verletzt).
  **Der erste Vorschlag in ERGEBNIS Abschnitt 8 ("a und b so waehlen, dass ... reell trifft") geht so nicht.**
- **Glaettung im Sinne Sorkins/ASS macht es schlimmer.** Die geglaettete Mittelung ersetzt rho durch die
  Nichtlokalitaetsdichte rho_k < rho (ASS S. 10: rho wird "non-locality-scale"). Fuer Johnstons Linkkern heisst das
  Im omega = (sqrt 6/4) m^4/(omega sqrt rho_k): Faktor (l_k/l)^2 schneller. Beispiel l_k = 1e-18 m statt l_P:
  Faktor ~4e33, Elektron-e-Faltung ~3e-10 s statt 1e24 s. **Glaettung und Stabilitaet des Mittels ziehen hier in
  entgegengesetzte Richtungen (zwei Regime: Rauschen will grosses l_k, Mittel will kleines).**
- **Was hilft (Kandidat): mehrschichtige Pfadsumme mit Summe der Sprungamplituden null.**
  - Spruenge entlang n-Element-Intervallen mit Amplituden a_n. Faktorisierung bleibt exakt (disjunkte Intervalle).
  - Koeffizient von ln Z^2 in k~_gen: (pi/(4c)) sum_n a_n, weil int tau^3 mu_n dtau = 1/(4c) fuer jedes n.
  - Normierung: sum_n a_n (pi/sqrt c) Gamma(n + 1/2)/n! = 1.
  - Links plus 1-Element-Intervalle: a0 = 2a, a1 = -2a (a = Johnstons Wert). Dann faellt der Imaginaerteil erster
    Ordnung weg; der naechste kommt aus Z^2 ln Z^2/c, also Im omega ~ m^6/(omega rho) mit noch unbekanntem Vorzeichen
    (Koeffizient ~ sum a_n Gamma(n + 3/2)/n! = -a sqrt(pi)/2 != 0).
  - Vergleich: Die 4D-BD-Koeffizienten (4, -36, 64, -32)/sqrt 6 haben ebenfalls Summe 0 (ASS (2.12), (3.14a) mit k = 1).
  - Preis [H]: wechselnde Vorzeichen bringen mehr Rauschen je Realisierung (Sorkin 2007: BD-Fluktuationen wachsen
    mit rho). Ob die Johnston-Variante self-averaging bleibt, ist offen. Neue Pole bei kleiner Dichte moeglich.
  - Ob das in der Literatur steht: nicht gefunden (noch nicht gesucht).
- **Schwerer-Skalar-Schranke [ES]:** Higgs als freier Skalar mit Johnstons Mittel bei l = l_P: e-Faltung 2,6 Jahre,
  ueber das Weltalter ~5e9 e-Faltungen. Vertraeglich nur fuer (l/l_P)^2 < 1/(5e9), also l < ~1,4e-5 l_P. Das ist eine
  eigene Konsistenzabschaetzung, keine Literaturschranke, und haengt an der Annahme "Mittel = wirksame Dynamik".

## 4. Erwartungsverstoesse (das eigentliche Ergebnis)

- V1 (zu E3, Surya 2019 lokal + ASS 2014, 24-Monats-Pruefung A6/A12 ohne Gegenbefund): Glaettung mit
  Nichtlokalitaetsskala macht die 4D-Operatoren **nicht** nachweislich stabil. ASS fanden keinen stabilen
  4D-GCB-Operator; Surya 2019 nennt es "open question". Erwartung E3 korrigiert: "Glaettung daempft Fluktuationen,
  Stabilitaet in 4D offen; fuer Johnstons Mittel verschlimmert sie das Anwachsen um (l_k/l)^2".
- V2 (zu E2, Regime): Die bekannte 4D-Instabilitaet ist eine andere als unsere: UV, masselos, Rate ~ 1/l_k. Unsere ist
  IR, nur massiv, Rate ~ m^3 l^2. E2 ist im Wortlaut eingetroffen, in der Sache aber nicht dieselbe Instabilitaet.
- V3 (nicht erwartet, A2 + A4): Johnstons Mittel und der BD-Operator sind exakt verknuepft: B~ = Z^4 k~ (Johnston 2010
  (A.62), 2014 (111); von mir gegen ASS (2.17) in zwei UV-Ordnungen geprueft). Folge: Der massive BD-Skalar
  (naiver Massenterm) zerfaellt mit derselben Rate, mit der Johnstons Mittel waechst. Gleicher p^4 ln p^2-Term,
  entgegengesetztes Vorzeichen.
- V4 (zu E3, A3): Die Literatur-Abhilfe fuer den Massenterm ist nicht Glaettung, sondern **die Masse ins Argument
  der nichtlokalen Funktion zu legen**, f(box + m^2) statt f(box) - m^2 (BBL 2015, Abschn. 3). Wie man das auf der
  Kausalmenge baut, nennen BBL ein offenes Problem. Fuer Johnstons Form waere das k~(Z^2 + m^2) statt k~/(1 + m^2 k~).
- V5 (zu E4, A4): Johnston 2014 hat die Korrekturen erster Ordnung schon gerechnet, exakt gleich meiner Schritt-C-
  Entwicklung, aber nur als formale Reihe (mit saekularem Term). E4 bleibt im Wortlaut eingetroffen; die Rechnung
  dahinter ist aber nicht neu, nur die Resummation und die Folgerung.

## 5. Offene Rueckfragen (wandern mit)

- ~~R1: Welches Regime hat die 4D-Instabilitaet der BD-/ASS-Operatoren?~~ Beantwortet (A1): UV, masselos, Nullstelle
  bei Z_A ~ 3,8 - 25,4 i.
- R2: Gibt es nach 2019 eine stabile 4D-Familie? Nach Recherchestand (A6, A12) nicht belegt; Abfrage unvollstaendig
  (G5). Bleibt offen.
- R3: Fuer Einzelrealisierung: Ist das Wachstum selbstmittelnd (gequencht gegen geglueht)? Teilantwort (E5-Zeile):
  kurzzeitig ja (G je Saat ~ G des Mittels; Varianz faellt laut Johnston). Ueber t ~ 1/Gamma offen.
- R4 (neu): Wie baut man "Masse im Argument" (BBL f(box + m^2)) als Pfadsumme auf der Kausalmenge? BBL Fussnote 10:
  offen. Kandidat Mehrschicht-Spruenge mit sum a_n = 0 (2b) ist nur eine Teilloesung.
- R5 (neu): Vorzeichen des Imaginaerteils des 4D-BD-Operators jenseits der IR-Entwicklung (BBL: Diskontinuitaet in 4D
  "not positive definite"). Fuer die Massenschale reicht die IR-Ordnung; fuer schwere Felder bei kleiner Dichte nicht.

## 6. Gestrichenes

- ~~"Glaettung kann stabil machen" als Abhilfe fuer das Anwachsen~~ (E3, gestrichen nach 2b und A1).
- ~~"a und b bei endlicher Dichte anpassen" als Abhilfe~~ (ERGEBNIS Abschn. 8, Vorschlag 1; gestrichen nach 2b: mit
  reellem a, b nicht moeglich).

## 6b. Unterscheidungspunkte (Regel 2)

- Anwachsen echt (Mittel = Physik) gegen Artefakt der Mittelung: trennbar nur bei t >~ 1/Gamma in einer einzelnen
  grossen Streuung. Bei rho ~ 1 bis 2 und m = 1 ist 1/Gamma ~ 2 bis 3; Laufstrecke ~10/m braucht ein 4D-Gebiet, das
  N >> 2e4 verlangt. Mit der heutigen Technik (N ~ 2e4) nur angedeutet: G je Saat ~ G des Mittels ueber 2/m.
- Johnston-IR-Instabilitaet gegen BD-UV-Instabilitaet: masselos (Johnston stabil, BD instabil) und Gang der Rate mit
  rho (Johnston ~ rho^(-1/2) -> 0, BD ~ rho^(1/4) -> unendlich). Am Schreibtisch trennbar, schon getrennt.
- Kontrollgroesse sigma = sum a_n (ln-Koeffizient): sigma > 0 Wachstum, sigma = 0 Rate ~ m^6/(omega rho), sigma < 0
  Zerfall. Trennbar in einer kleinen Rechnung (Rechenkarten-Vorschlag im DOSSIER).
- Glaettung hilft gegen Glaettung schadet: Rate ~ 1/sqrt(rho_k). Trennbar durch rho_k bei festem rho; im Mittel
  trivial (Formel), fuer das Rauschen nicht.

## 7. Gegensweep am Ende (Pflicht, mind. drei Punkte, einer geprueft)

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
- G1 (geprueft): "Planckdichte" = l_P^-4. Surya 2019 (lokal, Lambda-Abschnitt): "we have equated the discreteness scale
  lc with the Planck length lp". Arbeitsannahme, nicht Ergebnis. Mit reduzierter Plancklaenge (sqrt(8 pi) l_P)
  waechst die Rate um 25: Top ~2 Wochen, Higgs ~5 Wochen, Elektron ~1e5 Weltalter.
- G2 (geprueft): Zeitkonvention im Code. johnston_punkte nutzt exp(-i omega t) auf einer Linie ueber allen
  Singularitaeten; Im omega > 0 heisst Wachstum. Passt zu Schritt C.
- G3 (geprueft): Einzelsaat gegen Mittel im vorhandenen Lauf. ERGEBNIS Tab. 3.3: G je Saat (Median) 1,69 bis 2,09 gegen
  G des Mittels 1,63 bis 1,98. Kein Hinweis, dass Einzelnetze langsamer wachsen.
- G4 (geprueft, Methode): WebFetch-Zusammenfassungen. Bei A10 erfand der Zusammenfasser Pole, Daempfung und
  Wachstumsinstabilitaeten. Alle [S] dieses Feldes stammen aus lokal gelesenem Text (pdftotext auf stdout oder
  Seitenbild), ausser den Abstracts aus A7 (paraphrasiert, nur als Abstract-Inhalt verwendet) und A11 (woertlich).
- G5 (geprueft): Vollstaendigkeit der 24-Monats-Abfrage. A6 fand 1510.04656 und 1701.07212 nicht, obwohl beide
  einschlaegig sind. "Nach Recherchestand nicht belegt" gilt also mit Luecke.
- G6 (nicht geprueft): Ob der Higgs-Schluss traegt. Das Higgs ist selbstwechselwirkend; Vakuumstabilitaet ist eine
  QFT-Frage (SJ-Zustand, Wechselwirkung), nicht nur eine Frage des klassischen retardierten Propagators.
- G7 (nicht geprueft): Ob Johnstons Mittel auch fuer Fermionen-Analoga gilt; fuer 4D gibt es keinen Johnston-Dirac-Kern.

## 8. Abschluss

- DOSSIER.md geschrieben ab 08:45:17 CEST, gegengelesen (Zahlen, Seitenzahlen, Zitate) bis 2026-10-04 08:51:41 CEST (date).
- 12 von 15 WebFetch-Abrufen verbraucht (A5 Fehlschlag). Keine Rechnung auf der .69, lokal kein python, awk, perl.
