# ERGEBNIS WOLFRAM-KEV-SCAN (Runde 37, .69-Ordner runde41-wolfram-kev)

Code-Agent wolfram-kev-scan, Leitung claude-primary. Zeiten per date (CEST; .69-Logs in UTC = CEST minus 2 h). Plan und Code
eingefroren 2026-10-04 14:57:06 (EINGEFROREN-SHA256.txt); Hauptlaeufe 14:57:14 bis 15:05:48; Auswertung 15:11:41 (eingefrorener
Code, lauf-69/auswertung.json, Pruefsummen lauf-69/PRUEFSUMMEN.txt). Bericht geschrieben ab 15:15:19.

## Ergebnis zuerst

1. **Kev laeuft und hat alles bewertet (WK0 erfuellt):** 548 von 548 Abschnitten (aus 414 Seiten, 496 abgerufene HTML-Seiten),
   keine NaN, zwei parallele Laeufe auf p4000a/p4000b mit 495 s bzw. 472 s (je unter 600 s), Median 1,16 s je Abschnitt.
2. **Blinde Gegenprobe: Kev ist fuer die Schichtzuordnung nicht besser als grep, eher schlechter (WK1 und WK2 nicht erfuellt).**
   Treffer unter den Top 10 von 25 im Mittel 3,5 (Kev) gegen 4,0 (Stichwortsuche); S1 2 von 3 gegen 3 von 3, S4 0 von 1 gegen
   1 von 1, S0 und S2 gleich; AUC Kev 0,58 bis 0,83, Stichwort 0,84 bis 1,00. Die Stichprobe hat fuer S1/S2/S4 nur 3/2/1 relevante
   Abschnitte und fuer S3 keinen, das Urteil ist also schwach, aber in jeder Schicht gleich gerichtet.
3. **Warum (nachtraegliche Diagnose, nicht vorab festgelegt):** Kevs fuenf Schichtwerte messen fast dasselbe ("wie
   gehaltvoll/technisch wirkt der Abschnitt"): Korrelation zwischen den Schichten 0,63 bis 0,91 ueber alle 548 Abschnitte; in
   den Listen S1 bis S4 stehen 4.8 "Homogeneity" und 4.9 "Adjacency Matrices" jeweils auf Platz 1 und 2, dazu je dreimal 4.6
   "Dimension-Related Characterizations" und 3.7 "22->32-Regeln" unter den ersten vier, keiner davon handelt von Teilchen,
   Wechselwirkung oder Schwerkraft. Kev-Top-15 und Stichwort-Top-15 ueberlappen je Schicht in 0 bis 1 Abschnitten. 8.9 "Elementary Particles" steht
   in Kevs S2-Liste erst auf Rang 66, aber in der S4-Liste (Schwerkraft) auf Rang 4; 4.7 "Curvature" auf S4-Rang 161.
4. **Was Kev doch leistet:** die Ja/Nein-Frage "Bezug zu Kausalgraphen/Kausalmengen" (Ue3) trennt in der Gegenprobe perfekt
   (AUC 1,00; Stichwort 0,96) und stimmt ueber alle Abschnitte mit der Stichwortsuche ueberein (Spearman 0,75); ihre Top 15 sind eine
   brauchbare Ue3-Leseliste (u. a. Q&A "How do your models relate to causal set theory and causal dynamical triangulation?",
   6.5, 6.7, 5.14). Als Seitenfilter liefert Kev grob "Kapitel 8 der Technical Introduction" (17 der 30 Leselisten-Seiten), also
   das, was auch das Inhaltsverzeichnis sagt.
5. **Wichtigste Luecke fuer "nichts uebersehen":** die Bulletins auf bulletins.wolframphysics.org (u. a. "Event Horizons,
   Singularities and Other Exotic Spacetime Phenomena", "Confluence and Causal Invariance") wurden nicht abgerufen
   (Host-Grenze www, 600er-Grenze erreicht). Sie sind fuer S4 und Ue3 vermutlich wichtiger als jede Kev-Sortierung und gehoeren
   von Hand gelesen (Liste unten).

## Abdeckung

- Abruf 14:23:55 bis 14:43:43 (code/crawl.sh; robots.txt: alles erlaubt; nacheinander, 1,2 s Pause, User-Agent
  "fmhc-physics-research-scan (contact: project lead)"): 600 Abrufe, davon 496 HTML-Seiten ok; 55 RSS-Feeds (Sitemap-Eintraege
  .../feed/, sofort verworfen), 43 x 404, 4 x 301 auf bulletins.wolframphysics.org (nicht verfolgt), 1 x writings.stephenwolfram.com
  (fremder Host), 1 Abbruch. Index mit URL, Zeit, Groesse, sha256: seiten/INDEX.tsv (Rohdaten seiten/0001.html ...).
- Aufbereitung (code/aufbereiten.py auf der .69): 54 Seiten waren Dubletten (gleiche Datei unter URL ohne Schraegstrich),
  4 Abschnitte Textdubletten; uebrig 548 Abschnitte aus 414 Seiten, 145 932 Woerter (Median 269 Woerter, 329 Abschnitte unter 300,
  219 zwischen 300 und 600, keiner darueber). Bereiche: Register (universes) 224, technical-introduction 206, questions 71,
  livestreams 12, archives 11, technical-documents 9, glossary 8, sonstige 7.
- Kev (kev-0.8b, fp16 auf Quadro P4000, Einbettung auf der CPU): Lauf A1 p4000a 274 Abschnitte in 495 s, Lauf B1 p4000b 274 in
  472 s (Import und Laden je ~100 s, Aufwaermen ~19 s); reine Rechenzeit 770 s, Median 1,16 s, p90 2,17 s, Hoechstwert 5,8 s je
  Abschnitt; GPU-Spitze 2,7 bzw. 3,1 GiB; 0 NaN; keine doppelten oder fehlenden IDs. Rauchlaeufe: rauch-69/ (Rauch 0 gescheitert,
  Rauch 1 synthetisch, Rauch 2 neun echte Abschnitte).

### Was fehlt

- **Bulletins** (bulletins.wolframphysics.org), gefunden, aber nicht gelesen (9 Links): 2020/05 event-horizons-singularities-
  and-other-exotic-spacetime-phenomena (S4), 2020/06 exploring-rulial-space-the-case-of-turing-machines, 2020/08 a-candidate-
  geometrical-formalism-for-the-foundations-of-mathematics-and-physics, 2020/08 a-short-note-on-the-double-slit-experiment-and-
  other-quantum-interference-effects-in-the-wolfram-model, 2020/10 local-multiway-systems-a-new-approach-to-wolfram-model-
  evolution, 2020/11 confluence-and-causal-invariance (Ue3), 2021/02 multiway-turing-machines, 2021/10 multicomputation-with-
  numbers-the-case-of-simple-multiway-systems, 2022/06 multicomputational-irreducibility. Der Hub www.wolframphysics.org/bulletins
  leitet auf writings.stephenwolfram.com/category/physics/ um (ausserhalb des Auftrags).
- **Register-Einzelseiten:** 75 von 898 (die 61 Registerlisten mit allen Signaturen sind vollstaendig dabei).
- **Technical Documents:** nur die Uebersichtsseite; die Aufsaetze (Gorard u. a. zu Relativitaet und QM) sind PDFs bzw. externe
  Links und waren ausgeschlossen. Das Gesamt-PDF der Technical Introduction fehlt ebenfalls, ihr Text steht aber vollstaendig in
  den HTML-Abschnitten (Kapitel 1 bis 10).
- **visual-gallery:** nur die Startseite (Rest sind Bild- und PDF-Downloadseiten).

## Gegenprobe (blind) und Urteile

Stichprobe 25 Abschnitte (Seed 20261004, daten/gegenprobe-ids.txt), von Hand eingestuft und gespeichert 14:47:47
(gegenprobe-hand.json, sha256 b05aae2f...), bevor irgendein Kev-Wert fuer einen Seitenabschnitt vorlag. Treffer@10 = erwartete Zahl
Hand-relevanter unter den 10 Hoechstbewerteten (Gleichstaende zufaellig aufgeloest); Zufall = 10*k/25.

| Schicht | k relevant | Kev Treffer@10 | Stichwort Treffer@10 | Zufall | Spearman Kev / Stichwort | AUC Kev / Stichwort | WK1-Forderung | WK1 |
|---|---|---|---|---|---|---|---|---|
| S0 Buehne | 20 | 10,0 | 10,0 | 8,0 | 0,40 / 0,47 | 0,79 / 0,84 | >= 6 | ja |
| S1 Ausbreitung | 3 | 2,0 | 3,0 | 1,2 | 0,21 / 0,56 | 0,68 / 0,97 | >= 3 | **nein** |
| S2 Teilchen | 2 | 2,0 | 2,0 | 0,8 | 0,31 / 0,74 | 0,83 / 1,00 | >= 2 | ja |
| S3 Wechselwirkung | 0 | - | - | - | - | - | entfaellt | - |
| S4 Schwerkraft | 1 | 0,0 | 1,0 | 0,4 | 0,06 / 0,44 | 0,58 / 0,92 | >= 1 | **nein** |
| kausal (Ue3, nicht urteilsrelevant) | 12 | 10,0 | 10,0 | 4,8 | 0,87 / 0,88 | **1,00** / 0,96 | - | - |

- **WK0 (65 %): erfuellt.** Alle 548 Abschnitte bewertet, keine NaN, beide Laeufe innerhalb ihrer Einheit (495 s, 472 s).
- **WK1 (45 %): nicht erfuellt.** S1 (2 statt 3) und S4 (0 statt 1) verfehlen die Forderung min(6, k).
- **WK2 (40 %): nicht erfuellt.** Mittel ueber S0, S1, S2, S4: Kev 3,5, Stichwortsuche 4,0.
- Einschraenkung: k = 3, 2, 1 fuer S1, S2, S4 und k = 0 fuer S3; ein einziger Abschnitt entscheidet dort. Die Richtung ist aber in
  allen Kennzahlen gleich (Spearman und AUC der Stichwortsuche in jeder Schicht hoeher), und der Ganzbestand zeigt dasselbe
  (Punkt 3 oben).
- Ganzbestand (nicht urteilsrelevant, Plan Abschnitt 9): Ueberlappung Kev-Top-15 mit Stichwort-Top-15 S0 0, S1 0, S2 1, S3 0, S4 1,
  kausal 5; Spearman Kev gegen Stichworttreffer ueber alle 548: S0 0,24, S1 0,08, S2 0,08, S3 0,14, S4 0,05, kausal 0,75.
- Verteilungen der Kev-Werte (0 bis 10): Mittel S0 6,96, S1 5,77, S2 5,34, S3 5,97, S4 6,13 bei Streuung 1,1 bis 1,5; nichts liegt
  unter 2,07. Das synthetische Schuhticket aus Rauch 1 bekam S0 5,82 und S3 5,39: Absolutwerte sind bedeutungslos, nur Raenge zaehlen.
- Nachtraegliche Diagnose (nach dem Lauf gerechnet, mit jq aus lauf-69/kev-*.jsonl; aendert kein Urteil): Pearson zwischen Kevs
  Schichtwerten ueber 548 Abschnitte S0-S1 0,70, S1-S2 0,82, S2-S3 0,91, S2-S4 0,77, S3-S4 0,75, S1-S4 0,84, S0-S4 0,63; S4 gegen
  kausal -0,12. Rangplaetze von Schluesselabschnitten in Kevs Schichtlisten (von 548): 8.6 Motion and Special Relativity S1 19;
  8.9 Elementary Particles S2 66 und 111 (aber S4 4 und 21); 8.7 Vacuum Einstein Equations S4 19 und 53; 4.7 Curvature S4 161;
  4.15 Geodesics S4 137 und 139; 8.8 Matter, Energy and Gravitation S4 26 bis 360; 8.19 Local Gauge Invariance S2 11 und 57.

## Top 15 je Schicht (Kev, eingefrorene Regel)

Lesehinweis: Wegen der Schicht-Korrelation sind die Listen S1 bis S4 weitgehend dieselbe Liste "gehaltvolle Abschnitte aus
Kapitel 4 und 8"; die Stichwort-Top-15 (lauf-69/auswertung.json, Feld top15_stichwort) treffen die Schichten besser (S1: 8.6 Motion
and Special Relativity vorn; S2: 8.9 Elementary Particles; S4: 4.15 Geodesics, 4.7 Curvature, 8.8 Matter, Energy and Gravitation).
Die kausal-Liste ist die verlaesslichste Kev-Liste. Werte: Kev-Score der Schicht bzw. p(ja) fuer kausal; konkret = p(ja) fuer
"nachrechenbare Aussage"; Art = wahrscheinlichste Antwort der choice-Frage.

### Top 15 S0

| # | Kev S0 | konkret | Art | Seite | Ueberschrift | Auszug |
|---|---|---|---|---|---|---|
| 1 | 9.3 | 0.34 | claim | /technical-introduction/limiting-behavior-and-emergent-geometry/homogeneity-and-local-graph-neighborhoods/ | 4.8 Homogeneity and Local Graph Neighborhoods | In studying Vr we are looking at the total size of the neighborhood up to distance r around a point in a graph. But what about the actual lo |
| 2 | 9.28 | 0.65 | claim | /technical-introduction/potential-relation-to-physics/wave-particle-duality-uncertainty-relations-etc/ | 8.16 Wave-Particle Duality, Uncertainty Relations, Etc. | Wave-particle duality was an early but important concept in standard quantum mechanics, and turns out to be a core feature of our models, in |
| 3 | 9.27 | 0.69 | computation | /technical-introduction/limiting-behavior-and-emergent-geometry/adjacency-matrices-and-age-distributions/ | 4.9 Adjacency Matrices and Age Distributions | We have made explicit visualizations of the connectivity structures of the graphs (and hypergraphs) generated by our models. But an alternat |
| 4 | 9.27 | 0.22 | derivation | /technical-introduction/potential-relation-to-physics/local-gauge-invariance/ | 8.19 Local Gauge Invariance | An important phenomenon discussed especially in the context of quantum field theories is local gauge invariance (e.g. [134]). In our models  |
| 5 | 9.11 | 0.39 | derivation | /technical-introduction/potential-relation-to-physics/units-and-scales/ | 8.20 Units and Scales | To go further, however, we must estimate Ξ. Ultimately, Ξ is determined by the actual evolution of the multiway system for a particular rule |
| 6 | 9.09 | 0.64 | other | /technical-introduction/typical-behaviors/rules-depending-on-two-ternary-relations-the-23-33-case/ | 3.10 Rules Depending on Two Ternary Relations: the 2333 Cas | There are 79,359,764 inequivalent left-connected 23  33 rules. The fraction of these rules showing continued growth is considerably smaller |
| 7 | 9.03 | 0.36 | claim | /technical-introduction/potential-relation-to-physics/event-horizons-and-singularities-in-spacetime-and-quantum-mechanics/ | 8.18 Event Horizons and Singularities in Spacetime and Quant | A different situation can occur when there is also disconnection in the causal graph—leading in our models to disconnection in the spatial h |
| 8 | 9.02 | 0.88 | computation | /technical-introduction/limiting-behavior-and-emergent-geometry/the-notion-of-dimension/ | 4.5 The Notion of Dimension | As we run the rule, the structure it produces gets larger, so it becomes easier to estimate the growth rate of Vr. The picture below shows Δ |
| 9 | 9.0 | 0.55 | other | /technical-introduction/limiting-behavior-and-emergent-geometry/the-notion-of-dimension/ | 4.5 The Notion of Dimension | Estimating dimension from Vr(X) averaged over all points we get (for graphs made from 6 and 7 recursive subdivisions): The dotted line indic |
| 10 | 8.99 | 0.17 | other | /technical-introduction/ | A Class of Models with the Potential to Represent Fundamenta | by stephen wolfram A class of models intended to be as minimal and structureless as possible is introduced. The models can be viewed as desc |
| 11 | 8.93 | 0.36 | other | /livestreams/ | Video Work Logs | with Stephen Wolfram ✕ close BlackHoles-02.nb BlackHoles-05.nb BlackHoles-06.nb May 08, 2020» with Stephen Wolfram & Jonathan Gorard ✕ close |
| 12 | 8.93 | 0.21 | claim | /technical-introduction/potential-relation-to-physics/quantum-measurement/ | 8.14 Quantum Measurement | But there is a problem here. Because in effect we are asking the observer to “outcompute” the system itself. Yet we can expect that the evol |
| 13 | 8.92 | 0.53 | other | /livestreams/ | Pre-Launch Working Meetings | Working Session: Rule Enumeration & Bell Ringing (Dec. 23, 2019) » with Stephen Wolfram ✕ close RuleEnumeration-43.nb BellRinging-01.nb Work |
| 14 | 8.89 | 0.07 | claim | /technical-introduction/potential-relation-to-physics/multiway-systems-in-the-space-of-all-possible-rules/ | 8.22 Multiway Systems in the Space of All Possible Rules | But now remember that the observer is also embedded in the same system, so the fundamental rate at which it can do computation is defined by |
| 15 | 8.88 | 0.42 | other | /technical-introduction/limiting-behavior-and-emergent-geometry/the-notion-of-dimension/ | 4.5 The Notion of Dimension | There are, however, many subtle issues. The first—immediately evident in practice—is that if our graph is finite (like the grids above) then |

### Top 15 S1

| # | Kev S1 | konkret | Art | Seite | Ueberschrift | Auszug |
|---|---|---|---|---|---|---|
| 1 | 9.48 | 0.34 | claim | /technical-introduction/limiting-behavior-and-emergent-geometry/homogeneity-and-local-graph-neighborhoods/ | 4.8 Homogeneity and Local Graph Neighborhoods | In studying Vr we are looking at the total size of the neighborhood up to distance r around a point in a graph. But what about the actual lo |
| 2 | 9.18 | 0.69 | computation | /technical-introduction/limiting-behavior-and-emergent-geometry/adjacency-matrices-and-age-distributions/ | 4.9 Adjacency Matrices and Age Distributions | We have made explicit visualizations of the connectivity structures of the graphs (and hypergraphs) generated by our models. But an alternat |
| 3 | 9.1 | 0.52 | claim | /technical-introduction/potential-relation-to-physics/the-structure-of-space/ | 8.4 The Structure of Space | This plots the effective “dimension exponent” of r in Vr as a function of r, averaged over all nodes in the hypergraph, for a succession of  |
| 4 | 8.92 | 0.87 | claim | /technical-introduction/limiting-behavior-and-emergent-geometry/dimension-related-characterizations/ | 4.6 Dimension-Related Characterizations | Having seen how our notion of dimension works in cases where we can readily recognize emergent geometry, we now turn to using it to study th |
| 5 | 8.88 | 0.17 | other | /technical-introduction/ | A Class of Models with the Potential to Represent Fundamenta | by stephen wolfram A class of models intended to be as minimal and structureless as possible is introduced. The models can be viewed as desc |
| 6 | 8.83 | 0.22 | derivation | /technical-introduction/potential-relation-to-physics/local-gauge-invariance/ | 8.19 Local Gauge Invariance | An important phenomenon discussed especially in the context of quantum field theories is local gauge invariance (e.g. [134]). In our models  |
| 7 | 8.81 | 0.81 | derivation | /technical-introduction/the-updating-process-for-string-substitution-systems/the-concept-of-branchial-graphs/ | 5.15 The Concept of Branchial Graphs | The particular rule shown here has the property that it is causal invariant, but also that all branch pairs resolve in just one step. And fr |
| 8 | 8.79 | 0.65 | claim | /technical-introduction/potential-relation-to-physics/wave-particle-duality-uncertainty-relations-etc/ | 8.16 Wave-Particle Duality, Uncertainty Relations, Etc. | Wave-particle duality was an early but important concept in standard quantum mechanics, and turns out to be a core feature of our models, in |
| 9 | 8.72 | 0.71 | derivation | /technical-introduction/potential-relation-to-physics/wave-particle-duality-uncertainty-relations-etc/ | 8.16 Wave-Particle Duality, Uncertainty Relations, Etc. | But now recall that we identified momentum as corresponding to the flux of causal edges across timelike hypersurfaces. So to do our momentum |
| 10 | 8.71 | 0.21 | claim | /technical-introduction/potential-relation-to-physics/quantum-measurement/ | 8.14 Quantum Measurement | But there is a problem here. Because in effect we are asking the observer to “outcompute” the system itself. Yet we can expect that the evol |
| 11 | 8.68 | 0.42 | other | /technical-introduction/limiting-behavior-and-emergent-geometry/the-notion-of-dimension/ | 4.5 The Notion of Dimension | There are, however, many subtle issues. The first—immediately evident in practice—is that if our graph is finite (like the grids above) then |
| 12 | 8.58 | 0.33 | claim | /technical-introduction/equivalence-and-computation-in-our-models/computational-capabilities-of-our-models/ | 7.3 Computational Capabilities of Our Models | An important way to characterize our models is in terms of their computational capabilities. We can always think of the evolution of one of  |
| 13 | 8.57 | 0.36 | claim | /technical-introduction/potential-relation-to-physics/event-horizons-and-singularities-in-spacetime-and-quantum-mechanics/ | 8.18 Event Horizons and Singularities in Spacetime and Quant | A different situation can occur when there is also disconnection in the causal graph—leading in our models to disconnection in the spatial h |
| 14 | 8.55 | 0.32 | claim | /technical-introduction/potential-relation-to-physics/event-horizons-and-singularities-in-spacetime-and-quantum-mechanics/ | 8.18 Event Horizons and Singularities in Spacetime and Quant | Having discussed the general correspondence between relativity and quantum mechanics suggested by our models, we can now consider the extrem |
| 15 | 8.55 | 0.2 | other | /technical-introduction/potential-relation-to-physics/basic-concepts-of-quantum-mechanics/ | 8.12 Basic Concepts of Quantum Mechanics | Quantum mechanics is a key known feature of physics, and also, it seems, a natural and inevitable feature of our models. In classical physic |

### Top 15 S2

| # | Kev S2 | konkret | Art | Seite | Ueberschrift | Auszug |
|---|---|---|---|---|---|---|
| 1 | 9.6 | 0.69 | computation | /technical-introduction/limiting-behavior-and-emergent-geometry/adjacency-matrices-and-age-distributions/ | 4.9 Adjacency Matrices and Age Distributions | We have made explicit visualizations of the connectivity structures of the graphs (and hypergraphs) generated by our models. But an alternat |
| 2 | 9.31 | 0.34 | claim | /technical-introduction/limiting-behavior-and-emergent-geometry/homogeneity-and-local-graph-neighborhoods/ | 4.8 Homogeneity and Local Graph Neighborhoods | In studying Vr we are looking at the total size of the neighborhood up to distance r around a point in a graph. But what about the actual lo |
| 3 | 9.16 | 0.87 | claim | /technical-introduction/limiting-behavior-and-emergent-geometry/dimension-related-characterizations/ | 4.6 Dimension-Related Characterizations | Having seen how our notion of dimension works in cases where we can readily recognize emergent geometry, we now turn to using it to study th |
| 4 | 9.13 | 0.05 | other | /technical-introduction/typical-behaviors/rules-depending-on-more-than-one-relation-the-22-32-case/ | 3.7 Rules Depending on More Than One Relation: The 2232 Cas | The smallest nontrivial signature that can lead to growth (and therefore unbounded evolution) is 22  32. There are 4702 distinct left-conne |
| 5 | 8.93 | 0.14 | claim | /technical-introduction/potential-relation-to-physics/correspondence-between-relativity-and-quantum-mechanics/ | 8.17 Correspondence between Relativity and Quantum Mechanics | One of the surprising consequences of the potential application of our models to physics is their implications around deep relationships bet |
| 6 | 8.92 | 0.04 | outlook | /technical-introduction/potential-relation-to-physics/cosmology-expansion-and-singularities/ | 8.11 Cosmology, Expansion & Singularities | An obvious question is whether any traces of the initial conditions might persist, perhaps even through the whole evolution of the system. T |
| 7 | 8.86 | 0.27 | other | /technical-introduction/potential-relation-to-physics/units-and-scales/ | 8.20 Units and Scales | Most of our discussion so far has focused on how the structure of our models might correspond to the structure of our physical universe. But |
| 8 | 8.74 | 0.39 | derivation | /technical-introduction/potential-relation-to-physics/units-and-scales/ | 8.20 Units and Scales | To go further, however, we must estimate Ξ. Ultimately, Ξ is determined by the actual evolution of the multiway system for a particular rule |
| 9 | 8.7 | 0.21 | claim | /technical-introduction/potential-relation-to-physics/quantum-measurement/ | 8.14 Quantum Measurement | But there is a problem here. Because in effect we are asking the observer to “outcompute” the system itself. Yet we can expect that the evol |
| 10 | 8.65 | 0.85 | claim | /questions/relations-to-other-approaches/what-do-your-models-imply-regarding-the-black-hole-information-paradox/ | What do your models imply regarding the black hole informati | March 13, 2020 Answered by: Jonathan Gorard The maximum rate of quantum entanglement (i.e. the natural propagation velocity of geodesics in  |
| 11 | 8.63 | 0.22 | derivation | /technical-introduction/potential-relation-to-physics/local-gauge-invariance/ | 8.19 Local Gauge Invariance | An important phenomenon discussed especially in the context of quantum field theories is local gauge invariance (e.g. [134]). In our models  |
| 12 | 8.62 | 0.36 | claim | /technical-introduction/potential-relation-to-physics/event-horizons-and-singularities-in-spacetime-and-quantum-mechanics/ | 8.18 Event Horizons and Singularities in Spacetime and Quant | A different situation can occur when there is also disconnection in the causal graph—leading in our models to disconnection in the spatial h |
| 13 | 8.52 | 0.71 | derivation | /technical-introduction/potential-relation-to-physics/wave-particle-duality-uncertainty-relations-etc/ | 8.16 Wave-Particle Duality, Uncertainty Relations, Etc. | But now recall that we identified momentum as corresponding to the flux of causal edges across timelike hypersurfaces. So to do our momentum |
| 14 | 8.49 | 0.52 | claim | /technical-introduction/potential-relation-to-physics/the-structure-of-space/ | 8.4 The Structure of Space | This plots the effective “dimension exponent” of r in Vr as a function of r, averaged over all nodes in the hypergraph, for a succession of  |
| 15 | 8.45 | 0.04 | outlook | /technical-introduction/potential-relation-to-physics/quantum-measurement/ | 8.14 Quantum Measurement | In freezing time in something like the foliation in the picture above what we are effectively doing is creating a coordinate singularity in  |

### Top 15 S3

| # | Kev S3 | konkret | Art | Seite | Ueberschrift | Auszug |
|---|---|---|---|---|---|---|
| 1 | 9.71 | 0.69 | computation | /technical-introduction/limiting-behavior-and-emergent-geometry/adjacency-matrices-and-age-distributions/ | 4.9 Adjacency Matrices and Age Distributions | We have made explicit visualizations of the connectivity structures of the graphs (and hypergraphs) generated by our models. But an alternat |
| 2 | 9.47 | 0.34 | claim | /technical-introduction/limiting-behavior-and-emergent-geometry/homogeneity-and-local-graph-neighborhoods/ | 4.8 Homogeneity and Local Graph Neighborhoods | In studying Vr we are looking at the total size of the neighborhood up to distance r around a point in a graph. But what about the actual lo |
| 3 | 9.46 | 0.05 | other | /technical-introduction/typical-behaviors/rules-depending-on-more-than-one-relation-the-22-32-case/ | 3.7 Rules Depending on More Than One Relation: The 2232 Cas | The smallest nontrivial signature that can lead to growth (and therefore unbounded evolution) is 22  32. There are 4702 distinct left-conne |
| 4 | 9.38 | 0.87 | claim | /technical-introduction/limiting-behavior-and-emergent-geometry/dimension-related-characterizations/ | 4.6 Dimension-Related Characterizations | Having seen how our notion of dimension works in cases where we can readily recognize emergent geometry, we now turn to using it to study th |
| 5 | 9.17 | 0.22 | derivation | /technical-introduction/potential-relation-to-physics/local-gauge-invariance/ | 8.19 Local Gauge Invariance | An important phenomenon discussed especially in the context of quantum field theories is local gauge invariance (e.g. [134]). In our models  |
| 6 | 9.05 | 0.52 | claim | /technical-introduction/potential-relation-to-physics/the-structure-of-space/ | 8.4 The Structure of Space | This plots the effective “dimension exponent” of r in Vr as a function of r, averaged over all nodes in the hypergraph, for a succession of  |
| 7 | 9.0 | 0.39 | derivation | /technical-introduction/potential-relation-to-physics/units-and-scales/ | 8.20 Units and Scales | To go further, however, we must estimate Ξ. Ultimately, Ξ is determined by the actual evolution of the multiway system for a particular rule |
| 8 | 9.0 | 0.36 | claim | /technical-introduction/potential-relation-to-physics/event-horizons-and-singularities-in-spacetime-and-quantum-mechanics/ | 8.18 Event Horizons and Singularities in Spacetime and Quant | A different situation can occur when there is also disconnection in the causal graph—leading in our models to disconnection in the spatial h |
| 9 | 8.97 | 0.62 | claim | /technical-introduction/the-updating-process-for-string-substitution-systems/the-concept-of-branchial-graphs/ | 5.15 The Concept of Branchial Graphs | Causal graphs provide one kind of summary of the evolution of a system, based on capturing the causal relationships between events. What we  |
| 10 | 8.97 | 0.27 | other | /technical-introduction/potential-relation-to-physics/units-and-scales/ | 8.20 Units and Scales | Most of our discussion so far has focused on how the structure of our models might correspond to the structure of our physical universe. But |
| 11 | 8.93 | 0.04 | outlook | /technical-introduction/potential-relation-to-physics/cosmology-expansion-and-singularities/ | 8.11 Cosmology, Expansion & Singularities | An obvious question is whether any traces of the initial conditions might persist, perhaps even through the whole evolution of the system. T |
| 12 | 8.92 | 0.65 | claim | /technical-introduction/potential-relation-to-physics/wave-particle-duality-uncertainty-relations-etc/ | 8.16 Wave-Particle Duality, Uncertainty Relations, Etc. | Wave-particle duality was an early but important concept in standard quantum mechanics, and turns out to be a core feature of our models, in |
| 13 | 8.91 | 0.06 | claim | /technical-introduction/potential-relation-to-physics/cosmology-expansion-and-singularities/ | 8.11 Cosmology, Expansion & Singularities | In our models the evolving hypergraph represents the whole universe, and the expansion of the universe is potentially a consequence of the g |
| 14 | 8.9 | 0.32 | claim | /technical-introduction/potential-relation-to-physics/event-horizons-and-singularities-in-spacetime-and-quantum-mechanics/ | 8.18 Event Horizons and Singularities in Spacetime and Quant | Having discussed the general correspondence between relativity and quantum mechanics suggested by our models, we can now consider the extrem |
| 15 | 8.88 | 0.21 | claim | /technical-introduction/potential-relation-to-physics/quantum-measurement/ | 8.14 Quantum Measurement | But there is a problem here. Because in effect we are asking the observer to “outcompute” the system itself. Yet we can expect that the evol |

### Top 15 S4

| # | Kev S4 | konkret | Art | Seite | Ueberschrift | Auszug |
|---|---|---|---|---|---|---|
| 1 | 9.8 | 0.69 | computation | /technical-introduction/limiting-behavior-and-emergent-geometry/adjacency-matrices-and-age-distributions/ | 4.9 Adjacency Matrices and Age Distributions | We have made explicit visualizations of the connectivity structures of the graphs (and hypergraphs) generated by our models. But an alternat |
| 2 | 9.59 | 0.34 | claim | /technical-introduction/limiting-behavior-and-emergent-geometry/homogeneity-and-local-graph-neighborhoods/ | 4.8 Homogeneity and Local Graph Neighborhoods | In studying Vr we are looking at the total size of the neighborhood up to distance r around a point in a graph. But what about the actual lo |
| 3 | 9.24 | 0.13 | claim | /technical-introduction/potential-relation-to-physics/elementary-particles/ | 8.9 Elementary Particles | Elementary particles are entities that—at least for some period—preserve their identity through space and time. In the context of our models |
| 4 | 9.24 | 0.05 | other | /technical-introduction/typical-behaviors/rules-depending-on-more-than-one-relation-the-22-32-case/ | 3.7 Rules Depending on More Than One Relation: The 2232 Cas | The smallest nontrivial signature that can lead to growth (and therefore unbounded evolution) is 22  32. There are 4702 distinct left-conne |
| 5 | 9.2 | 0.65 | claim | /technical-introduction/potential-relation-to-physics/wave-particle-duality-uncertainty-relations-etc/ | 8.16 Wave-Particle Duality, Uncertainty Relations, Etc. | Wave-particle duality was an early but important concept in standard quantum mechanics, and turns out to be a core feature of our models, in |
| 6 | 9.07 | 0.2 | other | /technical-introduction/potential-relation-to-physics/basic-concepts-of-quantum-mechanics/ | 8.12 Basic Concepts of Quantum Mechanics | Quantum mechanics is a key known feature of physics, and also, it seems, a natural and inevitable feature of our models. In classical physic |
| 7 | 9.03 | 0.21 | claim | /technical-introduction/potential-relation-to-physics/quantum-measurement/ | 8.14 Quantum Measurement | But there is a problem here. Because in effect we are asking the observer to “outcompute” the system itself. Yet we can expect that the evol |
| 8 | 8.97 | 0.71 | derivation | /technical-introduction/potential-relation-to-physics/wave-particle-duality-uncertainty-relations-etc/ | 8.16 Wave-Particle Duality, Uncertainty Relations, Etc. | But now recall that we identified momentum as corresponding to the flux of causal edges across timelike hypersurfaces. So to do our momentum |
| 9 | 8.9 | 0.57 | claim | /technical-introduction/potential-relation-to-physics/basic-concepts-of-quantum-mechanics/ | 8.12 Basic Concepts of Quantum Mechanics | But now causal invariance makes a crucial contribution. Because it implies that all such different branches must eventually converge. And in |
| 10 | 8.88 | 0.47 | claim | /technical-introduction/potential-relation-to-physics/correspondence-between-relativity-and-quantum-mechanics/ | 8.17 Correspondence between Relativity and Quantum Mechanics | In relativity there is a fairly well-developed notion of an idealized observer. The observer is typically represented by some some causal fo |
| 11 | 8.79 | 0.21 | other | /technical-introduction/potential-relation-to-physics/quantum-formalism/ | 8.13 Quantum Formalism | In effect, therefore, each branchlike hypersurface can be thought of as exposing some linear combination of basic states, each one with a ce |
| 12 | 8.73 | 0.62 | claim | /technical-introduction/the-updating-process-for-string-substitution-systems/the-concept-of-branchial-graphs/ | 5.15 The Concept of Branchial Graphs | Causal graphs provide one kind of summary of the evolution of a system, based on capturing the causal relationships between events. What we  |
| 13 | 8.71 | 0.39 | derivation | /technical-introduction/potential-relation-to-physics/units-and-scales/ | 8.20 Units and Scales | To go further, however, we must estimate Ξ. Ultimately, Ξ is determined by the actual evolution of the multiway system for a particular rule |
| 14 | 8.71 | 0.19 | claim | /technical-introduction/potential-relation-to-physics/quantum-measurement/ | 8.14 Quantum Measurement | At some point in the evolution of a string substitution system we might see a large number of different strings. But we can view them all as |
| 15 | 8.71 | 0.13 | claim | /technical-introduction/potential-relation-to-physics/reversibility-and-irreversibility/ | 8.10 Reversibility and Irreversibility | One feature of the traditional formalism for fundamental physics is that it is reversible, in the sense that it implies that individual stat |

### Top 15 kausal

| # | Kev kausal | konkret | Art | Seite | Ueberschrift | Auszug |
|---|---|---|---|---|---|---|
| 1 | 1.0 | 0.98 | claim | /questions/relations-to-other-approaches/are-your-models-consistent-with-the-holographic-principleads-cft-correspondence/ | Are your models consistent with the holographic principle/Ad | March 13, 2020 Answered by: Jonathan Gorard They certainly seem to be! Indeed, as discussed in the answer about implication for the black ho |
| 2 | 1.0 | 0.95 | other | /technical-introduction/equivalence-and-computation-in-our-models/correspondence-with-other-systems/ | 7.1 Correspondence with Other Systems | Our goal with the models introduced here is to have systems that are intrinsically as structureless as possible, and are therefore in a sens |
| 3 | 1.0 | 0.94 | claim | /technical-introduction/the-updating-process-for-string-substitution-systems/the-significance-of-causal-invariance/ | 5.9 The Significance of Causal Invariance | One might think that all rules would work like the one we just studied, and would give different causal graphs depending on what specific pa |
| 4 | 1.0 | 0.93 | derivation | /questions/relations-to-other-approaches/how-do-your-models-relate-to-causal-set-theory-and-causal-dynamical-triangulation/ | How do your models relate to causal set theory and causal dy | March 17, 2020 Answered by: Jonathan Gorard Very directly. Indeed, the causal graphs that one investigates in the context of Wolfram model s |
| 5 | 1.0 | 0.9 | derivation | /technical-introduction/potential-relation-to-physics/motion-and-special-relativity/ | 8.6 Motion and Special Relativity | In the traditional formalism of physics, the principles of special relativity are in a sense introduced as axioms, and then their consequenc |
| 6 | 1.0 | 0.84 | claim | /technical-introduction/the-updating-process-for-string-substitution-systems/causal-graphs-for-particular-updating-sequences/ | 5.8 Causal Graphs for Particular Updating Sequences | The multiway causal graph that we have just constructed shows the causal relationships for all possible paths of evolution in a multiway sys |
| 7 | 1.0 | 0.73 | claim | /technical-introduction/the-updating-process-in-our-models/causal-graphs-for-causal-invariant-rules/ | 6.5 Causal Graphs for Causal Invariant Rules | An important consequence of causal invariance is that it establishes that a rule produces the same causal graph independent of the particula |
| 8 | 1.0 | 0.66 | other | /technical-introduction/the-updating-process-for-string-substitution-systems/foliations-and-coordinates-on-causal-graphs/ | 5.14 Foliations and Coordinates on Causal Graphs | One way to describe a causal graph is to say that it defines the partial ordering of events in a system—or, in other words, it is a represen |
| 9 | 1.0 | 0.66 | derivation | /questions/main/ | How do black holes work within the context of your models? | Spacetime event horizons are characterized by the existence of localized disconnections in the causal graph; if one timelike path in the cau |
| 10 | 1.0 | 0.48 | other | /technical-introduction/the-updating-process-in-our-models/updating-events-and-causal-dependence/ | 6.1 Updating Events and Causal Dependence | Consider the rule: When we discussed this rule previously, we showed the first few steps in its evolution as: But to understand the updating |
| 11 | 1.0 | 0.3 | other | /technical-introduction/the-updating-process-for-string-substitution-systems/events-and-their-causal-relationships/ | 5.7 Events and Their Causal Relationships | So far the nodes in our graphs have always been states generated by substitution systems. But we can also introduce nodes to represent the “ |
| 12 | 1.0 | 0.28 | other | /technical-introduction/the-updating-process-in-our-models/typical-causal-graphs/ | 6.7 Typical Causal Graphs | But what is notable is that if we ask about the overall causal relationships between events, we realize that even events that happened many  |
| 13 | 1.0 | 0.15 | other | /glossary/ | The Wolfram Physics Project: Glossary | Arity: The number of elements in something, typically a hyperedge. "Binary" is "arity 2", "Ternary" is "arity 3", etc. "Binary hyperedges" a |
| 14 | 1.0 | 0.15 | other | /technical-introduction/additional-material/appendix-graph-types/ | Multiway Causal Graph | Graph representing causal connections among all possible updating events that can occur in all possible paths of evolution for the system. E |
| 15 | 0.99 | 0.89 | derivation | /questions/quantum-mechanics/how-can-your-models-be-consistent-with-bells-theorem/ | How can your models be consistent with Bell’s theorem? : The | March 7, 2020 Answered by: Jonathan Gorard Despite the deterministic nature of the Wolfram model, consistency with Bell’s theorem is actuall |


## Leseliste 30 Seiten (Kev, eingefrorene Regel)

Seitenwert = Mittel ueber S0 bis S4 des jeweils besten Abschnittswerts der Seite. 17 der 30 Seiten sind aus Kapitel 8
("Potential Relation to Physics"), 5 aus Kapitel 4. Die ersten zehn mit je einem Satz (aus den Abschnittstexten; Urteil, ob Kevs
Platz verdient ist, in Klammern):

1. 4.9 Adjacency Matrices and Age Distributions: Adjazenzmatrizen wachsender Hypergraphen, nach Entstehungsreihenfolge geordnet,
   behalten trotz Wachstum (~1,84 je Schritt) ihre Struktur (nur S0-Diagnostik; von Kev ueberbewertet).
2. 4.8 Homogeneity and Local Graph Neighborhoods: ob lokale Nachbarschaften ueberall gleich aussehen und ihre Verteilung sich
   mit der Evolution stabilisiert (S0/S1, emergenter homogener Raum; plausibel, aber nicht Platz 2).
3. 4.6 Dimension-Related Characterizations: Dimensionsschaetzung ueber V_r auch fuer Regeln ohne erkennbare Geometrie (S1
   Dimension; berechtigt).
4. 3.7 Rules Depending on More Than One Relation, the 22->32 Case: 4702 Regeln dieser Signatur und die Abhaengigkeit von der
   Aktualisierungsreihenfolge (nur S0; ueberbewertet).
5. 8.16 Wave-Particle Duality, Uncertainty Relations: Materie als Geodaetenbuendel im Multiway-Kausalgraphen, E ~ omega,
   Unschaerfe aus dem Fluss kausaler Kanten (S2 und kausal; berechtigt).
6. 8.14 Quantum Measurement: Messung als Zusammenfassen von Zweigen zu "generational states" unter Kausalinvarianz (QM, keine
   unserer fuenf Schichten).
7. 8.19 Local Gauge Invariance: Eichinvarianz aus lokalen Symmetrien der Regeln plus Kausalinvarianz im Multiway-Kausalgraphen
   (S2/S3 Eichfelder; berechtigt).
8. 8.20 Units and Scales: elementare Zeit, Laenge und Energie des Modells und ihr Abstand zu Planck-Einheiten, mit Zahlen
   (S1/S4-Skalen, konkret; berechtigt).
9. 8.4 The Structure of Space: Raum als Hypergraph-Zustand auf einer raumartigen Hyperflaeche, Abstand als kuerzester Weg,
   Dimension aus V_r ~ r^d samt Korrekturen (S0/S1, Uebergang zu S4; berechtigt).
10. 5.15 The Concept of Branchial Graphs: Branchial-Graphen als Karte der Zweige einer Multiway-Evolution (QM/kausal; fuer
    unsere Schichten Nebenstrang).

**Von Kev verfehlt oder zu weit hinten** (Stichwortlisten und eigenes Lesen): 8.9 Elementary Particles (nicht unter den 30,
S2-Rang 66), 4.7 Curvature und 4.15 Geodesics (nicht unter den 30), 8.6 Motion and Special Relativity (Platz 19), 8.7 The Vacuum
Einstein Equations (Platz 18), 8.8 Matter, Energy and Gravitation (Platz 27), die Q&A-Seite zu Kausalmengen und CDT (nur in der
kausal-Liste) und die Bulletins (nicht abgerufen).

| # | Seitenwert | staerkste | S0 | S1 | S2 | S3 | S4 | Abschn. | URL |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.512 | S4 | 9.27 | 9.18 | 9.6 | 9.71 | 9.8 | 1 | /technical-introduction/limiting-behavior-and-emergent-geometry/adjacency-matrices-and-age-distributions/ |
| 2 | 9.43 | S4 | 9.3 | 9.48 | 9.31 | 9.47 | 9.59 | 1 | /technical-introduction/limiting-behavior-and-emergent-geometry/homogeneity-and-local-graph-neighborhoods/ |
| 3 | 8.99 | S3 | 8.8 | 8.92 | 9.16 | 9.38 | 8.69 | 1 | /technical-introduction/limiting-behavior-and-emergent-geometry/dimension-related-characterizations/ |
| 4 | 8.976 | S3 | 8.65 | 8.4 | 9.13 | 9.46 | 9.24 | 1 | /technical-introduction/typical-behaviors/rules-depending-on-more-than-one-relation-the-22-32-case/ |
| 5 | 8.942 | S0 | 9.28 | 8.79 | 8.52 | 8.92 | 9.2 | 2 | /technical-introduction/potential-relation-to-physics/wave-particle-duality-uncertainty-relations-etc/ |
| 6 | 8.85 | S4 | 8.93 | 8.71 | 8.7 | 8.88 | 9.03 | 5 | /technical-introduction/potential-relation-to-physics/quantum-measurement/ |
| 7 | 8.822 | S0 | 9.27 | 8.83 | 8.63 | 9.17 | 8.21 | 2 | /technical-introduction/potential-relation-to-physics/local-gauge-invariance/ |
| 8 | 8.77 | S0 | 9.11 | 8.17 | 8.86 | 9.0 | 8.71 | 5 | /technical-introduction/potential-relation-to-physics/units-and-scales/ |
| 9 | 8.766 | S1 | 8.76 | 9.1 | 8.49 | 9.05 | 8.43 | 2 | /technical-introduction/potential-relation-to-physics/the-structure-of-space/ |
| 10 | 8.734 | S3 | 8.74 | 8.81 | 8.42 | 8.97 | 8.73 | 2 | /technical-introduction/the-updating-process-for-string-substitution-systems/the-concept-of-branchial-graphs/ |
| 11 | 8.69 | S0 | 9.03 | 8.57 | 8.62 | 9.0 | 8.23 | 3 | /technical-introduction/potential-relation-to-physics/event-horizons-and-singularities-in-spacetime-and-quantum-mechanics/ |
| 12 | 8.636 | S3 | 8.46 | 8.31 | 8.92 | 8.93 | 8.56 | 2 | /technical-introduction/potential-relation-to-physics/cosmology-expansion-and-singularities/ |
| 13 | 8.564 | S4 | 8.55 | 8.55 | 8.11 | 8.54 | 9.07 | 5 | /technical-introduction/potential-relation-to-physics/basic-concepts-of-quantum-mechanics/ |
| 14 | 8.548 | S2 | 8.8 | 7.62 | 8.93 | 8.51 | 8.88 | 4 | /technical-introduction/potential-relation-to-physics/correspondence-between-relativity-and-quantum-mechanics/ |
| 15 | 8.48 | S0 | 8.89 | 8.49 | 8.2 | 8.53 | 8.29 | 3 | /technical-introduction/potential-relation-to-physics/multiway-systems-in-the-space-of-all-possible-rules/ |
| 16 | 8.466 | S4 | 8.69 | 7.97 | 8.27 | 8.61 | 8.79 | 4 | /technical-introduction/potential-relation-to-physics/quantum-formalism/ |
| 17 | 8.446 | S4 | 8.35 | 8.37 | 8.29 | 8.51 | 8.71 | 1 | /technical-introduction/potential-relation-to-physics/reversibility-and-irreversibility/ |
| 18 | 8.386 | S0 | 8.78 | 8.48 | 7.95 | 8.03 | 8.69 | 2 | /technical-introduction/potential-relation-to-physics/the-vacuum-einstein-equations/ |
| 19 | 8.376 | S4 | 8.24 | 8.46 | 8.06 | 8.46 | 8.66 | 1 | /technical-introduction/potential-relation-to-physics/motion-and-special-relativity/ |
| 20 | 8.324 | S3 | 8.38 | 7.97 | 8.04 | 8.79 | 8.44 | 1 | /technical-introduction/limiting-behavior-and-emergent-geometry/nested-patterns/ |
| 21 | 8.264 | S2 | 8.27 | 8.27 | 8.65 | 7.97 | 8.16 | 1 | /questions/relations-to-other-approaches/what-do-your-models-imply-regarding-the-black-hole-information-paradox/ |
| 22 | 8.262 | S0 | 8.99 | 8.88 | 8.16 | 8.31 | 6.97 | 1 | /technical-introduction/ |
| 23 | 8.252 | S1 | 8.44 | 8.58 | 7.56 | 8.26 | 8.42 | 3 | /technical-introduction/equivalence-and-computation-in-our-models/computational-capabilities-of-our-models/ |
| 24 | 8.238 | S0 | 9.02 | 8.68 | 7.16 | 8.27 | 8.06 | 4 | /technical-introduction/limiting-behavior-and-emergent-geometry/the-notion-of-dimension/ |
| 25 | 8.236 | S3 | 8.2 | 8.11 | 8.02 | 8.62 | 8.23 | 1 | /technical-introduction/the-updating-process-in-our-models/large-scale-structure-of-causal-graphs/ |
| 26 | 8.128 | S3 | 8.24 | 8.06 | 8.32 | 8.39 | 7.63 | 2 | /technical-introduction/potential-relation-to-physics/time-and-spacetime/ |
| 27 | 8.124 | S4 | 8.29 | 8.48 | 7.09 | 8.25 | 8.51 | 4 | /technical-introduction/potential-relation-to-physics/matter-energy-and-gravitation/ |
| 28 | 8.104 | S0 | 8.37 | 8.07 | 7.88 | 8.23 | 7.97 | 2 | /technical-introduction/potential-relation-to-physics/basic-concepts/ |
| 29 | 8.09 | S0 | 8.75 | 8.28 | 6.75 | 8.19 | 8.48 | 2 | /technical-introduction/the-updating-process-in-our-models/local-symmetries/ |
| 30 | 8.086 | S0 | 8.87 | 7.73 | 7.74 | 8.35 | 7.74 | 2 | /technical-introduction/the-updating-process-for-string-substitution-systems/causal-foliations-and-causal-cones/ |

## Nachtraegliche Leseempfehlung (nicht eingefroren, aus Stichwortlisten, kausal-Liste und eigenem Lesen)

Fuer den feldforscher, der laut seiner Seitenkarte Kapitel 8 der Technical Introduction schon weitgehend gelesen hat, liegt der
Zusatznutzen ausserhalb von Kapitel 8:

- S1/S4 (Dimension, Kruemmung): 4.5 The Notion of Dimension, 4.6 Dimension-Related Characterizations, 4.7 Curvature,
  4.15 Geodesics (Stichwort-Spitze S4).
- Ue3 (Kausalgraphen wie Kausalmengen): Q&A "How do your models relate to causal set theory and causal dynamical
  triangulation?"; 5.7 Events and Their Causal Relationships, 5.8 Causal Graphs for Particular Updating Sequences, 5.14 Foliations
  and Coordinates on Causal Graphs, 6.1 Updating Events and Causal Dependence, 6.5 Causal Graphs for Causal Invariant Rules,
  6.7 Typical Causal Graphs, Large-Scale Structure of Causal Graphs, Causal Foliations and Causal Cones (alle in Kevs kausal-Liste
  bzw. Leseliste).
- S2: 8.9 Elementary Particles (Stichwort-Spitze S2), Q&A zu Spin-Netzwerken, Spin-Schaeumen und Schleifenquantengravitation.
- Bulletins (nicht abgerufen): event-horizons-singularities-and-other-exotic-spacetime-phenomena, confluence-and-causal-invariance,
  local-multiway-systems.

## Selbstanzeigen

1. Abruf: 55 der 600 Abrufe gingen an RSS-Feeds aus der Sitemap (.../feed/), 54 an Dubletten (entdeckte Links ohne
   Schraegstrich, Normalisierung fehlte). Dadurch nur 75 Register-Einzelseiten, und die Grenze war erreicht. Meine Auslegung
   "unter wolframphysics.org" = nur www.wolframphysics.org schloss bulletins.wolframphysics.org aus; dort liegen lange,
   physiknahe Texte. Das ist die wichtigste Luecke dieses Scans.
2. Rauchlauf 0 scheiterte (Laden ueber den Host-Speicher, Spitze 4,0 GB = MemoryMax, kalte HDD): 10 min Spur ohne Ergebnis;
   Lader danach geaendert (vor dem Einfrieren).
3. fp16 auf Pascal statt Kevs fp32-Referenzpfad; keine Paritaetsprobe gegen fp32 gerechnet. Werte koennen in der zweiten
   Nachkommastelle abweichen; Rangfolgen nahe beieinander liegender Abschnitte sind nicht belastbar.
4. Zustaende bis 1169 Token, Kev ist nur bis 384 Zustandstoken trainiert.
5. Fragenkatalog von mir formuliert und nicht vorab an Kev geprueft; die beschrifteten Stufen 5 und 10 ziehen Wahrscheinlichkeit
   an (gestauchte Werte). Andere Formulierungen (z. B. noul je Schicht statt score) wurden nicht versucht.
6. Gegenprobe: ein Leser (ich), ein Durchgang, 25 Abschnitte; S1/S2/S4 mit k = 3/2/1, S3 mit k = 0. Die Stichprobe besteht zu 6/25
   aus Registerseiten bzw. -listen und zu 6/25 aus Q&A (davon 2 Listen); 13/25 stammen aus der Technical Introduction. Ein zweiter,
   fremder Einstufer fehlt.
7. Plan erst nach Abruf, Aufbereitung, Handeinstufung und Rauchlaeufen geschrieben (Reihenfolge laut Auftrag: erst Rauchlauf,
   dann einfrieren). Vor dem Einfrieren sah ich Kev-Werte fuer vier synthetische und neun echte Nicht-Stichproben-Abschnitte
   (Rauch 1 und 2, Auswertungstest), alle nach der Handeinstufung (14:47:47).
8. GPU-Spitze auf p4000a 2,7 GiB bei 2,6 GiB freiem Speicher vor dem Laden (das Ollama-Modell belegte den Rest): knapp, kein
   Speicherfehler; ob der Ollama-Dienst kurz betroffen war, habe ich nicht geprueft.
9. Der erste Auswertungsaufruf auf cpu4 wartete hinter fremden Laeufen an der Sperre; ich habe meine eigenen wartenden Prozesse
   per PID beendet und denselben Aufruf auf cpu3 gestartet.
10. Nachtraegliche Diagnosen (Schicht-Korrelationen, Rangplaetze, Leseempfehlung) standen nicht im Plan; sie erklaeren, aendern
    aber kein Urteil.
11. brain-kev-0.8b nicht getestet. Falls man Kev weiter verfolgen will: Laut Kev-README hilft ein kurzer Feinschliff mit einigen
    hundert gelabelten Beispielen mehr als jede Umformulierung; dafuer braeuchte es aber erst gelabelte Physikabschnitte.
12. Registerseiten enthalten Wolfram-Language-Code als Text (Rauschen fuer Kev und Stichworte); Q&A-Kategorieseiten mit Anrissen
    ueberschneiden sich mit den Einzelseiten.

## Dateien

- PLAN.md (+ PLAN.md.eingefroren-20261004-145706), EINGEFROREN-SHA256.txt, gegenprobe-hand.json
- seiten/ (Rohdaten, INDEX.tsv), meta/ (robots.txt, Sitemap, Listen, crawl.log)
- code/ (crawl.sh, aufbereiten.py, kev_lauf.py, kev_bewerten.py, fragen.json, stichworte.json, auswertung.py, je mit eingefrorener
  Kopie; kev_bewerten.py.v1-rauch0 und aufbereiten.py.v1 sind die verworfenen Vorfassungen)
- daten/ (abschnitte.jsonl, Stichprobe, Statistik), daten-v1/ (verworfene erste Aufbereitung)
- rauch-69/ (Rauch 0 bis 2, Auswertungstest), lauf-69/ (kev-a/b.jsonl, Logs, auswertung.json, tabellen.md, PRUEFSUMMEN.txt)
- .69: /home/fmh/fmhc-physics-remote/runde41-wolfram-kev/ (gleiche Struktur). ~/brain-kev unveraendert: find -newermt 14:00 CEST ergab um 15:18:54 null Dateien; keine Einheit, kein Server, kein Dienst blieb zurueck.

## Einfach gesagt

Wir haben rund 500 Seiten der Wolfram-Physik-Webseite heruntergeladen, in 548 Textstuecke zerlegt und ein kleines KI-Modell (Kev)
gefragt, wie sehr jedes Stueck von Raum, Licht, Teilchen, Kraeften oder Schwerkraft handelt. Kev hat alles beantwortet, gibt aber
fast jedem Stueck bei allen fuenf Themen aehnliche Noten: Es merkt eher, ob ein Text wichtig klingt, als worum es darin geht. Eine
einfache Suche nach Woertern wie "gravity" oder "particle" hat in unserer Stichprobe genauso gut oder besser getroffen. Nur bei der
Frage "Geht es um Kausalgraphen?" lag Kev immer richtig. Die wichtigsten noch ungelesenen Texte sind die "Bulletins" auf einer
Unterseite, die wir nicht heruntergeladen haben.
