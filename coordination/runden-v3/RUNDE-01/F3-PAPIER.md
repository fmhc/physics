# F-3 Papiertest: Duenne-Wand-Grenze unseres Q-Balls gegen den MIT-Beutel

Bearbeiter: Anthropic-Agent (Opus 5.5) fuer claude-primary, Runde 1. Datei begonnen 2026-09-30 00:23:59 CEST (gemessen).
Explorativ, nur Papier. Alle Herleitungen sind eigene Schreibtischrechnungen **[S]**, ungeprueft durch ein zweites Haus;
die eingebauten Kontrollen stehen in Abschnitt 4. Nichts ist an 938 MeV oder 0,84 fm angepasst.

## Ergebnis

1. **Unser duennwandiger Q-Ball ist kein MIT-Beutel, sondern ein Fluessigkeitstropfen.** Bei fester Ladung Q gilt [S]

   E(R) = 3Q²/(16π R³) + (4π/3)·B·R³ + 4πσR²  mit  B = U(S0) = 1/2 bei S0 = 1  und  σ = √2/4.

   Der MIT-Beutel hat E(R) = a/R + (4π/3)·B·R³. Der Bewegungsterm faellt bei uns wie R⁻³, dort wie R⁻¹. Deshalb waechst
   unser Klumpen wie ein Atomkern (E ∝ Q, R ∝ Q^(1/3), konstante Dichte innen) und nicht wie ein Nukleon im Beutel
   (M ∝ N^(3/4), R ∝ N^(1/4)).
2. **Rollenzuordnung:** B entspricht der Potentialdichte im Innern, U(S0) = 1/2 (in physikalischen Einheiten m⁴/(2λ)).
   Die "innere Bewegung" ist die Phasendrehung mit ω0 = 1/√2, Energiedichte ω0²·S0. Sie verhaelt sich wie ein steifes
   Medium (Druck gleich Energiedichte), die Quarks im Beutel wie Strahlung (Druck ein Drittel der Energiedichte). Daraus
   folgt im Minimum E = 2·B·V bei uns und E = 4·B·V im Beutel [S].
3. **M·R ist nicht konstant.** Im Atlas stehen keine 3D-Werte fuer M und R, nur das exakte 1D-Profil. Aus diesem
   Profil folgen geschlossene Formeln (Abschnitt 3). An drei Atlaspunkten ω² = 0,51, 0,7 und 0,9 ergibt sich
   M·R½ = 9,26, 4,09 und 3,62. In 3D gilt duennwandig M·R ≈ 0,391·Q^(4/3), also etwa 4,7e3, 9,2e4 und 1,9e6 fuer
   Q = 1e3, 1e4 und 1e5 (mit Wandenergie). Konstant ist bei uns M·R³/Q² = 3/(8π), nicht M·R. Im MIT-Beutel ist
   M·R = (4/3)·a konstant, unabhaengig von B.
4. **Die Beutelform braucht ein zweites Feld.** Die a/R-Form entsteht, wenn die geladenen Quanten in einer Hoehle
   sitzen, die ein anderes Feld bildet (Friedberg-Lee mit Fermionen, Friedberg-Lee-Sirlin mit Bosonen,
   [aus dem Gedaechtnis]). In unserem Einfeldmodell bildet das geladene Feld seinen Beutel selbst. Dann sitzt die Ladung
   im homogenen Kondensat, nicht in einer Hoehlenmode.
5. **Codex' Potential ist das des Atlas.** coordination/exploration-20260929-qballs/pde3d/run.py (Z. 14-24) rechnet mit
   U = s − s² + s³/2, Kraft (1 − 2s + 1,5s²)ψ, E = ∫(|ψ̇|² + |∇ψ|² + U), Q = −2∫Im(ψ*ψ̇). Das ist
   L = |∂tψ|² − |∇ψ|² − U(S) wie im Atlas: gleiche Masse m = 1, Q = 2ω∫|ψ|². field3d (engine.py) benutzt dieselbe
   Normierung.

## 1. Duenne-Wand-Grenze unseres Potentials

Modell (Atlas, Einkanal): L = |∂tψ|² − |∇ψ|² − U(S), S = |ψ|², U = S − S² + S³/2, ψ = f(x)·e^(iωt).
Dann Q = 2ω∫f² und E = ∫(ω²f² + |∇f|² + U).

- **Innenraum [S]:** Bei fester Ladung und homogenem Inneren (Dichte S0, Volumen V) ist
  E = Q²/(4·S0·V) + U(S0)·V + Wand. Minimieren ueber V gibt E = Q·√(U(S0)/S0), Minimieren ueber S0 dann S0 = 1 (Minimum
  von U/S = 1 − S + S²/2) mit U/S = 1/2. Also ω0 = √(1/2), E → Q/√2, V = Q/√2 und R = 0,5527·Q^(1/3). Das stimmt mit dem
  Atlas ueberein: "U(S)/S hat bei S = 1 sein Minimum 1/2".
- **Druck im Innern [S]:** Fuer ein homogenes Kondensat ist der Druck gleich der Lagrangedichte,
  p = ω²S − U(S). Bei ω0 und S0 = 1 ist p = 1/2 − 1/2 = 0. Das Innere ist ein selbstgebundener Tropfen ohne
  Ueberdruck, wie Kernmaterie bei Saettigung. Die Energiedichte innen ist ω0²·S0 + U(S0) = 1.
- **Wand [S]:** Bei ω0 gilt im 1D-Wandprofil f'² = U − ω0²f² = f²(1 − S)²/2. Die Wandenergie je Flaeche ist
  σ = ∫(f'² + U − ω0²f²) dx = 2∫f'² dx = √2·∫0^1 (f − f³) df = √2/4 ≈ 0,354. Kontrolle: Das exakte 1D-Profil hat
  zwei Waende, und E − ω0·Q strebt dort gegen √a = 1/√2 = 2σ (Abschnitt 3).
- **Energie bei fester Ladung [S]:** E(R) = 3Q²/(16πR³) + (2π/3)R³ + √2·πR². Das Minimum ohne Wand liegt bei
  R⁶ = 9Q²/(32π²), also V = Q/√2 wie oben.

## 2. Vergleich mit MIT-Beutel und Friedberg-Lee

| Groesse | MIT-Beutel | unser duennwandiger Q-Ball [S] |
|---|---|---|
| Energie bei fester Teilchenzahl | a/R + (4π/3)BR³ | c3/R³ + (4π/3)BR³ + 4πσR², c3 = 3Q²/(16π) |
| B | Energiedichte des falschen Vakuums im Beutel | U(S0) = 1/2 (physikalisch m⁴/(2λ)) |
| innere Bewegung | N Quarks in der niedrigsten Hoehlenmode, je x/R, x ≈ 2,04 [aus dem Gedaechtnis] | Phasendrehung ω0 = 1/√2 des ganzen Kondensats, Energie ω²S0V = ωQ/2 |
| Zustandsgleichung der Bewegung | Strahlung, p = ρ/3 | steif, p = ρ |
| Gleichgewicht | E = 4BV, M·R = (4/3)a (unabhaengig von B) | E = 2BV, M·R³ = 2c3 = 3Q²/(8π) |
| Skalierung mit der Teilchenzahl | M ∝ N^(3/4), R ∝ N^(1/4) | M ∝ Q, R ∝ Q^(1/3) (Tropfen) |

- Die Minimierung von a/R + (4π/3)BR³ gibt R⁴ = a/(4πB) und E = (4/3)a/R [S, Standardrechnung]. Die
  Beutelformel stammt aus Chodos u. a., Phys. Rev. D 9 (1974) 3471, DOI 10.1103/PhysRevD.9.3471 [aus dem Gedaechtnis].
- Friedberg und Lee, Phys. Rev. D 15 (1977) 1694, DOI 10.1103/PhysRevD.15.1694 [aus dem Gedaechtnis]: Fermionen an
  ein reelles Feld σ gekoppelt; im Innern ist σ ≈ 0 und die Quarks sind leicht. Im duennwandigen Grenzfall entsteht die
  MIT-Form mit B = U(0) − U(σ_Vakuum). Die bosonische Fassung (Friedberg, Lee, Sirlin, Phys. Rev. D 13 (1976) 2739,
  DOI 10.1103/PhysRevD.13.2739, [aus dem Gedaechtnis]) gibt mit masselosen geladenen Bosonen in der Hoehle a = πQ, weil die niedrigste s-Mode kR = π
  hat [S]. In beiden Faellen bilden zwei verschiedene Felder Beutel und Inhalt.
- Coleman (Nucl. Phys. B 262 (1985) 263, DOI 10.1016/0550-3213(85)90286-X) nennt den duennwandigen Einfeld-Q-Ball
  "Q-matter" [aus dem Gedaechtnis]. Das Tropfenbild ist also bekannt.
- **In 1D fallen beide Formen zusammen [S]:** Dort ist der Bewegungsterm des Q-Balls Q²/(8·S0·R) und der des Beutels
  N·π/(2R); beide fallen wie 1/R. Der Unterschied entsteht erst in 3D (R⁻³ gegen R⁻¹) und in der Abhaengigkeit von der
  Teilchenzahl (Q² gegen N). Das exakte 1D-Profil des Atlas kann die Beutelfrage deshalb nicht entscheiden.

## 3. M und R: Atlas-Profil in 1D und duennwandige Naeherung in 3D

**Was im Atlas steht:** nur das exakte 1D-Profil S(x) = 2a/(1 + b·cosh(2√a·x)), a = 1 − ω², b = √(2ω² − 1).
Die 3D-Q-Baelle sind laut Atlas "nur numerisch bekannt"; Zahlen fuer M und R stehen dort nicht.

**Geschlossene 1D-Formeln aus dem Atlasprofil [S]** (mit L = ln[(1 + √(2a))/b]):

- Q = 2√2·ω·L
- E = √a + (2ω² + 1)·L/√2
- G = ∫f'² dx = (√(2a) − b²L)/(2√2), und E = ωQ + 2G
- halbe Breite bei halber Zentraldichte: R½ = arcosh((1 + 2b)/b)/(2√a)

| ω² | ω | Q | E = M | E/Q | R½ | M·R½ |
|---|---|---|---|---|---|---|
| 0,51 (duenne Wand) | 0,7141 | 5,341 | 4,477 | 0,838 | 2,068 | 9,26 |
| 0,70 | 0,8367 | 2,4415 | 2,2986 | 0,941 | 1,779 | 4,09 |
| 0,90 (dicke Wand) | 0,9487 | 1,2912 | 1,2690 | 0,983 | 2,852 | 3,62 |

- Nicht konstant: Der Wert faellt zwischen den drei Punkten auf weniger als die Haelfte.
- Duennwandig waechst er wie Q²/4.
- Dickwandig (ω → 1) strebt er gegen 2·arcosh 3 = 3,525. Das ist die Skaleninvarianz des 1D-NLS-Solitons (Q ∝ √a,
  Breite ∝ 1/√a). Diese Konstanz ist vorab ableitbar und kein Beutelmerkmal.

**3D, duennwandige Naeherung [S]** (unsere Einheiten m = 1, Kopplung 1; Wandenergie addiert, ihre Rueckwirkung auf R
vernachlaessigt):

| Q | R = 0,5527·Q^(1/3) | E ≈ Q/√2 + 1,357·Q^(2/3) | M·R | M·R ohne Wand (0,391·Q^(4/3)) |
|---|---|---|---|---|
| 1e3 | 5,53 | 843 | 4,66e3 | 3,91e3 |
| 1e4 | 11,91 | 7,70e3 | 9,17e4 | 8,42e4 |
| 1e5 | 25,65 | 7,36e4 | 1,89e6 | 1,81e6 |

In physikalischen Einheiten ist M·R/(ħc) = M̃R̃/λ, haengt also zusaetzlich an der Kopplung. Beim MIT-Beutel faellt B
aus M·R heraus.

## 4. Kontrollen der eigenen Rechnung

- **dE/dQ = ω:** analytisch geprueft. Aus den Formeln folgt dL/dω = −√2·ω/(b²√a), und damit dE/dω = ω·dQ/dω exakt.
- **Differenzenquotient:** ΔE/ΔQ zwischen ω² = 0,7 und 0,9 ist 0,895 und liegt zwischen den Frequenzen 0,837 und 0,949;
  zwischen 0,51 und 0,7 ist er 0,751 (Frequenzen 0,714 und 0,837).
- **Formel fuer G:** an allen drei Punkten gegen (E − ωQ)/2 nachgerechnet (0,3313; 0,12795; 0,0220).
- **Duennwandiger Grenzwert:** Bei ω² = 0,51 gilt E ≈ ω0·Q + 2σ = 4,484 gegen exakt 4,477.
- **Keine Maschinenrechnung:** Alle Zahlen sind von Hand gerechnet, mit 4 bis 5 gueltigen Stellen, weil auf dem Laptop
  keine Interpreter laufen duerfen. Ein zweites Haus sollte Abschnitt 1 und die Tabelle gegenrechnen, bevor eine Zahl
  weiterverwendet wird.

## 5. Gegenprobe Dicke-Wand-Grenze

Sie ist hier wenig wert. Die Beutelanalogie bricht nicht erst dickwandig, sondern schon duennwandig (R⁻³ statt R⁻¹).
Dickwandig bricht sie erwartungsgemaess ein zweites Mal: Es gibt kein flaches Inneres und damit kein B. In 3D waechst
dort R wie 1/√(1 − ω²), und M·R divergiert [aus dem Gedaechtnis fuer das 3D-NLS-Verhalten].

## Latten

**L1 ja** (vorab: Scheitert H, hat E(R) eine andere R-Abhaengigkeit und M·R ist nicht konstant; genau das trat ein) ·
**L2 nein** (die Dicke-Wand-Kontrolle trennt nichts, weil die Analogie schon duennwandig bricht) · **L3 entfaellt**
(analytisch; Kontrollen in Abschnitt 4) · **L4 ja** (Coleman 1985 "Q-matter"; Friedberg-Lee als Beutelgrenze mit
zweitem Feld) · **L5 nein** (kein anpassungsfreier Messbezug; nichts an Protonmasse oder -radius angepasst).

**Vorschlag: verwerfen in dieser Form.** Das Einfeldmodell ist ein Tropfen, kein Beutel, und das ist Literatur. Wer
F-3 weiterverfolgen will, braucht ein Zweifeldmodell nach Friedberg-Lee (neue Karte, Modellwechsel). Das waere dann
ebenfalls Literatur. Die Tropfenlesart (Q-Ball wie Atomkern) waere eine eigene, ebenfalls bekannte Karte.

## Einfach gesagt

Das Proton-Beutelmodell sagt: Leichte Quarks flitzen in einer Blase herum, und ihr Druck haelt die Blase gegen den
Aussendruck offen. Unser Q-Ball funktioniert anders: Das Feld dreht sich innen im Gleichtakt, und je mehr Ladung
hineinkommt, desto groesser wird der Klumpen bei gleicher Dichte, wie ein Wassertropfen oder ein Atomkern. Deshalb
waechst Masse mal Radius bei uns stark mit der Ladung, waehrend es im Beutelmodell bei gleicher Quarkzahl eine feste
Zahl ist. Unser Q-Ball ist
also eher ein Modell fuer einen Kern als fuer ein Nukleon. Fuer ein echtes Beutelmodell braeuchte man ein zweites Feld,
und genau das haben Friedberg und Lee schon vor fast 50 Jahren gebaut.
