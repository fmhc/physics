# ZELT-KOMMUTATOR-2: Plan (Code-Agent, Runde 49, explorativ nach v3)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-05 12:58:35 CEST (date). Plantext ab 13:33:56 CEST (date),
  vor jeder Rechnung. Zeitbox 150 min ab Start.
- Grundlage: KARTE.md (ZP0 bis ZP3, UT1 bis UT4; Wortlaut, Schwellen, Wahrscheinlichkeiten unveraendert). Gelesen:
  PACHNER-TAKT-1 (KARTE, PLAN eingefroren, ERGEBNIS, pt.py eingefroren, Logs in lauf-69), LAMBDA-TURING-L Abschn. 4.2
  und 5 (K2), GIELEN-RIED-TIEF-L Abschn. 3, 6, 7 (K2), Quelle 2610.03479v1 Gl. (24) bis (36) im Textauszug
  (gielen-ried-tief-l/quellen), RUNDE-42 (Ernte PACHNER-TAKT-1).
- Kennzeichen: [M] vorab ableitbar, [S] an der Quelle gelesen, [P] Projektdatei, [E] hier gerechnet, [F] Festlegung
  dieses Plans, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.
- Synthetisch (euklidisches Regge, Kommutator-Schicht aus PACHNER-TAKT-1), keine Messdaten.
- Code: code/pt.py = bytegleiche Kopie von pachner-takt-1/code/pt.py.eingefroren-20261004-173434 (sha256 bc360991...),
  unveraendert; neuer Code nur in code/zk.py (importiert pt) und code/zk_auswertung.py.

## 1. Schreibtisch (vor jeder Rechnung)

### 1.1 Schicht [P]
- Netz n = 4, Hoehen nach Klasse (0 / 0,25 / 0,5 / 0,75), Diagonalen C2. A = (2, 2, 2) Klasse 0 bei t = 0,
  B = A + (1/2, 1/2, 0) Klasse Z bei t = 0,75. A' = A + N_A e_t, B' = B + N_B e_t; L: (N_A, N_B) = (0,3; 0,5),
  G: (0,4; 0,4). AB = Zelt A auf Sigma_0, dann Zelt B auf Sigma_1; BA umgekehrt. 48 Simplizes, 3 Innenkanten, 111
  Randkanten. Randdaten wie pt.welle_laengen (H_yy = -H_zz = cos(k (x - x_A)), L_kubisch = (L/a)/sqrt2).

### 1.2 Kombinatorik [M]
- In C2 tragen Diagonalen nur die Klassen Y und Z (d0 = max{M+1, M+3} mod 4). A (Klasse 0) liegt auf keiner Diagonale:
  Stern 8 + 6 x 2 = 20 Tetraeder. B (Klasse Z) liegt in 4 seiner 6 Oktaeder auf der Diagonale: 8 + 4 x 4 + 2 x 2 = 28.
  20 + 28 = 48 wie gemessen [P].
- Link der Kante AB in Sigma_0 (relativ zu A, raeumlich): c1 = (1/2, 0, 1/2) [Y], c2 = (0, 1/2, 1/2) [X],
  c3 = (-1/2, 1/2, 0) [Z], c4 = (0, 1/2, -1/2) [X], c5 = (1/2, 0, -1/2) [Y]; Fuenfeck (k = 5): zwei regulaere
  Tetraeder, ein Oktaeder mit Diagonale c5-c1 (Klasse Y, AB in 1 Tetraeder), eines mit Diagonale durch B (AB in 2).
- Zerlegung: Gemeinsam sind {A, A', T} (T in Stern A ohne B, 15) und {B, B', T} (T in Stern B ohne A, 23), also 38.
  Je Spalte i (Paar c_i, c_i+1) hat AB die zwei Simplizes {A, A', B, c_i, c_i+1} und {A', B, B', c_i, c_i+1}, BA die zwei
  {A, B, B', c_i, c_i+1} und {A, A', B', c_i, c_i+1}. **Differenzmenge 10 gegen 10.**
- **Grad der Kante A'B in AB = 2k = 10**; ihr Link ist die Doppelpyramide ueber dem Fuenfeck mit den Polen A und B'.
- Region R = Q * L: Q = Viereck A, A', B', B, L = Fuenfeck. AB = (Q mit Diagonale A'B) * L, BA = (Q mit AB') * L.
- **Kuerzeste Pachner-Folge:**
  - Untergrenze: A'B verschwindet nur durch einen 4-2-Zug (5-1 entfernt nur Kanten an der entfernten Ecke), AB' entsteht
    nur durch einen 2-4-Zug. Der Link von A'B (10 Dreiecke) muss vorher auf den Rand eines Tetraeders (4) schrumpfen. Jeder
    Zug aendert die Dreieckszahl eines Kantenlinks um -2, 0 oder +2; Schrumpfen (-2) koennen nur 3-3-Zuege (A'B im alten
    Dreieck), 4-2-Zuege an anderen Kanten oder 5-1-Zuege. Mit m 2-4-Zuegen (= m 4-2-Zuege, Kantenbilanz) und s Paaren
    1-5/5-1 ist die Laenge >= m + s + 4, also >= 5, Gleichheit nur fuer m = 1, s = 0 und genau drei 3-3-Zuege.
  - Bau: 2-4 am Spaltentetraeder {A', B, c_i, c_i+1} (Spitzen A und B') erzeugt AB', die Spalte i in BA-Form und zwei
    Q-Simplizes {A, A', B, B', c_i}, {A, A', B, B', c_i+1}. Jeder 3-3-Zug am Dreieck {A', B, c_j} (Grad 3) dreht eine
    Nachbarspalte in BA-Form und schiebt den Q-Simplex weiter. Nach drei 3-3-Zuegen hat A'B Grad 4 (Link = Rand von
    {A, B', c, c'}); der 4-2-Zug entfernt A'B und beide Q-Simplizes. Laenge k = 5: 2-4, 3-3, 3-3, 3-3, 4-2.
  - Ein 3-3-Zug kann nicht der erste sein: In AB hat kein Dreieck mit A'B den Grad 3 ({A, A', B} und {A', B, B'} Grad 5,
    {A', B, c_i} Grad 4).
  - **ZP1 ist damit vorab eingetroffen [M]**; der Rechner bestaetigt das durch Breitensuche (Abschn. 2).
  - L und G haben dieselbe Kombinatorik (nur Hoehen verschieden) [M].

### 1.3 Geometrie: Die Zwischenschritte sind flach entartet [M]; Regularisierung [F]
- A, A', B, B' liegen in einer Ebene des R^4 (Zeltzuege rein zeitlich). Jeder Q-Simplex hat 4-Volumen null. In jeder
  Spalte ist Q der einzige Kreis (circuit); die Spalte ist der Verbund Q * Strecke und hat nur die zwei Zerlegungen A'B
  und AB'. Nachbarspalten teilen Q * c_i, also gibt es ohne neue Ecken nur die zwei geometrischen Zerlegungen AB und BA.
  **Kein Pachner-Weg ist bei senkrechten Zelten geometrisch**; Hesse-Formen der Zwischenschritte sind singulaer.
- **Regularisierung [F]:** A' wird raeumlich um tau s e_z verschoben (Zelt mit kleiner Schiebung), s = +1 oder -1. Dann ist
  Q ein duennes Tetraeder in der Hyperebene H durch die Ebene von Q und e_z; Normale ~ (1, -1, 0, 0). Seiten der c_i:
  + - - - + (c3 am weitesten). Zwei Spalten mit Seitenwechsel ((1,2) und (4,5)) koennen 2-4 bzw. 4-2 tragen, drei Spalten
  ohne Wechsel 3-3 [M, Kreisvorzeichen]. Welche Zuege geometrisch sind, prueft der Rechner (Abschn. 2.3).
- tau in {0,2; 0,1; 0,05; 0,025} (kubische Einheiten), **Haupt-tau = 0,1**. AB und BA werden fuer jedes tau neu
  gerechnet (D(tau)); tau = 0 reproduziert PACHNER-TAKT-1.
- Auswahlregel (rein geometrisch, vor jedem Defekt): Kandidaten in dieser Reihenfolge: A' mit s = +1, A' mit s = -1,
  B' mit s = +1, B' mit s = -1. Genommen wird der erste Kandidat, fuer den bei L und G und allen vier tau ein kuerzester
  Weg geometrisch ist. Kanonischer Weg: unter den geometrischen kuerzesten Wegen der erste in der Sortierung der
  Breitensuche (Zuege als sortierte Tupel). Gibt es keinen, ist Teil A je Zug "nicht auswertbar".

### 1.4 Defekt je Zug [F, M]
- Fuer jede Zerlegung T_0 = AB, T_1 bis T_4, T_5 = BA dieselben Randlaengen (aus den flachen Kantenvektoren der Randkanten
  der Schicht bei diesem tau), Innenkanten nichtlinear geloest (pt.loese, Newton). p_j = dS/dl ueber die 111 Randkanten,
  S_j die Wirkung, DeltaT_j = Summe der 4-Volumina.
- Defekt des Zugs j: **d_j = || p_j - p_(j-1) ||_2** (dasselbe Mass wie D). D(tau) = || p_5 - p_0 ||.
- [M] Die Vektorsumme der p_j - p_(j-1) ist exakt p_5 - p_0 (Teleskop), ebenso die Summe der S_j - S_(j-1). ZP2 ist also
  nur mit Normen eine Pruefung: Summe d_j >= D (Dreiecksungleichung), Gleichheit genau bei gleichgerichteten
  Defektvektoren.
- [L/M, DKS-Lesart] 2-4 und 4-2 mit lokaler flacher Loesung lassen die Hamilton-Funktion exakt gleich (14 Randlaengen
  legen 6 Punkte im R^4 fest, die neue Kante ist ihr flacher Abstand). Ein 3-3-Zug hat 15 Kanten auf 6 Ecken, also einen
  Kruemmungsfreiheitsgrad; er kann die Hamilton-Funktion aendern.
- Zusaetzlich linear: Schur-Komplement Q_j der flachen Hesse-Form, linearer Defekt ||(Q_j - Q_(j-1)) w||.
- **Geaendert nach Rauchtest r2 (ohne Kenntnis von Defekten):** Die duennen Q-Simplizes haben die Hoehe ~ tau ueber der
  Ebene von Q; Laengenstoerungen eps l veraendern das Hoehenquadrat um ~ 2 l^2 eps. Nichtlineare Loesungen der
  Zwischenschritte sind daher nur fuer eps << tau^2 sinnvoll (bei tau = 0,025 und eps = 1e-3 nicht) [M]. r2 brach bei
  flachen Randdaten mit "Matrix is not positive definite" ab (Start der Innenkanten bei den unverschobenen flachen
  Laengen). Folge:
  - **Hauptmass in Teil A ist der lineare Defekt** d_j = eps ||(Q_j - Q_(j-1)) w|| und D_lin = eps ||(Q_5 - Q_0) w||
    (die Karte rechnet "linearisiert"; PACHNER-TAKT-1: D/eps = 0,9770 gegen D1 = 0,9773 [P]). Verhaeltnisse und
    Exponenten sind damit eps-frei.
  - Nichtlinear wird weiter gerechnet (Kontrolle), Start der Innenkanten bei den Laengen derselben Vorschrift (Welle bzw.
    flache Verschiebung) statt bei den flachen; Fehlschlaege werden je Fall vermerkt (K6), nicht wiederholt.

### 1.5 Unimodulare Uhr [M]
- DeltaT = Summe_sigma V_sigma (Gl. 36 der Arbeit [S]) aus den geloesten Kantenlaengen (Volumen aus pt.koord_aus_laengen).
- Flach: V(Zelt v) = (1/4) h_v Vol3(Projektion des Sterns); jedes Tetraeder hat raeumlich 1/24. DeltaT_L =
  (1/4)(0,3 x 20 + 0,5 x 28)/24 = 5/24, DeltaT_G = (1/4) 0,4 x 48/24 = 1/5.
- **D_T = |DeltaT(AB) - DeltaT(BA)| / DeltaT(AB)**, bei tau = 0 (Originalgeometrie). Flach (eps = 0 und flach verschobene
  Ecken) D_T = 0 [M].

### 1.6 Agenten-Vorhersagen (vorab; gehen in kein Kartenurteil ein)

| Nr | Vorhersage |
|---|---|
| V1 | Breitensuche: kein Weg mit <= 4 Zuegen, kuerzeste Laenge 5, jeder kuerzeste Weg = 1 x 2-4, 3 x 3-3, 1 x 4-2 |
| V2 | Geometrisch ist bei s = +1 oder s = -1 (A') ein kuerzester Weg; 2-4 und 4-2 haben Defekt <= 1e-10 D (DKS) |
| V3 | Die drei 3-3-Defekte wachsen fuer tau -> 0 (etwa wie 1/tau); dann ist Summe d_j >> D und ZP2 verfehlt (50 %) |
| V4 | D_T ist erster Ordnung (UT4 eingetroffen) und q liegt in [1,75; 2,75] (UT2) (50 %) |

## 2. Laeufe und Messgroessen

### 2.1 Laeufe auf der .69 (kleintest.sh, Spuren cpu5 und cpu6; je <= 10 min, 1 Thread, 4 GB)

| Lauf | Inhalt |
|---|---|
| KB | Kombinatorik (L und G), Breitensuche in R (Tiefe bis 5 von AB, alle kuerzesten Wege), Geometrie-Pruefung aller kuerzesten Wege fuer alle Kandidaten und tau, Auswahl |
| KI | isolierte Zuege: 2-4/4-2 und 3-3 an sechs allgemeinen Punkten mit gekruemmten und flachen Randdaten |
| DL | Teil A, Variante L: tau in {0,2; 0,1; 0,05; 0,025}; eps in {1e-3, 1e-4} x L/a in {4, 8, 16, 32}; flach (eps_flach = 1e-3 und 1e-4, L/a = 4); eps = 0; linear |
| DG | dasselbe fuer G |
| UT | Teil B bei tau = 0: L und G, eps in {0, 1e-3, 1e-4} x L/a in {4, 8, 16, 32}; flach; D zum Vergleich mit PACHNER-TAKT-1 |
| AW | Auswertung (zk_auswertung.py) |

### 2.2 Exponenten-Fitregel
- Exponent = Steigung der Ausgleichsgeraden von log(Wert) gegen log(a/L) ueber alle vier L/a = 4, 8, 16, 32 (kleinste
  Quadrate, gleiche Gewichte). Fehler = Standardfehler der Steigung aus den Residuen (2 Freiheitsgrade); dazu die drei
  lokalen Steigungen zwischen Nachbarpunkten. Liegt ein Wert unter 1e-13 (absolut, D_T relativ), ist der Exponent "unter
  Rundung" und nicht auswertbar.

### 2.3 Geometrie-Pruefung einer Zerlegung
- Geometrisch heisst: jedes Simplex |V| > 1e-10 l_max^4; an jedem inneren Tetraeder liegen die beiden Spitzen auf
  verschiedenen Seiten; an jedem Randtetraeder liegt die Spitze auf derselben Seite wie in AB.

## 3. Urteilsregeln (mechanisch in code/zk_auswertung.py)

- Robustheitsregel fuer "nach Kartenwortlaut" in Teil A: Die Karte kennt tau nicht. Urteil nach Wortlaut = Urteil ueber
  das ganze Kartenraster (L und G, eps 1e-3 und 1e-4, alle L/a) beim Haupt-tau, wenn es bei allen vier tau gleich ausfaellt;
  sonst "unklar (haengt an der Regularisierung)".
- **ZP0** ("flache Randdaten, Defekt jedes Zugs < 1e-13 relativ"): nach Plan eingetroffen genau dann, wenn auf dem
  kanonischen Weg bei Haupt-tau, L und G, eps_flach = 1e-3: linear eps_flach max_j ||(Q_j - Q_(j-1)) w_flach|| / ||p_0||
  < 1e-13 und, wo nichtlinear loesbar, max_j d_j / ||p_0|| < 1e-13 (w_flach = Ableitung von pt.flach_laengen, L/a = 4).
  Nach Wortlaut: dazu eps_flach = 1e-4, Robustheitsregel.
- **ZP1** ("Die kuerzeste Folge AB -> BA enthaelt mindestens einen 3-3-Zug"): eingetroffen genau dann, wenn die
  Breitensuche (vorwaerts Tiefe 3, rueckwaerts Tiefe 2, also bis Laenge 5) einen kuerzesten Weg findet und jeder
  kuerzeste Weg mindestens einen 3-3-Zug enthaelt; findet sie keinen: nicht auswertbar. Nach Plan = nach Wortlaut
  (kombinatorisch, ohne tau). Vorab [M] eingetroffen.
- **ZP2** ("D gleich der Summe der Einzeldefekte auf 1 %"), linear: nach Plan eingetroffen genau dann, wenn bei L,
  Haupt-tau fuer alle vier L/a gilt |Summe_j d_j - D_lin| / D_lin <= 0,01. Nach Wortlaut: L und G, alle L/a (eps-frei),
  Robustheitsregel ueber tau.
- **ZP3** ("Der Einzeldefekt faellt im Bereich L/a = 4 bis 32 mit einem Exponenten 2,0 bis 2,5"), linear: Einzeldefekte
  sind die Zuege mit d_j > 1e-6 D_lin bei L/a = 4 (die DKS-Nullzuege fallen heraus). Nach Plan eingetroffen genau dann,
  wenn bei L, Haupt-tau jeder dieser Exponenten in [2,0; 2,5] liegt; gibt es keinen solchen Zug: nicht auswertbar. Nach
  Wortlaut: L und G, Robustheitsregel ueber tau.
- **UT1 / UT2 / UT3** (q >= 2,75 / 1,75 <= q < 2,75 / q < 1,75): q = Exponent von D_T (Fitregel 2.2), tau = 0. Nach Plan:
  Variante L, eps = 1e-3; genau die Klasse, in der q liegt, ist eingetroffen. Nach Wortlaut: q fuer L und G bei beiden eps;
  eine Klasse ist eingetroffen, wenn alle vier q in ihr liegen, "unklar", wenn einige, nicht eingetroffen, wenn keines.
  Liegt D_T bei eps = 1e-3 ueberall unter 1e-13: alle drei nicht auswertbar (D_T verschwindet).
- **UT4** ("D_T linear in eps, Verhaeltnis der Werte bei 1e-3 und 1e-4 zwischen 9 und 11"): nach Plan eingetroffen genau
  dann, wenn D_T(1e-3)/D_T(1e-4) in [9; 11] fuer alle vier L/a bei L; nach Wortlaut zusaetzlich bei G.

## 4. Kontrollen (gehen ueber die Urteile hinaus)
- K1: D bei tau = 0 reproduziert lauf-69/ko.json von PACHNER-TAKT-1 (L und G, alle L/a, eps = 1e-3) auf 1e-8 relativ zu
  D (Rundung der Impulse etwa 1e-14 bei D bis 9e-6; vor jeder Rechnung von 1e-10 gelockert, Grund Rundung).
- K2: eps = 0: D_T <= 1e-13; DeltaT gleich 5/24 (L) bzw. 1/5 (G) auf 1e-13 relativ; flach verschobene Ecken: D_T <= 1e-13.
- K3: Teleskop: || Summe_j (p_j - p_(j-1)) - (p_5 - p_0) || <= 1e-12 ||p_0||; T_5 des Weges gleich der BA-Schicht aus
  dem Bau wie pt.lauf_kommutator (gleiche Simplexmenge nach Umbenennung A' <-> B'; Impulse auf 1e-12 relativ zu ||p||,
  bei tau = 0).
- K4: isolierter 4-2-Zug mit Loesung: Defekt <= 1e-10 relativ (gekruemmt und flach); isolierter 3-3: flach <= 1e-12,
  gekruemmt > 1e-8 (sonst ist die DKS-Gegenprobe stumpf).
- K5: L und G ergeben dieselbe Folge (gleicher kanonischer Weg).
- K6: Newton-Rest <= 1e-12 (relativ zu ||p||) in allen geloesten Faellen; nicht loesbare Faelle je tau aufzaehlen;
  D(tau) gegen D(0) und gegen eps D_lin(tau): Abweichung je tau angeben.
- K7: DKS-Lesart im Netz (linear): 2-4- und 4-2-Defekt <= 1e-10 D_lin bei allen tau, L/a, L und G; jeder 3-3-Defekt
  >= 1e-3 D_lin.
- K8 (beschreibend): nichtlinearer gegen linearen Defekt je Zug, d_j / (eps d_j,lin), wo loesbar.

## 5. Rauchtest und Einfrieren
- Rauchtests (je <= 120 s) erst nach diesem Plantext: nur Laufzeit, Speicher, Rueckgabe, Schluessel und rein
  geometrische/kombinatorische Kontrollen (Geometrie-Pruefung, Kantenbilanz) ansehen; keine Defekte, keine D_T, keine
  Exponenten, keine Urteile.
- Danach PLAN.md und code/ als .eingefroren-<zeit> kopieren, sha256 in EINGEFROREN-SHA256.txt.
- **Rauchtest r1** (cpu5/cpu6, 11:43:52 bis 11:44:06 UTC, zk.py 48b9670e...): kb 13,3 s, 48 MB; ki 0,2 s. Gelesen nur:
  Schluessel, Kombinatorik-Kontrollen (48/48 Simplizes, Differenz 10/10, gemeinsam 38, Sterne 20/28, k = 5, Grad 10/10,
  G gleich L) und die Geometrie-Pruefung: bei tau = 0 ist kein Zwischenschritt geometrisch (Volumen 0, wie 1.3); Kandidat
  A' (beide s) faellt bei L, tau = 0,2 aus (BA nicht geometrisch); **gewaehlt nach der Regel: B' mit s = +1**, je tau 3
  geometrische kuerzeste Wege, derselbe kanonische fuer L und G; kleinstes relatives Zwischenvolumen 1,8e-5 (L, tau =
  0,025). Nicht gelesen: Breitensuche-Ergebnis, ki-Werte.
- **Rauchtest r2** (cpu5/cpu6, 11:44:35 bis 11:44:44 UTC): uhr (L, G; eps 1e-3, L/a 4) 8,5 s, rc 0. defekte (L; tau 0,1
  und 0,025; L/a 4, 32) brach bei den flachen Randdaten ab (Cholesky, Abschn. 1.4). Nichts weiter gelesen.
- Danach im Code: Start der Newton-Iteration (loese_start, Kopie von pt.loese), Fehlerfang je Fall, linearer Flachtest,
  Auswertung mit linearem Hauptmass, tau-Liste aus den Daten.
