# K-2 Lesung: Boson Star Factory (arXiv:2609.24913) als fremde Latte fuer unseren Loeser

Bearbeiter: Anthropic-Agent (Opus 5.5) fuer claude-primary, Runde 1. Datei begonnen 2026-09-30 00:25:56 CEST (gemessen).
Explorativ. Gelesen an der Quelle: arXiv:2609.24913v2 (Gervalle, Delgado, Costa Filho, Herdeiro, Jaramillo, Luna, Radu;
gr-qc, v1 21.09.2026, v2 22.09.2026), PDF-Seiten 1 bis 6 und 27 bis 30 (Titel, Inhalt, Modell, Ansatz, Abschnitt 6,
Tabelle 10). Die Benchmark-Tabellen in Abschnitt 5 (S. 15 bis 20) habe ich nicht gelesen, weil sie gravitierende
Sterne ohne Selbstwechselwirkung betreffen. Eigene Folgerungen sind mit **[S]** markiert.

## Ergebnis

1. **Es gibt genau einen flachen Q-Ball, und er hat nur zwei Zahlen.** Abschnitt 6 (PINN-Machbarkeitsstudie) rechnet in
   Minkowski-Raum einen **drehenden** Q-Ball mit Windung m = 1 und ω = 0,99. Das Potential ist
   U(|Ψ|²) = λ|Ψ|²(|Ψ|⁴ − a|Ψ|² + b) mit λ = 0,5, a = 2, b = 1,1 (Gl. 74). Tabelle 10 nennt aus einer spektralen
   Referenzloesung E = 136,06 und Q = 157,09, die PINN-Werte sind 137,83 und 159,64 (Fehler 1,30 und 1,63 Prozent).
   J, weitere ω-Werte oder Profile in Zahlen gibt es nicht. Die "eight significant digits" des Abstracts betreffen
   gravitierende Bosonensterne mit freiem Feld (Gl. 1, kein Selbstwechselwirkungsterm). Unser Loeser rechnet ohne
   Gravitation, fuer ihn sind sie nicht brauchbar.
2. **Die Referenz ist schwaecher als erhofft:** fuenf gueltige Stellen, ein einziger Spektral-Code ("collocation
   spectral methods on a Chebyshev grid, via Newton-Raphson iterations"), kein Dreifachabgleich.
3. **Normierung mit einer Unstimmigkeit [S].** Kinetischer Term und Ladung sind wie bei uns: Gl. 73 ergibt
   L = |∂tΨ|² − |∇Ψ|² − U, und Gl. 86 ist Q = 2ω∫φ² d³x. Die Feldgleichung Gl. 75 schreibt rechts U'(φ).
   - Wirkungslesart (U'(φ) meint dU/dS · φ): Die Masse ist √(λb) = 0,742 < ω = 0,99. Dann gibt es gar keinen
     lokalisierten Q-Ball.
   - Woertliche Lesart (U'(φ) = dU/dφ): Das passt zu Gl. 80, κ = √(2λb − ω²) = 0,346. Das Profil loest dann effektiv das
     Wirkungspotential W = 2U = 1,1S − 2S² + S³. Das ist das Modell von Kleihaus, Kunz und List mit λ = 1
     (PRD 72 (2005) 064002, gr-qc/0505143, [aus dem Gedaechtnis]; die Arbeit zitiert es als Ref. 12).
   - Die Energie in Gl. 85 setzt aber U statt W ein. Tabellenwert E = 136,06 kann nicht die zum Profil passende Energie
     sein: Nach dem Virialsatz gilt E − ωQ = (2/3)∫(|∇φ|² + m²φ²/ρ²) > 0, die Tabelle hat E/Q = 0,866 < ω.
   - Mit E(Tab.) = E_85 folgt G = ∫(|∇φ|² + m²φ²/ρ²) ≈ 23,30 und die zum Profil passende Energie E_W ≈ 171,06
     > m·Q = 164,76. Der Referenz-Q-Ball liegt also vermutlich auf dem dicken, instabilen Ast.
4. **Das Potential ist nicht unseres.** Es gehoert zu derselben sextischen Familie; in unseren Einheiten (Masse 1,
   quartischer Koeffizient 1) lautet es U = S − S² + 0,275·S³, unseres ist S − S² + 0,5·S³ [S]. Das Verhaeltnis
   c3·c1/c2² ist 0,275 gegen 0,5 und haengt nicht von der Lesart ab. In ihrer Schreibweise ist unser Potential
   λ = 0,5, a = 2, b = 2 (Wirkungslesart). Direkt vergleichen laesst sich keine unserer Zahlen.
5. **Unser Loeser laesst sich nicht ohne Umbau darauf stellen.** field3d/fixedq.py hat die Koeffizienten fest im Code
   (engine.py Z. 27 und 33), rechnet zwei Kanaele plus Higgs und setzt eta = 0,1 und portal_g = 0,001. Vor allem
   minimiert es E bei fester Ladung. Bei Q = 157,09 faende es damit vermutlich den energieaermeren Ast, nicht die
   Referenz [S]. Noetig sind: Koeffizienten als Parameter, ein Einfeld-Modus, ein m = 1-Startfeld und ein Loeser bei
   festem ω (Newton-Krylov). Geschaetzt weniger als 1 h neuer Code, danach hoechstens 10 min .69 (Plan unten).

**Vorschlag: weiter, klein.** Die Arbeit enthaelt einen flachen Q-Ball; die Karte bleibt also offen. Voraussetzung ist,
dass die Leitung den Umbau freigibt. Vorher sollte ein zweites Haus Abschnitt 6 der Arbeit und Punkt 3 oben gegenlesen
(10 min), weil der Vergleich an meiner Lesart der Normierung haengt.

## 1. Was in der Arbeit steht (Zitate)

- Gl. 73, Minkowski: S = ∫d⁴x [−½ g^μν(Ψ*,μ Ψ,ν + Ψ*,ν Ψ,μ) − U(|Ψ|²)].
- Gl. 74: U(|Ψ|²) = λ|Ψ|²(|Ψ|⁴ − a|Ψ|² + b); "we will use the physical parameters λ = 0.5, a = 2, b = 1.1, m = 1,
  ω = 0.99".
- Gl. 75: (∂r² + (2/r)∂r + (1/r²)∂θ² + (cos θ/(r² sin θ))∂θ − m²/(r² sin²θ) + ω²)φ = U'(φ).
- Gl. 80: κ = √(U''(0) − ω²) = √(2λb − ω²).
- Gl. 81: Startfeld φ_guess = ½e^(−⅛[z² + (x_c − 3)²]) − ½e^(−⅛[z² + (x_c + 3)²]).
- Gl. 85: E = 2π∫dr r²∫dθ sin θ (ω²φ² + (∂rφ)² + (1/r²)(∂θφ)² + m²φ²/(r² sin²θ) + U(φ)).
- Gl. 86: Q = 4πω∫dr r²∫dθ sin θ φ².
- Tabelle 10: Spectral E = 136,06, Q = 157,09; PINN E = 137,83, Q = 159,64; Fehler 1,30 und 1,63 Prozent.
- Abb. 11 und 12: Ring mit Maximum φ ≈ 0,53 bei x ≈ 0,77 in kompaktifizierter Koordinate, also r ≈ 3,3 bei
  r = x/(1 − x) [S, abgelesen]; maximale Abweichung PINN gegen Spektral 0,0093 auf 64 × 62 Knoten.
- Gl. 39 (fuer Bosonensterne): J = mQ. Fuer den flachen Q-Ball folgt J = mQ ebenso aus dem Ansatz [S]. Mit m = 1 ist
  J = Q = 157,09; das ist keine Tabellenzahl, sondern nur eine Kontrolle der Windung.

## 2. Eigene Folgerungen zur Normierung [S]

- Virialsatz (Derrick-Skalierung bei festem ω): Mit T = ω²∫φ² = ωQ/2, G = ∫(|∇φ|² + m²φ²/ρ²) und P_W = ∫W gilt
  G + 3(P_W − T) = 0. Daraus folgt E_W = T + G + P_W = ωQ + (2/3)G > ωQ.
- Tabelle 10 hat E/Q = 136,06/157,09 = 0,866 < 0,99. Also ist 136,06 nicht E_W.
- In woertlicher Lesart ist E_85 = T + G + ∫U = T + G + P_W/2 = (3/4)ωQ + (5/6)G. Mit ωQ = 155,52 folgen
  G = 23,30, P_W = 69,99, E_W = 171,06 und E_W/Q = 1,089 > √1,1 = 1,049.
- Umrechnung in unsere Einheiten: S = 0,55·S̃ und x = x̃/√1,1. Dann ist W̃ = S̃ − S̃² + 0,275·S̃³,
  ω̃ = 0,99/√1,1 = 0,94393, Q̃ = 2Q = 314,18 und Ẽ = 1,90693·E (Ẽ_85 = 259,46, Ẽ_W = 326,19). Das ist nur eine
  Querkontrolle; rechnen sollte der Lauf direkt in den Einheiten der Arbeit.

## 3. Laufplan fuer die .69 (hoechstens 10 min GPU, nur nach Freigabe des Umbaus)

**Rechenort:** .69, CUDA, float64, unter Controller und gemeinsamem Lock. Start nach VS-1 (etwa 05:00) oder in einer
Portionsluecke. Code neu in coordination/runden-v3/RUNDE-01/k2/; field3d bleibt unveraendert.

**Code vorab (nicht auf der GPU-Uhr, kleiner 1 h):**
- Einfeld-Potential W(S) = c1·S + c2·S² + c3·S³ mit Kraft (c1 + 2c2·S + 3c3·S²)ψ, Siebenpunkt-Laplace wie in engine.py
- m = 1-Startfeld: Gl. 81 im kartesischen Gitter mal (x + iy)/ρ, Drehachse z
- Newton-Krylov bei festem ω:
  - Residuum −∇²ψ + (W'(S) − ω²)ψ
  - GMRES(40) mit FFT-Vorkonditionierer (−∇² + κ²)⁻¹
  - Schrittweitensteuerung ueber die Residuumsnorm
  - optional nach jedem Schritt Symmetrisierung auf den Sektor ψ(R90 x) = i·ψ(x), z-gerade
- Messgroessen: Q = 2ω∫|ψ|², E_W, E_85 = E_W − ∫W/2, G, P_W, T, Virialrest (G + 3P_W − 3T)/E_W, J_z/Q, Residuum,
  Newton-Schritte, Laufzeit, Spitzenspeicher

**Arme (L = 48, periodisch; κ = 0,346 laesst bei |x| = 24 etwa 4e−5 des Maximums [S]):**

| Arm | Gitter | Koeffizienten (c1, c2, c3) | Budget |
|---|---|---|---|
| K0 Kostenprobe | h = 0,5 (96³), 3 Newton-Schritte | (1,1; −2; 1) | bis 1 min |
| A1 | h = 0,5 (96³) | (1,1; −2; 1) | bis 2 min |
| A2 | h = 0,375 (128³) | (1,1; −2; 1) | bis 4 min |
| F falscher Koeffizient | h = 0,5 (96³) | (1,12; −2; 1), also 2 Prozent im Massenterm | bis 2 min |

- Die Atlas-Gitter N = 25 und 33 taugen hier nicht: Bei L = 48 waere h etwa 1,5 bis 2, die Ringbreite ist etwa 2.
- Ergibt K0 hochgerechnet mehr als 8 min, faellt A2 auf h = 0,4 (120³). Die Groesse wird vor A1 festgelegt, nicht
  nach einem Ergebnis.

**Vorab gebundene Auswertung:**
- Richardson aus A1 und A2 mit Ordnung 2: X_R = X_A2 + (X_A2 − X_A1)/((0,5/0,375)² − 1).
- Q_R und E85_R gegen 157,09 und 136,06:
  - "trifft" bei hoechstens 2e−3 relativer Abweichung
  - "unklar" zwischen 2e−3 und 1e−2
  - "verfehlt" ueber 1e−2
- Normierungskontrolle: Nur E_85 darf 136,06 treffen. Trifft stattdessen E_W, ist meine Lesart falsch; das wird so
  berichtet. Zusaetzlich sollte G nahe 23,30 und E_W nahe 171,06 liegen (Vorhersage aus Abschnitt 2).
- Gegenprobe 1: |Q_F − Q_A1| muss mindestens 5-mal |Q_A2 − Q_A1| sein, sonst ist die Latte zu stumpf fuer einen
  2-Prozent-Fehler (L2).
- Gegenprobe 2: |Q_A1 − Q_A2|/Q unter 5 Prozent, sonst ist das Gitter zu grob (L3).
- Kontrollen ohne Referenzwert: |J/Q − 1| unter 1e−3, Virialrest unter 1e−3.

**Abbruch:** Konvergiert Newton auf ψ ≈ 0 (Norm unter 1e−3 des Startfelds), laeuft er in eine m = 0-Loesung (J/Q
unter 0,9) oder konvergiert er in 30 Schritten nicht, gilt der Arm als "nicht konvergiert". Dann wird weder
nachjustiert noch umgedeutet; die Leitung entscheidet ueber einen neuen Anlauf.

**Rueckfall, falls der Newton-Teil nicht rechtzeitig fertig ist:** fixedq-artige Minimierung bei Q = 157,09 im
m = 1-Sektor. Kommt dabei ω = 0,99 heraus, ist der Vergleich moeglich. Kommt ω kleiner heraus, lag der Loeser auf dem
anderen Ast. Das ist dann kein Fehler des Loesers, aber auch kein Vergleich, und so wird es berichtet.

## 4. Grenzen

- Die Karte prueft den Loeser, nicht die Physik (K-2-Karte).
- Ein drehender Q-Ball auf einem kartesischen Gitter erhaelt den Drehimpuls nur naeherungsweise (field3d README).
  Deshalb die J/Q-Kontrolle.
- Fuenf Stellen aus einem Code: Selbst "trifft" heisst nur Uebereinstimmung auf etwa 1e−3, und zwar fuer eine einzige
  Konfiguration eines fremden Potentials.
- Meine Normierungslesart ist ungeprueft. Das zweite Haus liest Abschnitt 6 vor dem Lauf.

## Latten

**L1 ja** (vorab gebunden: "verfehlt" ueber 1e−2; der falsche Koeffizient muss verfehlen) · **L2 geplant** (Arm F
mit 2 Prozent Fehler im Massenterm, Faktor 5 gegen die Gitteraenderung) · **L3 geplant** (zwei Gitter, Richardson,
Grobheitsgrenze 5 Prozent) · **L4 nein** (die Tabellenwerte sind fremd und folgen nicht aus unseren Daten; nur G und
E_W sind aus ihnen abgeleitet und werden mitgeprueft) · **L5 nein** (Loeserpruefung, keine Messdaten; Nutzen hoechstens
mittel).

**Vorschlag: weiter** mit Umbau (unter 1 h Code, hoechstens 10 min .69). Die Karte bleibt offen, weil die Arbeit einen
flachen Q-Ball enthaelt. Die Latte ist aber schmaler als in KARTEN.md angenommen: fuenf statt acht Stellen, ein Code
statt drei.

## Einfach gesagt

Die Arbeit vergleicht drei Rechenprogramme fuer Bosonensterne und bekommt acht gleiche Stellen. Das gilt aber nur fuer
Sterne mit Schwerkraft ohne unsere Art von Selbstanziehung. Fuer einen Q-Ball ohne Schwerkraft gibt es nur ein
Beispiel, einen drehenden Ring, mit zwei Zahlen auf fuenf Stellen. Dazu steckt in der Arbeit eine kleine Unstimmigkeit
beim Faktor 2 im Potential, die man vor dem Nachrechnen klaeren muss. Unser Programm muesste fuer den Vergleich etwa eine
Stunde umgebaut werden; danach reichen wenige Minuten auf der Grafikkarte, um zu sehen, ob es die fremden Zahlen trifft.
