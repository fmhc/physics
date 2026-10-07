# Y-1 (Runde 10): Wirbel-Dreier in einem Ball, Y-Gesetz oder Dreiecks-Gesetz? Plan und Vorab

- Bearbeiter: Anthropic-Code-Agent (Opus 5.5) fuer die Leitung claude-primary. Explorativ (v3). Alles [H]: ein Vorbild,
  kein Proton, kein QCD-Einschluss (kein Eichfeld, kein Spin 1/2).
- Zeiten (date, CEST): Beginn 10:46:26; dieser Plan ab 11:04:20, vor jedem Lauf und vor jedem Rauchtest. Kopie
  PLAN.md.eingefroren-<Zeit> vor dem ersten Lauf.
- Belegstufen: [Hand] Herleitung, [A] an der Quelle gelesen, [S] nur Suchtreffer, [num] numerisch, [num+K] mit Kontrolle,
  [H] Hypothese, [nachtr.] erst nach einem Ergebnis.
- Gelesen: ROT-1 ERGEBNIS.md, REGGE-1.md, BAND-1.md (nur lesen), rot1.py; farben-20260927/BERICHT-FARBEN.md (0, W6, 4.3),
  IDEE-UND-HANDRECHNUNG.md; RUNDE-08/fa1/ERGEBNIS.md; RUNDE-09/SUCHWORTE.md; KANDIDAT.md 3.2 und 5.1; Eto und Nitta 2012
  an der Quelle (Abschnitt 2.6).

## 1. Modell und Parameter

- L = sum_a (|d_t psi_a|^2 - |grad psi_a|^2) - U(S) + g sum_{a<b} J_ab Re[(psi_a^* psi_b)^2], U = S - S^2 + S^3/2, N = 3,
  **J_ab = 1 fuer alle drei Paare**, g = +0,5 (Haupt) und +0,2 (wie ROT-1, gleiches Vorzeichen), g = 0 als Kontrolle.
- Statische Energie bei fester Ladung (psi_a = phi_a e^{-i omega t}):
  E = Q^2/(4 N) + sum_a int |grad phi_a|^2 + int U(S) - g int C, N = sum_a int |phi_a|^2,
  C = sum_{a<b} Re[(phi_a^* phi_b)^2] = (|P|^2 - sum_a |phi_a|^4)/2, P = sum_a phi_a^2 (Identitaet der Leitung, 27.09.).
- g != 0: nur die Gesamtladung ist erhalten (KANDIDAT 3.2). Deshalb **feste Gesamtladung, ein gemeinsames omega**
  (stationaerer Zustand). g = 0: jede Q_a einzeln fest (Q/3), sonst ist das Minimum entartet.
- Gemischter Ball: psi_a = F(r)/sqrt3, gleichphasig. Mit C = S^2/3 gilt U_eff = S - b S^2 + S^3/2, **b = 1 + g/3**
  (N = 2 in ROT-1: 1 + g/4). Q = 3600 (R ~ 29), Box [-38,4; 38,4)^2, dx = 0,3 (n = 256); fein dx = 0,2.
- Anders als bei N = 2 gibt es **keine Symmetrie g <-> -g**: psi_a -> e^{i alpha_a} psi_a muesste fuer alle drei Paare
  alpha_b - alpha_a = pi/2 mod pi erfuellen, das ist fuer ein Dreieck unmoeglich (Frustration, FA-1). K4 entfaellt, an
  ihre Stelle tritt die Probe der Komponentenvertauschung (S_3).

## 2. Schreibtisch

### 2.1 Vakua und Wandtypen [Hand]

- g > 0: Das Minimum der Kopplung bei festem S ist die Gleichverteilung n_a = S/3 mit allen relativen Phasen 0 oder pi
  (C = S^2/3). Restgruppe U(1) x Z_2^2 (KANDIDAT 3.2), also vier diskrete Vakua, gekennzeichnet durch (phi_2, phi_3) =
  (theta_2 - theta_1, theta_3 - theta_1) in pi Z^2.
- Elementare Waende (ein Sprung um pi):
  - W_1: theta_1 springt gegen die beiden anderen, (phi_2, phi_3) -> -(pi, pi)
  - W_2: (pi, 0); W_3: (0, pi)
  - Die Sprungvektoren +-(1,0), +-(0,1), +-(1,1) (in pi) bilden ein **Dreiecksgitter**. Wegen S_3 haben alle drei
    Wandtypen dieselbe Spannung.
  - **W_1 + W_2 + W_3 = 0** (in den Vakuumkennzeichen): Drei verschiedene Waende koennen in einem Punkt enden. Das ist der
    Y-Knoten. Zwei gleiche Waende heben sich in den Kennzeichen auf, tragen aber zusammen eine volle Windung.
- Wandtyp: Ising-artig wie in ROT-1, d. h. an der W_1-Wand geht psi_1 durch null, psi_2 = psi_3 fuellen auf.
- Spannung bei festem S (Weg psi_1 = sqrtS cos alpha, psi_2 = psi_3 = sqrt(S/2) sin alpha):
  - Kopplungsverlust g S^2 (1 - 3 cos^2 alpha)^2/12
  - sigma_W = 2 sqrt(g S^3/12) int_{alpha_0}^{pi - alpha_0} (1 - 3 cos^2 alpha) dalpha = **0,4611 sqrt(g) S^{3/2}**
    (Integral = sqrt2 - (pi/2 - alpha_0) = 0,79873, cos^2 alpha_0 = 1/3)
  - Zum Vergleich N = 2 (ROT-1, "Pol"): sigma = sqrt(g) S^{3/2}. Die W-Wand bei N = 3 ist weniger als halb so teuer, weil
    an ihr nur ein Drittel der Kopplung fehlt.

### 2.2 Was ein Wirbel mitbringt [Hand]

- Ein Wirbel in psi_1 (bei A) laesst (phi_2, phi_3) um (-2pi, -2pi) laufen. Mit Waenden heisst das: **zwei W_1-Waende**
  gehen von A aus (oder gleichwertige Zerlegungen mit mehr Waenden). B (psi_2) bringt zwei W_2, C (psi_3) zwei W_3.
- Die Summe der drei Windungen ist null: (-2,-2) + (2,0) + (0,2) = 0. Nur der Dreier (oder Wirbel plus Gegenwirbel in
  derselben Komponente, "Meson") ist geschlossen. Ein Paar A + B allein hat (0, -2) uebrig und braucht ein W_3-Doppelband
  bis zum Ballrand (Unterschied zu N = 2).
- Zwei gleiche Waende (etwa beide W_1 von A) entsprechen im reellen Bild Knick und Gegenknick von psi_1. Sie ziehen sich an,
  koennen sich aber wegen der Windung nicht aufheben. Erwartet [H]: Sie verschmelzen zu einem **psi_1-freien Kanal**, der von
  psi_2 und psi_3 gefuellt ist; darin kann die Phase von psi_1 frei um 2 pi laufen. Kosten je Laenge etwa
  sigma_W + (g/12) S^2 w (w Kanalbreite). Alternativen: Linse aus zwei getrennten W_1-Waenden (2 sigma_W) oder leerer
  Schlitz wie ROT-1 statisch (2 sigma_Rand = b^2/sqrt2).
- Das "Doppelband" eines Wirbels heisse im Folgenden Arm, seine Spannung **tau_2**.

### 2.3 Netze [Hand]

Minimale Netze fuer drei festgehaltene Wirbel A, B, C (Kirchhoff im Dreiecksgitter):
- **Y:** Die drei Doppelbaender (2 W_1 von A, 2 W_2 von B, 2 W_3 von C) treffen sich in einem Knoten J. Bei gleichen
  Spannungen 120 Grad, J im Fermat-Steiner-Punkt; hat ein Winkel >= 120 Grad, liegt J in dieser Ecke.
  **E_Y = tau_2 L_St.**
- **Kette durch eine Ecke V:** Die Doppelbaender der beiden anderen Wirbel laufen in den Kern von V (dort wandelt sich
  W_1 + W_1 in W_3 + W_3 um, weil psi_V im Kern null ist). E = tau_2 (Summe der zwei an V anliegenden Kanten).
  Fuer >= 120 Grad ist die Kette durch die stumpfe Ecke gleich dem Y.
- **Dreieck mit einer Wand je Kante ist unmoeglich:** Mit Sprungvektoren x, y, z auf AB, BC, CA gilt z - x = (-2,-2),
  x - y = (2,0), y - z = (0,2); keine Wahl mit je einem Elementarsprung erfuellt das (geprueft: x_13 = x_12 + x_23 fuehrt
  zum Widerspruch). Das billigste Kantennetz hat vier Waende (zum Beispiel W_1 auf AB und CA, W_2 + W_3 auf BC), also
  sigma_W (a + b + 2c), fuer das gleichseitige Dreieck 4 a sigma_W = 2 a tau_2 (bei tau_2 = 2 sigma_W), so viel wie die
  Kette und mehr als Y (1,732 a tau_2).
- Folgerung [Hand, H]: **Erwartet ist das Y-Gesetz mit sigma_Y = tau_2**, nicht das Dreiecks-Gesetz. Ein Dreiecks-Fit mit
  freier Steigung kann trotzdem an Einzelreihen passen (gleichseitig allein ist in beiden Gesetzen linear); getrennt wird
  ueber die Form (Abschnitt 3).
- Gemeinsame Phase [Hand, H]: Ausserhalb der Baender sind die Phasen verriegelt. Um jeden einzelnen Wirbel windet die
  gemeinsame Phase dann nicht (der Arm schluckt die Windung), um den ganzen Dreier windet sie einmal. Der "ganze Wirbel" der
  gemeinsamen Phase sitzt deshalb **im Knoten J** (Y) bzw. in der mittleren Ecke (Kette). Messbar als Windung 2 von
  P = sum_a psi_a^2 (psi.psi). Folge: keine lange log-Wechselwirkung zwischen den drei Wirbeln (anders als bei g = 0).

### 2.4 Zahlen fuer die Spannungen [Hand] (festes S = b, duennwandig)

| g | b | sigma_W | 2 sigma_W (Linse) | Kanal sigma_W + (g/12) b^2 w | 2 sigma_Rand = b^2/sqrt2 (Schlitz) | ROT-1 N = 2: statisch / 2 sigma_Pol |
|---|---|---|---|---|---|---|
| 0,5 | 1,1667 | 0,411 | 0,822 | 0,411 + 0,057 w | 0,962 | 0,973 / 1,749 |
| 0,2 | 1,0667 | 0,227 | 0,454 | 0,227 + 0,019 w | 0,805 | 0,613 / 1,000 |

- Arbeitswert **tau_2(0,5) = 0,6 +- 0,2**, **tau_2(0,2) = 0,3 +- 0,12**. Verhaeltnis tau_2(0,2)/tau_2(0,5) = 0,45 bis
  0,65 (Kanal oder Linse; Schlitz gaebe 0,84).

### 2.5 Pruefgroesse ohne Nullpunkt [Hand]

- Verhaeltnis L_St/(P/2) (P Umfang): kollinear 1, gleichseitig 2/sqrt3 = 1,1547. Die Gesetze unterscheiden sich also
  hoechstens um 15,5 %. Das verlangt Formvariation bei gleicher Groesse und Energiedifferenzen, die viel genauer sind
  als 15 % der Bandenergie.
- **Steigungsverhaeltnis R = (dE/da, gleichseitig) / (dE/dl, kollinear mit Armen l):** Y: sqrt3/2 = **0,866**; Dreieck:
  1,5/2 = **0,750**; Grenze 0,808. Beide Steigungen sind frei vom Nullpunkt (Kern-, Knoten- und Ballbeitraege).
- Zusaetzlich zwei Zweiparameter-Fits E = E_c + sigma L ueber alle Geometrien eines g, mit L = L_St (Y) bzw. P/2
  (Dreieck); Vergleich der Restfehler.
- Eichung: Meson (psi_1-Wirbel plus psi_1-Gegenwirbel, Abstand d) misst tau_2 direkt: E = E_c + tau_2 d. Dann sagt Y
  sigma_Y = tau_2 vorher, das Dreieck mit Paarbaendern sigma_Delta = tau_2 (E = tau_2 P/2), gleichseitig also 1,732 gegen
  1,500 tau_2 je Seitenlaenge.

### 2.6 Eto und Nitta 2012 an der Quelle [A] (arXiv:1201.0343v2, PRA 85, 053645)

- Modell: Gross-Pitaevskii mit Rabi-Kopplung -omega_ij psi_i^* psi_j, also **erste Ordnung** in der relativen Phase
  (-2 v_i v_j omega_ij cos(theta_i - theta_j)), dazu g_ij |psi_i|^2 |psi_j|^2 (Gl. 1).
- Je Bruchwirbel eine Wand: Beim (1,0,0)-Wirbel "stick together" die beiden Waende der relativen Phasen zu einer mit
  T_1 = sqrt(T_12^2 + T_31^2) < T_12 + T_31 (Gl. 10, S. 3).
- Z_3-symmetrischer Fall (alle omega gleich): Dreier als **gleichseitiges Dreieck der Wirbellagen**, Groesse
  A ~ 0,56 omega^{-0,25} (Gl. 11, Abb. 4). Die Wirbel liegen so dicht, dass man die Waende nicht sieht (S. 3). Bei
  omega_12 = 0 "Stab" (Kette), bei grossem omega_12 kollabiert das Dreieck (Abb. 3).
- Relaxation mit freien Wirbeln (Fussnote 18), also **keine** Energie gegen festgehaltene Geometrie und **kein** Y-
  gegen-Dreieck-Vergleich. Eine Quark- oder Baryon-Analogie steht in den Seiten 1 bis 5 nicht (Berichtigung zu SUCHWORTE
  B3.2 [S]: "ausdrueckliche Quark-Einschluss-Analogie" dort nicht gefunden).
- Unterschied zu uns: Unsere Kopplung ist zweiter Ordnung (cos 2 Delta), je Wirbel also **zwei** pi-Waende (Z_2 statt
  Wicklungswand), und der Ball ist endlich (Rand, feste Ladung).

## 3. Geometrien und Zahlen je Gesetz

Ecken mit Schwerpunkt im Ursprung; A = psi_1-Wirbel, B = psi_2, C = psi_3 (je Windung +1). Kette = kuerzeste Kette.

| Geometrie | Ecken | L_St (Y) | P/2 (Dreieck) | Kette | Knoten Y |
|---|---|---|---|---|---|
| gleichseitig a = 6 / 9 / 12 / 15 | Umkreis a/sqrt3; A bei 210, B bei 330, C bei 90 Grad | 10,392 / 15,588 / 20,785 / 25,981 | 9 / 13,5 / 18 / 22,5 | 12 / 18 / 24 / 30 | Mitte |
| gestreckt, Spitze C 40 Grad, Schenkel l = 9 / 13 | A, B = (-+0,34202 l, -0,31323 l), C = (0; 0,62646 l) | 13,789 / 19,917 | 12,078 / 17,446 | 15,156 / 21,892 | (0; -0,1157 l) = (0; -1,04) / (0; -1,50) |
| stumpf, Spitze B 150 Grad, Schenkel l = 6 / 9 | B = (0; 0,17255 l), A, C = (-+0,96593 l; -0,08627 l) | 12 / 18 | 11,796 / 17,693 | 12 / 18 | in B |
| kollinear, B in der Mitte, Arme l = 5 / 6,5 / 8 / 10 | A = (-l, 0), B = (0, 0), C = (l, 0) | 10 / 13 / 16 / 20 | 10 / 13 / 16 / 20 | 10 / 13 / 16 / 20 | in B |

- Mit tau_2 = 0,6 (g = 0,5) sagt Y fuer gleichseitig a = 9 -> 15 den Anstieg 0,6 x 10,39 = **6,24** vorher, das Dreieck mit
  sigma_Delta = tau_2 **5,40**; kollinear l = 6,5 -> 10: beide **4,20**.
- Gleiche L_St, verschiedene Form: gleichseitig a = 9 (15,59), gestreckt l = 9 (13,79) und kollinear l = 8 (16):
  Y ordnet E nach L_St, das Dreieck nach P/2 (13,5 / 12,08 / 16). Kollinear l = 8 liegt im Y-Bild **ueber** a = 9
  (16 > 15,59), im Dreiecksbild **deutlich darueber** (16 > 13,5).
- Umkreisradius hoechstens 10, Ballradius ~ 29: Abstand jeder Ecke zum Rand >= 18 > Armlaenge (<= 10). Ein offenes Netz
  (Arme zum Rand) ist teurer als der geschlossene Dreier.

## 4. Rechnung

- Code y1.py (Kopie von rot1.py, erweitert). Unterbefehle:
  - **dreier** (g = 0,5 bzw. 0,2, Saat neutral / Y / Kette)
  - **meson** (psi_1-Wirbel und -Gegenwirbel, d = 6 / 9 / 12 / 15; dazu paar3: A = psi_1, B = psi_2 ohne C)
  - **k1** (N = 2 mit psi_3 = 0 wie ROT-1 paar)
  - **null** (g = 0)
  - **fein**
- Gradientenfluss wie ROT-1 paar: halbimplizit, tau = 0,5, 12000 Iterationen (Pseudozeit 6000). Phasenklammer im Ring
  0,5 < r < 2 um jeden Wirbel (Phase der eigenen Komponente = +-Winkel + bester Mittelwert, Betrag frei).
- **Neu: Schwerpunktbindung.** BAND-1 statisch zeigte, dass der Ball bei fester Ladung frei gleitet, bis ein Wirbel
  draussen liegt (bandstat2 nicht konvergiert). Deshalb wird der S-Schwerpunkt nach jedem Schritt per Fourier-Verschiebung
  auf den Dreiecksschwerpunkt (Ursprung) zurueckgesetzt (Nebenbedingung, nicht Kraft). Die aufsummierte Verschiebung wird
  berichtet. Empfindlichkeit: ein Lauf mit Ziel Steiner-Punkt.
- Saaten (alle mit psi_a = F/sqrt3 |v_a| e^{i theta_a}):
  - neutral: theta_a = Winkel um den eigenen Wirbel (die Anfangswaende liegen auf Thales-Kreisen der Kanten, also eher
    dreiecksartig)
  - Y: theta_a = arg(x - J) + f(arg(x - x_a) - arg(x - J)), f staucht die 2 pi-Aenderung in eine Linse der Halbbreite 1 um
    den Arm (wie BAND-1 band2)
  - Kette durch V: wie Y mit J = V
  - E(Geometrie) = kleinste konvergierte Energie ueber die Saaten; jede Saat wird mit ihrem Netz berichtet.
- Messungen je Lauf:
  - E und Teile, omega, Q_a/Q; Konvergenz max |E - E(1000 Iterationen davor)|
  - **Knoten:** Lagen der Windungsbloecke von arg P (P = psi.psi); Soll: Windung 2 im Knoten
  - Kreis um alle drei (Radius Umkreis + 3): Vorzeichenwechsel von cos 2 Delta_ab je Paar (0 = geschlossenes Netz)
  - Armprofil: n_a/S entlang der Strecke Wirbel a -> Steiner-Punkt und an den Kantenmitten (Kanal, Linse oder Schlitz)
  - Klumpenzahl (Ball ganz?)
  - Bilder: RGB aus (n_1, n_2, n_3)/S, S, Kopplungsdefizit g (S^2/3 - C) (Bandenergiedichte), arg P mit Windungen

## 5. Kontrollen

- **K1** (Code und ROT-1): k1 mit psi_3 = 0, Q = 700, L = 38,4, tau = 0,3, 6000 Iterationen, ohne Schwerpunktbindung,
  g = 0,5 und 0,2, d = 5 / 6,5 / 8 / 9,5 -> dieselben E wie ROT-1 paar_ergebnis.json.
- **Eichung tau_2** (zwei Wirbel allein): Meson bei g = 0,5 und 0,2; Vergleich mit ROT-1 (0,97 / 0,61 statisch, N = 2).
  paar3 (A + B ohne C): Y mit dem Rand, Steigung (sqrt3/2) tau_2 = 0,866 tau_2 [Hand].
- **g = 0:** dieselben 12 Geometrien, Q_a einzeln fest; keine Waende, kein linearer Anstieg.
- **fein:** dx = 0,2 fuer gleichseitig a = 12 und kollinear l = 8 (bester Saat-Typ aus grob) und Meson d = 12.
- **S_3:** gestreckt l = 9 mit vertauschten Komponenten (zyklisch und eine Transposition): gleiche E.
- **Schwerpunktziel:** gestreckt l = 13 mit Ziel Steiner-Punkt statt Schwerpunkt.

## 6. Vorab (p = meine Wahrscheinlichkeit)

| Nr. | Erwartung | p |
|---|---|---|
| V1 | g = 0,5: geschlossenes Netz (0 Wechsel auf dem Kreis um alle drei) bei der besten Saat in allen 12 Geometrien | 0,8 |
| V2 | Knoten (arg-P-Windung) innerhalb 1,5 vom Steiner-Punkt bei gleichseitig und gestreckt, innerhalb 1,5 von B bei stumpf und kollinear (beste Saat) | 0,65 |
| V3 | Die Y-Saat gibt in >= 5 der 6 spitzwinkligen Geometrien die kleinste Energie (Gleichstand auf 1e-3 zaehlt als Y, wenn das Netz Y ist) | 0,6 |
| V4 | Die neutrale Saat endet in >= 4 der 6 spitzwinkligen Geometrien im Y-Netz (nicht in einem Kantennetz) | 0,5 |
| V5 | Kette gleichseitig a >= 9 bleibt Kette und liegt um (2 - sqrt3) a tau_2 +- 40 % ueber Y | 0,35 |
| V6 | Steigungsverhaeltnis R (g = 0,5, gleichseitig a = 9..15 gegen kollinear l = 6,5..10) in [0,81; 0,92] | 0,55 |
| V7 | Y-Fit (alle Geometrien, g = 0,5) hat kleineren Restfehler (RMS) als der Dreiecks-Fit | 0,7 |
| V8 | sigma_Y (Fit) = tau_2 (Meson) +- 25 % | 0,5 |
| V9 | tau_2(0,5) in [0,4; 0,8] | 0,6 |
| V10 | tau_2(0,2)/tau_2(0,5) in [0,45; 0,65] | 0,5 |
| V11 | Arm = Kanal: n_a/S auf der Armmitte < 0,1 bei S > 0,5 S_0 (sonst Linse oder Schlitz) | 0,5 |
| V12 | g = 0: \|dE/dL_St\| < 0,2 tau_2(0,5) | 0,7 |
| V13 | S_3-Probe: E gleich auf <= 1e-9 relativ | 0,95 |
| V14 | fein gegen grob: E(gleichseitig 12) - E(kollinear 8) auf 3 % gleich | 0,7 |
| V15 | K1: E gleich ROT-1 auf <= 1e-8 relativ | 0,8 |
| V16 | "Zweier schlaegt Dreier" (Paar plus Einzelwirbel mit Band zum Rand) in keiner Geometrie bei g = 0,5 | 0,85 |
| V17 | g = 0,2: R ebenfalls in [0,81; 0,92] | 0,45 |
| V18 | paar3: Steigung 0,866 tau_2 +- 30 % | 0,4 |

## 7. Scheiterregeln (vorab, je g)

- **Y bestaetigt** (im Sinn von v3: getroffen), wenn alle drei gelten:
  - R >= 0,808
  - Restfehler(Y-Fit) < Restfehler(Dreiecks-Fit)
  - Knoten bei Steiner bzw. in der stumpfen Ecke in >= 2/3 der Geometrien (V2-Kriterium).
- **Dreieck bestaetigt**, wenn R < 0,808 und Restfehler(Dreieck) < 0,77 x Restfehler(Y).
- **Weder noch**, wenn keine der beiden Regeln greift oder beide Fits Restfehler > 10 % der E-Spanne haben.
- **Zerfall ("Zweier schlaegt Dreier")**, ein eigener, erlaubter Ausgang, wenn bei der besten Saat in >= 1/2 der
  Geometrien:
  - der Kreis um alle drei >= 2 Wandwechsel zeigt (Arme zum Rand), oder
  - der Ball in >= 2 Klumpen zerfaellt.
  - Dann wird beschrieben, welcher Wirbel frei wird und welches Paar verbunden bleibt.
- **Nicht auswertbar**, wenn die Konvergenz (max \|dE\| in 1000 Iterationen) fuer mehr als 1/4 der Laeufe ueber 0,02
  liegt.
- Grenzfaelle nach Wortlaut. Keine nachtraegliche Aenderung von Geometrien, Fenstern oder Schwellen.

## 8. Zweiter Arm "andere Theorie" (nur bei Zerfall nach 7)

- Nur wenn der Ausgang "Zerfall" eintritt: dieselbe Rechnung mit + c sum_a \|psi_a\|^4, c = 0,4 > \|g\| J/2 = 0,25
  (g = 0,5).
- **Das ist eine andere Theorie, nicht die Gesamtformel.** Vorab dazu [Hand]:
  - Bei g > 0 aendert c das Vakuum nicht (gleichphasige Gleichverteilung bleibt; BERICHT-FARBEN 4.3: A < 0, B > 0).
  - c verteuert jede Entmischung, also Ising-Waende und Kanaele: tau_2 steigt um grob c b^2 w/3.
  - Der Schalter c > \|g\|J/2 aus BERICHT-FARBEN betrifft g < 0 (gleichseitiger Dreier (1, omega, omega^2) statt Paar).
    Faellt der Arm an, rechne ich zusaetzlich g = -0,5, c = 0,4 mit derselben Geometriereihe.

## 9. Aufrufe, Budget

- Aus /home/fmh/fmhc-physics-remote/runde10-y1/ ueber kleintest.sh, Spuren p4000a und p4000b, je Aufruf <= 10 min,
  Budget im Skript 480 s.
- Rauchtest lokal: CPU, 1 Thread, nice -n 19, timeout 120, dx 0,6, wenige Iterationen.
- Geplant (Reihenfolge):
  1. k1
  2. meson (g = 0,5 / 0,2, paar3)
  3. dreier g = 0,5 neutral
  4. dreier g = 0,5 Y
  5. dreier g = 0,5 Kette + S_3 + Schwerpunktziel
  6. dreier g = 0,2 (Y und neutral)
  7. null
  8. fein
- Schaetzung: 12 Konfigurationen x 3 Komponenten bei n = 256 etwa 20 ms je Iteration (aus ROT-1 bandstat2), 12000
  Iterationen etwa 4 min je Aufruf.

## 10. Nachtrag 11:19:36 (date), nach den lokalen Rauchtests, vor jedem Ergebnis der .69

- Rauchtests lokal 11:14 bis 11:18 (CPU, 1 Thread, nice 19, timeout 120, dx 0,6, 300 Iterationen; lauf-lokal/). Nur
  Programmpruefung, keine Physik (nicht konvergiert).
- Aenderung an der Auswertung (nicht an der Physik): Die Knotensuche maskierte die Plaketten von arg P mit \|P\|. Im Knoten
  ist aber auch S fast null (Rauchtest: Dichteloch im Steiner-Punkt der Y-Saat, in der Ecke A der Kettensaat). Deshalb:
  - Plaketten ohne Dichtemaske (nur Ballinneres)
  - zusaetzlich die Umlaufwindung von P auf Kreisen r = 1,5 und 3 um A, B, C und den Steiner-Punkt
  - Knotenklasse zuerst ueber "Umlaufwindung 2 bei r = 3"
  - Dichteloch S_min/S_0 in r < 2 um A, B, C, J
- Beobachtung aus dem Rauchtest [H, nicht gewertet]: Der "ganze Wirbel" der gemeinsamen Phase im Knoten hat einen Kern mit
  S -> 0. Der Knoten kostet also Kernenergie. Das ist fuer alle Y-Geometrien mit innerem Knoten gleich (Achsenabschnitt),
  fuer Kette und stumpf/kollinear sitzt er in einer Ecke. R (PLAN 2.5) ist davon frei.
- Selbstanzeige: Kurz vor 11:17:06 habe ich lokal versehentlich einen leeren `python3 -` mit leerem, gequotetem Heredoc
  gestartet (Rest eines Befehlsmusters). Gerechnet wurde nichts. Bitte ins Arbeitsfeld uebernehmen.
- Code auf der .69: y1.py sha256 fd60ac15a9c62bba..., per neue Datei + mv. Laeufe ab 09:18:37 UTC (11:18:37 CEST).

## 11. Nachtrag 11:28:44 (date), NACH den Ergebnissen dreier_y und dreier_neutral (g = 0,5), vor dreierc/mesonc

- Offengelegt: Ich kenne die g = 0,5-Ergebnisse von dreier_y und dreier_neutral (beide Saaten enden im selben Zustand,
  Energien gleich auf 1e-6) und K1 (E wie ROT-1 auf alle gedruckten Stellen).
- Beobachtet [num, noch nicht ausgewertet]: **keine Waende, keine Kanaele zwischen den Wirbeln.** Jeder Wirbel hat einen
  grossen Kern ohne die eigene Komponente (Radius ~3). Der Rauchtest (Windungszaehlung, 11:26) zeigt dafuer den
  Mechanismus: ein Gegenwirbel derselben Komponente im Kern schirmt den festgehaltenen Wirbel ab, und die drei
  Ausgleichswirbel sitzen zusammen in einem Loch mit S -> 0 (ganzer Wirbel: bei kleinen Dreiecken im Steiner-Punkt, bei
  grossen in einer Ecke). E(Groesse) flacht ab.
- Das Band reisst also durch Paarbildung in den Wirbelkernen. Das faellt nicht unter den Wortlaut von "Zerfall" in 7
  (keine Arme zum Rand, ein Klumpen). Ich werte 7 trotzdem nach Wortlaut aus und beschreibe den Mechanismus getrennt.
- Die Karte verlangt bei "keinem stabilen Dreier" den zweiten Arm. Ich rechne ihn deshalb jetzt, obwohl der Ausloeser in
  8 enger gefasst war (Abweichung vom Plan, hier offengelegt). **Andere Theorie**, nicht die Gesamtformel:
  + c sum_a \|psi_a\|^4, c = 0,4, g = 0,5.
- Vorab zum zweiten Arm (vor dem Lauf):

| Nr. | Erwartung | p |
|---|---|---|
| C1 | Mit c schrumpfen die Kerne; an >= 8 von 12 Geometrien kein Gegenwirbel (eigene Windung bei r = 4,5 bleibt 1) | 0,5 |
| C2 | Arme als Kanal oder Wand (n_a/S < 0,1 auf der Armmitte) an >= 6 von 12 Geometrien | 0,4 |
| C3 | Y nach Regel 7 (R >= 0,808, Y-Fit besser, Knoten) | 0,3 |
| C4 | Meson mit c: E(d) linear, Steigung tau_2 zwischen 0,8 und 1,6 | 0,35 |
| C5 | Mit c derselbe abgeschirmte Zustand wie ohne c (E flacht ab) | 0,35 |

- Laeufe: dreierc (12 Geometrien, Y-Saat), mesonc (Meson d = 6/9/12/15 und vier Geometrien mit neutraler Saat), dazu
  dreier_y und meson noch einmal mit den neuen Windungsdiagnosen (Ausgabe ausgabe_diag; Physik und Code-Pfad gleich,
  also zugleich Reproduktionsprobe). Code y1.py sha256 f9e483e8... (nur Diagnosen und Unterbefehle neu).
- g = -0,5 mit c (gleichseitiger Dreier als Vakuum) rechne ich nicht: Die Saat braucht dort das chirale Vakuum, das ist in
  der verbleibenden Zeit nicht sauber zu bauen.

## 12. Nachtrag (Zeit in der Zeile darunter, date), nach meson und dreier_kette, vor dreier_k4

- Zeit: siehe Zeile "Nachtrag 12 geschrieben" am Ende dieses Abschnitts.
- Offengelegt: meson (g = 0,5 / 0,2) und dreier_kette sind gelaufen. Das Meson flacht ab (g = 0,5: E(6/9/12/15) =
  2144,55 / 2148,38 / 2149,02 / 2149,11), also reisst auch das Band zwischen Wirbel und Gegenwirbel. Die Knotenlage
  (Plaketten) liegt bei gestreckt und stumpf 6 auf einer Kantenmitte, nicht im Steiner-Punkt; die Klasse "Steiner" aus
  der Umlaufwindung bei r = 3 ist dort zu grob (wird in ERGEBNIS berichtigt, nicht umgedeutet).
- Frage: Liegt das Reissen am Modell oder an der Klammer? Der Klammerring (0,5 < r < 2) liegt innerhalb des entleerten
  Kerns (Radius ~3); der Gegenwirbel sitzt knapp ausserhalb des Rings. **dreier_k4:** derselbe Y-Lauf mit Ring bis r = 4
  (Gegenwirbel muesste dann in dichtes Feld). Geometrien mit Kanten > 8: gleichseitig 9 / 12 / 15, gestreckt 13, stumpf 9,
  kollinear 8,5 / 10 / 12; Meson d = 9 / 12 / 15 / 18. Keine Aenderung der Physik, nur der Klammer.
- Vorab (p):

| Nr. | Erwartung | p |
|---|---|---|
| K4a | kein Gegenwirbel (eigene Windung bei r = 4,5 bleibt 1) an >= 6 von 8 Dreiern | 0,5 |
| K4b | Arme als Kanal (n_a/S < 0,1 auf der Armmitte) an >= 4 von 8 | 0,45 |
| K4c | Y nach Regel 7 (R aus gleichseitig 9..15 gegen kollinear 8,5..12) | 0,3 |
| K4d | Meson linear bis d = 18, Steigung 0,3 bis 1,0 | 0,4 |
- Nachtrag 12 geschrieben: 2026-09-30 11:31:08 CEST; y1.py sha256 d04cdfd861c11928...
