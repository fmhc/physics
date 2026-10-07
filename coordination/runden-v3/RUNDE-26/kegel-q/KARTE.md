# KEGEL-Q: Haftet ein Q-Ball an einer Fuenfer-Ecke des Dreiecksnetzes? (Runde 26)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 04:05:09 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - Finns Dreieckskugel (KUGELSCHALE-1: 12 Fuenfer-Ecken, bei grossem gamma als Spitzen).
  - RUNDE-23/IDEEN-LOGIK-TEILCHEN.md, Befund 3a.
  - Pool-Eintrag KEGEL-Q.
- **Schreibtisch der Leitung (exakt fuer den zentrierten Ball):**
  - Ein Kegel mit Defizit delta hat den Winkelumfang Theta = 2 pi - delta, eine Fuenfer-Ecke delta = pi/3, eine
    Siebener-Ecke delta = -pi/3.
  - Fuer einen Q-Ball auf der Spitze gilt dieselbe radiale Gleichung wie in der Ebene; nur die Flaeche skaliert mit
    Theta/2 pi. Daher gilt exakt E_Kegel(Q) = E_eben(s Q)/s mit s = 2 pi/Theta.
  - Weil E/Q bei VK-stabilen Baellen mit Q faellt, ist die Bindung B(Q) = E_eben(Q) - E_eben(sQ)/s positiv an
    Fuenfer-Ecken und negativ an Siebener-Ecken.
  - Duennwandig: B ~ 8,7 % bzw. -8,0 % der Oberflaechenenergie.
  - Abseits der Spitze ist der Kegel flach. Die Kraft wirkt also nur, solange der Ball die Spitze ueberdeckt, und faellt
    danach mit dem Schwanz exp(-2 kappa d) ab (kappa^2 = 1 - omega^2) [H].
- **Ableitbarkeitspruefung:** Die Bindung bei d = 0 folgt aus der ebenen 2D-Familie (exakt, nur Interpolation). Die
  Kraft gegen den Abstand und das Gittermodell sind nirgends gerechnet.

## Test (Code-Agent)

- **Modell M1** (U = S - S^2 + S^3/2), 2D.
- **Gitter:**
  - Trianguliertes Gebiet mit einer Fuenfer-Ecke in der Mitte (aus einem Sechseckflicken ein 60-Grad-Keil entfernt und
    verklebt).
  - Zum Vergleich eine Siebener-Ecke (Keil eingefuegt) und ein flacher Flicken (Kontrolle).
  - Laplace als Kotangens-Laplace mit Eckflaechen.
  - Feine Gitter (Kante h <= 0,4) und gross genug fuer die Baelle (Radius um 5 bis 10).
- **Energie bei fester Ladung Q** (phi = f e^{i omega t}, f reell):
  - E[f] = Q^2/(4 Sum A_i f_i^2) + Sum ueber Kanten w_ij (f_i - f_j)^2 + Sum A_i U(f_i^2)
  - Minimieren bei festem Q.
- **(a) Bindung bei d = 0:**
  - Ball auf der Spitze gegen Ball weit weg bzw. im flachen Flicken, bei mehreren Q.
  - Vergleich mit E_eben(sQ)/s aus der ebenen Familie (radial gerechnet).
- **(b) Kraftgesetz:** Energie gegen den Abstand d des Ladungsschwerpunkts von der Spitze. Weg im Plan festlegen, z. B.
  festgehaltener Schwerpunkt per Nebenbedingung (Lagrange-Multiplikator, keine Strafenergie in E) oder Freilauf mit
  Beschleunigungsmessung.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KQ0 | Flacher Flicken: Die Ball-Energie haengt nicht vom Ort ab (Schwankung < 1e-4 relativ, ausser am Rand) | 85 % |
| KQ1 | Fuenfer-Ecke, d = 0: B(Q) trifft E_eben(Q) - E_eben(sQ)/s innerhalb 5 % (Diskretisierung), bei mindestens drei Q | 65 % |
| KQ2 | Fuenfer-Ecke zieht an (E(d) steigt mit d), Siebener-Ecke stoesst ab (E(d) faellt mit d) | 75 % |
| KQ3 | Kurze Reichweite: Fuer d > R_ball + 4/kappa ist |E(d) - E(unendlich)| < 1 % von |B| | 60 % |

**Bedeutung (vorab):**
- KQ1 bis KQ3 treffen ein:
  - Q-Baelle werden von Fuenfer-Ecken (positive Kruemmung) mit einer kurzreichweitigen Kraft gebunden und von
    Siebener-Ecken abgestossen, wie ein Tropfen im Kegel (Kapillaritaet [L?]).
  - Auf einer facettierten Dreieckskugel saessen Q-Baelle an den 12 Spitzen [H]. Das waere eine Bruecke zwischen
    Geometrie-Teilchen (Defekten) und Feld-Teilchen.
- KQ2 trifft nicht ein: Das Vorzeichen der Kruemmungskraft ist anders als im Duennwand-Bild. Beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min, 4 GB).
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf vorher erlaubt, mit Parametern, die in keinem echten Lauf
  vorkommen.
- Zeitbox 120 min.
