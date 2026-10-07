# INDUZIERT-DICHTE-2D: Plan (Code-Agent, Runde 38)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 07:07:51 CEST (date). Code ab 07:23:07 CEST, Plantext ab
  07:34:23 CEST (date).
- **Vor diesem Plantext gerechnet:** Rauchlaeufe r1 bis r4, kontrolle-r1/-r2 und Probe p1 (Abschnitt 11). Sie zeigten
  schon Werte der Messgroesse (N = 16 000, 10 Rauchsaaten). Das steht offen in Abschnitt 11. Vorhersagen und
  Schwellen der Karte sind davon unberuehrt.
- **Grundlage:**
  - KARTE.md: ID0 bis ID3 mit Schwellen unveraendert uebernommen.
  - INDUZIERT-ZUFALL-2D: code/zufall2d.py unveraendert kopiert (sha256 37a0fe8f...). Benutzt werden daraus Netz,
    Kotangens-Laplace, log det' per Erdung und duenner LU, zufallsnetz (Kontrolle K2), zweite (Richardson).
  - induziert.py unveraendert kopiert (sha256 b3867eac...), nur weil zufall2d.py es fuer seine Kontrollen importiert.
  - INDUZIERT-1 Teil A: Polyakov-Bezug, Flaechenglied (K1 dort).
- **Kennzeichen:**
  - [M] eigene Mathematik
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [F] Festlegung dieses Plans (von der Karte offen gelassen)
  - [K] Kartenpunkt (Fehler oder Lesart der Karte, vor dem Einfrieren offengelegt)
  - [H] Hypothese

## 1. Geometrie und Kopplung (gemeinsame Zufallszahlen)

- **Torus** [0, L)^2 in Koordinaten, L = sqrt(N), Metrik g = e^(2 sigma) delta mit sigma = s cos(k.x),
  k = 2 pi kint/L (kint ganzzahlig).
- **Grundpunkte** z_i: N gleichverteilte Punkte, Saat numpy default_rng([20261004, N, saat]) wie INDUZIERT-ZUFALL-2D.
  Gleiche Saat heisst also gleiche Grundpunkte wie dort (fuer ID0 gewollt).
- **Abbildung psi_s [M]:**
  - Phase phi = k.z mod 2 pi. Gesucht phi' mit Phi_s(phi') = phi, wobei
    Phi_s(t) = (1/I0(2s)) int_0^t e^(2 s cos u) du = t + sum_m 2 I_m(2s)/(m I0(2s)) sin(m t) (30 Glieder).
  - Newton bis abs(Schritt) < 1e-14; Bildpunkt x = z + khat (phi' - phi)/abs(k) (mod L). Die Querkoordinate bleibt.
  - Die Bildpunkte sind exakt unabhaengig mit Koordinatendichte e^(2 sigma(x))/I0(2s) verteilt: physikalisch
    gleichverteilt, Dichte N/A_g mit A_g = A I0(2s).
  - Damit ist jede Differenz in s erwartungstreu: E_z[Gamma(psi_s(z), s)] ist genau der Ensemble-Mittelwert bei s,
    fuer jedes s.
- **Punktzahl [F, K2]:** N bleibt fest (Binomialprozess, wie INDUZIERT-ZUFALL-2D). Siehe Abschnitt 10 zum
  Flaechenglied.
- **Kontrolle K1:** Newton-Residuum, Momente <e^(-2 sigma)> = 1/I0(2s) und <cos(k.x)> = I1(2s)/I0(2s) als z-Wert,
  KS-Abstand, Querkoordinate unveraendert. Fuer s = +-0,25 und +-0,5, kint = (2,0) und (3,3), N = 64 000.

## 2. Netz und Laengen

- **Netz [Karte]:** Delaunay der Bildpunkte in Koordinaten (Qhull).
  - Periodisch ueber Randstreifen der Breite 8 aus den 8 Nachbarkopien statt aller 9 Kopien (Laufzeit).
  - Behalten werden die Dreiecke mit Schwerpunkt im Grundbereich; Ecken modulo N, Orientierung positiv.
  - Kontrolle K2: Dreiecksmenge gleich der 9-Kopien-Fassung aus zufall2d.py (Grundpunkte N = 4 000 und 16 000) und
    gleich einer 9-Kopien-Triangulierung der Bildpunkte bei s = 0,5.
- **Physikalische Kantenlaengen (geo) [M, F]:** Geodaete zweiter Ordnung um den Kantenmittelpunkt m:
  - log l = log abs(d) + sigma(m) + [b + a^2 - (d x grad sigma(m))^2]/24
  - mit a = d.grad sigma(m) und b = (d.grad)^2 sigma(m).
  - Das ist das Linienintegral von e^sigma (Glieder b und a^2) minus die Verkuerzung durch die Kruemmung des Weges
    (Querglied).
  - Mittelpunktsregel und Eckenregel e^((sigma_i + sigma_j)/2) unterscheiden sich davon in zweiter Ordnung in l.
  - Kontrolle K3: Vergleich mit numerisch minimierter Weglaenge (Zwei-Parameter-Kurvenschar, Gauss-Legendre 64) auf
    60 Zufallskanten mit abs(s) k l bis 0,5.
- **Abweichung vom Delaunay in der physikalischen Metrik (Karte: "Abweichung offenlegen"):**
  - Je Auswertung werden gezaehlt: Kanten mit negativem Kotangens-Gewicht aus physikalischen Laengen, deren Summe,
    neue Kanten gegenueber dem Netz bei s = 0.
  - Beschreibend gerechnet wird zusaetzlich die Variante intr. Sie kippt Kanten mit negativem Gewicht, wenn die andere
    Diagonale (Laenge aus der Metrik) ein groesseres Gewicht hat.
  - Ohne diese Bedingung pendeln Vierecke, deren Kruemmungsdefekt groesser ist als ihr Abstand vom Kozirkularen
    (Rauchlauf r1, Abschnitt 11).
- **Materie und log det' (wie INDUZIERT-ZUFALL-2D):**
  - K = Kotangens-Laplace aus den physikalischen Laengen, Gamma = 1/2 log det' K, det' K = N det K_(0)
  - LU mit U_ii > 0 und perm_r = perm_c je Aufruf
  - K ist die P1-Steifigkeit, also auch bei einzelnen negativen Gewichten positiv semidefinit.
  - Kontrolle K4: LU gegen dichte slogdet und Eigenwerte auf Bildnetzen N = 400 (koord und intr, s = 0,5).

## 3. Differenzenschema [F, K1]

- **Je Saat, Richtung und k:** D(S) = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/S^2 mit S = 0,5 (Urteil). Dabei ist
  Gamma(+-S) jeweils mit eigenem Delaunay-Netz der Bildpunkte psi_(+-S)(z) gerechnet.
  - Gamma(0) ist das Netz der Grundpunkte; es ist bei allen k derselbe Wert.
  - Messgroesse y = D/A mit A = L^2 = N (physikalische Flaeche bei s = 0).
- **Warum grosses S und nicht "kleines s0" (Abschnitt 10, K1):**
  - Gamma(s) ist je Stichprobe stetig, hat aber an jedem Kantenkippen einen Knick.
  - Kippen geschieht schon bei winzigen s: 2 neue Kanten bei s = 1e-4, 212 bei 0,01, 9 300 von 48 000 bei 0,5
    (N = 16 000). Die Rate ist etwa N je Einheit s und haengt nicht von k ab (K5).
  - Die Knicke sind kein Fehler, sondern der Mechanismus, ueber den das neu vernetzte Ensemble die Scherung abbaut.
    Ohne sie misst man die Scher-Steifigkeit des festen Netzes (Gamma'' ~ 0,7 A, also ~ 0,7/k^2 in c).
  - Die Differenz ist fuer jedes S erwartungstreu (Abschnitt 1). Ihr Rauschen faellt wie S^(-1/2), denn die Knicke
    addieren sich wie eine zusammengesetzte Poisson-Folge.
  - Rauchlauf r2 (Abschnitt 11): Streuung je Saat bei S = 0,25 etwa 2,6-mal groesser als bei S = 0,5.
  - Glieder hoeherer Ordnung in S: Ein kovariantes Ensemble hat keine k^2-Glieder in s^4 (Polyakov ist exakt
    quadratisch in sigma) [M, H]. k-unabhaengige s^4-Anteile gehen in den Achsenabschnitt a (Abschnitt 4).
  - S = 0,25 bei N = 16 000 wird beschreibend mitgerechnet (Gang mit S).
- **Rundung:** LU auf ~1e-15 relativ (K4). Das gibt in D(0,5) bei Gamma ~ 4,5e4 hoechstens ~1e-9 absolut,
  vernachlaessigbar gegen das Saatrauschen (~1e2 in D).

## 4. Flaechenglied und Messgroesse [F]

- Ein Flaechenglied (kosmologische Konstante) ist in Gamma'' unabhaengig von k: Gamma'' = 2 lambda A + c k^2 A + ...
  Also gilt y = a + c k^2 + O(k^4).
- **Regel (vor dem Einfrieren festgelegt):**
  - Je Saat werden y(n) ueber die beiden Achsenrichtungen 0 und 90 Grad gemittelt.
  - Dann kleinste Quadrate y(n) = a + c k_n^2 ueber n = 2, 4, 8, 12 (N = 64 000; abs(k) = 0,0497 / 0,0993 / 0,199 /
    0,298) bzw. n = 1, 2, 4, 6 (N = 16 000; dieselben abs(k)).
  - Die Steifigkeit pro Flaeche und k^2 nach Abzug des Flaechenglieds ist c.
  - Saatmittel c und Standardfehler SE = Std(c je Saat, ddof 1)/sqrt(M).
  - Der Fit je Saat entfernt auch den gemeinsamen Versatz durch Gamma(0) (gleich fuer alle k einer Saat).
- **Beschreibend:**
  - a (Flaechenglied)
  - c mit a = 0 erzwungen
  - Fit a + c k^2 + d k^4
  - c je k: (y - a)/k^2
  - je Richtung getrennt
  - N = 16 000 mit S = 0,5 und 0,25
  - intr gegen koord auf eigenen Saaten
- **Kartenwortlaut "kleinstes k":** c_kmin = (y(n_min) - a)/k_min^2 je Saat (abs(k) = 0,0497), Saatmittel und SE.
  Wird mit derselben Regel wie ID1 beurteilt und mitberichtet (Abschnitt 10, K3).

## 5. Vorhersagen der Karte (unveraendert)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| ID0 | Kontrolle: Variante "feste Punkte" gibt c_P = +0,159 auf 2 % wieder | 85 % |
| ID1 | [H] Mit Streuung nach physikalischer Flaeche liegt die konforme Steifigkeit (Saatmittel, kleinstes k, N = 64 000) innerhalb 30 % von -1/(24 pi) | 35 % |
| ID2 | Das Ergebnis mit Streuung nach Flaeche unterscheidet sich von +0,159 um mehr als 3 Standardfehler | 70 % |
| ID3 | [H] Das Vorzeichen der konformen Steifigkeit ist negativ (wie Polyakov) | 50 % |

## 6. Urteilsregeln (mechanisch durch code/dichte_auswertung.py nach lauf-69/auswertung.json)

- **Tor [F].** Gilt eines nicht, sind ID1 bis ID3 "nicht auswertbar":
  - (a) Jedes Netz (Grundnetz und jedes Bildnetz) erfuellt: V - E + F = 0, E = 3N, F = 2N, jede Kante in genau zwei
    Dreiecken, Orientierung > 0, Koordinatenflaeche = L^2 auf 1e-9, alle physikalischen Dreiecksflaechen > 0,
    laengste Kante < L/4.
  - (a, Fortsetzung) Grundnetz Delaunay; jede LU mit U_ii > 0 und perm_r = perm_c; Newton-Residuum von psi <= 1e-12.
  - (b) K1: Residuum <= 1e-12 und alle Momenten-z-Werte <= 4. K2: alle Dreiecksmengen gleich. K3: Laengenformel
    gegen numerische Geodaete <= 1e-3 relativ. K4: LU gegen dicht <= 1e-9 relativ.
- **ID0 [F]:**
  - Feste Grundpunkte, festes Delaunay-Netz bei s = 0, nur die Kantenlaengen aendern sich (geo-Regel, wie im
    Hauptlauf).
  - c = Gamma''/(k^2 A) per Richardson mit h = 0,01 (wie INDUZIERT-ZUFALL-2D), N = 64 000, n = 2 (abs(k) = 0,0497),
    Mittel ueber 0 und 90 Grad je Saat, dann Saatmittel ueber die Saaten 0 bis 2.
  - Eingetroffen, wenn abs(c/0,159 - 1) <= 0,02.
  - Ohne Flaechenglied-Abzug: Auf festem Netz gibt es keins (INDUZIERT-1 K1).
  - Mitberichtet: Eckenregel (identisch zur Konvention von INDUZIERT-ZUFALL-2D; gleiche Saaten, also je Saat
    vergleichbar), Mittelpunktsregel, S-Schema bei S = 0,5 auf festem Netz.
- **Hauptgroesse:** c (Abschnitt 4) bei N = 64 000, S = 0,5, Netz koord, Saaten 0 bis 65.
- **Unterscheidbarkeit (Brief):**
  - Gilt SE > (0,159 + 1/(24 pi))/3 = 0,0574, so erlaubt das Rauschen die Unterscheidung zwischen +0,159 und -0,013
    nicht.
  - Dann sind ID1 bis ID3 "nicht auswertbar", mit Abschaetzung der noetigen Saaten.
- **ID1 [F: Rauschregel; Schwelle der Karte]:** Band B = [1,3 P; 0,7 P] mit P = -1/(24 pi), also
  [-0,01724; -0,00928].
  - Eingetroffen: c in B und SE <= 0,3 abs(P) = 0,00398.
  - Nicht eingetroffen: Abstand von c zu B > 2 SE.
  - Sonst nicht auswertbar.
  - Mitberichtet: noetige Saatzahl fuer SE = 0,3 abs(P)/2; Kartenwortlaut c_kmin mit derselben Regel.
- **ID2:** Eingetroffen, wenn abs(c - 0,159)/SE > 3, sonst nicht eingetroffen.
- **ID3 [F: Rauschregel]:**
  - Eingetroffen, wenn c + 2 SE < 0.
  - Nicht eingetroffen, wenn c - 2 SE > 0.
  - Sonst nicht auswertbar.
  - Kartenwortlaut (Vorzeichen des Saatmittels allein) wird mitberichtet.
- **Abbruch:** Fehlen Saaten, wird mit den fertigen geurteilt (offengelegt). Unter 16 Saaten bei N = 64 000 sind ID1
  bis ID3 "nicht auswertbar".

## 7. Kontrollen

- K1 bis K4 wie oben.
- **K5:** Kantenkippen gegen s ohne LU, Saat 990, N = 16 000 und 64 000, abs(k) = 0,05 / 0,1 / 0,2 / 0,3,
  s = 1e-4 bis 0,5. Gezaehlt: neue Kanten (koord), negative Gewichte, Kippungen und Rest in intr.
- **ID0** selbst ist die Kontrolle "feste Punkte". Je Saat soll die Eckenregel die Werte aus INDUZIERT-ZUFALL-2D
  wiedergeben (Saaten 0 bis 2, N = 64 000, n = 2; dort lauf-69/zufall-N64000-s0.json).
- **Laufend:** Netz-, LU- und Newton-Pruefungen in jedem Netz (Tor a).

## 8. Laeufe

- .69, /home/fmh/fmhc-physics-remote/runde38-induziert-dichte/ (code/, rauch/, lauf/), nur ueber kleintest.sh, Spuren
  cpu3 und cpu4, hoechstens zwei zugleich, nacheinander je Spur. Jeder Lauf schreibt nach jeder Saat.
- **cpu3:**
  - kontrolle (K5 bei N = 16 000 und 64 000)
  - fest N = 64 000 Saaten 0 bis 2 (n = 2, 4, 8, 12; 0 und 90 Grad)
  - dichte N = 64 000 Saaten 0 bis 10, 22 bis 32 und 44 bis 54
  - dichte N = 16 000 Saaten 32 bis 63
- **cpu4:**
  - dichte N = 64 000 Saaten 11 bis 21, 33 bis 43 und 55 bis 65
  - dichte N = 16 000 Saaten 0 bis 31
  - intr N = 16 000 Saaten 100 bis 115 (S = 0,5, beide Varianten)
- **Einstellungen:** N = 64 000 mit S = 0,5; N = 16 000 mit S = 0,25 und 0,5. Richtungen 0 und 90 Grad.
- **Laufzeit (gemessen, Abschnitt 11):** N = 64 000 etwa 2,0 s je Bildnetz, 32 s je Saat; N = 16 000 0,4 s
  bzw. 13 s je Saat.
- **Danach:** dichte_auswertung.py lauf lauf/auswertung.json.

## 9. Agenten-Vorhersagen (nach den Rauchlaeufen, vor den Hauptlaeufen)

Die Rauchlaeufe zeigten c bei N = 16 000 (Abschnitt 11). A4 ist deshalb keine echte Vorhersage mehr.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Tor besteht | 95 % |
| A2 | ID0 eingetroffen; die Eckenregel trifft die Werte aus INDUZIERT-ZUFALL-2D je Saat auf <= 1e-9 relativ | 90 % |
| A3 | [M] Achsenabschnitt a ist mit 0 vertraeglich (abs(a) <= 3 SE): Bei fester Punktzahl ist K skaleninvariant, ein Flaechenglied gibt es dann nicht | 80 % |
| A4 | c (N = 64 000) liegt zwischen -0,03 und +0,01 (absehbar aus r2) | - |
| A5 | N = 16 000: S = 0,25 und S = 0,5 geben c im Rahmen von 2 SE gleich | 75 % |
| A6 | intr und koord unterscheiden sich in c um weniger als 0,2 SE | 85 % |
| A7 | Die Saatstreuung von c faellt von N = 16 000 nach 64 000 um einen Faktor 1,5 bis 3 | 65 % |

## 10. Kartenpunkte (vor dem Einfrieren offengelegt)

- **[K1] "s0 so klein, dass wenige Kanten kippen" (Brief):**
  - Wenige Kippungen heisst s0 <~ 1e-4 bei N = 16 000 (2 Kippungen) und noch kleiner bei 64 000.
  - Dann misst die Differenz die Scher-Steifigkeit des festen Netzes plus seltene, sehr grosse Knickbeitraege. Die
    Varianz waechst wie 1/s0 (Abschnitt 3).
  - Deshalb gilt S = 0,5 mit vielen Kippungen; die Kopplung bleibt erwartungstreu.
  - Nach Brief-Wortlaut ("wenige kippen") waere das Ergebnis bei vertretbarem Aufwand nicht auswertbar. Gerechnet ist
    das nicht.
- **[K2] Flaechenglied und Punktzahl:**
  - Die Karte sagt: "Bei fester physikalischer Dichte bleibt die Punktzahl im Mittel konstant." Genau genommen
    waechst sie bei fester Dichte mit A_g = A I0(2s) = A (1 + s^2 + ...).
  - Hier bleibt N fest; die Dichte sinkt global um den Faktor 1/I0(2s).
  - Weil die Kotangens-Gewichte nur von Winkeln abhaengen, ist Gamma = 1/2 log det' K unter globaler Streckung exakt
    invariant. Eine globale Dichteaenderung wirkt also nicht.
  - [M, H] Im Kontinuum mit dichtegebundenem Abschneiden fallen das kosmologische Glied (~ N) und log A_g ganz heraus.
    Erwartet ist a = 0 (A3).
  - Die Regel der Karte (Abzug per Ausgleich ueber k) wird trotzdem angewandt; a bleibt frei.
- **[K3] "kleinstes k" (ID1):**
  - Nach Abzug eines k-unabhaengigen Glieds gibt es keinen Einzelwert bei einem k. Die Steifigkeit ist die Steigung
    ueber das Fenster, das beim kleinsten k beginnt.
  - Das Kipprauschen in Gamma'' haengt nicht von k ab. Das Signal waechst wie k^2.
  - Der Einzelwert beim kleinsten k ist deshalb rund 30-mal verrauschter als die Steigung (Probe p1:
    SE 0,12 gegen 0,007 bei 10 Saaten).
  - Kartenwortlaut c_kmin wird mitberichtet und mit derselben Regel geurteilt; erwartet: nicht auswertbar.
- **[K4] "Poisson-Punkte":** Gerechnet wird mit fester Zahl (Binomialprozess, wie INDUZIERT-ZUFALL-2D). Eine
  schwankende Zahl wuerde gemeinsame Zufallszahlen fuer verschiedene s unmoeglich machen.
- **[K5] Delaunay in Koordinaten:**
  - Die Abweichung vom physikalischen Delaunay ist klein. Negative Gewichte: im Mittel 0,07 %, hoechstens 0,3 % der
    Kanten (Probe p1).
  - Die Variante intr aendert y um <= 3e-5 bei einem Saatrauschen von ~2e-3 (r4).
  - Keine Berichtigung: Geurteilt wird nach Kartenwortlaut (koord), intr ist beschreibend.
- **Kein Kartenfehler,** der ein Urteil der Karte veraendern wuerde, ausser [K1] (betrifft nur das Schema) und [K3]
  (Lesart von "kleinstes k"; beide Lesarten werden berichtet).

## 11. Rauchlaeufe (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC; Rauchsaaten >= 900, nicht in den Hauptlaeufen)

- **kontrolle-r1** (05:25:40 bis 05:27:22, cpu3, rc 0):
  - K1: Residuum 8,9e-16; z-Werte <= 0,34; KS * sqrt(N) = 1,09 bzw. 0,75 (bei allen s gleich, wie es sein muss:
    psi bildet die Grundphasen exakt ab).
  - K2 gleich (N = 4 000, 16 000; Gamma auf 10 Stellen gleich).
  - K3: geo <= 2,4e-4, Mittelpunkt <= 1,2e-2, Ecken <= 1,1e-2 (abs(s) k l bis 0,51).
  - K4 <= 3,4e-13 absolut.
  - K5 (koord): 2 / 16 / 212 / 2 206 / 9 330 neue Kanten bei s = 1e-4 / 1e-3 / 1e-2 / 0,1 / 0,5 (N = 16 000, E = 48 000),
    fast gleich fuer alle k. Negative Gewichte bis 122 (0,25 %) bei abs(k) = 0,3, s = 0,5.
- **dichte-r1** (05:25:42 bis ~05:28, cpu4; N = 16 000, Saaten 900 und 901, S = 0,25 und 0,5, nur 0 Grad):
  - **Fehler gefunden:** Die erste Fassung von intr kippte jede negative Kante bedingungslos. 80 Durchgaenge
    pendelten zwischen beiden Diagonalen (Kruemmungsdefekt groesser als der Abstand vom Kozirkularen).
  - Berichtigt: nur kippen, wenn die andere Diagonale ein groesseres Gewicht hat; intr nur noch beschreibend.
  - Gesehene Werte y: Saat 900 S = 0,5: 0,0044 / 0,0030 / 0,0051 / -0,0005 (abs(k) 0,05 bis 0,3); Saat 901:
    -0,0002 / 0,0010 / 0,0002 / 0,0017.
- **dichte-r2** (05:31:04 bis 05:33:20, cpu3; N = 16 000, Saaten 902 bis 911, beide Achsen, S = 0,25 und 0,5,
  koord): 13 s je Saat.
- **dichte-r3** (05:33:20 bis 05:34:27, cpu3; N = 64 000, Saaten 900 und 901, S = 0,5): 2,0 s je Bildnetz, 31,8 und 34,4 s je Saat; y in
  Saat 900 zwischen -0,0032 und -0,0010, in Saat 901 zwischen -0,0027 und +0,0012 (gesehen, nicht ausgewertet).
- **dichte-r4** (05:31:06 bis 05:31:17, cpu4; N = 16 000, Saaten 912 und 913, intr): 2 bis 59 Kippungen je Netz,
  Rest negativ 3 bis 106; y_intr - y_koord <= 3,4e-5.
- **kontrolle-r2** (05:31:17 bis 05:31:42, cpu4): wie r1, intr ohne Pendeln.
- **Probe p1** der Auswertung (05:33:32 bis 05:33:36, cpu4; r2 als N = 16 000, r4 als intr):
  - Tor bestanden.
  - **Gesehen:** N = 16 000, S = 0,5, 10 Rauchsaaten: c = -0,0093 +- 0,0067 (Std je Saat 0,021), a = -0,0011 +- 0,0008.
    S = 0,25: c = -0,011 +- 0,018. c_kmin = -0,09 +- 0,12. c mit a = 0: -0,025 +- 0,010.
  - Das liegt nahe bei Polyakov (-0,0133) und weit weg von +0,159. Damit ist ID2 absehbar eingetroffen. Fuer ID1 und
    ID3 entscheidet der Hauptlauf bei N = 64 000.
- **Zeitfolge der Festlegungen:**
  - Die Schwellen sind die der Karte. Die Rauschregeln (2 SE bei ID1 und ID3, Unterscheidbarkeit nach Brief), die
    Fit-Regel (Abschnitt 4), S = 0,5 und die Saatzahlen standen im Auswertungscode fest, bevor ich die Werte aus
    Probe p1 sah.
  - S = 0,5 hatte ich nach r1 und r2 gewaehlt (Rauschen und Kippen), also nachdem ich die y-Werte aus r1 gesehen hatte.
  - Die Saatzahl 66 bei N = 64 000 folgt aus der Laufzeit (r3) und der Streuung (p1).
