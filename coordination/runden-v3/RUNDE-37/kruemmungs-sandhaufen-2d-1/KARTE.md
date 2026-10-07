# KRUEMMUNGS-SANDHAUFEN-2D-1: Gibt Finns Regel "Kruemmung wird umverteilt" Lawinen wie ein Sandhaufen? (Runde 48, Finns Idee, 2D-Vorstufe)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 11:12:43 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - Finn, 05.10.2026, woertlich: "Self organized criticality und so" und "Was ist wenn Krümmung zu Spannung wird und umgekehrt?"
  - Leitung an Finn (10:37): Die Regel "Fehlwinkel ueber Schwelle wird an die Nachbarn verteilt" waere die fehlende Umverteilung fuer SOC. Gebaut wird sie, sobald geklaert ist, ob es sie schon gibt.
  - KRUEMMUNG-SPANNUNG-SPIN-L (KS5 nicht eingetroffen, nach Recherchestand, 19 Abrufe): Eine Sandhaufen-Regel mit Fehlwinkel als Korn ist nicht gefunden. Nahtreffer: Dantas 2021, Vacaru 2010, Vallarino 2026, T1-Umordnungen im Schaum.
  - Der Kartenvorschlag ist woertlich aus dem DOSSIER uebernommen (Abschnitt 6.2). Zusaetze der Leitung sind mit [Zusatz Leitung] markiert.
- **Projektbefunde [P]:**
  - SOC-RAUM-L (RUNDE-48): Flache Umklappzuege verteilen keine Kruemmung um; SOC braucht eine Umverteilungsregel. 1/f ist keine allgemeine SOC-Folge.
  - RAUM-GAS-L: Umklappen darf keine Wellenenergie kosten.
  - Projektsuche (Sandhaufen, Lawine, sandpile, avalanche, Kantenflip, BTW): nur RUNDE-05 (Q-Ball-"Lawinen" in 1D, Bio-Analogie, geparkt). Ein Kruemmungs-Sandhaufen ist im Projekt neu.
- Kennzeichen: [M], [E], [P], [S], [L], [H], [ES].

## Modell

- Dreiecksflaeche (kombinatorisch). Kruemmungsladung der Ecke v: q_v = 6 - c(v), c = Zahl der Nachbarn (Bowick/Giomi, S. 22 [S, aus dem DOSSIER]).
- **Bezug zu Regge [M, Zusatz Leitung]:** Bei gleichseitigen Dreiecken ist der Fehlwinkel an v genau q_v pi/3. Die Ladung ist also die Regge-Kruemmung eines gleichseitigen 2D-Netzes (dynamische Triangulierung). In 3D waere das Gegenstueck 2 pi - c arccos(1/3) je Kante.
- **Kippen:** Eine Ecke mit abs(q_v) >= 2 kippt. Ein Kantenflip in ihrem Stern senkt abs(q_v) um 1 und gibt die Ladung an Nachbarn weiter.
  - Bei q_v >= 2 (zu wenig Nachbarn) wird eine Kante des Rings um v geflippt, sodass v eine Kante gewinnt.
  - Bei q_v <= -2 (zu viele) wird eine Kante an v geflippt.
  - Die Wahl der Kante und der Reihenfolge legt der Plan fest. Es gibt zwei Arme: zufaellig und deterministisch.
- **Antrieb:** ein zufaelliger Flip je Schritt, Lawinen laufen vor dem naechsten Antrieb zu Ende (Zeitskalentrennung).
- **Zulaessigkeit:** keine Ecke vom Grad < 3, keine Doppelkanten. Ein Flip, der das verletzt, ist nicht erlaubt.
- **Senke:** Auf der offenen Scheibe kippen Randecken nicht und nehmen Ladung auf. Die geschlossene Kugel hat keine Senke.

## Ableitbarkeitsprobe

- **Vorab ableitbar [M]:**
  - Summe q_v = 6 chi bleibt bei jedem Flip erhalten (Kugel: 12).
  - Ein Flip aendert genau vier Ladungen um +-1: Die Enden der alten Kante verlieren je einen Nachbarn, die zwei gegenueberliegenden Ecken gewinnen je einen.
  - Die Kugel hat keine Senke.
  - **[Zusatz Leitung]:** Die Zustandsmenge ist endlich und der Antrieb zufaellig, also hat die Kette eine stationaere Verteilung. "Keine stationaere Verteilung" ist deshalb keine pruefbare Vorhersage. KH2 ist darum umformuliert (siehe unten), der Entwurf steht im DOSSIER.
  - **[Zusatz Leitung]:** Anders als im BTW-Sandhaufen ist Summe abs(q) nicht erhalten. Ein Kippen senkt eine Ladung und kann drei andere heben.
- **Vorab erwartbar [ES, P]:** Ohne Senke haengt das Verhalten an der Ladungsdichte, wie bei einem Sandhaufen fester Energie.
- **Nicht ableitbar:**
  - die Verzweigungsrate
  - ob mit Senke ein Potenzgesetz entsteht
  - Exponent und Abschneiden in Abhaengigkeit von N

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KH0 | Kontrolle [M]: Summe q_v = 12 auf der Kugel nach jedem Schritt exakt; keine Ecke vom Grad < 3, keine Doppelkanten | 95 % |
| KH1 | [H] Auf der offenen Scheibe folgt P(s) ueber mindestens 2 Dekaden einem Potenzgesetz mit tau zwischen 1,0 und 1,6 | 35 % |
| KH2 | [H, umformuliert von der Leitung] Auf der geschlossenen Kugel zeigt P(s) kein Potenzgesetz ueber mindestens 2 Dekaden (fehlende Senke) | 60 % |
| KH3 | [H] Auf der Scheibe waechst das Abschneiden s_c mit N wie N^D, D > 0,3 (N = 500, 2000, 8000) | 40 % |

**Bedeutung (vorab, aus dem DOSSIER):**
- **KH1 und KH3 treffen ein:** Finns Umverteilungsregel gibt SOC, aber nur mit Senke. Fuer 3D waere der Kandidat fuer die Senke die Nicht-Erhaltung von Summe l eps [M]; das waere als SOC-UMKLAPP-1-Regel zu pruefen.
- **KH1 scheitert:** Der Kruemmungs-Schwellwert allein gibt keine Lawinen. Dann ist die Kopplung ueber Spannung (Bowick/Giomi Gl. 55, Schaum-T1) der naechste Kandidat; dort gibt es Lawinen nur nass ([P] Tewari).
- **[Zusatz Leitung]:** Das ist eine kombinatorische 2D-Vorstufe ohne Geometrie und Dynamik der Laengen. Sie zeigt nur, ob die Regel ueberhaupt Lawinen erzeugen kann, nicht, ob Finns 3D-Raum sie hat. Eine Folge fuer Lambda oder Schwerewellen gibt es daraus nicht.

## Kontrollen (aus dem DOSSIER)

- Ein BTW-Sandhaufen auf demselben Graphen eicht die Exponenten.
- zufaellige gegen deterministische Flip-Wahl
- Antriebsrate gegen null pruefen (versteckter Parameter, SOC-RAUM-L [P])

## Rahmen

- Code-Agent. Neuer Code (2D-Triangulierung mit Kantenflips). Als Startnetz eine zufaellige Delaunay-Triangulierung bzw. eine geodaetische Kugel; die Wahl begruendet der Plan.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu7. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
