# BETA-NETZ-V: zweite Ordnung (PPN beta) auf Finns gefuelltem Netz V (Versuch ohne Karte, Runde 37)

- Code-Agent fuer die Leitung claude-primary. Finn, 05.10.: einfach machen und ausprobieren. Kein Plan-Einfrieren, keine
  Vorhersagetabelle, kein frischer Leser.
- Zeiten (date; .69 in UTC, CEST = UTC + 2):
  - Start 2026-10-05 17:04:41 CEST.
  - Laeufe auf der .69 von 15:23:32 bis 15:50:02 UTC, alle rc = 0, alle ueber kleintest.sh (cpu8, cpu9, cpu10).
  - Text ab 17:43:12 CEST, Nachtrag 4.1 ab 17:50 CEST.
- Alles ist synthetische Gitterrechnung an einem gedachten periodischen Netz (numpy, 1 Thread). Keine Messdaten.
- Kennzeichen: [E] gerechnet, [M] eigene Herleitung, [L] Literatur aus dem Gedaechtnis, ungeprueft, [H] Hypothese,
  [N] nach Sicht auf Zahlen geschrieben.
- Einheiten: r in l_P (Finn-Kante). Staerke s: Quelle sigma = s an einer Ecke, Kopplung wie MATERIE-NETZ-1, Variante V1
  (q = 1/2). Je Einheitsquelle ist A = 0,05627 l_P der 1/r-Koeffizient von mu1, das Doppelte des dortigen A (andere
  Normierung). Netz V: 68 Kanten, 10 Ecken, 58 Tetraeder je Zelle.

## 1. Ergebnis zuerst

1. **Die volle nichtlineare Statik auf V ist geloest [E].** Grundlage sind exakte Diederwinkel, die Eckenregel R1 und ein
   Takt je Ecke.
   - Gerechnet bei vier Staerken (s = +-0,25, +-0,5; Takt an der Quelle 0,95 bzw. 0,89) auf L = 6 und L = 12.
   - Das Quasi-Newton-Verfahren konvergiert in 9 bis 12 Schritten auf eine Schrittweite unter 1e-13.
   - Der s^2-Anteil des Takts trifft die Stoerungsrechnung zweiter Ordnung auf 4,1e-6 (L = 6) bzw. 3,5e-6 (L = 12). Deshalb
     ist die zweite Ordnung fuer L = 16, 24, 32 per Stoerungsrechnung gerechnet.
   - Mit wachsender Staerke (L = 8, Nachtrag 4.1) konvergiert das Verfahren bei positiver Masse bis zum Takt 0,59 an der
     Quelle. Bei Takt 0,27 ist es nach 60 Schritten noch nicht fertig, aber noch fallend; bei s = -3,5 divergiert es.
2. **beta im Fernfeld: mit 1 vertraeglich [E].**
   - Gemessen ist die lokale Takt-Quelle zweiter Ordnung gegen Einsteins Wert, je Schale, auf unendliches Volumen
     extrapoliert (L = 16, 24, 32).
   - Ergebnis: beta(r) = 0,91 (r = 4,5), 0,94 (5,5), 0,96 (6,5), 0,98 (7,5 bis 9,5), 1,00 (10,5 bis 11,5). Ab r = 4,5
     stimmen alle drei Quellecken auf 0,01 ueberein.
   - Fuer r -> unendlich folgt beta = 1,00 bis 1,02, je nachdem ob man c/r^3 oder c/r^2 ansetzt.
   - Nahe der Masse liegt beta weit darunter: 0,58 bei 2,6 l_P, 0,85 bei 3,5 l_P.
3. **Einschraenkung: In den Eichrichtungen sind die Gittergleichungen bei zweiter Ordnung nicht erfuellbar [E].**
   - Den Rest M lam2 nimmt, wie in der KKT von mn.py, ein Multiplikator auf (gebrochene Verschiebungs-Invarianz). Er ist
     bei L = 16 und 24 an festem r gleich, gehoert also zum Gitter und nicht zum Torus.
   - Er faellt wie r^-3,0, die Quelle zweiter Ordnung selbst wie r^-4.
   - Punkt 2 nutzt die Takt-Quelle ohne diesen Eichanteil (Variante A). Mit ihm, also in der tatsaechlich geloesten
     KKT-Loesung (Variante B), ergibt sich beta = 0,95 +- 0,05 (Schalen 0,88 bis 1,05), ebenfalls mit 1 vertraeglich,
     aber fuenfmal unschaerfer.
4. **gamma = 1 in erster Ordnung ist eine Identitaet der isotropen Eichung [M, E: Abweichung 2,5e-16].**
   - Neu ist eine grosse Massenrenormierung: mu2 hat ein 1/r-Glied mit A2/A von ungefaehr 0,12 bis 0,17 je Einheit s
     (Fits instabil). Es ueberdeckt den beta-Anteil um mehr als das Zehnfache; deshalb tragen Fits von mu2 nicht.
   - Die raeumliche zweite Ordnung (delta) ist mit meiner Probe nicht bestimmbar. Die Schalenwerte bei L = 24 reichen von
     0,13 bis 1,77 (P0) und von -5,9 bis 4,4 (H0).
   - Ein nicht-konformer Rest der Laengen zweiter Ordnung liegt bei 0,5 bis 1,2 % von a2.
5. **Was aus dem Aufbau folgt und was gerechnet ist:**
   - Aus dem Aufbau [M, L]:
     - Die Gleichungen sind die Regge-Fassung der statischen Einstein-Gleichungen mit Takt: Summe N_v H_v entspricht dem
       Integral von N sqrt(g) R.
     - Konvergiert Regge im Kontinuum gegen Einstein (Wong 1971, Barrett/Williams 1988, Brewin/Jansen 2000 [L,
       ungeprueft]), ist beta = 1 im Fernfeld zu erwarten.
   - Gerechnet [E]:
     - Die Gitter-Nichtlinearitaet von V verdirbt das nicht. beta(r) naehert sich 1 von unten, etwa wie 1 - 10/r^3.
     - Das Nahfeld unter 4 l_P weicht stark ab.
     - Die Eichrichtungen sind bei zweiter Ordnung verletzt, und das klingt langsamer ab als die Quelle.

## 2. Was gerechnet wurde und wie N und Laengen nichtlinear geloest sind

- **Unbekannte:** Kantenlaengen l_e = l0_e (1 + a_e) auf dem L^3-Torus (a exakt, keine Linearisierung) und der Takt
  N_v = 1 + mu_v je Ecke.
- **Gleichungen** (code/bn.py, Netz.rest):
  - Zwang G_v = H_v(l) - sigma_v = 0 mit H_v = Summe ueber Kanten an v von l_e eps_e(l). eps_e = 2 pi - Summe der inneren
    Diederwinkel, exakt aus den sechs Laengen je Tetraeder.
  - Statik F_e = Summe_v N_v dH_v/dl_e = 0. Ruhende Materie haengt nicht von l ab.
  - Die Ableitungen der Diederwinkel stammen aus einem komplexen Schritt auf cos theta.
  - Skaliert: R_F = -(l0/2) F, linear gleich B a - q c mu, und R_G, linear gleich c^H a. B, c, M, W stammen aus ew.py
    und mn.py (unveraendert kopiert, sha256 wie in MATERIE-NETZ-1).
- **Eichung:** M^H (a + q W mu) = 0. Damit gilt in erster Ordnung exakt a1 = -q W mu1. Die flachen Eckpositionen sind
  dann isotrope Koordinaten, und nur so ist beta ablesbar.
  - In der Eichung M^H a = 0 aus mn.py gaebe es eine radiale Verschiebung von etwa -q A r-Dach [M]. Sie verschoebe beta
    um etwa 1/2.
  - Der Rest der Gleichungen in Eichrichtungen geht in M lam.
- **k = 0** wird in keiner Ordnung geloest; das entspricht einem neutralisierenden Hintergrund. Der Takt ist bis auf einen
  Faktor bestimmt, deshalb wird ln N verglichen.
- **Nichtlinear (Modus nl):**
  - Quasi-Newton mit der flachen KKT-Matrix, je k einmal invertiert. Start bei der linearen Loesung s x1.
  - Die Iteration loest R_F + M lam = 0, R_G = 0 und die Eichbedingung exakt fuer alle k ungleich 0.
  - mu2 = [mu(s) + mu(-s)]/(2 s^2), Richardson ueber s = 0,25 und 0,5.
- **Stoerungsrechnung (Modus pert):** Q2 = [R(+h x1) + R(-h x1)]/(2 h^2) aus dem exakten Rest (h = 0,01 und 0,02,
  Richardson), dann ein KKT-Solve.
- **beta-Probe (bn_quelle.py, bn_quelle2.py, bn_extra.py, bn_extra2.py) [M, N]:**
  - Der Takt-Operator P = -W^H B W vernichtet 1/r und Konstanten.
  - Isotrope ART im Vakuum: Lap n2 = (2 beta - 1) |grad n1|^2 und Lap(n1^2/2) = |grad n1|^2.
  - Je Schale also R = Summe Q P mu2 / Summe Q P(mu1^2/2) = 2 beta - 1.
  - Die Quelle von mu2 ist S = Q2G + W^H Q2F (Variante A) plus W^H M lam2 (Variante B, dort ohne den gleichmaessigen
    Torus-Anteil je Untergitter).
  - Torus: beta_roh = beta(r) + a y mit y = (4 pi/3) r^3/V (Kontinuum, fuehrende Ordnung), linear ueber L = 16, 24, 32
    extrapoliert (Rest <= 0,0016 fuer r >= 4,5).

## 3. Tabelle (Quelle P0; mu je Einheitsquelle, L = 24, Torus-normiert mit Mittel 0)

| r (l_P) | mu1 | mu2 | gamma | beta(r), A, P0 | A, C1 | A, H0 | beta(r), B, P0 |
|---|---|---|---|---|---|---|---|
| 2,6 | -0,01663 (2,76) | 0,002766 (2,76) | 1 (Identitaet) | 0,581 | 0,586 | 0,633 | 0,592 |
| 3,5 | -0,01135 (3,72) | 0,001858 (3,72) | 1 | 0,849 | 0,834 | 0,853 | 0,876 |
| 4,5 | -0,008148 (4,73) | 0,001327 (4,73) | 1 | 0,914 | 0,912 | 0,907 | 0,886 |
| 5,5 | -0,006052 (5,75) | 0,000981 (5,75) | 1 | 0,943 | 0,943 | 0,948 | 0,884 |
| 6,5 | -0,004616 (6,74) | 0,000746 (6,74) | 1 | 0,964 | 0,965 | 0,966 | 0,969 |
| 7,5 | -0,003553 (7,75) | 0,000573 (7,75) | 1 | 0,977 | 0,978 | 0,980 | 1,047 |
| 8,5 | - | - | 1 | 0,982 | - | - | 0,929 |
| 9,5 | -0,002114 (9,75) | 0,000339 (9,75) | 1 | 0,984 | - | - | 0,954 |
| 10,5 | - | - | 1 | 0,998 | - | - | 0,958 |
| 11,5 | -0,001206 (11,73) | 0,000194 (11,73) | 1 | 1,004 | - | - | 0,916 |
| r -> unendlich | | | | 1,003 (c/r^3), 1,015 (c/r^2) | 1,000 / 1,019 | 0,998 / 1,015 | 0,969 / 0,971 (Rest bis 0,10) |

- beta-Spalten: Schalen [r0; r0 + 1), r = Schalenmittel, auf L -> unendlich extrapoliert. C1 und H0 nur aus L = 16 und
  24, deshalb nur bis 7,5. Ab r = 8,5 stammt P0 nur aus L = 24 und 32.
- mu1 und mu2 stehen bei den Halbschalen-Mitteln in Klammern. mu2 ist vom 1/r-Glied (Massenrenormierung) und der Torus-
  Konstante beherrscht. Der beta-Anteil A^2/(2 r^2) liegt bei r = 4,7 nur bei etwa 7e-5 [M, Schreibtisch].
- Rohwerte ohne Torus-Extrapolation, P0, A: siehe lauf-69/extra.log. Bei r = 7,5 sind es 1,003 / 0,986 / 0,979 fuer
  L = 16 / 24 / 32.

## 4. Kontrollen [E]

| Kontrolle | Wert |
|---|---|
| Schlaefli an krummen Tetraedern, sum l dtheta/dl | 3,3e-16 relativ |
| flaches Netz: eps, R_F, R_G | 1,8e-15; 1,1e-15; 2,2e-15 |
| Linearisierung des exakten Rests gegen B, -q c, c^H aus ew.py (alle k, L = 6) | 2,5e-7 / 1,3e-7 (h^2-Fehler, h = 1e-4) |
| F = Gradient von Phi = Summe N_v H_v an krummen Konfigurationen (L = 4) | 2,6e-7 bis 6,2e-7 bei h = 1e-4, viermal so viel bei 2h |
| Euler: Summe l F = Summe N H | 6e-15 bis 2e-14 |
| a1 = -q W mu1 (isotrope Eichung); lam1 | 2,5e-16; 6,8e-15 |
| A je Einheitsquelle (L = 16 / 24) gegen 2 x 0,028135 aus MATERIE-NETZ-1 | 0,056294 / 0,0562696 |
| Q2: Richardson-Unterschied h gegen 2h | 3e-6 bis 1,2e-4 relativ |
| nichtlinear gegen Stoerung, mu2 (L = 6 / 12) | 4,1e-6 / 3,5e-6; eps^4-Anteil bei s = 0,5: 0,27 % |
| lam der nichtlinearen Loesung | 1,27e-5 (s = 0,25), 5,0e-5 (s = 0,5): waechst wie s^2 |
| Q P mu2 = S - Mittel(S) | 5e-15 bis 6e-15 |
| Torus-Extrapolation, Variante A | linear in 1/V, Rest <= 0,0016 fuer r >= 4,5 |

### 4.1 Nachtrag: wachsende Staerke (L = 8, nach Sicht, 15:46:45 bis 15:50:02 UTC) [E, N]

Quasi-Newton mit flacher KKT-Matrix, Start jeweils bei s x1, hoechstens 60 Schritte, Ziel Schrittweite unter 1e-13.

| s | Takt an der Quelle N | max a | Schritte | letzte Schrittweite | lam |
|---|---|---|---|---|---|
| +1 | 0,790 | 0,131 | 16 | 6,7e-14 | 2,0e-4 |
| -1 | 1,217 | 0,130 | 19 | 9,7e-14 | 2,1e-4 |
| +2 | 0,586 | 0,263 | 28 | 5,1e-14 | 8,0e-4 |
| -2 | 1,440 | 0,261 | 58 | 7,1e-14 | 8,9e-4 |
| +3,5 | 0,274 | 0,487 | 60 (nicht fertig) | 1,6e-9, faellt je Schritt um den Faktor 0,77 | 3,1e-3 |
| -3,5 | - | - | Abbruch nach Schritt 4 (Schrittweite 7,4, dann NaN) | - | - |

- U = A s/r bei r = 2 l_P [M, Kopf]: etwa 0,028 (s = 1), 0,056 (s = 2), 0,098 (s = 3,5).
- Bei s = 1 und 2 geben die Staerken mu2 nur noch auf 1,3e-3 (s^4-Anteil 1,6 % bzw. 6,4 %). Fuer beta sind deshalb die
  kleinen Staerken (L = 6, 12) und die Stoerungsrechnung massgeblich.
- Zahlen zur nachgearbeiteten Karte der Leitung (KARTE.md, 17:06:58, von mir nicht geaendert), ohne Urteil:
  - B1: gamma = 1 ist hier Identitaet der Eichung (2,5e-16), nicht gemessen.
  - B2: beta(r) liegt in Variante A bei 0,91 (r = 4,5), 0,94 (5,5), 0,96 (6,5) und 0,98 (7,5); in Variante B bei 0,88 bis
    1,05.
  - B3: Bei positiver Masse ist s = 2 bis 1e-13 konvergiert (U(2) etwa 0,056); s = 3,5 (U(2) etwa 0,1) ist nach 60
    Schritten bei 1,6e-9 und faellt noch; s = -3,5 divergiert.

## 5. Grenzen

1. **Die echte Gitterloesung ist nicht gerechnet.** Der Eichrest M lam2 sagt: Mit allen Gittergleichungen muesste die
   Verschiebung der Ecken (Pseudo-Eichung) schon in erster Ordnung von den Termen zweiter Ordnung festgelegt werden.
   - Das ist der bekannte Bruch der Verschiebungs-Invarianz bei gekruemmtem Regge (Bahr/Dittrich 2009 [L, ungeprueft]).
   - Varianten A und B behandeln diesen Rest verschieden und sind beide nur Naeherungen an die echte Gitterloesung.
   - Physikalisch heisst B: Die Ecken nahe der Masse brauchen aeussere Kraefte, um in isotropen Koordinaten zu bleiben.
     Ohne sie wuerden sie sich verschieben [H].
2. **beta ist nur lokal gemessen** (Takt-Quelle je Schale), nicht ueber Bahnen. Die Periheldrehung ist daraus nur ueber
   (2 + 2 gamma - beta)/3 erschlossen [L]. Es gibt keine Shift und keine Dynamik.
3. **Torus:** Die Korrektur ist Kontinuum in fuehrender Ordnung. Variante B haengt staerker an L, als die Korrektur
   erfasst, und hat deshalb Schalenschwankungen bis 0,1.
4. Es gibt nur Punktquellen an drei Eckarten und nur V mit Takt-Kopplung V1 (q = 1/2), keinen Q-Ball und kein S.
5. Die raeumliche zweite Ordnung (delta) ist nicht bestimmt. Der nicht-konforme Rest von a2 waechst relativ zu a2 nach
   aussen (0,55 % bei r = 2,5, 1,2 % bei 11,5). Bei festem r steigt er mit L leicht (L = 16 gegen 24: +9 bis +13 %); die
   Ursache ist offen.
6. Das Nahfeld (r < 4 l_P) weicht stark ab. Was ein Planet dort saehe, ist mit dieser Probe nicht beantwortet.

## 6. Regelabweichungen und Selbstanzeigen

1. **/dev/null:** Beim Start der ersten drei Hauptlaeufe (17:25 CEST) habe ich auf der .69 die nohup-Ausgabe nach /dev/null
   umgeleitet. Die Laufprotokolle selbst stehen in lauf/*.log. Danach habe ich in Dateien im Arbeitsordner umgeleitet.
2. **jq mit Rechnung zur Anzeige:** Auf der .69 habe ich jq mehrfach rechnen lassen, zum Beispiel mu2 r^2, nu2 r, SM/n und
   Rundungen. Meine Deutung von SM als Torus-Anteil stuetzte sich zuerst darauf; bestaetigt ist sie in bn_auswertung.py und
   bn_quelle2.py (Python auf der .69). Lokal habe ich jq nur lesend benutzt.
3. **Nach Sicht geschrieben [N]:**
   - bn_test2.py, bn_quelle.py, bn_auswertung.py, bn_extra.py, bn_quelle2.py und bn_extra2.py entstanden nach Sicht auf
     die ersten Zahlen.
   - Die beta-Probe ersetzt die in bn.py eingebauten Fits, weil diese instabil waren (beta - 1 je nach Band zwischen -1
     und +24).
   - Varianten A und B sowie die Torus-Formel sind nach Sicht festgelegt.
4. **Zahlen per Hand (im Kopf, nicht per Skript):**
   - A^2/(2 r^2) bei r = 4,7 und A2/A (Spanne aus den Fitkoeffizienten 0,0065 bis 0,0093)
   - die Abfall-Exponenten r^-3,0 (M lam2, Schalen [2; 3) bis [11; 12)), r^-4 (Q2F) und r^-2,04 (lam2)
   - die Prozentwerte des nicht-konformen Rests (Abschnitt 5) und "fuenfmal unschaerfer"
   - Alle anderen Zahlen stammen aus den Laeufen.
5. **Plattenvorfall .69 (17:07 bis 17:08 CEST):** Er betrifft diesen Versuch nicht. Der erste Upload war um 17:23 CEST,
   alle Uploads per sha256 verglichen, neue Skripte unter neuem Namen und dann mv. code/, lauf/ und rauch/ (46 Dateien)
   bestehen lokal sha256sum -c (PRUEFSUMMEN-lokal.txt). Waehrend der Laeufe waren 18 GB frei.
6. **Grenzen der Laeufe:** Der laengste Lauf brauchte 318 s (quelle-L32), der groesste Speicher war 0,54 GB (pert-L24).
   Kein Lauf kam ueber 10 min.

## 7. Einfach gesagt

Wir haben eine ruhende Masse in Finns gefuelltes Netz gesetzt und diesmal auch die zweite Ordnung ausgerechnet, also wie
die Uhr langsamer geht, wenn die Masse doppelt so stark wirkt. Einstein sagt dafuer einen ganz bestimmten Wert (beta = 1),
und das Netz kommt ab etwa sechs Kantenlaengen Abstand auf wenige Prozent und ab etwa zehn Kantenlaengen auf ein Prozent
daran heran. Ganz nah an der Masse weicht das Netz deutlich ab, und die Ecken dort muessten sich eigentlich ein wenig
verschieben; diese Verschiebung haben wir noch nicht ausgerechnet.

## 8. Dateien

- code/: bn.py (Hauptcode: test, pert, nl), bn_test2.py (Gradientenprobe), bn_quelle.py und bn_quelle2.py (lokale
  beta-Probe), bn_auswertung.py, bn_extra.py, bn_extra2.py (Extrapolation); ew.py, mn.py, tp.py unveraendert aus
  MATERIE-NETZ-1 (sha256 fa7b6417..., b36984d3..., 419d7da6...).
- rauch-69/: test-L6, pert-L6, nl-L6, test2-L4 (json und log).
- lauf-69/: pert-L16, pert-L24, nl-L12, nl-L8-stark, quelle-L16/24/32, quelle2-L16/24/32, auswertung*, extra, extra2 (json
  und log).
- KARTE.md: von der Leitung nachgearbeitet (17:06:58 CEST), von mir nicht geaendert.
- PRUEFSUMMEN-69.txt (auf der .69 erzeugt), PRUEFSUMMEN-lokal.txt (lokale Pfade).
- Auf der .69: /home/fmh/fmhc-physics-remote/beta-netz-v/ (code/, rauch/, lauf/).
- Journal, Peerbus und Commit uebernimmt die Leitung.
