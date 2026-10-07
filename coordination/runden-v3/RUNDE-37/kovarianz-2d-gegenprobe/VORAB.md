# KOVARIANZ-2D-GEGENPROBE: Vorab-Datei (Kontinuumsvorhersagen, vor jeder Messung)

- Code-Agent fuer die Leitung claude-primary. Abschnitte 1 bis 3 geschrieben ab 2026-10-04 16:31:53 CEST (date), vor
  jeder Rechnung (auch vor dem vorab-Lauf). Abschnitt 4 (exakte Quadratur, reine Kontinuumsrechnung, keine Gitterzahl)
  wird nach dem vorab-Lauf ergaenzt; die Zeit steht dort.
- Kennzeichen: [M] eigene Mathematik, [L] Literatur aus dem Gedaechtnis, [P] Projektdatei, [E-v] numerische Auswertung
  einer Kontinuumsformel (keine Messung), [H] Hypothese, [K] Kartenpunkt (vor dem Rechnen festgehalten).
- **Konvention (wie kovarianz.py):** Gamma = 1/2 log det' K, K = P1-Steifigkeit (Kotangens-Laplace) aus den
  Kantenlaengen, k1.auswerten, Fassung roh (in 2D ist korr = 0). Delta Gamma = Gamma(verformt, QI) - Gamma(rund, Q),
  gepaart je Saat und N. **In 2D ist die Vorhersage fuer Delta Gamma selbst N-unabhaengig**; die 4D-Groesse
  y = Delta Gamma/sqrt(N) wird nur zum Vergleich mitberichtet.

## 1. Schreibtisch

**S1 Polyakov-Formel und Normierung [L, M].**
- Osgood-Phillips-Sarnak (Polyakov-Alvarez) fuer g = e^(2 sigma) g0 auf einer geschlossenen Flaeche:
  log det' Delta_g - log det' Delta_g0 = -(1/(6 pi)) [1/2 Int abs(grad0 sigma)^2 dA0 + Int K0 sigma dA0] + log(A_g/A_0).
  Die Formel ist fuer konforme Aenderungen exakt (integrierte Spuranomalie), nicht nur in zweiter Ordnung [L].
- Probe gegen die Projektkonvention [M, P]: Auf dem flachen Torus (K0 = 0) gibt die Haelfte davon
  Delta Gamma = -(1/(24 pi)) Int abs(grad sigma)^2; mit sigma = s cos(k x) folgt Gamma'' = -k^2 A/(24 pi) = P k^2 A, genau
  die Definition von P = -1/(24 pi) in INDUZIERT-DICHTE-2D. Gleiche Normierung, gleicher Faktor 1/2.
- **Flaeche:** Die Vorschrift normiert Int e^(2 sigma) dA0 = A0 = N (Verformung.c_norm). Das Glied log(A_g/A_0) faellt weg.
- **Nullmode:** Gamma = 1/2 log det' K (Produkt der von null verschiedenen Eigenwerte; kugel.py: 1/2 (log det K_(0) +
  log N)). Das Kontinuums-det' laesst die Nullmode ebenfalls weg; ihr Normierungsglied ist log A, also fest.
  Gitter: log det' K = log det'(M^-1 K) + Summe log m_i - log(Summe m_i/N). Bei Punkten der Dichte 1 bezueglich g ist
  Summe log m_i in Erwartung fuer rund und verformt gleich bis auf ein Kruemmungsglied proportional Int K dA (in 2D
  topologisch). Vorhersage fuer Gamma und Gamma_M daher dieselbe [M, H fuer die Gitterkorrekturen].
- Auf der Kugel ist alles skaleninvariant (Int abs(grad sigma)^2 dA und Int K0 sigma dA0 haengen nicht vom Radius a ab):
  **Delta Gamma_P = -(1/(12 pi)) [1/2 Int abs(grad sigma)^2 dOmega + Int sigma dOmega]**, Einheitskugel, mit dem
  normierten sigma (inklusive Konstante c). **Unabhaengig von N.**
- Onofri-Ungleichung [L]: Bei fester Flaeche ist die Klammer >= 0, Gleichheit genau fuer Moebius-Faktoren. Also
  Delta Gamma_P <= 0: die runde Kugel ist das Maximum von det' (OPS). Fuer M ist Delta Gamma_P exakt 0.

**S2 Zweite Ordnung [M].** sigma = c + tau, Int tau dOmega = 0. Feste Flaeche: c = -Int tau^2 dOmega/(4 pi) + O(3), also
Int sigma dOmega = -Int tau^2 dOmega. Fuer tau in der Kugelflaechenfunktion vom Grad l:
Delta Gamma_P = -(1/(12 pi)) (l(l+1)/2 - 1) Int tau^2 dOmega. l = 1: 0. l = 2: -(1/(6 pi)) Int tau^2 dOmega.
Fuer sigma = eps (1 - 3 cos^2 theta) (zonale l = 2-Funktion, wie in kovarianz.py 1 - 5 cos^2 theta fuer S^4) ist
Int (1 - 3 cos^2 theta)^2 dOmega = 16 pi/5, also **Delta Gamma_P = -(8/15) eps^2 = -0,5333 eps^2** (zweite Ordnung).

**S3 Projekt-Koeffizient [P].** Vorhersage pred = kappa Delta Gamma_P mit kappa = 1,075 +- 0,071 (INDUZIERT-DICHTE-2D-GROB,
Grenzwert k -> 0; Hauptwert) bzw. 0,924 +- 0,087 (INDUZIERT-DICHTE-2D, Fenster-Steigung bei k eps ~ 0,3).
- Gitterdispersion [H, Uebertrag vom Torus]: GROB fand c(k) = c(0) + d k^2 mit d = +0,0215 +- 0,0025 (Netzabstand 1).
  Die l = 2-Mode der Kugel hat k^2 = 6/a^2 = 24 pi/N = 0,075 / 0,038 / 0,019 / 0,0094 bei N = 1000 / 2000 / 4000 / 8000.
  Wirkt die Dispersion nur auf das Gradientenglied (Anteil 3 gegen Kruemmungsglied -1 in S2), sinkt der Betrag um
  etwa 17 / 9 / 4 / 2 % (N = 1000 / 2000 / 4000 / 8000). Das ist eine O(1/N)-Abhaengigkeit, ein schwaches Wachstum des
  Betrags mit N um hoechstens etwa 15 % von N = 1000 auf 4000; nicht das 4D-Muster (Wachstum etwa wie N).

**S4 Was in 2D von der Vorschrift uebrig bleibt [M].**
- Die P1-Steifigkeit ist in 2D vom Grad n - 2 = 0 in den Laengen: Die Kotangens-Gewichte haengen nur von den Winkeln
  jedes Dreiecks ab. Eine Skalierung je Simplex aendert K nicht. **Also Gamma(QI) = Gamma(CI) bis auf Rundung**, und
  rund Gamma_Q = Gamma_C (INDUZIERT-KUGEL-1, KH: 0,0) [P]. Die Volumenzuordnung je Simplex wirkt in 2D nur auf Gamma_M
  (Massenmatrix). Die Diagnose-Variante ohne Volumenzuordnung (CI) ist fuer Gamma identisch, fuer Gamma_M nicht.
- Moebius (M): Transport = exakte Moebius-Abbildung, Huelle kombinatorisch gleich (Moebius-Invarianz der leeren Kreise),
  Einbettung = runde Kugel, Sehnen = Sehnen der Originalpunkte (wie in 4D, dort Punkte gleich auf 4e-14). **Delta Gamma
  fuer M ist damit exakt null bis auf Rundung, fuer QI und CI.** Nur Gamma_M (QI) kann abweichen: Der g-Inhalt des
  Grosskreis-Dreiecks der Karte ist nicht der Inhalt des Bilddreiecks (Quelle des 4D-Rests -0,0017).
- Was 2D also prueft: Transport, Huelle in der konformen Karte, Einbettungssehnen (Winkel), Neuvernetzung und Paarung,
  den Code des Verformungszweigs. Das ist der Teil, den in 4D auch die CI-Lesart ohne Volumenzuordnung enthaelt; sie
  zeigte die Anomalie ebenfalls (Faktor 9,8 und 18,1) [P].
- Damit der 2D-Lauf derselbe Codepfad ist: generischer Code (n als Parameter, Ausdruecke wie kovarianz.py); Kontrolle
  K4D: mit n = 4 muss er kovarianz.py (live aufgerufen und aus dessen Laufdatei) wiedergeben.

**S5 Erwartung bei sauberer Vorschrift [M].**
- E[Delta Gamma] = E[Gamma(g_eps)] - E[Gamma(g0)] (Linearitaet des Erwartungswerts; die Paarung aendert nur das Rauschen).
- Die verschobenen Punkte sind exakt gleichverteilt bezueglich g (massstreue Abbildung einer Gleichverteilung), das Netz
  ist bis auf Glieder zweiter Ordnung in h grad sigma das Delaunay-Netz von g (ein Kreis der Karte ist in erster Ordnung
  ein verschobener g-Kreis), die Sehnen sind Abstaende in einer isometrischen Einbettung. Ist die Konstruktion so
  kovariant, ist E[Gamma(g_eps)] eine glatte, unter SO(3) symmetrische Funktion von eps; die erste Ableitung bei
  eps = 0 verschwindet, die Antwort ist fuer kleine eps quadratisch. Ein mit N wachsender Anteil oder eine in abs(eps)
  lineare Antwort ist nur bei nicht kovarianter Konstruktion oder einem Codefehler moeglich [M].
- Dasselbe Argument gilt in 4D; die 4D-Daten widersprechen ihm. Deshalb ist die Gegenprobe ueberhaupt aussagekraeftig.

**S6 Rauschen und Messbarkeit [M, ES].**
- Die Transportabbildung (nur theta verschoben) schert lokal: ln(Streckung theta / Streckung phi) = -2 eps sin^2 theta
  in erster Ordnung (quadratisches Mittel etwa 1,46 abs(eps)). Die Kotangens-Gewichte aendern sich damit in erster
  Ordnung mit zufaelligem Vorzeichen; erwartet Std(Delta Gamma) ~ c abs(eps) sqrt(N) mit c von der Ordnung 0,1 bis 1
  (Anhalt: INDUZIERT-DICHTE-2D, Std der Zweitdifferenz 144 bei N = 64 000 und S = 0,5) [ES].
- Das Polyakov-Signal ist N-unabhaengig und quadratisch: -0,0053 bei eps = -0,1. Signal/Rauschen je Saat dann etwa
  0,002 bis 0,02 bei N = 1000. **Der Betrag (KG3) und, bei sauberer Vorschrift, die Steigung (KG1) sind mit 100 bis 500
  Saaten voraussichtlich nicht entscheidbar** [ES]. Bei der groessten Amplitude (-0,4) waechst das Signal 16-fach, das
  Rauschen etwa 4-fach. Der Rauchlauf misst das Rauschen; der Plan legt danach Saatzahl, KG1-Amplituden und
  KG3-Amplitude fest.
- Trennschaerfe fuer das 4D-Muster: In 4D war Delta Gamma/N = -0,016 / -0,014 / -0,012 bei eps = -0,1. Dieselbe
  Groesse je Punkt waere in 2D Delta Gamma = -16 / -27 / -48 bei N = 1000 / 2000 / 4000, also viele Rausch-SE je Saat.
  Schon 1 % davon (-0,5 bei N = 4000) waere bei einer SE um 0,1 bis 0,2 sichtbar.

**S7 Kartenpunkte [K] (vor dem Rechnen).**
- **[K1]** Die Volumenzuordnung je Simplex wirkt in 2D nicht auf Gamma (S4). Die Diagnose-Variante ist fuer Gamma
  identisch (Kontrolle C5), aussagekraeftig nur fuer Gamma_M (Nebenlesart). Ein Fehler, der nur in der
  Volumenzuordnung steckt, kann sich in 2D-Gamma nicht zeigen.
- **[K2]** KG0 ist fuer Gamma vorab entschieden (exakt null, S4): Er kann nur durch Rundung oder ein falsches Netz
  scheitern, ist also eine Codekontrolle, kein Test. Die Gamma_M-Nebenlesart prueft die Volumenzuordnung.
- **[K3]** KG3 und (bei sauberer Vorschrift) KG1 sind voraussichtlich nicht entscheidbar (S6). Der Plan legt dafuer
  "nicht entschieden" bzw. "nicht auswertbar" fest. KG2 ist bei sauberer Vorschrift im Wortlaut "innerhalb 2 SE" fast
  sicher erfuellt, kann aber scheitern, wenn die Antwort mit N waechst; die Trennschaerfe wird berichtet.
- **[K4]** Das 2D-Netz ist relativ zur Kruemmung viel feiner als das 4D-Netz (h^2 K0 = 8 pi/N <= 0,025 gegen h^2 R ~ 1
  bis 2). Eine saubere 2D-Antwort schliesst Fehler aus, die nicht an der Grobheit haengen (Code, Transport, Huelle,
  Sehnen), aber keinen reinen Effekt des groben 4D-Netzes (Hypothese (a) in KOVARIANZ-KUGEL-1).
- **[K5]** Die 2D-Antwort ist Delta Gamma, nicht Delta Gamma/sqrt(N) (S1). KG2 wird in Delta Gamma geurteilt.
- **[K6]** "Polyakov-Vorhersage": KG3 gegen kappa_GROB Delta Gamma_P (Unterschied zu kappa = 1: 7,5 %, unter jedem
  erreichbaren Fehler); Delta Gamma_P (kappa = 1) wird mitberichtet.

## 2. Verformungen und Kontinuumsantworten (zweite Ordnung, von Hand) [M]

| X | Verformung | Delta Gamma_P (zweite Ordnung) | kappa_GROB Delta Gamma_P |
|---|---|---|---|
| M | sigma = -ln(cosh t + sinh t cos theta), t = 0,2 | 0 (exakt, alle Ordnungen) | 0 |
| K-0.025 | sigma = eps (1 - 3 cos^2 theta) + c, eps = -0,025 | -0,000333 | -0,000358 +- 0,000024 |
| K-0.05 | eps = -0,05 | -0,001333 | -0,001433 +- 0,000095 |
| K-0.1 | eps = -0,1 (Hauptamplitude, wie 4D) | -0,005333 | -0,00573 +- 0,00038 |
| K-0.2 | eps = -0,2 | -0,02133 | -0,0229 +- 0,0015 |
| K-0.4 | eps = -0,4 | -0,0853 | -0,0917 +- 0,0061 |
| K+0.05 | eps = +0,05 (Gegenvorzeichen, beschreibend) | -0,001333 | -0,001433 +- 0,000095 |

- Fuer eps > 1/12 ist das Profil nicht als Rotationsflaeche einbettbar (Kruemmung am Pol 1 - 12 eps < 0); deshalb
  negatives eps wie in 4D. Fuer eps = -0,4 ist die Einbettung moeglich (abs(s'/e^sigma) <= 1, am Pol gleich 1, innen hoechstens
  0,41), die Flaeche hat dann eine Taille mit negativer Kruemmung am Aequator [M]; Pruefung profil_min im vorab-Lauf.
- Exakte Werte (alle Ordnungen, mit c) in Abschnitt 4.

## 3. Was als saubere Antwort gilt

- M: Delta Gamma = 0 (Gamma, vorab entschieden). K: E[Delta Gamma] = kappa Delta Gamma_P, N-unabhaengig bis auf O(1/N)
  (S3), quadratisch in eps bis auf die exakten hoeheren Ordnungen (Abschnitt 4).
- Nicht sauber: ein Anteil, der mit N waechst (Aenderung von N = 1000 auf 4000 ueber 2 SE und ueber 10 %), oder eine
  Antwort, die mit abs(eps) etwa linear faellt.

## 4. Exakte Kontinuumswerte (vorab-Lauf, reine Quadratur) [E-v]

- Ergaenzt ab 2026-10-04 16:34:52 CEST (date). Quelle: kovarianz2d.py vorab (.69, Spur cpu, 14:34:15 bis 14:34:31 UTC,
  rc 0; rauch-69/vorab.json). Eindimensionale Quadratur (8192 Zellen, 10-Punkt-Gauss-Legendre) des Polyakov-Funktionals
  mit dem normierten sigma; keine Gitterrechnung, kein Gamma eines Netzes.

| X | c (Normierung) | profil_min | Delta Gamma_P (exakt) | zweite Ordnung | **pred = kappa_GROB Delta Gamma_P** | Scherung rms / max |
|---|---|---|---|---|---|---|
| M | 1e-16 | 0 | -2e-17 (exakt 0) | 0 | **0** | 5e-10 / 3e-8 |
| K-0.025 | -0,000505 | -2e-16 | -0,0003318 | -0,0003333 | **-0,000357 +- 0,000024** | 0,036 / 0,051 |
| K-0.05 | -0,002037 | -2e-16 | -0,0013210 | -0,0013333 | **-0,001420 +- 0,000094** | 0,073 / 0,104 |
| K-0.1 | -0,008284 | 2e-16 | -0,0052387 | -0,0053333 | **-0,00563 +- 0,00037** | 0,145 / 0,217 |
| K-0.2 | -0,034064 | 4e-16 | -0,020645 | -0,021333 | **-0,02219 +- 0,00147** | 0,284 / 0,468 |
| K-0.4 | -0,140503 | 0 | -0,081166 | -0,085333 | **-0,0873 +- 0,0058** | 0,516 / 1,081 |
| K+0.05 | -0,001961 | 0 | -0,0013464 | -0,0013333 | **-0,001447 +- 0,000096** | 0,073 / 0,096 |

- Proben: kleines eps (1e-3): Delta Gamma_P/eps^2 = -0,53343 gegen -8/15 (relativ 1,9e-4, dritte Ordnung); M: Polyakov-
  Funktional 8,9e-16 (exakt 0); M-Profil = Kreis auf 4,6e-15; Flaeche aller Verformungen 1 auf 3e-15; alle Profile
  einbettbar (profil_min >= -2,2e-16, Schwelle -1e-12).
- **Polyakov-Steigung (exakt, ln abs(Delta Gamma_P) gegen ln abs(eps)):** paarweise 1,993 / 1,988 / 1,979 / 1,975
  (-0,025/-0,05 bis -0,2/-0,4); Ausgleich ueber eps = -0,1, -0,2, -0,4: 1,977. Alle im KG1-Band 1,8 bis 2,2.
- Fehler der Vorhersage: nur aus kappa (6,6 %); Quadraturfehler < 1e-12. Mit kappa_DICHTE = 0,924 +- 0,087 ware jeder
  Wert um 14 % kleiner im Betrag; mit kappa = 1 gilt die Spalte "exakt".
- Gitterdispersion (S3, [H]): l = 2 hat k^2 = 0,0754 / 0,0377 / 0,0188 / 0,0094 (N = 1000 / 2000 / 4000 / 8000).
- Die Scherung der Transportabbildung (ln Streckungsverhaeltnis, flaechengewichtet) ist 1,45 abs(eps) bei kleinem eps,
  wie in S6 von Hand.
