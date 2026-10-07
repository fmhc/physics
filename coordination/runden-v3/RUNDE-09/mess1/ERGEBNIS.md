# MESS-1 "Troepfchen-Bruecke" (Runde 9): Ergebnis

- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung claude-primary (Finn 07:53: "überlege noch mal wo wir in
  bestehenden experimenten sowas aus rechnungen nachweisen können"). Explorativ (v3). Literatur und Rechnung in einer Hand.
- Beginn 2026-09-30 07:51:27 CEST (date). PLAN.md mit Vorab-Erwartung ab 07:58:41 (date), vor jedem Abruf und jeder
  Rechnung. Diese Datei begonnen 2026-09-30 08:27:07 CEST (date); Ende: letzte Zeile.
- Code: mess1.py (numpy). Laeufe auf der .69 ueber kleintest.sh (Spuren cpu, cpu2), Ausgaben lauf-69/; lokale Rauchtests
  in lauf-lokal/. Code-Staende (SHA-256, erste 16 Zeichen): 62dcfcefa1bb0aed (prof1, geb0, w0a), 21e9964b63546887
  (pol0a), 548f1d6171b50966 (qb01, w0b, w2a, pol0b, geb2 und alle lokalen Rauchtests ab 08:21:59; Endstand).
- Markierungen: **[H]** Hypothese; **[L?]** aus dem Gedaechtnis, nicht an der Quelle geprueft; **[Abs]** nur
  arXiv-Zusammenfassung gelesen; ohne Marke: an der Quelle gelesen (PDF-Text). Modell ist keine Messung.

## 0. Ergebnis zuerst

1. **Stellen: nein.** Im Troepfchen (erweiterte GP-Gleichung, symmetrische Mischung, 3D, l = 0) hat die Abstrahlungsbreite
   keine Nullstelle, weder fuer die Grundatmung noch fuer die Oberschwingungen; auch l = 2 nicht (eine Gitterstufe).
   - Gerechnet fuer N~ = 20,2 bis 7535 (mu = -0,105 bis -0,46) und eps bis 2,0 (in Einheiten von Petrov).
   - Methode: Nullstellenabbildung W wie bic2, zwei Gitterstufen (h = 0,02 und 0,01), 72 bis 75 Profile mal 151 bis 191
     Energien. Keine Zelle, in der beide Komponenten das Vorzeichen wechseln; die Nullkonturen der beiden Komponenten
     liegen in getrennten mu-Bereichen.
   - Positivkontrolle bestanden: Dieselbe portierte W-Maschine findet die bekannte Q-Ball-Nullstelle (omega*^2 =
     0,797677, rho* = 1,7446) mit Umlauf +1 und gibt im Nachbarkasten Umlauf 0 (beide Gitterstufen).
2. **Die Atmung ist im Selbstverdampfungsfenster gar keine schmale Resonanz.**
   - Sie liegt fuer 20,1 < N~ < ~950 ueber der Schwelle -mu (Petrov 2015: 20,1; Ferioli u. a., arXiv 1912.09594: 934; hier 20,1 und
     ~953).
   - Pole nur am oberen Rand: N~ = 432 / 561 / 647 / 752 mit Gamma/Re eps = 0,41 / 0,29 / 0,22 / 0,12 (Guete 1 bis 4).
     Darunter (N~ <= 341) kein Pol mit Gamma < 0,4: die Mode ist im Kontinuum aufgeloest.
   - Beim Q-Ball war die Atmungsresonanz schmal (Gamma ~ 4e-3 bis 5e-3 bei rho ~ 1,7 zwischen den Stellen), weil ein
     Zustand des geschlossenen Kanals in der Wand gefangen war. **Genau dieser Wandtopf fehlt dem Troepfchen**
     (Abschnitt 4): Der geschlossene Kanal liegt um mindestens 2|mu| ~ 1 tief, der Topf in der Wand ist nur 0,82 tief.
     Die Vorab-Vorhersage E-R4 ist getroffen.
3. **Messbezug:** Fuer bestehende 39K-Experimente gibt es keine Einbruchs-Vorhersage bei N_n, weil es die Stellen im
   Modell nicht gibt.
   - Pruefbar bleibt nur das glatte Bild: Die Atmung ist zwischen N~ = 20,1 und ~950 stark gedaempft (Guete <= 4), ausserhalb
     linear ungedaempft (gebunden).
   - In Laborgroessen (39K, delta a = -3,2 a0, grob): N~ = 934 entspricht ~5,6e6 Atomen, tau = 2,5 ms, Atmung ~26 Hz,
     Abklingzeit ~20 ms bei N~ ~ 560. Heutige 39K-Troepfchen (N~ zwischen N~_c = 18,65 und grob 200) liegen tief im Bereich ohne
     Pol; Semeghini u. a. 2018 sahen dort passend "keine Oszillation" (Abschnitt 7).
4. **Folgerung fuer die Bruecke [H]:** Ein Laborsystem fuer unsere Leiter braucht einen schmalen, an eine Wand gebundenen
   Zustand eines geschlossenen Kanals, nicht nur ein flaches Profil mit duenner Wand. (Oberflaechenmoden l = 2 siehe
   Abschnitt 5.)

## 1. Kontrollen

| Groesse | hier (h = 0,02, Profilschritt 0,01) | Quelle | Stand |
|---|---|---|---|
| N~_c (Minimum von N~(mu)) | 18,6497 bei mu = -0,0614 (Parabel durch -0,055/-0,060/-0,065) | Petrov 2015: 18,65; mu_c "0.061" (Vorzeichen im PDF-Text verloren, muss negativ sein) | getroffen |
| N~'' = d^2 N~/d mu^2 bei mu_c | ~2290 (zweite Differenz, Schritt 0,005) | Petrov: 2190 | 4 % daneben, Differenzenschritt grob |
| Energie null (E~ = 0) | N~ = 22,56 (linear zwischen mu = -0,12 und -0,14) | Petrov: 22,55 | getroffen |
| Atmung tritt unter die Schwelle (unterer Rand) | zwischen N~ = 19,92 (gebunden, eps = 0,09982 < 0,1) und 20,24 (nicht gebunden) | Petrov: 20,1 | getroffen |
| Atmung tritt unter die Schwelle (oberer Rand) | geb0 (.69): zwischen N~ = 881 (nicht gebunden) und 1044 (gebunden, 0,41758 < 0,42). Rauchtest geb0-rand (lokal): 942 nicht gebunden, 958 gebunden (Bindung 7,8e-6), 975 (1,6e-4), 1009 (1,0e-3); sqrt(Bindung) linear hochgerechnet: N~_2 ~ 953; h = 0,01 ziffergleich | Ferioli u. a. 2020: 934 (Fits bis 940) | 2 % daneben |
| Erste Mode l = 2 unter der Schwelle | geb2 (.69): 91,34 nicht gebunden, 94,35 gebunden (Bindung 0,00148), 97,51 (0,00741), 100,83 (0,01352); linear: N~_th ~ 93,6 | Petrov, Hu und Liu 2020: 94,2 | 0,7 % daneben |
| Grosse Tropfen: Atmung ~ pi c/R | mu = -0,45 (N~ = 3962, R_halb = 9,55): eps_0 = 0,299, Handformel 2,72/9,55 = 0,285 | eigene Handrechnung (PLAN.md) | 5 % |
| Q-Ball-Positivkontrolle (W-Umlauf) | +1 in der Zelle omega^2 0,7976..0,7980, rho 1,744..1,745 (h = 0,02 und 0,01); Nachbarkasten 0,7996..0,8008: 0 | THEORIE-ATMUNGS-NULLSTELLEN.md, Tab. 2.2 | bestanden |
| Q-Ball-Pol an der Stelle | rho = 1,74461755 - 2e-16 i; f(0) = 1,0242355039 | BEWEIS-1: f(0) = 1,02423550657 | 3e-9 |
| Zwei Gitterstufen W (l = 0) | h = 0,02 (w0a) und 0,01 (w0b): beide ohne Kandidatenzelle, gleiche Konturlage | - | stabil |

- Grenze der Profile: Das Schiessen in doppelter Genauigkeit traegt bis mu = -0,46 (N~ = 7500, Anschluss bei f/f0 =
  7,8e-3). Bei mu = -0,47 und -0,48 laufen die Klammern schon auf dem Plateau auseinander (prof1: Anschluss bei 0,98 und
  1,0); diese Zeilen (auch geb0 bei -0,48 und w0a bei -0,465 bis -0,475) sind **ungueltig** und nicht verwendet.
- Einheitenformeln (Petrov Gl. 7 und 9): Mit Petrovs n1 = 3,3e14 cm^-3 gibt mess1.py xi = 1,92 um und tau = 2,26 ms
  (Petrov: 1,96 um, 2,4 ms) und N2 = 1,1e5 bei N~ = 30 (Petrov: 1,1e5). Aus Gl. 7 mit a11 = 84,3, a22 = 33,5 a0 folgt
  aber n1 = 2,4e14 (Petrov 3,3e14): Petrov hat offenbar die Streulaengen bei B0 - 250 mG benutzt, ich die bei B0.
  Umrechnungen in Abschnitt 7 sind deshalb auf etwa 30 % genau.

## 2. Schwellenlage und Breite der Atmung gegen N~

Gebundene l = 0-Moden (geb0; Nullstellen von D unter der Schwelle) und Resonanzpole (pol0a, pol0b; eps = Re - i Gamma,
Gamma = Amplitudenrate; Guete Q = Re eps / (2 Gamma)):

| mu | N~ | Schwelle -mu | Grundatmung | weitere l = 0-Moden |
|---|---|---|---|---|
| -0,070 | 18,73 | 0,070 | gebunden 0,0468 (weich, nahe N~_c) | |
| -0,100 | 19,92 | 0,100 | gebunden 0,09982 | |
| -0,105 bis -0,38 | 20,2 bis 341 | 0,105 bis 0,38 | **kein Pol mit Gamma < 0,4** im Fenster Re eps in (-mu - 0,1, -mu + 1,1) | |
| -0,390 | 432 | 0,390 | 0,4565 - 0,1894 i | |
| -0,400 | 561 | 0,400 | 0,4237 - 0,1241 i | |
| -0,405 | 647 | 0,405 | 0,4057 - 0,0895 i | |
| -0,410 | 752 | 0,410 | 0,3866 - 0,0476 i (Re unter der Schwelle, zweites Blatt) | 1,0784 - 0,4424 i |
| -0,415 | 881 | 0,415 | kein Pol gefunden (Uebergang) | 1,0167 - 0,3821 i |
| -0,420 | 1044 | 0,420 | gebunden 0,41758 | |
| -0,440 | 2353 | 0,440 | gebunden 0,3514 | |
| -0,450 | 3962 | 0,450 | gebunden 0,2989 (Rauchtest rauch1, lokal) | 0,5655 - 0,0751 i (Rauchtest pole-rauch2, lokal; pol0b s. u.) |
| -0,460 | 7535 | 0,460 | gebunden 0,2410 | gebunden 0,4583 (n_r = 1, knapp unter der Schwelle) |

- Die Breite der Grundatmung faellt zum oberen Rand monoton (0,19 -> 0,05) und geht dort nicht wie bei einer
  s-Wellen-Schwelle glatt gegen 0 ueber der Schwelle: Der Pol wandert unter die Schwelle aufs zweite Blatt (N~ = 752)
  und wird dann gebunden. Kein Minimum, kein Einbruch.
- **Oberschwingungen im duennwandigen Bereich** (pol0b, .69, eingetragen 2026-09-30 08:36 CEST; eps = Re - i Gamma):

| mu | N~ | n_r = 1 | n_r = 2 | n_r = 3 |
|---|---|---|---|---|
| -0,420 | 1044 | 0,9536 - 0,3261 i | | |
| -0,425 | 1252 | 0,8895 - 0,2744 i | | |
| -0,430 | 1520 | 0,8247 - 0,2269 i | 1,4190 - 0,4708 i | |
| -0,435 | 1875 | 0,7596 - 0,1835 i | 1,3000 - 0,3873 i | |
| -0,440 | 2353 | 0,6945 - 0,1441 i | 1,1818 - 0,3130 i | |
| -0,445 | 3016 | 0,6297 - 0,1081 i | 1,0652 - 0,2474 i | 1,5706 - 0,4158 i |
| -0,450 | 3962 | 0,5655 - 0,0751 i | 0,9507 - 0,1902 i | 1,3921 - 0,3215 i |
| -0,455 | 5363 | 0,5023 - 0,0428 i | 0,8389 - 0,1407 i | 1,2193 - 0,2412 i |
| -0,460 | 7535 | gebunden 0,4583 (geb0) | 0,7302 - 0,0984 i | 1,0532 - 0,1742 i |

  - Jede Oberschwingung wird mit N~ gleichmaessig schmaler (Gamma/Re eps von 0,34 auf 0,085 fuer n_r = 1) und tritt
    dann unter die Schwelle. Kein Minimum, kein Vorzeichenwechsel: Das ist ein undichter Hohlraum (Schallwelle im
    Tropfen, die an der Oberflaeche in freie Atome uebergeht), keine Feshbach-Resonanz.
  - Bei N~ = 7535 zusaetzlich n_r = 4 und 5: 1,4174 - 0,2624 i und 1,8292 - 0,3673 i.
- Gitterstufe der Pole (Rauchtest pole-h01-rauch, lokal, h = 0,01): mu = -0,40: 0,42374143 - 0,1241 i; mu = -0,45:
  0,56554963 - 0,07505 i, ziffergleich mit h = 0,02. Der dafuer vorgesehene .69-Lauf pol0h01 wartete ueber 6 min auf die
  Spur cpu2 und wurde von mir abgebrochen, bevor er startete (Vermerk in seinem Log).

## 3. Nullstellenabbildung W: keine gebundenen Zustaende im Kontinuum

- W(eps, mu) = Omega(b1, j1) + i Omega(b2, j1) bei reellem eps; b1, b2 fortlaufend orthonormierte regulaere Loesungen
  (Basiswechsel mit positiver Diagonale, Umlaufsinn bleibt), j1 die im Kanal v abklingende Loesung von aussen. W = 0 <=>
  gebundener Zustand im Kontinuum (Satz aus bic2/PLAN.md). Imaginaere Reste: 0,0 (alle Groessen reell, wie es sein muss).
- w0a: 75 mu (-0,105 .. -0,475) x 151 eps (0,1 .. 1,6), h = 0,02. w0b: 72 mu (-0,105 .. -0,46) x 191 eps (0,1 .. 2,0),
  h = 0,01. **Beide: keine Kandidatenzelle** (Vorzeichenwechsel in beiden Komponenten) oberhalb der Schwelle.
- Lage der Nullkonturen (w0b, nur eps > -mu):
  - Re W = 0: nur fuer mu = -0,13 .. -0,21; die Kontur laeuft von (eps 1,72; mu -0,13) zur Schwelle bei (0,21; -0,21).
  - Im W = 0: fuer mu = -0,105 .. -0,125 knapp ueber der Schwelle (eps 0,14 bis 0,15) und fuer mu <= -0,30 (1 bis 4
    Konturen, von eps 1,87 bei mu = -0,30 abwaerts).
  - Die Konturen beruehren sich nirgends; das Ergebnis ist deshalb nicht an der Rasterweite haengen geblieben.
- Belegstufe: "nicht gesehen" im abgeschnittenen radialen linearen Modell, zwei Gitterstufen, Positivkontrolle bestanden.
- Abweichung vom Plan: Statt "kurve" (Vorzeichen der auslaufenden Amplitude entlang eines Resonanzasts) habe ich das volle
  W-Gitter gerechnet. Es gibt im Fenster keinen schmalen Ast, dem man folgen koennte (Abschnitt 2), und das Gitter
  erfasst jede Nullstelle unabhaengig von einem Ast.

## 4. Warum nicht: der fehlende Wandtopf (Vorab E-R4, getroffen)

- BdG fuer l = 0 hat dieselbe Form wie beim Q-Ball: U'' = 2 (D - eps) U + 2 C V, V'' = 2 C U + 2 (D + eps) V.
  Offen ist u fuer eps > -mu, v ist immer geschlossen.
- Beim Q-Ball sass ein Zustand des geschlossenen Kanals in der Wand (dp_min < (omega - rho)^2 < dp(S0)) und leckte nur
  schwach in den offenen Kanal. Das gab eine schmale Resonanz, und deren Kopplung wechselte mit der Phase der Innenwelle
  das Vorzeichen (Phasenregel).
- Beim Troepfchen ist der Kanal v an der Stelle n = 0,41 am tiefsten: D_min = -0,8192 - mu (Hand).
  - Erlaubt waere er nur bei D + eps < 0. Mit eps > -mu folgt D_min + eps > -0,8192 - 2 mu.
  - Fuer den flachen Grenzfall (mu -> -1/2) ist das +0,18 > 0: Der Kanal v ist ueberall verboten, einen Wandzustand gibt
    es nicht.
  - Ein Topf ist nur fuer mu > -0,41 und eps < -0,8192 - mu moeglich (kleine Tropfen, knapp ueber der Schwelle). Auch dort
    zeigt W keine Nullstelle.
- Folge: keine schmale Resonanz (die Pole haben Guete 1 bis 4) und keine Stelle. Das Stufenmodell (scharfe Oberflaeche,
  PLAN.md) gibt ebenfalls keine BIC.
- **[H] Uebertrag:** Die Leiter ist keine Eigenschaft "duenne Wand plus flaches Inneres" allein. Sie braucht einen
  gebundenen Zustand eines geschlossenen Kanals nahe der Wand, dessen Energie ueber dem Wandtopf und unter dem Inneren
  liegt. Das ist die Pruefliste fuer jedes Laborsystem.

## 5. Oberflaechenmoden l = 2 (Nachtrag, eingetragen 2026-09-30 08:30 CEST)

- Schwelle (lokaler Rauchtest geb2-rauch, h = 0,02): N~ = 88,47 kein gebundener l = 2-Zustand; 94,35 gebunden bei 0,30352
  (Schwelle 0,305); 100,83 gebunden bei 0,29648. Linear hochgerechnet tritt die Mode bei N~ ~ 93,6 unter die Schwelle
  (Petrov, Hu und Liu: 94,2; 0,7 % daneben). Die l = 2-Rechenwege (Fliehkraftterm, Reihenstart r^3, Hankel mit nu = 3)
  sind damit gegen die Literatur geprueft. Der .69-Lauf geb2 (91,34 nicht gebunden; 94,35 / 97,51 / 100,83 gebunden) gibt
  dasselbe: N~_th ~ 93,6.
- W-Gitter l = 2 (w2a, .69, h = 0,02, 72 mu x 151 eps bis 1,6): **keine Kandidatenzelle**. Re W = 0 nur fuer mu = -0,17 ..
  -0,245, Im W = 0 nur fuer mu <= -0,38; getrennt wie bei l = 0. Also auch keine stille Oberflaechenmode (eine
  Gitterstufe).

## 6. Literatur (Erwartung vor dem Abruf in PLAN.md, 07:58:41)

Abrufe (date): Petrov-PDF 07:59:37; arXiv-Abfragen 08:15:05 bis 08:15:44, 08:24:04, 08:25:22, 08:25:38; Zusammenfassungen
08:15:56; PDFs Hu und Liu, Fort und Modugno, Ferioli u. a., Semeghini u. a., Cabrera u. a. ab 08:23:16. Die allgemeine
Websuche war in dieser Sitzung erschoepft (Kontingent 200 von 200); gesucht wurde deshalb nur ueber die arXiv-Schnittstelle
(Titel und Zusammenfassungen). Verlage (PRL, PRA) und Google Scholar sind nicht durchsucht.

| Punkt | Befund | Erwartung | Abgleich |
|---|---|---|---|
| EGPE, N_c, Selbstverdampfung | Petrov 2015 (arXiv 1506.08419, gelesen): Gl. (10) wie angenommen; N~_c = 18,65; metastabil fuer N~ < 22,55; "Only the monopole mode reenters at N~ = 20.1"; "in the interval 20.1 < N~ < 94.2 there are no modes below -mu"; Einheiten Gl. (7), (9); 39K-Beispiel: xi = 1,96 um, tau = 2,4 ms, N~ = 30 <-> N1 = 0,75e5, N2 = 1,1e5, tau_life ~ 150 ms mit K3 = 1e-29 cm^6/s | E-L1: N_c, 22,5, unterer Rand ~20 getroffen; "Oberflaechenmoden erst bei einigen hundert bis tausend unter der Schwelle" **verfehlt** (erste Mode schon bei 94,2) | teils |
| Oberer Rand der Atmung | Ferioli u. a. (arXiv 1912.09594, gelesen): "self-evaporating up to N~ = 934, where the monopole mode reenters"; Zeitrechnung: im Fenster "damped oscillation with decreasing frequency", gedaempfte Kosinusfits auf Zeitfenstern, Frequenz sinkt bis -mu, danach sehr langsame Restdaempfung | E-L2 (nur Zeitentwicklungen, keine Pol-Breiten) | getroffen |
| Breite gegen N, Nullstellen, Fano, "embedded modes" | Hu und Liu (arXiv 2008.04629, 2020, gelesen): diskrete Moden "only survive below the particle-emission threshold", N_th = 94,2 (gamma = 1/2), keine Breiten ueber der Schwelle. Fort und Modugno (41K-87Rb, arXiv 2012.10347) [Abs]: Selbstverdampfung als Zeitentwicklung, Parameterbereich fuer ein Experiment. Keine Arbeit mit Pol-Breiten, Nullstellen oder BIC bei Troepfchen gefunden | E-L2: ~85 % "nicht berichtet" | getroffen |
| 24-Monats-Suche (10/2024 bis 09/2026) | arXiv-Abfragen droplet + monopole / breathing / excitation spectrum / Fano / embedded / quasi-bound / bound state in the continuum: 2606.29370 (Atmung dipolarer Gase, Summenregeln, gefangen) [Abs], 2511.02394 (Kompressionsmodul, Atmungsfrequenz) [Abs], 2603.10304 (EFT der Oberflaechenschwingungen, Atmung wird bei kritischem Parameter mechanisch instabil) [Abs], 2601.18541 (1D-Bildung, Atmungsdaempfung aus Breitenoszillationen) [Abs]. BIC-Treffer betreffen nur Polaritonen in photonischen BIC-Strukturen. **Keine stille Monopolmode bei Troepfchen gefunden** | E-L2 | getroffen (Recherchestand, nur arXiv) |
| Experimente 39K | Semeghini u. a. 2018 (PRL 120, 235301; arXiv 1710.10890, gelesen): freier Raum mit Levitation, B_c = 56,85 G; bei 56,45 G faellt N in den ersten 10 ms schnell (Dreikoerperverluste), Groesse bis t_c konstant; bei 56,64 G "no oscillation of the size is visible", passend zur Selbstverdampfung ("discrete excitation modes are allowed only for N > 10^6 at this magnetic field"); "difficult to distinguish a self-evaporation effect in the losses dynamics". Cabrera u. a. 2018 (Science [L?]; arXiv 1708.07806, gelesen): Wellenleiter, delta a = -5,5 bis -2,4 a0 | E-L3: keine aufgeloeste Atmungsbreite, Dreikoerperverluste dominieren, Selbstverdampfung hoechstens indirekt | getroffen |
| 41K-87Rb | D'Errico u. a. 2019 (arXiv 1908.00761) [Abs]: langlebige heteronukleare Troepfchen im freien Raum | - | Kandidat fuer laengere Messzeiten |
| Eingebettete Solitonen | Yang, Malomed, Kaup 1999; Champneys u. a. 2001 [L?, in L4-BIC-LITERATUR.md der Runde 6 gelesen]: Kodimension 1. arXiv-Abfrage "embedded soliton" + experiment/observation: kein Experiment unter den Treffern | E-L4 | getroffen (Recherchestand) |
| Kubisch-quintisches Licht | Michinel u. a. 2002/2006 [L?]; 2507.19324 "Quantum Droplets of Light in Semiconductor Microcavities" (2025) [nur Titel]. Keine Atmungsbreite gefunden | E-L4 | offen, nicht vertieft |
| Riesen-Monopolresonanz | nicht vertieft; Fluchtbreite klein gegen Gesamtbreite [L?] | E-L5 | offen |

## 7. Messbezug in Laborgroessen (39K, Einheiten nach Petrov Gl. 7 und 9)

Streulaengen: a11 = 84,3 a0 (|1,0>), a22 = 33,5 a0 (|1,-1>) bei B0 (Petrov), delta a als Stellgroesse; auf ~30 % genau
(Abschnitt 1). N je N~ zaehlt beide Komponenten.

| delta a | xi | tau | N je N~ | Fenster N~ 20,1 .. 934 in Atomen | Atmungspole N~ 432 .. 752 |
|---|---|---|---|---|---|
| -2,5 a0 | 2,94 um | 5,3 ms | 1,11e4 | 2,2e5 .. 1,0e7 | 4,8e6 .. 8,4e6 |
| -3,2 a0 | 2,04 um | 2,55 ms | 6,0e3 | 1,2e5 .. 5,6e6 | 2,6e6 .. 4,5e6 |
| -4,8 a0 | 1,11 um | 0,76 ms | 2,2e3 | 4,4e4 .. 2,1e6 | 9,5e5 .. 1,7e6 |

- Frequenz und Daempfung der Atmung bei N~ = 561 (eps = 0,424 - 0,124 i): f = 0,424/(2 pi tau) = 26 Hz und
  Abklingzeit 1/Gamma = tau/0,124 = 21 ms bei delta a = -3,2 a0; 89 Hz und 6 ms bei -4,8 a0.
- Heutige 39K-Troepfchen: Semeghini u. a. starten mit einem BEC von bis zu 4e5 Atomen; der Tropfen verliert durch
  Dreikoerperverluste Atome, bis N unter N_c faellt, und wird dann zum Gas. Mit delta a(56,45 G) ~ -4,8 a0 (grob, aus
  B_c = 56,85 G und Petrovs Steigung 12,09 a0/G) sind das N~ ~ 18,65 bis hoechstens ~180. Dort hat die Atmung nach
  unserer Rechnung keinen Pol mit Gamma < 0,4/tau: Eine Anregung zerfliesst in etwa einer Schwingung. Das passt zu "no
  oscillation of the size is visible" (Semeghini, 56,64 G).
- Genauigkeit: Atomzahl ~10 bis 20 % [L?], Dreikoerperverluste halbieren N in ~10 ms (Semeghini). Die Daempfungszeiten der
  Atmung (6 bis 21 ms) liegen in derselben Groessenordnung; eine aufgeloeste Messung von Gamma(N) ist in 39K heute schwer,
  eher in langlebigen 41K-87Rb-Tropfen.
- **Was pruefbar waere, ohne neue Physik:** der Rand bei N~ ~ 930 (darueber ungedaempfte, darunter stark gedaempfte
  Atmung). Das ist die Vorhersage von Petrov bzw. Ferioli u. a., nicht unsere. Einbrueche bei N_n sagen wir fuer dieses System nicht
  voraus (Modell: keine).

## 8. Vorab-Abgleich (PLAN.md)

| Vorab | Ausgang |
|---|---|
| E-R1 Kontrollen (N_c 18,65 +- 0,05, E = 0 bei ~22,5, zwei Gitterstufen) | getroffen |
| E-R2 Schwellenlage (unten 19 bis 30, oben 400 bis 3000) | getroffen (20,1 und ~953) |
| E-R2 "an beiden Enden Gamma ~ q" | **verfehlt**: Der Pol geht unter die Schwelle aufs zweite Blatt (l = 0, keine Zentrifugalbarriere) |
| E-R3 glatt, keine Nullstelle | getroffen |
| E-R3 Gamma/eps_0 zwischen 1e-3 und 1e-1 | **verfehlt**: 0,12 bis 0,41, und fuer N~ <= 341 gar kein Pol mit Gamma < 0,4 |
| E-R4 Mechanismus: kein Wandtopf, keine Leiter im duennwandigen Bereich | getroffen (bis N~ = 7535) |
| E-R5 Oberschwingungen ueber der Schwelle (n_r = 1 bis N~ ~ 5000), "Breiten groesser als die der Grundmode, glatt" | getroffen: n_r = 1 ueber der Schwelle bis N~ ~ 5400 (Pol 0,502 - 0,043 i), bei 7535 gebunden; Breiten glatt und monoton (pol0b) |
| E-L1 bis E-L5 | siehe Abschnitt 6 |

## 9. Grenzen

- Nur die symmetrische Einkomponenten-Reduktion (Petrov Gl. 10); relative Bewegung der Komponenten, Massenunterschiede,
  endliche Reichweite (Cikojevic u. a. 2020: bis 20 % bei Anregungsfrequenzen [Abs]), Dreikoerperverluste und Levitation
  fehlen.
- Nur l = 0 vollstaendig; l = 2 siehe Abschnitt 5. Dipolare Troepfchen nicht gerechnet.
- N~ > 7500 (mu < -0,46) nicht gerechnet: Das Schiessen in doppelter Genauigkeit reicht dort nicht (Abschnitt 1).
  Nach Abschnitt 4 erwarte ich dort ebenfalls keine Stellen (Wandtopf fehlt erst recht) [H].
- Endlicher Aussenrand, abgetastete Konturen, keine Intervallrechnung.

## 10. Fehlerkasten

- Lokale Erkundungslaeufe (Skripte dbg1 bis dbg4 im Sitzungs-Scratchpad, je < 20 s, CPU, 1 Thread, nice 19, timeout 120)
  haben die Fenster fuer die Polsuche festgelegt. Ihre Ausgaben gingen nur auf die Konsole, nicht nach lauf-lokal/. Alle
  berichteten Zahlen stammen aus lauf-69/ bzw. den lauf-lokal-Dateien (Rauchtests, Einheiten).
- Die Polsuche fand anfangs Pole mit |D| ~ 1e-11 nicht, weil das Konvergenzmass zu streng war; berichtigt (Annahme bei
  |D| < 1e-8), vor pol0a.

## 11. Wo sonst? Vorschlaege fuer die Leitung (alles [H])

- Die Pruefliste aus Abschnitt 4: ein offener Kanal, ein geschlossener Kanal mit einem an Wand oder Oberflaeche gebundenen
  Zustand (Energie zwischen Wandtopf und Innerem) und ein Groessenparameter, der die Phase der Innenwelle verschiebt.
- Symmetrische Zweikomponenten-Troepfchen (Modell fuer 39K) erfuellen Punkt 2 nicht (dieses Ergebnis). Bei ungleichen
  Streulaengen, Massen (41K-87Rb) oder Besetzungen kommt ein zweiter offener Kanal hinzu; dann sind nur Minima zu
  erwarten, keine exakten Stellen (Abschnitt 13). Die Relativmoden der
  Komponenten liegen nach Petrov ohnehin tief im Kontinuum.
- Naechster Kandidat im Labor waere ein Troepfchen mit einer Randschicht: Drei-Komponenten- oder "Schalen"-Troepfchen,
  bei denen eine Komponente die Oberflaeche benetzt (arXiv 2312.15846, 2605.28469; nur Titel gelesen). Die Randschicht
  koennte den fehlenden Wandzustand liefern, wie die zweite Komponente in GF-BIC. Das ist eine Rechenkarte, keine
  Messvorhersage.
- Eingebettete Solitonen in chi(2)-Optik (Yang, Malomed, Kaup) haben dieselbe Kodimension 1; ein Experiment dazu habe ich
  nicht gefunden (nur arXiv durchsucht).
- Vorschlag fuer MESS-1: **parken**. Im Troepfchen ist die Antwort "nein" mit Positivkontrolle; eine Messvorhersage fuer
  bestehende Experimente gibt es nicht.

## 12. Einfach gesagt

Wir wollten wissen, ob man unsere "stillen Schwingungen" der Q-Baelle in echten Versuchen mit ultrakalten
Atomtroepfchen wiederfinden kann. Dazu haben wir am Computer berechnet, wie ein solches Troepfchen "atmet", also
abwechselnd groesser und kleiner wird, und ob es Troepfchengroessen gibt, bei denen es dabei keine Atome verliert. Die
Antwort ist nein: Wo die Atmung Atome verlieren kann (mittlere Troepfchengroessen), verliert sie sie auch, und zwar so
schnell, dass die Schwingung nach ein bis vier Schwuengen vorbei ist; eine Groesse, bei der der Verlust genau null wird,
gibt es nicht. Der Grund ist, dass dem Troepfchen die "Falle am Rand" fehlt, die beim Q-Ball einen Teil der
Schwingung festhaelt; dass unser Werkzeug solche stillen Stellen sonst sicher findet, haben wir am Q-Ball nachgeprueft.
Fuer Experimente heisst das: Kalium-Troepfchen sind der falsche Pruefstand, man braeuchte ein System mit einem
zusaetzlichen, am Rand gefangenen Zustand.

---
Erster Abschluss: 2026-09-30 08:36:52 CEST (date). Danach Pause der Leitung (Nutzungslimit, etwa 08:37 bis 09:51).

## 13. Nachtrag nach der Pause: Hinweise aus SUCH-1 (RUNDE-09/SUCHWORTE.md, Punkt 4)

- Begonnen 2026-09-30 09:57:00 CEST (date). Die Obertontabelle (pol0b) und die Gitterpruefung der Pole standen schon vor der Pause in
  Abschnitt 2 (eingetragen 08:36); es ging nichts verloren. Keine neue Rechnung.
- **1D immer gebunden, 3D nur dickwandig im Kontinuum.** Tylutki, Astrakharchik, Malomed, Petrov 2020 (arXiv 2003.05803)
  [Abs, abgerufen 09:56:12]: "A notable exception is the breathing mode which we find to be always bound"; die anderen
  Moden kreuzen der Reihe nach die Schwelle. Das passt zu unserem 3D-Bild: Die Grundatmung liegt nur fuer 20,1 < N~ < ~953
  im Kontinuum, also bei kleinen, dickwandigen Tropfen, und ist dort breit (Abschnitt 2).
- **Hoehere Obertoene als bessere Kandidaten: gerechnet, auch dort keine Stelle.**
  - pol0b: n_r = 1 bis 5 fuer N~ = 1044 bis 7535, W-Gitter bis eps = 2,0 in zwei Gitterstufen.
  - Die Obertoene sind schmaler als die Grundatmung (Gamma/Re eps bis 0,085), aber ihre Breite faellt glatt und monoton
    mit N~ und wird nirgends null.
  - Der Grund aus Abschnitt 4 gilt fuer sie erst recht: Der geschlossene Kanal braucht D + eps < 0, und hoeheres eps macht
    ihn nur noch verbotener. SUCH-1s Erwartung [ES] "Obertoene besser" trifft also fuer die Breite zu, fuer Stellen nicht.
- **Zwei offene Kanaele, nur Minima.** SUCH-1 nennt unausgewogene Mischungen (Flynn u. a. 2022, arXiv 2209.04318, nach
  SUCH-1 [A], von mir nicht abgerufen). Nach dem Zaehlargument (THEORIE-ATMUNGS-NULLSTELLEN.md, 3.4: vier statt zwei
  Bedingungen) gibt es dort entlang N nur Minima.
  - [H], Schreibtisch: Das betrifft auch ausgewogene reale 39K-Mischungen. Mit a11 = 84,3 und a22 = 33,5 a0 sind die
    Emissionsschwellen der beiden Sorten im Allgemeinen verschieden, und Gleich- und Gegentakt entkoppeln nicht mehr. Oberhalb beider
    Schwellen kann die Atmung Atome jeder Sorte abgeben.
  - Petrovs Einfeld-Reduktion verdeckt das. Selbst wenn sie Stellen haette, wuerden daraus in der vollen Zweikomponenten-
    Rechnung Minima. Gerechnet ist das nicht.
- Folge fuer den Bericht: Das Ergebnis "keine Stellen im Troepfchen" wird durch die drei Hinweise gestuetzt, nicht
  geaendert. Vorschlag bleibt: MESS-1 parken; eine Laborbruecke braucht einen gebundenen Wandzustand eines geschlossenen
  Kanals und genau einen offenen Kanal.

---
Ende: 2026-09-30 09:57:00 CEST (date, nach dem Schreiben gemessen).
