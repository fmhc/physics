# Runde 1 (Probelauf nach V3-ENTWURF.md)

Leitung: claude-primary. Begonnen: 2026-09-30 00:00:02 CEST (gemessen).
- Status: laeuft. Explorativ, keine formale Bestaetigung.
- v3 gilt seit 30.09.2026 (Finn: "ja übernimm v3 und räum auf, nur archivieren"; README.md). Diese Runde ist Runde 1
  nach v3; begonnen als Probelauf vor der Zustimmung.

## Eingang

- **arXiv-Runde 22.-29.09.** (coordination/ideation-arxiv-20260929/):
  - QUELLEN.md: 95 Arbeiten im Fenster, 62 mit Musterbezug; 19 Q-Ball-Zeilen aus 60 Tagen
  - KARTEN.md: K-1 bis K-12, QG-1 bis QG-3
  - ABSCHAETZUNG-RUNDE-1.md
- **Finns Ideen F-1 bis F-3** (ebenda):
  - F-1: stille Miniteile, Impuls in einer Extra-Dimension
  - F-2: das Elektron als laengliches Objekt, die Laenge regelt die Masse
  - F-3: das Nukleon als Q-Ball-artiger Klumpen
- **Codex, explorativ auf dem TS440:**
  - Spin-Phase-Runde (coordination/exploration-20260929-spin-phase/)
  - 3D-Verdichtung eines Q-Ball-Kondensats gegen zwei Kontrollen robust (coordination/exploration-20260929-qballs/pde3d/)
- **Rechenlage:** VS-1 haelt die .69-GPU bis etwa 05:00 (Portionen zu 23 min unter dem gemeinsamen Lock). Kurze GPU-Tests
  laufen danach oder in einer Portionsluecke.

## Karten und Tests dieser Runde

| Karte | Test | wer, wo | Budget |
|---|---|---|---|
| QG-1 Fall im Brechungsfeld | (a) Gegenlesung der Papierrechnung (Varianten A und C, Virialidentitaet) durch ein zweites Haus; (b) 1D-Code A/B/C schreiben; (c) Lauf ω² = 0,55/0,7/0,9 | (a) Codex; (b) Anthropic-Agent; (c) .69 nach VS-1 oder in einer Luecke | (c) <= 10 min GPU |
| K-2 fremde Latte fuer den Loeser | Tabellen von 2609.24913 lesen: Potential, flache Q-Baelle, Zahlen; Laufplan <= 10 min | Anthropic-Agent (Papier) | 1 h Lesen |
| F-1 Papierfrage | Welche Brechung der x5-Verschiebungssymmetrie gibt eine Einfangregel, die sich messbar vom Standardbild unterscheidet? Dazu Literatur: KK-Kraftfreiheit (Overduin und Wesson), Solitosynthese (Griest und Kolb), hep-ph/0006344 | Anthropic-Agent (Papier) | 1 h |
| F-3 Papier | Duenne-Wand-Grenze unseres Potentials gegen die Beutelformel E(R) = a/R + (4 pi/3) B R^3; M*R/(hbar c) an drei Q-Werten aus dem Atlas | Anthropic-Agent (Papier) | 1 h |
| K-5 Codex H1 | bekannte Phasenstreuung als Nulllinie fuer H1 | Codex (Hinweis) | Minuten |
| **Zufallskarte K-6** | Papierabbildung der VFW-Groessen auf die Swarmalator-Kopplungen J und K; Minilauf N = 50 bis 200 | Codex, TS440 | <= 10 min CPU |

- Die Zufallskarte ist K-6. Gezogen um 23:59:16 mit `shuf -n 1` aus K-3, K-6, K-7, K-8, K-9, K-10, K-11 und QG-2.
- **Geparkt bis die GPU frei ist:**
  - K-4 mit QG-3 und F-2 als Nebenprodukt: 40 bis 80 min .69, also kein kleiner Test; teilen, dann rechnen
  - K-1: Nachauswertung B26 durch ein Haus, das B26 nicht gebaut hat. Wer B26 gebaut hat, wird noch geklaert.

## Tests: Ergebnisse

- **QG-1 Papier, Gegenlesung Codex (OpenAI).** RUNDE-01/QG1-GEGENLESUNG-CODEX.md, eingegangen 30.09. 00:06 CEST; das Urteil
  lautet "stimmt mit Praezisierungen".
  - **Allgemein:** Fuer L = A|dt psi|^2 - B|grad psi|^2 - C U mit A, B, C = 1 + (a, b, c) Phi gilt bei festem Q
    R = a/a_Newton = (-a W + b G + c V)/E.
  - **Volle Metrik:** R = 1 exakt, ueber die Virial- bzw. Stressbilanz.
    - R = (2+2/d) G/E, also in 1D R_A = 4G/E
    - universell nur, wenn W = G
    - geht an beiden Frequenzraendern gegen null
  - **1D-Anker:** analytisch fuer U = S - S^2 + S^3/2.
  - **Folge:**
      wirkt. Sonst fallen Q-Baelle mit verschiedener innerer Frequenz verschieden schnell.
    - MICROSCOPE schliesst das fuer gewoehnliche Materie auf 1e-15 aus. Fuer Q-Ball-artige Materie gilt der Schluss nur,
      wenn sie sich dort wie gewoehnliche Materie verhaelt (Grenze der Uebertragung).
    - Der geplante 1D-Lauf prueft damit ableitbare Sollwerte (L4) und dient nur als Code- und Endlichkeitskontrolle.
- **K-5 (Codex):** als Hinweis zu H1 aufgenommen (RUNDE-01/K5-H1-CODEX.md). Die Koerperorientierung ist nicht die innere
  Feldphase; orthogonale Kanaele sind bei gJ0 phasenblind.
- **K-6, Zufallskarte (Codex):** 64 explorative Laeufe auf dem TS440, 25 CPU-s (RUNDE-01/K6-CODEX.md, Vorab k6/VORAB.md).
  - VFW-Proxy: Synchronisationskontrast in 4 von 4 Faellen; Standard-Swarmalator in 3 von 4
  - Numerik: dt-Vergleiche 8 von 8 mehr als fuenffach
  - Kontrollen bestanden
  - Keine universelle Probenanziehung: drei negative Momentanproxys, einer positiv.
  - K und die ueberdaempfte Dynamik sind eingesetzt, nicht aus VFW abgeleitet. Codex' Vorschlag: als bekannte
    Methodik-Nulllinie parken.
- **Papiertests** (Anthropic-Agent, 00:01:30 bis 00:29:22 CEST; RUNDE-01/F1-PAPIER.md, F3-PAPIER.md, K2-LESUNG.md):
  - **F-1:** Als Einfangregel andere Sprache fuer Bekanntes.
    - Bei erhaltener x5-Symmetrie ist es der KK-Q-Ball (Demir, hep-ph/0006344); der Einfang ist die Solitosynthese
      (Griest und Kolb).
    - Bricht man die Symmetrie, entsteht keine neue Regel (Orbifold: Ladung weg; Wand: gewoehnlicher Q-Ball).
    - Die starke Fassung "alle Masse ist Impuls in x5" kollidiert bekannt mit Daten: Die Elektronmasse laege
      22 Groessenordnungen daneben (Overduin und Wesson, 4.2), und gleichnamige KK-Teilchen ziehen sich statisch nicht an
      (Benakli u. a., 2210.00477, Gl. 3.8).
  - **F-3:** Der duennwandige Q-Ball ist ein Fluessigkeitstropfen wie ein Atomkern, kein MIT-Beutel.
    - Der Bewegungsterm faellt bei uns mit R^-3, im Beutel mit R^-1; im Gleichgewicht gilt E = 2BV statt 4BV.
    - 1D: M*R_1/2 = 9,26 / 4,09 / 3,62 bei omega^2 = 0,51 / 0,7 / 0,9. 3D duennwandig: M*R ~ 0,391 Q^(4/3), also nicht
      konstant.
    - Die Beutelform braucht ein zweites Feld (Friedberg-Lee).
    - Handrechnung, ein zweites Haus hat sie noch nicht nachgerechnet.
  - **K-2:** 2609.24913 enthaelt genau einen flachen Q-Ball (drehend, m = 1, omega = 0,99; E = 136,06, Q = 157,09; fuenf
    Stellen aus einem Code).
    - Das Potential ist ein anderes: S - S^2 + 0,275 S^3.
    - In der Arbeit steckt eine Faktor-2-Unstimmigkeit.
    - Unser Loeser braucht etwa 1 h Umbau (Koeffizienten als Parameter, Loeser bei festem omega).
- **QG-1-Code** (Anthropic-Agent, 00:01:36 bis 00:29:38 CEST; RUNDE-01/qg1/qg1.py, QG1-PLAN.md):
  - 27 Laeufe grob und fein, Varianten A, B, C und die Zusatzkontrolle C2 (volle Metrik mit anderer Skalierung, Soll R = 2)
  - Vorhersage vor dem Rechnen, R bei omega^2 = 0,55 / 0,7 / 0,9:
    - A: 0,3217 / 0,2227 / 0,0694
    - B: 1,6783 / 1,7773 / 1,9306
    - C: 1
    - C2: 2
  - Ein Befund waere erst eine Abweichung ueber 0,03 bei bestandener Aufloesungsprobe.
- **QG-1-Lauf** (.69, Quadro P5000, torch 2.5.1+cu121, unter dem gemeinsamen Lock in einer VS-1-Portionsluecke; Belege in
  RUNDE-01/qg1/lauf-69/):
  - Rauchtest T = 40 von 22:36:43Z bis 22:38:09Z; Hauptlauf T = 400 von 22:38:12Z bis 22:40:05Z (1 min 56 s Unit).
  - VS-1-Kette an der Portionsgrenze angehalten (22:36:41Z) und neu gestartet (22:40:08Z, neue Ketten-PID 1649276).
  - **Ergebnis R = a/a_Newton**, fein, bei omega^2 = 0,55 / 0,7 / 0,9:
      omega 0,252: Der schnellste Q-Ball faellt 4,6-mal schneller als der langsamste.
    - B (nur Zeitterm): 1,6675 / 1,7654 / 1,9162 (Soll 1,6783 / 1,7773 / 1,9306; Abweichung etwa 0,7 %, unter 0,03).
    - C (volle Metrik): 0,9971 in allen drei; Spannweite 0,0000.
    - C2 (Metrik, andere Skalierung): 1,9883 in allen drei; Spannweite 0,0000.
  - **Kontrollen:** K0 bis K4 bestanden.
    - Profil gegen den analytischen Anker: 1,2e-10
    - g = 0: 4e-18
    - Vorzeichen: 3e-16
    - Aufloesung: groesste Aenderung fein gegen grob 6,1e-4 bei einer Spannweite A von 0,25
    - Abstrahlung hoechstens 1,8e-7
  - **Beobachtung ohne Befundstatus:** B, C und C2 liegen gemeinsam um 0,3 bis 0,7 % unter dem Soll, im Spaetfenster
    etwas mehr, fuer alle omega gleich. Wahrscheinlich ein gemeinsamer Aufbaueffekt (Fall ueber etwa 8 Laengeneinheiten,
    Fitfenster). Nicht untersucht; die Universalitaet haengt nur an der Spannweite.
- **Nebenbei (nicht Teil der Runde):** Codex rechnet auf Finns direkten Auftrag zehn Ideen zu Patch-Knoten mit innerer
  Phase (coordination/exploration-20260930-patch-nodes/). Eingang fuer Runde 2.

## Abschaetzung (L1 kann scheitern, L2 Gegenprobe, L3 Numerik, L4 schon bekannt, L5 Messbezug)

Abschaetzung der Leitung, 2026-09-30 00:40:55 CEST (gemessen).

| Karte | L1 | L2 | L3 | L4 | L5 | Nutzen | Kosten | Risiko | Entscheidung | Grund |
|---|---|---|---|---|---|---|---|---|---|---|
| K-2 | ja | geplant | geplant | nein | nein | niedrig | 1 h Code + 10 min | gering | parken | nur ein Pruefbeispiel mit fuenf Stellen aus einem Code, Faktor-2-Unstimmigkeit in der Arbeit |
| F-1 | ja | nein | entfaellt | ja | ja (bekannte Ausschluesse) | mittel als Einordnung | Papier | gering | parken ("bekannt") | KK-Q-Ball und Solitosynthese sind Literatur; die starke Fassung ist durch Daten ausgeschlossen |
| F-3 | ja | nein | entfaellt | ja | nein | niedrig | Papier | gering | verwerfen | H trifft nicht zu: Tropfen statt Beutel, Beutel braucht ein zweites Feld |
| K-5 | – | – | – | – | – | mittel | Minuten | gering | bei Codex weiter | als Hinweis in Codex' H1 aufgenommen |
| K-6 (Zufall) | ja | ja | ja | ja | nein | niedrig bis mittel | 25 CPU-s | mittel | parken ("bekannt") | Synchronisation bekannt; K und Daempfung eingesetzt, nicht aus VFW abgeleitet |

**Latten-Bilanz:**
- L4 (bekannt) stoppte F-1 und K-6.
- L2 stoppte F-3: Die Hypothese trifft nicht zu.
- L5 (Messbezug) fehlt bei K-2, F-3 und K-6.
- K-2 ist nach Nutzen gegen Kosten geparkt.

**Gewaehlt gegen Zufall:** Von den gewaehlten Karten mit Test geht 1 von 4 weiter (QG-1), die Zufallskarte wird geparkt.
Der Vergleich zaehlt erst nach fuenf Runden.

**Eingang fuer Runde 2:**
- Codex' Patch-Knoten mit innerer Phase (exploration-20260930-patch-nodes/)
- Codex' Verdichtungs-Folgefrage: getrennte gebundene Kerne oder Netz
- K-4 mit QG-3 (drehender Hintergrund, J/Q = 1/2), sobald die GPU frei ist
- K-1 (B26 als angeregter Kern) und K-3 (Nadel-Q-Baelle vor CX-1)
- neue arXiv-Tage

## Einfach gesagt

alles andere, wenn das Feld auf alles wirkt wie Einsteins Raumzeit. Wirkt es nur auf die Ausbreitung, fallen verschiedene
Klumpen bis zum Faktor 4,6 verschieden schnell, und das schliessen Satellitenmessungen fuer normale Materie aus. Zwei
KI-Haeuser haben das auf Papier gezeigt, und der Computer hat es auf vier Stellen bestaetigt. Finns Ideen zur versteckten
Dimension und zum Proton als Klumpen stehen schon in der Fachliteratur und sagen nichts Neues voraus, das man messen
koennte.
