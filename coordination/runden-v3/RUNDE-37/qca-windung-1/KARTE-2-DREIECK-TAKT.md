# DREIECK-TAKT-1 mit QCA-WINDUNG-2: Kann ein lokaler Takt mit Drehsinn je Dreieck eine verdrehte Spielregel (W3 != 0) und damit Netto-Haendigkeit erzeugen? (Runde 41)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 16:32:57 CEST (date), vor jeder
  Rechnung. Folgekarte zu QCA-WINDUNG-1; an denselben Agenten (Kontext und W3-Code vorhanden).
- **Finn (04.10., woertlich):**
  - Nachricht zwischen 16:16 und 16:22: "die dreiecke die sich bilden, die muessten doch pro "zyklus" einen takt auch
    haben und eine richtung, koennte daraus ein feld entstehen aus ticks was eine welle sendet die links oder rechtsrum
    laeuft"
  - Frueher am Tag: "kann es sein das linksdrehende bzw rechtsdrehende teilchen so sind weil deren takt falsch rum geht?"
- **Stand:**
  - QCA-WINDUNG-1: W3 = 0 in allen 53 Projekt-Automaten. Die Grad-1-Kontrolle (nicht endlichreichweitig) zeigt den
    ungepaarten Weyl-Punkt im Gegentakt.
  - Tetraeder-Demonstrator (Spielzeug): Die Tick-Reihenfolge erzeugt eine kleine Netto-Drehung.
  - Literatur [L]: In 2D geben Quantenlaeufe aus Teilverschiebungen und Muenzen Chern-Baender und einseitige Randwellen
    (Kitagawa u. a. 2010); kreisfoermiger Antrieb macht Floquet-Chern-Phasen (Oka/Aoki 2009).
- **Schreibtisch der Leitung [M, ungeprueft; im Plan pruefen]:**
  - W3 ist additiv unter punktweisem Produkt: W3(AB) = W3(A) + W3(B) auf T^3.
  - Eine Teilverschiebung entlang einer Richtung haengt nur von einer Impulskombination ab, also W3 = 0; eine Muenze
    ohne k-Abhaengigkeit hat ebenfalls W3 = 0.
  - Folge: **Jeder Automat, der ein Produkt aus Teilverschiebungen entlang je einer Richtung und festen Muenzen ist, hat
    W3 = 0**, egal in welcher Reihenfolge.
  - Insbesondere aendert die Umkehr der Tick-Reihenfolge W3 nicht. Das passt dazu, dass Zeitumkehr allein links und
    rechts nicht tauscht.
  - Netto-Haendigkeit braucht also mindestens einen Schritt, der von drei unabhaengigen Impulsrichtungen zugleich
    abhaengt.
  - Offen ist, ob es endlichreichweitige unitaere Laurent-Matrizen in 3D mit W3 != 0 ueberhaupt gibt, und wenn ja, ob
    sie sich als lokaler Takt je Dreieck bauen lassen.

## Auftrag

1. **Literatur (hoechstens 3 Abrufe):**
   - ein explizites 3D-Floquet- oder QCA-Modell mit W3 != 0 an der Quelle, etwa das Beispiel in Bessho/Sato 2006.04204
     oder Higashikawa/Nakagawa/Ueda 2019: Ist es endlichreichweitig oder nur quasilokal?
   - Kitagawa u. a. 2010 als 2D-Kontrolle
2. **Schreibtisch pruefen:** Additivitaet und W3 = 0 fuer Produkte aus Teilverschiebungen numerisch an Beispielen (das
   ist eine Kontrolle).
3. **2D-Kontrolle:** Ein Quantenlauf nach Kitagawa auf dem Dreiecks- bzw. Wabengitter mit umlaufender Sprungfolge:
   Chern-Zahl der Baender und einseitige Randwelle auf einem Streifen. Die Umkehr der Folge kehrt die Randrichtung um
   oder nicht.
4. **3D-Suche:** endlichreichweitige Automaten mit Schritten, die drei Richtungen zugleich koppeln; als Finns Bild ein
   Takt je Dreieck mit festem Drehsinn, also eine zyklische Sprungfolge um die Dreiecke eines Tetraeders bzw. einer
   BCC- oder Pyrochlor-Zelle. Gefragt ist W3; bei W3 != 0 die Weyl-Punkte, ihre Chiralitaet, ihre Quasienergie und die
   Isotropie des tiefsten Kegels.
5. Plan, Rauchlauf, Einfrieren wie ueblich.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| DT0 | Kontrollen: Produkte aus Teilverschiebungen und Muenzen haben W3 = 0 (auf 1e-8); der 2D-Lauf nach Kitagawa hat Baender mit Chern-Zahl ungleich 0 und eine einseitige Randwelle | 85 % |
| DT1 | [H] Es wird ein endlichreichweitiger 3D-Automat mit W3 != 0 gefunden oder aus der Literatur nachgebaut | 35 % |
| DT2 | [H] Wenn DT1: Sein tiefster Kegel bei Quasienergie 0 ist ungepaart und isotrop auf 10 % | 30 % |
| DT3 | [H] Ein Takt je Dreieck mit festem Drehsinn (Finns Bild) gibt in 2D eine einseitige Randwelle, deren Richtung der Drehsinn bestimmt | 60 % |

**Bedeutung (vorab):**
- **DT0 und DT3 treffen ein, DT1 nicht:** In 2D erzeugt Finns Dreiecks-Takt einseitige Wellen. In 3D bleibt die
  Haendigkeit bei lokalen Spielregeln aus einfachen Schritten gepaart; der Takt-Weg zu chiralen Fermionen ist dann eng.
- **DT1 trifft ein:** Es gibt eine lokale verdrehte Spielregel. Das ist ein Baustein fuer chirale Fermionen in K-A bzw.
  K-AM, frei und ohne Eichfeld.

## Rahmen

- Spuren p4000b und p4000a wie bisher. Je Lauf <= 10 min, 1 Thread. Zeitbox 120 min.
- Regeln wie in QCA-WINDUNG-1.
