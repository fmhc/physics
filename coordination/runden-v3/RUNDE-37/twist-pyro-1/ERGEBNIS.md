# TWIST-PYRO-1: Ergebnis (Runde 40)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date):**
  - Start 2026-10-04 11:34:08 CEST; Plantext ab 11:54:40; Text dieses Ergebnisses ab 12:08:01 CEST.
  - Rauchlaeufe 11:59:56 bis 12:04:07 CEST (vier Laeufe und ein Kandidatenlauf, PLAN.md Abschnitt 7).
  - Plan und Code eingefroren 12:05:06 CEST (EINGEFROREN-SHA256.txt).
  - Hauptlauf auf der .69 12:05:14 bis 12:05:20 CEST (10:05:14 bis 10:05:20 UTC), Spur cpu6 ueber kleintest.sh,
    rc = 0, 6,11 s Rechenzeit. Auswertung 12:05:20 CEST, rc = 0.
  - Nachtrag (Fig. 5, Gl. 11, Gegenbeispiel) 12:07:14 CEST, rc = 0.
- **Kennzeichen:** [S] an der Quelle gelesen (Levin/Wen, PRB 73, 035122 (2006), arXiv:hep-th/0507118v2, lokale Kopie
  in quellen/); [M] eigene Mathematik; [H] Hypothese; [Z] Zusatz des Plans, nicht aus der Karte.
- **Art des Ergebnisses:** synthetische, exakte Ganzzahl-Rechnung an Modellgittern, keine Messdatenbestaetigung. Das
  Ergebnis der Hauptlesart war vor der Rechnung ableitbar (PLAN.md Abschnitt 1.5). Die Rechnung prueft den Nachbau,
  die Schreibtisch-Argumente und die Lesart der Quelle.

## Ergebnis zuerst

1. **Der Levin/Wen-Twist laesst sich auf beide Lesarten von Finns Netz uebertragen**, wenn man die Rahmungsregel der
   Quelle lokal liest (Hauptlesart S: nur Kreuzungen an den Knoten der Kurve zaehlen):
   - Diamant ("durch"): 0 von 93 096 Paaren gedrehter Sechsecke antivertauschen; die Huepfalgebra gibt -1 in allen
     5184 Tripeln.
   - Pyrochlor-Kanten ("entlang"): 0 von 73 536 Paaren (Dreiecke und Sechsecke) antivertauschen; -1 in allen
     15 360 Tripeln.
   - Beides gilt bei allen drei Projektionen und beiden Zellgroessen. Alle Huepfer vertauschen mit allen gedrehten
     Schleifen; keine Schleife aendert eine Ladung.
   - TP0 bis TP3 sind eingetroffen.
2. **Das war vorab ableitbar** [M, PLAN.md 1.2 bis 1.4]:
   - Die Ladung ueber orientierte Kanten braucht kein bipartites Gitter.
   - Die Huepfer an einem Knoten zerfallen fuer jeden Grad in zwei Gruppen ("links" und "rechts" der
     Rahmungsrichtung). Daraus folgt -1 fuer jedes Tripel.
   - Ein Jordan-Argument (zwei geschlossene Kurven der Ebene kreuzen sich gerade oft) macht alle gedrehten Schleifen
     vertraeglich, auf jedem Netz.
   - Dreiecke und Nicht-Bipartitheit spielen keine Rolle. Die Sorge der Karte ("Pyrochlor kann scheitern") hat keinen
     Grund im Gitter.
3. **Die woertliche Lesart scheitert schon an der Quelle:** Zaehlt man jede Kreuzung der ganzen Kantenstrecke
   (Lesart V), dann antivertauschen Plaketten schon auf LWs eigenem kubischen Gitter (512 Paare bei L = 4, jede
   Projektion), ebenso Sechsecke beim Diamant und Dreiecke/Sechsecke beim Pyrochlor. Das widerspricht LWs Aussage, (7)
   gelte fuer jede Projektion. Lesart V ist also keine treue Lesart der Quelle. Das Schreibtisch-Gegenbeispiel ist
   nachgerechnet (Nachtrag: s_V = 1, s_S = 0).
4. **Kontrollen:**
   - ungedreht +1 in allen Tripeln (T3); kubischer Nachbau -1 (T4)
   - Fig. 5 (8 von 8 Kanten) und Gl. (11) (3 von 3 Huepfern) exakt nachgebaut
   - Gegenprobe G1: Huepfer mit falsch gerichteter Rahmung erzeugen 512 bis 5184 antivertauschende Paare; die
     Vertraeglichkeitspruefung kann also scheitern.
5. **Nicht gezeigt:**
   - ob ein solches Quanten-Pfeil-Eis eine Coulomb-Phase hat und wie stark seine Fermionen ans Licht koppeln
   - welchen Hintergrundfluss die Fermionen auf den Dreiecken sehen
   - Spin 1/2 unter Drehungen
   - Gezeigt ist nur die algebraische Vertraeglichkeit.

## Urteile (lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan, Lesart S (Haupturteil) | Wortlaut, S | nach Plan, V | Wortlaut, V |
|---|---|---|---|---|---|---|
| TP0 | T3 = +1, T4 = -1; T1 kubisch erfuellt | 90 % | eingetroffen | eingetroffen | nicht eingetroffen | nicht eingetroffen |
| TP1 | [H] Diamant: T1 fuer mind. eine Projektion, T2 = -1 | 65 % | eingetroffen (P1, P2, P3) | eingetroffen | nicht auswertbar (Kontrolle TP0) | nicht eingetroffen |
| TP2 | [H] Pyrochlor-Kanten: T1 fuer mind. eine Projektion | 40 % | eingetroffen (P1, P2, P3) | eingetroffen | nicht auswertbar (Kontrolle TP0) | nicht eingetroffen |
| TP3 | [H] falls TP2: T2 = -1, unabhaengig von der Projektion | 50 % | eingetroffen | eingetroffen | entfaellt | entfaellt |

- **"nach Plan"** enthaelt zusaetzlich [Z]: Huepfer vertauschen mit allen gedrehten Schleifen (LW S. 6), Gegenprobe G1
  muss anschlagen, und TP1/TP2 sind gesperrt, wenn TP0 nicht eintrifft. **"Wortlaut"** prueft nur T1 bis T4 wie auf
  der Karte.
- Die Hauptlesart S war vor der Rechnung festgelegt (PLAN.md 1.4, mit Begruendung und Selbstanzeige).
- Alle Urteile wie die Schreibtisch-Erwartung in PLAN.md Abschnitt 6.

## Kennzahlen

### Netze (Zaehlungen wie erwartet)

| Netz | Knoten | Kanten | Grad | kleinste Schleifen | T1a-Fehler | T3: +1 |
|---|---|---|---|---|---|---|
| kubisch L = 3 / 4 | 27 / 64 | 81 / 192 | 6 | 81 / 192 Plaketten | 0 / 0 | 3240 / 7680 Tripel |
| Diamant n = 2 / 3 | 64 / 216 | 128 / 432 | 4 | 128 / 432 Sechsecke | 0 / 0 | 1536 / 5184 |
| Pyrochlor n = 1 / 2 | 16 / 128 | 48 / 384 | 6 | 32 + 16 / 256 + 128 (Dreiecke + Sechsecke) | 0 / 0 | 1920 / 15 360 |

- Nicht einfache Schleifen 0, Mehrfachkanten 0, Torus-Zusammenfaelle 0.
- Alle 18 Paare (Netz-Groesse, Projektion) generisch: 0 Entartungen, 0 unklare Kreuzungen.
- Huepfer haben nie ferne Kreuzungen (0 in allen Faellen), wie in PLAN.md 1.3 hergeleitet.

### Lesart S (Hauptlesart), gleich fuer P1, P2, P3

| Netz | Schleifenpaare | antivertauschend | T2: -1 | (Huepfer, Schleife) | antivertauschend | G1 (Gegenprobe) |
|---|---|---|---|---|---|---|
| kubisch L = 3 | 3240 | 0 | 3240 von 3240 | 6561 | 0 | 972 |
| kubisch L = 4 | 18 336 | 0 | 7680 von 7680 | 36 864 | 0 | 2304 |
| Diamant n = 2 | 8128 | 0 | 1536 von 1536 | 16 384 | 0 | 1152 / 1536 / 1536 |
| Diamant n = 3 | 93 096 | 0 | 5184 von 5184 | 186 624 | 0 | 3888 / 5184 / 5184 |
| Pyrochlor n = 1 | 1128 | 0 | 1920 von 1920 | 2304 | 0 | 512 |
| Pyrochlor n = 2 | 73 536 | 0 | 15 360 von 15 360 | 147 456 | 0 | 4096 |

- V1 (Paulimultiplikation) und V3 (symplektisch) stimmen in allen Tripeln ueberein (0 Inkonsistenzen).

### Lesart V (Kontrast), antivertauschende Paare P1 / P2 / P3

| Netz | Schleifenpaare | davon nach Typ | (Huepfer, Schleife) | T2 |
|---|---|---|---|---|
| kubisch L = 3 | 216 / 216 / 216 | Plakette-Plakette | 108 / 108 / 108 | -1 ueberall |
| kubisch L = 4 | 512 / 512 / 512 | Plakette-Plakette | 256 / 256 / 256 | -1 ueberall |
| Diamant n = 2 | 384 / 640 / 384 | Sechseck-Sechseck | 320 / 256 / 320 | -1 ueberall |
| Diamant n = 3 | 1296 / 2160 / 1296 | Sechseck-Sechseck | 1080 / 864 / 1080 | -1 ueberall |
| Pyrochlor n = 1 | 64 / 48 / 48 | Dreieck-Sechseck 48 / 48 / 32; Sechseck-Sechseck 16 / 0 / 16 | 48 / 72 / 64 | -1 ueberall |
| Pyrochlor n = 2 | 640 / 384 / 640 | Dreieck-Sechseck 384 / 384 / 256; Sechseck-Sechseck 256 / 0 / 384 | 384 / 576 / 512 | -1 ueberall |

- Kein Dreieck-Dreieck-Paar antivertauscht, auch in Lesart V.
- Die Zahl der antivertauschenden (Huepfer, Schleife)-Paare ist in Lesart V gleich der Zahl der fernen Kreuzungen
  (z. B. kubisch L = 4: 256 und 256; Diamant n = 3, P2: 864 und 864) [beschreibend].
- Beim Pyrochlor n = 1 weichen die Zahlen je Zelle von n = 2 ab (Umlauf auf dem kleinen Torus, mehrere Bilder einer
  Schleife). Lesart S ist davon nicht betroffen (0 bei beiden Groessen).

## Kontrollen

- **T3 (ungedreht):** +1 in allen 34 920 Tripeln aller Netze. Folgt aus der Pauli-Algebra und prueft nur den Code [M].
- **T4 (kubischer Nachbau, P1):** -1 in 3240 und 7680 Tripeln, in beiden Lesarten.
- **Nachbau der Quelle (Nachtrag, kubisch L = 4, P1):**
  - Fig. 5: Drehmenge der xz-Plakette = genau die acht Kanten der Abbildung, in Lesart S und V.
  - Gl. (11): x-Kante -> -z- und -y-Bein am rechten Ende; y-Kante -> +x-Bein unten, -z-Bein oben; z-Kante -> +x- und
    +y-Bein unten. Alle drei wie vorab erwartet.
  - Gegenbeispiel aus PLAN.md 1.4 (xz-Plakette p bei y = 0, yz-Plakette r' bei x = 1, y = -1..0): s_S = 0, s_V = 1,
    wie vorab erwartet.
- **Gegenprobe G1 [Z]:** Huepfer mit gleichsinniger Rahmung (delta_h = +delta_p) antivertauschen mit vielen Schleifen
  (Tabelle oben, Lesart S). Die Huepfer-Schleifen-Pruefung kann also scheitern; mit der LW-Richtung (rechts unten gegen
  links oben) gibt sie 0.
- **Generizitaet:** 0 Entartungen und 0 unklare Kreuzungen in allen 18 Faellen.
- **Was nicht scheitern konnte [M]:** T1a (Orientierung), T2 und T3 (Zwei-Cliquen-Satz bzw. leere Z-Mengen), in
  Lesart S auch T1b und Z3 (Jordan-Argument). Scheitern konnten: der Nachbau von Fig. 5 und Gl. (11), die beiden
  Schreibtisch-Argumente selbst und die Generizitaet der Projektionen. Neu (nicht vorab hergeleitet) war nur, wie stark
  Lesart V auf Diamant und Pyrochlor scheitert.

## Kartenberichtigungen (vor dem Einfrieren, PLAN.md Abschnitt 1)

1. **Spin 1/2:** Fuer Spin 1/2 vertauschen schon ungedrehte Schleifen mit gemeinsamer Kante nicht. T1 ist deshalb als
   Drehvorzeichen gefasst (Rotor-Algebra wie LW, exakt ueber GF(2)). Fuer Spin 1/2 heisst T1: Der gedrehte Kommutator
   ist gleich dem ungedrehten, bis auf eine unitaere Z-Kette [M, nicht mit Matrizen gerechnet].
2. **Ableitbarkeit:** Die Karte nennt TP1 "teilweise", TP2 und TP3 "nein" ableitbar. In Lesart S sind alle vier vorab
   ableitbar; offen war nur die Lesart von Gl. (8).
3. **Lesart von Gl. (8):** "Kanten, die die Rahmung C' kreuzen" ist zweideutig (ganze Kante oder nur am Kurvenknoten).
   Beide Lesarten sind gerechnet; nur die lokale (S) macht die Aussagen der Quelle wahr.
4. **[Z] Zusaetze:** Huepfer-Schleifen-Vertraeglichkeit (LW S. 6 verlangt sie; ohne sie waere T2 = -1 fuer jede
   Projektion gesetzt) und Gegenprobe G1. Beide getrennt markiert; die Wortlaut-Urteile kommen ohne sie aus.

## Latten (v3)

- **L1 kann scheitern:** teilweise. In Lesart S war alles ableitbar; scheitern konnten Nachbau und Argumente.
  Lesart V konnte und hat gezeigt, dass die Pruefung "antivertauscht" melden kann.
- **L2 Gegenprobe:** ja. Ungedreht (T3), G1, Lesart V als Kontrast, Gegenbeispiel.
- **L3 Numerik:** exakt, ganzzahlig (Kreuzungen mit ganzzahligen Kreuzprodukten, Vorzeichen ueber GF(2)).
- **L4 schon bekannt:** teilweise. LW behaupten "Any projection will work" fuer das kubische Gitter [S]. Dass die lokale
  Lesart auf jedem Netz traegt, habe ich nur am Schreibtisch und an drei Netzen gezeigt; eine Literaturstelle dazu habe
  ich nicht gesucht.
- **L5 Messbezug:** keiner.

## Bedeutung fuer Finns Bild

- **Belegt im Modell [M, nachgerechnet]:**
  - Beide Lesarten von "dadurch oder daran entlang" vertragen den LW-Twist: Auf dem Spin-Eis-Gitter ("durch") und auf
    den Pyrochlor-Kanten ("entlang") koennen die Enden der Pfeilfaeden algebraisch Fermionen sein (H1 aus
    DYON-STATISTIK-L ist baubar).
  - Das Gitter ist dafuer nicht der Engpass. Bipartit oder nicht, Grad 4 oder 6, Dreiecke oder nicht: alles gleich.
  - Der Twist ist eine Eigenschaft der Dynamik, nicht des Netzes: Jede kleine Schleifenbewegung der Pfeile traegt ein
    Vorzeichen, das von den Pfeilen auf den angrenzenden Beinen abhaengt, und nur von diesen (lokale Lesart).
- **Nicht gezeigt [H]:**
  - ob das gedrehte Quanten-Pfeil-Eis eine Coulomb-Phase hat und wie gross alpha dann ist (O1 aus DYON-STATISTIK-L)
  - welchen Hintergrundfluss die Fermionen auf Dreiecken und Sechsecken sehen (LW Gl. 20); auf dem nicht-bipartiten
    Netz koennte er die Fermionenbaender frustrieren
  - ob Finns "Krafteinheiten" so eine Vorzeichenregel natuerlich mitbringen
- **Vorschlag fuer eine Folgekarte [H, nicht gerechnet]:** Das Produkt der gedrehten Huepfer um Dreieck und Sechseck
  auf den Pyrochlor-Kanten berechnen (Gegenstueck zu LW Gl. 20), daraus den Hintergrundfluss und die freie
  Fermionen-Bandstruktur. Erst dort kann "entlang" sich von "durch" unterscheiden.

## Selbstanzeigen

1. **Hauptlesart in Kenntnis der Erwartung:** Lesart S habe ich gewaehlt, als ich vom Schreibtisch wusste, dass S
   besteht und V an TP0 scheitert. Beide Lesarten sind vollstaendig berichtet.
2. **Vor dem Einfrieren gesehen:**
   - Die Rauch-Urteile mit den kleinsten Groessen (rauch, rauch3, rauch4), alle wie im Hauptlauf.
   - Danach habe ich P1 und P3 ersetzt. Grund: exakte Projektionszufaelle beim Diamant (ein Knoten liegt projiziert genau
     auf einer Kante desselben Sechsecks), 128 unklare Kreuzungen. Einziges Kriterium war die Generizitaet; P3 kam per
     vorab im Skript festgelegter Regel aus fuenf Kandidaten (der erste generische).
   - Mit den alten Projektionen haette TP1 sich nur auf P2 gestuetzt; das Urteil waere gleich gewesen.
3. **Lokale Werkzeuge ausserhalb der Liste:** wc, pdfinfo, head, tr, ls, cat (nur Anzeige), dazu eine Shell-Schleife mit
   echo. Lokal lief kein Interpreter.
4. **Auf der .69 ausserhalb des Starters:** nur mkdir, mv, ls, cat, grep, tail, sha256sum. Beim Einfrieren habe ich die
   drei Codedateien per scp direkt ueber die vorhandenen kopiert (nicht ueber .neu und mv). Es lief keine Instanz, der
   Inhalt war identisch (Pruefsummen gleich).
5. **Quelle:** keine neuen Abrufe (0 von 3), lokale Kopie des Feldforschers. Fig. 4 bis 6 habe ich nur als niedrig
   aufgeloestes Seitenbild gesehen; meine Lesart der Figuren stuetzt sich auf den exakten Nachbau (Fig. 5: 8 von 8
   Kanten, Gl. 11: 3 von 3 Huepfern).
6. **Nachtrag nach dem Einfrieren:** code/nachtrag_fig5.py importiert den eingefrorenen Code unveraendert. Grund: Drei
   Schreibtisch-Aussagen (Fig. 5, Gl. 11, Gegenbeispiel) standen im Hauptlauf nicht einzeln. Die Erwartungen stehen
   fest im Skript.
7. **Gleitkomma:** nur in der Diagnose-Beispielliste unklarer Kreuzungen (Text, im Hauptlauf leer). Kein Urteil haengt
   daran.
8. **Spin 1/2** ist nur ueber die Herleitung in PLAN.md 1.1 behandelt, nicht mit Matrizen gerechnet.
9. **Laufbuchhaltung:** Nach dem Einfrieren nichts an Plan, Code oder Urteilsregeln geaendert; genau ein Hauptlauf und
   eine Auswertung. Zeitbox 120 min ab 11:34:08; Hauptlauf beendet 12:05:20. Kein Journaleintrag, kein Peerbus, kein
   Commit.

## Dateien

- **Plan:** PLAN.md und PLAN.md.eingefroren-20261004-120506; Pruefsummen in EINGEFROREN-SHA256.txt.
- **Code:** code/twist_pyro.py, code/auswertung.py, code/kandidaten.py (je mit .eingefroren-20261004-120506);
  code/nachtrag_fig5.py (Nachtrag).
- **Quelle:** quellen/arxiv-hep-th-0507118.pdf und .txt (Kopie aus DYON-STATISTIK-L/quellen/).
- **Rauchlaeufe:** rauch-69/ (rauch, rauch2, rauch3, rauch4 mit Auswertungen; kandidaten).
- **Hauptlauf:** lauf-69/haupt.json, haupt.log, auswertung.json, auswertung.log, nachtrag_fig5.json und .log;
  Pruefsummen beider Rechner in lauf-69/PRUEFSUMMEN.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/runde40-twist-pyro/ (code/, rauch/, lauf/).

## Einfach gesagt

Finns Netz soll Pfeile tragen, die durch Tetraeder oder an ihren Kanten entlang laufen; wo ein Pfeilfaden endet, sitzt
ein Teilchen. Damit dieses Teilchen sich wie ein Elektron verhaelt (beim Vertauschen ein Minuszeichen), muss jede kleine
Kreisbewegung der Pfeile ein zusaetzliches Vorzeichen bekommen, das von den Nachbarpfeilen abhaengt. Wir haben exakt
nachgerechnet, dass diese Regel auf beiden Netzen widerspruchsfrei funktioniert, auch auf dem Netz mit Dreiecken, bei
dem man Probleme erwartet hatte. Das liess sich schon vorher mit Papier und Bleistift zeigen; die Rechnung bestaetigt es
und zeigt nebenbei, dass man die Regel aus dem Fachartikel genau richtig lesen muss, sonst geht sie sogar im
Originalmodell kaputt. Ob so ein Netz wirklich Licht und schwach gekoppelte Elektronen hervorbringt, ist damit noch
nicht gezeigt.
