# Urteil: traegt mit Einschraenkung (GEGENLESEN INDUZIERT-KUGEL-1, Runde 40)

Status: abgeschlossen. 2 A-Befunde (A1 betrifft die Meldung an Finn, A2 den Folgetest), 3 B-Befunde, 3 C-Befunde.

- Gegenleser: pruefer-opus (Haus Anthropic), frischer Leser, Schreibtisch, keine Laeufe.
- Beginn (date): 2026-10-04 11:49:26 CEST. Letzter Eintrag ab 12:08:41 CEST (date), also rund 19 min von 45.
- Auftrag: RUNDE-37/kugel-gegenlesen/KARTE.md, sha256 1b4f59e0dbf436a4499b7d943a55c5321fa6f8c41abe1059fb389acc523b872f.
- Rechnungen im Kopf mit Rechenweg; jq nur zum Auslesen der Rohdaten (Systemregel "keine Rechnung auf dem Rechner" ist
  strenger als die Einladung zu jq-Kontrollrechnungen und gilt daher).

## Ergebnis

**Traegt mit Einschraenkung.** Die Messung und ihr Vorzeichen tragen. Die Meldung "ein kovariantes Netz gibt Einsteins
Vorzeichen" muss enger gefasst werden (A1), und der vorgeschlagene Ellipsoid-Test ist so nicht sauber (A2).

1. **Messung [E] traegt:**
   - beta_S = -1,651 +- 0,052, 40 von 40 Saaten negativ, y ueber den Faktor 8 in N flach.
   - Die Torusseite hat kein sqrt(N)-Glied (abs(b_T) <= etwa 0,1); das Vorzeichen kommt also von der Kugel.
   - Quote: 20 von 20 nachgerechneten Zahlen stimmen (61,56; 0,9168; 11,19; Umrechnungen; SE; t; p; Regge-Quotienten;
     B; G = 0,74; gamma-Verschiebung; H-Kont -0,578; zeta(0) = 29/90 - 1).
2. **Volumenumrechnung begruendet:**
   - Das Glied "Kosmologie mal Volumenfehler" ist exakt die Differenz roh - korr; korr entfernt es.
   - Das Einstein-Vorzeichen von Gamma haengt nicht daran (roh S -1,19, C -3,14).
   - Gamma_M roh mit Sehnen (+0,16) ist ein Vergleich bei Dichte 1,245 gegen Dichte 1 und keine Gegenlesart.
3. **Identifikation:**
   - beta = 61,56 B_Regel gilt wegen der Kugelsymmetrie fuer die beiden gerechneten Regeln.
   - B haengt an der Regel (S - C = -0,196).
   - Aeussere Kruemmung ist auf S^4 nicht trennbar, aber auch kein Fremdglied.
   - Allgemeine Kovarianz ist nicht gezeigt: Eine intrinsische Regel fehlt.
4. **Nicht gedeckt:** Dass das Torus-Vorzeichen aus nicht kovarianten Anteilen kam, ist nur [H]. Gezeigt ist allein,
   dass H-kov fuer mindestens eine Konstruktion mit 5,7 SE verletzt ist. Torus-c und beta widersprechen einander nur
   unter dieser Annahme.
5. **Schreibtischfehler 0,9168:** richtig gefunden, fuer das Urteil folgenlos.
6. **2D-Kontrolle:** Sie prueft die Konstruktion, nicht die 4D-Artefakte.
7. **Folgetest:** Regeln G (geodaetisch) und Q (volumentreu je Simplex) gepaart auf denselben S^4-Saaten, nicht das
   Ellipsoid als Huelle.

## Gelesene Quellen

- RUNDE-37/induziert-kugel-1/:
  - KARTE.md und PLAN.md Z. 1-99. PLAN ist per cmp bytegleich mit PLAN.md.eingefroren-20261004-110255, ebenso alle
    fuenf Code-Kopien; die sha256 stimmen mit EINGEFROREN-SHA256.txt.
  - ERGEBNIS.md Z. 1-168 und 204-300. Abschnitt 4 (Kontrollen) habe ich nur ueber PLAN S3, S4 und 2 gelesen.
  - code/kugel.py Z. 94-140 und 220-354.
  - lauf-69/auswertung.json (jq: fits, beta_je_saat) und lauf-69/messung-n4-N1000-s0.json (jq keys, geo).
  - rauch-69/rauch-a/-b/-c.json (jq: blind = true, keine gamma-Felder, LU-Info ohne log det).
- RUNDE-37/induziert-g-l/DOSSIER.md Z. 146-166 (6.3) und 196-222 (8.3).
- RUNDE-37/induziert-dichte-4d/PLAN.md und ERGEBNIS.md, nur grep-Ausschnitte (Faktor 0,92, Definition von c, IV0/IV1).
- Nicht gelesen:
  - code/auswertung_kugel.py; die Fitwerte habe ich per jq gegen die Tabellen geprueft.
  - rauch-69/probe/.
  - Kein Versiegeltes, kein anderer Gegenleser-Ordner.
- Werkzeuge: cat, sed -n, grep, jq, cmp, sha256sum, ls, wc, date.
  - jq diente zum Auslesen. Einmal habe ich in jq zur Anzeige gerundet und min, max und Anzahl gebildet; jede Rechnung
    in diesem Text ist im Kopf gerechnet.

## Frage 1: Identifikation

**Urteil: ja, beta misst B, aber nur das B der jeweiligen Laengenregel (B_C, B_S), kein regelunabhaengiges B. Die
Trennung im Lauf ist bis auf einen regelabhaengigen O(h^2)-Anteil sauber.** Fundstellen: DOSSIER 8.3, PLAN 1 (S1, S3,
S5, Regge-Absatz), ERGEBNIS 3.1 bis 3.4, code/kugel.py Z. 114-138 und 220-272.

- Grund [M]: S^4 ist homogen und isotrop, die Konstruktion (Gleichverteilung, Huelle = sphaerisches Delaunay) ist
  isometrie-invariant. Jedes lokale Glied der Ordnung N (l/a)^2 ist dann proportional zu Int sqrt(g) R, und wegen
  a^2 = 0,19492 sqrt(N) gilt N/a^2 ~ sqrt(N). Jede O(h^2)-Antwort des Gitters auf die Kruemmung landet also in beta. Das
  ist zugleich die Identifikation (beta = 61,56 B_Regel) und ihre Grenze (B haengt an der Regel).
- S1 nachgerechnet: R = 12/a^2, Vol = (8 pi^2/3) a^4, Int R = 32 pi^2 a^2; 315,83 mal 0,19492 = 61,56. Auch
  halb_int_R = 973,39 in messung-n4-N1000-s0.json: 30,781 mal 31,623 = 973,4. Richtig.
- Weitere Zahlen im Kopf:
  - B = -1,651/61,56 = -0,0268.
  - G = -1/(16 pi B) = 1/(50,27 mal 0,0268) = 1/1,347 = 0,742.
  - H-Kont: Lambda^2 = Wurzel(32 pi^2) = Wurzel(315,8) = 17,77; 17,77/(192 pi^2) = 17,77/1895 = 0,00938; mal 61,56 =
    0,577, mit negativem Vorzeichen. Das Vorzeichen (Eigenzeit, a_1 = R/6) ist das Einstein-Vorzeichen.
  - zeta(0) auf S^4: a_2 = (1/180)(24 - 36)/a^4 + (1/72)(144/a^4) = (-1/15 + 2)/a^4 = (29/15)/a^4. Mal Vol/(16 pi^2)
    ergibt 29/90.
  - gamma = 61/360 - 1/4 = -29/360.
  - Alles stimmig.

| Glied, das wie sqrt(N) wachsen kann | Groesse | Im Lauf | Urteil |
|---|---|---|---|
| Kosmologieglied mal globaler Volumenfehler | (N-1)/4 ln(V_R/N), C +1,70, S -0,48 sqrt(N) | steckt genau in roh; korr entfernt es exakt (Identitaet, Kontrolle KE 1e-10) | getrennt (Frage 2) |
| Kosmologieglied mal lokaler Volumenverteilung (nicht gleichfoermige O(h^2)-Verzerrung je Simplex) | sqrt(N) | nicht getrennt; S und C unterscheiden sich genau darin: S - C = -0,196 +- 0,002 | Regelanteil, etwa 12 % von beta |
| Polytop-Kruemmung (Regge-Defizit) | 1 - 0,9203 / 0,9434 / 0,9598 / 0,9715 = 0,0797 / 0,0566 / 0,0402 / 0,0285; Quotienten 1,41 / 1,41 / 1,41 = Wurzel 2 | faellt wie 1/sqrt(N), geht in delta | richtig |
| Aeussere Kruemmung (Regel C) | auf S^4 nabelig: K_ab = g_ab/a, K^2 = 16/a^2, K_ab K^ab = 4/a^2, R = 12/a^2 | nicht trennbar, aber auch kein Fremdglied (Frage 2, letzter Punkt) | siehe dort |
| ln N aus zeta(0) | gamma = -29/360 = -0,081; mal b0 = 0,0388 ergibt 0,003 | Fit mit gamma = 0 | vernachlaessigbar |
| Euler-Charakteristik, R^2-Glieder, h^4-Reste | O(1) | delta | richtig |
| Rand | keiner (beide geschlossen) | - | - |
| Torus-Endlichkeit, Saum | Gamma_T/N = 1,313 / 1,315 / 1,313 / 1,314. Ein Glied b_T sqrt(N) aenderte Gamma_T/N um b_T (1/31,6 - 1/89,4) = 0,0204 b_T; gesehen <= 0,002, also abs(b_T) <= etwa 0,1. Ein 4D-Saumglied wuechse wie N^(3/4) und kippte y um den Faktor 1,68; y ist flach (+-0,05) | | das Vorzeichen kommt von der Kugelseite |

- Mechanismus [ES, beschreibend]: Simplizes je Punkt Kugel 27,46 / 28,68 / 29,56 / 30,21 gegen Torus etwa 31,8;
  Fehlbetrag 4,34 / 3,12 / 2,24 / 1,59, Quotienten 1,39 / 1,39 / 1,41, also wie 1/sqrt(N). Positiv gekruemmt heisst
  weniger Nachbarn je Punkt, also kleineres log det. Das ist eine intrinsische Netzeigenschaft und macht das
  Vorzeichen plausibel.
- Was nicht stimmt: "exakt kovariant" (KARTE KUGEL-1, ERGEBNIS 1.1). Punktprozess und Triangulierung sind
  isometrie-invariant und auf S^4 intrinsisch. Die Laengenregeln C und S sind aber ueber die Einbettung definiert
  (Sehne, Jacobi-Faktor der Radialprojektion). Auf S^4 sind sie nur deshalb intrinsisch, weil die Kugel nabelig ist
  (Befund B1).

## Frage 2: Volumenkonvention

**Urteil: korr ist die begruendete Fassung, und die Formeln stimmen. Das Einstein-Vorzeichen von Gamma haengt nicht an
der Umrechnung. Am Vorzeichen haengen Gamma_M mit Sehnen, KU4 roh und die Reihenfolge S/C.** Fundstellen: PLAN S3,
S3', 2 (Volumenkorrektur); code/kugel.py Z. 126-132; ERGEBNIS 3.1.

- Begruendung: K kennt nur die Laengen, also das Netz der Regel R mit dem Volumen V_R. "Zahl = Volumen" verlangt
  V = N. korr ist exakt Gamma desselben Netzes nach globaler Streckung auf V = N. roh vergleicht dagegen bei der Dichte
  N/V_R mit einem Torus der Dichte 1 (Regel C, N = 1000: 1/0,8030 = 1,245). Die Differenz roh - korr ist genau das
  Dichte- oder Kosmologieglied. **Zur Leitungsfrage:** Das Glied "Kosmologie mal O(h^2)-Volumenfehler" auf der
  Ordnung sqrt(N) gibt es. Es ist exakt die Umrechnung und steckt in roh; in korr ist es global entfernt. Uebrig
  bleibt nur die lokale Volumenverteilung (Frage 1, Zeile 2), und die ist Teil von B_Regel.
- Formeln nachgerechnet [M]: K vom Grad 2, also Gamma(lambda l) = Gamma(l) + (N-1) ln lambda. m_i vom Grad 4:
  -1/2 Sum ln m_i gibt -2N ln lambda, +1/2 ln(Sum m/N) gibt +2 ln lambda. Fuer Gamma_M zusammen
  (N - 1 - 2N + 2) ln lambda = -(N-1) ln lambda. Mit lambda^4 = V_K/V_R: Gamma + (N-1)/4 ln(V_K/V_R),
  Gamma_M - (N-1)/4 ln(V_K/V_R). Der Code nimmt V_R aus den Laengen der jeweiligen Regel (p1(sq)), also je Regel das
  eigene Volumen. Auch Gamma_M = Gamma - 1/2 Sum ln m + 1/2 ln(V_R/N) ist richtig (Matrix-Baum-Satz: alle
  Hauptminoren gleich, det'(DKD) = det K_(0) Prod(1/m) Sum m).
- Zahlen im Kopf:
  - C, N = 1000: 249,75 mal ln(1/0,8030) = 249,75 mal 0,2194 = 54,8; durch 31,62 ergibt 1,733 (Tabelle 1,73).
  - C, N = 8000: 1999,75 mal 0,0760 = 152,0; durch 89,44 ergibt 1,700.
  - S, N = 1000: 249,75 mal (-0,0630) = -15,7, also -0,497.
  - Einzelnetz Saat 0, N = 1000: V_C = 802,47, ln(1,2462) = 0,2201, mal 249,75 = 54,97.
  - Alles stimmig.
- Haengt nicht am Vorzeichen: Gamma bei S und C. roh -1,190 +- 0,053 und -3,135 +- 0,052, korr -1,651 und -1,455.
  Bei S sind alle 40 Saaten in beiden Fassungen negativ (jq: korr -2,344 bis -1,052, roh -1,886 bis -0,591).
- Haengt am Vorzeichen:
  - Gamma_M mit Sehnen: roh +0,159 +- 0,055 (26 von 40 Saaten positiv), korr -1,521.
  - KU4 roh bei C: -3,135 - 0,159 = -3,294. Das ist fast nur Volumen (zweimal 1,68 = 3,36, Rest 0,066 = korr).
  - Reihenfolge der Regeln: roh S - C = -1,190 + 3,135 = +1,945, korr -0,196.
  - Betrag von beta und Abstand in KU2.
- Gegenfall geprueft: Man koennte "die Kugel ist die Geometrie, V = V_K = N" sagen und roh nehmen. Dann stellte ein
  Polytop mit V_C = 0,80 N eine Geometrie vom Volumen N dar, obwohl der Operator nur das Polytop kennt. Das ist mit
  "Zahl = Volumen" unvereinbar. +0,16 ist also keine konkurrierende Lesart, sondern ein Vergleich bei Dichte 1,245
  gegen Dichte 1. ERGEBNIS 1.3 ("einziger gefundener Hebel, der ein Vorzeichen drehen kann") und 7 ("eine
  Konvention") sagen das nicht (Befund B2).
- Aeussere Kruemmung (Leitungsfrage): Auf S^4 ist Sehne = 2a sin(d/(2a)) eine Funktion des inneren Abstands d und
  des inneren Kruemmungsradius (a^2 = 12/R). Ebenso haengt J_T nur an Simplexdaten und a. Regel C laesst sich auf S^4
  also nicht von einer intrinsischen Regel unterscheiden, und ein getrenntes Aussenglied kann es dort nicht geben.
  Allgemein kovariant sind C und S trotzdem nicht: Auf einer nicht nabeligen Flaeche hingen sie an K_ab. Fuer die
  Aussage "kovariantes Netz" fehlt eine allgemein intrinsische Regel (geodaetische Laengen, Frage 8).

## Frage 3: Schreibtischfehler der Karte (Faktor 0,9168)

**Urteil: richtig. Unter H-kov gilt beta = 11,19 c_Torus, also ist der Zielwert in KU2 +1,24 +- 0,50 und nicht
+1,14 +- 0,46. Fuer das Urteil hat das keine Folge.** Fundstellen: PLAN S2', induziert-dichte-4d/PLAN.md Z. 110-112 und
205 (dort schon "0,92 bei S = 0,25"), induziert-dichte-4d/ERGEBNIS.md Z. 20-21 (y = a + c k^2 ueber zwei k, dy
abgezogen).

- c = 6 B nachgerechnet: g = e^(2 sigma) delta in 4D, sqrt(g) R = e^(2 sigma)(-6 Box sigma - 6 (grad sigma)^2).
  Partiell integriert ist -6 Int e^(2 sigma) Box sigma = +12 Int e^(2 sigma)(grad sigma)^2, zusammen
  +6 Int e^(2 sigma)(grad sigma)^2. Richtig.
- Erster Faktor: Mittel von e^(z cos u) sin^2 u ist I1(z)/z. Mit z = 2S ist Int e^(2 sigma)(grad sigma)^2 =
  S^2 k^2 V I1(2S)/(2S); die Zweitdifferenz verdoppelt das. Bei S = 0,25 ist I1(0,5) = 0,25 + 0,0078125 + 0,0000814 =
  0,257894, durch 0,25 ergibt **1,03158**.
- Zweiter Faktor: Bei fester Punktzahl ist die Dichte 1/I0(4S), und B ~ rho^(1/2) (B ~ Lambda^2, Lambda^4 ~ rho). Es
  gilt I0(1) = 1 + 0,25 + 0,015625 + 0,000434 + 0,0000068 = 1,266066, die Wurzel ist 1,125196, der Kehrwert **0,888734**.
- Produkt: 1,03158 mal 0,888734 = 0,888734 + 0,028063 = **0,91680**. Dann 6 mal 0,9168 = 5,5008 und
  61,562/5,5008 = **11,19**. Zielwert 11,19 mal 0,111 = 1,242, SE 11,19 mal 0,045 = 0,504. Auch ERGEBNIS 3.3 rechnet
  so: -1,651/11,19 = -0,148. Alles stimmig.
- Anmerkung: Der Faktor setzt eine reine Einstein-Wirkung bei endlichem S voraus. Glieder in k^4 sind im
  Zwei-Punkt-Fit des Torus nicht getrennt (ERGEBNIS-4D Z. 352). Das betrifft die Vergleichbarkeit (Frage 6), nicht den
  Faktor.

## Frage 4: 2D-Kontrolle

**Urteil: Sie prueft nur die Konstruktion (Huelle, Orientierung, P1-Aufbau, log det, 2D-Torus), nicht die
4D-Artefakte. Ihr Ausgang beta_2D = 0 stand bei fehlerfreiem Code vorab fest.** Fundstellen: KARTE KUGEL-1
("Vorab ableitbar"), PLAN S4, ERGEBNIS 1.2, 3.1, 7.

- Vorab ableitbar [M]: In 2D ist K vom Grad 0, Int R = 8 pi ist topologisch, und O(h^2 R) N = O(1). Ein sqrt(N)-Glied
  kann nur ein Fehler erzeugen. KU0 ist also eine Fehlerprobe, keine Messung, und als solche nuetzlich.
- Was sie fuer 4D nicht sieht:
  - Die Volumenumrechnung, also die Hauptfrage der Leitung: Gamma hat in 2D kein Volumenglied.
  - Die Regel S: In 2D ist sie exakt gleich C (Kontrolle KH).
  - Die O(h^2)-Diskretisierung der Kruemmung: in 2D O(1), in 4D sqrt(N).
  - Den 4D-Torus-Code: 2D nutzt zufall2d.py, 4D dichte4d.py.
  - Ein Saumartefakt: Es wuechse in 2D wie sqrt(N), in 4D wie N^(3/4). Die 2D-Probe ist also auch hierfuer nicht
    uebertragbar. In 4D deckt es stattdessen die Flachheit von y ab (Frage 1).
- ERGEBNIS 7 schraenkt richtig ein ("soweit es auch in 2D wirken wuerde"). In einer Meldung an Finn darf die
  2D-Kontrolle nicht als Artefaktkontrolle fuer 4D erscheinen (Befund C1).

## Frage 5: Statistik

**Urteil: Die SE tragen als statistische Fehler, und das Vorzeichen ist statistisch zweifelsfrei. Sie enthalten aber
keine systematische Bandbreite, und die ist groesser als die SE.** Fundstellen: PLAN 3 und 4; ERGEBNIS 3.1 und 3.2;
lauf-69/auswertung.json (.dim["4"].fits).

- Nachgerechnet:
  - SE = 0,33117/Wurzel 40 = 0,33117/6,3246 = 0,05236 und t = -1,6515/0,05236 = -31,5.
  - Regel S: 40 von 40 beta_j negativ (jq min/max: -2,344 und -1,052).
  - WLS: chi^2 = 2,45 bei 2 Freiheitsgraden ergibt p = e^(-1,225) = 0,29. Die Probe hat mit 4 Punkten wenig Trennkraft.
- Unabhaengigkeit: Die Kugelsaaten haben eigene Schluessel [20261004, 39, n, N, saat], die Torussaaten 39000 + saat.
  Selbst wenn eine Saat ueber die N korreliert waere, bleibt die SE aus der Streuung der beta_j zwischen den Saaten
  gueltig.
- Modell: y je N ist -1,688 / -1,736 / -1,637 / -1,681 (Spanne 0,099 bei SE je Punkt etwa 0,04). Die Streuung je Saat
  ist in y-Einheiten konstant (0,23 bis 0,28), also gilt Std(Delta Gamma) ~ sqrt(N). Die Teilbereiche (-1,593 +- 0,081
  und -1,624 +- 0,091) und der Dreiparameterfit (-1,52 +- 0,36) zeigen dasselbe Vorzeichen. Das traegt.
- Nicht in der SE:
  - Regelspanne: S - C = -0,196, gepaart fast rauschfrei (Std je Saat 0,011). Das ist Systematik, kein Rauschen, und
    etwa viermal so gross wie die SE.
  - Nicht gerechnete Regeln: Auf dem Torus aenderte die Regel c um 0,26 (sp +0,111, geo+ +0,371; ERGEBNIS-4D IV1). In
    beta-Einheiten sind das 0,26 mal 11,19 = 2,9, also mehr als abs(beta). Die Uebertragung ist nicht zwingend [ES]:
    Auf dem Torus unterscheiden sich die Regeln schon in erster Ordnung in l grad sigma, auf S^4 erst in O(h^2/a^2).
    Die S^4-Spanne ist entsprechend klein (0,196 in beta, also 0,0175 in c-Einheiten).
  - Forderung: "-1,65 +- 0,05 (stat.), Regelspanne C-S 0,20, weitere Regeln nicht gerechnet" (Befund B3).

## Frage 6: Lesart

**Urteil: Als Befund nicht gedeckt; als [H] zulaessig, aber "kam aus" ist zu stark. Torus-c und beta sind nur unter
H-kov vergleichbar, und genau diese Annahme ist jetzt mit 5,7 SE verletzt. Wo die nicht kovarianten Anteile sitzen,
ist offen.** Fundstellen: KARTE KUGEL-1 (Bedeutung KU1), ERGEBNIS 1.5, 3.3, 7; DOSSIER 6.3; induziert-dichte-4d/ERGEBNIS.md
Z. 20-33, 58-59, 352.

- Verschiedene Messgroessen:
  - Der Torus misst die Antwort auf eine inhomogene konforme Mode: endliche Amplitude S = 0,25 bei 79 % gekippten
    Simplizes, zwei k-Werte (k^4 nicht getrennt), Delaunay in Koordinaten, Regel sp.
  - S^4 misst die Antwort auf homogene Kruemmung bei gleichverteilten Punkten.
  - Im Kontinuum steuert beides dasselbe B (c = 6 B mal 0,9168, beta = 61,56 B). Auf dem Gitter gilt das nur fuer eine
    kovariante Konstruktion.
- Diskrepanz: Erwartet c = -0,148 (S) bzw. -0,130 (C), gemessen +0,111 +- 0,045. Der Abstand 0,259 ist 0,259/0,045 =
  5,8 SE. Der SE-Beitrag von S^4 in c-Einheiten ist 0,052/11,19 = 0,005 und spielt keine Rolle. Gezeigt ist damit nur:
  Mindestens eine der beiden Konstruktionen traegt nicht kovariante Anteile von der Ordnung des Signals.
- Fuer die Torus-Seite spricht [ES]: Dort unterscheiden sich die Regeln schon in erster Ordnung (Frage 5), und die
  Liste in ERGEBNIS 7 ist plausibel.
- Gegen eine glatte Lesart sprechen zwei Punkte:
  - Das Torus-Vorzeichen ist selbst schwach: 2,5 SE bei rho = 1; bei rho = 0,5 ist c = -0,017 +- 0,045, erwartet waere
    0,111 mal 0,707 = 0,078.
  - Auch die S^4-Regeln sind nicht allgemein kovariant (Frage 2). Ein Gitter-B, das zwischen "R aus Gradienten" und
    "R homogen" unterscheidet, waere ebenfalls eine Nicht-Kovarianz, und die koennte auch auf der S^4-Seite liegen.
- "Kehrbefund" und "das Gegenteil des Torus-Befunds" (KARTE KUGEL-GEGENLESEN) gelten nur unter H-kov. Gemessen sind zwei
  verschiedene Groessen, die einander nur unter dieser Annahme widersprechen (Befund A1).

## Frage 7: Rueckwaerts

**Urteil: Keine Selbstanzeige aendert das Urteil.** Fundstellen: ERGEBNIS Kopf und 6; PLAN 10; EINGEFROREN-SHA256.txt;
rauch-69/rauch-a.json.

- Auswerteskript waehrend der Rauchlaeufe:
  - Geprueft: auswertung_kugel.py mtime 10:57, Rauchstart 10:56:16 CEST, Einfrieren 11:02:55, Hauptlaeufe ab 11:03:07
    CEST.
  - Die Rauchdateien enthalten nur Streuungsfelder (jq: blind_streuung.../std_je_wurzelN, keine Mittel, kein Gamma).
  - Alle eingefrorenen Kopien sind bytegleich mit den Arbeitsfassungen, und die sha256 stimmen mit
    EINGEFROREN-SHA256.txt.
  - Eine Ausgangskenntnis ist nicht erkennbar.
- Festlegung auf korr:
  - Getroffen vor den Hauptlaeufen, mit Kenntnis der Volumenverhaeltnisse, aber ohne Gamma-Werte.
  - Fuer die Kernaussage (Gamma negativ) ist sie ohne Belang, weil roh dasselbe Vorzeichen hat.
  - Sie wirkt nur auf KU4, Gamma_M (C) und die S/C-Reihenfolge. Inhaltlich ist sie ohnehin die richtige Fassung
    (Frage 2).
- "2 SE" in KU2: Bei entgegengesetztem Vorzeichen (Abstand 2,89 bei SE 0,5) ist KU2 in jeder Lesart verfehlt.
- Weitere Rueckwaerts-Funde in registerfreien Stellen:
  - "exakt kovariant" in ERGEBNIS 1.1 und 7 (Befund B1).
  - "das induzierte Regge-Glied ... [E]" in ERGEBNIS 1.1: Gemessen [E] ist das sqrt(N)-Glied. Dass es das
    Regge/Einstein-Glied ist, ist [M] und haengt an der Isometrie-Invarianz (Befund C2).
  - "Konvention" in ERGEBNIS 1.3 und 7 (Befund B2).
  - "KU3 nicht eingetroffen ... das Vorzeichen ist robust gegen die Laengenregel" (ERGEBNIS 2) gilt fuer zwei verwandte
    Sehnenregeln (B3).
  - KU4 ist nur im Wortlaut getroffen; das zeigt der Agent selbst an (C3).

## Frage 8: Folgetest

**Urteil: Das gestauchte S^4 als konvexe Huelle ist nicht der schaerfste Test und so auch nicht sauber auswertbar
(Befund A2). Schaerfer und billiger sind zwei weitere Laengenregeln gepaart auf denselben S^4-Netzen: Regel G
(geodaetisch) und Regel Q (volumentreu je Simplex).**

Gegen das Ellipsoid (Huelle in R^5) [M]:
1. **Stationaer:** Bei festem Volumen ist Int sqrt(g) R eine symmetrische Funktion der Halbachsen
   a_i = a(1 + eps_i). Ihre erste Ordnung ist proportional zu Sum eps_i, und das ist bei festem Volumen 0 (dasselbe sagt
   Hilbert: Einstein-Metriken sind kritische Punkte). Das Signal ist also O(eps^2 sqrt(N)). Dasselbe gilt fuer jedes
   aeussere Integral, sodass innen und aussen nur ueber die Koeffizienten zweiter Ordnung trennbar sind. Dafuer braucht
   es ein grosses eps.
2. **Huelle ist nicht das innere Delaunay:** conv(A X) = A conv(X). Die Huelle auf E = A S^4 ist also das Bild des
   sphaerischen Delaunay der Urbilder, Delaunay in der runden Urbildmetrik und nicht in der Metrik von E. Die Simplizes
   sind dadurch lokal um bis zu eps gestreckt. Gamma je Punkt aendert sich dann in O(eps^2) (die erste Ordnung
   verschwindet aus Isotropie), also um ein Glied ~ N eps^2, das der flache Torus nicht abzieht. Gegen das Signal
   eps^2 sqrt(N) ist das etwa sqrt(N)-mal groesser (31 bis 89 bei N = 1000 bis 8000, mal einem unbekannten
   Koeffizientenverhaeltnis). Ein freies N-Glied im Fit kostet viel SE (vgl. PLAN S5 fuer ln N).
3. **Regel S ist dort nicht definiert:** Die Radialprojektion ist auf E nicht die natuerliche Abbildung.
4. Wer das Ellipsoid trotzdem will (Tensorform, ERGEBNIS 7 (c)), braucht zuerst eine **2D-Vorprobe:** Ellipsoid gegen
   S^2 bei gleichem N. Dort ist Int R = 8 pi formunabhaengig und K skaleninvariant, also muss Gamma_E - Gamma_S
   intrinsisch O(1) sein. Ein Glied ~ N zeigt die Streckung der Huelle direkt; das kostet Sekunden je Saat. Fuer 4D
   braucht es danach eine innere Triangulierung.

Empfohlener Test: **Regeln G und Q gepaart auf denselben S^4-Netzen**
- **G:** Laenge = a arccos(x_i . x_j/a^2). Das ist allgemein intrinsisch (innerer Abstand, inneres Delaunay). beta_G
  misst also per Konstruktion nur die innere Geometrie, und auf S^4 ist das nur R. Der Vergleich G gegen C beziffert,
  was die Sehnen an Einbettung tragen. G ist auch die einzige Regel, mit der der Satz "ein kovariantes Netz gibt
  Einsteins Vorzeichen" wirklich gedeckt waere (B1).
- **Q:** wie S, aber J_T ersetzt durch das Quadraturmittel ueber das Simplex. V_Q liegt schon vor (V_Q/V_K = 0,99791
  bis 0,99977).
  - Umrechnung fuer Q, N = 1000: 249,75 mal ln(1/0,99791) = 249,75 mal 0,00209 = 0,52, durch 31,62 ergibt 0,017
    sqrt(N).
  - N = 8000: 1999,75 mal 0,00023 = 0,46, durch 89,44 ergibt 0,005 sqrt(N).
  - Also ist roh = korr bis auf 1 % von beta. Damit erledigt Q die Volumenfrage der Leitung per Konstruktion; es prueft
    zugleich das lokale Volumenglied (Frage 1, Zeile 2).
- **Paarung:**
  - Gleiche Saaten und rng-Schluessel geben gleiche Huellen. Gamma_C und Gamma_S muessen dann bitgleich zu lauf-69
    herauskommen; das ist eine Reproduktionsprobe gratis.
  - Paardifferenzen rauschen wie S - C (0,011 je Saat). Mit 10 Saaten ist SE(Differenz) etwa 0,011/3,16 = 0,0035 und
    SE(beta) etwa 0,33/3,16 = 0,10; das reicht fuer das Vorzeichen.
- **Zeit [ES, nicht gemessen]:** zwei Kugel-LU mehr je Netz, geschaetzt plus 40 bis 60 %. Bei N = 8000 also hoechstens
  3 Saaten je Lauf (3 mal 84 s mal 1,6 = 403 s = 6,7 min). Alternativ zuerst ohne 8000; ohne 8000 ergab sich
  -1,624 +- 0,091.
- **Annahmepruefungen:** G-Simplizes einbettbar (nicht_einbettbar = 0); V_G/V_K vorab berichten.

**Ableitbarkeitsprobe**
- Vorab ableitbar, also keine Messung: V_G/V_K, V_Q/V_K, beide Umrechnungen (Q hoechstens 0,017 sqrt(N)), die
  Einbettbarkeit und die Reproduktion von Gamma_C und Gamma_S.
- Rohdatenprobe (jq keys, messung-n4-N1000-s0.json): Je Regel stehen nur V, gamma, gamma_M, korr, korr_M, sum_log_m,
  lam_min, m_min und LU-Daten in der Datei, dazu geo mit a, V_K, V_C, V_S, V_Q und halb_int_R. Es gibt keine Kanten-,
  Simplex- oder K^-1-Daten. Gamma_G und Gamma_Q sind daraus nicht ableitbar, nicht einmal in erster Ordnung
  (1/2 Spur K^-1 dK).
- Sichtprobe:
  - Wer korr fuer richtig haelt, erwartet beta_Q,roh nahe beta_S,korr und beta_G nahe beta_C, jeweils im Abstand der
    Groesse S - C.
  - Beides kann scheitern. beta_G >= 0 oder beta_Q,roh >= 0 oeffnet die Vorzeichenfrage wieder. Ein Abstand weit ueber
    0,2 hiesse, dass die Volumenverteilung je Simplex ein sqrt(N)-Glied traegt, das die globale Umrechnung nicht
    erfasst.
  - Schwellen und Wahrscheinlichkeiten setzt die Leitung (Rollentrennung).
- Projekt-grep (12:06, RUNDE-37, "geodaet/geodät/geodesic"): Treffer nur fuer geo+ auf Torus und 2D. In kugel.py dient
  arccos nur den Diederwinkeln (Regge). Eine S^4-Rechnung mit geodaetischen Laengen gibt es nicht; ERGEBNIS 7 sagt
  dasselbe.
- Zweite Prioritaet, fuer Frage 6: das Torus-Schema auf S^4 uebertragen (ERGEBNIS 7 (b)). Punkte nach e^(4 sigma)
  streuen, runde Huelle, Laengen nach sp, und dann gegen B_S vergleichen. Das prueft das [H] zum Torus direkt, ist aber
  kein Zehn-Minuten-Umbau.

## Befunde A/B/C mit Vorschlag

A = vor der Meldung an Finn bzw. vor dem Folgetest zu beheben; B = im Text zu berichtigen; C = Kleinigkeit.

- **A1 (Lesart der Meldung; Fragen 1, 2 und 6):**
  - Gedeckt ist: Das sqrt(N)-Glied ist auf einem isometrie-invarianten S^4-Netz fuer zwei verwandte Sehnenregeln und
    zwei Masse negativ, und unter dieser Invarianz ist es das Einstein-Glied.
  - Nicht gedeckt sind "ein kovariantes Netz gibt Einsteins Vorzeichen" in allgemeiner Form (keine allgemein intrinsische
    Regel gerechnet) und "Das Torus-Vorzeichen kam aus nicht kovarianten Anteilen" als Befund. "Kehrbefund" bzw.
    "das Gegenteil des Torus-Befunds" gilt nur unter H-kov.
  - Vorschlag im Wortlaut fuer die Meldung: "Auf einem symmetrischen Zufallsnetz auf der 4-Kugel hat die induzierte
    Wirkung gegenueber dem flachen Torus ein negatives sqrt(N)-Glied: beta = -1,65 +- 0,05 (stat.), Spanne zwischen
    den zwei Laengenregeln 0,20, alle 40 Saaten negativ, unabhaengig von der Volumenumrechnung. Wegen der
    Kugelsymmetrie ist das das Einstein-Glied mit positivem G, gezeigt fuer Sehnen- und Schwerpunktlaengen. Das
    widerspricht mit 5,7 SE der Annahme, der Torus-Wert c = +0,111 messe dasselbe kovariante B. Welche Konstruktion
    nicht kovariante Anteile traegt, ist offen [H: eher der Torus]. Eine allgemein intrinsische Regel (geodaetische
    Laengen) steht aus."
- **A2 (Folgetest; Frage 8):** Das gestauchte S^4 als Huelle in R^5 ist nicht inneres Delaunay. Seine Streckung
  erzeugt ein Glied ~ N eps^2, das der Torus nicht abzieht, gegen ein Signal ~ eps^2 sqrt(N) (Int R ist bei festem
  Volumen stationaer); Regel S ist dort nicht definiert. Das betrifft nur den Plan, nicht den Befund.
  - Vorschlag: "Folgetest zuerst: Regeln G (geodaetisch) und Q (volumentreu je Simplex) gepaart auf denselben
    S^4-Saaten, mit bitgleicher Reproduktion von Gamma_C und Gamma_S. Ellipsoid erst nach einer 2D-Vorprobe und nur
    mit innerer Triangulierung."
- **B1 ("exakt kovariant", KARTE KUGEL-1, ERGEBNIS 1.1 und 7):** Vorschlag: "isometrie-invariant; Punktprozess und
  Triangulierung sind auf S^4 intrinsisch, die Laengenregeln C und S sind ueber die Einbettung definiert und nur auf
  der nabeligen Kugel intrinsisch."
- **B2 ("Konvention", "einziger Hebel", ERGEBNIS 1.3 und 7):** Vorschlag: "Die Umrechnung ist die von 'Zahl = Volumen'
  verlangte Normierung auf das Volumen, das der Operator sieht. roh vergleicht bei der Dichte N/V_R (Regel C,
  N = 1000: 1,245) mit Dichte 1; die Differenz ist genau das Kosmologieglied. Das positive Gamma_M roh mit Sehnen
  (+0,16) ist daher keine Gegenlesart."
- **B3 (Unsicherheit; ERGEBNIS 1.1, 2 zu KU3):** Die SE ist rein statistisch. Vorschlag: "beta_S = -1,65 +- 0,05
  (stat.); systematisch Regelspanne C-S 0,20, weitere Regeln nicht gerechnet." Statt "das Vorzeichen ist robust
  gegen die Laengenregel": "gleiches Vorzeichen fuer zwei verwandte Sehnenregeln."
- **C1 (2D-Kontrolle, ERGEBNIS 1.2):** Vorschlag: "Fehlerprobe der Konstruktion mit vorab feststehendem Ausgang
  beta_2D = 0; ueber Volumenumrechnung, Regel S und O(h^2)-Glieder in 4D sagt sie nichts."
- **C2 ("Regge-Glied ... [E]", ERGEBNIS 1.1):** Vorschlag: "gemessen [E]: negatives sqrt(N)-Glied; Einstein-Glied [M],
  unter Isometrie-Invarianz."
- **C3 (KU4):** Wie der Agent selbst schreibt, ist KU4 nur im Wortlaut getroffen. Der Kartensatz "Das Mass bestimmt
  das Vorzeichen mit" gehoert nicht in die Meldung.

## Einfach gesagt

Der Agent hat ein Zufallsnetz auf eine vierdimensionale Kugel gelegt und gemessen, ob die Kruemmung die Netzenergie
senkt oder hebt. Sie senkt sie, in allen 40 Wiederholungen, und das passt zu Einsteins Schwerkraft. Die grosse
Volumenumrechnung ist kein Trick: Ohne sie vergleicht man ein zu kleines Netz mit einem richtig grossen, und fuer die
Hauptgroesse bleibt das Vorzeichen sogar ohne sie gleich. Nicht bewiesen ist dagegen, warum der fruehere Torus-Test
das andere Vorzeichen zeigte. Ausserdem sind erst zwei sehr aehnliche Regeln fuer die Kantenlaengen gerechnet. Der
naechste kleine Test sollte deshalb dieselben Netze mit echten Kugelabstaenden und mit volumengenauen Bausteinen
nachrechnen. Eine gestauchte Kugel bringt eigene Fehler mit, die groesser waeren als das Signal.
