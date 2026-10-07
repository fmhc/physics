# INDUZIERT-DICHTE-2D-GROB: Plan (Code-Agent, Runde 38)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 09:01:24 CEST (date). Code ab 09:11:37 CEST, Plantext ab
  09:17:30 CEST (date).
- **Vor diesem Plantext gerechnet** (Abschnitt 10): Rauchlaeufe (b) mit den Saaten 0 und 1, Skalenprobe (a) mit den
  Saaten 0 und 1 (nur n = 2 und 4), Vergleich mit dem Hauptlauf, ein synthetischer Selbsttest und eine Probe der
  Auswertung auf Kopien des Hauptlaufs. Neue Werte bei grossem k (n = 8, 12 im Lauf a) habe ich vor dem Einfrieren
  nicht gerechnet und nicht gesehen.
- **Grundlage:** KARTE.md (IG0 bis IG3 mit Schwellen unveraendert), RUNDE-37/induziert-dichte-2d/ (PLAN.md eingefroren
  20261004-073639, code/, lauf-69/auswertung.json), gegenlesen/GEGENLESEN.md.
- **Kennzeichen:** [M] eigene Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [S] an der Quelle gelesen,
  [F] Festlegung dieses Plans (von der Karte offen gelassen), [K] Kartenpunkt, [H] Hypothese.

## 1. Code

- **Kopie:** code/dichte2d_grob.py aus induziert-dichte-2d/code/dichte2d.py.eingefroren-20261004-073639 (sha256
  8f3a4deb...). zufall2d.py und induziert.py unveraendert kopiert (sha256 37a0fe8f... und b3867eac...).
- **Aenderung** (vollstaendig in code/AENDERUNG.diff, 4 Stellen):
  - Modus dichte bekommt die Option A=<Torusflaeche>; L = sqrt(A). Ohne Option gilt A = N, also L = sqrt N wie
    eingefroren.
  - grundpunkte(N, saat, L) und Flaeche A = L^2 in y = D/A statt fest N.
  - **Randstreifen [K2]:** RAND = 8 gilt in mittleren Abstaenden (rand = 8 L/sqrt N). Bei L = sqrt N ist das genau 8,
    der eingefrorene Wert.
  - Kopf-Kommentar. Sonst nichts geaendert: S, Abbildung psi, Delaunay, Laengenformel, log det', Pruefungen.
- **Auswertung:** code/grob_auswertung.py (neu). Tor-Pruefungen und eingefrorene Fit-Regel woertlich aus
  dichte_auswertung.py uebernommen; neu sind der gemeinsame Ausgleich (Abschnitt 4), der Bitvergleich und der
  Selbsttest.

## 2. Einheiten und Skalengleichheit [M]

- **Netzabstand** eps = L/sqrt N = sqrt(A/N). Hauptlauf: eps = 1 (L = sqrt N). Lauf (a): N = 16 000, L = sqrt(64 000),
  also eps = 2.
- **Umrechnung (festgelegt):** k_eps = abs(k) eps; y_eps = Gamma''/N = y_koord A/N; x = k_eps^2.
  - Mit y_koord = a_k + c k^2 + d_k k^4 folgt y_eps = a_eps + c x + d x^2 mit a_eps = eps^2 a_k, c unveraendert,
    d = d_k/eps^2.
  - c ist dimensionslos und in beiden Einheiten gleich. d und a gelten ab hier in Netzabstands-Einheiten.
- **k-Werte (Torus-Einheiten wie der Hauptlauf N = 64 000):**

| Lauf | N | L | eps | n | abs(k) (Koordinaten) | k eps | x = (k eps)^2 |
|---|---|---|---|---|---|---|---|
| M64 (Hauptlauf) | 64 000 | 252,98 | 1 | 2, 4, 8, 12 | 0,0497 / 0,0993 / 0,1987 / 0,2980 | dieselben | 0,00247 / 0,00987 / 0,0395 / 0,0888 |
| M16 (Hauptlauf) | 16 000 | 126,49 | 1 | 1, 2, 4, 6 | 0,0497 / 0,0993 / 0,1987 / 0,2980 | dieselben | dieselben |
| (a) G | 16 000 | 252,98 | 2 | 2, 4, 8, 12 | 0,0497 / 0,0993 / 0,1987 / 0,2980 | 0,0993 / 0,1987 / 0,3974 / 0,5961 | 0,00987 / 0,0395 / 0,1579 / 0,3553 |
| (b) B | 16 000 | 126,49 | 1 | 1, 2, 4, 6 | wie M16 | wie M16 | wie M16 |

- **Skalengleichheit [M]:** Kotangens-Gewichte haengen nur von Winkeln ab. Laengenformel, psi und Delaunay sind
  skalenkovariant.
  - Alles haengt also nur von N, n (k eps = 2 pi n/sqrt N), S und der Saat ab. Lauf (a) ist in exakter Arithmetik
    gleich N = 16 000, L = sqrt N mit n = 2, 4, 8, 12.
  - Bei L = 2 sqrt(16 000) skalieren alle Zwischenwerte mit Zweierpotenzen. Zu erwarten ist daher sogar
    Bitgleichheit. Rauchprobe: bestaetigt (Abschnitt 10).
  - Folge: Die "groebere Dichte" ist rechnerisch dasselbe wie "doppeltes k in Netzabstaenden". Genau das braucht die
    Bestimmung von d.
  - Folge: Lauf (a) bekommt neue Saaten. Mit den Saaten 0 bis 63 waeren die Punkte n = 2 und 4 bitgleich zum Hauptlauf
    und keine neuen Daten.

## 3. Laeufe

- **Ort:** .69, /home/fmh/fmhc-physics-remote/runde38-induziert-grob/ (code/, rauch/, lauf/), nur ueber kleintest.sh,
  Spuren cpu und cpu7, je ssh-Aufruf ein Start, hoechstens zwei zugleich.
- **Einstellungen (wie Hauptlauf):** S = 0,5; Richtungen 0 und 90 Grad; Netz koord (Kartenwortlaut); intr = 0.
- **(b) Kontrolle [F, K3]:** N = 16 000, ohne Option A (also L = sqrt N), n = 1, 2, 4, 6, Saaten 0 bis 63 (dieselben
  wie der Hauptlauf), Bloecke b-s0 (0 bis 31) und b-s32 (32 bis 63).
- **(a) Hauptlauf grob:** N = 16 000, A = 64 000, n = 2, 4, 8, 12, Saaten 200 bis 439 in fuenf Bloecken zu 48:
  a-s200, a-s248, a-s296, a-s344, a-s392.
- **Verteilung:** cpu7: a-s200, a-s248, a-s296. cpu: b-s0, b-s32, a-s344, a-s392.
- **Laufzeit (gemessen, Abschnitt 10):** 0,43 s je Bildnetz, 7,2 s je Saat mit 16 Bildnetzen. Bloecke: (b) etwa 230 s,
  (a) etwa 350 s, alle unter 600 s.
- **Saatzahl [F]** (Karte: "so viele wie fuer +-0,005 in d noetig, vorab abschaetzen"):
  - Rauschmodell des Gegenlesers: Versatz je Saat plus unabhaengiger Rest. Bei N = 16 000 in y_eps: Rest
    sigma ~ 0,0012, Versatz tau ~ 0,0026 (aus Std je Saat 0,0177 und y-Streuung 0,0029 des Hauptlaufs).
  - G allein (je Saat a + c x + d x^2): SE(d) ~ 42 sigma/sqrt(M) = 0,050/sqrt(M). Fuer +-0,005 braucht man etwa
    100 Saaten.
  - Gemeinsam mit M64 und M16, die c festlegen: SE(d) ~ 0,005 schon bei etwa 16 Saaten, 0,0035 bei 64, 0,0024 bei
    240 (Rechnung von Hand, Selbsttest Abschnitt 10).
  - Geplant sind 240 Saaten, auch fuer SE(c) ~ 0,0009. Begrenzt ist das durch die Zeitbox.
- **Abbruch:** Fehlen Bloecke (Zeitbox, Abbruch nach 600 s), wird mit den fertigen Saaten geurteilt (offengelegt).
  Unter 32 Saaten in (a) sind IG1 bis IG3 nicht auswertbar. Fehlende Saaten von (b) machen IG0 nicht auswertbar.
- **Danach:** grob_auswertung.py auswerten <Hauptlauf-Ordner> lauf lauf/auswertung.json. Der Hauptlauf-Ordner
  /home/fmh/fmhc-physics-remote/runde38-induziert-dichte/lauf wird nur gelesen (sha256 wie dort in PRUEFSUMMEN.txt).

## 4. Gemeinsamer Ausgleich (Urteil) [F]

- **Datensaetze:** M64 (Saaten 0 bis 65), M16 (0 bis 63), G (200 bis 439). Alle mit S = 0,5, koord, je Saat y_eps(n)
  gemittelt ueber 0 und 90 Grad. (b) geht nicht in den Ausgleich, es wiederholt M16.
- **Modell (Karte):** y_eps = a + c x + d x^2, gemeinsam ueber beide Dichten und alle drei Datensaetze, x = (k eps)^2.
  - c ist der Grenzwert k -> 0 der konformen Steifigkeit, d das k^4-Glied in Netzabstands-Einheiten.
  - Gewertet werden das k^0-, k^2- und k^4-Glied; Fenster sind alle zwoelf Zellen, k eps von 0,050 bis 0,596.
- **Kovarianz der Saatfehler:**
  - Je Datensatz die Stichproben-Kovarianz Sigma_D (4 x 4, ddof 1) der y_eps-Vektoren ueber die Saaten, ohne
    angenommene Struktur.
  - Sie enthaelt den Versatz je Saat (laut Gegenleser rund 80 %) und jede k-Abhaengigkeit.
  - GLS auf den zwoelf Zellmitteln mit Kovarianz blockdiag(Sigma_D/M_D). Das ist gleichwertig zur GLS ueber alle
    Saaten mit dieser Kovarianz.
- **Fehler:** SE_GLS aus (X^T C^-1 X)^-1. Verwendet wird SE_U = SE_GLS max(1, sqrt(chi^2/FG)) (Birge-Faktor).
- **Modellprobe:** chi^2 der zwoelf Zellen gegen das Modell, 9 Freiheitsgrade. Liegt p < 0,01, sind IG1 bis IG3 "nicht
  auswertbar": Das Modell der Karte traegt dann nicht. Die Lesarten aus Abschnitt 7 werden dann nur beschrieben.
- **Selbsttest (synthetisch):** wahres a, c = P, d = -0,035, Rauschen wie oben, 300 Wiederholungen. Ergebnis: Zug-Std
  0,99 / 1,02 / 1,00, chi^2-Mittel 9,4, Fehlalarm der Modellprobe 1,3 %. Ein k^6-Glied 0,5 x^3 loest die Probe aus
  (p = 5e-17).

## 5. Vorhersagen der Karte (unveraendert)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IG0 | Kontrolle (b): Der Kopie-Code mit L = sqrt N gibt den Hauptlauf (N = 16 000: -0,0131 +- 0,0022) innerhalb 2 SE wieder | 90 % |
| IG1 | d (k^4-Glied) ist auf <= +-0,01 bestimmt | 70 % |
| IG2 | [H] Der Grenzwert k -> 0 liegt zwischen 0,7 P und 1,2 P (P = -1/(24 pi)) | 60 % |
| IG3 | [H] Der Grenzwert liegt innerhalb 15 % von P | 35 % |

## 6. Urteilsregeln (mechanisch durch code/grob_auswertung.py nach lauf-69/auswertung.json)

- **Tor [F]:** In (a) und (b) erfuellt jedes Netz die eingefrorenen Pruefungen. Das sind Euler, E = 3N, F = 2N, jede
  Kante in genau zwei Dreiecken, Orientierung > 0, Koordinatenflaeche = L^2 auf 1e-9, physikalische Flaechen > 0,
  laengste Kante < L/4, Grundnetz Delaunay, LU mit U_ii > 0 und perm_r = perm_c, Newton-Residuum <= 1e-12.
- **Vorbedingungen fuer IG1 bis IG3:** Tor (a) bestanden, IG0 eingetroffen, mindestens 32 Saaten in (a),
  Modellprobe p >= 0,01. Sonst "nicht auswertbar" mit Vermerk.
- **IG0 [F, K3]:**
  - c_b wird nach der eingefrorenen Regel gebildet: je Saat Mittel ueber 0 und 90 Grad, OLS y = a + c k^2 ueber
    n = 1, 2, 4, 6, Saatmittel und SE.
  - Eingetroffen, wenn abs(c_b - c_M16) <= 2 SE_M16, mit c_M16 = -0,013110 und SE_M16 = 0,002218 (nach derselben Regel
    aus den Hauptlaufdateien; Karte: -0,0131 +- 0,0022). Sonst nicht eingetroffen. Faellt das Tor (b), ist IG0 nicht
    auswertbar.
  - Mitberichtet: Bitvergleich Saat fuer Saat (Gamma(0), Gamma(+-S), D).
- **IG1 [F: 1 SE]:** Eingetroffen, wenn SE_U(d) <= 0,01, sonst nicht eingetroffen. "+-" heisst ein Standardfehler,
  wie in Karte und Gegenlesen. Kartenwortlaut ohne Birge-Faktor wird mitberichtet.
- **IG2 [F: Rauschregel wie ID1 im eingefrorenen Plan; Band der Karte]:** Band B2 = [1,2 P; 0,7 P] = [-0,015916;
  -0,009284].
  - Eingetroffen: c in B2 und SE_U(c) <= 0,25 abs(P) = 0,003316 (halbe Bandbreite).
  - Nicht eingetroffen: Abstand von c zu B2 > 2 SE_U(c).
  - Sonst nicht auswertbar. Kartenwortlaut (c in B2, ohne Rauschregel) wird mitberichtet.
- **IG3 [F: dieselbe Regel]:** Band B3 = [1,15 P; 0,85 P] = [-0,015252; -0,011274].
  - Eingetroffen: c in B3 und SE_U(c) <= 0,15 abs(P) = 0,001989.
  - Nicht eingetroffen: Abstand > 2 SE_U(c).
  - Sonst nicht auswertbar. Kartenwortlaut wird mitberichtet.
- **Bedeutung:** wie auf der Karte vorab festgelegt (IG2 trifft ein / IG3 trifft ein / IG2 verfehlt).

## 7. Beschreibend (kein Urteil)

- Ausgleich ohne M64 (nur N = 16 000), Fenster k eps <= 0,40 (ohne G bei n = 12), mit k^6-Glied, mit eigenem a je
  Datensatz
- Kovarianz nach dem Versatz-Modell des Gegenlesers (sigma^2 I + tau^2 J je Datensatz, Varianzanalyse)
- feste Saatversaetze (je Saat eigener Achsenabschnitt)
- geschichtetes Jackknife ueber Saaten fuer die SE
- nur k^2 (ohne k^4) ueber alle k und im Fenster 0,40
- Fenster-Steigungen nach der eingefrorenen Regel: G gegen M64 bei gleichen k in Torus-Einheiten. Die Differenz mal
  1/(Hebel G - Hebel M64) gibt eine Zwei-Punkt-Schaetzung von d (Hebel 0,371 gegen 0,093).
- G gegen M16 bei gleichem k eps (0,099 und 0,199): unabhaengige Saaten, nach Skalengleichheit dasselbe Ensemble
- c(k) = (y - a)/x je Zelle mit Modellgerade c + d x
- Varianzanteile (Versatz, Rest) je Datensatz und Streuung je k
- noetige Saatzahl fuer SE(d) = 0,005 und 0,01
- Bilder: lauf-69/bild-ck-gegen-k2.png (c(k) gegen k^2 fuer beide Dichten mit Ausgleichskurve und Polyakov-Linie;
  y gegen k^2), lauf-69/bild-streuung-grob.png

## 8. Kartenpunkte (vor dem Einfrieren offengelegt)

- **[K1] Skalengleichheit (Abschnitt 2):**
  - Die Karte spricht von einem groeberen Netz bei gleichem k in Torus-Einheiten. Rechnerisch ist das dasselbe Netz bei
    doppeltem k eps.
  - Das ist kein Fehler der Karte: Der Test misst d genau ueber den groesseren Hebel in k eps.
  - Die Bitgleichheit schliesst aber jeden "Dichte-Effekt" jenseits von k eps aus. Ein Unterschied zwischen den
    Dichten kann nur ueber k eps entstehen. Der gemeinsame Ausgleich in Netzabstands-Einheiten ist deshalb die
    richtige Form.
- **[K2] Randstreifen:**
  - Der eingefrorene Code setzt RAND = 8 mit dem Kommentar "mittlerer Abstand 1". Bei eps = 2 waeren 8 Einheiten nur
    4 Abstaende.
  - Abschaetzung [M]: Der Umkreisradius im Poisson-Delaunay hat u = pi rho R^2 ~ Gamma(2, 1). Im duennen Teil bei
    S = 0,5 ist die Koordinatendichte 0,29/eps^2.
    - R > 4 Einheiten (Streifen 8 bei eps = 2) haben dort etwa 12 % der Dreiecke. Randdreiecke wuerden falsch.
    - Mit 16 Einheiten sind es etwa 7e-6, wie im Hauptlauf.
  - Deshalb skaliert die Kopie den Streifen mit eps. Die Bitgleichheit der Skalenprobe belegt, dass das Netz damit
    exakt das skalierte Hauptlauf-Netz ist.
  - Nach Kartenwortlaut ("sonst nichts aendern") waere der Streifen fest geblieben. Gerechnet ist das nicht.
    Vermutlich gaebe es Tor-Fehler oder falsche Randdreiecke.
- **[K3] IG0 "innerhalb 2 SE":** Die Karte laesst offen, ob (b) neue oder dieselben Saaten nutzt. Festgelegt sind
  dieselben Saaten 0 bis 63. Das ist die schaerfste Probe der Kopie: Erwartet ist Bitgleichheit, also Abstand 0. SE ist
  der des Hauptlaufs (0,0022).
- **[K4] Rauschregeln fuer IG1 bis IG3** fehlen auf der Karte. Festgelegt wie ID1 im eingefrorenen Plan (Abschnitt 6).
  Kartenwortlaut (Punktwert im Band) wird mitberichtet.
- **[K5] "Grenzwert k -> 0"** ist der Achsenabschnitt c des Modells mit k^0, k^2 und k^4. Das setzt voraus, dass k^6
  im Fenster bis k eps = 0,6 nicht noetig ist. Geprueft wird das durch die Modellprobe (Abschnitt 4); bei Verfehlen
  gilt "nicht auswertbar".
- **[K6] "Ausgleich wie im eingefrorenen Plan"** (Karte, Test) gilt fuer IG0 und die Fenster-Steigung. Das Urteil zu
  IG1 bis IG3 folgt der Auswertungsvorschrift der Karte (gemeinsamer Ausgleich mit k^4).
- **Kein Kartenfehler,** der ein Urteil nach Kartenwortlaut veraendert. [K2] betrifft nur die Ausfuehrung von "L als
  Argument".

## 9. Agenten-Vorhersagen (vor den Hauptlaeufen)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| B1 | Tor besteht in (a) und (b) | 90 % |
| B2 | (b) ist in allen 64 Saaten bitgleich zum Hauptlauf | 97 % |
| B3 | Modellprobe besteht (p >= 0,01) | 75 % |
| B4 | Saatstreuung von y_eps in G bei k eps = 0,099 und 0,199 wie M16 (Faktor 0,8 bis 1,25) | 80 % |
| B5 | d < 0 (wie auf dem festen Netz, dort etwa -0,035) | 55 % |

## 10. Rauchlaeufe (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC)

- **b-s0** (07:12:27 bis 07:12:42, cpu, rc 0): (b) mit den Saaten 0 und 1, n = 1, 2, 4, 6, S = 0,5. Dauer 7,3 und
  7,1 s je Saat.
- **a-skala-s0** (07:12:29 bis 07:12:37, cpu7, rc 0): (a) mit A = 64 000, Saaten 0 und 1, nur n = 2 und 4. Dauer 3,9
  und 3,8 s je Saat (8 Bildnetze).
- **Vergleiche** (07:15:53 bis 07:15:57, cpu):
  - b-s0: 16 von 16 Zeilen bitgleich zum Hauptlauf (Gamma(0), Gamma(+-S), D, y).
  - a-skala-s0: 8 von 8 Zeilen bitgleich zu M16 bei gleicher Saat und gleichem n. Gamma(0), Gamma(+-S) und D sind
    gleich; y_eps = 4 y_koord ist bitgleich.
  - Tor in beiden bestanden.
- **Selbsttest** (07:16:05 bis 07:16:07, cpu7): synthetisch, Abschnitt 4.
- **Probe der Auswertung** (07:16:27, cpu):
  - Erster Versuch: Division durch null. In der Probe war G eine Kopie von M64 mit gleichem Hebel. Berichtigt mit
    Schutz gegen gleichen Hebel.
  - Zweiter Versuch (07:16:50 bis 07:16:56, rc 0): Codepfad und Bilder laufen.
  - Gesehen habe ich nur Werte aus dem Hauptlauf (G = M64-Kopie, B = Saaten 0 und 1): c = -0,0066 +- 0,0038,
    d = -0,062. Das ist der bekannte k^4-Fit des Hauptlaufs; durch die doppelte M64 ist der Fehler zu klein. Die
    "Urteile" dieser Probe sind bedeutungslos.
- Die y-Werte der Rauchlaeufe habe ich nicht einzeln angesehen. Sie sind ohnehin bitgleich zu bekannten
  Hauptlaufwerten.
