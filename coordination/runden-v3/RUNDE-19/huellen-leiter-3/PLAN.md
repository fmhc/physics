# PLAN HUELLEN-LEITER-3 (Runde 19)

- Code-Agent. Start 2026-10-02 16:09:59 CEST (date). Plan geschrieben ab 16:26:33 CEST (date), vor jedem .69-Lauf.
- Gelesen: KARTE; HUELLEN-LEITER-2: KARTE, ERGEBNIS, PLAN, PLAN-NACHTRAG-1, code/, aus/k0 (Newton-Wurzeln und W der
  12 K0'-Stellen); RUNDE-18/huellen-leiter: ERGEBNIS, aus/laeufe/stellen.json, umlauf-P-st*.json,
  umlauf-punkte-P-st1.json, z-st1-0100/0105/0110 und z-st2-0110 (nur w2, Rchi, Knotenzahl, rho der Nullstellen),
  aus/logs/prof-st1.log. Nichts aus dem Suchbereich (keine Zeilen oder Paare > 110 der Runde 18 geoeffnet).
- Verbindlich (Karte): K0', Kontrolle der Stabilisierung, lagebasiertes Annahmekriterium, P1' und P2' unveraendert,
  getrennte Wertung der kontaminierten Sprosse (k = 1, 40,51), Bedeutung. Nichts davon wird nach dem Ergebnis geaendert.
  Abweichungen und Lesarten stehen unten, jeweils als **[Abweichung]** oder **[Lesart]** markiert, mit Grund.
- Code: code/huellen_leiter2.py, code/stille3.py, code/beutel.py unveraendert aus HUELLEN-LEITER-2 (sha256 2755359c...,
  1d15a38c..., f831e818..., verglichen). Neu: code/huellen_leiter3.py (Variante F, Newton, Befehle k0, test, umlauf,
  auswertung). Referenzen: ref/stellen-r18.json (5ce185ec...), ref/zeilen-r18.json (586c3689...).

## 1 Zwei Varianten der Kopplung und ihre Rollen

- **S (Schnitt)** = HUELLEN-LEITER-2: chi < 1e-12 -> 0 in der Linearisierung (Klasse PotStab, unveraendert).
- **F (Fortsetzung)** = zweite Stabilisierung der Karte, "chi im Inneren glatt und positiv fortgesetzt": An allen
  Gitterpunkten mit Index <= i_s (i_s = groesster Index mit chi < 1e-12) wird chi ersetzt durch
  chi_F(r) = chi(r_a) * phi(r) / phi(r_a), phi(r) = sinh(m0 r) / r (phi(0) = m0), r_a = r_(i_s + 1) (erster aufgeloester
  Punkt), m0^2 = U_chichi(S(0), chi = 0) = 2 S(0) - 1. Das ist die Loesung der linearisierten Gleichung
  (r chi)'' = m0^2 (r chi) im Inneren, also die analytische Fortsetzung des inneren Abklingens. Ueberall sonst chi
  unveraendert. Wie bei S werden alle vier Matrixelemente mit chi_F gebildet; geaendert ist bitweise nur M_ac (chi_F^2
  <= 1e-24, PLAN HUELLEN-LEITER-2 Abschnitt 1); der Code zaehlt das wie PotStab und meldet Punkte unter i_s mit
  chi >= 1e-12 (nicht zusammenhaengende Maske).
- **[Abweichung] Rollen:** Die Lagen (Newton-Wurzeln, Delta R, P1', Annahme ausser Umlauf) kommen wie in der Karte aus
  S ("Code wie HUELLEN-LEITER-2"). Die **Vorzeichen** (Rechteck-Umlauf fuer das K0'-Vorzeichen, fuer "+-1 aufgeloest"
  in der Annahme und fuer P2') kommen aus F. S-Umlaeufe werden ueberall mitgerechnet und berichtet.
  - Grund (aus den Daten von HUELLEN-LEITER-2, vor jedem eigenen Lauf): Der Umlauf von W ist eine Konvention der
    Basis der regulaeren Loesungen; S dreht sie auf k = 3 bis 9 ab R ~ 28 (Anhang B: Zellen-Umlauf an Nr 74 und Nr 83,
    k = 3, umgekehrt; D2: Rechteck-Umlauf an allen aufgeloesten Proben mit umgekehrt). K0' verlangt das Vorzeichen der
    Runde 18 an Nr 74 und 83; mit S wuerde K0' dort aus einem Konventionsgrund scheitern, nicht wegen der Lage. F
    erhaelt die Saat aus der Ballmitte (Vorschlag in HUELLEN-LEITER-2, Abschnitt 6) und damit die Konvention der
    Runde 18 auf k = 0 bis 3 (Abschnitt 7).
  - Die Kontrolle der Stabilisierung vergleicht dieselben zwei Varianten wie die Karte (S gegen "glatt und positiv
    fortgesetzt"), also unveraendert.

## 2 Newton und Startwerte (vorab festgelegt)

- **Newton auf W** = m_ac + i m_bc (werte_E1 aus Code 1, Abklingloesungen ab dem Gebietsrand): zwei reelle
  Gleichungen in (omega^2, rho), Jacobi-Matrix aus Vorwaertsdifferenzen 1e-6 (wie Code 1). Daempfung: Schritt mit
  einem Faktor so verkuerzt, dass |d omega^2| <= 2e-4 (~0,23 in R) und |d rho| <= 2e-3. Hoechstens 30 Schritte.
  Konvergiert, wenn der ungedaempfte Schritt < 1e-10 (max-Norm) ist. Ankerprofil = naechste Zeile mit
  omega^2 <= Start (wie Vorlaeufer), Umgebung von Code 1 (Profile auf dem Ankergitter).
- **Startwerte der Sprossen:**
  - omega^2_start = lineare Interpolation von omega^2 in der Tabelle (Rchi, omega^2) der Zeilen 0 bis 125 von Stufe 1
    (eigene Profile, Zeilenliste der Runde 18) beim vorhergesagten R. Gleicher Start fuer beide Stufen.
  - rho_start = quadratisches Polynom in x = 1/R durch die letzten drei gezaehlten Stellen der Kurve k aus Runde 18
    (R und rho der Stufe 1 aus ref/stellen-r18.json; Lagrange, exakt durch die drei Punkte), ausgewertet bei
    x = 1/R_vorhergesagt. Punkte: k = 0: Nr 62, 72, 81; k = 1: Nr 69, 78, 88; k = 2: Nr 68, 76, 85; k = 3: Nr 65,
    74, 83.
  - R_vorhergesagt woertlich aus der Karte: k = 0: 39,59 / 42,00; k = 1: 40,51 (kontaminiert) / 42,62; k = 2: 40,24 /
    42,36; k = 3: 39,77 / 41,93.
- **[Abweichung] Nachstarts:** Liefert der Start keine angenommene Stelle auf Kurve k mit |R - R_vorhergesagt| <= 0,5,
  dann zwei weitere Starts mit denselben Formeln bei R_vorhergesagt - 0,25 und + 0,25 (in dieser Reihenfolge, Abbruch
  beim ersten Erfolg). Grund: Ein einzelner Newton-Lauf kann ohne Bezug zur Lage scheitern (Daempfung, Nachbarkurve
  k = 1/2 nur 0,009 in rho entfernt). Bei Stellenabstaenden >= 2,1 in R gibt es hoechstens eine Stelle der Kurve im
  Fenster; die Nachstarts verschieben also keine Lage. Berichtet wird, welcher Start gefunden hat.

## 3 K0' (verbindlich, zuerst ausgewertet)

- Stellen: je Kurve k = 0 bis 3 die drei mit groesstem R (Nr 62, 72, 81; 69, 78, 88; 68, 76, 85; 65, 74, 83), beide
  Stufen.
- Je Stelle und Stufe drei Newton-Laeufe (Abschnitt 2) vom selben Start (Lage der Runde 18 auf dieser Stufe) mit
  demselben Anker: Kopplung der Runde 18 ("alt", = Code der Runde 18), S und F.
- **[Lesart] Bezug "reproduziert auf 1e-8":** die Newton-Wurzel mit der Kopplung der Runde 18 (gleicher Code, gleicher
  Start). Die tabellierte Halbierungslage der Runde 18 ist selbst nur auf ~1e-8 bis 1e-7 genau (Interpolationsfehler,
  PLAN HUELLEN-LEITER-2 Abschnitt 3) und taugt nicht als 1e-8-Bezug; sie wird berichtet.
- **Bestanden, wenn alle gelten (12 Stellen, beide Stufen):**
  - K0'a: alt- und S-Newton konvergiert, |d omega^2| <= 1e-8 und |d rho| <= 1e-8 (S gegen alt).
  - K0'b: Rechteck-Umlauf von W (Variante F, um die F-Wurzel) aufgeloest (groesster Phasensprung < 0,4 rad) und gleich
    dem Umlauf der Runde 18 (umlauf_1 bzw. umlauf_2 in ref/stellen-r18.json; dort Zellen-Umlauf, an Nr 81, 83, 85, 88
    durch Rechteck bestaetigt).
  - Dazu (Kriterium, da F die Vorzeichen liefert): F-Newton konvergiert und F-Wurzel gegen alt auf 1e-8.
- Rechteck wie Runde 18: Code 1 umlauf_mit_rueckfall, 16 Punkte je Kante, Verfeinerung bis Sprung < 0,4 rad
  (hoechstens 24 Runden, 3000 Punkte), Halbbreite min(1e-3, 0,4 Abstand zum E1-Rand, 0,25 gap, 0,5 dw2_zeile) mit gap
  und dw2_zeile der Runde 18 (Rueckfall auf 1e-4, wenn nicht aufgeloest).
- Berichtet (kein Kriterium): S-Umlauf an allen 12 (Erwartung Abschnitt 7), |W| und sigma2/sigma1 an jeder Wurzel,
  Abstand zur Tabelle der Runde 18.
- **K0' nicht bestanden:** P1' und P2' bleiben offen (nicht auswertbar); die Testlaeufe werden nur als Information
  berichtet.
- Ich werte K0' formal aus (Befehl auswertung k0), bevor ich irgendeine Ausgabe der Testlaeufe ansehe.

## 4 Test: Annahme einer Sprosse

- Fuer jede der 8 Sprossen und jede Stufe: Newton (S) ab dem Start (Abschnitt 2), dann am Endpunkt:
  - **Konvergenz [Lesart + Abweichung]:** "W < 1e-10 konvergiert" = Newton konvergiert (Schritt < 1e-10) und
    |W| am Endpunkt <= 1e-9. Grund: Der Rauschboden von |W| an korrekt konvergierten bekannten Stellen liegt nach
    HUELLEN-LEITER-2 (aus/k0, gleiche Codefamilie) bei bis 1,9e-10 (Nr 78, S) bzw. 1,7e-10 (Nr 69, alt); ein
    Restkriterium |W| < 1e-10 wuerde korrekt gefundene Stellen am Rauschen scheitern lassen. Ob |W| < 1e-10 woertlich
    erfuellt ist, steht je Stelle in der Tabelle.
  - **[Abweichung, Zusatz] Rangabfall:** sigma2/sigma1 von G <= 1e-6 (sonst Scheinnullstelle mit Zeile c = 0).
  - **Kurve k [Lesart]:** "wie im Vorlaeufer" = Rang der Nullstelle von m_bc von unten in der Zeile bei omega^2 der
    Wurzel (Runde 18 PLAN 4; Zeilenrechnung zeile_k aus HUELLEN-LEITER-2 auf dem Profil an der Wurzel); die naechste
    Nullstelle muss auf <= 1e-6 bei rho der Wurzel liegen. Dazu die Knotenzahl der c-Komponente an der Wurzel: Sie muss
    dem Wert der Runde 18 fuer diese Kurve gleichen (Zeilen 100 bis 110 beider Stufen: k = 0, 1, 2, 3 -> 0, 0, 2, 2).
    Beides Pflicht.
  - **Fenster:** |R_gefunden - R_vorhergesagt| <= 0,5, R = Rchi des Profils an der Wurzel (Stufe 1).
  - **Rechteck-Umlauf** von W um die Wurzel auf beiden Stufen aufgeloest und +-1 (Variante F, Abschnitt 1; S
    berichtet). Halbbreite wie in Abschnitt 3 mit gap = Abstand zur naechsten Nullstelle von m_bc in derselben Zeile
    (oder zum Zeilenrand) und dw2_zeile = Abstand der umgebenden Zeilen.
  - **Stufen:** S-Wurzeln beider Stufen auf <= 1e-6 gleich (omega^2 und rho).
- Angenommen, wenn alles gilt. Sonst: nicht angenommen; Nachstarts nach Abschnitt 2. Keine angenommene Stelle im
  Fenster: "nicht gefunden".
- Delta R = R_gefunden - R_vorhergesagt (Stufe 1).

## 5 Kontrolle der Stabilisierung (verbindlich)

- An jeder angenommenen neuen Stelle und Stufe: F-Newton ab der S-Wurzel. Gewertet (Karte: zwei neue Stellen): die
  zwei angenommenen unkontaminierten Sprossen mit kleinstem R_vorhergesagt (Reihenfolge 39,59; 39,77; 40,24; 41,93;
  42,00; 42,36; 42,62). Bestanden, wenn dort auf beiden Stufen F konvergiert und |d omega^2|, |d rho| <= 1e-8 gegen S.
  Die uebrigen Vergleiche werden berichtet.
- Nicht bestanden (oder weniger als zwei angenommene Stellen): Lage nicht bestaetigt, P1' und P2' offen.

## 6 Wertung

- **P1'** eingetroffen, wenn alle 7 unkontaminierten Sprossen angenommen sind und je |Delta R| <= 0,10. Eine nicht
  gefundene Sprosse ist ein Fehlschlag. Sonst nicht eingetroffen. Offen nur nach Abschnitt 3 oder 5.
- **P2'** je Kurve die Folge: letzte Stelle der Runde 18 (Nr 81, 88, 85, 83; F-Umlauf aus dem K0'-Lauf), dann die
  angenommenen neuen Sprossen nach R. Gewertet werden nur Schritte zwischen direkt aufeinander folgenden Gliedern (ein
  nicht gefundenes Glied unterbricht die Folge). Ein Schritt ist erfuellt, wenn der F-Umlauf das Vorzeichen wechselt,
  auf beiden Stufen; ungleiche Stufen zaehlen als nicht erfuellt.
  - **[Lesart] Kontamination:** Schritte, an denen die Sprosse k = 1 / 40,51 beteiligt ist, werden getrennt gewertet.
    Haupt-P2' = alle uebrigen Schritte (k = 0, 2, 3 und auf k = 1 keiner).
  - Eingetroffen, wenn alle gewerteten Schritte erfuellt sind und es mindestens einen gibt; nicht eingetroffen, wenn
    einer nicht erfuellt ist; offen ohne gewerteten Schritt.
- **Kontaminierte Sprosse k = 1 / 40,51:** gleiche Annahme und Delta R, getrennt berichtet, nicht in P1'/P2'.
- **Bedeutung (woertlich nach Karte):** P1' und P2' eingetroffen -> "Die Sprossenregel sagt neue stille Stellen
  voraus [H]". **[Lesart]** "Abweichungen > 0,3" = mindestens eine der 7 Sprossen mit |Delta R| > 0,3 oder nicht
  gefunden -> "Die Regel gilt nur im bisherigen Bereich." Sonst Zwischenausgang ohne diese Aussagen, berichtet wie
  gefunden.

## 7 Erwartung vorab (Schreibtisch, [H], nicht gerechnet)

- Lagen: S und F gegen alt an den K0'-Stellen <= 1e-12 (HUELLEN-LEITER-2: S <= 1e-13).
- Vorzeichen: Die Saat in die c-Loesung kommt dort her, wo chi * (Wachstum der a/b-Mode bis zur Wand) am groessten ist.
  Mit exaktem chi ~ sinh(m0 r)/r (m0 ~ 1,19 < Wachstumsrate ~ 1,8) ist das die Ballmitte, wo die c-Loesung festes
  Vorzeichen hat. S verlegt die Saat an den Schnittradius r_s ~ R - 23; dort hat die c-Loesung auf k = 3 (erster Knoten
  bei r ~ 11 bis 12) ab R ~ 34 das andere Vorzeichen. Runde 18 saete ab dem Rundungsrand (chi ~ 1e-16, r ~ R - 31,
  vor dem ersten Knoten fuer k <= 3). Erwartet: F-Umlauf = Runde 18 an allen 12 K0'-Stellen; S-Umlauf an Nr 74 und 83
  umgekehrt, sonst gleich.
- Risiko F: Die Saat aus der Mitte waechst bei R ~ 42 auf ~1e12 bis 1e13 der c-Loesung (Runde 18 bei R ~ 30: ~1e10,
  ohne Lagefehler). Moeglicher Genauigkeitsverlust von F zeigt sich in K0' (F gegen alt) und in der Kontrolle.
- Kontaminierte Sprosse: Die in HUELLEN-LEITER-2 gesehene Stelle bei R = 40,49 hat rho = 1,2484. Kurve k = 1 liegt bei
  R = 39 bei rho = 1,188 (Zeile 110), k = 5 bei 1,254. Die gesehene Stelle liegt also vermutlich nicht auf k = 1.
  Die Karte wertet die Sprosse trotzdem getrennt; daran aendere ich nichts.
- Startwerte: rho_start liegt nach Schaetzung auf ~1e-5 an der Kurve; omega^2_start entspricht R_vorhergesagt.

## 8 Laeufe (.69, kleintest.sh, Spuren cpu bis cpu4, je <= 600 s)

- Ordner /home/fmh/fmhc-physics-remote/runde19-huellen-leiter-3/ (code/, hilfs/, ref/, aus/, logs/), alle Pfade absolut.
- V0: py_compile. V1: Profile Stufe 1 und 2, Zeilen 0 bis 125 (Saat bei Q = 200 wie Vorlaeufer); Vergleich mit
  profile-info der Runde 18 (w2, Q, Rchi; bitgleich erwartet). 
- V2 (K0'): Befehl k0 je Stufe in Teilen (alt, S, F Newton; F-Rechteck); danach S-Rechtecke (Information).
- V3 (Test): Befehl test je Stufe in Teilen (S-Newton mit Nachstarts, Zeile, F-Newton ab S-Wurzel, F- und S-Rechteck).
  Laeuft parallel zu V2 auf anderen Spuren; Ausgaben erst nach der K0'-Auswertung angesehen.
- V4: auswertung k0 (zuerst), dann auswertung test.
- Programmfehler werden behoben und mit sha256 dokumentiert; Verfahren bleibt. Nachtraege nur eingefroren
  (PLAN-NACHTRAG-n.md.eingefroren-*), als nachtraeglich markiert.
