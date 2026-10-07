# TETRA-KETTE: Ergebnis (Code-Agent fuer die Leitung, Runde 26, explorativ)

- Gerechnet auf der .69 (kleintest.sh, CPU-Spuren cpu, cpu2, cpu3, cpu4, cpu6):
  - zwei Rauchlaeufe 02:07:31 bis 02:07:49 UTC (04:07 CEST), Parameter in keinem echten Lauf
  - sechs echte Laeufe 02:09:32 bis 02:09:56 UTC (04:09:32 bis 04:09:56 CEST), je 6,5 bis 11,8 s
  - Auswertung (code/auswertung.py) 02:10:28 UTC
  - alle rc = 0
- Auswerteregeln in PLAN.md ab 04:06:35 CEST, vor dem Rauchlauf. Plan und Code eingefroren 04:09:22 CEST
  (PLAN.md.eingefroren-20261003-040922, code/*.eingefroren-20261003-040922), vor dem ersten echten Lauf.
- Daten: lauf-69/ (Laeufe, auswertung.json mit den Urteilen), rauch-69/. Code: code/tetra_kette.py (sha256 665af77b...),
  code/auswertung.py (1e4ee4e0...).
- Geschrieben ab 04:15:00 CEST (date).
- Einheiten im Modell: B = 1, Stablaenge L = 1; Momente in B/L, Kraefte in B/L^2. Ein Tetraeder weiter = eine Ecke
  weiter = 0,316 L entlang der Achse.

## Ergebnis zuerst

1. **Die Spannung des Defekts klingt schnell ab, aber in Stufen.**
   - Je drei Tetraeder faellt das groesste Endmoment um den Faktor 7,7 bis 12 (k = 2 bis 10). Innerhalb einer Stufe
     bleibt es etwa gleich oder steigt leicht (T_4/T_3 = 1,03; T_7/T_5 = 1,16).
   - Im Mittel (Fit k = 2 bis 8) faellt es um den Faktor 2,12 je Tetraeder, Abklinglaenge 1,33 Tetraeder.
   - Am Kettenende (k = 11) ist noch 7e-5 des Hoechstwerts uebrig.
   - Dieselbe Stufenform zeigt das Moment je Ecke (Gruppen v_2 bis v_4, v_5 bis v_7, v_8 bis v_10, v_11 bis v_13). Sie
     haengt also nicht an der Zuordnung der Staebe zu Tetraedern.
2. **Vorab:**
   - TKe0 eingetroffen, TKe1 nicht, TKe2 nicht, TKe3 eingetroffen, jeweils gleich bei N = 10 und 16.
   - TKe1 scheitert an der ersten Stufe: Streng fallend ist das Moment nur ueber vier Tetraeder.
   - TKe2 scheitert an R^2 = 0,83; das Verhaeltnis 2,12 liegt im vorhergesagten Fenster (2 bis 30).
   - Keine vorab festgelegte Bedeutung ist ausgeloest (siehe unten).
3. **Muster:**
   - Im Defekt-Tetraeder wie in TETRA-STAB: Defektstab (v_0, v_1) unter Zug (+0,59 B/L^2), die vier Nachbarn unter Druck
     (-0,10 bis -0,22), der Gegenstab (v_2, v_3) unter Zug (+0,22).
   - Dahinter wechseln Zug und Druck oft: 19 Vorzeichenwechsel in allen drei Stabfamilien. In der Familie (i, i+2)
     wechselt das Vorzeichen in Dreiergruppen (+ + +, - - -, + + +).
   - Die Kraefte klingen wie die Momente ab (Mittel 1,90 je Tetraeder, nicht gewertet).
4. **Kontrollen bestanden:**
   - Ohne Defekt spannungsfrei (|tau| <= 8e-14, |F| <= 1,2e-10).
   - Gleichgewicht je Verbinder <= 1,1e-9; Reaktion am festen v_14 <= 1e-10. Das Gebilde haelt sich selbst im
     Gleichgewicht.
   - Der TETRA-STAB-Defektfall d_20 wird mit dem neuen Code auf 2,8e-10 reproduziert.
   - Gitter N = 10 gegen 16: Abweichung bis 2,9 % (k <= 8), Urteile gleich.
   - Das feste Ende wirkt nur auf die letzten drei Tetraeder: M = 12 gegen 16, k <= 8 auf 1,4e-3.
   - Stabil: Hesse-Matrix positiv definit.
5. **In echten Groessen** (Knicklicht 20 cm, 5 mm, voller LDPE-Stab angenommen, B ~ 7,7e-3 N m^2, also
   B/L = 38,5 N mm und B/L^2 = 0,19 N; Groessenordnung):
   - Am Defekt bis 12,5 N mm Moment (Biegespannung ~1,0 MPa) und 0,11 N Kraft.
   - Bei k = 2 (13 cm weiter entlang der Achse) 0,6 N mm; bei k = 5 (32 cm) 0,05 N mm; bei k = 8 (51 cm) 0,004 N mm.
   - Abklinglaenge ~8 cm entlang der Achse; Faktor ~10 je 19 cm, also etwa je Stablaenge.

## Vorab gegen Ausgang

Mechanisch nach PLAN.md (Zuordnung Stab (i, j) -> Tetraeder k = max(0, j - 3); Messschwelle s = 2e-8 bei N = 10,
3,9e-8 bei N = 16).
Die Urteile stehen in lauf-69/auswertung.json.

| Nr | Vorhersage | Wahrsch. | Ausgang |
|---|---|---|---|
| TKe0 | Ohne Defekt spannungsfrei: alle \|tau\|, \|F\| L < 1e-8 B | 90 % | **eingetroffen**: \|tau\| <= 8,2e-14, \|F\| <= 1,2e-10 (N = 10 und 16) |
| TKe1 | Das groesste Endmoment je Tetraeder faellt mit dem Abstand vom Defekt ueber mindestens sechs Tetraeder monoton | 70 % | **nicht eingetroffen**: streng fallend nur k = 0 bis 3 (vier Tetraeder); T_4/T_3 = 1,032 (N = 16) bzw. 1,033 (N = 10) |
| TKe2 | Der Abfall ist exponentiell (log-linearer Fit ueber Tetraeder 2 bis 8 mit R^2 > 0,95), Verhaeltnis je Tetraeder zwischen 2 und 30 (Abklinglaenge 0,29 bis 1,44 Tetraeder) | 55 % | **nicht eingetroffen**: R^2 = 0,830 (beide N). Verhaeltnis 2,120 (N = 16) bzw. 2,125 (N = 10), im Fenster; Abklinglaenge 1,33 Tetraeder |
| TKe3 | Die Axialkraft der Staebe wechselt entlang der Kette mindestens einmal das Vorzeichen | 50 % | **eingetroffen**: 19 Wechsel ausserhalb von Tetraeder 0 (Familie (i, i+1): 7, (i, i+2): 3, (i, i+3): 9), beide N |

**Bedeutung (vorab festgelegt) und was davon ausgeloest ist:**
- Fall "TKe1 und TKe2 treffen ein" (abgeschirmt, Abklinglaenge um ein Tetraeder, wie ein massives Feld [H]): **nicht
  ausgeloest**, beide sind nicht eingetroffen.
- Fall "TKe2 trifft nicht ein, weil der Abfall langsamer ist (Potenzgesetz); die Kette traegt die Spannung weit":
  **nicht ausgeloest**.
  - TKe2 scheitert nicht an der Geschwindigkeit, sondern an der Stufenform. Das mittlere Verhaeltnis 2,12 liegt im
    vorhergesagten Fenster.
  - Ein Potenzgesetz passt schlechter: log-log-Fit k = 2 bis 8 mit R^2 = 0,74 (Exponent 3,1) gegen 0,83 log-linear.
  - Ueber die ganze Kette faellt das Moment um den Faktor 15 000. Weit traegt die Kette die Spannung also nicht.
- Die Karte sah den Fall "schnell, aber in Stufen" nicht vor. Ich ersetze keine Bedeutung. Beschreibend gilt: Die
  Spannung bleibt in der Naehe des Defekts, ihre Huellkurve faellt etwa wie 2,1^(-k). Ob man das "abgeschirmt wie ein
  massives Feld" nennen darf, bleibt [H].
- Gegenbild WINKELFELD-1 (Kontinuum, 3D-Scharnierquelle, Kopplung ~ d^(-2,4) bis d^(-2,7)): Die Kette verhaelt sich
  anders, sie ist ein schlankes Tragwerk mit endlichem Querschnitt [H].

## Lesart [H] (nachtraeglich)

- **Warum so schnell:**
  - Mit Gelenken statt Einspannungen waere die Tetrahelix statisch bestimmt (3V - 6 = 39 Staebe). Jeder Schnitt im
    Inneren (hinter Ecke i, 2 <= i <= 11) trennt genau sechs Staebe.
  - Eine in sich ausgeglichene Last erzeugt dann hinter dem Schnitt keine Stabkraft (sechs Gleichungen, sechs
    Unbekannte). Ein reines Gelenk-Stabwerk traegt den Defekt also gar nicht weiter.
  - Weiter kommt die Spannung nur ueber die Einspannmomente. Die Kraefte folgen den Momenten, weil sie in jedem Schnitt
    deren Querkraefte ausgleichen muessen.
- **Abschaetzung nach Hardy Cross (Momentenausgleich [L]):**
  - Die Staebe sind laengs sehr steif, die Sehnen bleiben fast fest. Jeder innere Verbinder dreht sich dann gegen sechs
    Staebe.
  - Ein Stab gibt die Haelfte seines Endmoments an das andere Ende weiter; auf sechs Staebe verteilt erhaelt jeder
    Nachbar 1/12.
  - Die Gleichung 12 phi_q + Summe_(d = 1..3) (phi_(q+d) + phi_(q-d)) = 0 hat zwei Arten abklingender Loesungen:
    - lambda = 0,46 e^(+-i 69 Grad) je Ecke, also Verhaeltnis 2,18, mit schwingendem Vorzeichen
    - lambda = -0,40, also Verhaeltnis 2,49, mit Vorzeichenwechsel je Ecke
  - Das passt zum gemessenen Mittel 2,12 und zu den vielen Vorzeichenwechseln (TKe3).
  - Die Stufen koennen aus der Ueberlagerung dieser Loesungen kommen. Dass sie genau drei Ecken lang sind, erklaert die
    Skalar-Rechnung nicht sicher: Die Phase 69 Grad gaebe Stufen von etwa 2,6 Ecken (180/69). Die Helix dreht je Ecke
    um 131,8 Grad, fast ein Drittel Umlauf. Das ist offen.
  - Die Rechnung ist von Hand gemacht und nicht im Code geprueft. Ich hatte sie vor den Laeufen im Kopf, aber nicht
    aufgeschrieben; sie zaehlt deshalb als nachtraeglich.

## Je Tetraeder k (Defekt 10 Grad, M = 12, v_14 fest)

- T_k: groesstes |tau| der zugeordneten Staebe (beide Enden), in B/L.
- F_k: groesste |F|, in B/L^2.
- Vorzeichen: Axialkraft der zugeordneten Staebe in der Reihenfolge der Spalte "Staebe" (+ Zug, - Druck), N = 16. Alle
  Werte liegen ueber der Messschwelle.
- Echt: T_k in N mm (x 38,5).

| k | Staebe | T_k (N = 16) | T_k (N = 10) | F_k (N = 16) | Vorzeichen | T_k echt (N mm) |
|---|---|---|---|---|---|---|
| 0 | (0,1) (0,2) (0,3) (1,2) (1,3) (2,3) | 0,3235 | 0,3226 | 0,595 | + - - - - + | 12,5 |
| 1 | (1,4) (2,4) (3,4) | 0,1230 | 0,1228 | 0,189 | + - - | 4,7 |
| 2 | (2,5) (3,5) (4,5) | 0,01577 | 0,01556 | 0,0263 | - + - | 0,61 |
| 3 | (3,6) (4,6) (5,6) | 0,01301 | 0,01284 | 0,0207 | + + - | 0,50 |
| 4 | (4,7) (5,7) (6,7) | 0,01342 | 0,01327 | 0,0223 | - + - | 0,52 |
| 5 | (5,8) (6,8) (7,8) | 1,419e-3 | 1,385e-3 | 3,41e-3 | - - + | 0,055 |
| 6 | (6,9) (7,9) (8,9) | 1,542e-3 | 1,506e-3 | 2,88e-3 | + - - | 0,059 |
| 7 | (7,10) (8,10) (9,10) | 1,650e-3 | 1,615e-3 | 2,46e-3 | - - + | 0,064 |
| 8 | (8,11) (9,11) (10,11) | 1,159e-4 | 1,125e-4 | 5,45e-4 | + + - | 0,0045 |
| 9 | (9,12) (10,12) (11,12) | 1,970e-4 | 1,905e-4 | 5,37e-4 | - + + | 0,0076 |
| 10 | (10,13) (11,13) (12,13) | 2,143e-4 | 2,077e-4 | 3,25e-4 | + + - | 0,0083 |
| 11 | (11,14) (12,14) (13,14) | 2,170e-5 | 2,088e-5 | 2,85e-5 | - + + | 0,0008 |

- Verhaeltnis T_k/T_(k+1) (N = 16): 2,63; 7,80; 1,21; 0,97; 9,46; 0,92; 0,93; 14,2; 0,59; 0,92; 9,87.
- Verhaeltnis T_k/T_(k+3) (N = 16, k = 2 bis 7): 11,1; 8,4; 8,1; 12,2; 7,8; 7,7.
- Moment je Ecke (N = 16, nicht gewertet), v_0 bis v_14: 0,257; 0,323 | 0,072; 0,076; 0,050 | 7,6e-3; 5,4e-3; 5,3e-3 |
  6,4e-4; 6,6e-4; 6,3e-4 | 4,3e-5; 9,2e-5; 6,3e-5 | 5,5e-6.
- Defekt-Tetraeder (N = 16): Der Defektstab ist ein flacher Bogen (Stich 0,034, Sehne 0,9969); sein groesstes Moment
  sitzt am Ende bei v_1 (0,323; bei v_0: 0,257). Der Gegenstab (v_2, v_3) traegt fast kein Moment (0,009), aber Zug.

## Kontrollen

- **TKe0** (ohne Defekt): siehe Tabelle; Newton endet nach 2 (N = 10) bzw. 1 (N = 16) Schritt am Rundungsboden.
- **Gleichgewicht** je freiem Verbinder:
  - Kraftsumme <= 3,9e-10 (M = 12) bzw. 1,1e-9 (M = 16), Momentsumme <= 4,1e-13.
  - Reaktion am festen Verbinder: Kraft <= 1,9e-10, Moment <= 8,6e-11.
  - Gradient am Ende <= 2,0e-9 (M = 12) bzw. 4,4e-9 (M = 16), Rundungsboden.
  - Defektlaeufe: Newton 8 bis 9 Schritte. In den Kettenlaeufen nie verschoben (Hesse-Matrix entlang des Wegs positiv
    definit), in der Gegenprobe g_20 einmal (mu bis 0,93; Start weit vom Bogenzustand).
- **Gitter N = 10 gegen 16:**
  - T_k weicht um 0,3 % (k = 0) bis 2,9 % (k = 8) und 3,8 % (k = 11) ab, N = 10 stets kleiner.
  - Fit-Verhaeltnis 2,125 gegen 2,120, R^2 0,8297 gegen 0,8298; alle Urteile gleich.
  - Der Plan erwartete < 1 % (Selbstanzeige).
- **Randkontrolle M = 12 gegen M = 16** (N = 10): k <= 8 auf <= 1,4e-3; k = 9, 10, 11: +1,7 %, -4,4 %, +8,4 %. Das feste
  Ende wirkt also nur auf die letzten drei Tetraeder, nicht auf den Fitbereich.
- **Gegenprobe:**
  - Ein Tetraeder (M = 1, N = 20, Grundneigung 5 Grad, Defekt 10 Grad, v_0 fest) gegen TETRA-STAB d_20: groesste
    Abweichung 2,8e-10 ueber |tau| (beide Enden), Axialkraft und Sehne aller sechs Staebe.
  - Reproduziert. Schon im Rauchlauf stimmte der Fall 3/6 Grad (N = 40) mit TETRA-STAB r3c auf <= 3e-9.
- **Geometrie:** Kantenlaengen auf 1,1e-15 gleich 1, Volumen je Tetraeder auf 7e-16 regulaer.
- **Stabilitaet:**
  - Kleinste Hesse-Eigenwerte 0,0017; 0,0023; 0,033; dann 2,66 (N = 16), bei N = 10 0,0028; 0,0037; 0,051; 2,84.
  - Positiv definit, also stabil. Die drei weichen Richtungen sind vermutlich Biegung und Drillung der einseitig
    gehaltenen Kette [H].
  - Die Zahlen haengen von N ab, weil die Koordinaten nicht massegewichtet sind; aussagekraeftig ist nur das Vorzeichen.
- **Nicht gewertet:**
  - Fit der Kraefte k = 2 bis 8: Verhaeltnis 1,90, R^2 0,90.
  - Zuordnung nach Mitgliedschaft: T_3 = T_4 exakt (dasselbe Stabende, der im Plan befuerchtete Gleichstand), streng
    fallend ebenfalls nur vier Tetraeder; Fit Verhaeltnis 2,00, R^2 0,87.
  - Das Scheitern von TKe1 haengt also nicht an der Zuordnung.

## Latten (v3)

- L1: ja. TKe1 und TKe2 sind gescheitert.
- L2: ja. Kontrolle ohne Defekt; derselbe Code reproduziert TETRA-STAB d_20 auf 2,8e-10.
- L3: ja. Gitter N = 10 und 16 (Urteile gleich, Profil auf <= 3,8 %), Kettenlaenge M = 12 und 16.
- L4: teilweise.
  - Exponentielles Abklingen ausgeglichener Lasten in schlanken, periodischen Tragwerken ist bekannt (Saint-Venant;
    Abklingraten aus der Uebertragungsmatrix) [L].
  - Fuer die Stufenform der Tetrahelix mit eingespannten Ecken nicht gesucht (Websuche erschoepft).
- L5: nein. Ein Handversuch mit Knicklichtern waere moeglich, die Momente fallen aber schon ab k = 2 unter 1 N mm.

## Literatur [L, aus dem Gedaechtnis, Angaben nicht nachgeprueft]

- Saint-Venant-Prinzip: R. A. Toupin, Arch. Rational Mech. Anal. 18 (1965) 83; C. O. Horgan, J. K. Knowles, Adv. Appl.
  Mech. 23 (1983) 179.
- Gelenk-Stabwerke: N. G. Stephen, P. J. Wang, Int. J. Solids Struct. 33 (1996) 79 ("On Saint-Venant's principle in
  pin-jointed frameworks"). Abklingraten aus den Eigenwerten der Uebertragungsmatrix einer Wiederholungseinheit.
- Momentenausgleich: H. Cross, Proc. ASCE 56 (1930), Fortleitungszahl 1/2.
- Tetrahelix: A. H. Boerdijk, Philips Res. Rep. 7 (1952) 303; H. S. M. Coxeter, Canad. Math. Bull. 28 (1985) 385;
  R. B. Fuller, Synergetics (1975), "Tetrahelix".

## Selbstanzeigen

- Der Rauchlauf rauch1 (M = 4, Defekt 7 Grad, v_6 fest) zeigte vor dem Einfrieren den Verlauf k = 0 bis 3 einer kurzen
  Kette (0,221; 0,084; 0,012; 0,0075). Die Auswerteregeln standen vorher fest (04:06:35 gegen Laufbeginn 04:07:31).
- Zwei Festlegungen habe ich im Plan selbst getroffen: die eindeutige Zuordnung (kleinstes k) und TKe3 nur ausserhalb
  von Tetraeder 0, je Stabfamilie. Beide Urteile halten auch mit den anderen Lesarten:
  - Nach Mitgliedschaft und je Ecke faellt T ebenfalls nicht monoton.
  - Die dominante Axialkraft je Tetraeder hat die Vorzeichenfolge + - + - + + + - - - - + (beide N).
- Die Gittererwartung im Plan (< 1 %) war zu knapp; gemessen bis 2,9 % im Fitbereich. Das war kein Kriterium.
- Die Hardy-Cross-Abschaetzung ist nachtraeglich (siehe Lesart).
- Newton endete am Rundungsboden (Gradient bis 4,4e-9), nicht bei 1e-13. Der Plan sah das vor. Die Messschwelle
  (2e-8 bzw. 3,9e-8) liegt mehr als zwei Groessenordnungen unter allen gewerteten Werten (kleinstes T im Fitbereich
  1,1e-4, kleinste Axialkraft 7,8e-6).
- Grenzen: keine Torsion, ideal starre Verbinder, kein Eigengewicht, keine Reibung, nur ein Defektort (v_0, v_1).
  Die Knicklicht-Zahlen nehmen einen vollen Stab an. Ob die Lage der Stufen vom Defektort relativ zu den drei Straengen
  der Helix abhaengt, ist nicht geprueft.

## Einfach gesagt

Wir haben am Rechner eine gedrehte Kette aus 12 Tetraedern gebaut, aus 39 biegsamen Staeben, und nur einen einzigen
Stab am Anfang schief eingesteckt. Die Spannung, die dieser eine Stab erzeugt, wird entlang der Kette schnell kleiner:
etwa alle drei Tetraeder auf ein Zehntel, und am Ende ist fast nichts mehr davon uebrig. Sie nimmt aber nicht
gleichmaessig ab, sondern in Stufen, und Zug und Druck wechseln sich dabei immer wieder ab. Weil wir ein gleichmaessiges
Abklingen vorhergesagt hatten, trafen zwei unserer vier Vorhersagen nicht ein. Ein Fehler in einer solchen Kette stoert
also vor allem seine Nachbarschaft und kaum das ferne Ende.
