# LIFE-FCC-1: Plan (Runde 38, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 07:59:00 CEST, Plantext ab 08:15 CEST (date).
- Karte: KARTE.md (unveraendert). Vorhersagen LF0 bis LF3 und ihre Schwellen sind unten woertlich uebernommen.
- Kennzeichen: [M] eigene Mathematik (Schreibtisch), [F] Festlegung dieses Plans (Karte laesst es offen), [K] Kartenpunkt,
  [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese, [E] gerechnet (erst im Ergebnis).
- Rechnen nur auf der .69, Spur cpu7, ueber kleintest.sh; Ordner /home/fmh/fmhc-physics-remote/runde38-life-fcc/.
- Code: code/life_fcc.py, umgebaut aus RUNDE-37/life-diamant-1/code/life_diamant.py.
- Synthetische Rechnung. Kein Messdatenbezug; Ergebnisse sind keine Messdatenbestaetigung.

## 1. Gitter und Darstellung

- **Knoten:** ganzzahlige (x, y, z) mit gerader Summe, Einheit a/2 (a = kubische Zellkante). Nachbarabstand sqrt(2).
- **Nachbarn:** die 12 Vektoren (+-1, +-1, 0) und Vertauschungen, die Ecken eines Kuboktaeders.
- **Darstellung [F]:** wie LIFE-DIAMANT-1 duennbesetzt, sortierte int64-Schluessel, unbegrenztes Gitter, kein
  periodischer Kasten.
  - Schluessel = (Saat << 48) | (x + 2^15) << 32 | (y + 2^15) << 16 | (z + 2^15).
  - **Saaten als Stapel [F]:** Alle Saaten einer Regel laufen in einem Array. Die Saatnummer steht in den oberen Bits;
    Nachbarverschiebungen erreichen sie nie, weil abs(x), abs(y), abs(z) < 2^15 bleiben.
  - Ein numpy-Schritt rechnet damit alle Saaten zugleich. Beendete Saaten (tot, gross, Formwiederkehr) werden sofort
    aus dem Stapel genommen.
  - Kontrolle Z0 (f): Stapellauf und Einzellaeufe muessen Saat fuer Saat gleich ausgehen.
- **Schritt:** Nachbarzahl je Kandidat ueber Sortieren der 12 verschobenen Schluessel; neuer Zustand 1, wenn (tot und Zahl
  in B) oder (lebend und Zahl in S).

## 2. Regelraum

- B = [b1..b2] mit 1 <= b1 <= b2 <= 12 (78 Intervalle), S = [s1..s2] mit 0 <= s1 <= s2 <= 12 (91 Intervalle):
  7098 Regeln (Karte). Index = bi * 91 + si (bi, si in lexikografischer Reihenfolge von (b1, b2) bzw. (s1, s2)).
- Alle 7098 werden gerechnet, auch die nach Abschnitt 3 gleiterfreien (sie dienen als Kontrollen Z1, Z2, Z4).
- **Zusatz [F, nicht geurteilt]:** die 78 Regeln B = [b1..b2] mit S leer (Index 7098 bis 7175), siehe K2. Nur wenn nach
  Stufe 2 Zeit bleibt; beschreibend.

## 3. Schreibtisch vor der Rechnung [M]

- **M1 (B1-Regeln, b1 = 1: 12 x 91 = 1092 Regeln):** Jedes endliche, nicht leere Muster waechst in jede Richtung mit
  Lichtgeschwindigkeit; es stirbt nie aus.
  - Beweis: Fuer eine generische Richtung f sei x* der lebende Knoten mit groesstem f und e der Nachbarvektor mit
    groesstem f(e). y = x* + e hat ausser x* nur Nachbarn y - e' mit f > f(x*), die tot sind. y hat also genau 1 lebenden
    Nachbarn und wird geboren; max f steigt in jedem Schritt um f(e).
  - Folge: In B1-Regeln gibt es weder Stilleben noch Oszillatoren noch Gleiter.
- **M2 (S = [0..12], 78 Regeln):** Lebende Knoten sterben nie; die Menge waechst monoton.
  - Ein endliches Muster, das in Form wiederkehrt (P(t+p) = P(t) + d) und zugleich P(t) enthaelt, hat d = 0 und
    P(t+p) = P(t).
  - Folge: keine Oszillatoren mit p > 1, keine Gleiter; nur tot (unmoeglich bei nicht leerem Start), Stilleben, gross
    oder offen.
- **M3 (Lichtkegel):**
  - Je Schritt waechst ein Muster hoechstens um einen Nachbarvektor. Die Huelle der 12 Vektoren ist das Kuboktaeder
    K = {abs(x)+abs(y)+abs(z) <= 2, max abs(x_i) <= 1} (a/2 je Schritt).
  - Jeder Gleiter erfuellt d/p in K. Der Graphabstand im fcc-Netz ist genau die K-Norm max((abs(x)+abs(y)+abs(z))/2,
    max abs(x_i)).
  - In Einheiten c = eine Nachbarkante (sqrt(2) a/2) je Schritt ist die Hoechstgeschwindigkeit
    - laengs <110> (Nachbarrichtungen): 1 c,
    - laengs <111> (Raumdiagonalen): sqrt(2/3) c = 0,816 c,
    - laengs <100> (Wuerfelachsen): 1/sqrt(2) c = 0,707 c.
  - **Lichtkegelanteil** f = Geschwindigkeit / Hoechstgeschwindigkeit der eigenen Richtung
    = max((abs(dx)+abs(dy)+abs(dz))/(2p), max abs(d_i)/p). Das ist die Groesse der Karte in LF2.
- **M4 (Huelle, b1 >= 7: 21 x 91 = 1911 Regeln):** Ein Knoten ausserhalb der konvexen Huelle des lebenden Musters hat
  hoechstens 6 lebende Nachbarn.
  - Beweis: Seine lebenden Nachbarn liegen in einem offenen Halbraum durch ihn. Von den 12 zentralsymmetrischen
    Kuboktaederecken liegen dort hoechstens 6.
  - Folge: Bei b1 >= 7 gibt es ausserhalb der Huelle keine Geburt. Die Huelle schrumpft oder bleibt; kein Wachstum ueber
    den Startbereich hinaus und kein Gleiter.
- **M5 (Kandidaten):** Nach M1, M2 und M4 koennen Gleiter nur bei 2 <= b1 <= 6 und S != [0..12] vorkommen:
  45 x 91 - 45 = 4050 Regeln.
- **M6 (Drehung = Phasenversatz):** Bildet ein Element g der Ordnung m Phase 0 auf Phase k ab (bei L d = d), so gilt
  m k = 0 mod p. Halbe Periode (k = p/2) verlangt also gerade Ordnung.
  - In O (24 Drehungen) haben C2, C2' und C4 gerade Ordnung; in T (12) nur die C2 um die Wuerfelachsen.
- **[L] Bezug:**
  - Bei Conways Leben (Moore-Nachbarschaft) sind die schnellsten endlichen Raumschiffe c/2 orthogonal und c/4
    diagonal (Lichtkegel der Richtung).
  - Leben in 3D auf dem kubischen Gitter mit 26 Nachbarn (Bays, ab 1987) kennt Gleiter, z. B. in 4555 und 5766 [L?].
  - Ob Bays auch das fcc-Netz (Rhombendodekaeder-Zellen, 12 Nachbarn) untersucht hat, weiss ich nicht sicher [L?].

## 4. Suche (Festlegungen [F])

- **Saaten Stufe 1 [F]:** Startbereich Wuerfel [0, 5)^3 mit 63 Knoten. Jeder Knoten lebt mit Wahrscheinlichkeit rho;
  rho in {0,15; 0,3; 0,45; 0,6}, je 6 Saaten, also 24 je Regel (Karte: 16 bis 32).
  - Fuer jede Regel dieselben Startmuster (numpy default_rng([380441, Dichteindex, Saatindex])).
- **Verlauf je Saat:** bis T = 256 Schritte. Abbruch bei
  - tot (keine lebenden Knoten);
  - gross: mehr als C_max = 600 lebende Knoten (Wachstum bzw. Chaos im Sinn der Karte; Wachstumsabbruch);
  - Formwiederkehr: Kennung (Abschnitt 5) schon gesehen bei t0. Dann p = t - t0, d = Verschiebung der Bezugsecke.
    d = 0, p = 1: Stilleben; d = 0, p > 1: Oszillator; d != 0: Gleiter (ganzes Muster);
  - offen: T erreicht oder Zeitkappe.
- **Zeitkappe je Regel [F]:** Knotenschritt-Budget statt Uhrzeit (reproduzierbar).
  - Stapel der Saaten: W1 = 1 500 000 Knotenschritte (Summe der lebenden Knoten ueber alle Schritte).
  - Einzellaeufe der Objekte: W1_obj = 600 000.
  - Danach enden alle noch laufenden Saaten bzw. Objekte als offen (gekappt) zum Zeitpunkt t der Kappe.
  - Hoechstens 400 verschiedene Objekte je Regel. Weitere werden als "verworfen" gezaehlt.
- **Objekte [F]:** Damit Gleiter neben Truemmern gefunden werden, wie LIFE-DIAMANT-1:
  - Zerlegung in Haufen: Einzelverknuepfung bei euklidischem Abstand <= R = 4,5 (a/2).
  - Verschiedene Haufen haben damit K-Abstand >= 4 [M]. Sie beeinflussen sich mindestens einen Schritt lang nicht.
  - Zerlegt wird an den Pruefpunkten t = 64, 128, 192 (nur bei mindestens 2 Haufen) und am Ende bei offen und Gleiter.
  - **Abweichung von LIFE-DIAMANT-1 [F]:** Ein gross-Ende wird nicht zerlegt.
    - Grund: Laufzeit; Tausende explodierende Regeln, je Muster mehrere Millisekunden.
    - [H]: Aus einer Explosion, deren Front sich mit fast Lichtgeschwindigkeit ausbreitet, entkommt ein langsamerer
      Gleiter kaum. Langsam wachsende Muster werden an den Pruefpunkten zerlegt.
  - Jeder Haufen mit hoechstens C_iso = 300 Knoten wird **allein** weitergerechnet: T_iso = 128 Schritte, gleiche
    Abbruchregeln, als Stapel aller Objekte der Regel. Ergebnis je Regel nach Kennung zwischengespeichert.
  - Erkennt dieser Einzellauf Formwiederkehr mit d != 0, ist der Haufen ein Gleiter der Regel.
- **Gleiter-Pruefung:** Nach Erkennung werden p Schritte weitergerechnet; die Folgephase muss dieselbe Kennung und die
  Verschiebung d haben ("geprueft"). Kennung des Gleiters = kleinste Kennung unter seinen p Phasen.
- **Stufe 2 [F] (Karte: Regeln mit kleinen, langlebigen Mustern, weder Aussterben noch Wachstum):**
  - **Auswahlregel (vor dem Einfrieren, mechanisch aus Stufe 1):**
    - Je Regel zaehle ich die "klein-langlebigen" Saaten: Endklasse Stilleben, Oszillator, offen oder Gleiter
      (weder tot noch gross), Endgroesse <= 200 Knoten und Endzeit t >= 8 (nicht sofort erstarrt).
    - Kandidat: mindestens eine solche Saat, b1 != 1 und S != [0..12] (M1, M2). M4-Regeln (b1 >= 7) bleiben Kandidaten;
      sie dienen dort als Kontrolle.
    - Rangfolge: Zahl der klein-langlebigen Saaten absteigend, dann Regelindex aufsteigend; hoechstens N2 = 400 Regeln (Obergrenze in 4.1 vor dem Einfrieren aufgehoben).
  - **Saaten Stufe 2:** je Regel 96 neue Saaten, gleiche Dichten:
    - 48 im Bereich [0, 5)^3 (63 Knoten, andere Zufallszahlen als Stufe 1),
    - 32 im Bereich [0, 7)^3 (172 Knoten),
    - 16 im Bereich [0, 9)^3 (365 Knoten).
  - Gleiches T, C_max, Objekte und Pruefung. Kappen W2 = 6 000 000 (Stapel), W2_obj = 1 500 000 (Objekte).
  - Die Bereiche 7 und 9 koennen C_max schon durch Fuellen ueberschreiten. Die Klassenkarte stammt deshalb nur aus
    Stufe 1.
- **Grenzen (offengelegt):**
  - Perioden bis 256 minus Einschwingzeit (ganzes Muster), bis 128 minus Einschwingzeit (Objekte); bei Kappe weniger.
  - Groessen bis 600 Knoten (ganzes Muster) bzw. 300 (Objekte).
  - Nur Gleiter, die aus einer der Saaten binnen 256 Schritten entstehen und sich an einem Pruefpunkt oder am Ende
    abgetrennt haben.
  - Die Suche findet Gleiter; ihre Abwesenheit beweist sie nicht.
- **Laufzeitregel [F], vor dem Laufzeit-Rauchlauf festgelegt:**
  - Rauchlauf an der festen Stichprobe der 20 Regeln mit Index 355 k (k = 0..19), Stufe 1 wie geplant.
  - Hochrechnung H1 = mittlere Zeit je Regel x 7098.
  - H1 <= 30 min: Stufe 1 wie geplant.
  - 30 < H1 <= 60 min: 4 Saaten je Dichte (16 je Regel), sonst nichts geaendert.
  - H1 > 60 min: 16 Saaten und W1, W1_obj halbiert.
  - Bloecke je hoechstens 540 s Rechenzeit (Abbruch im Skript vor der naechsten Regel). Fortsetzung im naechsten Block
    an der ersten nicht gerechneten Regel.
  - Stufe 2 laeuft in Rangfolge in hoechstens zwei Bloecken. Nicht erreichte Regeln werden als nicht gerechnet
    gemeldet.

### 4.1 Rauchlaeufe und Revision N2 (vor dem Einfrieren, offengelegt)

- Zeiten .69 (UTC): Kontrolle 06:15:35 bis 06:15:37; rauch1 (20 Stichprobenregeln 355 k) 06:17:30 bis 06:17:31.
  Beide rc = 0, Spur cpu7. Der Code war dabei derselbe wie beim Einfrieren, bis auf PARAM N2_max (400, jetzt None).
- **Gesehen (offengelegt):**
  - Kontrolle: LF0 (a), (b), (c) und Z0 (d), (e) bestanden (rauch-69/kontrolle.json). Durchgangsprobe: je Typ 4 von 4
    Gleitern mit erwartetem p, d, Richtung und f = 1; Quellen "ganz" und "objekt".
  - rauch1, 24 Saaten je Regel: 9 Regeln Wachstum (alle 4 B1-Regeln der Stichprobe mit 24 von 24 gross), 5
    ausgestorben, 2 Stilleben, 4 Oszillator (Perioden 2 und 4). Kein Gleiter, keine Kappe. Hoechste Stufe-2-Zahl 17
    (B4-6/S0-10).
  - Laufzeit 0,4 s fuer 20 Regeln, also H1 = 0,02 s x 7098 = etwa 2,4 min.
- **Laufzeitregel:** H1 <= 30 min, also Stufe 1 wie geplant (24 Saaten, T = 256, W1 und W1_obj unveraendert).
- **Revision N2 (Begruendung: Laufzeit, nicht Ausgang):** Weil Stufe 1 nur Minuten kostet, faellt die Obergrenze
  N2 = 400 weg.
  - Stufe 2 rechnet alle Kandidaten der Auswahlregel in der festgelegten Rangfolge, soweit zwei Bloecke zu je 540 s
    reichen. Nicht erreichte Kandidaten werden gemeldet.
  - Auswahlregel, Rangfolge, Saaten, Kappen und alle Urteilsregeln bleiben unveraendert.
  - Ich kannte dabei das Rauchergebnis (kein Gleiter in 20 Stichprobenregeln).
- Der Zusatz S leer (K2) laeuft nach Stufe 2 in einem eigenen Block (lauf/zusatz-s-leer.jsonl), wenn die Zeitbox es
  zulaesst; beschreibend.

## 5. Einordnung und Kennzahlen [F]

- **Kennung:** lebende Knoten als Schluessel minus Bezugsecke (komponentenweises Minimum von x, y, z), sortiert.
  Verschiebungen zwischen Mustern sind fcc-Vektoren; Saatbits fallen heraus.
- **Geschwindigkeit:** d kartesisch (a/2). v/c = abs(d) / (p sqrt(2)), c = eine Nachbarkante je Schritt.
  Lichtkegelanteil f (M3).
- **Richtung:** d durch ggT, Betraege sortiert: <110> Nachbarrichtung, <100> Wuerfelachse, <111> Raumdiagonale,
  sonst <hkl> "andere".
- **Groesse:** kleinste und groesste Knotenzahl ueber die Phasen.
- **Saatklassen:** tot, still, osz, gleiter (ganzes Muster), gross, offen.
- **Regelklasse (Vorrang):** Gleiter > Wachstum (eine Saat gross) > offen (eine Saat offen mit ungeklaertem Haufen oder
  gekappt) > Oszillator > Stilleben > ausgestorben.

## 6. Drehverhalten [F]

- Gruppe: Oh, die 48 vorzeichenbehafteten Permutationsmatrizen (alle bilden das fcc-Gitter auf sich ab).
  - Darin O (24 Drehungen des Wuerfels, det = +1) und T (12 Drehungen des Tetraeders {(1,1,1), (1,-1,-1), (-1,1,-1),
    (-1,-1,1)}).
  - Gemeldet wird getrennt fuer O, T und alle 48.
- Fuer jeden Gleiter G und jedes Element g: Bild g(Phase 0), Kennung.
  - "selbst": Kennung unter den Phasen von G; Phasenversatz k; Pruefung L d = d.
  - "anderer": Kennung eines anderen gefundenen Gleiters derselben Regel (andere Richtung).
  - "nicht gefunden": Das Bild ist nach Symmetrie ein Gleiter, wurde aber in der Suche nicht gefunden.
- Stabilisator: alle g mit Bild "selbst" und L d = d; Bahngroesse = 48 / Stabilisatorgroesse (Zahl der Lagen).
- Bahn (Gleiterform): kleinste Kennung ueber alle 48 Bilder aller Phasen. Gleiter einer Bahn sind dieselbe Form, auch
  ueber Regeln hinweg.
- Beschreibend: g != E mit g(Phase 0) = Phase p/2 und L d = d ("Drehung um die Laufachse = halbe Periode"), getrennt
  fuer O, T und die uebrigen Elemente.

## 7. Vorhersagen (Karte, unveraendert) und Urteilsregeln

| Nr | Vorhersage (Karte) | Wahrsch. | Urteilsregel [F] |
|---|---|---|---|
| LF0 | Kontrolle: Gitter korrekt (12 Nachbarn); die Durchgangsprobe mit Kunst-Gleitern findet alle | 90 % | eingetroffen, wenn (a), (b) und (c) unten alle bestehen; sonst nicht eingetroffen |
| LF1 | [H] Mindestens eine Intervallregel hat einen Gleiter, der aus Zufallsstarts entsteht | 60 % | eingetroffen bei mindestens einem geprueften Gleiter (Abschnitt 4, ganzes Muster oder Objekt) in mindestens einer der 7098 Regeln, Stufe 1 und 2 zusammen; sonst nicht eingetroffen |
| LF2 | [H] Falls Gleiter gefunden werden: Alle sind hoechstens halb so schnell wie die Lichtkegelgrenze ihrer Richtung | 60 % | ohne Gleiter: nicht auswertbar. Sonst eingetroffen, wenn max f <= 0,5 + 1e-9 ueber alle Gleiter (f nach M3); sonst nicht eingetroffen |
| LF3 | [H] Falls Gleiter gefunden werden: Es gibt mehr als eine Gleiterform (nicht nur eine Regel mit einem Gleiter) | 50 % | ohne Gleiter: nicht auswertbar. Gleiterform = Bahn (Abschnitt 6) ueber alle Regeln. Eingetroffen bei mindestens 2 verschiedenen Bahnen; sonst nicht eingetroffen |

- **LF0 im Einzelnen:**
  - (a) Gitter:
    - Periodischer kubischer Kasten 8^3 (a/2): 256 Knoten, jeder Grad genau 12 (Abstandsnachbarn mit Minimalbild).
    - Schluessel-Nachbarn = Abstandsnachbarn = die 12 Vektoren, an allen Knoten.
    - Schalen im unbegrenzten Gitter: 12, 6, 24, 12 Knoten bei Abstand^2 = 2, 4, 6, 8.
    - Graphabstand (Breitensuche bis 4) = K-Norm an allen 309 Knoten.
  - (b) Kunstfolgen (vorgegebene Phasen, je Periode um d verschobene Kopie, teils mit Vorlauf aus Zufallsmustern):
    - 7 Faelle: Gleiter p = 3, 1, 5, 2, 7 mit verschiedenen d; Oszillator p = 4; Stilleben.
    - Alle muessen mit richtiger Klasse, richtigem p und d erkannt werden.
    - Dazu Kennung verschiebungsfrei (100 von 100), Zerlegung trennt zwei entfernte Haufen (2) und vereint zwei nahe (1).
  - (c) Durchgangsprobe der ganzen Kette (Stapel, Pruefpunkt-Zerlegung, Objektlaeufe, Gleiterpruefung, Drehverhalten,
    JSON) mit Kunst-Schritten nach LIFE-DIAMANT-1 Fassung 2.
    - Ein Kunst-Schritt bildet jeden Knoten mit z < 1000 auf R x + t ab; die anderen stehen.
    - Drei Kunst-Gleiter: R = 1, t = (1,1,0) (p = 1, d = (1,1,0), <110>); R = zyklische Vertauschung, t = (1,1,0)
      (p = 3, d = (2,2,2), <111>); R = 90 Grad um z, t = (1,0,1) (p = 4, d = (0,0,4), <100>). Alle haben f = 1.
    - Je Typ 4 Saaten: eine reine Laufsaat und drei Laufsaaten mit einem entfernten stehenden Block (z + 2000).
      Laufsaat und Block haben verschiedene Kennungen.
    - Bestanden, wenn je Typ jede Saat mindestens einen Gleiter liefert, alle gefundenen Gleiter das erwartete p, d,
      die Richtung und f = 1 haben und geprueft sind, und unter den Quellen "ganz" und "objekt" vorkommen.
- **Zusatzkontrollen (keine Kartenvorhersagen, aber Sperren):**
  - Z0:
    - (d) Schritt gleichverhaltend unter allen 48 Elementen von Oh und unter fcc-Verschiebungen (8 Regeln, je 4
      Muster); Gruppe 48, davon 24 in O, 12 in T.
    - (d) Stapel = Einzeln: 5 Regeln x 24 Saaten, Klasse, t, p, d und Endmuster gleich.
    - (e) Lichtkegel B1-12/S0-12 aus einem Knoten: nach t = 1..6 genau die Kugel {K-Norm <= t}: 13, 55, 147, 309, 561,
      923 Knoten.
  - Z1: alle 1092 B1-Regeln: keine Saat tot, still, osz oder gleiter; kein Gleiter (M1).
  - Z2: alle 78 Regeln mit S = [0..12]: keine Saat osz oder gleiter, kein Objekt osz oder gleiter, kein Gleiter (M2).
  - Z3: jeder Gleiter "geprueft" und d/p in K, also f <= 1 (M3).
  - Z4: alle 1911 Regeln mit b1 >= 7: keine Saat gross oder gleiter, kein Gleiter (M4).
- **Sperre [F]:** Besteht LF0 nicht, oder scheitert Z0 bis Z4, oder sind nicht alle 7098 Regeln in Stufe 1 gerechnet,
  dann sind LF1 bis LF3 "nicht auswertbar" (mit Vermerk).
- **Stufe 2 unvollstaendig:** Haupturteil auf Stufe 1 plus dem gerechneten Teil von Stufe 2, mit Vermerk. Zusaetzlich
  gebe ich das Urteil nur auf Stufe 1 an.
- **Nebenlesarten (beschreibend, nicht geurteilt):**
  - LF3 nach Kartenklammer: Zahl der Paare (Regel, Bahn) >= 2.
  - LF2 in Karteneinheit c: max v/c.
  - LF2 je Richtungsklasse.

## 8. Kartenpunkte [K] (vor dem Einfrieren)

- **K1 (LF3, mehrdeutig):** "mehr als eine Gleiterform (nicht nur eine Regel mit einem Gleiter)" laesst offen, ob dieselbe
  Form in zwei Regeln als eine oder zwei Formen zaehlt.
  - Festlegung: Form = Bahn unter Oh, Verschiebung und Phase, ueber alle Regeln.
  - Die Lesart der Klammer (Paare Regel/Bahn) melde ich mit. Weichen die beiden Urteile ab, nenne ich beide.
- **K2 (Luecke der Regelklasse):** Die Intervallklasse hat immer S nicht leer. Damit fehlen die "Seeds"-artigen Regeln
  mit S leer, die in 2D besonders viele Raumschiffe tragen [L].
  - Keine Aenderung der Urteile; die 78 Regeln B = [b1..b2], S leer rechne ich nur als Zusatz (Abschnitt 2), wenn Zeit
    bleibt.
- **K3 (Bedeutung LF1):** "bewegte Teilchen mit Hoechstgeschwindigkeit" lese ich als "mit einer Hoechstgeschwindigkeit
  (Lichtkegel)". LF1 wird nur nach Existenz geurteilt.
- **K4 (Drehungen):** Die Symmetriegruppe des fcc-Netzes um einen Knoten ist Oh (48). Die Karte nennt O (24) und T (12);
  ich melde O, T und die 24 Spiegelelemente getrennt.
- **K5 (keine Kartenfehler gefunden):** Regelzahl 2^26 und 78 x 91 = 7098 stimmen. Die richtungsabhaengige Lichtkegelgrenze
  der Karte ist richtig (M3).
  - Sie liegt laengs <110> genau bei einer Nachbarkante je Schritt, sonst darunter.

## 9. Eigene Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Z1 haelt (M1) | 99 % |
| A2 | Z2 haelt (M2) | 99 % |
| A3 | Z4 haelt (M4) | 99 % |
| A4 | LF1 eingetroffen | 60 % |
| A5 | Falls Gleiter: alle in Regeln mit b1 in {3, 4} | 50 % |
| A6 | Falls Gleiter: LF2 eingetroffen | 65 % |
| A7 | Falls Gleiter: LF3 eingetroffen | 55 % |
| A8 | Falls Gleiter: Die schnellsten (nach f) laufen laengs <110> | 40 % |

## 10. Ablauf und Abgabe

- Rauchlaeufe (vor dem Einfrieren, offengelegt): Kontrolle (LF0, Z0) und die 20 Stichprobenregeln nach der
  Laufzeitregel, nur fuer Laufzeit und Kontrollen.
- Einfrieren: PLAN.md.eingefroren-JJJJMMTT-HHMMSS, sha256 von Plan und Code in EINGEFROREN-SHA256.txt.
- Hauptlaeufe: Kontrolle, dann die 7098 Regeln in Bloecken, dann Stufe 2. Danach code/auswertung.py ->
  lauf-69/auswertung.json, regeln.tsv, gleiter.json, Bilder (Klassenkarte, Geschwindigkeiten, Gleiter-Bildfolge).
- Code nach dem Einfrieren nur bei echten Fehlern aendern, offenlegen.
- code/auswertung.py entsteht nach diesem Einfrieren, waehrend die Hauptlaeufe rechnen. Sie wird vor jeder Sicht auf
  Hauptergebnisse mit eigenem Stempel eingefroren und setzt nur die Urteilsregeln aus Abschnitt 7 um.
  - Bis dahin sehe ich von den Hauptlaeufen nur Zeilenzahlen und Logzeilen.
