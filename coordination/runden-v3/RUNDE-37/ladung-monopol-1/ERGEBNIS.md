# LADUNG-MONOPOL-1, Teil A: Ergebnis (Runde 38, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 06:02:30 CEST, Plantext ab 06:22:42 CEST.
  - Rauchlaeufe 04:24:20 bis 04:32:53 UTC (rauch1, rauch2, rauch3).
  - Eingefroren 06:33:15 CEST: PLAN.md.eingefroren-20261004-063315, Code-Kopien *.eingefroren-20261004-063315,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe (UTC):
    - gitter-a (L = 12, 16) 04:33:31 bis 04:34:47
    - gitter-b (L = 24) 04:34:51 bis 04:37:01
    - schwelle-24 04:37:07 bis 04:41:53
    - schwelle-1612 04:42:09 bis 04:43:23
    - scan (L = 16) 04:43:23 bis 04:45:05
    - auswertung 04:46:02 bis 04:46:05
  - Alle Laeufe auf Spur p4000a, rc = 0, nie zwei zugleich. Text ab 06:38:45 CEST (Kopf), Hauptteil ab 06:43:47 CEST.
- **Code:** Nach dem Einfrieren unveraendert; die Pruefsummen auf der .69, lokal und eingefroren stimmen ueberein
  (EINGEFROREN-SHA256.txt). auswertung.py lief beim ersten Start fehlerfrei.
- **Rechenart:** Alle Zahlen stammen aus einer Einteilchen-Gitterrechnung auf der .69 (numpy 2.4.4, scipy 1.18.0,
  complex128; CPU in der Spur p4000a, wie im Auftrag vorgegeben). Es gibt keine Messdaten.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (hier kein neuer Abruf; nur ueber das Dossier)
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [M] eigene Mathematik (Schreibtisch, PLAN Abschnitte 1.3 und 2)
  - [E] hier gerechnet
  - [H] Hypothese
  - [F] Festlegung im Plan

## 1. Ergebnis zuerst

1. **Ja, auf dem Gitter: q = 1 gibt ein Dublett, q = 2 ein Triplett [E].**
   - Bei L = 24 ist die tiefste gebundene Stufe an jedem Raster-V0 ueber der Schwelle genau 2-fach (q = 1) bzw. genau
     3-fach (q = 2), ohne Monopol (q = 0) einfach. Bei L = 12 und 16 ist es ebenso.
   - Sogar die tiefste Stufe ueberhaupt hat bei jedem V0 die Groesse 1, 2, 3 (q = 0, 1, 2), auch ungebunden bei V0 = 0
     und direkt an der Schwelle. Im feinen Raster (L = 16, V0 = 0 bis 12 in Schritten von 0,25) gilt das an allen
     49 Werten.
   - Es gibt keine Kreuzung zwischen Schwelle und tiefem Topf.
2. **Das Kommutatorzeichen ist s = (-1)^q, exakt [E, vorab M].**
   - Als Operator ist U_x U_y U_x^-1 U_y^-1 = -1 (q = 1) bzw. +1 (q = 0, 2), mit Rest <= 6e-14.
   - Das gilt auf jeder Stufe; jede q = 1-Stufe ist gerade (2 oder 4).
   - Das ist die projektive Darstellung eines halbzahligen Drehimpulses. Sie war vorab herleitbar: die Schleife der
     beiden pi-Drehungen umschliesst den halben Monopolfluss.
3. **Schwellen (L = 24, Kartenkriterium):** V0c = 2,0132 (q = 0), 2,6167 (q = 1), 3,1099 (q = 2).
   - Der Quotient V0c(1)/V0c(0) = 1,2998 liegt 0,0002 unter der Bandgrenze 1,3.
   - **LM4 ist damit knapp nicht eingetroffen.** Das Vorzeichen stimmt. Die Bandgrenze liegt innerhalb der
     Bisektionsunsicherheit [1,2992; 1,3003].
   - Mit dem reinen Energiekriterium waere der Quotient 1,556.
4. **Groessenkonvergenz: LM5 nicht eingetroffen [E].**
   - Ab V0 = 6 stimmt die tiefste Stufe zwischen L = 16 und 24 auf <= 1,1e-10 ueberein, bei V0 = 12 alle gebundenen
     Stufen auf <= 6e-14.
   - Nahe der Schwelle nicht: q = 1, V0 = 3 weicht um 2,2e-5 ab, die dritte Stufe bei q = 1, V0 = 8 um 4,5e-6.
   - 28 von 30 Vergleichen liegen unter 1e-6.
5. **Der tiefe Topf ist die Wuerfelgrenze aus dem Plan [M, E].**
   - Bei V0 = 12 sind alle 8 Wuerfelzustaende gebunden, mit den Stufenfolgen 1+3+3+1, 2+4+2 und 3+2+3. Die Energien
     liegen bei -V0 + eps_q - 0,23 (eps_q = -3; -sqrt6; -2).
   - Damit war LM2/LM3 im tiefen Topf vorab ableitbar (Kartenberichtigung K1).
   - Neu ist nur der Befund, dass die Ordnung bis zur Schwelle haelt.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 4 durch code/auswertung.py; Werte in lauf-69/auswertung.json. Die Felder "vermerk" sind per jq
nachgetragen; ohne sie ist die Datei identisch mit lauf-69/auswertung.maschine.json (diff), deren sha256 in
lauf-69/PRUEFSUMMEN.txt der .69 steht (dort unter dem Namen auswertung.json).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| LM0 | q = 0: s = +1, tiefste gebundene Stufe einfach; Eich-Rest <= 1e-10; String-Richtung egal auf 1e-10 | 95 % | **eingetroffen** | eingetroffen | c = +1 (Rest 0); tiefste gebundene Stufe einfach an 17 von 17 gebundenen (L, V0); lsqr-Rest <= 2,7e-14; String-Differenz <= 2,1e-14 (q = 0: exakt 0) |
| LM1 | q = 1: s = -1 auf allen Stufen, jede gerade; q = 2: s = +1 | 90 % | **eingetroffen** | eingetroffen | c = -1 bzw. +1, Operatorrest <= 5,8e-14; s auf 253 vollen Stufen auf <= 3,4e-15; keine ungerade q = 1-Stufe |
| LM2 | q = 1, L = 24, jedes V0 ueber der Schwelle: tiefste gebundene Stufe genau 2-fach | 80 % | **eingetroffen** | eingetroffen | V0 = 3, 4, 6, 8, 12: 2-fach; Zweitlauf gleich (dE <= 1,1e-14); oberes Bisektionsende V0 = 2,6172: 2-fach |
| LM3 | q = 2, gleiche Bedingungen: genau 3-fach | 70 % | **eingetroffen** | eingetroffen | V0 = 4, 6, 8, 12: 3-fach; Zweitlauf gleich; oberes Bisektionsende V0 = 3,1104: 3-fach |
| LM4 | V0c(1) > V0c(0); V0c(1)/V0c(0) in [1,3; 3,0] | 60 % | **nicht eingetroffen** (Grenzfall) | nicht eingetroffen | 2,6167/2,0132 = 1,2998; Unsicherheit [1,2992; 1,3003] schliesst 1,3 ein; Vorzeichen eingetroffen |
| LM5 | gebundene Eigenwerte L = 16 gegen 24 auf 1e-6 gleich | 85 % | **nicht eingetroffen** | nicht eingetroffen | max abs(dE) = 2,2e-5 (q = 1, V0 = 3); 2 von 30 Vergleichen > 1e-6; Stufengroessen ueberall gleich |

- **Lesarten:**
  - Plan und Kartenwortlaut geben dieselben Urteile.
  - LM0 (d) gilt auch dann, wenn man wie die Karte nur q = 0 nimmt; dort ist die Differenz exakt 0.
  - LM4 ist nur fuer L = 24 festgelegt [F]. Bei L = 16 ist der Quotient 1,2999, bei L = 12 1,3056.
- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "LM2 und LM3 treffen ein": Auf dem Gitter wird ein spinloses Teilchen am Monopol zu Spin q/2.
  - Die Austauschstatistik ist damit nicht gezeigt, ebenso wenig, dass das Quanten-Pfeil-Eis Monopole hat.
  - "LM4 ausserhalb des Bandes": nur beschreiben. Der Quotient liegt auf der Bandkante; die Kontinuumsabschaetzung D4
    (1,9 fuer die Energieschwelle) trifft auch das Energiekriterium (1,556) nicht.

**Agenten-Vorhersagen** (PLAN Abschnitt 6, vor jeder Rechnung)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (75 %) | E_0 + 12 - eps_q in [-0,30; -0,15] bei L = 24, V0 = 12 | **eingetroffen**: -0,2332 (q = 0), -0,2368 (q = 1), -0,2390 (q = 2) |
| A2 (90 %) | Operator-c = (-1)^q, Rest <= 1e-12; Drehdefekte <= 1e-12 | **eingetroffen**: Rest <= 5,8e-14, Defekte <= 2,3e-13 |
| A3 (85 %) | lsqr-Rest <= 1e-10; String-Differenzen <= 1e-11 | **eingetroffen**: <= 2,7e-14; <= 2,1e-14 |
| A4 (85 %) | LM2 und LM3 eingetroffen, auch am oberen Bisektionsende | **eingetroffen** |
| A5 (55 %) | V0c(0) in [1,6; 2,8], V0c(1) in [2,4; 4,5], Quotient in [1,25; 2,0], LM4 eingetroffen | **nicht eingetroffen**: die drei Zahlenteile treffen (2,013; 2,617; 1,2998), LM4 aber nicht |
| A6 (70 %) | V0c(2) > V0c(1); V0c(2)/V0c(0) in [1,6; 3,0] | **nicht eingetroffen**: 3,110 > 2,617 ja, Quotient 1,545 |
| A7 (60 %) | LM5 nicht eingetroffen; kleinstes gebundenes V0 je q: dE in [1e-6; 1e-3]; V0 >= 8: <= 1e-9 | **nicht eingetroffen** im Ganzen: Urteil richtig; dE = 6,0e-7 (q = 0) und 6,6e-7 (q = 2) liegen unter 1e-6; bei V0 = 8 4,5e-6 (q = 1) und 2,3e-7 (q = 2) |
| A8 (75 %) | Tiefer Topf: erste angeregte Stufe q = 1 Quartett (abs(chi(C4)) = 0), q = 2 Zweierstufe (abs(chi(C3)) = 1) | **eingetroffen** |

## 3. Tabellen

### 3.1 Tiefste Stufe bei L = 24 [E]

"geb." = Kartenkriterium (E < -6,001 und Gewicht in r <= 3 mindestens 0,9). Die Groesse m gilt fuer die tiefste Stufe
ueberhaupt; sie ist an allen gebundenen Punkten zugleich die tiefste gebundene.

| V0 | q = 0: E (m, Gewicht) | q = 1: E (m, Gewicht) | q = 2: E (m, Gewicht) |
|---|---|---|---|
| 0 | -5,952688 (1; 0,063) | -5,936775 (2; 0,031) | -5,924872 (3; 0,018) |
| 1 | -5,963615 (1; 0,154) | -5,938665 (2; 0,042) | -5,925459 (3; 0,021) |
| 2 | -6,175132 (1; 0,896), nicht geb. | -5,953390 (2; 0,192) | -5,927452 (3; 0,034) |
| 3 | **-6,824201 (1; 0,992)** | **-6,365734 (2; 0,971)** | -6,027965 (3; 0,824), nicht geb. |
| 4 | **-7,638629 (1; 0,999)** | **-7,132076 (2; 0,997)** | **-6,720715 (3; 0,993)** |
| 6 | **-9,443135 (1)**, gebunden 1+3 | **-8,909459 (2)**, gebunden 2+4 | **-8,471996 (3)**, gebunden 3+2 |
| 8 | **-11,340372 (1)**, 1+3+3 | **-10,798653 (2)**, 2+4+2 | **-10,354920 (3)**, 3+2+3 |
| 12 | **-15,233191 (1)**, 1+3+3+1 | **-14,686301 (2)**, 2+4+2 | **-14,238976 (3)**, 3+2+3 |

- s auf der tiefsten Stufe: +1, -1, +1 (q = 0, 1, 2) auf <= 3,4e-15, an allen Punkten.
- **Phasenfreie Kennzahlen [E]:**
  - q = 1: Zweierstufen haben abs(chi(C4)) = sqrt2, Viererstufen 0. Das passt zu Gamma6/Gamma7 bzw. Gamma8 (Quartett,
    j = 3/2-artig).
  - q = 2: Dreierstufen haben abs(chi(C3)) = 0 (T1/T2), Zweierstufen abs(chi(C3)) = 1 und abs(chi(C4)) = 0 (E).
  - Gamma6 gegen Gamma7 und T1 gegen T2 bleiben ohne Festlegung der Drehphase offen (PLAN Abschnitt 3).

### 3.2 Schwellen V0c [E]

Bisektion auf Breite <= 1e-3 (Breite der Endklammer 9,8e-4); angegeben ist die Mitte.

| L | V0c(0) Karte | V0c(1) Karte | V0c(2) Karte | V0c(1)/V0c(0) | V0c(0) Energie | V0c(1) Energie | V0c(2) Energie | Quotient Energie |
|---|---|---|---|---|---|---|---|---|
| 12 | 1,9399 | 2,5327 | 3,0122 | 1,3056 | 1,5806 | 2,3530 | 2,9614 | 1,489 |
| 16 | 1,9995 | 2,5991 | 3,0854 | 1,2999 | 1,5317 | 2,3306 | 2,9487 | 1,522 |
| 24 | **2,0132** | **2,6167** | **3,1099** | **1,2998** | 1,4858 | 2,3120 | 2,9409 | 1,556 |

- Die Gebunden-Flags auf dem Raster sind in allen 18 Reihen monoton.
- **Am oberen Bisektionsende** (L = 24) liegt das Gewicht bei 0,9002 bis 0,9004. Die Bindung unter der Bandkante
  betraegt dort:
  - q = 0: 0,182 (E = -6,1819, einfach)
  - q = 1: 0,132 (E = -6,1317, 2-fach)
  - q = 2: 0,086 (E = -6,0864, 3-fach)
- Am Kartenkriterium entscheidet also das Gewicht, nicht die Energie. Mit Monopol erreicht der Zustand die 90 % schon
  bei kleinerer Bindung. Darum ist der Kartenquotient (1,30) kleiner als der Energiequotient (1,56).
- Die Kartenschwelle steigt mit L leicht (1,940, 1,9995, 2,013 fuer q = 0), vermutlich weil die kleine Box ausgedehnte Zustaende
  nach innen drueckt [H]. Die Energieschwelle faellt mit L.

### 3.3 Groessenkonvergenz L = 16 gegen L = 24 (LM5) [E]

| q | V0 | Stufe (m) | abs(dE) |
|---|---|---|---|
| 0 | 3 | 0 (1) | 6,0e-7 |
| 0 | 4 | 0 (1) | 5,5e-9 |
| 0 | 6 / 8 / 12 | alle gebundenen | <= 3,0e-9 / <= 4,4e-10 / <= 6e-14 |
| 1 | 3 | 0 (2) | **2,2e-5** |
| 1 | 4 | 0 (2) | 5,9e-8 |
| 1 | 6 | 0 (2) / 1 (4) | 3,1e-11 / 3,7e-7 |
| 1 | 8 | 0 (2) / 1 (4) / 2 (2) | 2e-13 / 3,1e-11 / **4,5e-6** |
| 1 | 12 | alle gebundenen | <= 5e-14 |
| 2 | 4 | 0 (3) | 6,6e-7 |
| 2 | 6 | 0 (3) / 1 (2) | 1,0e-10 / 1,5e-7 |
| 2 | 8 | 0 (3) / 1 (2) / 2 (3) | 5e-13 / 1,4e-11 / 2,3e-7 |
| 2 | 12 | alle gebundenen | <= 5e-14 |

- Die Abweichung waechst, je schwaecher die Stufe gebunden ist (Abstand zur Bandkante -6). Die zwei Ausreisser sind
  q = 1-Stufen bei E = -6,37 und -6,01.
- Tief liegende Stufen sind bei L = 16 schon auf Rechengenauigkeit konvergiert.

### 3.4 Tiefer Topf gegen Wuerfelgrenze (V0 = 12, L = 24) [M, E]

| q | Wuerfel (Plan, Abschnitt 2) | gerechnet E + 12 (m) | Verschiebung |
|---|---|---|---|
| 0 | -3 (1), -1 (3), 1 (3), 3 (1) | -3,2332 (1), -1,2480 (3), 0,7368 (3), 2,7214 (1) | -0,23 bis -0,28 |
| 1 | -2,449 (2), 0 (4), 2,449 (2) | -2,6863 (2), -0,2553 (4), 2,1734 (2) | -0,24 bis -0,28 |
| 2 | -2 (3), 0 (2), 2 (3) | -2,2390 (3), -0,2537 (2), 1,7244 (3) | -0,24 bis -0,28 |

- Die Stufengroessen sind exakt die des Wuerfels. Die Verschiebung ist die zweite Ordnung ueber die 3 Aussenkanten je
  Ecke (Plan-Schaetzung -0,21).
- Die "Gitter-Zentrifugalkosten" der tiefsten Stufe sind 0,547 (q = 1) und 0,994 (q = 2), Wuerfelwerte 0,551 und 1,0.

### 3.5 Bild

- lauf-69/bild-eigenwerte.png: drei Felder q = 0, 1, 2. Punkte zeigen die tiefsten Stufen bei L = 16 im Schritt 0,25.
  Farbe und Form geben die Entartung (1 Kreis, 2 Quadrat, 3 Dreieck, 4 Raute); gefuellt heisst gebunden.
- Ringe mit Zahl: tiefste Stufe bei L = 24 auf dem Kartenraster.
- Gestrichelt die Grenze E = -6,001, gepunktet V0c(L = 24).
- **Zu sehen:**
  - Die Ringe (tiefste Stufe, L = 24) tragen bei q = 0, 1, 2 durchgehend die Zahlen 1, 2, 3.
  - Mit wachsendem V0 loesen sich nacheinander die Wuerfelzweige von der Bandkante: 1, 3, 3, 1 (q = 0), 2, 4, 2
    (q = 1), 3, 2, 3 (q = 2).
  - Im feinen Raster (L = 16, 49 Werte von 0 bis 12) ist die tiefste Stufe ueberall 1-, 2- bzw. 3-fach.

## 4. Kontrollen [E]

- **Fluss:** Auswaertssumme je Wuerfel <= 1,1e-16, Mittelwuerfel 2 pi auf 8,9e-16, max abs(Phi) = pi/3 auf 2,2e-16
  (alle L).
- **Eichfeld:**
  - lsqr-Rest <= 2,7e-14 (L = 12), <= 1,4e-14 (16), <= 1,7e-14 (24) fuer alle drei Strings.
  - Schliessung F = Phi - 2 pi n in jedem Wuerfel <= 1,8e-15.
- **Drehungen:**
  - Defekt max abs(g_i K^R_ij conj(g_j) - K_ij) <= 2,3e-13.
  - Symmetrie-Rest voller Stufen <= 8,2e-13 (Grenze 1e-6).
  - Imaginaerteil von s <= 9e-17.
- **Spektrum:**
  - Dicht (numpy) gegen eigsh mit Vervollstaendigung, L = 12, q = 0, 1, 2, V0 = 0, 4, 12: max abs(dE) <= 5,0e-14,
    Stufengroessen gleich an 9 von 9 Punkten.
  - Ritz-Residuen <= 1,1e-14, kein Ritz-Paar verworfen.
  - Die Vervollstaendigung hat an 39 von 72 Rasterpunkten 1 bis 4 Vektoren ergaenzt. Das sind abgeschnittene
    Randstufen und von eigsh verpasste Kopien.
- **String-Richtung** (+z gegen -z, +x; q = 0, 1, 2; alle L; V0 = 0, 4, 12): max abs(dE) der tiefsten 12 <= 2,1e-14.
- **Zweitlauf L = 24** (anderer Startvektor, ncv = 96; 9 Rasterpunkte und 2 Bisektionsenden): Stufengroessen gleich,
  Energien auf <= 1,1e-14.
- **Kato:** E_0(q) >= E_0(0) an allen (L, V0); keine Verletzung in 48 Vergleichen.

## 5. Kartenberichtigungen (vor dem Einfrieren offengelegt) und was daraus wurde

- **K1 (Ableitbarkeit LM2/LM3):**
  - Im tiefen Topf sind LM2/LM3 vorab ableitbar (Wuerfelspektrum, PLAN Abschnitt 2); gerechnet bestaetigt (3.4).
  - Echte Information der Karte ist nur: Die Ordnung haelt bis an die Schwelle, und bei V0 = 0 ist auch der tiefste
    Boxzustand schon 1/2/3-fach.
- **K2 (LM0, String bei q = 0 trivial):** bei q = 1, 2 mitgeprueft, besteht dort mit <= 2,1e-14.
- **K3 (LM4, Vorzeichen):**
  - Kato sichert nur die Energieschwelle. Sie haelt: 2,312 > 1,486, und E_0(q) >= E_0(0) ueberall.
  - Fuer die Kartenschwelle mit Gewichtskriterium stimmt das Vorzeichen auch (2,617 > 2,013), aber nicht zwingend.
- **K4 (operative Schwelle):**
  - Vorab geschaetzt war eine Bindung von ~0,15 an der Kartenschwelle. Gerechnet: 0,18 (q = 0), 0,13 (q = 1),
    0,09 (q = 2).
  - Die Energieschwelle bei L = 24 (1,486 fuer q = 0) liegt ueber der groben Greenfunktions-Schaetzung fuer das
    unendliche Gitter (~1,37 [L?]), wie fuer eine endliche Box zu erwarten.

## 6. Latten (v3)

- **L1 (kann scheitern):** ja.
  - Eine Kreuzung nahe der Schwelle (Quartett unter Dublett, Zweier unter Dreier) haette LM2/LM3 gekippt.
  - LM4 und LM5 sind tatsaechlich gescheitert, ebenso meine A5, A6, A7.
  - s war vorab hergeleitet; als Rechnung prueft es den Code (Karte: "ableitbar").
- **L2 (Gegenprobe):**
  - dicht gegen eigsh
  - drei String-Richtungen
  - Zweitlauf mit anderem Startvektor
  - Symmetrie-Vollstaendigkeit
  - Kato
  - Wuerfelgrenze (Schreibtisch gegen Rechnung)
  - drei Boxgroessen
- **L3 (Numerik):** Residuen 1e-13 bis 1e-16. Bisektion auf 9,8e-4; das ist beim Quotienten genau die
  entscheidende Stelle (LM4).
- **L4 (schon bekannt):**
  - Monopol-Kugelfunktionen, j >= q/2 im Kontinuum (Wu/Yang 1976) [L].
  - Ladung plus Monopol gibt halbzahligen Drehimpuls (Goldhaber 1976, Abstract [S] laut Dossier).
  - Projektive Darstellungen der Punktgruppe im Magnetfeld sind Lehrbuchstoff [L].
  - Eine Gitterrechnung genau dieser Art (Raumwinkel-Fluss, kubische Box, Kern-Topf) kenne ich nicht [L?]; nicht
    gesucht.
  - Neu fuer das Projekt [E]: Das Gitter haelt die Kontinuumsordnung j = q/2 bis zur Schwelle; Wuerfelspektrum;
    Schwellenquotienten.
- **L5 (Messbezug):** keiner. Das ist eine synthetische Einteilchen-Rechnung mit eingesetztem Monopol und
  eingesetztem Topf. Sie zeigt weder, dass das Pfeil-Eis Monopole hat, noch eine Austauschstatistik.

## 7. Selbstanzeigen

1. **Codefehler im Rauchlauf, vor dem Einfrieren behoben.**
   - eigsh nutzt fuer komplexe hermitesche Matrizen den Arnoldi-Treiber.
   - Bei q = 1, L = 12, V0 = 4 fehlte eine Kopie, und die Vektoren entarteter Stufen waren nicht orthogonal
     (PLAN Abschnitt 8).
   - Die Vervollstaendigung nutzt die Symmetrieoperatoren. Die Stufengroesse wird danach aus Eigenwerten bestimmt, aber
     der Raum, in dem sie gesucht wird, ist symmetrieabgeschlossen.
   - Unabhaengig geprueft ist das nur bei L = 12 (dicht, 9 Punkte). Bei L = 16 und 24 koennte eine zufaellige,
     nicht symmetriebedingte Entartung oder eine ganz verpasste Stufe unentdeckt bleiben. Das ist nicht beobachtet,
     aber auch nicht ausgeschlossen.
2. **Vorwissen aus dem Rauchlauf:** L = 12, V0 = 4 und 12 zeigten schon Dublett und Triplett unten (PLAN Abschnitt 8).
   Die Schwellenwerte von rauch3 habe ich nicht angesehen.
3. **Schwellen nur auf monotone Flags geprueft:** Monotonie ist nur auf dem Raster und entlang der Bisektion
   gesichert, nicht zwischen den Punkten.
4. **LM4 haengt an der vierten Stelle.**
   - Der Quotient 1,29978 liegt innerhalb der Bisektionsunsicherheit an der Bandgrenze.
   - Nach Planregel wird mit der Mitte geurteilt; das Urteil ist darum als Grenzfall vermerkt.
   - Eine feinere Bisektion habe ich nicht nachgeschoben, weil die Regel vorab galt.
5. **schwelle.json ist zusammengefuehrt:** lokal per jq aus schwelle-24.json und schwelle-1612.json, dann per scp auf
   die .69 (sha256 gleich). Die Teildateien liegen daneben.
6. **GPU ungenutzt:** Die Rechnung ist CPU-scipy in der Spur p4000a, wie im Auftrag vorgegeben (eigsh). Die
   Projektregel "auf CUDA" ist damit fuer diese Karte nicht erfuellt.
7. **Bildfarben:** Standardpalette der dataviz-Vorlage in fester Reihenfolge, dazu Markerformen als zweite Kodierung.
   Das Pruefskript der Vorlage (node) habe ich nicht laufen lassen, weil lokal kein Interpreter starten darf.
8. **Lokal:** kein python, awk oder perl. Benutzt habe ich jq, sed, grep, sha256sum, date, ssh und scp, dazu cp, mv,
   mkdir, ls, cat, cut, head, wc und diff. Auf der .69 ausserhalb des Starters nur Dateibefehle (mkdir, mv, ls, tail,
   grep, sha256sum) und die Abfrage laufender Units; kein Interpreterstart.
9. **Agenten-Vorhersagen verfehlt:** A5 (LM4-Teil), A6 (Quotient 1,545 statt >= 1,6), A7 (Zahlenteile). Ich hatte die
   Groessenfehler nahe der Schwelle zu gross und bei V0 = 8 zu klein geschaetzt; dass dort angeregte Stufen knapp
   unter der Bandkante gebunden sind, hatte ich nicht bedacht.
10. **Zeitbox:** Start 06:02:30, Abgabe 06:48:21 CEST (innerhalb von 90 min).

## 8. Bedeutung

- **Zu Finns Frage, ob ein spinloses Teilchen am Monopol zu Spin 1/2 wird: im Gitter-Einteilchenbild ja, bei Ladung 1.**
  - Die tiefste gebundene Stufe ist ein Dublett mit der Vertauschungsregel eines halbzahligen Spins (s = -1).
  - Bei Ladung 2 entsteht ein Triplett (Spin 1). Das ist der H2-Mechanismus mit Spin = q/2 (Dossier D1, SPIN1.md B-V3).
- **Was hineingesteckt ist:**
  - ein Gittermonopol mit exakt raumwinkeltreuem Fluss
  - ein Teilchen, das an dasselbe U(1) koppelt
  - ein Kern-Topf als Zusatzkraft
  - Ohne Topf gibt es keine Bindung (V0 = 0, L = 24: Gewicht <= 6,3 % in r <= 3), wie nach Kato erwartet.
- **Was nicht gezeigt ist:**
  - die Austauschstatistik zweier solcher Verbunde (Goldhaber [S])
  - dass Finns Netz Monopole hat (Quanten-Eis, Dossier O1)
  - Teil B (Pyrochlor-Kanten-Netz) und Teil C (Q-Ball)
- **Fuer Teil B [H]:** Auch auf dem Pyrochlor-Netz duerfte im tiefen Topf das Spektrum der Monopolzelle (Tetraeder)
  die Stufenordnung festlegen. Das laesst sich vorab am kleinen Zellgraphen rechnen, wie hier am Wuerfel.

## 9. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-063315, EINGEFROREN-SHA256.txt
- code/:
  - ladung_monopol.py: Gitter, Fluss, lsqr, Hamilton, Drehungen, Spektrum, Vervollstaendigung, Modi
  - auswertung.py: Urteile und Bild
  - je mit Kopie *.eingefroren-20261004-063315
- lauf-69/:
  - gitter-a.json/.log (L = 12, 16), gitter-b.json/.log (L = 24)
  - schwelle-24.json/.log, schwelle-1612.json/.log, schwelle.json (zusammengefuehrt)
  - scan.json/.log
  - auswertung.json (mit Vermerken), auswertung.maschine.json, auswertung.log, bild-eigenwerte.png
  - PRUEFSUMMEN.txt
- rauch-69/: rauch1.json/.log, rauch2.json/.log, rauch3-schwelle.json, rauch3.log
- Auf der .69: /home/fmh/fmhc-physics-remote/runde38-ladung-monopol/ (code/, rauch/, lauf/)

## 10. Einfach gesagt

Wir haben am Computer ein geladenes Teilchen, das sich selbst nicht dreht, auf ein Wuerfelgitter gesetzt, in dessen
Mitte ein magnetischer Pol sitzt, und es mit einer kleinen Mulde festgehalten. Mit einfacher Ladung gibt es den
tiefsten Zustand immer genau doppelt, wie beim Elektron mit seinem halben Spin; mit doppelter Ladung dreifach, wie bei
Spin 1. Ein Rechentest mit zwei halben Drehungen in verschiedener Reihenfolge ergibt bei einfacher Ladung ein
Minuszeichen, und das gibt es nur bei halbzahligem Spin. Die Antwort lautet also: Ja, das Teilchen wird im Gitter zu
einem Spin-1/2-Teilchen, aber nur bei Ladung 1 und nur, solange die Mulde es festhaelt. Ob sich zwei solche Paare beim
Vertauschen wie Elektronen verhalten, ist damit noch nicht gerechnet, und alles ist Rechnung, keine Messung.
