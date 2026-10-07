# ICO-STAB: Plan (Code-Agent fuer die Leitung claude-primary, Runde 29)

- Abschnitte 1 bis 5 (Modell, Laeufe, Messgroessen, Urteile, Kontrollen) geschrieben ab 2026-10-03 07:28:22 CEST (date).
  Die Rauchlaeufe (Abschnitt 6) liefen von 05:27 UTC (07:27 CEST) an und waren vor diesem Text fertig; ihre Ausgaben
  lese ich erst nach dem Schreiben der Abschnitte 1 bis 5. Abschnitt 6 und die Pruefsummen (7) kommen danach, vor dem
  Einfrieren.
- Karte: KARTE.md (unveraendert). Die Vorhersagen IS0 bis IS4 und ihre Bedeutung stehen dort fest.
- Code: code/ico_stab.py (Modell und Loeser, nach RUNDE-27/frust-3d/code/frust_3d.py), code/auswertung.py (mechanische
  Urteile).

## 1. Modell

- **Geometrie:** 13 Knoten. Zentrum 0 im Ursprung; Ecke 1 = (0, 0, R_c), Ecken 2 bis 6 oberer Ring (Hoehe R_c/sqrt5,
  Radius 2 R_c/sqrt5, Azimut 72 k Grad), Ecken 7 bis 11 unterer Ring (Hoehe -R_c/sqrt5, Azimut 72 k + 36 Grad), Ecke 12
  = (0, 0, -R_c). R_c = sin 72 Grad = 0,951057, Kante 1.
  - Das ist das Ikosaeder (0, +-1, +-phi) und zyklisch, skaliert auf Kante 1 und so gedreht, dass eine Ecke auf der
    z-Achse liegt. Der Code sucht die Kanten als alle Eckpaare im Abstand 1 (Pruefung: genau 30) und die Flaechen als
    alle Dreiecke aus Kanten (Pruefung: genau 20).
- **Staebe:** 12 Speichen (Zentrum-Ecke, Ruhelaenge l_sp) und 30 Kantenstaebe (Ruhelaenge 1). Alle gleich wie in
  FRUST-3D: B = 1, L = 1, Ks = 25600, N Segmente, von Natur aus gerade, keine Torsion. Dehnung (Ks/2) Summe
  (|e| - l0)^2/l0, Biegung (B/l0) Summe (1 - t_i . t_(i+1)).
- **(G) Gelenke (gewertet):** Die Verbinder sind Punkte, die Stabenden frei drehbar.
  - Lager (nur Starrkoerper, statisch bestimmt): Ecke 1 fest, Ecke 12 in x und y, Ecke 2 in y. Ihre Reaktionen muessen
    im freien Fall null sein (Kontrolle).
- **Zentrum frei** (freies Minimum): nur diese Lager.
- **Zentrum fest** (Konkurrenzzustand; nach Rauchlauf Runde 1 geaendert, Abschnitt 6): Die Lage des Zentrums ist keine
  freie Groesse, sondern das Mittel der 12 Ecken (X_0 = Summe X_v / 12; Gradient und Hesse-Matrix per Kettenregel).
  - Die Huelle ist ein Dreiecksnetz und praktisch starr, also hat jede Speiche fast die Sehne R_c. Alle zwoelf knicken
    gleich: Das ist der symmetrische Zustand mit symmetrischer Last.
  - Die Haltekraft ist die Summe der Speichenkraefte am Zentrum; sie geht zu gleichen Teilen an die Ecken und wird als
    Reaktion am Zentrum berichtet (Erwartung: null bis auf Rundung).
  - Erste Fassung (vor dem Rauchlauf): Zentrum im Ursprung fest. Dann dehnt sich die Huelle von der festen Ecke 1 aus,
    und das Zentrum sitzt neben der Huellenmitte.
- **(E) Einspannung (nur berichtet, ohne Urteil):** Verbinder als starre Koerper wie FRUST-3D, Ecke 1 fest in Lage und
  Drehung. Wunschrichtungen = Stabrichtungen im regulaeren Ikosaeder mit Zentrum (Kanten, Speichen radial).
- **Start:**
  - Ecken regulaer. Das Zentrum steht um den Versatz 0,01 L in der Startrichtung verschoben (Zentrum frei).
  - Startrichtungen: null (kein Versatz); ecke = zu Ecke 1; kante = zur Mitte der Kante 1-2; flaeche = zur Mitte der
    Flaeche 1-2-3; zufall1, zufall2, zufall3 = Normalverteilung mit numpy default_rng(1, 2, 3), normiert.
  - Knickanstoss: jeder Stab bekommt eine halbe Sinuswelle quer zur Sehne, Amplitude 1e-3 L. Speichen in Richtung
    a = (0,36; -0,48; 0,80), senkrecht zur Sehne gemacht (keine Speiche liegt parallel zu a); Kantenstaebe senkrecht zur
    Kante von der Mitte weg.
  - Bei Gelenken ist die Knickebene jeder Speiche frei (Drehung um die Sehne kostet nichts); der Anstoss bricht nur die
    gerade Lage.
- **Loeser:** wie FRUST-3D, unveraendert uebernommen.
  - Energie, Gradient, Hesse-Matrix je Stab gebuendelt (torch.func), global dicht.
  - Gedaempfter Newton (Cholesky von H + mu I, mu ab 1e-10 max|diag H|, bei Fehlschlag x10, Armijo).
  - Abbruch bei |grad| < 1e-13 oder am Rundungsboden (kein Fortschritt bei |grad| < 1e-8), hoechstens 300 Schritte je
    Phase.
  - Sattelflucht: Ist der kleinste Hesse-Eigenwert am Phasenende < -1e-6, folgt ein Stoss entlang des Eigenvektors
    (groesste Komponente 1e-2, sonst 3e-3, 1e-3, 3e-4, 1e-4; die erste, die die Energie senkt), dann neue Phase;
    hoechstens 6 Stoesse. Interne Zeitgrenze 480 s.
  - **Stabil** heisst: kleinster Eigenwert der Hesse-Matrix der freien Komponenten > -1e-6 (wie FRUST-3D).
- **Hesse-Analyse:**
  - Die Lager nehmen die sechs Starrkoerpermoden heraus, das volle Spektrum der freien Komponenten enthaelt sie also
    nicht.
  - Bei G hat jede geknickte Speiche eine exakte Nullrichtung (Drehung der inneren Knoten um die Sehne). Diese Drehmoden
    Q (orthonormal, je Stab mit Stich > 1e-5) werden mit H + 1e3 Q Q^T abgetrennt. Berichtet: volles Spektrum, Spektrum
    ohne Drehmoden, Anzahl negativer Eigenwerte ohne Drehmoden, Rest |H Q|.
- **Sattelprobe (nur Zentrum fest):** Im festgehaltenen Zustand wird das Zentrum losgelassen. Berichtet werden der
  Gradient des freien Problems (Restkraft am Zentrum) und das Hesse-Spektrum ohne Drehmoden. Negative Eigenwerte mit
  grossem Zentrumsanteil heissen: Der symmetrische Zustand ist ein Sattel des freien Problems.
- **Kraefte:** F = -dE_Stab/dX am Verbinder, Axialkraft entlang der Sehne, positiv = Zug (wie FRUST-3D).

## 2. Laeufe (echt)

| Lauf | N | Lagerung | Zentrum | Start | Versatz | amp | l_sp | Zweck |
|---|---|---|---|---|---|---|---|---|
| ctrl_12, ctrl_20 | 12, 20 | G | frei | zufall1 | 0,01 | 1e-3 | R_c | IS0 |
| sym_12, sym_20 | 12, 20 | G | fest | null | 0 | 1e-3 | 1 | Konkurrenzzustand, Sattelprobe, IS1, IS2 |
| frei_null_N | 12, 20 | G | frei | null | 0 | 1e-3 | 1 | freies Minimum (Start ohne Versatz) |
| frei_ecke_N, frei_kante_N, frei_flaeche_N | 12, 20 | G | frei | ecke, kante, flaeche | 0,01 | 1e-3 | 1 | freies Minimum |
| frei_zufall1_N bis frei_zufall3_N | 12, 20 | G | frei | zufall1 bis 3 | 0,01 | 1e-3 | 1 | freies Minimum |
| e_sym_12 | 12 | E | fest | null | 0 | 1e-3 | 1 | nur berichtet |
| e_frei_flaeche_12 | 12 | E | frei | flaeche | 0,01 | 1e-3 | 1 | nur berichtet |

- 20 Laeufe, je ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4, cpu6), Laufordner
  /home/fmh/fmhc-physics-remote/runde29-ico-stab/lauf/. Danach auswertung.py ueber eine Spur.
- Die E-Laeufe kommen zuletzt in die Spuren. Fehlen sie oder brechen sie ab, wird das berichtet, ohne Folge fuer die
  Urteile.
- Die Spur bricht nach 600 s ab. Ein abgebrochener Lauf wird offengelegt und nicht gewertet; fehlt ein gewerteter Lauf,
  ist das betroffene Urteil "nicht entscheidbar".

## 3. Messgroessen

- Je Stab: Axialkraft (beide Enden), Querkraft an den Enden, Stich (groesster Abstand der inneren Knoten von der
  Sehne), Sehne, Verkuerzung l_ruhe - Sehne, Verhaeltnis Druck / Euler-Last pi^2 B/l^2, groesstes Moment im Stab,
  Energie (Dehnung, Biegung).
- **Zentrum:** u = |X_0 - Mitte der 12 Ecken| (Mitte der verformten Huelle). Richtung: Winkel zur naechsten Ecke,
  Kantenmitte und Flaechenmitte (aus der verformten Huelle); je Speiche cos(theta) gegen u.
- Huelle: Axialkraft und Laenge der 30 Kantenstaebe (Kleinst-, Groesst-, Mittelwert), Eckradien.
- Gesamt: Energie, Biegeanteil (Biegung innen + Einspannung durch Gesamtenergie).
- **Messschwelle s** je Lauf: max(1e-9, 100 x groesster Gleichgewichtsrest der freien Komponenten), wie FRUST-3D.
- **Freies Minimum bei N:** unter den freien Laeufen bei N (sieben Starts), die stabil sind, der mit der kleinsten
  Energie. Ist keiner stabil, sind IS1 bis IS4 bei N "nicht entscheidbar".
- **Symmetrischer Zustand bei N:** Lauf sym_N.

## 4. Urteile (mechanisch, auswertung.py)

Die Vorhersagen der Karte, woertlich:

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IS0 | Kontrolle: Speichen-Ruhelaenge R_c ist spannungsfrei, \|F\| L, \|tau\| < 1e-8 | 90 % |
| IS1 | Ruhelaenge 1, (G): Speichen auf Druck, alle 30 Huellenstaebe auf Zug (Kontrolle, ableitbar) | 95 % |
| IS2 | (G): Das freie Minimum liegt mindestens 0,5 % unter dem symmetrischen Zustand, und das Zentrum ist um u in [0,035; 0,075] L verschoben | 60 % |
| IS3 | (G): Im freien Minimum ist mindestens eine Speiche gerade (Stich < 1 % L) und mindestens sechs sind geknickt (Stich > 5 % L) | 60 % |
| IS4 | (G): E_min liegt zwischen 5,2 und 6,2 B/L | 70 % |

Umsetzung:
- **IS0** (ctrl_12, ctrl_20): fuer beide Enden aller 42 Staebe |F| < 1e-8 und |tau| < 1e-8 (bei G ist tau = 0). Beide
  Laeufe muessen gelten.
- **IS1** (je N): Im symmetrischen Zustand sym_N **und** im freien Minimum haben alle 12 Speichen an beiden Enden eine
  Axialkraft < -s und alle 30 Kantenstaebe an beiden Enden > +s.
  - Die Karte nennt keinen Zustand; ich nehme die strengere Lesart (beide Zustaende des Hauptfalls). Die Teilergebnisse
    je Zustand werden berichtet.
- **IS2** (je N): (E_sym - E_frei)/E_sym >= 0,005 und 0,035 <= u <= 0,075, mit E_frei, u aus dem freien Minimum und
  E_sym aus sym_N.
- **IS3** (je N): Im freien Minimum ist die Zahl der Speichen mit Stich < 0,01 mindestens 1 und die Zahl mit
  Stich > 0,05 mindestens 6.
- **IS4** (je N): 5,2 <= E_frei <= 6,2.
- **Gitter:** Jedes Urteil IS1 bis IS4 wird bei N = 12 und N = 20 gefaellt. Gleich: dieses Urteil. Verschieden:
  "uneinheitlich (Gitter)", keine Bedeutung ausgeloest.
- **Bedeutung** (Karte): IS2 und IS3 eingetroffen: der Fall "Konvexitaetsmechanismus allgemein [H]". IS2 nicht
  eingetroffen: beschreiben (bei symmetrischem Minimum, u < 0,005, ist das der Fall der Karte "Lesart falsch oder nicht
  uebertragbar"; scheitert IS2 an der Spanne oder am Abstand, beschreibe ich das ohne diesen Fall).
- Die Hesse-Frage der Karte ("Ist die Hesse-Matrix im freien Minimum positiv?") wird berichtet, nicht gewertet: kleinster
  Eigenwert ohne Drehmoden > 0 heisst ja.

## 5. Kontrollen (berichtet)

- IS0-Laeufe: Der Anstoss (Versatz 0,01 und Knick 1e-3) muss verschwinden; u und Stich gegen null.
- Gleichgewicht je Verbinder (freie Komponenten; bei Zentrum fest einschliesslich des Zwoelftels der Haltekraft je Ecke)
  und Reaktionen an den Lagern (muessen null sein).
- Gelenk-Probe: Querkraft an den Stabenden (die Endkraft muss auf der Sehne liegen).
- Gitter N = 12 gegen 20: Energie, u, Speichenkraefte.
- Alle sieben Starts: Endenergie, u, Richtung, Zahl gerader und geknickter Speichen. Gleiche Endenergie heisst gleicher
  Zustand bis auf Symmetrie.
- Symmetrischer Zustand: Speichenkraefte und Stiche gleich? Haltekraft. Sattelprobe.
- Hesse-Matrix im freien Minimum: Zahl der Nullrichtungen = Zahl der geknickten Speichen? Kleinster Eigenwert ohne
  Drehmoden.
- **Schreibtisch des Code-Agenten (vor jeder Rechnung, kein Kriterium):**
  - Geknickte Speiche mit Verkuerzung Delta (Elastica, kleine Amplitude): Last P_E (1 + Delta/2), Energie
    P_E (Delta + Delta^2/4), Stich (2/pi) sqrt(Delta).
  - Symmetrisch: Delta_0 = 1 - R_c = 0,0489; E_sym ~ 12 P_E (Delta_0 + Delta_0^2/4) = 5,87 B/L, dazu ~0,03 Dehnung,
    also ~5,90. Speichen -10,1, Huelle +3,85 (T = P/(5 x 0,5257)), Stich ~0,14.
  - Die Summe der Sehnen ist im Zentrum minimal (konvex), also ist die Summe der Verkuerzungen dort maximal. Rueckt das
    Zentrum um u, faellt E um ~3,3 P_E u^2. Die Sattelprobe sollte drei negative Eigenwerte zeigen (Zentrum in drei
    Richtungen).
  - Das Zentrum wandert, bis die fernsten Speichen die Sehne 1 erreichen. Die erlaubte Zone ist der Schnitt der zwoelf
    Einheitskugeln um die Ecken; ihre Spitzen liegen in Flaechenrichtung.
    - Ecke: u = 0,049, E/P_E = 0,5866
    - Kante: u = 0,057, E/P_E = 0,5837
    - Flaeche: u = 0,061, E/P_E = 0,5823, gegen 0,5945 symmetrisch
    - Ecke und Kante sollten Sattel sein (entlang des Randes geht es abwaerts zur Flaechenrichtung).
  - **Erwartet:** Zentrum Richtung Flaechenmitte, u ~ 0,060. Die drei Speichen der Gegenflaeche sind gerade und
    gedrueckt, mit ~0,84 P_E ~ 8,3 (Kraeftegleichgewicht am Zentrum). Neun sind geknickt: je drei mit Delta ~ 0,096,
    0,058, 0,036, Stich ~ 0,20, 0,15, 0,12.
  - E_frei ~ 5,75 + 0,03 ~ 5,78, also ~2 % unter E_sym. Danach erwarte ich IS1 bis IS4 eingetroffen, die Huelle ueberall
    unter Zug (3 bis 4,5), und neun Nullrichtungen in der Hesse-Matrix.

## 6. Rauchlaeufe (vor dem Einfrieren, Parameter in keinem echten Lauf), ab 07:34 CEST eingetragen

- Ordner rauch-69/. Speichen-Ruhelaenge 0,98 (Fehlpass Delta_0 = 0,029 statt 0,049) oder N = 8; interne Zeitgrenze
  100 s. Alle rc = 0.
- **Runde 1** (05:27:08 bis 05:28:14 UTC, Spuren cpu, cpu2, cpu3, cpu4, cpu6, erste Codefassung):
  - rauch_ctrl_8 (N = 8, l_sp = R_c, Start zufall1 mit Versatz 0,01): spannungsfrei, Axialkraefte <= 1,1e-11, u = 0,
    9 Newton-Schritte, 5 s.
  - rauch_frei_8 (N = 8, G, Start flaeche) und rauch_frei_20 (N = 20, G, Start zufall1): Zentrum zur Flaechenmitte
    (Winkel 0,00 Grad), u = 0,0355. Drei Speichen gerade (Druck -9,15 bzw. -9,29, also 0,89 bzw. 0,90 der Euler-Last bei
    l = 0,98), neun geknickt in drei Gruppen (Stich 0,092, 0,116, 0,148). Huelle Zug +3,3 bis +4,2. Neun Nullrichtungen,
    ohne Drehmoden kleinster Eigenwert 1,24 bzw. 0,49 (stabil). 11 s bzw. 62 s (N = 20).
  - rauch_fest_8 (erste Fassung: Zentrum im Ursprung fest): Energie 3,514101 gegen frei 3,471035 bei N = 8. **Mangel:**
    Die Huelle dehnt sich von der festen Ecke 1 aus; das Zentrum sass 1,5e-4 neben der Huellenmitte. Die Stiche
    streuten um 0,5 %, und die Restkraft am losgelassenen Zentrum war 1,0e-2 statt null.
  - rauch_e_8 (N = 8, E, Start flaeche): 38 s; Zentrum in der Mitte (u < 1e-6), Speichen in zwei Gruppen (-24,3 und
    -15,1).
- **Aenderung nach Runde 1** (vor dem Einfrieren, offengelegt): Zentrum fest = Mittel der 12 Ecken statt Ursprung
  (Abschnitt 1). Grund: rauch_fest_8. Damit ist der Konkurrenzzustand symmetrisch, wie die Karte ihn meint. Keine Regel
  in Abschnitt 4 geaendert.
- **Runde 2** (05:32:33 UTC an, Code mit Zentrum = Mittel der Ecken):
  - rauch_fest2_8: alle zwoelf Speichen gleich (Stich 0,1060, -10,276), alle Kanten +3,9091. Restkraft am
    losgelassenen Zentrum 2,2e-10. **Sattelprobe: drei negative Eigenwerte** (-1,00, -0,96, -0,86), dann +15,1. Energie
    3,514102, das freie Minimum (3,471035) liegt 1,23 % darunter.
  - rauch_frei_null_8 und rauch_frei_ecke_8: beide wie rauch_frei_8 (Energie gleich auf 1e-8, andere Flaeche). Auch der
    Start ohne Versatz verlaesst den Sattel ohne Stoss; die Knickanstoesse brechen die Symmetrie.
  - rauch_e_fest_8 (E, Zentrum fest): gleiche Energie wie rauch_e_8 (6,683289), Sattelprobe ohne negativen Eigenwert,
    55 s.
  - rauch_fest2_20 (N = 20): 78 Newton-Schritte, 105 s mit Hesse-Analyse und Sattelprobe. Alle Speichen gleich (Stich
    0,1053, -10,407), Sattelprobe drei negative Eigenwerte (-0,38, -0,36, -0,32), Restkraft am Zentrum 7,4e-10.
  - auswertung.py an Verweisen in rauch-69/test/ (nur Codepruefung, 05:34:30 UTC): laeuft. Fuer diesen kleineren
    Fehlpass ergaebe sie IS0 bis IS3 eingetroffen, IS4 nicht (Energie 3,47 bzw. 3,51 < 5,2).
- **Was ich damit vor den echten Laeufen weiss (offengelegt):** Bei Delta_0 = 0,029 wandert das Zentrum zur
  Flaechenmitte, drei Speichen bleiben gerade, das freie Minimum liegt 1,2 % unter dem symmetrischen Zustand. Das
  entspricht dem Schreibtisch in Abschnitt 5. Die Regeln in Abschnitt 4 bleiben unveraendert.
- Laufzeit: Die echten Laeufe bei N = 20 brauchen nach Runde 2 etwa 1 bis 2 min, E bei N = 12 einige Minuten; die
  interne Zeitgrenze bleibt 480 s.
- code/laeufe.sh (Startskript, Lauftabelle aus Abschnitt 2) ist vor dem Einfrieren geschrieben und eingefroren.

## 7. Einfrieren

- Code-Pruefsummen (sha256), lokal und auf der .69 gleich (geprueft 07:35:05 CEST):
  - code/ico_stab.py: 3746c7da9153c5745d2f235171110089cf543e0f139b4b14bac066c3105e5b5d
  - code/auswertung.py: cb331390aad5ae766fbc8774d3c115fbd99a583bd6a6e56c43b46ad201b22f29
  - code/laeufe.sh: 8e39015fb98706320d9e60f97583c49e3f39b609f48da9caac0e96f9816ef4f0
- Eingefroren als PLAN.md.eingefroren-<Zeit> und code/*.eingefroren-<Zeit>, schreibgeschuetzt, vor dem ersten echten
  Lauf. Die Fassung vor dem Lesen der Rauchlaeufe liegt als PLAN.md.bak-vor-rauch daneben.
