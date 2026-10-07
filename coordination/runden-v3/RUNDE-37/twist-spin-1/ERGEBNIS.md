# TWIST-SPIN-1: Ergebnis (Runde 41)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date):**
  - Start 2026-10-04 13:14:01 CEST; Plantext ab 13:44:17; Text dieses Ergebnisses ab 13:51:43 CEST.
  - Rauchlaeufe 13:47:01 bis 13:49:45 CEST (drei Laeufe mit Auswertung, PLAN.md Abschnitt 7).
  - Plan und Code eingefroren 13:50:28 CEST (EINGEFROREN-SHA256.txt).
  - Hauptlauf auf der .69 13:50:34 bis 13:50:55 CEST (11:50:34 bis 11:50:55 UTC), Spur cpu6 ueber kleintest.sh,
    rc = 0, 21,4 s Rechenzeit. Auswertung 13:50:55 CEST, rc = 0.
- **Kennzeichen:** [S] an der Quelle gelesen (Levin/Wen, PRB 73, 035122 (2006), arXiv:hep-th/0507118v2, lokale Kopie
  in quellen/); [M] eigene Mathematik; [R] im Rauchlauf vor dem Einfrieren gesehen; [L] Gedaechtnis; [H] Hypothese;
  [Z] Zusatz des Plans, nicht aus der Karte.
- **Art des Ergebnisses:** synthetische, exakte Ganzzahl-Rechnung an Modellgittern, keine Messdatenbestaetigung. Die
  Haupturteile waren vorab ableitbar (PLAN.md 1.8). Offen war nur Stufe F (Fermionfluss); den habe ich im Rauchlauf
  vor dem Einfrieren gesehen.

## Ergebnis zuerst

1. **Mit fester Projektion wirken die Tetraeder-Drehungen nicht als Symmetrie der verdrehten Operatoren.** Die
   Projektion legt eine Raumrichtung nu fest. Schon die Vertauschungsregeln der Huepfer haengen davon ab, und nur eine
   kleine Untergruppe laesst sie unveraendert. Kein lokaler Eichfaktor kann das reparieren (PLAN.md 1.2).
   - Diamant: C3 (P1) bzw. V4 (P2, P3) statt T. Pyrochlor-T: eine C2. Pyrochlor-D3 am Platz: nur die Identitaet.
   - Auch LWs eigenes kubisches Modell hat nur D3 statt O und keine Vierteldrehung.
   - Alle 18 Faelle (Netz, Groesse, Projektion) wie vorab hergeleitet.
2. **Im Sektor fester Teilchenzahl wirken sie doch [Z]:** Ein Fermion, das um eine kleinste Schleife huepft, sieht
   ueberall den Fluss 0 (Phi = +1 auf allen 432 Sechsecken, 384 Pyrochlor-Schleifen, 192 Plaketten). Der Fluss ist
   gleichfoermig, also drehsymmetrisch. Das war nicht vorab hergeleitet; im Rauchlauf gesehen.
3. **Dort ist das Fadenend-Fermion spinlos.** (C3)^3, (C2)^2 und (C2 C3)^3 sind +1 an allen Knoten, die
   Invarianten sind +1, auch beim Pyrochlor-T ohne festen Knoten. Auf Paarerzeugern ist jedes Pruefvorzeichen +1. Das
   war am Knoten vorab hergeleitet: ein Zustand je Knoten erlaubt keine projektive Klasse. Die Quelle vergleicht ihre
   Fermionen selbst mit spinlosen Gitterfermionen (S. 7).
4. **Gegen die Vermutung der Leitung:** Spin und Statistik kommen auf Finns Netz nicht aus derselben Verdrehung. Die
   Statistik ist fermionisch (-1, TWIST-PYRO-1), der Spin unter Gitterdrehungen ganzzahlig. Der Guerteltrick braucht
   stetige Rahmungswechsel; auf dem Gitter bricht er dort, wo sich die Vertauschungsregeln aendern. Halber Spin braucht
   mindestens zwei Zustaende je Knoten oder entsteht erst in der Bandstruktur, wie bei LW (S. 9).
5. **Kontrollen:** ungedreht alles +1 (TS0); Handrechnung zu Fig. 5 exakt getroffen; beide Gegenproben schlagen an;
   alle geschlossenen Zellen haben +1 (kein frustrierter Fluss). Beim kleinsten Pyrochlor-Torus lassen sich 8 Zellen
   nicht pruefen, deshalb ist TS3-schwach "nicht auswertbar".

## Urteile (lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan (Stufe K, Haupturteil) | Wortlaut (Stufe W) | [Z] schwach (Stufe F) |
|---|---|---|---|---|---|
| TS0 | ungedreht echte Darstellung, alle Pruefvorzeichen +1 | 90 % | eingetroffen | eingetroffen | eingetroffen |
| TS1 | [H] Diamant: Tetraederdrehungen mit lokalen Eichfaktoren symmetrisch | 55 % | **nicht eingetroffen** (keine Projektion; K-Untergruppe C3 bzw. V4) | **nicht eingetroffen** (je Projektion nur e bzw. e und C2y) | eingetroffen (P1, P2, P3) |
| TS2 | [H] falls TS1: projektiv, Spin 1/2 (ein Pruefvorzeichen -1) | 45 % | entfaellt | entfaellt | **nicht eingetroffen** (Invariante (C2)^2 = +1, alle Werte +1) |
| TS3 | [H] Pyrochlor-Kanten wie Diamant | 40 % | eingetroffen (Pyrochlor-T: TS1 nicht eingetroffen, TS2 entfaellt, wie Diamant) | eingetroffen (ebenso) | nicht auswertbar (Pyrochlor n = 1: 8 Zellen nicht geschlossen) |

- **Plan** = Stufe K: Es gibt eine lokale Unitaere (Vorzeichen, Knotenfaktoren und CZ-artige Phasen), die jeden
  verdrehten Huepfer genau auf den gedrehten und jede Schleife auf +Schleife abbildet.
- **Wortlaut** = Stufe W: g W~(C) g^-1 = +- W~(gC) mal Faktoren (-1)^Q je Knoten ("Vorzeichen je Kante bzw. Knoten").
- **[Z] schwach** = Stufe F: Das Einteilchen-Huepfproblem (fester Teilchenzahl, hardcore) ist symmetrisch, weil der
  Fermionfluss g-invariant ist. Grundlage ist die Quelle S. 8: (19) und (20) bestimmen das Huepfproblem vollstaendig.
- Alle Plan- und Wortlaut-Urteile wie die Schreibtisch-Erwartung in PLAN.md 4. Schwach war offen.

## Kennzahlen

### Stufe K: Untergruppen mit invariantem Vertauschungsgraph (= Elemente, auf denen Stufe K traegt)

| Netz (Groessen) | P1 | P2 | P3 | wie PLAN.md 1.3 |
|---|---|---|---|---|
| Diamant, T am Knoten (n = 2, 3) | {e, C3, C3^2} um [111] | V4 = {e, C2x, C2y, C2z} | V4 | ja (6 von 6) |
| Pyrochlor, T am Tetraederzentrum (n = 1, 2) | {e, C2y} | {e, C2z} | {e, C2y} | ja (6 von 6) |
| Pyrochlor, D3 am Platz (n = 1, 2) | {e} | {e} | {e} | nicht hergeleitet |
| kubisch, O am Knoten (L = 3, 4) | D3 um [111] (6) | D3 um [1,-1,-1] (6) | D3 um [1,-1,-1] (6) | ja (6 von 6) |

- Abweichende Paare (l, m) je nicht-symmetrischem Element: Diamant n = 3: 864; Pyrochlor n = 2: 512 bis 1024;
  kubisch L = 4: 512.
- Auf allen K-Untergruppen sind alle Schleifenvorzeichen sigma = +1 und alle Huepfer exakt (Stufe K traegt genau
  dort).
- Relationsautomorphismen, wo berechenbar (alle Buchstaben K-symmetrisch): Diamant P1 (C3)^3, Diamant P2/P3 (C2)^2,
  Pyrochlor-T P2 (C2)^2, kubisch P1 (C3)^3: jeweils Identitaet, Paarerzeuger +1 (PLAN.md 1.6a).

### Stufe W (Kartenwortlaut)

- Diamant n = 3, P1: 324 bis 432 von 432 Huepfern und 432 von 432 Sechsecken haben eine nichtleere Fehlmenge je
  Element; Stufe W traegt nur fuer e. P2, P3: nur e und C2y (C2y bildet die eine Seite auf die andere ab; das hatte
  der Plan nicht einzeln vorhergesagt, nur das Scheitern an C2x und C3).
- Pyrochlor-T: P1, P2 nur e; P3 e und C2y. D3: nur e. Kubisch: je e und eine C2.

### Stufe F (Fermionfluss) [Z]

| Netz | Schleifen | Phi = +1 | inkonsistent | Phase -1 bzw. Start in V' (je Auswertung) |
|---|---|---|---|---|
| Diamant n = 3 | 432 Sechsecke | 432 (P1, P2, P3) | 0 | P1: 2592 von 5184; P2, P3: 3456 von 5184; beide stets gemeinsam |
| Pyrochlor n = 2 | 256 Dreiecke, 128 Sechsecke | 384 | 0 | 1536 von 3072 |
| kubisch L = 4 | 192 Plaketten | 192 | 0 | 768 von 1536 |

- Gleich bei den kleineren Groessen. |E n T| ist ueberall gerade.
- Damit traegt Stufe F fuer alle Elemente aller Gruppen, auch fuer C4 im kubischen Modell.

### PSG (Stufe F, ganze Gruppe)

- Holonomie-Maske 0 genuegt ueberall. Relationswerte an allen Knoten konstant +1: (C3)^3, (C2)^2, (C2 C3)^3 (T),
  (C3)^3, (C4)^4, (C4 C3)^2 (O), (C3)^3, (C2)^2, (C2 C3)^2 (D3). Paarerzeuger am Bezugsknoten +1.
- Invariante: (C2)^2 = +1 fuer T (Diamant und Pyrochlor), (C4)^4 = +1 fuer O; D3 hat keine (PLAN.md 1.6).
- Bei Fluss 0 ueberall sind die Eichfaktoren trivial: Die Drehungen wirken als reine Permutation der Knoten.

## Ableitbarkeit

- **Vorab hergeleitet [M] (PLAN.md 1.2 bis 1.6):** Seitensatz (K haengt nur an nu = 4 M_0 + 5 M_1), alle
  K-Untergruppen ausser D3, das Scheitern von Stufe W, die Trivialitaet der Klasse am festen Knoten, Paarerzeuger = +1
  bei exakter Symmetrie. Damit waren TS0, TS1 und TS2 (Plan, Wortlaut) und TS3 (Plan) vor der Rechnung bekannt.
- **Nur Kontrolle:** TS0; die K-Untergruppen; die Relationsautomorphismen; die PSG-Werte am Diamant-Knoten.
- **Neu durch die Rechnung:** Fermionfluss 0 auf allen Schleifen (vor dem Einfrieren im Rauchlauf gesehen [R]);
  daraus Stufe F; die PSG-Klasse beim Pyrochlor-T ohne festen Knoten (trivial); die Frustrationsfreiheit; die
  D3-Ergebnisse; welche Einzelelemente Stufe W tragen.
- Vertraeglich mit der Quelle S. 8, Gl. (20): Das Huepferprodukt um eine Doppelplakette ist der Eichfluss "up to some
  signs having to do with orientation conventions" [S]; in diesen Konventionen kommt kein Zusatzzeichen.

## Kontrollen

- **TS0 (ungedreht):** alle Elemente aller Gruppen tragen Stufe W, K und F; alle Relationsautomorphismen Identitaet;
  alle Paarerzeuger +1; PSG-Werte +1; Invarianten +1 bzw. keine (D3). Folgt aus D = 0 und prueft den Code [M].
- **Handrechnung Fig. 5 (kubisch L = 3 und 4, P1):** Phi = +1 und V' = {(1,0,0), (0,0,1)}, wie PLAN.md 1.5.
- **Gegenprobe Stufe F:** Fluss der Schleife 0 umgedreht: bis zu 2 Abweichungen je Element; die Pruefung kann also
  scheitern.
- **Gegenprobe Kante 0:** Huepfer auf Kante 0 mit -1: genau die Schleifen mit Kante 0 kippen (Diamant 6, Pyrochlor
  und kubisch 4), in allen Faellen.
- **Frustrationsprobe [Z]:** orientiertes Produkt der B~ ueber jede geschlossene Zelle +1: Diamant 64 und 216
  Adamantan-Kaefige, kubisch 27 und 64 Wuerfel, Pyrochlor n = 2 128 Zellen (64 Tetraeder, 64 Stumpf-Tetraeder),
  Pyrochlor n = 1 8 Tetraeder. Pyrochlor n = 1: 8 Stumpf-Tetraeder "nicht geschlossen" (Torus mit 16 Knoten).
- **Generik:** 0 Entartungen, 0 unklare Kreuzungen, 0 Torus-Zusammenfaelle in allen 24 Faellen (Netz, Groesse,
  Projektion).
- **Was nicht scheitern konnte [M]:** TS0; der Seitensatz als Folge von TWIST-PYRO-1 1.3; die Relationsautomorphismen
  (Identitaet per Konstruktion); die PSG-Werte am festen Knoten. Scheitern konnten: jede einzelne K-Untergruppe (eine
  Abweichung haette den Seitensatz widerlegt), die Schleifenvorzeichen sigma, der Fermionfluss (gleichfoermig oder
  nicht), die Frustrationsprobe und die PSG-Klasse beim Pyrochlor-T.

## Kartenberichtigungen

1. **Pruefvorzeichen auf Paarerzeugern** sind in einem bosonischen Modell bei exakter Symmetrie immer +1 (Relation =
   Skalar). Sie koennen 2T gar nicht zeigen. Die projektive Klasse liest man am Einzelfermion ab (PSG-Invariante).
2. **Einzelne Vorzeichen** (C3)^3 usw. haengen von der Normierung ab. Invariant ist fuer T nur
   I = lambda3^2 / (lambda1^2 lambda2^3), bei reellen Werten (C2)^2. Fuer D3 gibt es keine Invariante, und
   (C2 C3)^3 passt dort nicht (C2 C3 hat Ordnung 2).
3. **"Vorzeichen je Kante bzw. Knoten" reichen nicht:** Die Fehlmengen g T(C) + T(gC) sind Z-Operatoren, keine
   Vorzeichen. Selbst mit CZ-artigen Phasen bleibt nur eine Untergruppe.
4. **LWs kubisches Modell** ist mit fester Projektion selbst nur D3-symmetrisch, nicht O. Die Karte nahm fuer die
   Kontrolle Vierteldrehungen an.

## Latten (v3)

- **L1 kann scheitern:** teilweise. Plan- und Wortlaut-Urteile waren ableitbar; scheitern konnten der Seitensatz in
  jedem Einzelfall, sigma, der Fermionfluss, die Frustrationsprobe und die Pyrochlor-T-Klasse.
- **L2 Gegenprobe:** ja. Ungedreht, Fig. 5, Fluss-Gegenprobe, Kante-0-Gegenprobe, Frustrationsprobe.
- **L3 Numerik:** exakt, ganzzahlig (GF(2)/Z4).
- **L4 schon bekannt:** teilweise. Die Quelle vergleicht mit spinlosen Fermionen (S. 7) und charakterisiert das
  Huepfproblem durch (19), (20) (S. 8) [S]. Dass eine feste Projektion die Gitterdrehungen bricht, habe ich nicht in
  der Literatur gesucht (keine Abrufe).
- **L5 Messbezug:** keiner.

## Bedeutung fuer Finns Bild

- **Belegt im Modell [M, nachgerechnet]:**
  - Das Ende eines verdrehten Pfeilfadens ist auf Finns Netz ein Fermion (TWIST-PYRO-1), aber ein spinloses: Unter
    den Tetraeder-Drehungen verhaelt es sich wie ein Teilchen ohne Eigendrehung.
  - Die Verdrehung braucht eine feste Blickrichtung. Die Regeln selbst sind deshalb nicht drehsymmetrisch; das
    Teilchen merkt davon nichts, solange keine Paare entstehen (Fluss 0 ueberall).
  - Spin 1/2 entsteht hier nicht "von selbst" aus der Verdrehung. Der Spin-Statistik-Zusammenhang gilt auf dem Gitter
    nicht automatisch.
- **Offen [H]:**
  - Ein Knoten mit zwei inneren Zustaenden (z. B. zwei Pfeilsorten oder ein Kramers-artiges Paar) koennte 2T tragen.
    Das waere eine Zusatzstruktur, also eingesetzt.
  - Spin 1/2 kann wie bei LW in der Bandstruktur entstehen (pi-Fluss von Hand, Dirac-Punkte). Dann waere er eine
    Eigenschaft der Bewegung, nicht des Fadenendes.
  - Ob ein drehsymmetrischer Twist ohne feste Projektion existiert (z. B. Rahmung je Knoten aus der Tetraedergeometrie),
    ist nicht geprueft. Nach Satz K muesste er an jedem Knoten alle Huepfer paarweise antivertauschen lassen
    (vollstaendiger Graph, Jordan-Wigner-artige Ordnung); das ist mit einer Ebenenteilung nicht erreichbar.
- **Vorschlag fuer eine Folgekarte [H, nicht gerechnet]:** Zwei Pfeilsorten je Kante (oder Majorana-Paare je Knoten)
  mit T-symmetrischer Knotenordnung; Pruefgroesse: PSG-Invariante (C2)^2 = -1 am Knoten bei Statistik -1.

## Selbstanzeigen

1. **Stufe F vor dem Einfrieren gesehen:** Im ersten Rauchlauf war Phi ueberall +1. Danach habe ich Diagnosezaehler,
   die Kante-0-Gegenprobe und die vollstaendige Kaefigliste ergaenzt (PLAN.md 7). Keine Regel geaendert; die
   Frustrationsregel habe ich nicht gelockert, obwohl ich wusste, dass sie TS3-schwach "nicht auswertbar" macht.
2. **Vor dem Einfrieren gesehen:** die Rauch-Urteile mit den kleinsten Groessen (alle wie im Hauptlauf) und die
   K-Untergruppen (wie Plan).
3. **Festlegungen vor der Rechnung:** Lesart S aus TWIST-PYRO-1 (Lesart V nicht gerechnet); fuer TS3 Pyrochlor-T am
   Tetraederzentrum statt D3 am Platz (gleiche Gruppe wie beim Diamant); D3 nur berichtet.
4. **Quelle:** keine neuen Abrufe (0 von 3). Der Guerteltrick (Finkelstein/Rubinstein 1968) ist Gedaechtnis [L].
5. **Lokale Werkzeuge ausserhalb der Liste:** ls, cat, head, tail, wc, cd und Shell-Schleifen (nur Datei- und
   Anzeigebefehle). Lokal lief kein Interpreter.
6. **Auf der .69 ausserhalb des Starters:** nur mkdir, ls, cp (eingefrorene Kopien), mv, tail, cat, grep, sed (Anzeige
   des Starters), sha256sum. Die erste Fassung der Codedateien habe ich per scp direkt in code/ gelegt (neue Dateien,
   keine Instanz); alle spaeteren Fassungen ueber .neu und mv.
7. **Laufbuchhaltung:** Nach dem Einfrieren nichts an Plan, Code oder Urteilsregeln geaendert; genau ein Hauptlauf und
   eine Auswertung. Zeitbox 120 min ab 13:14:01; Hauptlauf beendet 13:50:55. Kein Journaleintrag, kein Peerbus, kein
   Commit.
8. **Grenze der Stufe F:** Sie stuetzt sich auf die Aussage der Quelle, dass (19) und (20) das hardcore-Huepfproblem
   vollstaendig bestimmen (S. 8). Paarerzeugung ist dort ausgeschlossen; fuer das volle bosonische Modell gilt nur
   Stufe K.

## Dateien

- **Plan:** PLAN.md und PLAN.md.eingefroren-20261004-135028; Pruefsummen in EINGEFROREN-SHA256.txt.
- **Code:** code/twist_spin.py, code/auswertung_spin.py, code/twist_pyro.py (unveraenderte Kopie aus TWIST-PYRO-1),
  je mit .eingefroren-20261004-135028.
- **Quelle:** quellen/arxiv-hep-th-0507118.pdf und .txt (Kopie aus TWIST-PYRO-1).
- **Rauchlaeufe:** rauch-69/ (rauch, rauch2, rauch3, je mit Auswertung).
- **Hauptlauf:** lauf-69/haupt.json, haupt.log, auswertung.json, auswertung.log; Pruefsummen beider Rechner in
  lauf-69/PRUEFSUMMEN.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/runde41-twist-spin/ (code/, rauch/, lauf/).

## Einfach gesagt

Wir wollten wissen, ob das Teilchen am Ende eines "verdrehten" Pfeilfadens in Finns Tetraeder-Netz nicht nur ein
Fermion ist, sondern auch einen halben Spin hat, wie ein Elektron. Die Antwort ist nein: Dreht man das Netz, verhaelt
sich das Teilchen wie ein Teilchen ohne Eigendrehung. Ausserdem braucht die Verdrehung eine feste Blickrichtung, und
deshalb sind die Regeln selbst nicht drehsymmetrisch; das Teilchen spuert das nur nicht, solange es allein herumhuepft.
Der Grund ist einfach: Ein halber Spin braucht mindestens zwei innere Zustaende, und ein Fadenende an einem Knoten hat
nur einen. Fuer einen echten halben Spin muesste Finns Netz an jedem Knoten etwas mehr Struktur mitbringen; das waere
dann eingesetzt und nicht von selbst entstanden.
