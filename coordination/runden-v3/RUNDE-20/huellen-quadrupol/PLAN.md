# PLAN HUELLEN-QUADRUPOL (Runde 20)

- Code-Agent, Start 2026-10-02 17:08:14 CEST (date). Plan geschrieben ab 17:20:06 CEST (date), vor jedem .69-Lauf.
- Verbindlich aus der Karte: Linearisierung mit l = 2, K1 (l = 1 und l = 0), Suche (M2, E1, omega^2 0,80 bis 1,40,
  zwei Gitterstufen, Zaehlung wie Vorlaeufer, Rechteck-Umlauf an allen Funden), Versatzdefinition, Q0 bis Q3,
  Bedeutung. Nichts davon wird nach dem Ergebnis geaendert. Was die Karte offen laesst, lege ich hier vorab fest und
  kennzeichne es als **[Plan]**.
- Gelesen: KARTE; RUNDE-19/huellen-dipol (KARTE, PLAN, ERGEBNIS, code/, aus/); RUNDE-18/huellen-leiter (ERGEBNIS, aus/);
  RUNDE-19/huellen-leiter-3/FREMDSTIMME.md. Selbstanzeige: Ordnerliste (nur Namen) von RUNDE-19/huellen-dipol/hilfs/
  gesehen, keine Datei daraus geoeffnet.
- Code (code/): quadrupol.py (eigen, aus dipol.py abgeleitet), auswertung_quadrupol.py (eigen, aus
  auswertung_dipol.py abgeleitet). Unveraendert importiert (sha256 wie Runde 18/19): stille3.py 1d15a38c...,
  huellen_leiter.py 68c0a1fb..., beutel.py f831e818..., auswertung.py 782058b1.... dipol.py und auswertung_dipol.py
  liegen nur als Vorlage daneben (nicht ausgefuehrt).

## 1 Linearisierung l = 2

- Hintergrund: radiales Profil wie Runde 18/19 (l = 0, unveraendert).
- Stoerung wie Code 1 und HUELLEN-DIPOL, Winkelteil jetzt Y_2m (reell): Kanaele a (w + rho, offen in E1),
  b (w - rho, zu), c' = c/2 (zu in E1). Radial u = r a usw.: u'' = (M(r) - E + l(l+1)/r^2) u mit M, E wie Code 1 und
  **l(l+1) = 6 in allen drei Kanaelen**. Schwellen und Bereiche unveraendert (gegen 2).
- **Regulaer am Ursprung (a, b, c ~ r^2, also u ~ r^3):** Start bei r0 = 2 hp mit derselben Reihe wie HUELLEN-DIPOL,
  allgemein u = r^(l+1) [v + r^2 V0 v / (2(2l + 3))], fuer l = 2: Nenner 14 (Ableitung: (l+3)(l+2) - l(l+1) = 4l + 6).
  Startfehler liegen im regulaeren Unterraum (aendert die Basis, nicht den Rang von G) oder in der singulaeren Loesung
  ~ r^-2, die gegen die regulaere wie (r0/r)^5 abklingt.
- **Abklingend (b, c) am Startradius:** u = r k_2(kappa r) ~ e^{-x}(1 + 3/x + 3/x^2), x = kappa r; normiert u = 1,
  u'/u = -(x^3 + 3x^2 + 6x + 6) / (R (x^2 + 3x + 3)) (Rechnung: u'' = (kappa^2 + 6/r^2) u geprueft). l = 0, 1 wie
  bisher. Offener Kanal a: keine Randbedingung (wie Code 1). Die E1-Messgroesse braucht keine Hankel-Asymptotik des
  offenen Kanals: Z_b, Z_c haben ausserhalb des Balls keine a-Komponente, das gilt fuer jedes l. werte_E2/werte_E3
  (l = 0-Asymptotik) werden nicht benutzt.
- **Umsetzung:** quadrupol.py ersetzt zur Laufzeit dieselben drei Kanalfunktionen wie dipol.py (HL.werte_k, S3.regulaer,
  S3.abklingend), l wird je Aufruf gesetzt (ell=0, 1 oder 2). Fuer l = 0 und l = 1 ist der Rechenweg woertlich der von
  Code 1 bzw. dipol.py (l = 0: Selbsttest von Runde 19 bitgleich). Alles andere (Zeilen, rho-Gitter, Nullstellen,
  Illinois, Rang, Unterzeilen, Halbierung, Zellen-Umlauf, Newton, Rechteck-Umlauf) ist unveraenderter Vorlaeufercode.
- **Triviale Moden:** Bei l = 2 gibt es keine Symmetriemoden (Translation ist l = 1, Phase und d/dw sind l = 0; Drehungen
  wirken auf den kugelsymmetrischen Ball trivial). Abgetastet wird ohnehin nur rho >= sqrt2 - w + 1e-4.

## 2 Messgroesse und Zaehlung (wie Vorlaeufer)

- W = m_ac + i m_bc, Zeile, Nullstellen von m_bc, Illinois, Unterzeilen (1/8), zwei Halbierungen, Zellen-Umlauf,
  "Stelle" (beide Stufen, gleiche Kurve, gleiches Zeilenpaar, Lage auf 1/16 Zeilenabstand, Zellen-Umlauf +-1 gleich,
  ohne Merker weg/steig/Rangsprung nach Plan-Regel/umlauf0): woertlich HUELLEN-DIPOL PLAN 2 (= Runde-18-PLAN 3 und 4),
  Auswertefunktionen aus auswertung.py (Runde 18) unveraendert.

## 3 Kurvenordnung (vorab begruendet)

- **Kriterium: k = Rang der Nullstelle von m_bc in der Zeile, von unten gezaehlt** (HUELLEN-DIPOL Abschnitt 6, Runde 18).
  Das haengt nicht an der Knotenzahl und wird uebernommen. Stuetzende Pruefungen (wie Vorlaeufer, berichtet): keine
  Abnahme der Nullstellenzahl zur Schranke hin, kein Rangsprung nach Plan-Regel, gleiche Zahl, Lage und Vorzeichenfolge
  auf beiden Stufen, Stetigkeit der Lage laengs der Kurve (Unterzeilen-Annahme |Newton - Gerade| < 0,3 Luecke).
- Knotenzahl der c-Komponente nur berichtet, **nirgends als Bedingung** (Lehre FREMDSTIMME Runde 19).
- Vergleich mit l = 0 und l = 1: Kurve gleichen Rangs k (Karte: "derselben Kurvenordnung", wie HUELLEN-DIPOL).

## 4 K1 (vor der Suche) und Probe l = 2

- **K1 mit demselben Code** (quadrupol.py, Modell M2, ell=0 bzw. ell=1), je Stufe 1 und 2. Fuer jede Referenzstelle:
  Zeilen i und i+1 und Paar i mit HL.cmd_block (Kette der Suche), auf Kurve k der Punkt mit kleinstem |omega^2 -
  Referenz|, dann Newton und Rechteck mit HL.cmd_umlauf (Anker wie Suche). Referenzen (ref/k1-referenz.json, per jq aus
  den Vorlaeuferdateien gezogen, Newton-Lagen Stufe 1):
  - l = 0 (Runde 18, Anhang A Nr 1, 5, 9 = Runde-17 Nr 15, 11, 7): k = 0, 1, 2; Paar 24, 50, 56; R = 3,2 / 8,4 / 11,8.
  - l = 1 (HUELLEN-DIPOL Nr 1, 5, 14): k = 0, 1, 2; Paar 32, 55, 66; R = 4,1 / 11,4 / 17,1.
- **Bestanden (Q0)**, je Stelle auf beiden Stufen: Punkt auf Kurve k in Paar i gefunden (ohne weg, steig != 0), Newton
  konvergiert, |d omega^2| und |d rho| <= 1e-6 zur Referenz, Rechteck-Umlauf aufgeloest und gleich dem
  Referenz-Umlauf, Zellen-Umlauf gleich dem Referenz-Umlauf. Alle 6 Stellen auf beiden Stufen -> K1 bestanden.
  [Plan: "wiederfinden" = Lage und Umlauf, wie HUELLEN-DIPOL D0.]
- **Suche nur nach bestandenem K1** (die Kette prueft das per jq vor dem ersten Block). Scheitert K1 an einem
  Programmfehler: beheben, sha256 dokumentieren, K1 neu; das Verfahren bleibt.
- **Probe l = 2 (nur berichtet, keine Bedingung) [Plan]:** K1 prueft die l = 2-eigenen Teile (Start r^3, k_2-Start)
  nicht. Darum auf Stufe 1 in den Zeilen 40, 60, 71 (omega^2 = 1,00 / 0,832 / 0,80) die Nullstellen von m_bc mit dem
  Standard gegen r0 = 4 hp und gegen den Abklingstart am Gebietsrand (statt n_start) vergleichen: Zahl, Vorzeichenfolge,
  max |d rho|, max relative |d s|.

## 5 Suche

- Profile wie Runde 18/19 (HL.cmd_profile, Saat BEUTEL Q = 200), Stufe 1 hp = 0,01, Stufe 2 0,005.
- Zeilen: dieselbe Liste wie HUELLEN-DIPOL (72 Zeilen, 1,40 bis 0,80; Runde-18-Regel mit Untergrenze 0,80). Die
  erzeugte zeilen.json wird per sha256 mit der Dipol-Liste verglichen.
- Bloecke von 1,40 abwaerts (HL.cmd_block, ell=2): Stufe 1 Zeilen 0 bis 71; Stufe 2 Zeilen 0 bis 40 und 40 bis 71.
  Jeder Aufruf < 600 s; jede Zeile und jedes Paar sofort als JSON; Fortsetzung mit demselben Aufruf.
- Gewertet wird der zusammenhaengende Bereich ab 1,40 bis zur tiefsten Zeile, bis zu der auf beiden Stufen alle Paare
  vorliegen (wie HUELLEN-DIPOL PLAN 5). Untergrenze wird berichtet ("wie weit gekommen").

## 6 Abstaende und Versatz (vorab festgelegt)

- Lagen: R = Huellenradius (chi = 1/2) der Stelle, Stufe 1. l = 0: gezaehlte Stellen im gewerteten Bereich von Runde 18
  (ref/l0-stellen-r18.json = RUNDE-18 aus/laeufe/stellen.json, volle Stellenzahl). l = 1: gezaehlte Stellen von
  HUELLEN-DIPOL (ref/l1-stellen-r19.json = RUNDE-19 aus/laeufe/stellen.json). l = 2: diese Suche.
- **Abstand** je Kurve: Delta R benachbarter Stellen derselben Kurve, Mittel, CV = Std (n - 1) / Mittel.
- **Versatz (Karte):** Fuer jede Stelle (l = 1 oder 2) mit Lage R auf Kurve k und den l = 0-Lagen R0_0 < R0_1 < ... der
  Kurve k: j = groesster Index mit R0_j <= R; v = (R - R0_j) / (R0_(j+1) - R0_j), modulo 1, in [0, 1). "Abstand" ist also
  der auf R0_unten folgende l = 0-Abstand (wie die 0,34 bis 0,47 in HUELLEN-DIPOL). [Plan, Rand:] Liegt R unter der
  ersten l = 0-Lage, gilt der erste Abstand (j = 0, v_roh < 0, dann modulo 1); liegt R ueber der letzten, der letzte.
  Kurven mit weniger als zwei l = 0-Lagen: kein Versatz. Fuer l = 0 ist v = 0 per Definition.
- Schreibtischprobe (vor dem Einfrieren, jq, hilfs/versatz.jq auf ref/): l = 1, k = 0 ergibt v = 0,344; 0,403; 0,430;
  0,445; 0,454; 0,461; 0,466, also die 0,34 bis 0,47 aus HUELLEN-DIPOL. Die Definition trifft den Vorlaeufer. (Die
  l = 1-Werte der Kurven k >= 1 sind damit schon gesehen; sie sind Bericht, keine Vorhersage.)
- **"im Mittel" (Q3) [Plan]:** Weil v modulo 1 definiert ist, ist nur der Kreismittelwert eindeutig:
  v_quer = arg(Summe exp(2 pi i v)) / (2 pi), modulo 1, ueber alle gezaehlten l = 2-Stellen mit Versatz (alle Kurven
  zusammen). Daneben berichtet: arithmetisches Mittel, kleinstes und groesstes v, Laenge des Mittelvektors, Werte je
  Kurve. Gewertet wird nur der Kreismittelwert.

## 7 Rechteck-Umlauf an allen Funden

- Je Stufe an allen Funden im gewerteten Bereich: alle gepaarten Stellen (gezaehlt oder nicht) mit der Lage dieser
  Stufe, dazu Funde nur einer Stufe. Newton und Rechteck wie Vorlaeufer (HL.cmd_umlauf, Halbbreite min(1e-3;
  0,4 Schwellenabstand; 0,25 Luecke; 0,5 Zeilenabstand)). Berichtet: Rechteck-Umlauf = Zellen-Umlauf je Stelle und
  Stufe. Gezaehlt wird wie im Vorlaeufer mit dem Zellen-Umlauf; jede Abweichung wird einzeln berichtet.

## 8 Wertung Q0 bis Q3 (vorab operationalisiert)

- **Q0:** Abschnitt 4 (alle 6 Stellen auf beiden Stufen).
- **Q1:** N = Zahl der Stellen im gewerteten Bereich mit 0,80 <= omega^2 <= 1,40. Eingetroffen bei N >= 5; nicht
  eingetroffen, wenn der Bereich bis 0,80 reicht und N < 5; offen, wenn er nicht bis 0,80 reicht und N < 5.
- **Q2 [Plan, wie HUELLEN-DIPOL D2/D3]:** Kurven mit >= 4 Stellen (>= 3 Abstaende). Je Kurve (a) CV < 0,10 und
  (b) |q_k - 1| <= 0,05 mit q_k = mittlerer Abstand l = 2 / mittlerer l = 0-Abstand derselben Kurve k, gemittelt ueber
  die l = 0-Abstaende mit Paarmitte in [R_min, R_max] der l = 2-Stellen der Kurve (keiner darin: der mit naechster
  Paarmitte). Eingetroffen, wenn es mindestens eine solche Kurve gibt und alle (a) und (b) erfuellen; nicht eingetroffen,
  wenn eine (a) oder (b) verfehlt; offen ohne solche Kurve.
- **Q3:** Eingetroffen, wenn 0,6 <= v_quer < 1,0 (v_quer = 0 entspricht 1,0 und zaehlt mit); nicht eingetroffen sonst;
  offen ohne Stelle mit Versatz.
- Berichtet, nicht gewertet: Abstaende, q und Versatz fuer l = 1 (alle 19 Dipol-Stellen) gleich definiert; l = 0
  Abstaende je Kurve (Versatz 0 per Definition); Geburt der Kurven; Knotenzahlen.

## 9 Vorabpruefung der Pflichtbedingungen (vor dem Einfrieren, nur Lesen der Vorlaeuferausgaben)

- K1-Stellen in den Vorlaeufer-Paardateien (genau dieser Code: Runde-18-Kette fuer l = 0, dipol.py-Kette fuer l = 1):
  in allen 12 Faellen (6 Stellen x 2 Stufen) genau ein Punkt im Paar, auf der erwarteten Kurve k, weg = false,
  steig != 0, Zellen-Umlauf = Referenz-Umlauf. Rechteck an allen sechs im ersten Versuch aufgeloest (Halbbreite 1e-3).
  Newton Stufe 2 gegen Stufe 1 der Referenzen <= 3e-9, also weit unter 1e-6.
- Die Runde-18-Paardateien 24, 50, 56 stammen aus der Codefassung vor Nachtrag 1 (version 1); die Lage aendert das
  nicht merklich, die Bedingung ist auf Newton-Lage und Umlauf gestellt, nicht auf Bitgleichheit der Zelle.
- Q1 bis Q3 sind nicht vorab ableitbar: l = 2 ist nie gerechnet. Beide Ausgaenge sind moeglich (Schreibtisch, nur
  Groessenordnung [H]: Nullstellen von j_2 liegen 0,83 bis 0,95 Abstaende hinter n pi, ihre Abstaende 1 bis 6 % ueber
  pi; bei l = 1 lagen die Kurven k >= 1 aber deutlich unter der Bessel-Lesart).

## 10 Laeufe (.69, kleintest.sh, nur Spur cpu6, nacheinander, je < 600 s)

- V0: py_compile aller Dateien; Zeilenliste.
- V1: Profile Stufe 1 und 2; K1 l = 0 und l = 1 je Stufe 1 und 2; Probe l = 2 (Stufe 1). Pruefung K1 (jq), sonst Halt.
- V2: Bloecke l = 2 (Abschnitt 5), Fortsetzung bei Abbruch.
- V3: Auswertung Stellen; Rechteck an allen Funden Stufe 1 und 2; Endauswertung (Q0 bis Q3).
- Programmfehler werden behoben und mit sha256 dokumentiert, das Verfahren bleibt. Folgelaeufe mit Verfahrensbezug nur
  mit eingefrorenem PLAN-NACHTRAG-n.md, als nachtraeglich markiert.

## 11 Bedeutung (woertlich Karte)

- Treffen Q1 bis Q3 ein: Eine Sprossenregel fuer alle l, R_n,l ~ (n + l/2 + konst) pi/k_innen [H].
- Trifft Q3 nicht ein: Der Versatz hat eine andere Ursache.
