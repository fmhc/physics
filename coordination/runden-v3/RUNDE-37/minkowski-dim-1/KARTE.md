# MINKOWSKI-DIM-1: Welche Dimension sieht unser Modell an Dreiecken und Tetraedern, die Minkowski-Dimension oder die spektrale? (Runde 48, Finns Auftrag)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 10:57:09 CEST (date), vor jeder Rechnung.
- **Herkunft:** Finn, 05.10.2026, Eingang vor 10:55:17, woertlich: "Haben wir minkowski Dimensionen an den Dreiecken ? Subagents test". Vorher ging es um Kakeya (Wang/Zahl: Minkowski- und Hausdorff-Dimension 3).
- **Lesart der Leitung:**
  - "Minkowski-Dimension" heisst hier die Kaestchen-Dimension (box counting), nicht die Minkowski-Raumzeit.
  - "an den Dreiecken" umfasst (a) die Dreiecke unserer Netze und (b) die Sierpinski-Dreiecke aus BAG-DIM.
  - Die Lesart "Minkowski-Raumzeit an den Dreiecken" (Lorentz-Signatur an den Gelenken) ist nicht Teil dieser Karte.
- **Projektbefunde [P]** (nicht als neu fuehren):
  - **BAG-DIM** (RUNDE-24/bag-dim/ERGEBNIS.md): Auf dem Sierpinski-Dreieck misst der Q-Ball-Beutel die spektrale Dimension d_s = 1,365 (p = 0,577 erwartet, 0,590 gemessen), nicht die Hausdorff-Dimension 1,585 (p = 0,613).
    - Die Beutel rasten auf Vereinigungen von Teildreiecken ein, mit log-periodischer Schwingung (Faktor 2 im Radius).
    - Auf dem Zufallsgraphen entsteht kein Beutel.
  - **DIM-BEUTEL** (RUNDE-16): Auf Gittern zaehlt der Beutelexponent die Dimension, d = p/(1 - p) (1,001 / 2,002 / 3,02).
  - **RUNDE-22** (geometrie-stand): CDT gibt im Grossen die spektrale Dimension 4,02, im Kleinen 1,80 +- 0,25 [S, Literatur].
  - **FADEN-DIM-2** (RUNDE-44): raue Faeden, Grenze 3.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar [M]:**
  - **Netze:** Die Vereinigung endlich vieler Dreiecke ist ein Polyeder; ihre Minkowski-Dimension ist 2. Das 2-Geruest eines periodischen Netzes hat unterhalb der Kantenlaenge a die Kaestchen-Steigung 2 und oberhalb (Kaestchen groesser a) 3, mit Uebergang bei a.
    - **Folge:** Unsere Netze sind einskalig, also nicht fraktal. Auf ihnen haben Minkowski-, Hausdorff- und spektrale Dimension im Grossen den Wert 3. Eine Rechnung dazu ist nur Kontrolle des Schaetzers.
  - **Sierpinski-Dreieck:** Minkowski = Hausdorff = log 3/log 2 = 1,585; spektral 2 log 3/log 5 = 1,365; Laufdimension log 5/log 2 = 2,322 [M, L].
  - **Sierpinski-Tetraeder** (Finns Tetraeder als Fraktal): Minkowski = Hausdorff = log 4/log 2 = **2** genau; spektral 2 log 4/log 6 = 1,547; Laufdimension log 6/log 2 = 2,585 [M; Formel 2 log(d+1)/log(d+3) aus der Literatur, L].
  - **Beutel:** Mit der Kette aus BAG-DIM (Beutel sieht d_s) folgt fuer das Sierpinski-Tetraeder p = d_s/(1 + d_s) = 0,607. Die Minkowski-Variante waere p = 2/3. Die Zahl der Beutelknoten gegen den Radius folgt trivial der Minkowski-Dimension, weil die Beutel auf Teilstuecken einrasten.
  - **Spektrale Dimension des einfachen kubischen Gitters (Graph-Laplace):** P(sigma) = [e^(-2 sigma) I_0(2 sigma)]^3, also d_s(sigma) = 12 sigma (1 - I_1(2 sigma)/I_0(2 sigma)).
    - Fuer kleine sigma geht das gegen 0, fuer grosse gegen 3 von oben (3 + 3/(8 sigma)).
    - Dazwischen schiesst es ueber 3 hinaus, mit einem Maximum ~3,6 nahe sigma ~ 1 [M, Handrechnung der Leitung mit Bessel-Tabellenwerten; vom Agenten nachzurechnen].
- **Nicht ableitbar:**
  - Form und Hoehe von d_s(sigma) fuer Finns Takt-Operator (umkreisbasierte Gewichte) auf V, C15, A15, Glas und den Danzer-Naeherungen
  - ob es auf irgendeinem unserer Netze an der Dreiecksskala eine Stufe nahe 2 gibt, wie in CDT
  - ob der Beutel auf dem Sierpinski-Tetraeder sauber einrastet (Nebentaeler, Metastabilitaet) und welche Dimension er sieht
- **Kennzahlen-Abgleich:** Sierpinski-Dreieck und Beutel aus BAG-DIM; Netze aus TT-ISO-1, DANZER-NAEHERUNG-2 und TT-GLAS-2. Das Sierpinski-Tetraeder und d_s(sigma) des Takt-Operators sind im Projekt neu.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| MD0 | Kontrolle [M]: Kaestchen-Steigung des 2-Geruests von V: 2,0 +- 0,1 fuer Kaestchen <= a/8 und 3,0 +- 0,1 fuer Kaestchen >= 2a; auf dem Sierpinski-Tetraeder (Stufe >= 6) 2,00 +- 0,05 | 90 % |
| MD1 | Kontrolle [M]: d_s(sigma) des einfachen kubischen Gitters hat ein Maximum zwischen 3,4 und 3,8 und naehert sich 3 von oben | 85 % |
| MD2 | [P-Kette] Sierpinski-Tetraeder: Die spektrale Dimension aus der Waermeleitungsspur liegt im Mittel ueber eine log-Periode bei 1,547 +- 0,08, und der Beutelexponent ueber volle Perioden bei 0,607 +- 0,03, naeher an 0,607 als an 0,667 | 50 % |
| MD3 | [H] Finns Takt-Operator auf V, C15 und A15: d_s(sigma) hat ein Maximum ueber 3,2 und keine Stufe zwischen 1,6 und 2,4 (keine Zone, in der die oertliche Steigung von d_s ueber eine halbe Dekade in sigma unter 0,1 bleibt und d_s dort zwischen 1,6 und 2,4 liegt) | 70 % |
| MD4 | [H] Glas (N = 512, vier Saaten): Das Maximum von d_s liegt mindestens 0,2 unter dem von V | 40 % |

**Bedeutung (vorab):**
- **MD0 trifft ein (erwartet):** Unsere Netze haben an den Dreiecken die Minkowski-Dimension 2 und im Grossen 3. Fraktal sind sie nicht. Das ist die direkte Antwort auf Finns Frage.
- **MD2 trifft ein:** Im Modell gibt es zwei Dimensionen. Beim Zaehlen (Minkowski) sieht man die Geometrie, beim Schwingen und bei Q-Baellen (spektral) die Dynamik. Auf Finns Tetraeder-Fraktal waere das 2 gegen 1,55. Auf den Kristallnetzen fallen beide auf 3 zusammen.
- **MD3 trifft ein:** Finns klassisches Netz zeigt an der Dreiecksskala keine CDT-artige Verkleinerung auf 2, sondern einen Ueberschwinger ueber 3. Das waere ein Unterscheidungspunkt zu CDT, asymptotischer Sicherheit und Horava [H].
  - Vorbehalt: In CDT entsteht die 2 aus dem Mittel ueber viele Geometrien (Quantenensemble). Unser Netz ist eine einzelne klassische Geometrie; der Vergleich ist deshalb nur bedingt.
- **MD3 verfehlt (Stufe nahe 2):** Das waere fuer ein einzelnes klassisches Netz ueberraschend und braeuchte eine Ursachenpruefung.

## Rahmen

- Code-Agent.
  - Code aus RUNDE-24/bag-dim/code (Sierpinski, Beutel), RUNDE-37/takt-umklapp-1/code (Takt-Operator, Hodge-Sterne), RUNDE-37/tt-iso-1/code, RUNDE-37/danzer-naeherung-2/code und RUNDE-37/tt-glas-2/code (Netze) kopieren, dort nichts aendern.
  - Das Sierpinski-Tetraeder selbst bauen, als Graph aus Ecken und Kanten der Teiltetraeder.
- d_s(sigma) aus der Spur exp(-sigma L) ueber das volle Spektrum: periodische Netze ueber Bloch-k (Gitter in der Brillouin-Zone), Glas und Fraktale ueber Eigenwerte. Die Normierung (Takt-Operator mit *0 bzw. Graph-Laplace) im Plan festlegen und begruenden.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu2, cpu3 und cpu4. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
