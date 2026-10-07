# KUBISCH-ANKER-L: Dossier. Laesst sich das kubische Richtungsmuster der Lichtverlangsamung auf Finns Netz mit vorhandenen Schranken schon pruefen? (Runde 44, Literatur, messnah)

- feldforscher fuer Leitung claude-primary. Start 2026-10-04 22:16:21 CEST, Abrufe 22:22:24 bis 22:34:38, Dossier ab
  22:38:36 CEST (alles date).
- Grundlage KARTE.md (KA1 bis KA3, unveraendert). Protokoll mit Erwartung vor jedem Abruf, Ausgang, Rueckfragen,
  Rechnungen und Berichtigungen: ARBEITSFELD.md (gleicher Ordner).
- 8 von 8 Abrufen verbraucht (arXiv-API viermal, arXiv-pdf dreimal, arXiv-API id_list einmal), keine Websuche. Kopien
  mit Abrufzeit in quellen/. Lokale Kopien frueherer Agenten (Martynenko 2026, JLM 2003, LHAASO 2024) zusaetzlich gelesen.
- Kennzeichen: [S] an der Quelle gelesen (Zeile Z. der pdftotext-Datei oder Tabelle), [S Abstract], [S-lokal] lokale Kopie
  eines frueheren Agenten, selbst gelesen, [P] Projektdatei, [L] Gedaechtnis, [M] Handrechnung, [ES] eigener Schluss,
  [H] Hypothese.

## 1. Ergebnis zuerst

1. **Schranken fuer den l = 4-Anteil gibt es (KA1 eingetroffen).** Zwei Arbeiten zerlegen alle 25 nicht doppelbrechenden
   d = 6-Koeffizienten c^(6)_(I)jm gleichzeitig aus vielen Himmelsrichtungen: Kislat/Krawczynski 2015 (~1e-14 GeV^-2) und
   Guerrero u. a. 2025 (95 %: die neun j = 4-Koeffizienten zwischen 0,6e-15 und 2,0e-15 GeV^-2) [S]. Sie sind rund 9
   Groessenordnungen schwaecher als die beste einzelne Sichtlinie (LHAASO, 1,05e-24 GeV^-2), weil "the least sensitive
   measurement in the sample of the best 25" alle Koeffizienten bestimmt (Guerrero [S]).
2. **Uebersetzung [M]:** a2(n) = -1/10 + (sqrt(pi)/90) [Y40 + sqrt(5/14)(Y44 + Y4,-4)] (Netzrahmen). In der SME-Form heisst
   das c00 = (sqrt(pi)/5) l^2 = 0,354 l^2, c40 = -0,0197 l^2, c4,+-4 = -0,0118 l^2; die drehfeste Groesse des j = 4-Teils ist
   0,073 c00. **Aus l = 4 allein folgt nur l < 7,7e-23 m** (Guerrero), rund 1e5-mal schwaecher als 7,0e-28 m (KA2
   eingetroffen).
3. **Trennen kann man heute nicht (KA3 eingetroffen).** Es gibt keinen anerkannten Richtungsnachweis. Die nominellen
   "Signale" der Literatur (5 von 32 GRB bei 4,7 bis 12,3 sigma, MAGIC Mrk 501, Agrawal u. a., Du u. a., Xiao/Song/Ma 2026)
   deuten die Autoren selbst als Quelleffekte oder als modellabhaengig. Fuer eine Trennung braeuchte es Nachweise (nicht
   Schranken) aus etwa 20 Richtungen mit je ~10 % Genauigkeit [M, grob].
4. **Fuer Finns Netz hilft die feste Kopplung, statt zu stoeren [M/ES]:** Jede Richtung ist subluminal, und der
   Unterschied zwischen den Richtungen ist hoechstens 4/3. Eine einzige Sichtlinie begrenzt deshalb alle Richtungen. Die
   LHAASO-Schranke 7,0e-28 m gilt bei jeder Ausrichtung. Die viel schaerferen HAWC-Werte (1e-31 GeV^-2) gelten nur fuer
   superluminales Licht und begrenzen das Netz nicht.
5. **Gegensweep:** Der staerkste moegliche "Satz gegen das feste Gitter" ist Vakuum-Cherenkov. Bei Lorentz-invarianten
   Elektronen liegt die Schwelle bei 1,6 sqrt(m_e M) (JLM Gl. 15 [S-lokal], [M]); das sind 30 TeV an der LHAASO-Grenze.
   PeV-Elektronen im Crab [L] erzwaengen dann l < ~1,6e-31 m [M, bedingt]. Sind die Elektronen mindestens so langsam wie das
   Licht, entfaellt die Schranke ganz (JLM [S-lokal]). Zweitens verbietet kubische Symmetrie Doppelbrechung bei k^2 nicht
   [L]. Dass Finns Netz keine hat, ist eine gerechnete Eigenschaft [P]. Das ist wichtig, weil die d = 6-Doppelbrechungs-
   schranken mit 1e-31 bis 1e-32 GeV^-2 7 bis 8 Groessenordnungen schaerfer sind [S].

## 2. Urteile KA1 bis KA3

| Nr | Erwartung (Karte, gekuerzt) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| KA1 | Veroeffentlichte Schranken fuer die l = 4-Koeffizienten (d = 6, nicht doppelbrechend) aus Quellen in mehreren Richtungen | 70 % | **eingetroffen** | Guerrero, Campoy-Ordaz, Potting, Gaug 2025, Tab. II (Layout-Text Z. 760-816 [S]): alle 25 Koeffizienten mit 95-%-Grenzen, darunter c40 [-2,0; 0,6], Re c41 [-0,7; 0,2], Im c41 [-1,0; 0,4], Re c42 [-0,7; 1,0], Im c42 [-1,0; 1,0], Re c43 [-0,6; 0,2], Im c43 [-0,6; 0,1], Re c44 [-0,5; 0,7], Im c44 [-0,9; 0,9] (e-15 GeV^-2). Kislat/Krawczynski 2015: "constraints on all 25 real coefficients", 25 AGN plus veroeffentlichte Grenzen [S Abstract], Werte in Data Tables D22 Teil 4 [S]. Dazu Labor (Laserinterferometrie) abs(c4m) < 2,4e-4 bis 1,3e-2 GeV^-2 (D22 Teil 3 [S]) |
| KA2 | Diese Schranken sind fuer l = 4 hoechstens so scharf wie die isotropen; die Netzschranke ueber l = 4 allein waere schwaecher als 7e-28 m | 75 % | **eingetroffen**, mit einer Feinheit | j = 4: 0,6e-15 bis 2,0e-15 GeV^-2 gegen isotrope bzw. Sichtlinien-Werte 1,05e-24 (LHAASO ueber Guerrero Gl. 28 [S]) bis 1e-20 (D22 Teil 5 [S]). Netzschranke ueber l = 4 allein 7,7e-23 m [M], also ~1e5-mal schwaecher. Feinheit: Innerhalb derselben globalen Zerlegung sind die j = 4-Grenzen etwas enger als die fuer c00 ([-3,4; 2,4]e-15), weil Y4m auf der Kugel groessere Spitzen hat als Y00 [M] |
| KA3 | Heute ist ein kubisches Muster mit unbekannter Ausrichtung nicht von einem isotropen zu trennen; es braucht ein Signal nahe der isotropen Schranke | 80 % | **eingetroffen** | Kein anerkannter Richtungsnachweis, auch nicht im 24-Monats-Fenster (F1, F6). Nominelle Signale werden von den Autoren als Quelleffekt oder modellabhaengig gelesen (Wei, J.-N. u. a. 2022 Z. 2278-2304 [S]; Agrawal u. a. 2021 [S Abstract]). Guerrero Z. 2028-2031 [S]: "a set of fourteen additional competitive bounds from very-high-energy or ultra-high-energy gamma-ray observatories could improve sensitivity to all c(I)jm by another five orders of magnitude!" Bedarf fuer eine Trennung [M]: N ~ 2270 s^2 Quellen mit Nachweis (Abschnitt 4.5) |

- Bedeutung nach der Karte: **KA3 trifft ein.** Das kubische Muster ist eine echte Vorhersage, heute aber nicht pruefbar.
  Pruefbar wird sie erst, wenn ueberhaupt eine quadratische Verlangsamung gemessen wird. Fuer L9 heisst das: ein Kandidat,
  keine Pruefung.
- Die Urteile sind kein Messbefund ueber das Netz. Sie sagen nur, was die Literatur heute trennen kann.

## 3. Erwartungsverstoesse (das eigentliche Ergebnis, wichtigstes zuerst)

| Nr | Erwartet (vorab, ARBEITSFELD) | Gefunden | Fundstelle | Korrektur |
|---|---|---|---|---|
| V1 gross | F2: Richtungssignal in der Mehrrichtungs-Arbeit 10 % | 5 von 32 GRB "incompatible with zero at the 4.7 sigma, 12.3 sigma, 5.0 sigma, 6.1 sigma, and 5.2 sigma"; AIC verwirft "kein LIV" mit 1e-6 bis 1e-34. Deutung der Autoren: "cannot be due to Lorentz-violating effects, as this would contradict with previous upper limits and must therefore be of intrinsic astrophysical origin". Dazu nominelle Werte in den Data Tables: GRB 190114C 5,05 +1,72/-1,25 e-13 (Du u. a. 2021), Mrk 501 3 +1/-2 e-22 (MAGIC ueber Kostelecky/Mewes), Agrawal u. a. 10^(-14,2 +- 0,1) GeV^-2; Xiao/Song/Ma 2026 "a preference for subluminal LV effects" (isotrop) | Wei, J.-N. u. a. 2022, Z. 2278-2304 [S]; D22 Teil 2, 3, 5 [S]; 2102.11248, 2602.01243 [S Abstract] | "Signal" heisst in diesem Feld: abhaengig vom Quellmodell. Fuer Finns Netz sind alle diese Werte mit der LHAASO-Sichtlinie unvereinbar, und zwar um gut 2 (Mrk 501) bis 13 Groessenordnungen (GBM), weil der Richtungskontrast hoechstens 4/3 ist [M] |
| V2 gross | F3: keine getrennten j = 4-Schranken (75 %) | Zwei vollstaendige Zerlegungen aller 25 Koeffizienten. Die neuere (Guerrero 2025) liegt im 24-Monats-Fenster und fehlte in meiner ersten Suche | D22 Teil 1 und 4 [S]; Guerrero Tab. II [S] | Die Karte (KA1, 70 %) hatte recht, meine Teilerwartung nicht |
| V3 gross | nicht erwartet in dieser Schaerfe | Die schwaechste der 25 besten Richtungen bestimmt alle Koeffizienten: y1 hat sigma 3,5e-25, y25 sigma 2,9e-15 GeV^-2 (gedrehte Kombinationen). Wer die Isotropie fallen laesst, verliert also rund 10 Groessenordnungen | Guerrero Z. 2020-2027 [S]; Tab. III (Layout Z. 840-870) [S] | [ES, Feldregel 6] Die Stellgroesse ist die Himmelsabdeckung mit starken Quellen, nicht die Zahl der Quellen. Finns Netz entgeht dem Verlust durch die feste l = 4/l = 0-Kopplung (Abschnitt 4.4) |
| V4 mittel | F3: LHAASO 221009A und Luftschauer-Schranken stehen in der SME-Sammlung | Data Tables v19 (Januar 2026, Literatur bis 31.12.2025): weder "LHAASO", "221009" noch "Martynenko". Zusammenfassung S3 nennt fuer c^(6)_(I)00 "two-sided" 1e-30 GeV^-2. Das passt zu HAWC (abs(c00) < 12,4e-31), und HAWC ist laut Abstract nur superluminal | F3 grep [S]; S3 Z. 2335-2360 [S]; HAWC 1911.08070 [S Abstract] | Fuer subluminale Modelle wie Finns Netz fuehrt die Zusammenfassung in die Irre. Die subluminal bindenden Werte stehen anderswo (LHAASO; Martynenko lokal [S-lokal]) |
| V5 mittel | Abschnitt 0: Martynenkos Cherenkov-Schwelle (2 m_e M^2)^(1/3) | JLM Gl. (15) gibt fuer n = 4 bei Lorentz-invarianten Elektronen p_th = (27/4)^(1/4) sqrt(m_e M), wie meine Kinematik. Li/Ma 2025: Crab-Vakuum-Cherenkov-Schranken sind 2022/2023 hergeleitet und in D-Schaum-Modellen umgehbar | JLM Z. 438-500 [S-lokal]; Martynenko 2026 Z. 176-209 [S-lokal]; 2505.06121 [S Abstract] | Widerspruch Martynenko gegen JLM offen (R1). Bedingte Netzschranke l < 1,6e-31 m [M] |
| V6 mittel | F2: angekuendigte volle Zerlegung wird ausgefuehrt (50 %) | Einleitung: "We combine these limits with previous results in order to fully constrain"; Diskussion: "it is not feasible to conduct a global fit" | Wei, J.-N. u. a. 2022, Z. 138-141 gegen Z. 2346-2350 [S] | Ausgefuehrt haben es andere (Kislat/Krawczynski, Guerrero) |
| V7 klein | F7: kein gezielter Test kubischer Richtungsabhaengigkeit | Neutronen-Interferometrie fuer richtungsabhaengige Dispersion eines kubisch-raumzentrierten Quantenlaufs: "could be employed to test any model that predicts a direction-dependent dispersion relation" | Brun/Mlodinow 2019, 1802.03911 [S Abstract] | Ein Labortest existiert, aber fuer massive Fermionen, nicht fuer Licht |
| V8 Kanal | Suchwoerter treffen | F1 ("time delay") verfehlte Guerrero ("time delays"); F7 verlangte "Lorentz" im Abstract und verfehlte Beane u. a. | ARBEITSFELD F1, F6, F7 | Die Urteile "nach Recherchestand" haben eine Wortwahl-Grenze |

## 4. Uebersetzung von Finns Muster in die Parametrisierung der Literatur

### 4.1 Zerlegung in Kugelflaechenfunktionen [M]

- Ausgang [P]: Phasentempo omega/k = c [1 + a2(n)(k l)^2], a2(n) = -1/8 + S4/24, S4 = n_x^4 + n_y^4 + n_z^4 (ERGEBNIS
  Z. 107-110; Karte). Achsen -1/12, Flaechendiagonalen -5/48, Raumdiagonalen -1/9, alle negativ (ERGEBNIS Z. 92 [P]).
- Mit x = sin t cos f, y = sin t sin f, z = cos t gilt x^4 + y^4 = sin^4 t (3/4 + cos 4f/4), also
  S4 - 3/5 = (2/5) P4(cos t) + (1/4) sin^4 t cos 4f.
- Mit Y40 = (3/(2 sqrt pi)) P4 und Y44 + Y4,-4 = (3/8) sqrt(35/(2 pi)) sin^4 t cos 4f (Condon-Shortley):
  **S4 - 3/5 = (4 sqrt(pi)/15) [Y40 + sqrt(5/14)(Y44 + Y4,-4)]**, z laengs einer Wuerfelachse.
- Proben: z-Achse beide Seiten 2/5; Raumdiagonale (cos t = 1/sqrt3, f = 45 Grad) beide Seiten -4/15. Kugelmittel
  <S4> = 3/5, <S4^2> = 3/9 + 6/105 = 41/105, Varianz 16/525.
- **Ergebnis:** a2(n) = -1/10 + (sqrt(pi)/90) [Y40 + sqrt(5/14)(Y44 + Y4,-4)]. Es gibt nur l = 0 und l = 4: l = 2 verbietet
  die kubische Symmetrie, ungerade l die Inversion. Der reine l = 4-Teil betraegt +1/60 (Achsen), -1/240
  (Flaechendiagonalen) und -1/90 (Raumdiagonalen). Relativ zum Mittel sind das Spitze 1/6 und RMS 0,073.

### 4.2 SME-Form an der Quelle und Umrechnung [S + M]

- SME, nicht doppelbrechend: s0 = sum_djm p^(d-4) Y_jm(n) c^(d)_(I)jm mit "n is the direction of the source" (Wei, J.-N.
  u. a. 2022, Z. 160, 180 [S]); Gruppentempo v_gr = 1 - (d - 3) s0 (Guerrero Gl. 25 [S]; Wei Z. 209 [S]); Umrechnung
  s+-/(2 E_QG,d-4^(d-4)) -> sum_jm Y_jm c^(d)_(I)jm (Guerrero Gl. 28 [S]). Phasentempo also 1 - s0.
- Abgleich mit dem Netz (hbar = c = 1): sum_jm Y_jm(n) c^(6)_(I)jm = -a2(n) l^2. Weil nur gerade j vorkommen, ist es
  gleich, ob n die Quell- oder die Flugrichtung ist.

| Groesse (Netzrahmen) | Formel [M] | Zahl | bei l = 7,0e-28 m = 3,55e-12 GeV^-1 |
|---|---|---|---|
| c^(6)_(I)00 | (sqrt(pi)/5) l^2 | 0,3545 l^2 | 4,5e-24 GeV^-2 |
| isotroper Koeffizient c-ring = c00/sqrt(4 pi) | l^2/10 | 0,1 l^2 | 1,26e-24 GeV^-2 |
| c^(6)_(I)40 | -(sqrt(pi)/90) l^2 | -0,01969 l^2 | -2,5e-25 GeV^-2 |
| c^(6)_(I)4,+4 = c^(6)_(I)4,-4 | -(sqrt(pi)/90) sqrt(5/14) l^2 | -0,01177 l^2 | -1,5e-25 GeV^-2 |
| uebrige c4m, alle j = 1, 2, 3 | 0 | 0 | 0 |
| drehfeste Norm N4 = (sum_m abs(c4m)^2)^(1/2) | (sqrt(pi)/90) sqrt(12/7) l^2 | 0,02579 l^2 | 3,2e-25 GeV^-2 |
| festes Verhaeltnis | c40/c00 = -1/18; N4/c00 = 0,0727 | | |

- Im Sonnen-Himmelsrahmen der SME mischt eine Drehung (drei Euler-Winkel, unbekannt) die neun c4m untereinander. N4 und
  c00 bleiben dabei fest. Finns Netz hat also vier Parameter (l^2 und drei Winkel), das allgemeine SME-Modell 25.
- Probe gegen das Projekt: LHAASO E_QG,2 > 6,9e11 GeV gibt sum Y c < 1/(2 (6,9e11)^2) = 1,05e-24 GeV^-2. Mit dem
  kleinsten abs(a2) = 1/12 folgt l^2 < 12 * 1,05e-24 GeV^-2, also l < 3,55e-12 GeV^-1 = 7,0e-28 m. Das ist die Zahl aus
  ERGEBNIS Abschn. 4 [P].
- **Abstand zur Literatur:** An der LHAASO-Grenze waeren Finns j = 4-Koeffizienten ~2e-25 GeV^-2. Die besten
  Einzelschranken liegen bei ~1e-15 GeV^-2. Dazwischen liegen 10 Groessenordnungen.

### 4.3 Schranke fuer l aus dem l = 4-Anteil allein [M]

- **Kastenrechnung:** Jede Ausrichtung, die mit allen neun 95-%-Intervallen vertraeglich ist, hat
  N4^2 <= sum w_i max(abs(Grenze_i))^2, mit w = 1 fuer c40 und w = 2 fuer Re und Im von c41 bis c44.
- **Guerrero 2025:** 4,0 + 2 (0,49 + 1,0 + 1,0 + 1,0 + 0,36 + 0,36 + 0,49 + 0,81) = 15,02, also N4 <= 3,88e-15 GeV^-2.
  Daraus l^2 < 3,88e-15/0,02579 = 1,50e-13 GeV^-2, also **l < 3,9e-7 GeV^-1 = 7,7e-23 m**.
- **Kislat/Krawczynski 2015** (Intervalle laut Tabelle, Niveau nicht gelesen): N4 <= 9,8e-14 GeV^-2, also l < 3,9e-22 m.
- **Zum Vergleich mit denselben Daten ueber l = 0:** c00 < 2,4e-15 gibt l < 1,6e-23 m. Ueber die beste Sichtlinie
  (LHAASO) folgt l < 7,0e-28 m.
- **Idealfall:** Zwei gleich empfindliche Sichtlinien liegen zufaellig laengs Achse und Raumdiagonale. Die Differenz
  (1/9 - 1/12) l^2 = l^2/36 gibt dann l^2 < 72 X statt 12 X. Selbst so ist der l = 4-Weg sqrt(6) = 2,4-mal schwaecher als
  der isotrope.
- Die Kastenrechnung ist grosszuegig: Alle neun Koeffizienten stehen dabei zugleich am Rand. Ein echter Fit der vier
  Netzparameter an Guerreros Kovarianz ist nicht gemacht. Er kann die Sichtlinien-Schranke nicht schlagen, weil y1 (beste
  Richtung) schon darin steckt [ES].

### 4.4 Warum die Ausrichtung fuer die Schranke kaum zaehlt (Allrichtungs-Satz) [M/ES]

- Der Sichtlinien-Koeffizient des Netzes C(n) = abs(a2(n)) l^2 liegt zwischen l^2/12 und l^2/9 und hat ueberall dasselbe
  Vorzeichen (subluminal).
- Eine Schranke X in einer Richtung gilt deshalb in jeder Richtung als <= (4/3) X. LHAASO allein gibt C(n) <= 1,4e-24
  GeV^-2 am ganzen Himmel.
- Das allgemeine SME-Modell kann dagegen in einer Richtung null und in einer anderen gross sein. Deshalb braucht es dort
  25 Richtungen (Wei, J.-N. u. a. Z. 113-117 [S]: "at least (d - 1)^2 sources distributed evenly in the sky").
- Folge 1: Superluminale Schranken (HAWC, Photonzerfall c00 > -1,1e-28 [S]) begrenzen das Netz nicht.
- Folge 2: Alle nominellen Signale aus V1 sind im Netzmodell mit LHAASO unvereinbar.
- Vorbehalt der Quelle: LHAASO hat Eigenverzoegerungen nicht modelliert, "nature has conspired to compensate" ist nicht
  ausgeschlossen (Guerrero Z. 1999-2008 [S]). Ein einzelnes Ereignis bleibt "an isolated event" (Z. 1011-1012 [S]).

### 4.5 Was eine Trennung braeuchte (Unterscheidungspunkte, Feldregel 2)

| Paar | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|
| isotrop gegen Finns kubisches Muster | Sichtlinien-Koeffizient relativ zum Mittel: 5/6 (Achsen), 25/24 (Flaechendiag.), 10/9 (Raumdiag.) gegen ueberall 1. Bedarf [M, grob, zufaellige Richtungen]: N ~ 2270 s^2 Quellen mit relativem Fehler s, also ~23 bei 10 %, ~6 bei 5 %, ~90 bei 20 %. Jede braucht einen Nachweis mit ~10 sigma, keine Schranke | heute nein: nur eine Quelle (GRB 221009A) erreicht die fuehrende Empfindlichkeit; Guerrero: 14 weitere konkurrenzfaehige Quellen allein fuer +5 Groessenordnungen im allgemeinen Fall [S] |
| Finns Netz gegen andere Netze/Operatoren | c40/c00 im Netzrahmen: Maxwell auf Finns Netz -1/18, Skalar Diamant -4/27, Grover -1/3, Wuerfel Z3 +2/9 [M aus P]. Das Vorzeichen zeigt, welche Richtung am schnellsten ist: bei Finns Netz die Achsen, beim Wuerfel die Raumdiagonalen | erst nach einem Nachweis in >= 5 Richtungen |
| Netzsignal gegen Eigenverzoegerung der Quelle | Netz: gleiche Groessenordnung in allen Richtungen (Faktor <= 4/3), Skalierung E^2 und dasselbe kosmologische Integral K(z) fuer alle Quellen. Quelle: von Quelle zu Quelle verschieden | teilweise: Stichproben ueber Rotverschiebung und Quelltyp (Guerrero Z. 2008-2010 [S] fordert genau das: "sources at different distances and of different origins") |
| Elektronen Lorentz-invariant gegen Elektronen auf dem Netz | Vakuum-Cherenkov-Schwelle 1,6 sqrt(m_e M) gegen keine Schwelle (eta <= xi <= 0, JLM [S-lokal]) | ja, ueber Crab-PeV-Elektronen [L]; die Zahl der Literatur ist nicht gelesen (O2) |

- Was fehlt also: (1) ueberhaupt ein Nachweis einer quadratischen Laufzeit; (2) viele Quellen mit TeV- bis PeV-Photonen
  am ganzen Himmel. Die Empfindlichkeit waechst mit E^2, keV-MeV-Daten liegen 9 bis 13 Groessenordnungen zurueck.
  (3) Eigenverzoegerungen auf etwa 10 % beherrscht. (4) Rotverschiebungen, die K(z) auf wenige Prozent festlegen.

### 4.6 Regime und Moderatoren (Feldregel 1)

| Streitpunkt | Regime A | Regime B | Moderator | Beleg |
|---|---|---|---|---|
| "Signal" gegen Nullresultat bei d = 6 | keV-MeV-Spektralverzoegerung (GBM): Werte 1e-15 bis 1e-11 GeV^-2, teils 4,7 bis 12,3 sigma | GeV-TeV-Laufzeit: Sichtlinie < 1e-24 GeV^-2 | Photonenergie und Quellmodell | Wei 2022 [S]; Agrawal 2021 [S Abstract]: konstante Eigenverzoegerung plus Streuung "no evidence", GRB-abhaengige Parameter "decisive evidence" |
| Einzelkoeffizienten ~1e-15 gegen Sichtlinie ~1e-24 | 25 freie Koeffizienten | 1 isotroper Koeffizient (oder Netz mit fester Kopplung) | Modellannahme und Himmelsabdeckung | Guerrero Z. 2020-2027 [S] |
| HAWC 1e-31 gegen LHAASO 1e-24 | superluminal (Photonzerfall) | subluminal (Laufzeit, Luftschauer) | Vorzeichen | HAWC [S Abstract]; D22 Teil 3 [S] |
| Vakuum-Cherenkov schliesst aus gegen ohne Belang | Elektronen Lorentz-invariant oder schneller als Licht | Elektronen mindestens so subluminal | Differenz der Sektoren eta - xi | JLM Gl. (15), Z. 498-500 [S-lokal]; Li/Ma 2025 [S Abstract] |

- [ES, Feldregel 6] "Richtungsabhaengigkeit verhindert die Schranke" hat drei Wege (zu wenige Richtungen, unbekannte
  Ausrichtung, Vorzeichenwechsel zwischen Richtungen). Die gemeinsame Groesse ist das Verhaeltnis von kleinstem zu
  groesstem Sichtlinien-Koeffizienten. Ist es endlich und positiv, wie bei Finns Netz mit 3/4, wird jede Sichtlinie zur
  Allrichtungs-Schranke.

## 5. Gegensweep, Kalibrierung, offene Fragen, Quellen, Selbstanzeigen

### 5.1 Gegensweep (Feldregel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlich | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | Finns Maxwell-Netz ist in jeder Richtung subluminal | ja [P] | a2 = -1/12 bis -1/9, alle negativ (ERGEBNIS Z. 92). Darum zaehlen superluminale Schranken nicht |
| G2 | E_QG,2 und SME-Koeffizient haengen ueber 1/(2 E^2) zusammen | ja [S] | Guerrero Gl. (28); Gruppentempo mit (d - 3) (Gl. 25; Wei Z. 209). Umrechnung 1,05e-24 GeV^-2 bestaetigt |
| G3 | Kubische Symmetrie verbietet Doppelbrechung bei k^2 | ja, Rechnung [M], Physik [L] | Nein. Kubische Kristalle haben k^2-Doppelbrechung laengs [110] (CaF2 bei 157 nm, Burnett u. a. 2001 [L]). Finns Netz zeigt keine, Gleichheit auf ~1e-10 [P]. Der Rest waere <= 1e-10 * 1,26e-23 = 1,3e-33 GeV^-2 und liegt unter den Doppelbrechungswerten 1e-31 bis 1e-32 (D22 Teil 7 [S]). Heute also nicht bindend. Es ist aber eine Eigenschaft dieses Operators, keine Folge der Symmetrie |
| G4 | Die (k l)^2-Entwicklung gilt bei TeV | ja [M] | k l = 1e4 GeV * 3,55e-12 GeV^-1 = 3,5e-8, das a4-Glied ist relativ ~1e-15 |
| G5 | Die Projektanker stehen in der SME-Sammlung | ja [S] | Nein (V4) |
| G6 | Das Netz ruht im Sonnen-Rahmen der SME | nein | Bewegung ~1,2e-3 c gegen die Hintergrundstrahlung [L] mischt ungerade j relativ ~1e-3 ein [ES]. Ohne Belang fuer Groessenordnungen |
| G7 | Die Elektronen sind Lorentz-invariant oder genauso langsam | nein [H] | Davon haengt der Vakuum-Cherenkov ab: entweder l < ~1,6e-31 m oder gar keine Schranke |

### 5.2 Kalibrierung

- **(a) Gemessen:**
  - LHAASO-Sichtlinie null (1,05e-24 GeV^-2);
  - HAWC ueber 100 TeV, superluminal null;
  - zwei globale Zerlegungen, alle 25 Koeffizienten mit null vertraeglich (Guerrero Tab. II: alle Intervalle enthalten 0);
  - nominelle GBM-Werte ungleich null, von den Autoren als Quelleffekt gedeutet;
  - Doppelbrechungsschranken d = 6 bei 1e-31 bis 1e-32 GeV^-2.
- **(b) Nuetzlich verdichtet [M/ES]:**
  - Zerlegung und Koeffiziententabelle (4.1, 4.2); l = 4-Schranke 7,7e-23 m;
  - Allrichtungs-Satz (Faktor 4/3) und die Unvereinbarkeit der nominellen Signale mit dem Netz;
  - Bedarf N ~ 2270 s^2; Kennung c40/c00 je Operator;
  - bedingte Cherenkov-Schranke 1,6e-31 m.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - KA3 war schon vor dem ersten Abruf fast ableitbar (ohne Nachweis keine Trennung, ARBEITSFELD 1.3). Die Abrufe haben
    das nur bestaetigt; der Treffer ist darum schwach.
  - Meine Sicherheit in die Cherenkov-Schwelle stieg mit JLM. Der Widerspruch zu Martynenko Gl. (7) ist aber nicht
    aufgeloest, und die Literaturzahl fuer quadratisches subluminales Licht habe ich nicht gelesen.
- **Warnzeichen:** Waehrend die Frage in feinere Teile zerfiel (Vorzeichen, Himmelsabdeckung, Elektronensektor,
  Quellmodell), wuchs meine Sicherheit, dass "nicht trennbar" gilt. Das ist durch Guerrero gedeckt. Fuer die bedingte
  Cherenkov-Zahl ist es nicht gedeckt.

### 5.3 Offene Fragen

1. R1: Gilt fuer subluminales Licht der Dimension 6 mit Lorentz-invarianten Elektronen die Schwelle 1,6 sqrt(m_e M)
   (JLM Gl. 15, meine Rechnung) oder (2 m_e M^2)^(1/3) (Martynenko 2026 Gl. 7)?
2. O2: Welche Zahl geben Li/Ma (PLB 829, 137034; PLB 835, 137536; PRD 108, 063006) fuer quadratisch subluminales Licht aus
   Crab-Elektronen? Gilt sie richtungsgemittelt?
3. R2: Worauf bezieht sich bei Kostelecky/Mewes 2008 "some support at one sigma ... for anisotropic violation"? Ist es der
   Mrk-501-Wert 3 +1/-2 e-22 gegen die GRB-Nullresultate [H]?
4. Traegt Finns Netz auch die Elektronen, und mit welchem a2 (Sektorfrage, vgl. LICHT-GLEICH-L [P])? Das entscheidet,
   ob der Vakuum-Cherenkov das Netz um vier Groessenordnungen schaerfer begrenzt.
5. Fehlt die k^2-Doppelbrechung in Finns Netz exakt (Symmetrie des Operators) oder nur numerisch klein? Die Rechnung
   zeigt ~1e-10 [P]; ein Beweis fehlt.

### 5.4 Quellenliste (Abrufstand 2026-10-04, Zeiten per date)

| Quelle | URL | Abruf, Kopie | gelesen |
|---|---|---|---|
| Wei, J.-N.; Liu, Z.-K.; Wei, J.-J.; Zhang, B.-B.; Wu, X.-F. (2022): Exploring Anisotropic Lorentz Invariance Violation from the Spectral-Lag Transitions of Gamma-Ray Bursts. Universe 8, 519 | https://arxiv.org/abs/2210.03897 | F2 22:23:18, quellen/F2-wei-2210.03897v1.pdf/.txt | [S] Z. 105-262, 548-557, 2276-2385, Literatur |
| Kostelecky, V. A.; Russell, N. (2026): Data Tables for Lorentz and CPT Violation, January 2026 update (arXiv:0801.0287v19) | https://arxiv.org/abs/0801.0287 | F3 22:24:43, quellen/F3-datatables-0801.0287.pdf/.txt, F3-datatables-D22-layout-S62.txt, -S63-69.txt | [S] Z. 268-279, S3 Z. 2335-2640, D22 S. 62-69, Literatur Z. 1124-1557 |
| Guerrero, M.; Campoy-Ordaz, A.; Potting, R.; Gaug, M. (2025): Bounding anisotropic Lorentz Invariance Violation from measurements of the effective energy scale of quantum gravity. PRD 112, 104002 (nach Data Tables) | https://arxiv.org/abs/2508.02883 | F5 22:30:07, quellen/F5-guerrero-2508.02883v1.pdf/.txt/-layout.txt | [S] Gl. 2, 3, 25-28, Z. 583-600, 969-1012, 1987-2031, Tab. II, III |
| Kislat, F.; Krawczynski, H. (2015): Search for anisotropic Lorentz invariance violation with gamma-rays. PRD 92, 045016 | https://arxiv.org/abs/1505.02669 | F4 22:29:09 | [S Abstract]; Werte ueber Data Tables D22 Teil 4 [S] |
| Albert, A. u. a. (HAWC) (2020): Constraints on Lorentz invariance violation from HAWC observations of gamma rays above 100 TeV. PRL 124, 131101 | https://arxiv.org/abs/1911.08070 | F4 | [S Abstract]; Werte ueber D22 Teil 3 [S] |
| Agrawal, R.; Singirikonda, H.; Desai, S. (2021): Search for Lorentz Invariance Violation from stacked Gamma-Ray Burst spectral lag data. JCAP 05, 029 | https://arxiv.org/abs/2102.11248 | F4 | [S Abstract] |
| Beane, S. R.; Davoudi, Z.; Savage, M. J. (2014): Constraints on the Universe as a Numerical Simulation. Eur. Phys. J. A 50, 148 [L fuer die Zeitschrift] | https://arxiv.org/abs/1210.1847 | F4 | [S Abstract] |
| Kostelecky, V. A.; Mewes, M. (2009): Electrodynamics with Lorentz-violating operators of arbitrary dimension. PRD 80, 015020 | https://arxiv.org/abs/0905.0031 | F4 | [S Abstract]; Formeln ueber Wei 2022 und Guerrero 2025 [S] |
| Wei, J.-J.; Wu, X.-F.; Zhang, B.-B.; Shao, L.; Meszaros, P.; Kostelecky, V. A. (2017): Constraining Anisotropic Lorentz Violation via the Spectral-Lag Transition of GRB 160625B. ApJ 842, 115 | https://arxiv.org/abs/1704.05984 | F1 22:22:24, quellen/F1-arxiv-api-anisotrop-laufzeit.xml | [S Abstract] |
| Kostelecky, V. A.; Mewes, M. (2008): Astrophysical Tests of Lorentz and CPT Violation with Photons. ApJL 689, L1 | https://arxiv.org/abs/0809.2846 | F1 | [S Abstract] |
| Xiao, Z.; Song, H.; Ma, B.-Q. (2026): Constraints on birefringence-free photon theory within standard-model extension | https://arxiv.org/abs/2602.01243 | F6 22:33:15, quellen/F6-arxiv-api-24monate.xml | [S Abstract] |
| Brun, T. A.; Mlodinow, L. (2019): Detection of discrete spacetime by matter interferometry. PRD 99, 015012 | https://arxiv.org/abs/1802.03911 | F7 22:33:56, quellen/F7-arxiv-api-gitter-kubisch.xml | [S Abstract] |
| Li, C.; Ma, B.-Q. (2025): Constraints to Lorentz violation and ultrahigh-energy electrons in D-foamy space-times. JHEP 10, 216 | https://arxiv.org/abs/2505.06121 | F8 22:34:38, quellen/F8-arxiv-api-vakuum-cherenkov.xml | [S Abstract] |
| Schreck, M. (2017): Vacuum Cherenkov radiation for Lorentz-violating fermions. PRD 96, 095026 | https://arxiv.org/abs/1702.03171 | F8 | [S Abstract] |
| Du, S. S. u. a. (2021), ApJ 906, 8 (GRB 190114C); Vasileiou, V. u. a. (2013), PRD 87, 122001; Aharonian, F. u. a. (H.E.S.S.) (2008), PRL 101, 170402; Albert, J. u. a. (MAGIC) (2008), PLB 668, 253; Boggs, S. E. u. a. (2004), ApJ 611, L77; Astapov/Kirpichnikov/Satunin (2019), JCAP 1904, 054; Rubtsov/Satunin/Sibiryakov (2017), JCAP 1705, 049; Kostelecky/Melissinos/Mewes (2016), PLB 761, 1 | ueber Data Tables | - | nur Tabellenwerte D22 [S], Arbeiten selbst nicht gelesen |
| Martynenko, N. S.; Rubtsov, G. I.; Satunin, P. S.; Sharofeev, A. K.; Troitsky, S. V. (2026): Constraining Lorentz invariance violation from the depth of air-shower maximum (arXiv:2608.05106v1) | https://arxiv.org/abs/2608.05106 | lokal RUNDE-34/grb-221009a/quellen/ | [S-lokal] Z. 1-24, 84-222, 692-712 |
| Jacobson, T.; Liberati, S.; Mattingly, D. (2003): Threshold effects and Planck scale Lorentz violation. PRD 67, 124011 | https://arxiv.org/abs/hep-ph/0209264 | lokal RUNDE-34/grb-221009a/quellen/ | [S-lokal] Z. 425-500 |
| Projektdateien: licht-finn-netz-1/ERGEBNIS.md, NACHTRAG-PHASE-GRUPPE.md; strang-anker-l/DOSSIER.md; licht-gleich-l/DOSSIER.md | lokal | - | [P] |

### 5.5 Selbstanzeigen

1. **Abrufweg:** Alle 8 Abrufe liefen mit curl statt WebFetch, damit es lokale Kopien mit Abrufzeit gibt. Jeder
   curl-Aufruf ist als ein Abruf gezaehlt. Die pdf-Dateien habe ich lokal mit pdftotext gelesen, teils mit -layout fuer
   einzelne Seiten.
2. **grep-Ausschluesse unvollstaendig:** Nur der erste grep ueber RUNDE-34/grb-221009a/quellen trug alle
   vorgeschriebenen --exclude-Optionen. Spaetere greps ueber einzeln genannte Dateien dort (Martynenko, JLM) und in
   meinem eigenen quellen/ liefen ohne diese Optionen. Keiner war rekursiv, und keine versiegelte Datei und kein
   KS-1-Ergebnis wurde beruehrt. Der find-Aufruf schloss die Pfade per -prune aus.
3. **Zeitangaben:** In zwei Erwartungskoepfen stand eine gerundete bzw. falsche Zeit ("22:3x" statt 22:29:09, "22:35"
   statt 22:34:38). Berichtigt in ARBEITSFELD Abschnitt 10. Die Reihenfolge Erwartung vor Abruf gilt in allen Faellen.
4. **Eigene Teilerwartungen verfehlt:** F2 (Signal 10 %) und F3 (keine j = 4-Schranken 75 %) lagen daneben. KA1 bis KA3
   sind unveraendert.
5. **Nur Abstract** sind HAWC (superluminal), Kislat/Krawczynski, Agrawal, Beane u. a., Xiao/Song/Ma, Brun/Mlodinow,
   Li/Ma und Schreck. Die HAWC-Einordnung "nur superluminal" fuer n = 2 stuetzt sich auf den Abstract und den Mechanismus
   Photonzerfall [L].
6. **[L]:** CaF2-Doppelbrechung (Burnett u. a. 2001), H.E.S.S.-Elektronen bis ~40 TeV, PeV-Elektronen im Crab, Bewegung
   gegen die Hintergrundstrahlung, sqrt(5/14) als Kennzahl kubischer Harmonischer (an zwei Punkten nachgerechnet).
7. **Rechnungen** von Hand, nicht gegengelesen: Zerlegung, Koeffiziententabelle, Kastenrechnung, Bedarf N ~ 2270 s^2
   (grob, zufaellige Richtungen, Gauss-Fehler) und Cherenkov-Zahlen. Ein echter Fit der vier Netzparameter an Guerreros
   Kovarianz fehlt.
8. **Suchgrenzen:** F1 verfehlte Guerrero wegen der Wortform, F7 verfehlte Beane u. a. wegen der Pflicht "Lorentz". Die
   Urteile "nach Recherchestand" stehen unter diesem Vorbehalt.
9. **Werkzeuge lokal:** date, ls, find, grep, sed, tr, cut, fold, head, wc, file, cat, mkdir, curl, pdftotext. Kein
   python, awk oder perl. Zwei Befehlszeilen enthielten blosse Shell-Variablen mit "awk" im Namen ("awk_free=1",
   "awk_none=1"); awk lief dabei nicht. Geschrieben nur in kubisch-anker-l/ (ARBEITSFELD.md, DOSSIER.md, quellen/).
   Kein Journal, kein Peerbus, kein Commit.
10. **Die Datei F5-guerrero-2508.02883v1.pdf meldet bei file "1 page(s)".** Der Text ist trotzdem vollstaendig (3251
    Zeilen, Literaturliste vorhanden); fuer das Ergebnis ohne Folge.

## 6. Einfach gesagt

Auf Finns Netz waere Licht sehr hoher Energie ein kleines bisschen langsamer, und zwar je nach Richtung verschieden: laengs
der Wuerfelachsen am wenigsten, laengs der Raumdiagonalen am meisten, hoechstens um ein Drittel verschieden. Forscher
haben Lichtblitze aus vielen Himmelsrichtungen ausgewertet, aber nirgends sicher eine solche Verlangsamung gefunden; die
Grenzen fuer die "Richtungsanteile" sind dabei viel schwaecher als die fuer den "Mittelwert", weil nur wenige Richtungen
mit sehr energiereichem Licht gut vermessen sind. Fuer Finns Netz ist das aber kein Nachteil: Weil das Licht in jeder
Richtung langsamer wird und die Richtungen sich hoechstens um ein Drittel unterscheiden, reicht schon ein einziger gut
gemessener Blitz fuer die Aussage: Wenn das Netz das Licht traegt, muss seine Masche kleiner als etwa 7e-28 m sein. Ob
das Muster wirklich kubisch ist, kann man erst pruefen, wenn man ueberhaupt eine Verlangsamung misst, und dann in etwa
zwanzig Richtungen.

## Vermerk der Leitung (2026-10-05 14:44:19 CEST, date): Empfindlichkeit, keine Schranke

- Die Werte "1e-31 bis 1e-32 GeV^-2" (Z. 30, 37, 184 und ARBEITSFELD Z. 196) sind nach Kostelecky/Mewes 2013 nur "approximate maximal sensitivity" (Zeichen <~, in den Data Tables "derived on theoretical grounds"). Strenge Schranken fuer alle 42 doppelbrechenden d = 6-Koeffizienten liegen bei 6,6e-18 bis 8,8e-18 GeV^-2 (Friedman u. a. 2020) [S, DOPPELBRECHUNG-V-L/DOSSIER.md].
- Der Satz "7 bis 8 Groessenordnungen schaerfer als die nicht doppelbrechenden Schranken" gilt nur fuer die Empfindlichkeit, nicht fuer strenge Schranken. Die uebrigen Aussagen dieses Dossiers bleiben unberuehrt.
