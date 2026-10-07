# REGULAER-V-1: Hat Finns Netz V eine Hebehoehe (gewichtete Delaunay-Zerlegung), und wie viel Spielraum hat sie? (Runde 49, Folgekarte aus VIERTE-KOORDINATE-L)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 12:40:49 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - Finn, 05.10.2026: "eine temporäre 4. Dimension wäre doch da ggf sinnvolle oder?" und "Oder eine Drehdimension dann quasi mit Spin".
  - Kartenvorschlag 6.1 aus VIERTE-KOORDINATE-L (RUNDE-37/vierte-koordinate-l/DOSSIER.md), weitgehend woertlich; Zusaetze der Leitung markiert.
- **Projektbefunde [P]:**
  - HODGE-L (DOSSIER 1a, Abschn. 4.3): V ist weder gut zentriert noch Delaunay; an 12 von 116 Flaechen je Zelle ist die Insphaeren-Bedingung bei w = 0 verletzt [M, von Hand].
  - VIERTE-KOORDINATE-L:
    - Delaunay ist die Unterseite der Huelle der auf |x|^2 angehobenen Punkte; gewichtete Delaunay mit Hoehen |x|^2 - w [M am Schreibtisch, Formel an keiner Quelle gesehen].
    - Die Hebehoehe ist in der Ebene gleichwertig zu einer Spannungsfunktion (Maxwell/Cremona). Die Gewichte wirken nicht auf die Regge-Wirkung bei festen Kantenlaengen und werden im Kontinuum konstant (de Goes 4.2) [S].
    - VK5: Eine dynamische Hebehoehe als physikalisches Feld ist nach Recherchestand nicht bekannt.
  - LAMBDA-TURING-L: Auf V liegen die 6 Oktaederecken auf einer Kugel; jede der 3 Diagonalen ist Delaunay (Flip-Flop).
  - UMKLAPP-1, TAKT-DYNAMIK-1: Die Dynamik nutzt Delaunay als Auswahlregel.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe

- **Vorab ableitbar [M]:**
  - w = konstant ist unzulaessig (12 von 116 Flaechen je Zelle verletzt, HODGE-L).
  - Die Regge-Wirkung haengt nicht an w; eine Konstante in w ist Eichrichtung; lineare Anteile in w sind auf dem Torus nicht periodisch.
  - Lokal regulaer an jeder Flaeche heisst global regulaer, weil die Hebung eine stueckweise lineare Funktion ist und lokale Konvexitaet genuegt.
- **Schreibtisch vor der Rechnung (Pflicht, im Plan) [Zusatz Leitung]:** die Bahnen der Raumgruppe (Fd-3m) auf den Ecken von V zaehlen. Mit bahnweise konstanten Gewichten bleiben wenige Unbekannte. Ist das LP dann von Hand loesbar, ist RV2 vorab entschieden; das Ergebnis vor dem Rechnen in den Plan schreiben.
- **Nicht ableitbar:**
  - ob ein nichtkonstantes w existiert
  - Breite der Gewichtskammer und welche Zuege an ihren Waenden liegen
  - Wirkung auf die l = 4-Anisotropie des gewichteten Laplace

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RV0 | Kontrolle: Bei w = 0 meldet das LP genau die 12 verletzten Flaechen je Zelle aus HODGE-L. Eine Delaunay-Zerlegung zufaelliger Punkte ist bei w = 0 zulaessig. Ein bekannt nicht-regulaeres Beispiel (2D "mother of all examples" [L], als Prisma in 3D) ist unzulaessig | 85 % |
| RV1 | [H] V ist regulaer (t_max > 0) | 55 % |
| RV2 | [H] Falls regulaer: bahnweise konstante (Fd-3m-symmetrische) Gewichte genuegen | 60 % |
| RV3 | [H] Innerhalb der Kammer aendert sich die langwellige l = 4-Anisotropie des gewichteten Laplace um weniger als 10 % ihres Werts in der Kammermitte | 50 % |

**Bedeutung (vorab):**
- **RV1 trifft ein:** Finns "vierte Richtung beim Zusammensetzen" gibt es fuer V als Hebehoehe, mit messbarem Spielraum. Dynamische Gewichte koppeln dann nur an die Materie; die Pruefung als universelles Feld (Fuenfte-Kraft-Schranken) wird sinnvoll.
- **RV1 verfehlt:** V hat keine Hebung. Die vierte Richtung gibt es fuer V dann nur als Zeit (Regge) oder als S^3-Kruemmung. Fuer die Delaunay-Dynamik auf V hiesse das: V ist kein Ruhezustand der Auswahlregel [Zusatz Leitung, H].

## Rahmen

- Code-Agent.
  - Lineares Programm auf einer periodischen Superzelle (L = 1 und 2): je innerer Dreiecksflaeche eine gewichtete Insphaeren-Ungleichung (linear in w) mit Marge t; t maximieren.
  - Danach Stichproben in der Kammer; gewichteter Hodge-Stern (3D-Gegenstueck nach Glickenstein bzw. de Goes, im Plan festlegen) und dessen l = 4-Anisotropie wie in DANZER-NAEHERUNG-2.
  - Netzbau aus RUNDE-37/tt-iso-1/code (V) und der Flaechenliste aus HODGE-L (falls dort Code bzw. Tabellen liegen); dort nichts aendern.
- Kontrolle: Das Ergebnis darf nicht von der Superzellengroesse (L = 1, 2) abhaengen.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
