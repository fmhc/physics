# RUECKFLUSS-INFO-1: Bringen die 44 % aus der verborgenen Haelfte Information zurueck oder nur Rauschen, und haengt die Zahl an der Paketbreite? (Runde 45, Luecke L5)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 04:50:39 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - Kartenvorschlag aus PT-AUSGLEICH-L (RUNDE-37/pt-ausgleich-l/DOSSIER.md, Abschnitt 6). Frage, Bau, RI1, RI2 und Ableitbarkeitsprobe von dort sind **woertlich bindend**; die Wahrscheinlichkeiten setzt die Leitung. Zusaetze der Leitung sind markiert.
  - SPIEGEL-HAELFTE-1 (RUNDE-37/spiegel-haelfte-1/): Bei W = 2 pi kommen r = 0,44 des abgeflossenen Gewichts zurueck. Gerechnet ist nur sigma = 4. Die Heuristik A9 erwartet r ~ 1/2.
  - GEMEINSAMES-NETZ v3.1 fuehrt die 44 % als Zahl in L5.
- **Finn (05.10.):** "teste herum, was richtig ist".
- Kennzeichen: [M], [E], [P], [H].

## Frage (woertlich aus dem Dossier)

Traegt der Rueckfluss aus der verborgenen Haelfte Information zurueck, wie im ungebrochenen PT-Bild (Kawabata/Ashida/Ueda: vollstaendige Rueckgewinnung), oder nur Rauschen, wie im gebrochenen?

## Bau

- **Woertlich:**
  - SPIEGEL-HAELFTE-1-Code unveraendert, als Kopie.
  - Zwei sichtbare Startpakete, gleiche Breite, verschiedener Spin oder Impuls.
  - Spurabstand D(t) der beiden reduzierten Zustaende der sichtbaren Haelfte fuer W in {0, pi, 2 pi}, je (i) mit festen Takten je Knoten und (ii) mit in jedem Schritt neu gezogenen Takten.
  - Mass fuer den Rueckfluss: Summe der Anstiege von D(t) bis t = 100 (Breuer-Laine-Piilo-artig [L]).
- **[Zusatz Leitung, technisch]:** "Reduzierter Zustand der sichtbaren Haelfte" ist hier die Einschraenkung auf den sichtbaren Unterraum P_2 (direkte Summe, kein Tensorfaktor).
  - Bei festen Takten ist rho_2^A - rho_2^B hoechstens vom Rang 2. Der Spurabstand folgt dann exakt aus der 2x2-Gram-Matrix von psi_2^A und psi_2^B.
  - Bei neu gezogenen Takten wird ueber M Ziehungen gemittelt, mit M vorab im Plan festgelegt. Der Spurabstand folgt aus der Gram-Matrix der 2M Vektoren.
  - Die Normierungskonvention fuer unternormierte Zustaende legst du im Plan vor der Rechnung fest.
- **[Zusatz Leitung, sigma-Leiter]:** Rueckgabequote r(t) = (w_2 - N_FJ)/(1 - N_FJ) wie in SPIEGEL-HAELFTE-1, bei W = 2 pi und festen Takten.
  - Breiten sigma = 4 (Kontrolle gegen 0,440), 8 und, falls es in 10 min pro Lauf passt, 12.
  - Zeiten bis t = 100, bei sigma = 4 zusaetzlich bis t = 200.
  - Gitter gross genug, dass der Rand bis t nicht erreicht wird; die Groesse steht im Plan.

## Ableitbarkeitsprobe (woertlich, dazu Zusatz)

- **Vorab ableitbar:**
  - W = 0: kohaerent, eta existiert, D(t) bleibt nahe am Startwert (S5).
  - Der Mittelwert der Amplitude bei W = 2 pi ist FJ (A8).
  - Bei neu gezogenen Takten folgt das Gewicht im Mittel einer Ratengleichung mit Gleichverteilung w_2 -> 1/2 (wie PLAN A9) [P, H].
- **Nicht ableitbar:** ob bei festen Takten (W = 2 pi) D(t) wieder steigt (Rueckgewinnung trotz verwuerfelter Phase) und ob neu gezogene Takte das verhindern.
- **[Zusatz Leitung]:** Ob r von sigma abhaengt, ist nicht ableitbar.
  - Der FJ-Verlust skaliert diffusiv mit t/sigma^2 (PT-AUSGLEICH-L, S2).
  - Die Mischung zwischen den Haelften ist oertlich. Beides zusammen legt keine Zahl fest.
- Projekt-grep (Loschmidt, Spurabstand, Kawabata, pseudo-herm, pseudo-unit): keine solche Karte (laut Dossier).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RI0 | Kontrolle: sigma = 4, W = 2 pi, feste Takte gibt r(100) = 0,440 +- 0,01 (SPIEGEL-HAELFTE-1) | 85 % |
| RI1 | [H, woertlich] Feste Takte, W = 2 pi: D(t) steigt bis t = 100 mindestens einmal um mehr als 1e-3 | 55 % |
| RI2 | [H, woertlich] Neu gezogene Takte, W = 2 pi: kein Anstieg ueber 1e-3, solange die Summe der Anstiege bei festen Takten groesser ist | 55 % |
| RI3 | [H, Zusatz Leitung] r(100) haengt nicht an der Breite: sigma = 8 (und 12) liegen innerhalb 0,44 +- 0,03 | 45 % |

**Bedeutung (woertlich, dazu Zusatz):**
- **RI1 trifft ein:** Finns Haelfte mit festem eigenem Takt ist "teilweise ungebrochen"; Information kommt zurueck.
- **RI1 verfehlt:** Der Ausgleich gibt Gewicht, aber keine Information zurueck. Fuer L5 bleibt nur der kohaerente Teil-Umklapp.
- **[Zusatz Leitung] RI3 verfehlt:** Die 44 % sind keine Kennzahl des Modells, sondern haengen an der Paketbreite. In GEMEINSAMES-NETZ v4 stehen sie dann nur mit sigma, oder mit dem Grenzwert, falls einer sichtbar wird (Heuristik A9: 1/2).

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und cpu6. Ist p4000b frei, darf er sie zusaetzlich nehmen.
- Je Lauf hoechstens 10 min, ein Thread. Zeitbox 90 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Ein ehrlicher Teilbericht ist besser als keiner.
