# REGGE-RAND-1: Ergebnis (Runde 36, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
  - Start 2026-10-03 23:04:00 CEST.
  - Plan geschrieben ab 23:26:14 CEST, eingefroren 23:35:10 CEST.
  - Hauptlaeufe 23:35:14 bis 23:42:00 CEST (Auswertung eingeschlossen).
  - Datei geschrieben ab 23:42:35 CEST (date).
- Alle Zahlen stammen aus Rechnungen auf der .69 (lauf-69/), Spur p4000a, reines numpy in float64. Es sind keine
  Messdaten.
- Kennzeichen:
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [S] an der Quelle gelesen, [H] Hypothese
  - [M] eigene Mathematik bzw. vorab ableitbar
  - [A] Festlegung des Agenten

## Ergebnis zuerst

1. **Die Fehlwinkel-Eckenregel ergibt auf dem Kuhn-Tetraedernetz exakt 8 x den Laplace-Operator des Wuerfelgitters.**
   - Der konforme Ansatz l_e = l0_e psi_e^2 wird linearisiert. Die Schablone des Eckenoperators ist dann:
     - Achsenkanten -8,000 (auf 2e-15)
     - Flaechen- und Raumdiagonalen <= 7e-15, also 0
     - Mitte 48
   - **Folge:** Die schiefen Kuhn-Diagonalen tragen in linearer Ordnung nichts bei. Das Feld kennt keine
     Vorzugsrichtung (1,1,1).
     - (1,1,0) und (1,-1,0) bzw. (1,1,1) und (1,1,-1) geben identische Werte; uebrig bleibt nur die kubische
       Gitterstruktur.
   - **Normierung exakt:** Ein quadratisches psi gibt an jeder Ecke -8 Laplace psi (auf 1e-14). Der Faktor 16 pi G der
     Karte stimmt also, und es folgt dpsi -> G M/(2r).
   - Vorab-Hypothese AP1 (70 %) eingetroffen. Grund [L?]: Das Kuhn-Netz ist eine entartete Delaunay-Zerlegung (alle 8
     Wuerfelecken auf einer Kugel); die dualen Flaechen der Diagonalen haben die Flaeche 0.
2. **RR0 und RR1 eingetroffen.**
   - Das Netz ist flach auf 2,7e-15, der Operator symmetrisch auf 5e-17. Die Konstante ist die einzige Nullmode.
   - Es gibt keine Schachbrettmoden. Die Schachbrettmode (pi,pi,pi) ist im Gegenteil die steifste Mode (96, das
     Maximum).
3. **RR2, RR3 und RR4 eingetroffen** (L = 64, torus-korrigiert):
   - r dpsi = G M/2 auf 0,77 %, ueber alle 16182 Gitterpunkte mit 6 <= r <= 16.
   - Richtungsschwankung bei r = 12: 0,41 % (Spitze-Spitze).
   - Kompakter und ausgedehnter Klumpen geben dieselbe Gauss-Masse auf 2e-14.
   - **Aber:** Sobald AP1 feststand (schon im Rauchlauf), waren RR1 bis RR4 vorab ableitbar. RR4 ist eine Identitaet
     (diskreter Gauss-Satz). Das sind Rechnungspruefungen, keine harten Tests.
4. **RR5 nicht eingetroffen** (vorab erwartet, AP6). Die Anziehung erscheint als Randgroesse:
   - Zwei Klumpen zusammen haben in allen 10 Faellen weniger Randmasse als getrennt.
   - Fuer kleine Massen trifft das genau die Newton-Bindung: Q = 0,994 bei m = 0,01.
   - Bei m/d = 0,1 liegt die Bindung aber 30 bis 38 % unter -G M1 M2/d (Q_kasten = 0,70, 0,65 bzw. 0,62 fuer
     d = 12, 16 und 20).
   - Das ist Kontinuumsphysik ruhender Materie (Kompaktheitskorrektur erster post-Newtonscher Ordnung), kein
     Gitterfehler. Brill-Lindquists exakte Formel gilt fuer Punktierungen, nicht fuer Klumpen.
5. **Bedeutung:**
   - In Finns Bild mit Strichen als Laengen gibt eine Masse ueber die Spaltwinkel der Tetraeder genau das Newton-Feld
     mit richtigem Faktor. Der Rand zaehlt genau die eingeschlossene Gesamtquelle.
   - Das ist Regge (Regime A): Die Regel "Kruemmung = Masse" ist hineingesteckt, nicht hergeleitet.
   - Geprueft ist nur der skalare, Newtonsche Teil (konform flache, zeitsymmetrische Daten). Die Spin-2-Moden
     (transversal-spurfrei) kommen darin nicht vor und sind hier **nicht** getestet.

## Urteile

| Nr | Karte (Wahrsch.) | Urteil | Kennzahl |
|---|---|---|---|
| RR0 | flach < 1e-12, symmetrisch, Skalierung ist Nullmode (90 %) | **eingetroffen** | max abs(eps) 2,7e-15 (L = 8 und 64); abs(A - A^T)/max 4,8e-17; abs(A 1)/max 9,3e-16 |
| RR1 | positiv definit ohne Konstante, keine Schachbrettmoden (65 %) | **eingetroffen** | L = 8/10/12: genau 1 Nullmode (Ueberlapp mit Konstante 1 - 8e-15), 0 negative; min A(k) auf dem L = 64-Gitter 0,0770 > 0; A(pi,0,0) = 32, A(pi,pi,0) = 64, A(pi,pi,pi) = 96 |
| RR2 | r dpsi = G M/2 auf 3 % fuer 6 <= r <= 16 (70 %) | **eingetroffen** | max abs(f - 1) = 0,77 % bei (0,0,6); roh (ohne Torus-Korrektur) 67,5 % |
| RR3 | Richtungsschwankung bei r = 12 < 2 % (60 %) | **eingetroffen** | S = 0,413 % (rel. Standardabw. 0,11 %); roh 8,0 % |
| RR4 | gleiche Gauss-Masse kompakt/ausgedehnt auf 1 % fuer R >= 10 (75 %) | **eingetroffen** | max abs(M_G(a)/M_G(b) - 1) = 1,7e-14 (Identitaet) |
| RR5 | Randmasse - (m1 + m2) = -G m1 m2/d auf 20 % fuer m/d <= 0,1 (40 %) | **nicht eingetroffen** | Q_kasten 0,62 bis 0,89; max abs(Q_kasten - 1) = 0,384 (d = 20, m/d = 0,1) |

- In lauf-69/auswertung.json stehen unter "urteile" dieselben Urteile.
- RR5 ist mit der Randkorrektur geurteilt, die nach Rauchlauf 3 eingefuehrt wurde (Selbstanzeige 2). Ohne Korrektur
  ist Q kleiner (0,30 bis 0,61). Am Urteil aendert sich nichts.

| Nr | Agenten-Vorhersage (PLAN Abschnitt 8, vorab) | Ergebnis |
|---|---|---|
| AP1 | A = 8(-Laplace_7), Diagonalen 0 (70 %) | eingetroffen: a_A = -8 auf 2e-15, a_F = 9e-16, a_R = 7e-15 |
| AP2 | zweitkleinster Eigenwert 8(2 - 2 cos(2 pi/L)); A(pi,pi,pi) = 96 ist das Maximum | eingetroffen (1,3e-14) |
| AP3 | RR2-Wert <= 1 % | eingetroffen: 0,77 % |
| AP4 | S(12) <= 0,5 % | eingetroffen: 0,41 % |
| AP5 | RR4-Wert <= 1e-10 | eingetroffen: 1,7e-14 |
| AP6 | RR5 nicht eingetroffen, Q (ohne Korrektur) < 0,7 bei m/d = 0,1 | eingetroffen: Q = 0,48/0,38/0,30; mit Kastenkorrektur 0,70/0,65/0,62, ebenfalls < 0,7 |
| AP7 | ohne Torus-Korrektur scheitert RR2 (> 50 %) | eingetroffen: 67,5 % |

## Tabellen

**Schablone des linearisierten Eckenoperators** (code/rr.py, Jacobi-Weg; komplexer Schritt durch F stimmt auf 1e-13)

| Nachbar | Koeffizient | 8 x (-Laplace_7) |
|---|---|---|
| Mitte | 48,000000000000014 | 48 |
| 6 Achsen (+-1,0,0) usw. | -7,999999999999998 | -8 |
| 6 Flaechendiagonalen +-(1,1,0) usw. | 9,3e-16 | 0 |
| 2 Raumdiagonalen +-(1,1,1) | 7,4e-15 bzw. 5,1e-15 | 0 |
| alle uebrigen Punkte (L = 8) | 0 exakt | 0 |

- Lokale Jacobi-Matrix d theta / d l des Kuhn-Tetraeders: symmetrisch auf 2,2e-16; Schlaefli-Summe l . J = 0 auf
  1,1e-15.
- Symbol A(k)/(8 k^2) bei k = 2 pi/256: 0,99995 (100), 0,99997 (110), 0,99998 (111), 0,99997 (123).
  - Bei k = pi/2: 0,81 (100) bis 0,93 (111). Das ist die Gitterdispersion des 7-Punkt-Laplace (Bild bild-symbol.png).

**Punktquelle, L = 64: f = r dpsi_korr/(G M/2) entlang von Strahlen** (Auszug; volle Daten in rr_linear.json)

| Richtung | r ~ 6 bis 7 | r ~ 12 | r ~ 16 | unendliches Gitter (Groessenreihe) bei r ~ 12 |
|---|---|---|---|---|
| (1,0,0) | 1,00771 (r = 6) | 1,00252 | 1,00410 | 1,00185 |
| (1,1,0) = (1,-1,0) | 0,99890 (7,07) | 0,99941 (11,31) | 0,99907 (15,56) | 0,99952 |
| (1,1,1) = (1,1,-1) | 0,99649 (6,93) | 0,99839 (12,12) | 0,99761 (15,59) | 0,99881 |

- Gitterkorrektur [L?]: (5 Summe x_i^4/r^4 - 3)/(8 r^2) gibt bei r = 6 +0,69 % (Achse) und bei r = 6,93 -0,35 %
  (Raumdiagonale). Gemessen: +0,77 % und -0,35 %.
- Der Anstieg laengs (100) jenseits von r = 12 ist der Torusrest (Hexadekapol, im Plan auf <= 0,3 % geschaetzt).
  Gemessen gegen die Groessenreihe: hoechstens 0,28 % bei r = 16.
- Bild: lauf-69/bild-r-dpsi.png.

**Richtungsschwankung S(r) (Punktquelle, L = 64, korrigiert)**

| r | 6 | 8 | 10 | 12 | 14 | 16 |
|---|---|---|---|---|---|---|
| S (Spitze-Spitze) | 1,22 % | 0,70 % | 0,47 % | **0,41 %** | 0,48 % | 0,68 % |
| roh (ohne Korrektur) | 4,9 % | 6,5 % | 7,6 % | 8,0 % | 9,6 % | 12,9 % |

- S faellt zunaechst mit dem Gitteranteil (10/3)/(8 r^2) [L?]: 1,16 % bei r = 6, 0,29 % bei r = 12.
  - Der Rest bei r = 12 (etwa 0,12 %) und der Anstieg danach sind der Torusrest.
  - Im unendlichen Gitter (Groessenreihe) ist die Spanne bei r ~ 12 zwischen (100) und (111) 0,30 %.
- Kugelklumpen bei r = 12: S = 0,17 %.
- Bild: lauf-69/bild-richtung.png. Die Werte gegen den Winkel zur Kuhn-Diagonale (1,1,1) liegen spiegelsymmetrisch in
  cos -> -cos. Die Diagonale ist also nicht ausgezeichnet.

**Gauss-Massen, L = 64 (M = 1; Hintergrundzusatz mquer |D_R|)**

| R | M_G Punkt | M_G Kugel | M_op (beide) | Kugelflaeche Punkt | Kugelflaeche Kugel | M_G roh (beide) |
|---|---|---|---|---|---|---|
| 10 | 1 - 2,4e-13 | 1 - 2,2e-13 | 1 - 2,4e-13 | 1,002513 | 1,002510 | 0,9647 |
| 16 | 1 - 4,0e-13 | 1 - 3,8e-13 | 1 - 4,0e-13 | 1,000976 | 1,000976 | 0,8629 |
| 20 | 1 - 4,3e-13 | 1 - 4,2e-13 | 1 - 4,3e-13 | 1,000687 | 1,000687 | 0,7371 |
| 28 | 1 - 2,2e-13 | 1 - 2,2e-13 | 1 - 2,2e-13 | 1,000412 | 1,000412 | 0,2935 |

- M_G ist der Gradientenfluss (Kartendefinition, geurteilt), M_op der Fluss des Regge-Operators. Wegen
  A = 8(-Laplace_7) sind beide identisch.
- Kugelflaeche (nur Bericht): 4000 Punkte mit trilinearer Interpolation. Die Abweichung +0,25 % bei R = 10 faellt etwa
  wie 1/R^2 (Interpolationsfehler). Punkt und Kugelklumpen stimmen auf 3e-6 ueberein.
- Bild: lauf-69/bild-gauss.png.

**RR5: Bindungsenergie als Randgroesse** (Dirichlet-Kasten L = 64, Kugeln a = 3, Rand R = 18)

| d | m | m/d | d <K> | Q_kasten (geurteilt) | Q ohne Korrektur | Kontinuum 2. Ordnung | <phi> | DeltaM | psi_max |
|---|---|---|---|---|---|---|---|---|---|
| 12 | 0,3 | 0,025 | 0,682 | 0,890 | 0,607 | 0,879 | 0,052 | -0,0041 | 1,074 |
| 12 | 0,6 | 0,05 | 0,682 | 0,810 | 0,552 | 0,768 | 0,100 | -0,0137 | 1,140 |
| 12 | 1,2 | 0,1 | 0,682 | 0,697 | 0,475 | 0,569 | 0,187 | -0,0405 | 1,258 |
| 16 | 0,4 | 0,025 | 0,584 | 0,866 | 0,505 | 0,849 | 0,069 | -0,0044 | 1,093 |
| 16 | 0,8 | 0,05 | 0,584 | 0,774 | 0,452 | 0,714 | 0,130 | -0,0142 | 1,175 |
| 16 | 1,6 | 0,1 | 0,584 | 0,653 | 0,381 | 0,476 | 0,238 | -0,0397 | 1,318 |
| 20 | 0,5 | 0,025 | 0,492 | 0,844 | 0,415 | 0,820 | 0,084 | -0,0044 | 1,111 |
| 20 | 1,0 | 0,05 | 0,492 | 0,743 | 0,365 | 0,662 | 0,158 | -0,0136 | 1,208 |
| 20 | 2,0 | 0,1 | 0,492 | 0,616 | 0,303 | 0,389 | 0,286 | -0,0366 | 1,374 |
| 12 | 0,01 | 0,0008 | 0,682 | 0,994 | 0,678 | 0,996 | 0,0018 | -1,0e-5 | 1,003 |

- Q_kasten = DeltaM/(-G M+ M- <K>), wobei <K> der Newton-Kern im selben Kasten ist (im freien Raum 1/d).
  "Kontinuum 2. Ordnung" = 1 - (<phi+> + <phi->) - (M+ + M-)<K>/2 mit gemessenem <phi> (PLAN Abschnitt 7).
- Alle 30 Loesungen sind konvergiert (Residuum <= 8e-11, 5 bis 42 Schritte).
- Q haengt kaum vom Rand ab: R = 16/18/20 und die Kontinuumsidentitaet Summe m/psi stimmen auf <= 0,006 ueberein.
- Bei kleinem m folgt das Gitter der Kontinuumsformel. Bei m/d = 0,1 liegt es deutlich darueber (0,70 gegen 0,57);
  dort fehlen der Formel die Terme dritter Ordnung.
- Bild: lauf-69/bild-rr5.png.

## Kontrollen

- **Flachheit:**
  - max abs(eps) = 2,7e-15 auf L = 8 und L = 64.
  - Tetraeder je Kante 6/6/6/4/4/4/6 (Achsen, Flaechen, Raum), wie in PLAN Abschnitt 1.
  - Gleichmaessige Skalierung psi = 1,3 bleibt flach (5,3e-15).
- **Zwei Operatorwege:**
  - Jacobi-Weg gegen komplexen Schritt durch das volle F: 1,1e-13 (L = 8, Zufallsfeld).
  - Residuen der FFT-Loesung auf L = 64: 1,9e-16 (Jacobi) bzw. 5,0e-16 (komplexer Schritt) fuer die Punktquelle,
    5e-14 bzw. 1,4e-13 fuer die Kugel.
- **Jacobi-Matrix:** komplexer Schritt gegen zentrale Differenz 2,8e-10; identisch fuer alle 6 Tetraeder-Orientierungen.
- **Dichtes Spektrum gegen Symbol:** <= 1,1e-13 (L = 8, 10, 12).
- **Torus-Korrektur gegen Groessenreihe (L = 64/128/256):**
  - korrigiertes L = 64 gegen extrapoliertes Unendlich: hoechstens 0,28 % fuer 6 <= r <= 16 (bei r = 16 laengs
    (100)); bei r <= 12 hoechstens 0,07 %.
  - Gefitteter 1/L-Koeffizient: xi = -2,8434 bis -2,8339, gegen xi = -2,837297 [L].
- **Normierung:** quadratisches psi, Diagonale -8,000000000000005 bzw. -7,999999999999989 (beide Wege); ausserhalb der
  Diagonale <= 8,4e-15.
- **Kontrolle RR5:** m = 0,01 ergibt Q_kasten = 0,994 (Kontinuum 0,996). Damit stimmt der Newtonsche Grenzfall der
  Bindung als Randgroesse.
- **Latten (v3):**
  - L1 (kann scheitern): ja fuer AP1/RR1 vor dem Rauchlauf. Bei a_F = -a_R = -6 haette die Schachbrettmode die
    Steifigkeit 0 gehabt [M]. Danach waren RR2 bis RR4 nur noch Rechnungspruefung; RR5 konnte scheitern und ist
    gescheitert.
  - L2 (Gegenprobe): zwei Operatorwege, Spektrum gegen Symbol, Groessenreihe gegen Torusformel, Kugel- gegen
    Wuerfelflaeche.
  - L3 (Numerik): 1e-13 bis 1e-16.
  - L4 (schon bekannt): Regge [S, Dossier], Gitter-Green-Funktion [L?], Glickensteins diskrete konforme Variation
    [L?], Brill-Lindquist [L].
  - L5 (Messbezug): keiner.

## Pruefung der Schreibtischherleitung der Karte

- **Bestaetigt:**
  - Eckenregel Summe l eps = 16 pi G m_v mit halber Kante je Ecke (exakt in linearer Ordnung)
  - dpsi = G M/(2r) im Fernfeld
  - Gauss-Masse -(1/(2 pi G)) mal Gradientenfluss
  - "Randmasse zaehlt nur die eingeschlossene Gesamtquelle": linear eine Identitaet
- **Eine Luecke [M]:** "Randmasse = m1 + m2 - G m1 m2/d" ist fuer ruhende Materie nur die fuehrende Ordnung.
  - Die relative Korrektur ist -(<phi1> + <phi2>) - G(M1 + M2)/(2d).
  - Nicht ueberlappende gleichfoermige Klumpen (a < d/2) haben <phi> > 1,2 G m/d. Damit ist bei m/d = 0,1 schon im
    Kontinuum Q <~ 0,66, in zweiter Ordnung gerechnet.
  - Die Gitterwerte liegen bei grossem m ueber der Formel zweiter Ordnung. Aber auch der guenstigste Fall (d = 12)
    erreichte nur 0,70.
  - RR5 war also fuer Klumpen bei m/d = 0,1 voraussichtlich nicht erreichbar, gleich welches Gitter.
  - Die exakte Brill-Lindquist-Form (nackte Massen) gilt fuer Punktierungen [L]; die sind auf diesem Gitter nicht
    darstellbar.
- **Rocek/Williams:** Die fuenfte Nullmode tritt im konformen Sektor des 3D-Kuhn-Gitters nicht auf. Ob sie im vollen
  Sektor (alle 7 Kantenlaengen je Ecke, Spin 2) auftritt, ist hier nicht geprueft.

## Selbstanzeigen

1. **AP1 schon im Rauchlauf gesehen.**
   - Die verlangte Normierungspruefung vor dem Einfrieren (rauch1) zeigt zwangslaeufig die Schablone.
   - Danach waren RR1 bis RR4 vorab ableitbar. Ihre Schwellen standen vorher fest und wurden nicht geaendert.
2. **RR5-Methode nach Rauchlauf 3 geaendert** (vor dem Einfrieren, PLAN Abschnitte 7 und 9): Randkorrektur Q_kasten
   statt Q, Kasten L = 64 statt 48, ein Lauf je d.
   - Die Korrektur verschiebt Q nach oben, also in Richtung "eingetroffen".
   - Begruendung: Der Dirichlet-Kasten verkleinert den Newton-Kern auf d <K> = 0,49 bis 0,68. Ohne Korrektur haette
     RR5 einen Kasteneffekt gemessen.
   - Q ohne Korrektur ist mitberichtet; AP6 ist wie vorab formuliert auf Q geurteilt. Das RR5-Urteil ist in beiden
     Fassungen "nicht eingetroffen".
3. **RR4 ist keine Messung:** Fuer jeden symmetrischen Operator mit Zeilensumme 0 gilt der diskrete Gauss-Satz exakt,
   und bei A = 8(-Laplace_7) faellt der Gradientenfluss mit dem Operatorfluss zusammen. Die Kugelflaechen-Fassung ist
   nicht trivial (Interpolation), stimmt fuer beide Klumpen aber ebenfalls auf 3e-6 ueberein; sie ist nur berichtet.
4. **Festlegungen [A]:**
   - RR2 ueber alle Gitterpunkte der Schale statt einiger Strahlen (strenger).
   - RR3 als Spitze-Spitze von r dpsi_korr. Mit Rohwerten waere RR3 bei 8,0 % gescheitert, allein weil die Torus-
     Konstante ueber die Schalendicke wirkt.
   - Fuer RR3 ist die Torus-Korrektur verwendet, obwohl die Karte sie nur bei RR2 nennt.
5. **xi aus dem Gedaechtnis [L]:** Die Groessenreihe bestaetigt xi auf 0,2 %.
6. **Glickenstein-Begruendung [L?]:** nicht an einer Quelle gelesen. Belegt ist nur der numerische Befund fuer dieses
   Gitter (auf 1e-14), nicht der allgemeine Satz.
7. **Nichtlineare Gitterterme:** Im Rauchlauf gab das nichtlineare F fuer psi = 1 + h x0 x1/2 den Wert 3,5 h^2. Im
   Kontinuum ist er 0, es ist also ein Gitterterm zweiter Ordnung. Er kann erklaeren, warum Q bei grossem m ueber der
   Kontinuumsformel zweiter Ordnung liegt; geprueft ist das nicht.
8. **Spurwahl:** Alle Laeufe nutzten Spur p4000a als reines CPU-numpy, ohne GPU; der Lock war je Lauf bis 2,3 min
   belegt. Hoechstens ein Lauf zugleich.
9. **Nicht gerechnet:** Gegenprobe Tetraeder-Oktaeder-Wabe (Zeit und Prioritaet). Die volle Spin-2-Analyse (alle
   Kantenlaengen) war nicht verlangt.
10. **L = 32 (Karte "L = 32 und 64"):** gerechnet, aber nicht geurteilt.
    - RR2-Wert 0,85 % (6 <= r <= 8).
    - S(12) = 4,2 % (r = 12 liegt dort jenseits von L/4).
    - Gauss-Massen 1 auf 1e-13.

## Bedeutung

- **Spin 2 aus Dreiecken und Tetraedern:**
  - Im Regge-Bild (Striche = Laengen, Kruemmung = Spaltwinkel an den Kanten) reproduziert das Kuhn-Netz den
    Newtonschen Teil der Allgemeinen Relativitaetstheorie exakt in linearer Ordnung, mit richtigem Faktor, ohne
    Schachbrettmoden und ohne Spur der schiefen Diagonalen.
  - Das gilt fuer den skalaren Sektor (Hamilton-Bedingung). Den Spin-2-Sektor deckt diese Karte nicht ab.
  - Wie im Dossier (Regime A): Spin 2 und Universalitaet sind mit der Regge-Regel hineingesteckt, nicht aus Punkten
    und Strichen hergeleitet.
- **Reicht der Rand?**
  - Fuer das Fernfeld ja, exakt: Der Fluss durch jede geschlossene Flaeche zaehlt nur die eingeschlossene Quelle, egal
    wie sie innen verteilt ist.
    - Das gilt aber fuer jede Gauss-Gesetz-Theorie, auch fuer Coulomb (FLUSS-1). Es ist also kein Kennzeichen der
      Schwerkraft.
  - Was die Schwerkraft am Rand auszeichnet, zeigt RR5: Zwei Massen zusammen haben weniger Randmasse als getrennt.
    - Die Anziehung erscheint also als Randgroesse, und fuer schwache Felder genau als -G M1 M2/d.
    - In der linearen Theorie ist sie exakt 0. Sie kommt aus der Nichtlinearitaet der Eckenregel; mechanisch steckt
      sie in der Skalierung F(lambda psi) = lambda^2 F(psi) [M].
    - Fuer kompakte Klumpen kommen post-Newtonsche Korrekturen von 10 bis 40 % hinzu.
- **Vorschlag [H]:** Spin 2 selbst braucht 3+1 Dimensionen; in 3D gibt es keine lokalen Freiheitsgrade (Dossier,
  Dimensionskette).
  - Der naechste Schritt ohne Vorabableitung waere daher der linearisierte 4D-Regge-Operator auf der Kuhn-Zerlegung des
    Hyperkubus (15 Kanten je Ecke), also ein Nachbau von Rocek/Williams. Er wuerde zeigen, ob genau zwei masselose
    Spin-2-Moden uebrig bleiben und wo die fuenfte Nullmode sitzt.
  - Fuer den hier gerechneten skalaren Teil waere die Tetraeder-Oktaeder-Wabe (Finns regelmaessige Tetraeder) die
    Gegenprobe.

## Dateien

- PLAN.md, PLAN.md.eingefroren-20261003-233510, EINGEFROREN-SHA256.txt
- code/:
  - rr.py: Gitter, Fehlwinkel, Operator, lineare Loesungen
  - rr_nl.py: RR5
  - rr_auswertung.py: Urteile und Bilder
  - Die Pruefsummen auf der .69 stimmen mit EINGEFROREN-SHA256.txt ueberein; nach dem Einfrieren wurde kein Code
    geaendert.
- lauf-69/:
  - auswertung.json
  - rr_linear.json, rr_nl_d12.json, rr_nl_d16.json, rr_nl_d20.json
  - Bilder bild-r-dpsi.png, bild-richtung.png, bild-gauss.png, bild-symbol.png, bild-rr5.png
- rauch-69/: Rauchlaeufe (rauch1.json; r2/ und r3/ mit Auswertungsproben auf L = 32 bzw. 24)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde36-regge/ (code/, rauch/, lauf/)

## Einfach gesagt

Wir haben ein Gitter aus lauter gleichen Tetraedern gebaut und die Striche als Laengen behandelt. Eine Masse an einer
Ecke streckt die Kanten in ihrer Naehe ein wenig; dann passen die Tetraeder um eine Kante nicht mehr genau zusammen,
und der kleine Spaltwinkel ist die Kruemmung. Die Rechnung zeigt, dass diese Spaltwinkel genau das bekannte 1/r-Feld der
Schwerkraft geben, mit dem richtigen Vorfaktor, in allen Richtungen fast gleich (unter 1 % Abweichung) und ohne
Schachbrett-Stoermuster. Auf einem Rand um die Masse liest man exakt die Gesamtmasse ab, egal ob sie innen als Punkt
oder als Klumpen sitzt; bei zwei Massen zeigt der Rand sogar die Anziehung als etwas kleinere Gesamtmasse, genau nach
Newton aber nur bei schwachen Feldern. Wichtig: Die Regel "Kruemmung = Masse" haben wir hineingesteckt (das ist Regge),
und die Spin-2-Wellen selbst haben wir hier noch nicht geprueft.
