# FADEN-DIM-1: Treffen und vernichten sich gewickelte Faeden auf einem Netz der Raumdimension D = 2 bis 6, und verschiebt Rauheit die Grenze 3? (Runde 43, Warteschlange)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 19:14:29 CEST (date), vor jeder Rechnung.
- **Herkunft:** Kartenvorschlag aus DIM-AUSWAHL-L (RUNDE-37/dim-auswahl-l/DOSSIER.md, Abschnitt FADEN-DIM-1, Z. 244
  ff.). Aufbau, Ableitbarkeitsprobe und F1/F2 von dort sind **bindend und woertlich**; Zusaetze der Leitung sind
  markiert.
- **Finn (04.10., 18:36 bis 18:40):** Einpendeln bei 3 bis 4 Dimensionen? Bis wann bleibt was stabil?
- **Literaturanker:** Brandenberger/Vafa 1989; glatte Faeden treffen sich nur in hoechstens 3 Raumdimensionen.
- Kennzeichen: [M], [E], [S], [L], [ES], [H].

## Aufbau (woertlich aus dem Dossier)

- Hyperkubischer Torus mit je ~1e6 Knoten: D = 3 mit L = 100, D = 4 mit L = 32, D = 5 mit L = 16, D = 6 mit L = 10.
  [Zusatz Leitung: D = 2 mit L = 1000 als zweite Kontrolle.]
- Ein Paar geschlossener Faeden mit Windung +1 und -1 um Richtung 1. Teilen sie einen Knoten, vernichten sie sich.
- **Bewegungsarten:** (G) glatt, starre Faeden, je Schritt Verschiebung in eine zufaellige Querrichtung; (R) rau, lokale
  Metropolis-Zuege, Rauheit ueber eine Biegesteifigkeit einstellbar.
- **Messgroessen** je D und Rauheit: Anteil der Paare, die sich bis T = c L^2 Schritte treffen, und Zeit bis zum
  Treffen.

## Ableitbarkeitsprobe (woertlich aus dem Dossier)

- (G) ist vorab ableitbar: Treffwahrscheinlichkeit je Durchlauf ~ (w/L)^(D-3) bei Fadendicke w. (G) taugt nur als
  Kontrolle K0.
- (R) ist nicht vollstaendig ableitbar. Es konkurrieren die raeumliche Brownsche Schnittregel (d <= 3) [L] und das
  Zittern in der Zeit (bis 5) [H], dazu endliche Dicke und Netzkorrelationen. Messgroesse ist die Kippdimension D*: ab
  ihr faellt der Treffanteil mit L.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| F1 | Kontrolle (G): in D = 3 Anteil ~ 1, in D = 4 Anteil ~ w/L (K0) | 85 % |
| F2 | [H] (R) verschiebt D* von 3 auf 4 oder 5 | 35 % [Zusatz Leitung: Wahrscheinlichkeit von der Leitung gesetzt] |

**Bedeutung (vorab):**
- **F2 trifft ein:** Raue Faeden finden sich auch in mehr als 3 Raumdimensionen. Die Brandenberger/Vafa-Auswahl der
  "3" haengt dann an der Glaette der Faeden [H].
- **F2 verfehlt:** Auch raue Faeden treffen sich zuverlaessig nur bis 3. Die "3" ist fuer Faeden robust.

## Rahmen

- Code-Agent; Start, sobald ein Rechenplatz frei ist.
- Laeufe nur auf der .69 ueber kleintest.sh. Je Lauf <= 10 min, 1 Thread. Zeitbox 90 min.
