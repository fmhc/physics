# IDEEN-SPIN-ZEIT: Ideen zu Spin-Schutz und 4D-Zeit (Runde 49, Leitung, nach Finns "ideate dazu weiter")

- Leitung claude-primary, geschrieben ab 2026-10-05 14:31:05 CEST (date). Ideen, keine Ergebnisse.
- Kennzeichen: [M] vorab ableitbar (Rechenweg hier), [P] Projektdatei, [L] Literatur aus dem Gedaechtnis, nicht an der
  Quelle geprueft, [ES] grobe Schreibtischschaetzung, [H] Hypothese.
- **Ausgangslage [P]:**
  - Z2-SCHUTZ-1: Barriere 360 -> 0 Grad auf dem Diamant-Netz 25,03 (G1) und 41,40 (G2); Sattel ein kleiner gesprungener
    Fleck an der Kernoberflaeche, sein Rand ein Z2-Wirbelring [H, Deutung des Agenten]; 420 -> -300 Grad (4 pi) ohne Sprung.
  - REGIME-K-2: gefuelltes V mal Zeit euklidisch TT-isotrop (8,0e-9); 26 Gittermoden negativer Steifigkeit je k, B1 7,
    Kuhn keine. V je Grundzelle: 10 Ecken, 68 Kanten, 116 Dreiecke, 58 Tetraeder; 4D: 146 Kanten.
  - UEBERLEITUNG-KH-1: Traegheit M_eff aus der 4D-Wirkung ist singulaer, die Raumdiagonale (111) ist statisch.
  - ZELT-KOMMUTATOR-2: Die Reihenfolge-Spur der Zeltzuege sitzt nur in den drei 3-3-Zuegen; die unimodulare Uhr erbt sie
    (Exponent 2,25 wie die Impulse).
  - DYON-STATISTIK-L und TWIST-PYRO-1: Fermionen im Quanten-Eis (Dyon) bzw. mit Levin/Wen-Twist auf Finns Netz sind
    bekannt bzw. vorab ableitbar; nichts davon wird hier als neu gefuehrt.

## I1 Das Spin-Vorzeichen kippt nur durch "Durchrutschen" einer Bindung bei 180 Grad [M]

- Rechenweg: Drehrahmen R_i in SO(3) auf den Ecken, Bindung B_ij = R_i^T R_j mit Winkel omega_ij in [0, pi]. Fuer
  omega < pi gibt es genau einen "kurzen" Lift nach SU(2) (Realteil > 0), und er haengt stetig vom Feld ab. Das Produkt der
  kurzen Lifte um einen Ring ist +1 oder -1 (Fluss), kann sich also nur aendern, wenn eine Bindung des Rings 180 Grad
  erreicht. Ohne Fluss -1 (wirbelfrei) ist das Vorzeichen Kern gegen Rand (die 360-Grad-Verdrehung) wegunabhaengig und
  unter stetiger Aenderung fest.
- Folge: Die Barriere ist endlich, weil die Guertel-Energie 4 sin^2(omega/2) bei 180 Grad beschraenkt ist (4 je Bindung).
  Eine Bindungsenergie mit gleicher Steifigkeit fuer kleine Winkel, die bei 180 Grad unbeschraenkt waechst (z. B.
  4 tan^2(omega/2), beide ~ omega^2), macht die Barriere unendlich, bei gleicher Langwellen-Physik [M].
- Vorbild: Zulaessigkeitsbedingung der Gittereichtheorie (Luescher 1982) und "topologische Gitterwirkungen"
  (Bietenholz u. a. 2010) [L].
- Bedeutung [H]: Ein Netz, das nicht reissen kann, haelt das Spin-Vorzeichen exakt. Exaktheit kommt aus einem Verbot,
  nicht aus einer hoeheren Schwelle.

## I2 Beim Umbau schuetzen Dreiecke doppelt so gut wie Sechsecke [M]

- Sprunghafte Aenderungen (Pachner-Takt, neue Kante; Monte-Carlo-Spruenge) koennen einen Wirbel ohne Durchrutschen
  erzeugen. Fluss -1 in einem Ring aus n Bindungen verlangt aber, dass die Drehwinkel zusammen mindestens 360 Grad ergeben
  (Dreiecksungleichung auf S^3: Winkel eines Produkts <= Summe der halben Winkel).
  - Dreieck (gefuelltes Tetraedernetz, Rahmen auf den Ecken): mindestens eine Bindung >= 120 Grad.
  - Sechserring (Diamant-Netz wie in Z2-SCHUTZ-1): schon >= 60 Grad je Bindung reicht.
- Takt-Regel [H]: "Ein Umbau ist nur erlaubt, wenn keine neue Kante mehr als 120 Grad verdreht ist." Auf dem gefuellten
  Netz entsteht dann nie ein Wirbel, auch nicht im Takt.
- Diskrete Drehdimension [M]: Nimmt der Rahmen nur die Drehungen der 600-Zelle an (120 Einheitsquaternionen, Schritt zum
  Nachbarn 36 Grad auf S^3 = 72 Grad Drehung) und liegen Nachbarn hoechstens einen Schritt auseinander, dann gilt
  3 x 72 = 216 < 360: Kein Dreieck kann je einen Wirbel tragen. Im Sechserring geht es (6 x 72 = 432). Damit waere
  FASER-SPIN-600-1 in diesem Punkt vorab entschieden.
- Die vierte Dimension bietet keinen Ausweg [M, Standard]: pi_1(SO(4)) = pi_1(SO+(3,1)) = Z2 wie pi_1(SO(3)).

## I3 Endliche Schwelle heisst nicht "kein halber Spin" [M, L]

- Quantenmechanisch tunneln die zwei Verdrehungszustaende ineinander. Kollektive Koordinate ist der gelifteten Kernrahmen
  in SU(2); ganzzahlige Spins sind die symmetrische, halbzahlige die antisymmetrische Kombination. Tunneln mit Amplitude t
  verschiebt sie gegeneinander um 2t, exponentiell klein in der Barriere [M].
- Auch bei exaktem Schutz ist der Grundzustand des Kreisels j = 0 (E ~ j(j+1)); halbzahlige Zustaende sind Anregungen [M].
  Zum Fermion wird das Objekt erst durch ein Zusatzvorzeichen: Finkelstein-Rubinstein-Bedingung bzw. Wess-Zumino-Term
  (Witten 1983) oder Interferenz zweier Tunnelwege mit Phase pi (Spin-Paritaets-Effekt: Loss, DiVincenzo, Grinstein 1992;
  von Delft, Henley 1992) [L].
- Kartenidee SPRUNG-PHASE-L [H]: Kann Finns Netz am Sprung selbst eine Phase pi liefern, etwa Fluss-Eis-Fluss durch den
  Wirbelring oder der Levin/Wen-Twist aus TWIST-PYRO-1? Literatur und Schreibtisch, mit Ableitbarkeitsprobe gegen
  DYON-STATISTIK-L.

## I4 Die negativen Gittermoden sind vielleicht Ueberzahl-Kanten ohne Traegheit [H, ES]

- Zaehlung [ES]: Je Ecke braucht die Raummetrik 6 Zahlen. Kuhn: 7 Kanten je Ecke, also 1 Ueberzahl-Kante, und genau die
  Raumdiagonale ist in M_eff statisch (UEBERLEITUNG-KH-1). V: 68 Kanten gegen 10 x 6 = 60, also 8 Ueberzahl-Kanten je
  Grundzelle. 4D: 146 Kanten gegen 10 x 10 = 100, also 46, davon 26 mit negativer Steifigkeit (REGIME-K-2).
- Hypothese: Die negativen Richtungen liegen in statischen bzw. Multiplikator-Richtungen. Dann sind sie im Grenzfall
  stetiger Zeit Zwangsbedingungen, keine Wellen, und machen nichts instabil.
- Zusatz-Vorhersage fuer UEBERLEITUNG-V-1 (in RUNDE-49.md vor dessen Ergebnisdatei eingetragen).
- Folgekarte GITTERMODEN-ZWANG-1 nach UEBERLEITUNG-V-1 und REGIME-K-3: Ueberlapp der negativen Eigenvektoren mit dem
  Kern von M_eff; Gegenprobe B1 (7 negative).

## I5 Takt-Reihenfolge: ein fester Taktplan oder eine 3-3-feste Wirkung [P, H, L]

- ZELT-KOMMUTATOR-2: Die Reihenfolge zaehlt nur in den 3-3-Zuegen, und die Uhr erbt den Fehler. Zwei Wege [H]:
  - fester Taktplan (Ecken in fester Farbfolge, wie Rot-Schwarz-Ordnung): Die Mehrdeutigkeit wird zu einem festen
    Gitterfehler. Pruefen, ob der Plan eine Vorzugsrichtung erzeugt (TT-Spanne im Regime K mit geordneten Zelten).
  - Wirkung, die unter 3-3 invariant ist ("perfekte" bzw. verbesserte Wirkungen, Bahr/Dittrich 2009 [L]). Nach
    ZELT-KOMMUTATOR-2 Abschn. 7 waeren die Zeltzuege dann hier weg-unabhaengig (einseitige Folgerung).
- Verbindung zu I2 [H]: Der Umbau in der voruebergehenden vierten Dimension ist zugleich der Ort der Uhr-Mehrdeutigkeit
  (3-3) und der einzige Ort, an dem das Spin-Vorzeichen ohne Durchrutschen kippen koennte (neue Kante). Eine einzige
  oertliche Takt-Regel ("Umbau nur in fester Farbfolge und nur, wenn neue Kanten unter 120 Grad verdreht sind") wuerde
  beides festlegen.

## Rangfolge der Leitung

1. Zusatz-Vorhersagen jetzt (UEBERLEITUNG-V-1, Z2-SCHUTZ-2), keine Kosten.
2. SPRUNG-PHASE-L (Literatur), sobald ein Platz frei ist; I3 ist die Stelle, an der aus "Spin-Zustaende moeglich"
   "Fermion" werden muesste.
3. GITTERMODEN-ZWANG-1 nach den zwei laufenden 4D-Karten.
4. Taktplan-Test nur, wenn Regime K stabil bleibt (REGIME-K-3).
5. Z2-SCHUTZ-3 (gefuelltes Netz gegen Diamant, tan-Energie) nur fuer nicht ableitbare Reste; I1 und I2 sind [M].

## Vermerk der Leitung (14:38:21, date): schon im Projekt

- **Selbstanzeige:** I1 (Zulaessigkeit nach Luescher als Zusatzregel fuer exakten halben Spin) und der Kern von I3 ("Die Z_2 ist billig; teuer ist die Sektorwahl, bei Skyrmionen der Wess-Zumino-Term"; der starre Rotor hat einen ganz- und einen halbzahligen Sektor) stehen in RUNDE-37/kruemmung-spannung-spin-l/DOSSIER.md (Abschn. 5.2 und Z. 318-319) [P]. Finn hatte die Ideen schon. Ursache: grep nach "Lüscher" mit Umlaut, die Datei schreibt "Luescher".
- **Neu bleiben nur (Schreibtisch):** in I1 der Rechenweg (Vorzeichenwechsel nur ueber eine Bindung bei genau 180 Grad) und die tan^2-Energie als Umsetzung der Regel; in I2 die Ringschwellen (Dreieck 120 Grad, Sechserring 60 Grad) und der Selbstschutz der 600-Zelle auf Dreiecken; in I3 die Tunnelaufspaltung 2t und der Satz, dass eine vorzeichenfreie Energie (Perron-Frobenius) nur den ganzzahligen Grundzustand liefern kann, das Vorzeichen also einen Phasenterm braucht (Kandidat auf Finns Netz: Levin/Wen-Twist, TWIST-PYRO-1 [P]); I4 und I5.
- **Folge:** SPRUNG-PHASE-L wird nicht gestartet (Kern bekannt: KRUEMMUNG-SPANNUNG-SPIN-L, DYON-STATISTIK-L, TWIST-PYRO-1, GUERTEL-1/2). Offen bliebe nur die enge Frage, ob die Z2-Wirbellinien des Drehrahmens die Strings des Levin/Wen-Netzes sein koennen; geparkt.

## Vermerk der Leitung (15:14:15, date): Vorlage zu I4

- REGGE-4D-SCHIEF-1 [P] zeigte schon: Im schiefen 4D-Kuhn-Netz wird die vorher tote Hyperdiagonale eine Gittermode negativer Steifigkeit (Signatur bei allgemeinem k 9 positiv, 2 negativ, gegen Kuhn 9 und 1). Die Verbindung "Ueberzahl-Diagonale -> negative Steifigkeit" ist also im Projekt belegt. Neu in I4 ist nur die Zaehlung fuer V (8 bzw. 46 Ueberzahl-Kanten) und die Lesart "im stetigen Grenzfall statisch, also Zwangsbedingung".
