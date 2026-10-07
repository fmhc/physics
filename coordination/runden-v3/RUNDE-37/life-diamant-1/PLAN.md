# LIFE-DIAMANT-1: Plan (Runde 38, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 07:05:49 CEST, Plantext ab 07:20:10 CEST (date).
- Karte: KARTE.md (unveraendert). Vorhersagen LD0 bis LD3 und ihre Schwellen sind unten woertlich uebernommen.
- Kennzeichen: [M] eigene Mathematik (Schreibtisch), [F] Festlegung dieses Plans (Karte laesst es offen), [K] Kartenpunkt,
  [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese, [E] gerechnet (erst im Ergebnis).
- Rechnen nur auf der .69, Spur cpu7, ueber kleintest.sh; Ordner /home/fmh/fmhc-physics-remote/runde38-life/.
- Synthetische Rechnung. Kein Messdatenbezug; Ergebnisse sind keine Messdatenbestaetigung.

## 1. Gitter und Darstellung

- Koordinaten in a/4 (a = kubische Zellkante). fcc-Primitivvektoren A1 = (0,2,2), A2 = (2,0,2), A3 = (2,2,0).
- Knoten (n1, n2, n3, s): Lage n1 A1 + n2 A2 + n3 A3 + s (1,1,1); s = 0 Untergitter A, s = 1 Untergitter B.
  - A hat seine 4 Nachbarn bei +e_a, B bei -e_a, e_a in {(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)} [M].
  - In Primitivkoordinaten: A bei n -> B bei n, n-e1, n-e2, n-e3; B bei n -> A bei n, n+e1, n+e2, n+e3 [M].
- **Darstellung [F, Abweichung von der Karte, K4]:** duennbesetzt, sortierte int64-Schluessel je lebendem Knoten,
  unbegrenztes Gitter, **kein periodischer Kasten**.
  - Grund: keine Rand- und Umlauf-Artefakte, Verschiebungen sind exakt verfolgbar, Kosten nur nach Zahl lebender Knoten.
  - Der periodische kubische Kasten (L = 3, 8 L^3 = 216 Knoten) dient nur der Gitterkontrolle LD0 (a): Nachbarn dort
    unabhaengig ueber den Abstand sqrt(3) a/4 mit Minimalbild bestimmt und gegen die Schluessel-Nachbarn verglichen.
- Ein Schritt: Nachbarzahl je Kandidat ueber np.unique der 4 verschobenen Schluessel; neuer Zustand 1, wenn (tot und
  Zahl in B) oder (lebend und Zahl in S).

## 2. Regelraum

- B Teilmenge von {1,2,3,4}, S Teilmenge von {0,...,4}: 16 x 32 = 512 Regeln (Karte). Index = bmaske*32 + smaske.
- [K3] STRATEGIE-SPIN, Weg 4 nennt 1024 Regeln (mit B0); die Karte schraenkt auf 512 ein. Es gilt die Karte.
- Alle 512 werden gerechnet, auch die nach Abschnitt 4 trivialen (sie dienen als Kontrollen Z1, Z2).

## 3. Schreibtisch vor der Rechnung [M]

- **M1 (B1-Regeln, 256 Stueck):** Jedes endliche, nicht leere Muster waechst in jeder Richtung unbegrenzt.
  - Beweisskizze: Fuer eine generische Richtung f sei x* der lebende Knoten mit groesstem f. Waehle den Strich e mit
    groesstem f(e) (bei B-Knoten unter den -e_b). Der Nachbar y = x* + e hat ausser x* nur Nachbarn mit f > f(x*),
    die tot sind; also genau 1 lebenden Nachbarn und wird geboren. Damit steigt max f in jedem Schritt.
  - Folge: In B1-Regeln gibt es weder Stilleben noch Oszillatoren noch Gleiter; jede Saat endet in "gross".
- **M2 (B leer, 32 Regeln):** Ohne Geburten nimmt die Menge lebender Knoten nie zu. Jeder Verlauf endet tot oder als
  Stilleben; keine Oszillatoren mit p > 1, keine Gleiter.
- **M3 (Lichtkegel; Kartenpunkt K1):**
  - Ueber zwei Schritte (A -> B -> A) kann sich ein Signal hoechstens um e_a - e_b bewegen. Fuer jede Richtung n gilt
    fuer die Hoehenfunktion M(t+2) <= M(t) + max_ab (e_a - e_b).n (Rekursion ueber die hoechsten A- und B-Knoten).
  - Folge: Jeder Gleiter erfuellt d/p in K = {abs(x)+abs(y)+abs(z) <= 2, max abs(x_i) <= 1} (in a/4 je Schritt),
    einem Kuboktaeder mit Ecken in den <110>-Richtungen.
  - In Einheiten der Karte (c = ein Strich je Schritt = sqrt(3) a/4) ist die hoechste Geschwindigkeit
    - laengs <110> (Flaechendiagonalen): sqrt(2/3) c = 0,816 c,
    - laengs <111> (Strichrichtungen +-e_a): 2/3 c = 0,667 c,
    - laengs <100> (Wuerfelachsen): 1/sqrt(3) c = 0,577 c.
  - **K1 (Kartenfehler):** "Grenzgeschwindigkeit c = ein Strich je Schritt" ist keine erreichbare Grenze. Ein Muster
    kann nicht zwei Schritte nacheinander laengs desselben Strichs laufen, weil A die Striche +e_a und B die Striche
    -e_a benutzt. Die echte Grenze ist richtungsabhaengig (oben) und liegt immer unter c.
  - Berichtigung: keine Aenderung der Urteilsregel. Die Karte legt LD2 ausdruecklich in ihrer Einheit fest
    ("v <= c/2"), also bleibt das Urteil nach Kartenwortlaut das Haupturteil. Zusaetzlich melde ich beschreibend
    die Lesart nach Life-Konvention: f = Anteil an der Lichtkegelgeschwindigkeit der eigenen Richtung,
    f = max((abs(dx)+abs(dy)+abs(dz))/(2p), max abs(d_i)/p).
  - Bedeutung von c/2 nach M3: 61 % der Hoechstgeschwindigkeit laengs <110>, 75 % laengs <111>, 87 % laengs <100>.
- **M4 (Kartenpunkt K2, Praezisierung):** Der Kartensatz "Muster aus nur einem Untergitter liegt nach einem Schritt
  nur auf dem anderen" gilt nur fuer 0 nicht in S. Mit 0 in S ueberleben die Knoten des alten Untergitters.
- **M5:** Nach M1 und M2 koennen Gleiter nur in den 7 x 32 = 224 Regeln mit leerem 1-Anteil und B nicht leer
  (B Teilmenge von {2,3,4}) vorkommen.
- **M6 (Drehung = halbe Periode):** Gilt R(Phase k) = Phase k + p/2 mit R der Ordnung m, so folgt m p/2 = 0 mod p,
  also m gerade. In der Tetraedergruppe T (12 Drehungen: E, 8 x C3 um <111>, 3 x C2 um <100>) haben nur die C2
  gerade Ordnung. "Drehung um die Laufachse = halbe Periode" ist mit T-Drehungen also nur fuer Gleiter laengs <100>
  moeglich. Um <111> kann eine C3 hoechstens einer Drittelperiode entsprechen.
- **[L] Bezug:** Bei Conways Leben (Moore-Nachbarschaft) sind die schnellsten endlichen Raumschiffe c/2 orthogonal
  und c/4 diagonal; c meint dort den Lichtkegel der Richtung (Schachbrettmetrik), also die Life-Konvention f.
  Leben in 3D auf dem kubischen Gitter mit 26 Nachbarn (Bays, ab 1987) kennt Gleiter, z. B. in 4555 [L?].
  Zu Leben auf dem Diamantgitter kenne ich keine Arbeit [L?].

## 4. Suche (Festlegungen [F])

- **Saaten [F7]:** Startbereich 2 x 2 x 2 kubische Zellen = Kartesisch [0, 8)^3 in a/4, 64 Knoten (32 A, 32 B).
  Jeder Knoten lebt mit Wahrscheinlichkeit rho; rho in {0,25; 0,4; 0,6}, je 16 Saaten, also 48 je Regel.
  Dieselben 48 Startmuster fuer jede Regel (numpy default_rng([380438, Dichteindex, Saatindex])).
- **Verlauf je Saat:** bis T = 256 Schritte. Abbruch bei
  - tot (keine lebenden Knoten);
  - Formwiederkehr: Kennung (Abschnitt 5) schon gesehen bei t0. Dann p = t - t0, d = Verschiebung der Bezugsecke.
    d = 0, p = 1: Stilleben; d = 0, p > 1: Oszillator; d != 0: Gleiter (ganzes Muster);
  - gross: mehr als C_max = 600 lebende Knoten (Wachstum bzw. Chaos im Sinn der Karte);
  - offen: T erreicht.
- **Objekte [F1]:** Damit Gleiter neben Truemmern gefunden werden:
  - Zerlegung des Musters in Haufen: Einzelverknuepfung bei Abstand <= R = 6 a/4. Verschiedene Haufen liegen damit
    mindestens 5 Striche auseinander und beeinflussen sich mindestens 2 Schritte lang nicht [M].
  - Zerlegt wird an den Pruefpunkten t = 64, 128, 192 (nur bei mindestens 2 Haufen) und am Ende bei gross, offen und
    Gleiter.
  - Jeder Haufen mit hoechstens C_iso = 300 Knoten wird **allein** weitergerechnet, T_iso = 128 Schritte, gleiche
    Abbruchregeln. Ergebnis je Regel zwischengespeichert nach Kennung.
  - Erkennt dieser Einzellauf Formwiederkehr mit d != 0, ist der Haufen ein Gleiter der Regel.
- **Gleiter-Pruefung:** Nach Erkennung werden p Schritte weitergerechnet; die Folgephase muss dieselbe Kennung und die
  Verschiebung d haben ("geprueft"). Kennung des Gleiters = kleinste Kennung unter seinen p Phasen.
- **Grenzen (offengelegt):**
  - Perioden bis 128 minus Einschwingzeit (Objekte), bis 256 minus Einschwingzeit (ganzes Muster).
  - Groessen bis 300 (Objekte) bzw. 600 Knoten (ganzes Muster).
  - Nur Gleiter, die aus einer der 48 Saaten binnen 256 Schritten entstehen und sich an einem Pruefpunkt oder am Ende
    abgetrennt haben. Seltene Gleiter, groessere Startbereiche, laengere Laeufe: nicht abgedeckt.
  - Die Suche findet Gleiter, sie beweist ihre Abwesenheit nicht.
- **Laufzeitregel [F8], vor jedem Rauchlauf festgelegt:** Rauchlauf an 9 Regeln: Indizes 0 (B/S), 31 (B/S01234),
  64 (B2/S), 66 (B2/S1), 140 (B3/S23), 204 (B23/S23), 268 (B4/S23), 396 (B34/S23) und die B1-Regel 33 (B1/S0).
  Hochrechnung = mittlere Zeit je Regel der 8 Nicht-B1-Regeln x 256 + Zeit der B1-Regel x 256. Liegt sie ueber
  45 min, gilt mechanisch T = 128 und 12 Saaten je Dichte (sonst nichts geaendert). Bloecke je hoechstens 480 s
  Rechenzeit (Abbruch im Skript vor der naechsten Regel), Fortsetzung im naechsten Block.

### 4.1 Rauchlaeufe und Revision F8 (vor dem Einfrieren, offengelegt)

- Zeiten .69 (UTC): Kontrolle 05:22:47 bis 05:22:49; rauch1 (9 Regeln nach F8) 05:22:59 bis 05:23:01;
  rauch2 (Stufe-2-Codepfad, 5 Regeln) 05:25:27 bis 05:25:30; rauch3 (vergroesserte Stufe 2, 3 Regeln) 05:26:07 bis
  05:26:12. Alle rc = 0, Spur cpu7.
- **Gesehen (offengelegt):**
  - Kontrolle: LD0 (a), (b), (c) und Z0 bestanden (rauch-69/kontrolle.json).
  - rauch1, 48 Saaten: B/S alle tot; B/S01234 alle Stilleben; B2/S 42 tot, 6 Oszillator; B2/S1 29 tot, 19 Stilleben;
    B3/S23 41/7 tot/Stilleben; B23/S23 6 tot, 42 Oszillator; B4/S23 43/5; B34/S23 41/7; B1/S0 alle gross.
    Kein Gleiter. Laufzeit 0,6 s fuer 9 Regeln.
  - rauch2/rauch3 (Stufe-2-Saaten, Regeln B2/S, B2/S0, B2/S1, B3/S234, B234/S01234): kein Gleiter; B234/S01234 mit
    47 von 960 Saaten "gross" (grosse Startbereiche). 0,3 bis 1,9 s je Regel.
- **Hochrechnung F8:** 8 Nicht-B1-Regeln im Mittel 0,047 s, B1-Regel 0,24 s; 512 Regeln etwa 74 s. Weit unter 45 min,
  also bleibt Stufe 1 wie geplant (T = 256, 48 Saaten).
- **Revision F8 (Begruendung: Laufzeit, nicht Ausgang):** Weil die geplante Suche nur gut eine Minute kostet, kommt vor
  dem Einfrieren eine Stufe 2 hinzu. Die Kartenschwellen und Urteilsregeln bleiben unveraendert. Die Erweiterung
  erhoeht nur die Trennschaerfe der Suche. Sie folgt aus der Laufzeit und ist offengelegt, weil ich die
  Rauchergebnisse (kein Gleiter in 12 Regeln) schon kannte.
  - **Stufe 2:** nur die 224 Regeln aus M5 (B Teilmenge von {2,3,4}, nicht leer). Je Regel 960 weitere Saaten,
    gleiche Dichten, gleiches T und gleiche Schranken:
    - 600 im Bereich 2 x 2 x 2 (Saatindex 16 bis 215),
    - 300 im Bereich 3 x 3 x 3 Zellen (216 Knoten),
    - 60 im Bereich 4 x 4 x 4 Zellen (512 Knoten).
  - Die Saaten sind nach Lage verzahnt. Zeitkappe 6 s je Regel: Danach werden die restlichen Saaten uebersprungen und
    gezaehlt.
  - Gespeichert werden nur Klassenzaehler und die Saaten mit Gleitern.
  - Die Bereiche 3 und 4 koennen die Schranke C_max = 600 schon durch Fuellen ueberschreiten. Deshalb stammt die
    Klassenkarte nur aus Stufe 1.
- **Urteilsgrundlage:**
  - Haupturteil: Gleiter aus Stufe 1 und Stufe 2 zusammen.
  - Zusaetzlich gebe ich das Urteil nur auf Stufe 1 an, also im urspruenglichen Umfang.
  - Ist Stufe 2 nicht vollstaendig gerechnet, gilt das Haupturteil auf dem gerechneten Teil, mit Vermerk.

## 5. Einordnung und Kennzahlen [F]

- **Kennung:** lebende Knoten als Schluessel minus Bezugsecke (komponentenweises Minimum von n1, n2, n3), sortiert.
  Verschiebungen sind fcc-Gittervektoren; das Untergitterbit bleibt Teil der Kennung.
  - Eine Verschiebung um (1,1,1) (A -> B) ist keine Gittersymmetrie (B + (1,1,1) ist kein Knoten). Die Kennung
    unterscheidet daher ein A-Muster von seiner B-Kopie. Untergitterwechsel kommen nur ueber echte Symmetrien
    (Bindungsmitten-Inversion) vor; die werden in Abschnitt 6 gesondert geprueft.
- **Geschwindigkeit [F2]:** d_kart = d1 A1 + d2 A2 + d3 A3 (a/4). v/c = abs(d_kart)/(p sqrt(3)).
  Life-Lesart f (Abschnitt 3, M3).
- **Richtung [F3]:** d_kart durch ggT, Betraege sortiert: <111> Strichrichtung (+e_a bei gerader Zahl von
  Minuszeichen, -e_a sonst), <100> Wuerfelachse, <110> Flaechendiagonale, sonst <hkl> "andere".
- **Groesse:** kleinste und groesste Knotenzahl ueber die Phasen.
- **Regelklasse (Vorrang):** Gleiter > Wachstum (eine Saat gross) > offen (eine Saat offen mit ungeklaertem Haufen)
  > Oszillator > Stilleben > ausgestorben.

## 6. Drehverhalten [F]

- Gruppe: die 24 Elemente von Td (vorzeichenbehaftete Permutationen, die {e_a} auf sich abbilden; ungerade Zahl von
  Vorzeichenwechseln faellt dabei heraus). Darunter die 12 Drehungen der Tetraedergruppe T (Determinante +1).
  Dazu je Element die Bindungsmitten-Inversion x -> (1,1,1) - x (tauscht A und B): 48 Elemente, beschreibend.
- Fuer jeden Gleiter G und jedes Element g: Bild g(Phase 0), Kennung.
  - "selbst": Kennung unter den Phasen von G; Phasenversatz k; Pruefung L d = d (L = linearer Teil).
  - "anderer": Kennung eines anderen gefundenen Gleiters derselben Regel (andere Richtung).
  - "nicht gefunden": Bild ist nach Symmetrie ein Gleiter, wurde aber in der Suche nicht gefunden.
- Bahn (Symmetrieklasse): kleinste Kennung ueber alle 48 Bilder aller Phasen. Gleiter einer Bahn sind dieselbe Art.
- Beschreibend: Gibt es g != E mit g(Phase 0) = Phase p/2 und L d = d (Drehung um die Laufachse = halbe Periode)?
  Getrennt fuer die 12 Drehungen von T und fuer die uebrigen Elemente.

## 7. Vorhersagen (Karte, unveraendert) und Urteilsregeln

| Nr | Vorhersage (Karte) | Wahrsch. | Urteilsregel [F] |
|---|---|---|---|
| LD0 | Kontrolle: Gitter korrekt (4 Nachbarn, bipartit); B leer und S = {0..4} haelt jedes Muster fest; die Einordnung erkennt eingesetzte Kunstmuster (verschobene Kopie) richtig | 90 % | eingetroffen, wenn (a), (b) und (c) unten alle bestehen; sonst nicht eingetroffen |
| LD1 | [H] Mindestens eine der 512 Regeln hat einen Gleiter, der aus Zufallsstarts entsteht | 50 % | eingetroffen bei mindestens einem geprueften Gleiter (Abschnitt 4) in mindestens einer Regel; sonst nicht eingetroffen |
| LD2 | [H] Falls Gleiter gefunden werden: alle sind hoechstens halb so schnell wie die Grenzgeschwindigkeit (v <= c/2) | 70 % | ohne Gleiter: nicht auswertbar. Sonst eingetroffen, wenn max v/c <= 0,5 + 1e-9 (c = ein Strich je Schritt, Kartenwortlaut) |
| LD3 | [H] Falls Gleiter gefunden werden: Die schnellsten laufen laengs einer Tetraeder-Strichrichtung oder ihrer Gegenrichtung | 45 % | ohne Gleiter: nicht auswertbar. "Die schnellsten" = alle Gleiter (ueber alle Regeln) mit v/c >= v_max (1 - 1e-9). Eingetroffen, wenn alle davon Richtung <111> (+e_a oder -e_a) haben; sonst nicht eingetroffen |

- **LD0 im Einzelnen:**
  - (a) Kubischer Kasten L = 3: 216 Knoten; jeder Grad genau 4; jede Kante verbindet A mit B; BFS-Zweifaerbung ohne
    Konflikt und gleich der Untergitterfaerbung; Schluessel-Nachbarn = Abstandsnachbarn und = +e_a (A) bzw. -e_a (B)
    an allen Knoten.
  - (b) B leer, S = {0,...,4}: alle 48 Saaten und 20 weitere Zufallsmuster bleiben 5 Schritte lang identisch und
    werden als Stilleben (p = 1, d = 0, t = 1) eingeordnet.
  - (c) Kunstfolgen (vorgegebene Phasen, je Periode um d verschobene Kopie, teils mit Vorlauf aus Zufallsmustern):
    7 Faelle (Gleiter p = 3, 1, 5, 2, 7 mit verschiedenen d; Oszillator p = 4; Stilleben). Alle muessen mit
    richtiger Klasse, richtigem p und d erkannt werden. Dazu Kennung verschiebungsfrei (100 von 100), A-Muster von
    B-Kopie unterschieden (100 von 100), Zerlegung trennt zwei entfernte Haufen (2) und vereint zwei nahe (1).
- **Zusatzkontrollen (keine Kartenvorhersagen, aber Sperren):**
  - Z0 (d, e): Schritt gleichverhaltend unter allen 48 Symmetrien und unter fcc-Verschiebungen (8 Regeln, je 4 Muster);
    Lichtkegel aus einem Knoten unter B1234/S01234: max(abs(x)+abs(y)+abs(z)) = 2t und max abs(x_i) = t bei geradem t.
  - Z1: alle 256 B1-Regeln: jede Saat "gross", kein Gleiter (M1).
  - Z2: alle 32 B-leer-Regeln: jede Saat tot oder Stilleben (ganzes Muster), kein Oszillator, kein Gleiter (M2).
  - Z3: jeder Gleiter "geprueft" und d/p in K (M3).
- **Sperre [F6]:** Besteht LD0 nicht, oder scheitert Z0, Z1, Z2 oder Z3, oder sind nicht alle 512 Regeln gerechnet,
  dann sind LD1 bis LD3 "nicht auswertbar" (mit Vermerk).
- **Nebenlesarten (beschreibend, nicht geurteilt):** LD2 nach Life-Konvention (max f <= 0,5); LD3 je Regel (Anteil der
  Gleiter-Regeln, deren schnellster Gleiter <111> laeuft) und nach f statt v/c.

## 8. Eigene Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Z1 haelt (M1) | 99 % |
| A2 | Z2 haelt (M2) | 99 % |
| A3 | Z3 haelt (M3) | 99 % |
| A4 | LD1 eingetroffen | 60 % |
| A5 | Alle Gleiter nur in Regeln mit 2 in B | 60 % |
| A6 | Falls Gleiter: LD2 eingetroffen (Life-Analogie: hoechstens halbe Lichtkegelgeschwindigkeit, also <= 0,41 c) | 75 % |
| A7 | Falls Gleiter: die schnellsten laufen laengs <110> (Flaechendiagonalen; dort ist der Lichtkegel am weitesten) | 45 % |
| A8 | Falls Gleiter: LD3 eingetroffen | 30 % |

## 9. Ablauf und Abgabe

- Rauchlaeufe (vor dem Einfrieren, offengelegt): Kontrolle (LD0, Z0) und 8 Regeln nach F8, nur fuer Laufzeit.
- Einfrieren: PLAN.md.eingefroren-JJJJMMTT-HHMMSS, sha256 von Plan und Code in EINGEFROREN-SHA256.txt.
- Hauptlaeufe: Kontrolle, dann die 512 Regeln in Bloecken; dann code/auswertung.py -> lauf-69/auswertung.json,
  regeln.tsv, gleiter.json, Bilder (Klassenkarte, Geschwindigkeiten, Gleiter 3D).
- Code nach dem Einfrieren nur bei echten Fehlern aendern, offenlegen.
- Zeitgruende: code/auswertung.py entsteht nach diesem Einfrieren, waehrend die Hauptlaeufe rechnen. Deren Ausgaben
  gehen nur in Logdateien auf der .69; ich lese sie erst, wenn auswertung.py geschrieben und mit eigenem Stempel
  (auswertung.py.eingefroren-*, sha256 in EINGEFROREN-SHA256.txt) eingefroren ist. auswertung.py setzt nur die
  Urteilsregeln aus Abschnitt 7 und 4.1 um.
