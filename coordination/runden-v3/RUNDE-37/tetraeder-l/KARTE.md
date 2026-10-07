# TETRAEDER-L: Eigenschaften, Wechselwirkungen und Umformungen von Tetraedern; Formen aus Formen (Literaturkarte, Runde 41)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-04 14:51:58 CEST (date), vor jedem Abruf.
- **Auftrag von Finn (04.10., woertlich):**
  - Nachricht zwischen 14:20 und 14:29: "recherchiere in der literatur was für eigenschaften und wechselwirkungen von
    tetraedern und so ausgehen bzw von transformationen"
  - Nachricht zwischen 14:29 und 14:31, zweiter Teil: "können wir aus verschiedenen formen oder punktwolken andere
    formen machen die was bedeuten?"
  - Der Drehungs-Teil derselben Nachricht (synchrones Drehen, Hopf, ladungstauschende Q-Baelle) liegt bei GUERTEL-1,
    hier nicht bearbeiten.
- **Vorarbeit im Projekt (zuerst lesen, nichts doppelt abrufen):**
  - RUNDE-34/TETRAEDER-ANALYSE.md: Analyse der Leitung mit Rechentabelle (Abschn. 1) und Analogien aus dem Gedaechtnis
    (Abschn. 3: Spin-Eis, Fraktonen, A4 und drei Familien, Spin 1/2 nur ueber Topologie, Frank-Kasper und
    Quasikristalle, Methan-Spektren). Fast alles dort ist [L]; diese Karte soll die tragenden Punkte an der Quelle
    pruefen und Neues ergaenzen.
  - RUNDE-37.md, Ernte PONZANO-1: 6j-Symbole, Ponzano-Regge, Biedenharn-Elliott (Pachner 2-3) exakt gerechnet; nicht
    erneut recherchieren, nur einordnen.
  - RUNDE-37/tensor-eis-pyro-1/ (zwei Graviton-Welten auf Auf- und Ab-Tetraedern), RUNDE-37/twist-pyro-1/,
    RUNDE-37/twist-spin-1/ERGEBNIS.md (T, nicht 2T), RUNDE-37/weltmodell-review-1/REVIEW.md (K-A, K-M, K-B),
    RUNDE-41.md Warteschlange (K-AM: Tetraeder als Raumscheiben eines Regge-Gitters, Flip-Flop Auf/Ab).
  - RUNDE-37/wolfram-scan-l/DOSSIER.md, Kartenvorschlag K2 (Pachner-Zuege auf Tetraedern als Wachstumsregel).
  - Ideenpool IDEEN-EVOLUTION/pool.jsonl (jq nach "TETRA", "A4", "Pachner").
- Kennzeichen: [S] an der Quelle gelesen (Zeile bzw. Abschnitt), [S Abstract], [P] Projektdatei, [L] Gedaechtnis,
  [L?] unsicher, [ES] eigener Schluss, [H] Hypothese.

## Erwartungen der Leitung (vor jedem Abruf) [L, L?]

| Nr | Erwartung |
|---|---|
| E1 | Harte Tetraeder ordnen sich von selbst zu einem dodekagonalen Quasikristall (Haji-Akbari u. a., Nature 2009); die dichteste bekannte Packung liegt bei etwa 0,856 (Dimer-Packung, Chen/Engel/Glotzer 2010) [L] |
| E2 | A4-Flavor: Die tribimaximale Mischung ist seit theta_13 != 0 (2012) ausgeschlossen; aktiv ist die modulare Form (Feruglio 2017, Gamma_3 = A4) mit Vorhersagen fuer Massensumme und CP-Phase; keine Bestaetigung [L] |
| E3 | Zamolodchikovs Tetraedergleichung (1980/81) ist das 3D-Gegenstueck der Yang-Baxter-Gleichung und beschreibt die faktorisierte Streuung gerader Strings in 2+1 Dimensionen; Loesungen gibt es (Bazhanov/Stroganov u. a.), ein physikalisches 3+1-Teilchenmodell daraus nicht [L?] |
| E4 | Quanten-Tetraeder (Barbieri 1998, Baez/Barrett 1999): Winkel bzw. Flaechen-Normalen nicht vertauschbar, Volumen mit diskretem Spektrum; Grenzfall der Amplituden ist die Regge-Wirkung (im Projekt PONZANO-1) [L] |
| E5 | Pachner-Zuege verbinden je zwei Triangulierungen derselben PL-Mannigfaltigkeit (Pachner 1991); als Dynamik: euklidische dynamische Triangulierungen scheitern (verzweigte Polymere bzw. zerknuellte Phase), kausale (CDT, Ambjoern/Jurkiewicz/Loll) geben eine ausgedehnte 4D-Phase mit spektraler Dimension um 2 im Kleinen [L] |
| E6 | Formen aus Formen: Quasikristalle als Schnitt eines hoeherdimensionalen Gitters (cut and project) sind etabliert; Tetraeder-Quasikristalle aus E8 (Quantum Gravity Research) sind nicht in etablierten Physik-Zeitschriften geprueft [L?] |
| E7 | Punktwolken zu Formen: Delaunay/Voronoi (im Projekt Standard) und persistente Homologie (Kosmisches Netz, amorphe Materialien) sind etablierte Werkzeuge; fuer entstehende Geometrie aus Zufallsnetzen bzw. Kausalmengen gibt es hoechstens Einzelarbeiten [L?] |
| E8 | Auf- und Ab-Tetraeder: Zwei durchdrungene Tetraeder bilden die Sternoktaeder-Figur (Ecken eines Wuerfels, Schnitt ein Oktaeder); die Mittelpunkte der Pyrochlor-Tetraeder bilden das zweiteilige Diamantgitter, die zwei Teilgitter sind genau Auf und Ab [L, M] |

## Fragen

1. **Eigenschaften:** Symmetrie (T, T_d, 2T, Darstellungen, McKay), Packung und Selbstordnung, Frustration (7,36 Grad),
   Quanten-Tetraeder. Was ist an der Quelle belegt, was aus TETRAEDER-ANALYSE bleibt [L]?
2. **Wechselwirkungen:** Regel je Tetraeder (Spin-Eis: emergente U(1), Monopole mit 1/r; Tensor-Regeln: Fraktonen),
   Tetraedergleichung (Streuung gerader Strings, Bezug zu Finns Punkte-ergeben-Striche und STRING-1), Kopplung von Auf-
   und Ab-Tetraedern.
3. **Umformungen:** Pachner-Zuege als Dynamik (CDT, Wachstumsregeln), Dualitaeten (Pyrochlor/Diamant, Sternoktaeder,
   Rektifizierung zum Oktaeder), Schnitt aus hoeheren Dimensionen.
4. **Formen aus Formen bzw. Punktwolken:** Welche Umformungen haben Bedeutung, weil sie etwas erhalten (Volumen,
   Reihenfolge, Topologie, Symmetrie)?
5. **A4 und drei Generationen:** Stand 2024 bis 2026 an der Quelle; gibt es eine konkrete, pruefbare Vorhersage?

**Je Punkt:** Bezug zu K-A bzw. K-AM, ob ein kleiner Test (<= 10 min) moeglich ist, und die Ableitbarkeitsprobe
(was steht schon in der Literatur oder in Projektdaten).

## Auftrag (feldforscher)

- Gezielte Abrufe hoechstens 14, keine Websuche (Kontingent erschoepft). arXiv-Abstracts, Volltexte und
  API-Abfragen zaehlen je als Abruf. Lokale Kopien in quellen/; Fundstellen nur aus selbst gelesenem Text.
- Je Erwartung den Ausgang mit Fundstelle; Gegensweep gegen die eigenen Selbstverstaendlichkeiten.
- **Abgabe:** RUNDE-37/tetraeder-l/DOSSIER.md und ARBEITSFELD.md, mit:
  - Ergebnis zuerst
  - Erwartungen mit Ausgang
  - Projektbezug je Punkt
  - hoechstens zwei Kartenvorschlaege mit Ableitbarkeitsprobe
  - Quellenliste mit Abrufstand
  - "Einfach gesagt" (3 bis 5 Saetze, fuer Finn)

## Rahmen

- Zeitbox 90 min. Kein Rechnen; lokal kein python, awk oder perl.
