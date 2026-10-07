# TETRA-STAB: Tetraeder aus leicht nach innen gebogenen Staeben, Spannungen an den Kontaktpunkten (Runde 24)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 01:36:25 CEST (date), vor jeder Rechnung.
- Finn, ~01:35: "Mach mal ein Modell Tetraeder aus leicht gebogenen nach innen Knicklichter artigen Dingern und rechne mit
  Spannungen bei den jontaktpunkten".
- Projekt-grep (fuenfte Probe) nach "Tetraeder":
  - WINKELFELD-1 (Kuhn-Tetraeder, Scharnierquelle)
  - URSUPPE-1 (Graphen)
  - Codex "Tetraeder-Aussenwirkung" (skalare Punktquellen)
  - Ein Stabmodell mit Kontaktpunkten gibt es nicht.

## Modell (Festlegung der Leitung)

- **Sechs Staebe ("Knicklichter")**, elastisch, isotroper Querschnitt, von Natur aus gerade, fast undehnbar.
  - Biegesteifigkeit B, Laenge L.
  - Diskret: N Segmente je Stab, Biegeenergie (B/l0) Summe (1 - t_i . t_(i+1)), Dehnung steif.
- **Vier Kontaktpunkte** (Ecken) als starre Verbinder mit Lage und Drehung. Jeder Verbinder haelt die drei Stabenden in
  festen Richtungen (eingespannt).
  - Um die eigene Achse duerfen sich die Staebe drehen (keine Torsion).
- **"Leicht nach innen gebogen":** Die Einspannrichtungen sind gegen die geraden Kanten des regulaeren Tetraeders um den
  Winkel alpha zur Tetraedermitte geneigt.
  - Jeder Stab muss deshalb einen nach innen gewoelbten Bogen bilden.
  - Der Verbinder entspricht einem Knicklicht-Verbinder mit etwas zu engem Winkel.
- **Freies Gebilde:** Ein Verbinder ist festgehalten (Lage und Drehung), damit keine Starrkoerperbewegung bleibt. Alles
  andere stellt sich ein.
- **Gemessen je Stabende:**
  - Kraft F (laengs und quer) und Moment tau, die der Stab auf den Verbinder ausuebt
  - je Verbinder: Summe der Kraefte und Momente
  - Stabform: Kruemmung, Kantenlaenge a

## Schreibtisch der Leitung (Vorhersage aus der Elastica)

- **Symmetrischer Fall:** Ein Stab mit nur Endmomenten (keine Endkraefte) hat konstante Kruemmung, ist also ein
  Kreisbogen.
  - Gesamtdrehung der Tangente 2 alpha, daher kappa = 2 alpha/L und Moment M = B kappa = 2 B alpha/L, laengs des ganzen
    Stabs gleich.
  - Endkraefte: null.
  - Kantenlaenge (Sehne): a = (L/alpha) sin alpha.
  - An jeder Ecke stehen die drei Momentvektoren senkrecht zur Achse Ecke-Mitte und sind um 120 Grad gegeneinander gedreht.
    Ihre Summe ist null.
  - Die Kontaktpunkte tragen also reine Biegemomente, die sich aufheben; Kraefte fliessen keine. [Elastica, L: Kreisbogen
    unter Endmomenten]
- **Reale Groessen:**
  - Knicklicht 20 cm lang, 5 mm dick, als voller LDPE-Stab angenommen, E ~ 0,25 GPa. Dann ist I = pi r^4/4 = 3,1e-11 m^4
    und B ~ 7,7e-3 N m^2.
  - Bei alpha = 5 Grad: M ~ 6,7 N mm je Stabende.
  - Biegespannung am Kontaktpunkt sigma = M r/I ~ 0,55 MPa (Groessenordnung; echte Knicklichter sind hohl).
- **Ein Defekt (ein Stab staerker geneigt)** bricht die Symmetrie. Dann heben sich die Momente an seinen Ecken nicht mehr
  auf, die Verbinder drehen sich, und es entstehen Kraefte an allen Kontaktpunkten.

## Tests

- A, symmetrisch: alpha = 0, 5, 10 und 20 Grad.
- B, Defekt: alle alpha = 5 Grad, nur Stab AB an beiden Enden 10 Grad.
- C, Stabilitaet: tiefste Eigenwerte der Hesse-Matrix im Gleichgewicht (Verbinder A fest) bei alpha = 5 und 20 Grad.
- Diskretisierung N = 50 und 100 als Gitterprobe.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TE0 | alpha = 0: spannungsfrei, alle |tau| und |F| L unter 1e-7 B | 95 % |
| TE1 | alpha = 5 Grad: |tau| je Stabende = 2 B alpha/L auf 1 %; |F| L < 1e-3 |tau|; Netto-Moment je Verbinder < 1e-5 |tau|; a = (L/alpha) sin alpha auf 1e-3 | 85 % |
| TE2 | alpha = 20 Grad: dieselben Beziehungen auf 2 % | 75 % |
| TE3 | Defekt AB: (i) groesstes Endmoment an AB; (ii) an allen Kontaktpunkten |F| L >= 1e-3 |tau_AB|; (iii) das Endmoment des Gegenstabs CD aendert sich um < 20 % gegen den symmetrischen Fall | (i) 90 %, (ii) 70 %, (iii) 55 % |
| TE4 | Hesse-Matrix bei alpha = 5 und 20 Grad positiv definit (stabil) | 80 % |

**Bedeutung (vorab):**
- TE1 und TE2 treffen ein: Das nach innen gebogene Tetraeder ist ein vorgespannter Koerper, dessen Kontaktpunkte nur
  Biegemomente tragen; diese heben sich an jeder Ecke auf. Er ist kraftfrei und "neutral".
  - [H, Analogie] Das entspricht einer neutralen Winkelladung (WINKELFELD-1).
- TE3 trifft ein: Ein einzelner "Defekt-Stab" erzeugt Kraefte an allen Kontaktpunkten, die Spannung verteilt sich ueber das
  ganze Tetraeder.
- TE4 trifft ein: Leichte Vorspannung macht es nicht instabil.

## Rahmen

- Explorativ (v3). Die Leitung rechnet selbst auf der .69 (kleintest.sh, CPU-Spur, je Lauf <= 10 min), Code
  code/tetra_stab.py.
- Rauchlauf mit alpha = 3 Grad, das in keinem echten Lauf vorkommt.
- Grenzen: keine Torsion, keine Reibung, Verbinder ideal starr, keine Schwerkraft.

## Laufplan (Nachtrag vor jedem echten Lauf, 2026-10-03 01:52:34 CEST)

- **Rauchlaeufe** (Parameter, die in keinem echten Lauf vorkommen):
  - alpha = 3 Grad, N = 20: tau = 0,104719 gegen soll 0,104720, |F| <= 1,8e-11, a = 0,999544 gegen soll 0,999543; 60 s.
    Nach der Loeseraenderung (L-BFGS mit gtol 1e-7, danach gedaempfter Newton) dasselbe in 91 s.
  - alpha = 3 Grad mit AB 6 Grad, N = 40: Momente 0,087 bis 0,187, Kraefte bis 0,17 B/L^2; 287 s.
  - Die Rauchlaeufe zeigen also schon, dass die Bogen-Vorhersage stimmt und ein Defekt Kraefte erzeugt. Die Vorhersagen
    standen vorher fest.
- **Abweichung von der Karte:** Diskretisierung N = 20 und 40 statt 50 und 100, wegen der Laufzeit (N = 40 dauert ~290 s).
  - Die Bogenloesung ist im diskreten Modell fuer jedes N exakt; die Abweichung von a ist von der Ordnung alpha^2/(6 N^2).
  - TE4 (Hesse-Matrix) wird nur bei N = 20 gerechnet.
- **Laeufe:** s0, s5, s10, s20 (symmetrisch, alpha = 0/5/10/20 Grad) und d (alpha = 5 Grad, AB 10 Grad), je N = 20 und 40;
  Hesse-Matrix bei s5 und s20 mit N = 20.
- **Auswerteregeln:**
  - TE1/TE2 an N = 20 und N = 40, beide muessen gelten.
  - "|F| L < 1e-3 |tau|" ueber alle zwoelf Stabenden.
  - Netto-Moment je freiem Verbinder (B, C, D) und Reaktion am festen Verbinder A.
  - TE3 (iii): tau von CD im Defektfall gegen s5 bei gleichem N.
