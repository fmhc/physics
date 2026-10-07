# STRING-1: Plan (Code-Agent fuer claude-primary, Runde 35)

- Karte: KARTE.md (unveraendert uebernommen: Vorhersagen S0 bis S6, Schwellen, Wahrscheinlichkeiten).
- Code-Agent, Arbeitsbeginn 21:02:53 CEST (date), Zeitbox 150 min (bis 23:32 CEST).
- Kennzeichen: [K] steht so in der Karte; [P] Festlegung dieses Plans, weil die Karte sie offenlaesst (vor dem Einfrieren
  festgelegt); [M] Mathematik; [L], [L?] Literatur aus dem Gedaechtnis; [H] Hypothese.
- Rechenort: .69, /home/fmh/fmhc-physics-remote/runde35-string/, nur Spur cpu6 ueber kleintest.sh, ein Lauf zugleich.

## 1. Modell und Messgroesse

- **Strommodell** [K]: d-dimensionaler Torus (Kantenlaenge L, periodisch), ganzzahliger Fluss n_e auf jeder Kante,
  Gewicht exp(-(K/2) sum_e n_e^2), K = J/T. Gauss-Gesetz: Divergenz (Abfluss minus Zufluss) = delta_M - delta_I.
  - Feste Ladungen: Quelle M (Wurmschwanz), Senke I (Wurmkopf). Das Vorzeichen ist durch die Symmetrie n -> -n
    unerheblich.
- **Messgroesse** [K]: F(r)/T = -ln[Z(r)/Z(0)], Z(0) = Summe ueber geschlossene Flusskonfigurationen.
- **Abstand** [P]: nur Verschiebungen auf den Gitterachsen, D = +-r e_mu, r = 0..L/2 auf dem Torus. Alle verschiedenen
  Achsenvektoren gleicher Laenge werden gemittelt: 2d Vektoren fuer 0 < r < L/2, d Vektoren fuer r = L/2.
  - Grund: Bei kurzer Korrelationslaenge haengt die Stringspannung von der Gitterrichtung ab. Euklidische Schalen
    wuerden verschiedene Richtungen mischen.
- **Winkelmodell (Gegenprobe)** [K]: Villain-XY mit K_V = 1/K und Gewicht je Kante
  V(phi) = sum_{m=-3}^{3} exp(-(K_V/2)(phi - 2 pi m)^2), phi = theta_y - theta_x auf [-pi, pi) reduziert.
  Gemessen wird G(r) = <cos(theta_x - theta_{x + r e_mu})>, gemittelt ueber alle x und mu.
  - **Dualitaet** [M]: Poisson-Summe je Kante, sum_n exp(-(K/2) n^2) e^{i n phi} ~ sum_m exp(-(phi - 2 pi m)^2/(2K)).
    Integration ueber die Winkel erzwingt das Gauss-Gesetz; die Einfuegung e^{i(theta_A - theta_B)} setzt die
    Ladungen. Also gilt G(r) = Z(r)/Z(0) exakt auf demselben Torus, Windungssektoren eingeschlossen.
  - **Abschnitt** [P]: m = -3..3. Groesster weggelassener Term relativ zum kleinsten Term m = 0 (bei phi = pi):
    2 exp(-(K_V/2)((7 pi)^2 - pi^2)) <= 2,8e-23 (K = 4,5, schlechtester Fall); fuer K = 0,5, 1,5, 2,5 noch kleiner.
    Numerisch gegen m = -12..12 auf 2001 Punkten in phi: Abweichung 0 in doppelter Genauigkeit (Pruefung, alle vier K).

## 2. Wurm (Strommodell) [P]

- Erweiterter Raum {(n, I, M)} mit Gewicht pi = exp(-(K/2) sum n^2) * w(I - M); w = Bias (siehe unten), sonst 1.
- **Zug A:** Richtung k aus 2d gleichverteilt (W. 1/2d). Der Kopf geht ueber die Kante nach I' = I + e_k; der Fluss in
  Laufrichtung f steigt um 1. Annahme min(1, exp(-(K/2)(2f + 1)) * w(D')/w(D)), D = I - M.
- **Detailliertes Gleichgewicht** [M]: Der Rueckzug waehlt von I' die Gegenrichtung (ebenfalls W. 1/2d). Er erhoeht den
  Fluss in seiner Laufrichtung um 1, setzt also n_e zurueck. Die Vorschlaege sind symmetrisch, also gilt mit der
  Metropolis-Annahme pi(a) P(a -> b) = pi(b) P(b -> a). Oeffnen (I = M -> I != M) und Schliessen sind derselbe Zug.
- **Zug B:** Ist nach Zug A I = M (geschlossen), wird die Lage x = I = M neu gleichverteilt gezogen. Alle V Lagen haben
  dasselbe Gewicht (gleiches n, gleiches w(0)). B ist ein Gibbs-Zug in der Lage und erhaelt pi. Die Kette A, B, A, ...
  erhaelt pi als Hintereinanderausfuehrung zweier pi-erhaltender Kerne.
- **Messung:** nach jedem Schritt Histogramm hist[D] += 1. Summiert ueber die Lage von M gilt
  hist[D]/w(D) ~ V Z(D), also G(r) = Z(r)/Z(0) = [sum_Achse hist/(n_vec w(r))] / [hist(0)/w(0)].
- **Bias** [P]: w(D) = exp(b |D|_max), |D|_max = Maximumsnorm des Torusabstands (auf der Achse = r).
  - Abseits der Achsen ist |D|_max kleiner als der Euklid-Abstand. Daher behalten die Achsen das groesste Nettogewicht,
    und der Wurm verliert sich nicht in den Diagonalen.
  - Der Bias aendert keine Erwartungswerte (wird exakt herausgerechnet), nur die Varianz.
  - Werte aus den Rauchlaeufen: b = 0,7 fuer d = 2, K = 2,5; b = 1,9 fuer d = 3, K = 4,5; b = 0 fuer K = 0,5 und 1,5.
- **Gauss-Pruefung (S0):** Vollpruefung der Divergenz an allen V Plaetzen nach dem Einlauf und nach jedem Block
  (Soll delta_M - delta_I). Gezaehlt wird jede abweichende Stelle; Soll 0.
- Zufallszahlen xoshiro256**, Startzustand aus numpy SeedSequence(seed); C-Kern string_kern.c, per ctypes geladen.

## 3. Winkelmodell [P]

- Metropolis je Platz der Reihe nach, theta' = theta + delta (2u - 1); kalter Start (alle theta = 0); Einlauf ohne
  Messung (1000 bis 3000 Durchgaenge), danach Messung nach jedem Durchgang.
- delta: 2,5 (d = 2, K = 2,5), 1,5 (d = 3, K = 1,5), 1,0 (d = 2, K = 0,5), pi (d = 3, K = 4,5).
- Kantenwerte ln V werden mitgefuehrt; je Zug 2d neue Kantenwerte.

## 4. d = 1 exakt [K]

- Offene Kette mit N = 400 Plaetzen, A = 150, B = 150 + r, r = 0..60. Gauss-Gesetz am Platz i: n_{i-1} - n_i = Q_i,
  n_{-1} = n_{N-1} = 0 (offene Enden).
- Ohne Paarbildung: Q_i = extern. Mit Paarbildung: Q_i = extern + q_i, q_i in {-1, 0, +1} mit Gewicht exp(-mu|q|/T).
  J = 1, T = 0,5, mu = 3, also K = 2, mu/T = 6.
- Uebertragungsmatrix ueber den Flusswert n in [-8, 8] mit Normierung je Schritt.
- **Kontrollen** [P]: Abschnitt n in [-16, 16]; Kette N = 600 mit A = 250; Abzaehlung aller Ladungsbelegungen fuer
  N = 6 (Pruefung: Abweichung 7,9e-16).

## 5. S6: Paarbildung in d = 3, per Wurm mit Ladungszuegen [P, wahlweise]

- **Herleitung des Felds** [M]: Mit dynamischen Ladungen q_x in {-1, 0, 1} (Gewicht z^|q|, z = exp(-mu/T)) gibt die
  Summe ueber q_x im dualen Modell je Platz sum_q z^|q| e^{-i q theta_x} = 1 + 2 z cos theta_x.
  - Das ist exakt. In erster Ordnung ist es exp(h cos theta) mit h = 2z = 2 exp(-mu/T); der Faktor 2 der Karte stimmt.
  - Der exakte Platzfaktor (1 + 2z cos theta) ist im Winkelmodell eingebaut (positiv fuer z < 1/2).
  - Pruefung: Ring d = 1, L = 8, K = 1, mu/T = 1. Villain mit Platzfaktor gegen exakte Uebertragungsmatrix mit
    Paarbildung (Spur): |z| <= 0,9 fuer r = 1..4. Faktor und Vorzeichen sind damit bestaetigt.
- **Warum nicht das Winkelmodell fuer S6** (nach Rauchlauf, offengelegt): Am Knick ist G ~ e^-10. Das Winkelmodell
  rauscht bei L = 24 in 4 min mit etwa 3e-5 je r, also etwa 40 % von G. Es loest den Knick nicht auf.
- **Wurm mit Ladungszuegen** (Karte erlaubt beides):
  - Zusaetzliche dynamische Ladungen q_x in {-1, 0, 1} mit Gewicht z^|q|; Gauss-Gesetz div n = q + delta_M - delta_I.
  - Zug C (mit W. 1/2 statt Zug A): Der Kopf springt nach I' (gleichverteilt), dabei q_I -> q_I - 1 und
    q_I' -> q_I' + 1, nur wenn danach |q| <= 1. Der Fluss bleibt unveraendert, das Gauss-Gesetz bleibt erfuellt.
  - Der Vorschlag ist symmetrisch, angenommen wird mit min(1, z^(Aenderung von sum|q|) w(D')/w(D)). Die Mischung
    pi-erhaltender Kerne erhaelt pi [M].
  - Pruefung (Rauchlauf, rauch/pruef_paare.json):
    - Ring d = 1, L = 8, K = 1, mu/T = 1 gegen die exakte Spur: |z| <= 0,93 ohne Bias, <= 0,79 mit Bias.
    - d = 2, L = 6, K = 1, mu/T = 1,5 gegen Villain mit Platzfaktor: |z| <= 1,6.
    - Gauss-Pruefung mit q: 0 Fehler.
  - Bias [P]: w(D) = exp(1,9 min(|D|_max, 6)): bis r = 6 flach, dahinter (Plateau) ungewichtet.
- **mu** [K/P]: Die Karte verlangt 2 mu/sigma(gemessen) ~ 6, also mu/T = 3/xi.
  - xi stammt aus dem String-Ausgleich (Abschnitt 7) des Rauchlaufs d = 3, L = 24, K = 4,5 (60 s, Bias 1,9):
    1/xi_rauch = 1,8910, also mu/T = 5,673 (z = 3,44e-3).
- Lauf: d = 3, L = 24, K = 4,5, mu/T = 5,673; F_h(r)/T auf der Achse fuer r = 0..12, 240 s, 50 Bloecke.

## 6. Gittergroessen, Statistik, Einlauf [P]

| Teil | d | K | L (klein / gross) | Bias b | Laeufe |
|---|---|---|---|---|---|
| Wurm | 2 | 0,5 und 2,5 | 64 / 128 | 0 / 0,7 | je ein Lauf |
| Wurm | 3 | 1,5 und 4,5 | 24 / 32 | 0 / 1,9 | je ein Lauf |
| Winkelmodell (S0) | 2 | 2,5 | 64 | | 1 |
| Winkelmodell (S0) | 3 | 1,5 | 24 | | 1 |
| Winkelmodell (nur berichtet) | 2 / 3 | 0,5 / 4,5 | 64 / 24 | | je 1, wenn Zeit bleibt |
| S6 (Wurm mit Paaren) | 3 | 4,5 | 24 | 1,9, Kappe 6 | 1 |
| d = 1 exakt | 1 | 2 | N = 400 | | 1 |

- Jeder Monte-Carlo-Lauf hat 240 s Rechenzeit. Davon gehen 10 % (mindestens 2e6 Schritte) in den Einlauf, ohne Messung.
  Dann folgen 50 gleich grosse Bloecke; die Blockgroesse ergibt sich aus dem im Einlauf gemessenen Tempo.
- Wurm etwa 4e7 Schritte/s, also etwa 9e9 Schritte je Lauf.
- Reihenfolge: d = 1, Gauss-Referenz, Wurm 2D (gross, klein), Wurm 3D, Winkelmodell S0, Zwischenauswertung, S6,
  Winkelmodell-Zusaetze, Endauswertung (code/laeufe.sh). Gesamt etwa 60 min.
- Startzahlen (seeds) 1001 bis 1013 fest im Skript.

## 7. Auswertung (code/auswertung.py, mechanisch)

- **Fehler** [P]:
  - Wurm: Jackknife ueber die 50 Bloecke (Weglassen eines Blocks, Verhaeltnis der Summen).
  - Winkelmodell: Standardfehler der 50 Blockmittel.
- **Daten fuer die Ausgleiche** [P]: y(r) = -ln(sum_b S_b(r)), S_b(r) = Achsenzaehler/(n_vec w(r)).
  - Es gilt y(r) = F/T(r) + const. Die Normierung durch Z(0) verschiebt nur die Konstante c. Ihre Schwankung gehoert
    nicht in die Formfehler.
  - Fehler sigma_y(r) per Jackknife; c wird danach auf F/T umgerechnet (c - y(0)).
- **Fenster** [P]: Achsenabstaende r = 2, 3, ..., L/4 (ganzzahlig).
  - d = 2: L = 128 gibt 31 Punkte, L = 64 gibt 15.
  - d = 3: L = 32 gibt 7 Punkte, L = 24 gibt 5.
  - Voraussetzung je Punkt: mindestens 1000 Achsenzaehler und keine leere Jackknife-Stichprobe. Fehlt das an einem
    Punkt des Fensters, ist der Fall "nicht auswertbar".
- **Ausgleichsformen** (gewichtete lineare kleinste Quadrate mit 1/sigma_y^2):
  - String r/xi + a ln r + c (k = 3) [K]
  - Logarithmus eta ln r + c (k = 2) [K]
  - Coulomb c - C/r (k = 2) [K]
  - linear sigma r + c (k = 2) [P, fuer S4]
  - Parameterfehler: Jackknife (Ausgleich je Weglass-Stichprobe mit denselben Gewichten).
- **"besser"** [P]: kleineres AIC = chi^2 + 2k, chi^2 mit den Diagonalfehlern sigma_y (unkorrelierter Ausgleich).
- **"jeder lineare Ausgleich" (S4)** [P]: die beiden Formen mit linearem Term, sigma r + c und r/xi + a ln r + c.
- **"F/T saettigt" (S4)** [P]: Q_sat = [F/T(L/2) - F/T(L/4)] / [F/T(L/4) - F/T(1)] < 0,2 (normierte Werte auf der
  Achse).
  - Schreibtisch: Coulomb mit Torus etwa 2/(L - 4) oder weniger, also unter 0,1; Logarithmus etwa 0,4 bis 0,7;
    linear etwa 1,1.
- **Uebereinstimmung Wurm gegen Winkelmodell (S0)** [P]:
  - z(r) = (G_W - G_V)/sqrt(sigma_W^2 + sigma_V^2) fuer r = 1..L/4 auf demselben L.
  - "stimmt" heisst |z| <= 3 fuer jedes dieser r ("innerhalb 3 sigma", wortgetreu).
  - Bei 16 (d = 2) bzw. 6 (d = 3) Vergleichen ist ein zufaelliges Verfehlen mit wenigen Prozent moeglich; das nehme
    ich in Kauf.
- **r_c (S5)** [P]: Schnitt des linearen Asts mit dem Plateau.
  - Ast: Gerade nach kleinsten Quadraten durch F/T_mit(r), r = 1..6.
  - Plateau: P = F/T_mit(60).
  - r_c = (P - c_Ast)/Steigung_Ast.
- **r_c (S6)** [P]: Schnitt der String-Kurve ohne Paare mit dem Plateau.
  - String-Kurve: Ausgleich r/xi + a ln r + c des Wurms ohne Paare, d = 3, K = 4,5, L = 24 (Hauptlauf).
  - Plateau: P = Mittel von F_h/T (Wurm mit Paaren, normiert mit Z_h(0)) ueber r = 9..12.
  - r_c = kleinstes r in [1; 40] (Gitter 0,001), an dem die String-Kurve P erreicht.
  - Vorhersage nach Karte: r_c,pred = 2 mu/sigma = 2 (mu/T) xi, xi aus demselben Hauptlauf.
  - Plateau-Vorhersage [H, Schreibtisch]: P_pred = 2 mu/T - 2 ln chi_1 mit chi_1 = sum_x Z(x)/Z(0) desselben Wurms
    (Lagenentropie: Die Paarladung sitzt mit Gewicht ~ G(x) irgendwo um A bzw. B).

### Urteilsregeln (Schwellen aus der Karte, unveraendert)

- **Gittergroesse** [P]: S1 bis S4 urteilt das groessere L (d = 2: 128, d = 3: 32). Gibt das kleinere L ein anderes
  Urteil, steht im Urteil der Vermerk "nicht konvergiert"; das Urteil bleibt beim groesseren L.
- **S0 eingetroffen**, wenn alle drei Teile gelten:
  - (a) Die Gauss-Pruefung meldet in allen 8 Wurm-Hauptlaeufen 0 Fehler.
  - (b) d = 1 ohne Paare: max_r |F/T(r) - (K/2) r| <= 1e-9 fuer r = 0..60; die Kontrollen (N = 600, n in [-16, 16])
    weichen um hoechstens 1e-9 ab.
  - (c) Wurm und Winkelmodell stimmen in d = 2 (K = 2,5, L = 64) und in d = 3 (K = 1,5, L = 24) nach obigem Mass.
  - Fehlt ein Teil, ist S0 "nicht auswertbar".
- **S1** (d = 2, K = 2,5): AIC(String) < AIC(Log) und a in [0,25; 0,75].
- **S2** (d = 2, K = 0,5): eta (Log-Ausgleich) in [0,068; 0,092].
- **S3** (d = 3, K = 4,5): AIC(String) < AIC(Coulomb) und a in [0,6; 1,4].
- **S4** (d = 3, K = 1,5): Q_sat < 0,2 und AIC(Coulomb) < AIC(linear) und AIC(Coulomb) < AIC(String) und
  C in [0,10; 0,36].
- **S5** (d = 1 exakt): r_c in [10; 13].
- **S6** (wahlweise, L = 24): eingetroffen, wenn alle drei Bedingungen gelten:
  - Saettigung: F_h/T(12) - F_h/T(9) < 0,3/xi
  - r_c in [0,7; 1,3] * r_c,pred (Karte: +-30 %)
  - |P - P_pred| <= 0,3 P_pred ("~" der Karte als +-30 % gelesen [P])
  - Nicht gerechnet heisst "nicht auswertbar" mit Vermerk.
- Die Punktschaetzung entscheidet, Fehler werden berichtet.

## 8. Rauchlaeufe (vor dem Einfrieren, offengelegt)

- Alle in rauch-69/ (lokal) bzw. rauch/ (.69), Spur cpu6, 19:19 bis 19:33 UTC. Seeds 11 bis 24 und 101 bis 301,
  verschieden von den Hauptlaeufen.
- **Pruefungen** (pruef, pruef2, pruef3, pruef_paare; alle bestanden):
  - Wurm d = 1, Ring L = 8, K = 1 gegen die exakte Formel (Windungssumme): z = -1,2 bis -1,4 an allen r. Das ist eine
    gemeinsame Verschiebung durch die Normierung, innerhalb 3 sigma.
  - Wurm d = 2, L = 6, K = 1: mit Bias gegen ohne |z| <= 1,3 (Euklid-Bias) bzw. 0,64 (Maximumsnorm); gegen Villain
    |z| <= 0,61.
  - Uebertragungsmatrix gegen Abzaehlung: 7,9e-16.
  - Villain mit Platzfaktor gegen exakte Paarbildung (Ring): |z| <= 0,88.
  - Villain-Abschnitt m = -3..3 gegen -12..12: 0.
  - Gauss-Pruefung: 0 Fehler in allen Laeufen.
- **Kleine Gitter ohne Bias, 30 s** (L = 32 bzw. 16):
  - Tempo etwa 4e7 Wurmschritte/s. Die Bilder F/T(r) entsprechen den Regimen der Karte: d = 2, K = 2,5 linear
    (Zuwachs etwa 0,72 je Schritt); d = 3, K = 4,5 linear (etwa 2,0 je Schritt); d = 2, K = 0,5 flach logarithmisch;
    d = 3, K = 1,5 saettigend.
  - F/T(1) = 0,125 (d = 2, K = 0,5) und 0,251 (d = 3, K = 1,5); Spinwellen-Wert K/(2d): 0,125 und 0,25.
  - Villain d = 2, L = 32, K = 2,5 und d = 3, L = 16, K = 1,5 stimmen mit dem Wurm (|z| <= 1,35).
- **Bias-Probe auf echten Groessen, 60 s** (offengelegt, weil es Hauptgroessen sind; andere Seeds, kuerzer):
  - d = 2, L = 64, K = 2,5, b = 0,7: Achsenzaehler je r 4,5e6 bis 1,3e7 (flach). String-Ausgleich auf [2; 16]:
    1/xi = 0,680, a = 0,490 +- 0,004, chi^2 = 4,6 bei 12 Freiheitsgraden; AIC(Log) etwa 2e6.
  - d = 3, L = 24, K = 4,5, b = 1,9: Achsenzaehler je r 1,2e7 bis 3e7. String-Ausgleich auf [2; 6]: 1/xi = 1,891,
    a = 0,547 +- 0,005, chi^2 = 87 bei 2 Freiheitsgraden. Die String-Form beschreibt dieses kurze Fenster schlecht:
    Die lokale Kruemmung waechst mit r (Uebergang vom steifen zum zitternden String).
    Auf diesem L laege a unter der Schwelle 0,6 von S3.
  - d = 3, L = 24, K = 1,5, b = 0: Fehler sigma_y etwa 0,0025. Coulomb C = 0,138 +- 0,011, AIC Coulomb 4,7 gegen
    String 7,2 gegen linear 25,1; Q_sat = 0,078.
  - d = 2, L = 32, K = 0,5 (30 s): eta = 0,0732 +- 0,0015.
  - Probe-Auswertung (rauch/auswertung.json) mit "gross" = 64 bzw. 24: S1 eingetroffen, S3 nicht eingetroffen,
    S4 eingetroffen; S2 auf L = 32 im Intervall. Die urteilenden Groessen 128 und 32 liefen nicht im Rauchlauf.
  - Wurm mit Paaren, d = 3, L = 24, mu/T = 5,673 (60 s):
    - F_h/T = 0; 2,20; 4,37; 6,45; 8,20; 9,33; 9,61; 9,65; 9,66 ... 9,67 (r = 0..12), also ein Plateau ab r ~ 6.
    - P_pred = 2 * 5,673 - 2 ln 2,320 = 9,66.
    - Mit der Rauch-String-Kurve liegt r_c bei etwa 4,6; r_c,pred = 6,0. Das Verhaeltnis 0,76 liegt knapp im
      Fenster [0,7; 1,3].
- **Was ich nach den Rauchlaeufen geaendert habe** (vor dem Einfrieren):
  - Bias-Norm von Euklid auf Maximumsnorm, aus Effizienzgruenden. Sie aendert keinen Erwartungswert; die Pruefung
    wurde wiederholt.
  - S6 vom Winkelmodell auf den Wurm mit Ladungszuegen umgestellt, wegen der Aufloesung (Abschnitt 5).
  - mu/T fuer S6 aus dem Rauchlauf gesetzt.
  - Die Fenster, Formen, AIC und Urteilsregeln standen im Entwurf dieses Plans, bevor ich die Bias-Proben auf L = 64
    und 24 gelesen hatte (Entwurf 21:26 CEST, Ausgaben gelesen 21:27 bis 21:33). Die Kleingitter-Rauchlaeufe
    (L = 32, 16) hatte ich vorher gesehen.
  - Keine Schwelle der Karte geaendert.

## 9. Vorab ableitbar [M]

- **S5** ist praktisch ableitbar. Handrechnung: Bruch kostet 2 mu/T = 12. Die Paarlage hat je Seite die Entropie
  ln sum_j e^-j = ln 1,582, zusammen 0,917. Das Plateau liegt also bei F/T ~ 11,08, die Gerade ohne Paare ist
  F/T = r, also r_c ~ 11,1. Das Intervall [10; 13] der Karte enthaelt das sicher; die Rechnung prueft vor allem den
  Code.
- **S0 (b)** ist trivial (offene Kette ohne Paare: genau ein Flusszustand).
- **S2** folgt fast aus der Gauss-Referenz (Spinwellen ohne Wirbel auf demselben Torus und Fenster):
  eta_Gauss = 0,0767 (L = 64) und 0,0771 (L = 128). Wirbel sind bei K_V = 2 mit etwa e^(-pi^2 K_V) ~ 3e-9 je Platz
  unterdrueckt [L?].
- **S4**: Gauss-Referenz C = 0,131 (L = 24) und 0,130 (L = 32); Q_sat = 0,066 bzw. 0,046. Wirbelschleifen machen C
  groesser [L?]; der Formvergleich gegen die String-Form ist dagegen nicht vorab entschieden.
- **S1, S3, S6**: Der Exponent a im endlichen Fenster ist nicht vorab ableitbar. Die Rauchlaeufe auf L = 64 bzw. 24
  geben Hinweise (Abschnitt 8); die urteilenden L = 128 bzw. 32 sind offen.

## 10. Einfrieren

- Kopie PLAN.md.eingefroren-<Zeit> (Zeit per date) und code/*.eingefroren-<Zeit>; sha256 in Abschnitt 11 der
  eingefrorenen Kopie bzw. in ERGEBNIS.md. Danach Plan und Urteilsregeln unveraendert; Code nur bei echten Fehlern,
  offengelegt.
