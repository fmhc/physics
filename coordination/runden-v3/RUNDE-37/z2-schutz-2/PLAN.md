# Z2-SCHUTZ-2: Plan (Runde 49; Barriere 360 -> 0 Grad: Kerngroesse oder Netzgroesse?)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-05 14:12:49 CEST (date). Plantext ab 14:23:51 CEST (date),
  vor Code und Rauchtest. Zeitbox 120 min ab Start, also bis 16:12:49 CEST.
- Karte: KARTE.md (ZT0 bis ZT3, unveraendert). Festlegungen [F] machen die Karte rechenbar; Zusaetze sind als
  **Zusatz** markiert und nicht urteilsbildend.
- Kennzeichen: [M] Mathematik; [E] Rechnung im Modell; [L] Literatur oder Gedaechtnis; [H] Hypothese; [F] Festlegung
  dieses Plans; [R] im Rauchtest gesehen; [P] Projektdatei. Alles ist eine synthetische Modellrechnung an einem
  Modellfeld, keine Messdatenbestaetigung.
- Vorwissen [P]: Z2-SCHUTZ-1 (PLAN, ERGEBNIS, code/, lauf-69/, nachtrag-69/). Bezugswert fuer ZT0: B(G1) = 25,028515686495666
  (CI-NEB, lauf-69/weg-haupt-r10-R20-neb.json); Bisektion dort 25,03391253168411; E_S(G1) = 4545,313250942401.

## 0. Vorab (Schreibtisch, vor jeder Rechnung)

1. **Was an der Bisektion von Z2-SCHUTZ-1 falsch war [P, M]:** Klasse "S" hiess "ab Schritt 30 keine Bindung mit
   c <= 0". Das hat zwei Fehler. (a) Der Familienzustand X(lambda) hat fuer lambda unter etwa 0,45 noch keine
   gesprungene Bindung; eine Bahn, die erst nach Schritt 30 springt, galt schon bei Schritt 30 als "S" (G3: lambda =
   0,375 bei Schritt 30 mit Knotenkraft 5,3 als "S" gezaehlt). (b) Eine Bahn, die S in anderer Hebung erreicht (einzelne
   Knoten q -> -q, gleiche Energie), hat Bindungen mit c < 0 und blieb "offen"; die Bisektion brach ab (G2, G3).
2. **Ebene Invarianz [M]:** Startzustand S, Familie X(lambda) und das Endfeld T liegen in der Ebene q = cos(psi) +
   k sin(psi) (k = z-Einheitsquaternion). Der Gradient von E = Summe 4(1 - (q_a . q_b)^2) eines ebenen Feldes ist eben,
   die Tangentialprojektion und die Normierung erhalten die Ebene. Die Bisektionsbahnen von Z2-SCHUTZ-1 waren daher
   bis auf Rundung eben. In psi gilt c_b = cos(psi_a - psi_b), E = Summe 4 sin^2(psi_a - psi_b),
   dE/dpsi_a = Summe 4 sin(2(psi_a - psi_b)). Das ist das SO(2)-Modell in phi = 2 psi; der Kern hat psi = pi, der Rand 0.
   Eichung: psi und psi + pi sind dasselbe SO(3)-Feld.
3. **Abstand zu S, eichinvariant [M]:** D(psi) := max ueber freie Knoten von sin^2(psi_i - psi_S,i) = max (1 - (q_i . q_S,i)^2).
   D = 0 genau dann, wenn jeder Knoten bis aufs Vorzeichen bei S ist (jede Hebung). In der Ebene gibt es keine
   Symmetrie-Nullmode (die zwei Nullmoden von S drehen die Drillachse aus der Ebene heraus).
4. **Entwurfsgrund fuer das Raster [M, H nicht urteilsbildend]:** Die Verdrillung am Kernrand ist bei harmonischem Profil
   g = 2 pi R / (r0 (R - r0)) (Drehwinkel je Laenge). Bei fester Kugel R = 24 ist g symmetrisch unter r0 <-> R - r0
   (r0 = 8: 1,18; 10: 1,08; 12: 1,05; 14: 1,08), die Kernoberflaeche waechst dagegen wie r0^2. Bei festem Kern r0 = 10
   faellt g mit R (R = 20: 1,26; 24: 1,08; 28: 0,98; 32: 0,91). Zahlen zur Barriere gebe ich nicht vorab.
5. **Dimensionen (AGENTS.md):** innere Symmetrie SO(3) (Feld), gerechnet in der ebenen Untermannigfaltigkeit (Bisektion)
   und im vollen SO(3)^N (Start, Hesse, CI-NEB mit Rauschen aus der Ebene); Raum: 3D-Diamant-Graph, keine Uebertragung
   auf 1D oder 2D.

## 1. Code [F]

- Ordner code/: unveraenderte Kopien aus Z2-SCHUTZ-1/code: finn.py, guertel2.py, guertel.py, stab.py, z2.py (Hashes wie
  dort eingefroren). **Neu:** code/z2s2.py (importiert z2 und finn; nur die geaenderten Teile) und
  code/auswertung_z2s2.py. Damit ist jede Aenderung als eigene Datei sichtbar.
- **Aenderung 1, Abbruchkriterium der Bisektion:** neue Klassenregel (Abschnitt 3), "offen" erst nach 1500 Schritten.
- **Aenderung 2, Relaxation fuer grosse Kugeln:** Bisektionsbahnen und Freigabe in der ebenen Darstellung psi
  (Abschnitt 0.2): gleiche FIRE-Arithmetik wie finn.fire_feld (dtstart 0,02, dtmax 0,1, alpha 0,1, Faktoren 1,1 / 0,5 /
  0,99, Nmin 5, Schrittdeckel 0,05 je Knoten), aber ein Skalar je Knoten statt vier Komponenten. Grund: Z2-SCHUTZ-1 brauchte
  auf (14, 28) etwa 0,078 s je FIRE-Schritt; Bisektion, Freigabe und CI-NEB passten nicht in 10 min. Mathematisch
  derselbe Fluss bis auf Terme der Ordnung (Schritt)^2 (Quaternion-FIRE normiert q + dx und projiziert v; psi-FIRE addiert
  dpsi = dx). Pruefung: Konsistenzprobe im Rauchtest (Abschnitt 8) und ZT0 auf G1.
- **Aenderung 3, Freigabe bis zur Ruhe:** Die Freigabe laeuft bis T (E < 1e-3) oder bis zur Ruhe in einem Zwischenminimum
  (groesste Knotenkraft <= 1e-6 bei E >= 1e-3), hoechstens 30000 Schritte oder Wandzeit. Ein Zwischenminimum wird
  erkannt und gemeldet (Abschnitt 6).
- **Aenderung 4, Hesse von S im Startlauf:** Start (Kopie von z2.modus_start, Quaternion-FIRE bis Knotenkraft 1e-7) und
  danach die vier kleinsten Eigenwerte der Riemannschen Hesse-Matrix von S (z2.hesse_matrix, z2.eigen_klein,
  z2.symmetriemoden unveraendert) in demselben Lauf. Kein Hesse-Lauf fuer Sattel und T (Z2-SCHUTZ-1: Laufzeitgrenze).
- **Unveraendert:** Netz und Energie (finn.Netz), Startprofil, Kappenfamilie, CI-NEB (z2.wegrechnung mit Eichung),
  Lokalisierung (z2.lokalisierung, ergaenzt um L10).

## 2. Netz, Raster und Zustaende [F]

- **Netz:** finn.Netz("diamant", r0, R), Zellkante 2, Bindungslaenge 0,866, Kern r <= r0 fest auf q = -1 (360 Grad),
  Rand r > R fest auf +1, Profil h harmonisch 3D.
- **Raster:**
  - Kern fest r0 = 10: R = 20 (G1), 24, 28, 32 (ZT0, ZT1).
  - Kugel fest R = 24: r0 = 8, 10, 12 (G2), 14 (ZT2). (10, 24) gehoert zu beiden Reihen.
  - Sieben Groessen: (10, 20), (10, 24), (10, 28), (10, 32), (8, 24), (12, 24), (14, 24).
- **Start S:** q = cos(pi h) + k sin(pi h), Kern und Rand gesetzt (finn.Netz.setze, 360 Grad), kein Rauschen, finn.fire_feld
  in Bloecken bis Knotenkraft <= 1e-7, nmax 20000. E_S := E am Ende (Quaternion). psi_S := atan2(q_3, q_0).
- **Ende T:** alle freien Knoten +1. E(T) = 0 = globales Minimum, weil E >= 0 [M]; keine Rechnung noetig.

## 3. Verfahren A: Bisektion auf der Trennflaeche, korrigiert [F]

- **Familie (unveraendert):** psi_i(lambda) = psi_S,i (1 - lambda w_i), w_i = clip((30 Grad + 30 Grad - gamma_i)/30 Grad,
  0, 1), gamma_i = Winkel zwischen Ort und n_P = (0,92; 0,33; 0,21) normiert. Kern und Rand bleiben fest.
- **Bahn:** psi-FIRE (Abschnitt 1) ab psi(lambda). Je Schritt Klasse pruefen:
  - **"T"**, sobald E < E_S - 1 (wie Z2-SCHUTZ-1);
  - **"S"**, sobald Schritt >= 30 und D(psi) <= 1e-3 (Abschnitt 0.3; zurueck bei S in irgendeiner Hebung);
  - **"M"**, sobald Schritt >= 30 und groesste Knotenkraft <= 1e-9 (Ruhe in einem Gleichgewicht, das weder S noch T ist;
    Festlegung nach Rauchtest 3 [R]: auf (11, 22) endeten zwei Bahnen nach 1500 Schritten in Ruhe, Knotenkraft 2e-14,
    D = 0,999, also weder S noch T; 600 Schritte Ruhe schliessen einen Sattel aus). "M" zaehlt in der Bisektion wie "T"
    als Nicht-S-Seite; die Bisektion sucht damit den Rand des Beckens von S (Austrittssattel);
  - **"offen"** nach 1500 Schritten ohne Klasse oder sobald 78 % des Laufbudgets verbraucht sind (Rest fuer die
    Freigabe).
- **Ablauf Stufe 1:** zuerst lambda = 1 (muss "T" oder "M" sein), dann bis zu 14 Halbierungen auf [0, 1], solange die
  Wandzeit unter 45 % des Laufbudgets liegt. Bei "offen" endet die Bisektion; die Klammer bis dahin bleibt.
- **Stufe 2, Nachschaerfen (edge tracking; Festlegung nach Rauchtest 2 [R]):** Auf (9, 18) kamen die Klammerbahnen nach 14
  Halbierungen dem Sattel nur bis zur groessten Knotenkraft 0,14 (S-Seite) bzw. 0,29 (T-Seite) nahe (gleiche Werte wie
  Rauchtest 7c von Z2-SCHUTZ-1). Darum: Familie Y(mu) = (1 - mu) psi_a + mu psi_b zwischen den Zustaenden kleinster Kraft
  der letzten S-Bahn (psi_a) und der letzten T-Bahn (psi_b) von Stufe 1; Bahnen und Klassen wie oben (FIRE neu mit
  Geschwindigkeit 0); erst mu = 1 (muss "T" oder "M" sein) und mu = 0 (muss "S" sein), dann bis zu 12 Halbierungen,
  solange die Wandzeit unter 55 % des Budgets liegt. **Stufe 2 gilt**, wenn beide Enden passen, mindestens 6 Halbierungen
  klassifiziert sind und die letzte obere und untere Bahn den Sattelbereich erreichen; dann ersetzen ihre Bahnen die von
  Stufe 1 (Sattelnaeherung, Endzustand fuer Freigabe und CI-NEB). Sonst bleibt Stufe 1. Grundlage [L]: Skufca, Yorke,
  Eckhardt 2006; Schneider, Eckhardt, Yorke 2007 (Neustart der Bisektion zwischen den Klammerbahnen), aus dem Gedaechtnis.
  Rauchtest 3 [R]: auf (9, 18) sank die kleinste Knotenkraft so auf 0,0018 (T-Seite) und 0,0037 (S-Seite).
- **Sattelbereich ohne Ruhe:** Zustaende mit groesster Knotenkraft <= 1e-6 zaehlen nicht zum Sattelbereich (Festlegung
  nach Rauchtest 4 [R]). Bei Bahnen der Klasse "M" ist der Zustand kleinster Kraft trotzdem meist die Annaeherung an das
  Zwischenminimum (Energie unter dem Sattel); die Sattelenergie kommt dann ueber das Maximum aus der Gegenseite. Eine
  Regel "erster Durchgang" (Suche endet, wenn die Kraft das Minimum um den Faktor 5 uebersteigt) habe ich in Rauchtest 6
  probiert und verworfen: auf (9, 18) stiegen die kleinsten Kraefte damit von 0,002 auf 0,17 (Code-Parameter anstieg = inf).
- **Stufe 3, Zwischenminimum am Rand (Festlegung nach Rauchtest 4 und 5 [R]):** Ist die letzte obere Bahn nach Stufe 1/2
  von Klasse "M" (Gleichgewicht M), fuehrt der Austrittssattel nicht direkt nach T. Dann wird der Rand des Beckens von T
  gesucht: Familie Y(mu) = (1 - mu) psi_M + mu psi_Te, psi_M = Ruhezustand jener Bahn, psi_Te = Endzustand (E < E_S - 1)
  der T-Bahn mit kleinstem lambda aus Stufe 1; oben "T", unten "S" oder "M"; erst mu = 1 und mu = 0, dann bis zu
  14 Halbierungen (bis 65 % des Budgets), danach Nachschaerfen wie Stufe 2 (oben "T", unten "S" oder "M", bis 72 %).
  Gilt mit mindestens 6 Halbierungen. (Der erste Entwurf mit der Kappenfamilie zwischen lambda_M und lambda_T lief in
  Rauchtest 5 nicht nah an einen zweiten Sattel.) Endet die letzte untere Bahn in S, ist der Weg S -> Sattel 2 -> T und
  B_A := E(Sattel 2) - E_S. Endet sie in demselben M (D zu M <= 1e-3), ist der Weg S -> Sattel 1 -> M -> Sattel 2 -> T und
  B_A := max(E(Sattel 1), E(Sattel 2)) - E_S. Sonst ist A ungueltig. Freigabe dann ab dem Ende der letzten T-Bahn von Stufe 3.
- **Zeitanteile des Bisektionslaufs:** Stufe 1 bis 45 %, Stufe 2 bis 55 %, Stufe 3 bis 65 %, Stufe 3b bis 72 %, jede Bahn
  endet spaetestens bei 78 % ("offen"), Freigabe bis 100 %.
- **Sattelnaeherung:** je Bahn der Zustand kleinster groesster Knotenkraft ab Schritt 30 **im Sattelbereich D(psi) >= 0,5**
  (Festlegung nach Rauchtest 1 [R]: mit der neuen S-Regel laeuft eine S-Bahn bis nahe S, und ohne diese Grenze war der
  Zustand kleinster Kraft das Bahnende bei S statt der Durchgang am Sattel. Am Sattel aus Z2-SCHUTZ-1 haben Kernbindungen
  c <= 0 [P]; der freie Knoten einer solchen Bindung dreht gegen S um mindestens 90 Grad minus den Bindungswinkel von S
  (<= 36 Grad), also D >= 0,66 [M]. Eine Bahn, die den Sattelbereich ab Schritt 30 nie erreicht, liefert keine
  Sattelnaeherung.)
  Ohne Stufe 3: **B_A := max(E_fmin(letzte obere Bahn), E_fmin(letzte untere Bahn)) - E_S**; "Sattel A" ist der
  fmin-Zustand mit der hoeheren Energie (mit Stufe 3 siehe dort).
- **Freigabe (Aenderung 3):** ab dem Endzustand der letzten oberen Bahn (ohne Stufe 3) bzw. der letzten T-Bahn von Stufe 3
  psi-FIRE bis T, Zwischenminimum, 30000 Schritte oder Wandzeit; laufendes E-Maximum wird gemeldet.
- **Gueltig A**, wenn: lambda = 1 ist "T" oder "M"; beide Seiten kommen vor; mindestens 10 Halbierungen (Stufe 1); der Weg
  ist belegt (ohne Stufe 3 immer, mit Stufe 3 wie dort); die letzten oberen und unteren Bahnen jeder benutzten Sattelstufe
  erreichen den Sattelbereich ab Schritt 30; **Genauigkeit:** deren kleinste Knotenkraft ist <= 0,05 (Z2-SCHUTZ-1 auf G1:
  0,025 und 0,0054); die Freigabe erreicht T und bleibt dabei unter E_S; S ist gueltig (Abschnitt 6).

## 4. Verfahren B: CI-NEB (unveraendert aus Z2-SCHUTZ-1) [F]

- Anfangsweg S -> Sattel-Naeherung untere Seite -> Sattel-Naeherung obere Seite -> Endzustand der letzten Bahn, die zur
  Freigabe fuehrt (als Quaternionen aus der Bisektion; mit Stufe 3 und Weg ueber M: S -> Sattel 1 unten -> Sattel 1 oben -> M
  -> Sattel 2 unten -> Sattel 2 oben -> Ende), auf M + 2 = 8 Bilder gleicher Bogenlaenge (g2.reparam_feld), innere Bilder mit Rauschen aus der Ebene
  (finn.rauschen, sigma 1e-3, Saat [49, 1, R]); z2.wegrechnung mit Eichung, Klettern ab Iteration 50, Konvergenz bei Kraft
  des Kletterbildes < 5e-3 (Bandkraft-Grenze 1,0), nmax 6000, Budget 480 s.
- **B_B := E_Kletterbild - E_S.** **Gueltig B**, wenn konvergiert und geklettert, S gueltig und die Freigabe aus A T
  erreicht (der Endpunkt des Bandes ist mit T verbunden).
- **Kontrolle K-Weg (beschreibend wie Z2-SCHUTZ-1):** |B_A - B_B| / min(B_A, B_B) <= 0,05, wenn beide gueltig.

## 5. Barriere und Lokalisierung [F]

- **Barriere je Groesse:** B(G) := Minimum ueber die gueltigen Verfahren (wie Z2-SCHUTZ-1; die Karte fragt nach der
  kleinsten Barriere). Grenze [M]: ein Keimort (n_P), eine Kappenfamilie; obere Abschaetzung der kleinsten Barriere.
- **Lokalisierung (ZT3):** Delta_b = e_b(Sattel) - e_b(S), e_b = 4(1 - c_b^2); Summe aller Delta_b = Barriere des Sattels.
  **L10 := (Summe der 10 groessten Delta_b) / (Summe aller Delta_b).** Beschreibend: n50, L6, groesstes Delta_b, Radius
  und Winkel zu n_P dieser Bindung, Zahl der Bindungen mit c <= 0 am Sattel (Hebung von S), Anteil der Kernbindungen.

## 6. Gueltigkeit, Endpunkte, Zwischenminima [F]

- **S gueltig**, wenn der Start konvergiert (Knotenkraft <= 1e-7) und K-Hesse besteht: lambda_1, lambda_2 in [-1e-5, 1e-5],
  lambda_3 > 1e-4 und der Raum der zwei kleinsten Eigenvektoren enthaelt die zwei Drehungen der Drillachse zu mindestens
  0,99 (wie Z2-SCHUTZ-1). Damit ist S ein echtes Minimum bis auf die zwei Symmetrie-Nullmoden.
- **T** ist das globale Minimum (E = 0) [M].
- **Zwischenminimum:** Endet die Freigabe in Ruhe bei E >= 1e-3 (oder ist die letzte Nicht-S-Bahn von Klasse "M"; dann
  beginnt die Freigabe schon in Ruhe), heisst die Groesse "Zwischenminimum" (E_M, Zahl der gesprungenen Bindungen
  beschreibend). A und B sind dann fuer die Barriere 360 -> 0 **ungueltig**; der Wert B_A gilt nur beschreibend als
  Austrittsbarriere aus S. Erreicht die Freigabe weder T noch Ruhe, ist die Groesse ebenfalls ungueltig. Bahnen der Klasse
  "M" weiter weg vom Rand machen eine Groesse nicht ungueltig, wenn die letzte Nicht-S-Bahn nach T fuehrt (der Weg
  S -> Sattel -> T ist dann belegt); ihre Zahl wird gemeldet.

## 7. Urteilsregeln [F] (mechanisch in code/auswertung_z2s2.py)

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| ZT0 | G1: A und B gueltig und je \|B_X / 25,028515686495666 - 1\| <= 1e-3 | G1: B_A und B_B vorhanden (Klammer bzw. Kletterbild) und je \|B_X / 25,03 - 1\| <= 1e-3 |
| ZT1 | B(10, 20) gueltig; mindestens eine der Groessen (10, 28), (10, 32) gueltig; eingetroffen, wenn fuer alle gueltigen R in {24, 28, 32} gilt \|B(10, R)/B(10, 20) - 1\| < 0,10, sonst nicht eingetroffen | B(10, 20) und B(10, R*) gueltig, R* = 28, falls gueltig, sonst 32; eingetroffen, wenn \|B(10, R*)/B(10, 20) - 1\| < 0,10 |
| ZT2 | R = 24, gueltige r0 aus {8, 10, 12, 14}, mindestens drei; p = Steigung der Ausgleichsgeraden ln B gegen ln r0; eingetroffen, wenn 1,5 <= p <= 2,5 und B mit r0 streng waechst | wie Plan, aber nur 1,5 <= p <= 2,5 |
| ZT3 | jede gueltige Groesse (mindestens drei): L10 >= 0,5 am Sattel jedes gueltigen Verfahrens | jede gueltige Groesse (mindestens eine): L10 >= 0,5 am Sattel des Verfahrens, das B(G) liefert |

- Fehlen die verlangten gueltigen Werte, lautet das Urteil "nicht auswertbar". In ZT1 gilt "nicht eingetroffen" schon,
  wenn B(10, 20) gueltig ist und eine gueltige Groesse ausserhalb 10 % liegt.
- Beschreibend: Bisektionsschritte (lambda, Klasse, Schritte, kleinste Kraft), Energieprofil des CI-NEB, Freigabe,
  E_S, Austrittsbarrieren ungueltiger Groessen, lokale Exponenten zwischen Nachbarradien.

## 8. Rauchtests [F]

- Nur auf (6, 12), (9, 18) und (11, 22) (nicht im Raster) und als Laufzeitprobe auf (10, 32) (Modus pruef, 20 Schritte am
  ungerelaxten Profil); je Lauf <= 120 s. ((11, 22) kam nach Rauchtest 2 dazu, als Groesse nahe am Raster.)
- **Konsistenzprobe (Modus pruef):** auf X(0,5) von (9, 18): relative Differenz der Energie psi gegen Quaternion, groesste
  Differenz der Knotenkraefte, und 60 Schritte psi-FIRE gegen Quaternion-FIRE (z2.fire_klasse-Arithmetik): groesste
  Abweichung in psi. Erwartet: Energie und Kraft auf Rundung, Bahnen bis auf kleine Abweichungen gleich.
- Ich sehe nur Klassen, Schrittzahlen, Kraefte, Laufzeiten, Ja/Nein-Felder und die Konsistenzdifferenzen an; keine
  Energie- oder Barrierenwerte.

## 9. Laufplan [F]

- Nur .69, ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu und cpu7, je Lauf <= 10 min
  (RuntimeMaxSec 600), 1 Thread. Ordner /home/fmh/fmhc-physics-remote/z2-schutz-2/ (code/, rauch*/, lauf/, nachtrag*/).
- Je Groesse drei Laeufe: start (FIRE + Hesse S, Budget 540 s fuer FIRE), bisekt (A + Freigabe, Budget 540 s; Stufe 1 bis
  50 %, Stufe 2 bis 65 %, Bahnen bis 75 %, Freigabe bis 100 %), weg (B, Budget 480 s).
- **cpu:** (10, 32) start, bisekt; (10, 28) start, bisekt, weg; (10, 32) weg.
- **cpu7:** (10, 20), (10, 24), (8, 24), (12, 24), (14, 24) je start, bisekt, weg; dann warten auf cpu und Auswertung.
- Der Startlauf schreibt vor der Hesse-Rechnung eine vorlaeufige JSON (ohne Hesse); laeuft die Hesse-Rechnung in die
  Grenze, gilt S als nicht geprueft (ungueltig).
- Eingefrorener Code, je Lauf genau einmal. Bricht ein Lauf ab, kann er als markierter Nachtrag laufen (beschreibend);
  urteilsbildend bleibt der eingefrorene Ablauf.

## Rauchtests und Festlegungen vor dem Einfrieren [R]

- Alle auf der .69 (Uhr dort UTC; CEST = UTC + 2), je Lauf <= 120 s, nur (6, 12), (9, 18), (11, 22) und die Laufzeitprobe
  (10, 32) im Modus pruef. Angesehen: rc, Klassen, Schrittzahlen, Kraefte, Abstaende D, Laufzeiten, Ja/Nein-Felder und die
  Konsistenzdifferenzen; keine Energie- oder Barrierenwerte (Ausnahme in ERGEBNIS.md angezeigt: L10 und n50 auf (9, 18) in
  Rauchtest 1 mit ausgegeben).
- **Rauchtest 1 (12:29 bis 12:30 UTC):** alle Modi rc = 0 ausser weg (6, 12) (rc = 1: keine Klammer, keine npz; auf
  (6, 12) kehrt schon lambda = 1 nach S zurueck, Hesse-Ueberlapp 0,11 / 0,54). Konsistenz psi gegen Quaternion auf (9, 18):
  Energie 2e-16 relativ, Kraft 8e-15, Querkraft 9e-15; nach 60 FIRE-Schritten groesste Abweichung |sin dpsi| = 9e-4, Energie
  1,5e-5 relativ (Terme der Ordnung Schritt^2). Laufzeit je Schritt (10, 32): psi 0,015 s, Quaternion 0,10 s.
  (9, 18): 14 Halbierungen, Freigabe erreicht T, CI-NEB konvergiert (165 Iterationen); Befund: S-Bahnen hatten ihren
  Zustand kleinster Kraft am Bahnende bei S -> Sattelbereich D >= 0,5.
- **Rauchtest 2 (12:33 UTC):** mit Sattelbereich kleinste Kraefte 0,29 (T) und 0,14 (S) nach 14 Halbierungen -> Stufe 2.
- **Rauchtest 3 (12:36 bis 12:39 UTC):** (9, 18) mit Stufe 2: 0,0018 / 0,0037, CI-NEB 102 Iterationen. (11, 22): Start
  konvergiert, Hesse besteht (Ueberlapp 1,000); eine Bahn je Stufe endete "offen" in Ruhe (Kraft 2e-14, D = 0,999) ->
  Klasse "M".
- **Rauchtest 4 (12:42 UTC):** (11, 22) mit Klasse "M": letzte obere Bahn "M", Freigabe beginnt in Ruhe, A ungueltig wie
  geplant; Befund: fmin der M-Bahnen war das Zwischenminimum selbst -> Ruhegrenze 1e-6 und Stufe 3.
- **Rauchtest 5 (12:46 bis 12:49 UTC):** (11, 22) Stufe 3 in der Kappenfamilie: T-Bahnen blieben bei kleinster Kraft 0,14,
  M-Bahnen knapp ueber der Ruhegrenze -> erster Durchgang (Faktor 5) und Stufe 3 auf der Strecke M -> T-Bahnende.
  CI-NEB (11, 22) nach 100 s nicht konvergiert (Rauchbudget). Auswertung laeuft (rc = 0, ohne Rasterdateien alles
  "nicht auswertbar").
- **Rauchtest 6 (12:51 bis 12:54 UTC):** Regel "erster Durchgang" (Faktor 5): (9, 18) nur noch 0,17 / 0,17 -> verworfen.
  (11, 22) Stufe 3 auf der Strecke M -> T-Bahnende: 14 Halbierungen, kleinste Kraefte 0,0005 (T) und 0,0014 (M);
  Stufe 3b nur 4 Halbierungen; die letzte untere Bahn endete in einem anderen Gleichgewicht als M (D > 1e-3), Weg damit
  nach Regel nicht belegt. CI-NEB (11, 22) mit sieben Wegpunkten nach 100 s nicht konvergiert.
- **Rauchtest 7 (12:55 bis 12:58 UTC, eingefrorene Fassung bis auf diesen Plantext):** (9, 18) wieder 0,0018 / 0,0037,
  A gueltig, CI-NEB 102 Iterationen. (11, 22): Austrittssattel genau (0,0064 auf der S-Seite), Stufe 3a genau (0,0005 auf
  der T-Seite), aber die untere Bahn endet in einem anderen Gleichgewicht als M; A dort nach Regel ungueltig
  (Austrittsbarriere nur beschreibend). Folgerung fuer die Hauptlaeufe: Groessen mit solchen Zwischenminima koennen
  ungueltig werden; das ist so gewollt und wird gemeldet.
