# PLAN HUELLEN-DIPOL (Runde 19)

- Code-Agent, Start 2026-10-02 15:41:30 CEST (date). Plan geschrieben ab 15:53 CEST (date), vor jedem .69-Lauf.
- Verbindlich aus der Karte: Linearisierung mit l = 1, K1, Suche (M2, E1, omega^2 0,80 bis 1,40, zwei Stufen),
  Ordnen nach chi-Kurven mit Abstand in R und Vergleich mit l = 0, D0 bis D4, Bedeutung. Nichts davon wird nach dem
  Ergebnis geaendert.
- Gelesen: KARTE; RUNDE-18/huellen-leiter ERGEBNIS, PLAN, PLAN-NACHTRAG-1 bis 4, code/ (huellen_leiter.py,
  auswertung.py, stille3.py, beutel.py, diag_profil.py nicht); RUNDE-17/stille-zweifeld/code/ (nur Hashvergleich);
  RUNDE-10/beweis2/BEWEIS-2.md (Lage der M1-Dipolstelle, Kanalkonvention l = 1).
- Code: code/dipol.py (eigen) importiert code/stille3.py (Code 1), code/beutel.py und code/huellen_leiter.py
  (HUELLEN-LEITER) unveraendert (sha256 1d15a38c..., f831e818..., 68c0a1fb..., gleich Runde 18).

## 1 Linearisierung l = 1

- Hintergrund: radiales Profil wie Runde 18 (l = 0, unveraendert).
- Stoerung wie BEWEIS-2 Satz T2 und Code 1: delta phi = e^{i w t}(a e^{i rho t} + b e^{-i rho t}) Y_1m (reelle Y_1m),
  chi-Stoerung c Y_1m mit Frequenz rho; Kanaele a (w + rho, offen in E1), b (w - rho, zu), c' = c/2 (zu in E1).
- Radial u = r a usw.: u'' = (M(r) - E + l(l+1)/r^2) u mit M, E wie Code 1 (Ea = (w + rho)^2, Eb = (w - rho)^2,
  Ec = rho^2) und l(l+1) = 2 in allen drei Kanaelen. Schwellen und Bereiche unveraendert (gegen 2).
- **Regulaer am Ursprung (a, b, c ~ r, also u ~ r^2):** Start bei r0 = 2 hp (erster RK4-Gitterpunkt) mit der Reihe
  u = r^2 [v + r^2 V0 v / 10], u' = 2 r v + (4/10) r^3 V0 v, V0 = M(0) - E, v = e_a, e_b, e_c (allgemein
  u = r^(l+1) [v + r^2 V0 v / (2(2l + 3))]; Fehler O(r0^6)). Fehler der ersten RK4-Schritte liegen im regulaeren
  Unterraum (aendert die Basis, nicht den Rang von G) oder in der singulaeren Loesung ~ r^-1, die relativ wie (r0/r)^3
  abklingt.
- **Abklingend (geschlossene Kanaele b, c) am Startradius R_z:** modifizierte Kugel-Bessel-Funktion l = 1,
  u = e^{-kappa r}(1 + 1/(kappa r)); normiert u(R_z) = 1, u'/u = -(1 + kappa R_z + kappa^2 R_z^2) / (R_z (1 + kappa R_z))
  (gleich J_0 von BEWEIS-2). Offener Kanal a: keine Startbedingung (wie Code 1).
- **Umsetzung:** dipol.py ersetzt zur Laufzeit genau drei Kanalfunktionen durch l-Fassungen: HL.werte_k (Suche),
  S3.regulaer und S3.abklingend (Newton, Rechteck, E2-Mass). Alles andere (Zeilen, rho-Gitter, Nullstellen,
  Illinois, Rang, Unterzeilen, Halbierung, Zellen-Umlauf, Newton, Rechteck-Umlauf) ist der unveraenderte Code der
  Vorlaeufer.
- **Selbsttest (im K1-Lauf):** Mit l = 0 liefern die Ersatzfunktionen an 5 Punkten dieselben Werte wie die Originale
  (erwartet bitgleich; berichtet wird max |Differenz|).

## 2 Messgroesse und Zaehlung (wie Vorlaeufer)

- W = m_ac + i m_bc (Code 1): G = W[Y_x, Z_y], 3x2, Gram-Schmidt-Ordnung c, b, a; m_xy die 2x2-Minoren. Stille Stelle
  <=> Rang G <= 1 <=> m_ac = m_bc = 0 (sigma2/sigma1-Probe). Der Rang haengt nicht von der Basis des regulaeren
  Unterraums ab; die Lage der Stellen ist damit unabhaengig von der Startnormierung.
- Zeile, Nullstellen von m_bc, Illinois (Runde-18-Nachtrag 1), Unterzeilen (1/8), zwei Halbierungen, Zellen-Umlauf
  U_z = sign(s(oben) - s(unten)) * sigma_c, Rechteck-Umlauf (Code 1), "Stelle" (beide Stufen, gleiche Kurve, gleiches
  Zeilenpaar, Lage auf 1/16 Zeilenabstand, Zellen-Umlauf +-1 gleich, ohne Merker): woertlich Runde-18-PLAN 3 und 4.

## 3 Triviale Moden

- Translation (delta phi ~ f'(r) x/r, delta chi ~ g'(r) x/r) und der Boost-Partner (Lorentz/Galilei-artig, Jordan-
  Kette) liegen bei rho = 0 (Zeitabhaengigkeit nur e^{i w t}). Phase und d/dw gehoeren zu l = 0.
- E1 verlangt rho > sqrt(m2) - w. Abgetastet wird rho >= sqrt2 - w + 1e-4 >= 0,2311 (w^2 <= 1,40) bzw. in K1
  rho >= 1 - w + 1e-4 >= 0,1226. rho = 0 liegt ausserhalb; triviale Moden koennen nicht gezaehlt werden.
- Kontrolle: Jede zusaetzliche K1-Stelle ausser der bewiesenen wird berichtet.

## 4 K1 (vor der Suche)

- Modell K1E1 von Code 1 (lam = 0, cpot = 0,5: chi entkoppelt, Masse^2 4; a, b Masse 1, Schwelle 1), l = 1. Zeilen
  omega^2 = 0,77; 0,76; 0,75; 0,74; 0,73, beide Stufen, ganze E1-Zeile, dieselbe Kette (Zeile, Rang, Unterzeilen,
  Halbierung), dann Newton und Rechteck wie Code 1 (Abklingstart bei R_bg).
- Referenz: BEWEIS-2 Satz T2, omega^2 = 0,75449601378, rho = 1,82634203018. Die Kartenwerte (0,7544960184 /
  1,8263420673) weichen davon um 4,6e-9 / 3,7e-8 ab; beide Abstaende werden berichtet, fuer 1e-6 ohne Belang.
- **Bestanden (D0):** auf beiden Stufen Newton-Lage auf 1e-6 an der Referenz (omega^2 und rho), Rechteck-Umlauf
  aufgeloest +-1 (Vorzeichen nicht vorhergesagt), gleich auf beiden Stufen. Sonst keine Suche (Karte), nur Bericht.

## 5 Suche

- Profile wie Runde 18 (Numerov-Newton, Saat BEUTEL Q = 200, Fortsetzung, Gebiet), Stufe 1 hp = 0,01, Stufe 2 0,005.
- Zeilen nach der Runde-18-Regel w2_{j+1} = w2_j - min(0,01; 0,5 (w2_j - 0,7281)^2 / 1,3736) ab 1,40, letzte Zeile
  0,80 (gleiche Logik wie Runde 18 mit Untergrenze 0,80). Damit sind die Zeilen bis auf die letzte die von Runde 18.
- Zeile, Paare: Runde-18-PLAN 3 und 4 mit Nachtrag 1, unveraenderter Code (cmd_block).
- Bloecke von 1,40 abwaerts, Stufen getrennt, jeder Aufruf < 600 s; jede Zeile und jedes Paar sofort als JSON;
  ein abgebrochener Block wird mit demselben Aufruf ab der ersten fehlenden Datei fortgesetzt.
- Bei Zeitnot: gewertet wird der zusammenhaengende Bereich ab 1,40 bis zur tiefsten Zeile, bis zu der auf beiden
  Stufen alle Zeilen und Paare vorliegen (Runde-18-Nachtrag 2). Untergrenze wird berichtet.

## 6 Ordnen nach chi-Kurven (vorab begruendet)

- **Kriterium: k = Rang der Nullstelle von m_bc in der Zeile, von unten gezaehlt** (wie Runde 18). Begruendung: Die
  Nullstellen von m_bc sind die gebundenen l = 1-Zustaende des geschlossenen (b, c)-Teils (chi-Topf der Huelle); als
  Eigenwerte eines radialen Problems kreuzen sie sich in einer Ein-Parameter-Familie generisch nicht, neue Kurven
  entstehen oben an rho = sqrt2, wenn R waechst. Runde 18 hat das bei l = 0 gestuetzt (keine Abnahme, kein
  Rangsprung, gleiche Zahl und Lage auf beiden Stufen).
- Knotenzahl der c-Komponente von Y_c auf (0, r_m] nur als Gegenprobe berichtet, nicht als Index: In Runde 18 war sie
  monoton im Rang, aber nicht eindeutig (0, 0, 2, 2, 4, ...), weil der letzte Knoten oft jenseits r_m liegt.
- Merker wie Runde 18 (Rangsprung nach Nachtrag-1-Wortlaut, Abnahme der Nullstellenzahl zur Schranke hin).
- Je Kurve: R der Stellen (R = Radius, wo chi = 1/2), Abstaende Delta R, Mittel, CV.

## 7 Rechteck-Stichprobe

- Je Kurve k = 0 bis 3 die Stelle mit kleinstem omega^2, dazu k = 4, 8, ...; beide Stufen; Newton und Rechteck
  wie Runde 18 (cmd_umlauf, Halbbreite min(1e-3; 0,4 Schwellenabstand; 0,25 Luecke; 0,5 Zeilenabstand)). Prueft
  Zellen-Umlauf = Rechteck-Umlauf. Reicht die Zeit, folgen weitere Stellen (nach k, dann omega^2 aufsteigend).

## 8 Wertung D0 bis D4 (vorab operationalisiert)

- D0: Abschnitt 4.
- D1: N = Zahl der Stellen (Abschnitt 2) im gewerteten Bereich innerhalb [0,80; 1,40]. Eingetroffen bei N >= 5;
  nicht eingetroffen, wenn der Bereich bis 0,80 reicht und N < 5; offen, wenn der Bereich nicht bis 0,80 reicht und
  N < 5.
- D2: Kurven mit >= 4 Stellen (>= 3 Abstaende): CV = Standardabweichung (n-1) / Mittel der Abstaende in R.
  Eingetroffen, wenn es mindestens eine solche Kurve gibt und alle CV < 0,15 haben; nicht eingetroffen, wenn eine
  CV >= 0,15 hat; offen ohne solche Kurve.
- D3: Je l = 1-Kurve k mit >= 3 Stellen: q_k = mittleres Delta R (l = 1, Kurve k) / mittleres Delta R (l = 0, Kurve
  gleichen Rangs k, Runde-18-ERGEBNIS Abschnitt 4, Lagen je Kurve), gemittelt ueber die l = 0-Abstaende, deren
  Paarmitte in [R_min, R_max] der l = 1-Stellen der Kurve liegt; liegt keine darin, der l = 0-Abstand mit der
  naechsten Paarmitte. Eingetroffen, wenn alle |q_k - 1| <= 0,15; nicht eingetroffen, wenn eines > 0,15; offen ohne
  solche Kurve. Nur berichtet (nicht gewertet), falls Zeit: Vergleich mit der l = 0-Kurve naechsten rhos bei gleichem R.
- D4: Abschnitt 9.

## 9 D4: Nachfolger der M1-Dipolstelle (Homotopie wie STILLE-ZWEIFELD)

- Verfahren von Code 1 (cmd_homotopie) bei l = 1, eigene Kopie in dipol.py: Modell(lam, cpot = 0,25), lam = 0; 0,05;
  ...; 1,0 (cpot fest, Masse^2 von chi 2). Start: K1-Newton-Lage (Stufe 1). Bei lam = 0 ist chi entkoppelt, die
  Stelle liegt in E2 (rho = 1,83 > sqrt2) mit T = 0.
- Je lam: Profil bei der aktuellen omega^2 per Newton aus dem vorigen (bei Scheitern 8 Teilschritte, wie Code 1);
  liegt der Punkt in E1: Newton auf W (l = 1); sonst Gauss-Newton auf T = |G| (E2-Mass von Code 1 mit l = 1), Klemme
  wie Code 1.
- Abweichungen von Code 1 (begruendet): festes Gebiet R_bg = 1,5 R_est + 25/sqrt(2 - w2) + 5 mit
  R_est = 1,3736/(w2 - 0,7281) + 0,55 (der M2-Ball bei w2 ~ 0,75 hat R ~ 50 und passt nicht in das M1-Gebiet von Code
  1); Rundungsschutz nach Runde-18-Empfehlung: Kopplung Mac = 0, wo |chi| < 1e-12 (nur D4; in der Suche ist R <= 20
  und chi innen >= ~1e-10).
- Die Klemme von Code 1 haelt den E2-Punkt bei rho >= sqrt2 + 1e-3; damit koennte die Verfolgung E1 nie erreichen
  (Ausgang vorab fest). Deshalb (Abweichung): Liegt der Gauss-Newton-Punkt an dieser Klemme (Abstand < 1e-6), wird
  zusaetzlich Newton auf W in E1 ab (omega^2, sqrt2 - 1e-3) versucht; konvergiert er in E1 mit sigma2/sigma1 < 1e-6,
  wird ab da diese E1-Stelle verfolgt.
- Fortsetzung bei Abbruch an der 600-s-Grenze: Profil und Zustand je Schritt gespeichert.
- Wertung: nicht eingetroffen, wenn bei lam = 1 die verfolgte Stelle eine E1-Stelle ist (Newton in E1 konvergiert,
  sigma2/sigma1 < 1e-6); eingetroffen, wenn die Verfolgung lam = 1 erreicht und dort keine E1-Stelle ist; offen, wenn
  sie vorher abbricht. Berichtet je Schritt: omega^2, rho, Bereich, T bzw. sigma2/sigma1, R. Nur Stufe 1.

## 10 Laeufe (.69, kleintest.sh, nur Spur cpu6, nacheinander, je < 600 s)

- V0: pruef.py (py_compile aller Dateien), Zeilenliste.
- V1: K1 Stufe 1 und 2 (mit Selbsttest); Profile Stufe 1 und 2. Suche erst nach bestandenem K1.
- V2: Bloecke Stufe 1 und 2 von 1,40 abwaerts, Fortsetzung bei Abbruch.
- V3: Auswertung (code/auswertung_dipol.py), Rechteck-Stichprobe Stufe 1 und 2, Endauswertung.
- V4: D4-Homotopie.
- Programmfehler werden behoben und mit sha256 dokumentiert, das Verfahren bleibt. Folgelaeufe mit Verfahrensbezug nur
  mit eingefrorenem PLAN-NACHTRAG-n.md, als nachtraeglich markiert.

## 11 Bedeutung (woertlich Karte)

- Treffen D1 und D2 ein: Die Huelle traegt auch Dipol-Leitern. Der Mechanismus ist nicht an l = 0 gebunden [H].
- D3 prueft, ob die Sprossenregel (halbe Innenwellenlaenge) fuer beide l dieselbe ist.
