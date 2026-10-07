# GUERTEL-2: Ergebnis (Runde 42; Teil A Staley-Weg, Teil B Guertel im Feld)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 17:13:05 CEST. Code 17:33 bis 17:36 CEST; Plantext ab 17:36:53 CEST, vor jedem Lauf.
  - Rauchlauf 15:38:39 bis 15:49:39 UTC (12 Units ueber kleintest.sh, Spur cpu10, alle rc = 0).
  - Eingefroren 17:50:29 CEST (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe 15:50:39 bis 16:40:01 UTC: 18 Units (17 Rechnungen und die Auswertung), alle rc = 0, keiner wiederholt.
  - Nachtrag N1: Vorhersage 18:13:32 CEST in PLAN.md, Lauf 16:18:01 bis 16:22:07 UTC (rc = 0).
  - Text ab 18:18:58 CEST.
- **Kennzeichen:**
  - [M] Mathematik
  - [E] Messung im Modell (synthetisch, keine Messdaten)
  - [H] Hypothese; [L] Gedaechtnis
  - [R] im Rauchlauf vor dem Einfrieren gesehen
- **Art:** synthetische Modellrechnung an Modellknoten und Modellfeldern, keine Messdatenbestaetigung.

## Ergebnis zuerst

1. **Teil A, Tetraeder-Knoten: Die Sperre S ist nicht bestimmt; die Methode ist gescheitert [E].**
   - Der Staley-Weg als Schalendrehung ist bei 16 bzw. 12 Segmenten nicht durchdringungsfrei (GZ0a verfehlt).
     Laeuft die Drehachse n(s) durch (+-1, 1, 0)/sqrt(2), liegen zwei Faeden in einer Drehebene, und die
     Segment-Sehnen schneiden sich.
   - Die Stringrelaxation repariert das nicht. S1 (beide Laengen) und S2 bleiben ungueltig und konvergieren nicht. Die
     Hoehe der ungueltigen Wege (um 485 bzw. 1200 ueber dem Start) ist keine Sperre.
   - Urteile: GZ1 formal nicht eingetroffen (String ungueltig), GZ2 nicht auswertbar.
2. **Die 720-Grad-Entwirrung findet sich auch mit mehr Aufwand nicht von selbst [E].**
   - Die ideale 4-pi-Wicklung relaxiert in eine Zwischenrast: L = 1,8 bei E = 170,74, W_x = (1, 0, 0, 1), das
     20-Fache des Grundzustands.
   - Die Temperaturleiter bis T0 = 4 ab X_W = (1, 0, 1, 0) entwirrt in keiner von 15 Saaten.
   - E_min(0) bleibt 8,409. GZ3 ist nach Plan nicht auswertbar, weil die heissen Stufen die Sonde verletzen; beschreibend
     gibt es keinen tieferen Zustand.
3. **Teil B, Ebene (SO(2)-Feld): Die Verdrillung sammelt sich an; GZ4 ist eingetroffen [E].**
   - E_min = 0; 175; 695; 1550; 2718 bei 0 bis 1440 Grad, also nahezu k^2.
   - Auf (16, 64) gibt es keinen Gittersprung. Auf groberen Gittern endet das mit dem ersten Sprung.
4. **Teil B, Raum (SO(3)-Feld): Der Guertel-Effekt zeigt sich auf unseren Gittern nicht [E].**
   - Die Vorwaertsverdrillung waechst ueber 360 Grad hinaus weiter, bis eine Bindung den Drehwinkel pi erreicht. Dann
     springt das Feld auf dem Gitter: grob bei 270 Grad, fein (6, 24) bei 450 Grad, (12, 24) bei 540 Grad (Nachtrag
     N1).
   - Danach ist E 360-periodisch. Auf (6, 24) und (12, 24) gilt E(720) = E(360) > 0, nicht E(0). Auf (3, 12) ist schon
     E(360) = 0, weil der Sprung vor 360 Grad liegt.
   - GZ5 ist nicht auswertbar (720 und 1440 Grad nur im gesprungenen Zustand), GZ6 ebenso (beide Strings ungueltig).
   - Beschreibend: Der **gebaute** Feld-Staley-Weg ist sprungfrei und hat aus der 4-pi-Verdrillung keine Sperre. Seine
     Energie ist erst flach, dann fallend. Die Relaxation nimmt trotzdem den Gittersprung.
5. **Bedeutung [H]:**
   - Topologisch ist der Guertel in beiden Modellen erlaubt. Mit einfacher Relaxation erreichbar ist er in keinem: Die
     Faeden rasten in Zwischenstellungen ein, das Feld weicht in einen Gittersprung aus.
   - Fuer Finns Frage heisst das: Den Guertel-Effekt zwischen Innen- und Aussenfeld gibt es im glatten Feld
     (Finkelstein-Rubinstein; [M] Topologie, [L] Literatur). In unseren diskreten Modellen gewinnt bisher der Gitterweg. Ob das an der Glaette oder an
     der Relaxation liegt, entscheidet erst ein gezielter Stoss in Staley-Richtung (Kartenvorschlag 1).

## Urteile (lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Wortlaut | tragende Werte |
|---|---|---|---|---|---|
| GZ0 | Kontrollen: Anfangsstring durchdringungsfrei an jedem Bild; trivialer Weg S = 0 auf 1 % | 85 % | **nicht eingetroffen** | **nicht eingetroffen** | Staley-Bau gueltig an 576 von 721 (L 1,8) bzw. 653 von 721 (L 1,3) Bildern, min Faden-Faden 0,00045 bzw. 0,00094; S0 = 0,236 (L 1,8; Plan-Grenze 0,412, Wortlaut-Grenze 0,084) und 3,7e-6 (L 1,3), beide gueltig |
| GZ1 | [H] L = 1,8: String endet ohne Durchdringung entwirrt, S < dE_360 | 40 % | **nicht eingetroffen** (String ungueltig; Sperre nicht bestimmt) | **nicht eingetroffen** (dito) | S1 ungueltig, nicht konvergiert; Start 170,744, W_x = (1, 0, 0, 1); Ende B0 entwirrt; S_plan/S_wort am Ende 7731/7893 (nicht urteilsfaehig); dE_360 = 41,24 |
| GZ2 | [H] S(1,8) < S(1,3), wenn beide Wege gefunden | 65 % | **nicht auswertbar** | **nicht auswertbar** | beide S1 ungueltig |
| GZ3 | [H] Staerkere Abkuehlung: E_min(0) mindestens 10 % unter GUERTEL-1 | 50 % | **nicht auswertbar** (60 % gueltige Saaten < 80 %) | **nicht auswertbar** | beschreibend: alle 20 Saaten 8,409; E_min(0)_neu/G1 = 1,00000; L 1,3: alle 5,1096 (50 % gueltig) |
| GZ4 | Kontrolle 2D (SO(2)): E_min waechst je Umdrehung bis 1440 Grad | 85 % | **eingetroffen** | **eingetroffen** | (16, 64): 0; 174,69; 695,19; 1550,22; 2718,11; Stufen 175, 520, 855, 1168; E(1440)/E(360) = 15,56; alle Zustaende gueltig |
| GZ5 | [H] 3D (SO(3)): E_min saettigt, E_min(720) innerhalb 10 % bei E_min(0), E_min(360) deutlich darueber | 45 % | **nicht auswertbar** | **nicht auswertbar** | (6, 24): 720 und 1440 Grad 0 von 5 gueltig (Gittersprung); ohne Sonde E_min(720) = E_min(360) = 3608,5, E_min(0) = 0 |
| GZ6 | [H] Sperre im Feld kleiner als im Faden, bezogen auf dE_360 | 40 % | **nicht auswertbar** | **nicht auswertbar** | Feld-String ungueltig (Start gesprungen), Faden-String ungueltig; gebauter Feld-Weg ohne Sperre, Faden-Bau mit Durchdringung (beschreibend) |

- Die Urteile nach Plan und nach Wortlaut stimmen ueberall ueberein. Bei GZ0 unterscheidet sich der Wortlaut nur im
  S0-Teil; das Ergebnis ist dasselbe, weil GZ0a in beiden Lesarten verfehlt ist.
- **GZ1 formal:** Die Planregel macht einen ungueltigen String zu "nicht eingetroffen". Inhaltlich ist die Sperre
  nicht gemessen (Selbstanzeige 6).
- **Nachtrag N1** (beschreibend, kein Urteil): Vorhersage "stetig entdrillt auf (12, 24)" (45 %) nicht eingetreten.

## Teil A: Faden-Knoten (GUERTEL-1-Modell, zweizaehlige Achse, Koerper bei 720 Grad = Identitaet)

### A1. Temperaturleiter (GZ3) [E]

| L | Winkel | T0 | Endenergien (5 Saaten) | Sonde gueltig | Windung W_x (gerundet) |
|---|---|---|---|---|---|
| 1,8 | 0 | 0,5 / 1 / 2 / 4 | alle 8,409 (= B0) | 5 / 5 / 2 / 0 | 0 0 0 0 |
| 1,8 | 720 (ab X_W) | 1 | 175,336 (4x), 176,335 | 5 | 1 0 1 0 |
| 1,8 | 720 | 2 | 175,336 (3x), 176,034, 176,431 | 5 | 1 0 1 0 |
| 1,8 | 720 | 4 | 175,336 (3x), 170,840, 170,744 | 4 | 1 0 1 0, eine Saat 1 1 1 0 (170,840) |
| 1,3 | 0 | 0,5 / 1 / 2 / 4 | alle 5,1096 (= B0) | 5 / 4 / 1 / 0 | 0 0 0 0 |

- **0 Grad:** Keine Saat findet einen tieferen Zustand als B0 (8,409 bzw. 5,1096). Die heissen Stufen verletzen die
  Sonde, deshalb sind nur 12 von 20 (L = 1,8) bzw. 10 von 20 (L = 1,3) Saaten gueltig.
- **Warum E bei 90 Grad tiefer liegt [M]:** In GUERTEL-1 war die Energie bei 60 bis 90 Grad tiefer (2,82 gegen 8,41).
  Das ist kein verpasstes Minimum bei 0 Grad. Der Abstand Ansatz-Anker waechst mit der Drehung: bei 0 Grad 1,8, bei
  90 Grad um x |2,9 u - 1,1 Rot(x, 90) u| = 2,74. Die schlaffen Faeden (Kontur 3,24) sind dann weniger gestaucht und
  weniger gebogen.
- **720 Grad ab X_W:** Keine der 15 Saaten entwirrt. Der tiefste Zustand ist 170,744 mit W_x = (1, 0, 1, 0), fuer
  T0 = 4.

### A2. Staley-Weg und Startzustaende [E]

- **Reproduktion:** Das wiederholte GUERTEL-1-Protokoll trifft X_W und B0 bitgleich (Abweichung 0,0;
  E(720) = 177,279).
- **GZ0a, Bau:** Der Weg ist nicht durchdringungsfrei.
  - L = 1,8: 576 von 721 Bildern gueltig; kleinster Faden-Faden-Abstand 0,00045 (Grenze 0,1).
  - L = 1,3: 653 von 721, kleinster Abstand 0,00094.
  - Der Koerper wird nie geschnitten (min rho 1,078 bzw. 1,084).
  - Die verletzten Bilder liegen nur in Phase 1, um n(s) = (1, 1, 0)/sqrt(2) und (-1, 1, 0)/sqrt(2). Bei s = 0,
    s = 0,5 und in Phase 2 ist der Weg sauber.
  - **Mechanismus [M]:** Steht n senkrecht auf zwei Ansatzrichtungen, zum Beispiel n = (1, 1, 0)/sqrt(2) auf
    (1, -1, -1) und (-1, 1, -1), liegen beide Faeden in derselben Drehebene. Ihre Spiralarme haben bei 2 pi auf 0,81
    Radius nur etwa 0,25 Abstand. Die Sehnen der Segmente (etwa 0,85 rad Drehung je Segment) schneiden dann ineinander.
    Fuer duenne, fein unterteilte Faeden gilt der Bau weiter [M]; bei 16 Segmenten nicht.
- **Ideale 4-pi-Wicklung, relaxiert (Start S1):** Sie entwirrt sich nicht von selbst.
  - L = 1,8: FIRE (1114 Schritte, Sonde bestanden) endet bei E = 170,744 mit W_x = (1, 0, 0, 1) und W_y = W_z = 0.
    Das ist eine Zwischenrast. Sie hat auf 1e-7 dieselbe Energie wie die beste heisse Leitersaat (170,743907,
    W_x = (1, 0, 1, 0)); die Windungen sind dort nur anders auf die Faeden verteilt.
  - L = 1,3: E = 584,361, W_x = (0, 1, 1, 0) (3104 Schritte).
- **Energie entlang des Anfangsstrings** (S1, L = 1,8, jedes 20. von 201 Bildern):
  - 170,7; 1000,6; 9524; 1,2e6; 25591; 25253; 17962; 9824; 4004; 789; 8,4.
  - An den Bildern mit Ueberlappung steigt das Maximum bis 9,7e24 (Abstossung bei fast null Abstand).

### A3. Stringrelaxation S1 (Hauptweg) [E]

| L | gueltig | E(Start) | E(Ende) | S am Ende (plan / wort) | S im Verlauf (Iteration 2500 bis 5000) | laufende Probe | Endpruefung |
|---|---|---|---|---|---|---|---|
| 1,8 | nein | 170,744 | 8,409 | 7730,6 / 7892,9 | 484 bis 494, dazwischen Spitzen bis 902 (danach bis 7731) | min Faden-Faden 0,00012; Rand -0,47 | alle Bilder in den Grenzen, aber Rand zwischen Bildern -0,53; Bildabstand bis 0,34 |
| 1,3 | nein | 584,361 | 5,110 | 214127 / 214706 | 1201 bis 1277, Spitzen bis 6e6 | min 0,00024; Rand -0,27 | 200 von 201 Bildern; Rand -0,40 |

- **S-Verlauf L = 1,8 (alle 250 Iterationen ab 1000):** 1043, 569, 569, 1679, 614, 502, 489, 494, 486, 486, 485, 486,
  651, 902, 485, 485, 491, 2559, 540, 584, 2136, 557, 502, 504, 3841, 1431, 735, 2029, 7731.
  - Bis etwa 3000 faellt der Wert und pendelt dann um 485.
  - Ab 5000 kommen Spitzen an Bild 128 bis 130 immer haeufiger (Faeden werden zusammengedrueckt).
- **Energieprofil am Ende** (L = 1,8, jedes 10. Bild): 170,7; 175,1; 222; 539; 444; 415; 597; 575; 445; 488; 623;
  623; 626; 7901; 244; 326; 460; 160; 9,8; 8,5; 8,4.
- **W_x entlang des (ungueltigen) Wegs:** Er wechselt mehrfach, zum Beispiel (1, 0, 0, 1), (1, 1, 0, 1),
  (0, 1, 1, 0). Es gibt auch Bilder mit W_x = 0 bei hoher Energie (vgl. die Achsenwanderung in GUERTEL-1).
- **Lesart:** Der relaxierte Weg ist kein Entwirrungsweg ohne Durchdringung. Seine Hoehe (um 485 bei L = 1,8 bzw.
  1200 bei L = 1,3) ist **keine Sperre**: Ein Weg mit Durchdringung kann Abkuerzungen nehmen oder Ueberlappung
  bezahlen. Die Sperre S bleibt unbestimmt.

### A4. S2 (vom Zwischenrast-Zustand X_W) und S0 (trivial) [E]

- **S2 (L = 1,8):**
  - Der Anfangsweg (X_W -> kompensiertes Protokoll -> Staley) hat schon im kompensierten Teil Ueberlappungen: 645 von
    779 Bildern gueltig, min Faden-Faden 0,016. Die Kompensation dreht radiale Perlenbewegungen bis zu 4 pi mit; das gibt
    Spruenge bis 0,28 zwischen Aufzeichnungen.
  - Relaxiert ist S2 ungueltig (min Faden-Faden im Lauf 1,3e-5, Rand -2,2).
  - S springt bis zum Ende zwischen 2e4 und 9e14, ohne sich zu setzen. Am Ende sind es 1,48e6 an Bild 50.
  - Energieprofil am Ende (jedes 20. Bild): 177,3; 173,8; 484; 431; 519; 537; 627; 243; 461; 10,3; 8,4. Die Spitzen
    liegen zwischen diesen Bildern.
  - **Keine Sperre bestimmbar.**
- **S0 (trivialer Weg 0 -> 0, GZ0b):** gueltig bei beiden Laengen.
  - L = 1,8: S = 0,236 (Verlauf alle 1000 Iterationen: 10,36; 3,54; 2,10; 1,33; 0,85; 0,55; 0,36; 0,24). Das liegt
    unter 1 % von dE_360 (0,412), aber ueber 1 % von E(B0) (0,084).
  - L = 1,3: S = 3,7e-6.

## Teil B: Orientierungsfeld

### Modell (PLAN B1)

- Gitter Z^3 bzw. Z^2 in einer Kugel bzw. Scheibe. Der Kern |x| <= r0 dreht um z mit Winkel theta, der Rand |x| > R
  steht fest.
- Kopplung je Nachbarbindung 3 - tr(R_a^T R_b) (3D, SO(3)) bzw. 2 - tr(R_a^T R_b) (2D, SO(2)).
- Quasistatisch in 10-Grad-Schritten mit Relaxation, Gitterwinkel alle 90 Grad.
- **Sonde "Gittersprung":** min q_a . q_b > 0 in 3D (stetige Hebung nach SU(2)), max |phi_a - phi_b| < pi in 2D.
  Spruenge aendern die Klasse, die im Kontinuum erhalten waere.

### B1. Energie E(theta) des Drehprotokolls [E]

| theta | 2D (16, 64) | 2D (6, 24) | 2D (3, 12) | 3D grob (3, 12) | 3D fein (6, 24) |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 90 | 10,9 | 10,7 | 10,4 | 111,3 | 232,3 |
| 180 | 43,7 | 42,6 | 41,2 | 435,2 | 924,5 |
| 270 | 98,3 | 95,5 | 91,3 | 111,4 (S) | 2060,7 |
| 360 | 174,7 | 168,9 | 158,0 | 0 (S) | 3608,5 |
| 450 | 272,7 | 262,1 | 33,3 (S) | 111,3 (S) | 1742,2 (S) |
| 540 | 392,2 | 373,8 | 41,2 (S) | 435,2 (S) | 924,5 (S) |
| 630 | 533,1 | 502,2 | 91,3 (S) | 111,4 | 2060,7 (S) |
| 720 | 695,2 | 393,6 (S) | 158,0 (S) | 0 | 3608,5 (S) |
| 810 | 878,2 | 262,1 (S) | 33,8 (S) | 111,3 | 1742,1 |
| 900 | 1081,9 | 373,8 (S) | 41,2 (S) | 435,2 | 924,5 |
| 1080 | 1550,2 | 392,8 (S) | 158,0 (S) | 0 (S) | 3608,5 |
| 1440 | 2718,2 | 392,9 (S) | 158,0 (S) | 0 | 3608,5 (S) |

- (S): Zustand nach einem Gittersprung (Sonde verletzt). 3D fein bei 1170 bis 1440 Grad wie bei 450 bis 720 Grad.
- **Groesster Bindungswinkel vor dem ersten Sprung:**
  - 2D (16, 64) bei 1440 Grad: 2,15 rad, kein Sprung.
  - 3D fein bei 360 Grad: min q . q = 0,583, also 1,90 rad.
  - Die Abschaetzung im Plan (1,40 rad) unterschaetzt das um den Faktor 1,36. Grund sind die Ecken der Kugel aus
    Gitterwuerfeln.

### B2. E_min mit Saaten (Protokollzustand plus 4 Stoesse, rms 0,1 rad) [E]

| Gitter | 0 | 360 | 720 | 1080 | 1440 |
|---|---|---|---|---|---|
| 2D (16, 64) | 0 (Rest 5e-6), 5/5 gueltig | 174,69, 5/5 | 695,19, 5/5 | 1550,22, 5/5 | 2718,11, 5/5 |
| 2D (6, 24) | 0, 5/5 | 168,95, 5/5 | 168,95, 0/5 | 168,95, 0/5 | 168,95, 0/5 |
| 2D (3, 12) | 0, 5/5 | 158,04, 5/5 | 158,04, 0/5 | 158,04, 0/5 | 158,04, 0/5 |
| 3D grob (3, 12) | 0, 5/5 | 0, 0/5 | 0, 5/5 | 0, 0/5 | 0, 5/5 |
| 3D fein (6, 24) | 0, 5/5 | 3608,52, 5/5 | 3608,52, 0/5 | 3608,52, 5/5 | 3608,52, 0/5 |

- **2D:** Die Verdrillung sammelt sich an. E_min(k 360)/E_min(360) = 1; 3,98; 8,87; 15,56, also nahezu k^2. Das ist
  das Bild der Ebene mit pi_1(SO(2)) = Z. Auf den groberen Gittern endet es mit dem ersten Sprung.
- **3D fein:** Die Vorwaertsverdrillung waechst ueber 360 Grad hinaus weiter, gueltig.
  - Schrittwerte vor der Gitter-Relaxation: 3611 (360, Sonde 0,612), 4413 (400, 0,436), 5481 (450, 0,084). Der Anstieg
    von 360 auf 450 Grad ist das 1,52-Fache; quadratisch waere 1,56.
  - Bei der laengeren Relaxation am Gitterwinkel 450 Grad springt das Feld (Sonde -0,994, E faellt auf 1742). Die Sonde
    zeigt den Sprung genau dort, wo die Bindungen den Drehwinkel pi erreichen.
  - Danach ist E 360-periodisch: E(540) = E(180), E(720) = E(360).
  - Der zweite Sprung zwischen 720 und 810 Grad stellt die Klasse wieder her (Sonde 0,097 bei 810 Grad); 1080 Grad ist
    wieder gueltig, mit E = 3608,5.
  - Die Stoesse bei 720 Grad bleiben alle im gesprungenen Zustand (3608,52, Sonde -0,976).
  - Der stetige Entdrillweg, also der Guerteltrick im Feld, wird auf diesem Gitter nicht gefunden.
- **3D grob:** Die Verdrillung waechst bis 270 Grad (Schrittwert 923, Sonde 0,31) und springt bei der Relaxation dort.
  Danach ist E 360-periodisch, mit Gitterwerten bis 435 bei 180 Grad.
- **Gemeinsam ueber alle 3D-Gitter:** Es gibt keinen stetigen Entdrillschritt. Der Vorwaertsast endet jedes Mal erst,
  wenn eine Bindung den Winkel pi erreicht.
  - grob bei 270 Grad, fein bei 450 Grad, (12, 24) bei 540 Grad (Nachtrag N1).
  - Je glatter das Gitter, desto spaeter der Sprung. Ein Abbiegen in den Guerteltrick zeigt sich bis dahin nicht.

### B3. Feld-Sperre (Feld-Staley-Weg bei 720 Grad) [E]

- **Gebauter Weg (3D fein, 81 Bilder):** durchweg sprungfrei (min q . q = 0,365).
  - Energie in Phase 1 konstant 13825,5 (jedes 10. Bild), wie in PLAN 0 Punkt 3 vorhergesagt [M]. Die Naht-Bindungen
    aendern das um weniger als 0,05.
  - Phase 2 faellt ueber 7860, 3588 und 912 auf 0.
  - **Entlang des gebauten Wegs gibt es aus der 4-pi-Verdrillung keine Sperre** (beschreibend; der Weg ist nicht
    relaxiert).
- **Relaxierter Start:** FIRE ab der 4-pi-Verdrillung (Rauschen 1e-3, 348 Schritte) endet bei E = 3608,52. Das ist ein
  gesprungener Zustand (Sonde -0,967). Der Steilabstieg nimmt also den Gittersprung, nicht den flachen Staley-Weg.
- **String (17 Bilder, 250 Iterationen):** ungueltig, weil schon der Start gesprungen ist (Sonde der ersten sieben
  Bilder < 0, Nachbarpruefung -0,99).
  - S_plan = 722,5, S_wort = 4331,0. Beide sind wegen der Ungueltigkeit nicht urteilsbildend.
  - S-Verlauf: 10217, 4265, 1792, 1267, 825, 722,5 (Iteration 0 bis 250 in 50er-Schritten), also nicht konvergiert.
- **3D grob:** Schon die 4-pi-Verdrillung hat dort Bindungen ueber pi; Start und String sind ungueltig.

## Nachtrag N1: glatteres 3D-Gitter (12, 24), beschreibend

- **Lauf und Aenderungen:**
  - Lauf 16:18:01 bis 16:22:07 UTC, rc = 0, eingefrorener Code. Vorhersage vorher in PLAN.md (18:13:32 CEST).
  - Kern r0 = 12, Rand R = 24, 65.267 Plaetze, 50.624 frei.
  - Protokoll bis 720 Grad, Stoesse bei 720 Grad.
- **Energie und Sonde (min q . q):**

| theta | 0 | 90 | 180 | 270 | 360 | 450 | 540 | 630 | 720 |
|---|---|---|---|---|---|---|---|---|---|
| E | 0 | 691,7 | 2756,3 | 6161,1 | 10848,1 | 16722,4 | 13178,3 (S) | 6161,1 (S) | 10848,1 (S) |
| Sonde | 1 | 0,987 | 0,945 | 0,869 | 0,738 | 0,489 | -1,000 | -0,994 | -0,989 |

- **Feinverlauf ueber 360 Grad:** E steigt glatt weiter, ohne Sprung und ohne stetiges Entdrillen:
  - 9149 (330), 10849 (360), 12682 (390), 14642 (420), 16726 (450), 18919 (480), 22755 (530 Grad, Sonde 0,01).
  - Bei 540 Grad faellt die Sonde unter null (-0,14), bei 550 Grad ist das Feld gesprungen (E = 12628).
- Bei 720 Grad bleiben alle vier Stoesse im gesprungenen Zustand (10848,05, Sonde -0,989).
- **Vorhersage N1** (stetig entdrillt, E(720) <= 0,10 E(360); 45 %): **nicht eingetreten.** Eingetreten ist der
  dritte Ausgang (Vorwaertsast ueber 360 Grad hinaus) mit anschliessendem Gittersprung.
- **Lesart [E, H]:**
  - Im Kontinuum ist der Vorwaertsast jenseits von 360 Grad ein Sattel [M]. Seine instabile Richtung (Kippen der
    Drillachse) waechst aber nahe 360 Grad nur langsam.
  - Mit 30 FIRE-Schritten je 10 Grad und Rauschen 1e-3 erreicht das Protokoll den Bereich grosser Bindungswinkel, bevor
    die Instabilitaet sichtbar wird. Dort oeffnet sich der Gittersprung und gewinnt.
  - Ob der Ast auf dem Gitter echt metastabil ist oder nur langsam zerfaellt, zeigt diese Rechnung nicht.

## Kontrollen

1. **Reproduktion GUERTEL-1 [E]:** Das wiederholte Drehprotokoll (drei Systeme, gleiche Saat) trifft B0 und X_W
   bitgleich. Die Naht zwischen kompensiertem Protokollweg und Staley-Weg stimmt auf 1,3e-15.
2. **GZ0a (Bau durchdringungsfrei):** verfehlt (A2).
3. **GZ0b (trivialer Weg):** Nach Plan bestanden (S0 = 0,236 bzw. 3,7e-6, beide gueltig, unter 1 % von dE_360),
   nach Wortlaut bei L = 1,8 nicht (0,236 > 1 % von E(B0) = 0,084). Die Stringmethode ist also gueltig, aber langsam.
   Im ersten Rauchlauf (2000 Iterationen, dts 1e-4) war S noch 16,1.
4. **GZ4 (2D-Feld):** eingetroffen. Kein Gittersprung bis 1440 Grad auf (16, 64); das Wachstum ist nahezu
   quadratisch.
5. **Sonden schlagen an, wo sie sollen:**
   - Faden: Die Anfangsstrings mit Ueberlappung und die relaxierten S1-Wege werden als ungueltig erkannt. Die
     FIRE-Rahmen der Startrelaxation (225 bzw. 152) und S0 bestehen.
   - Feld: Jeder Gittersprung erscheint als Vorzeichenwechsel von min q . q (3D) bzw. als |phi_a - phi_b| > pi (2D).
     Nach zwei Spruengen ist die Klasse wieder die alte (3D fein bei 810 und 1080 Grad, 3D grob bei 720 Grad), wie es
     Z_2 verlangt.
6. **Code und Daten:**
   - Alle 19 Laufdateien (Haupt- und Nachtrag) tragen kopf.code_sha256 = c9374a98... (guertel2.py, eingefroren) und
     g1_code_sha256 = 795f474d... (GUERTEL-1). auswertung.json traegt ff45b824... (eingefroren).
   - 51 von 51 Laufdateien haben auf beiden Rechnern dieselbe sha256 (lauf-69/PRUEFSUMMEN.txt, PRUEFSUMMEN-69-roh.txt;
     Nachtrag 3 von 3).
   - Der 2D-Hauptlauf (16, 64) wiederholt den Rauchlauf wertgleich (gleiche Parameter, gleiche Saat); nur Kopf und
     Laufzeit sind anders.

## Ableitbarkeit

- **Vorab ableitbar, nur Kontrolle [M]:**
  - Existenz des Entwirrungswegs fuer duenne Faeden.
  - 720-Periodizitaet von E_min im SO(3)-Kontinuum, Wachstum wie theta^2 im SO(2)-Kontinuum; GZ4 bestaetigt Letzteres
    auf dem feinen 2D-Gitter.
- **Gemessen, nicht ableitbar [E]:**
  - Die Diskretisierungsgrenze des Baus (Sehnen bei zwei Faeden in einer Drehebene).
  - Die Relaxation der idealen Wicklung in eine Zwischenrast (170,744 bzw. 584,361).
  - Keine Entwirrung bis T0 = 4.
  - Der Gittersprung im 3D-Feld bei 270 Grad (3, 12), 450 Grad (6, 24) und 540 Grad (12, 24, Nachtrag). Davor waechst
    der Vorwaertsast ueber 360 Grad hinaus weiter.
  - Der Faktor 1,36 zwischen geschaetztem und gemessenem groesstem Bindungswinkel.
- **Nicht bestimmt:** die Sperre S, sowohl im Fadenmodell als auch im Feld.

## Selbstanzeigen

1. **Reihenfolge:** Den Code (17:33 bis 17:36 CEST) habe ich vor dem Plantext (ab 17:36:53) geschrieben, beides vor
   jedem Lauf.
2. **Im Rauchlauf gesehen:**
   - Laufzeiten, Speicher und die Reproduktion.
   - Die Kontrollfelder GZ0a, einschliesslich der Lage der verletzten Bilder.
   - Den S-Verlauf der S0-Strings (GZ0b) und die 2D-Energien aller drei Gitter (GZ4).
   - Nicht gelesen habe ich die Startzustaende von S1/S2, die Energieprofile, die Leiterwerte und die 3D-Feldwerte. Sie
     stehen in den Rauchlaufdateien (rauch-69/), ich habe sie per jq ausgespart.
3. **Aenderungen nach dem Rauchlauf, vor dem Einfrieren (PLAN, Abschnitt Rauchlauf):**
   - Faden-String: dts 1e-4 -> 3e-4 und niter 2000 -> 8000. Gewaehlt nach zwei Blicken auf die GZ0b-Kontrolle
     (S = 16,1 bei 2000 Iterationen, 0,854 bei 5000). Das ist eine Kalibrierung an der Kontrolle; die Regel (1 % von
     dE_360) blieb.
   - Feldparameter (10-Grad-Schritte, weniger FIRE-Schritte, M = 17) wegen der Laufzeit.
   - Saaten des feinen 3D-Gitters in zwei Laeufen, mechanisch per jq zusammengefuehrt.
   - auswertung2.py: Konvergenzbezug bei 75 % von niter.
4. **GZ0a im Rauchlauf verfehlt, Bau nicht geaendert.** Damit startete der Hauptweg S1 mit Ueberlappungen. Ein
   geaenderter Bau haette die Kontrolle nachtraeglich passend gemacht.
5. **Moegliche Mitursache [H]:** Mit dts = 3e-4 sind tiefe Faden-Kontakte (Kontaktsteifigkeit mal dts > 2) nur durch
   die Schrittkappe 0,005 gebremst. Die spaeten Spitzen im S-Verlauf (ab etwa 5000 Iterationen) koennen deshalb auch
   vom groesseren Schritt kommen, nicht nur von den Anfangsueberlappungen. Getrennt geprueft habe ich das nicht.
6. **GZ1 formal "nicht eingetroffen":** Die Planregel (ungueltiger String = nicht eingetroffen, weil die Karte "ohne
   Durchdringung" vorhersagt) ist mechanisch angewandt. Inhaltlich ist die Sperre nicht bestimmt: Die Methode ist
   gescheitert, eine hohe Sperre ist nicht gemessen.
7. **Abschaetzung im Plan zu optimistisch:** groesster Bindungswinkel 1,40 rad geschaetzt, gemessen 1,90 rad (3D fein
   bei 360 Grad). Mit der richtigen Zahl haette das Urteilsgitter einen groesseren Kern gebraucht. Mit diesem Code und
   10 min je Lauf war das nicht moeglich (Nachtrag N1 rechnet (12, 24) nur bis 720 Grad).
8. **Nachtrag N1 nach dem Einfrieren:** Vorhersage mit Zeit (18:13:32 CEST) vor dem Lauf in PLAN.md; beschreibend,
   aendert kein Urteil.
9. **Werkzeuge:**
   - Lokal ausserhalb der Liste: ls, cat, tail, head, wc, cut, comm, sort, uniq, find, xargs, ps (nur meine
     ssh-Prozesse), nohup, Shell-Schleifen in Warte- und Monitor-Aufgaben. Kein lokaler Interpreter.
   - Auf der .69 ausserhalb des Starters: ls, cat, tail, du, find, xargs, sort, touch, uptime, systemctl --user
     list-units (nur lesend), Warteschleifen mit sleep in den Ketten; jq auch zum Zusammenfuehren der Saaten.
   - Kein Python ausserhalb von kleintest.sh.
10. **Dateien:**
    - Code per scp als neue Dateien. Lokale Korrekturen an guertel2.py und auswertung2.py vor dem Hochladen ueber .neu
      und mv; keine laufende Datei ueberschrieben.
    - Lauf N1 ging zwischen die Hauptlaeufe (Lock-Reihenfolge nicht festgelegt), auf derselben Spur cpu10.
11. **Zeitbox** 180 min ab 17:13:05 CEST. Kein Journaleintrag, kein Peerbus, kein Commit.

## Kartenvorschlaege (hoechstens zwei)

1. **GUERTEL-FELD-STAB-1 [H]: Sattel oder Rast? Der Vorwaertsast jenseits von 360 Grad auf dem glatten Gitter.**
   - **Rechnung:** (12, 24) bis 420 und 450 Grad drehen (gueltig nach N1). Dann gezielt in Staley-Richtung stoessen:
     Die Drillachse wird in der inneren Haelfte um eps gekippt, eps = 0,01, 0,1, 0,3. Danach lange relaxieren
     (FIRE 3000) mit Gittersprung-Sonde.
   - **Vorhersage [M fuer das Kontinuum, H fuer das Gitter]:** Der Ast ist ein Sattel; der Stoss fuehrt ohne Sprung in
     die umgekehrte Verdrillung (E faellt auf etwa E(720 - theta)). Wahrscheinlichkeit 50 %.
   - **Ableitbarkeitsprobe:** Im Kontinuum ableitbar (konjugierter Punkt). Auf dem Gitter nicht, weil die
     Bindungswinkel bei 450 Grad schon 2,1 rad betragen.
   - **Kann scheitern:** Der Stoss endet im Gittersprung oder faellt in den Ast zurueck.
   - **Laufzeit:** etwa 64 ms je Schritt, also etwa 3,5 min je Stoss; drei Laeufe.
2. **GUERTEL-3 [H]: Staley-Weg mit 32 Segmenten und FIRE-String.**
   - **Bau:** Gleiche Kontur, doppelte Segmentzahl. Die Drehung je Segment halbiert sich, die Sehnenabweichung
     viertelt sich [M]. Dann sollte GZ0a bestehen.
   - **Rechnung:** String mit FIRE-Dynamik statt gekapptem Gradientenschritt, wieder S gegen dE_360 bei 1,3 d und
     1,8 d.
   - **Ableitbarkeitsprobe:** Dass der Bau besteht, ist abschaetzbar; die Sperre nicht.
   - **Laufzeit:** Paarkosten etwa vierfach. Bei M = 201 sind das mehr als 10 min, also GPU-Spur oder kuerzere Wege
     noetig.

## Dateien

- **Plan:** PLAN.md (mit Abschnitt Rauchlauf und Nachtrag N1), PLAN.md.eingefroren-20261004-175029,
  EINGEFROREN-SHA256.txt.
- **Code:** code/guertel2.py (neue Modi), code/guertel.py (GUERTEL-1, unveraendert, sha256 795f474d...),
  code/auswertung2.py, je mit .eingefroren-20261004-175029.
- **Eingaben:** eingaben-g1/protokoll-L1.8.npz und -L1.3.npz (Kopien aus GUERTEL-1, sha256 wie dort).
- **Rauchlauf:** rauch-69/t/ (Zeitmessung), rauch-69/kontrolle/ (GZ0, GZ4, erster Versuch), rauch-69/kontrolle2/
  (zweiter S0-Versuch).
- **Hauptlaeufe:** lauf-69/
  - leiter-*, pfad-*, string-S{0,1,2}-*, feld-*; saat-a/ und saat-b/ (Teile der feinen 3D-Saaten).
  - auswertung.json; PRUEFSUMMEN.txt; Logs; kette-*.out.
- **Nachtrag N1:** lauf-69/nachtrag/.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/runde42-guertel-2/ (code/, rauch/, lauf/, nachtrag/, eingaben-g1/).

## Einfach gesagt

Wir wollten am Knoten mit vier Faeden messen, wie viel Energie der Weg kostet, auf dem sich die Faeden nach zwei
Umdrehungen wieder entwirren. Den Weg haben wir nach der Mathematik nachgebaut, doch mit nur 16 Gliedern je Faden
schneiden sich die Faeden an einigen Stellen, und die Rechnung konnte das nicht reparieren; die Hoehe der Huerde bleibt
offen. Im zweiten Teil lag statt der Faeden ein Feld aus kleinen Drehrahmen um einen drehenden Kern, und in der Ebene
sammelt sich dort die Verdrehung wie erwartet Umdrehung fuer Umdrehung an. Im Raum muesste sie sich nach zwei
Umdrehungen aufloesen (der Guerteltrick hinter dem halben Spin), doch auf unserem Rechengitter springt das Feld vorher
ruckartig, sodass sich alles schon nach einer Umdrehung wiederholt. Ob ein feineres Gitter oder ein gezielter Anstoss
den Guerteltrick doch erreicht, muss die naechste Rechnung zeigen.
