# QBALL-HADRON-1: Koennen angeregte Q-Baelle Hadronen sein? Erst ueberlegen, was logisch ist, dann das Logische rechnen (Runde 46, Finn-Auftrag)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 05:51:58 CEST (date), vor jedem Abruf und jeder Rechnung.
- **Finn (05.10., vor 05:50:21), woertlich:** "Angeregte qballs hadronen probier auch aus aber überleg was logisch ist"
- **Herkunft:**
  - REGGE-HADRON-REF-L 6.6: drehende Q-Baelle mit J = NQ (Volkov/Woehnert 2002 [S]). Frage an Finn: Regge-Bahnen oder J = NQ-Leitern?
  - RG-1 (RUNDE-06/regge, 2D): Der Turm drehender Q-Baelle folgt J ~ E^2 (alpha 2,01), aber ueber Ringe, deren Ladung mit dem Radius waechst. Das war vorab ableitbar. Nebenprobe bei festem Q: Exponent 0,899 (Q = 300) bzw. 0,924 (Q = 1000); ein starrer Rotor gaebe 2 [P].
  - HAGEDORN-1/-2: Lange Ringe sind instabil (Ausbeulen zur Ellipse, l = 2); stabil sind nur kleine m im Duennwand-Bereich [P].
  - Spin 1/2 ist mit der unveraenderten Formel unmoeglich, nur bosonisch (Gedaechtnis; Codex-Umbau C x S^2) [P].
  - Q-Baelle sind fuer Finn nur noch Teilchenmodell.
- Kennzeichen: [S], [S Abstract], [L], [L?], [M], [E], [P], [H].

## Teil 1: Logik zuerst (Schreibtisch und Literatur, vor jeder Rechnung)

- **Hadronen [L, an PDG pruefen]:**
  - Mesonen haben Baryonenzahl 0, Baryonen Baryonenzahl 1 und Spin 1/2 bzw. halbzahlig.
  - Fuehrende Regge-Bahnen sind linear: J = alpha_0 + alpha' M^2 mit alpha' ~ 0,9 GeV^-2, etwa rho - a2 - rho3 - a4.
  - Die Abstaende M^2(J+1) - M^2(J) sind etwa konstant.
- **Moegliche Zuordnungen (je pruefen, was sie verlangen und was sie ausschliesst):**
  - (i) Q = Baryonenzahl: Baryonen haetten Q = 1. Das ist Quantenbereich statt klassischer Ball, und Spin 1/2 fehlt.
  - (ii) Q-Ball als "Sack" mit Quarks innen (Friedberg/Lee 1977, nichttopologische Solitonen [L?]): Die Anregungen sind dann Quarkanregungen; Regge-Verhalten kaeme von langgezogenen drehenden Saecken (Johnson/Thorn 1976 [L?]).
  - (iii) Ein klassischer Turm bei festem Q mit hadronischem Spin = Windungszahl m (J = mQ): Ist E(m)^2 - E(0)^2 linear in m (Regge), oder E - E0 ~ m^2 (Rotor), oder etwas anderes?
- **Logischer Pruefstein, falls (iii) traegt [M]:** R2 = (E(2)^2 - E(0)^2)/(E(1)^2 - E(0)^2) = 2 und R3 = 3 fuer eine Regge-Gerade. Ein starrer Rotor gibt bei kleiner Anregung R2 ~ 4.
- **Rohdatenprobe (Pflicht vor jeder neuen Rechnung):**
  - Enthalten die RG-1-Rohdaten (RUNDE-06/regge/lauf-lokal, regge2d.py) E(m) bei festem Q (Rotorprobe Q = 300 bzw. 1000)?
  - Wenn ja, sind R2 und R3 eine Auswertung vorhandener Daten, keine Messung. Zuerst so rechnen (auf der .69 oder von Hand), dann entscheiden.
- **Literatur (hoechstens 6 Abrufe):**
  - Volkov/Woehnert 2002
  - Kleihaus/Kunz/List (drehende Q-Baelle in 3D, E(N) bei festem Q? [L?])
  - Friedberg/Lee 1977 bzw. Lee/Pang 1992 (Review nichttopologischer Solitonen)
  - Johnson/Thorn 1976 (rotierender Sack, Regge)
  - Gibt es Arbeiten "Q-Baelle bzw. nichttopologische Solitonen als Hadronen mit Regge-Bahnen"?

## Teil 2: Nur das Logische rechnen (nach Teil 1, eigener Plan)

- Nur wenn Teil 1 zeigt, dass ein Test bei festem Q sinnvoll und nicht schon in Altdaten ist:
  - kleiner 2D-Turm bei festem Q mit m = 0 bis 4 (RG-1-Code, Duennwand-Bereich, stabile m nach HAGEDORN), R2 und R3 messen, oder
  - die 3D-Pruefung (drehende Q-Baelle, achsensymmetrisch), falls in der Zeitbox machbar.
- Sonst ist der Ausgang die logische Antwort mit Begruendung. Das ist ausdruecklich ein gueltiges Ergebnis.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| QH0 | Kontrolle: Die RG-1-Daten bzw. der RG-1-Code reproduzieren die Rotorprobe (Exponent 0,899 bei Q = 300) auf 0,01 | 85 % |
| QH1 | [H] Bei festem Q (2D, RG-1-Familie, stabile m) ist E(m)^2 - E(0)^2 linear in m auf 10 %, also R2 = 2 +- 0,2 | 45 % |
| QH2 | [H] Die Logik schliesst im unveraenderten Modell Q-Baelle als Baryonen (Spin 1/2) und als Mesonen (Q != 0) aus; in der Literatur bleibt nur die Sack-Lesart (Friedberg/Lee) | 70 % |

**Bedeutung (vorab):**
- **QH2 trifft ein:** "Angeregte Q-Baelle = Hadronen" ist im unveraenderten Modell nicht logisch. Logisch ist hoechstens "Q-Ball = Sack, in dem Hadronen-Bausteine sitzen". Das geht so an Finn.
- **QH1 trifft ein:** Bei festem Q verhaelt sich der Turm Regge-artig. Das ist eine nicht triviale Eigenschaft des Modells, auch wenn die Zuordnung zu echten Hadronen offen bleibt.
- **QH1 verfehlt:** Die Q-Ball-Leiter bei festem Q ist kein Regge-Turm. RG-1s J ~ E^2 kam allein von der wachsenden Ladung.

## Rahmen

- Code-Agent mit Literaturteil, hoechstens 6 Abrufe (arXiv-API, INSPIRE-API, arxiv.org per WebFetch), keine Websuche.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu7. Je Lauf hoechstens 10 min, ein Thread. Zeitbox 120 min.
- Plan (Teil 2) vor Hauptlaeufen einfrieren.
