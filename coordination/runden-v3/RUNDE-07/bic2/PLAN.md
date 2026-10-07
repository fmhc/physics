# Runde 7, Karte BIC-2: Ist die Breite exakt null? (bic2)

- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung (Karte BIC-2 in RUNDE-07.md). Explorativ, v3.
- Beginn 2026-09-30 04:01:39 CEST (gemessen). Abschnitte 1 bis 6 geschrieben ab 04:31:04 (gemessen), **vor jedem
  Lauf von bic2.py** (auch vor dem Rauchtest). Ende: letzte Zeile.
- Status bei Abgabe: Code fertig, lokal nur py_compile und Rauchtest (Abschnitt 8). Alle Messlaeufe sind
  **ungerechnet**; sie laufen ueber die Leitung (Abschnitt 9).
- Neue Deutungen sind Hypothesen **[ES]**. Synthetische Kontrollen sind keine Messdatenbestaetigung.
- **Blindheit:** Die Codex-Dateien (resonance-20260930/feshbach-20260930/, 3D-OMEGA-SCAN-CODEX.md) habe ich nicht
  gelesen. Bekannt ist mir nur, was in RUNDE-06.md steht (Pflichtlektuere), darunter Codex' Arm B: gleiche Phase 0,313
  links und rechts mit Vorzeichenwechsel, Minimum-Sample 0,7976953 mit Gamma 3,7e-10. Da mein Ergebnis zu (a) in dieser
  Sitzung nicht entsteht (die Laeufe macht die Leitung), lese ich die Codex-Dateien auch danach nicht. Der Vergleich
  ist Sache der Leitung, nach Eintrag der Ergebnisse.

## Kurzfassung

- **bic2.py** ist eine Kopie von RUNDE-06/resonanz3d/resonanz3d.py. Die alten Befehle (rauch, pole, bruecke, zeit0,
  zeitlin) rechnen unveraendert; zeit0 speichert jetzt zusaetzlich Fensterraten und das Differenzsignal. Neu:
  - **exakt (a):** Pol, Eigenvektor und auslaufende Amplitude A_out je omega^2, fester Phasenbezug, Flussbreite,
    Krein-Norm; dazu die Nullstellenabbildung W(rho, omega^2) und ihre Umlaufzahl.
  - **kurve (b):** Breite und Nullstellen fuer U = S - S^2 + beta S^3 (jedes beta) und fuer U = ln(1 + S).
  - **nlfit (c):** Abklingraten aus zeit0-Ausgaben gegen eta.
- Kernvorhersagen:
  - (a) exakt null: Umlaufzahl von W gleich +-1, naechster Abstand der A_out-Kurve zum Ursprung unter 1e-8
    (in omega^2), Nullstelle bei omega*^2 = 0,79769 +- 2e-5.
  - (b) Die Nullstelle wandert mit beta nach oben, etwa x*(beta) = 0,75 / 0,775 / 0,816 / 0,83.
  - (c) Das "nichtlineare" Abklingen an omega* ist ueberwiegend die **lineare** Breite am verschobenen omega, weil der
    Stoss die Ladung und damit omega aendert (Abschnitt 5). p kommt nahe 2 heraus, aber aus diesem Grund.

## 1. Physik und Verfahren

**Gleichungen** (reduziert, U = r u, V = r v, dim = 3, l = 0):

- U'' = [dp - (omega + rho)^2] U + sp V
- V'' = sp U + [dp - (omega - rho)^2] V
- dp = U'(S) + S U''(S), sp = S U''(S)
  - U = S - S^2 + beta S^3: dp = 1 - 4S + 9 beta S^2, sp = -2S + 6 beta S^2
  - U = ln(1 + S): dp = 1/(1+S)^2, sp = -S/(1+S)^2
- Im Fenster 1 - omega < rho < 1 + omega ist nur der Kanal omega + rho offen (N_offen = 1). Bei rho* = 1,7446,
  omega* = 0,8931 liegt 1 + omega* um 0,149 hoeher.

**Drei Groessen fuer (a)**, alle in bic2.py exakt:

1. **A_out am Pol.** Newton (Pluecker-Determinante wie Runde 6) gibt den komplexen Pol rho(omega^2). Am Pol
   rechnet direkt_m die Loesungsvektoren direkt (y_a, y_b regulaer von r = h bis r_m; z1 auslaufend, z2 abklingend
   von R bis r_m). Der Nullvektor n von [y_a, y_b, z1, z2] (Spalten normiert, SVD) ist die Eigenfunktion.
   - Phasenbezug: n_b = 1. Das heisst: Der Ursprungskoeffizient des geschlossenen Kanals (V ~ n_b r) ist reell,
     positiv und gleich 1.
   - A_out = Koeffizient von w+ = exp(i q r) P(q r) im offenen Kanal; A_norm = A_out / sqrt(N_K).
   - Krein-Norm N_K = Integral ueber [0, R] von (omega + Re rho)|U|^2 - (omega - Re rho)|V|^2 (Simpson).
2. **Flussbreite.** Aus den Gleichungen folgt exakt
   [Im(U* U') + Im(V* V')]' = -2 Im rho [(omega + Re rho)|U|^2 - (omega - Re rho)|V|^2].
   Integriert von 0 bis R: Gamma = -Im rho = J(R) / (2 N_K) mit J(R) = Re q |U(R)|^2.
   - Gamma_fluss = J/(2 N_K) haengt quadratisch an A_out und hat keine Aufloesungsgrenze wie Im rho aus Newton
     (dort etwa 1e-12). So wird Gamma bis weit unter 1e-12 messbar.
   - Fuer rho > omega sind beide Terme von N_K positiv. Die Krein-Signatur ist also positiv (Punkt N7 der Literatur),
     und Gamma kann nicht negativ werden.
3. **Nullstellenabbildung W.** Bei reellem rho sind alle Koeffizienten reell. y_a (U ~ r am Ursprung) und
   y_b (V ~ r) sind die kanonischen regulaeren Loesungen. L(y) ist der Koeffizient der im geschlossenen Kanal
   wachsenden Loesung exp(+kappa r), berechnet als symplektisches Produkt Omega(y, z2) bei r_m (stabil).
   - W(rho, omega^2) := L(y_a) + i L(y_b), zwei reelle Zahlen.
   - **Satz [ES, Herleitung]:** Ein gebundener Zustand im Kontinuum (BIC) liegt genau dort, wo W = 0 ist.
     - Die regulaere Ebene P ist lagrangesch (Omega(y_a, y_b) = 0 bei r = 0, Omega ist erhalten).
     - Enthaelt P eine L^2-Loesung y*, dann ist Omega(y*, y) = 0 fuer jedes y in P. Bei grossem r ergibt das
       2 kappa d(y*) L(y) = 0, also L = 0 auf ganz P.
     - Umgekehrt: Ist L = 0 auf P, erzwingt dieselbe Identitaet parallele Fernfelder im offenen Kanal, also eine
       L^2-Kombination.
   - W = 0 sind zwei reelle Bedingungen an zwei reelle Unbekannte (rho, omega^2). Im Feshbach-Bild ist
     L(y_b) ~ c0 (rho - rho_c(omega^2)) und L(y_a) ~ Kopplung M(omega^2). Die Jacobimatrix ist also regulaer.
   - Eine regulaere Nullstelle hat die Umlaufzahl +-1 auf jeder kleinen Schleife in der Ebene (rho, omega^2). Sie
     ist **topologisch stabil**: Numerische Fehler kleiner als min |W| auf der Schleife aendern die Zahl nicht.
     Damit ist "exakt null" eine pruefbare Aussage, nicht nur eine sehr kleine Zahl.

**Zwei Berichtigungen zu Vorschlaegen der Runde 6 [ES]:**

- **Der Windungstest aus L4-BIC-LITERATUR.md (Fernfeld (c1, c2) der halbpropagierenden Loesung) taugt nicht.**
  - Nahe einer exakten BIC gilt D_+(rho reell) ~ (rho - rho_c) + i M^2: Das Fernfeld beruehrt null nur (Falte), weil
    Gamma >= 0 ist.
  - Seine Umlaufzahl ist deshalb 0, auch wenn die Nullstelle exakt ist. "0 heisst nur fast null" waere ein
    Fehlschluss. W hat diese Falte nicht.
- **Eine Umlaufzahl von A_out in (omega^2, beta) oder (omega^2, dim) ist nicht definiert.** Die Nullstellenmenge des
  Pol-A_out ist dort eine Kurve omega*^2(beta), keine isolierte Stelle; jede Schleife um einen Punkt schneidet sie.
  - Die zweite Parameterrichtung ist deshalb das reelle rho selbst (Ebene (rho, omega^2)).
  - beta dient als Robustheitsprobe: Eine regulaere Nullstelle muss mit beta stetig wandern (Teil b). Auf Wunsch kann
    exakt mit --beta und --x0/--rho0 aus kurve die Umlaufzahl fuer andere beta pruefen.

**Diskretisierung.** RK4 ist nicht symplektisch. Die diskrete BIC-Bedingung "z2 liegt in der regulaeren Ebene" bleibt
aber zwei reelle Bedingungen an (rho, omega^2). Also hat auch jede Stufe eine regulaere Nullstelle, verschoben um
O(h^4), solange die kontinuierliche eine hat. Ein Boden durch das Verfahren ist nicht zu erwarten. Moeglich ist nur
ein Unterschied O(h^4) zwischen Gamma_Newton und Gamma_fluss.

**Ablauf exakt (je Stufe h, eine Stufe je Aufruf):**

1. Profile fuer omega^2 = x0 + Offsets (Vorgabe 0, +-2e-5, +-1e-4, +-3e-4, +-5e-4, +-2e-3, +-8e-3). Die inneren
   kommen zuerst; wird die Zeit knapp, fallen aussen welche weg.
2. Alle Pole in einem Stapel (lin_multi: gemeinsames Gitter, eine Zeile je Profil).
3. Eigenvektoren am Pol: Tabelle x, Re rho, Gamma_Newton, Gamma_fluss, N_K, A_norm, arg A_norm, sig_min/sig_2.
4. Phasentest: arg A_norm modulo pi relativ zum linken Aussenpunkt, Sprung zwischen den Nachbarn der Nullstelle.
   Naechster Abstand zum Ursprung d_min aus einem komplexen Polynom zweiten Grades durch die 5 innersten Punkte.
   Kennzahl: d_min/|A'| in omega^2-Einheiten. Der Boden folgt als Gamma_min ~ 1,07 (d_min/|A'|)^2.
5. W auf einem Gitter (7 rho-Werte x Profile mit |dx| <= 5e-4); linearer Fit gibt die Nullstelle (rho*, x*) und
   det J; dazu s(x) = L(y_a) an der Stelle L(y_b) = 0.
6. Umlaufzahl von W auf zwei Rechtecken (halbe Breite 5e-4 und 1e-4 in omega^2), rho-Hoehe aus J.

**Ablauf kurve (b):**

- Profile auf einem omega^2-Raster; W bei reellem rho, 400 Punkte je omega^2 im Fenster (1 - omega, 1 + omega).
- Nullstellen von L(y_b) sind Kandidaten fuer Resonanzen; dort s = L(y_a).
- Pluecker-Newton gibt die komplexen Pole und Gamma. Aeste werden ueber benachbarte omega^2 verfolgt.
- Vorzeichenwechsel von s entlang eines Astes zeigen eine BIC. Danach bis 4 Sekantenschritte in omega^2 mit neuen
  Profilen.

**Potentiale fuer (b):**

- U = S - S^2 + beta S^3, beta = 0,40 / 0,45 / 0,55 / 0,60. Existenz: omega^2 in (1 - 1/(4 beta), 1), also untere
  Grenzen 0,375 / 0,444 / 0,545 / 0,583. Gerechnet ab 0,12 ueber der Grenze (Duennwand-Baelle machen die direkte
  Integration unsicher; das Programm meldet das Kernwachstum).
- **Log-Potential U = ln(1 + S)** (in Einheiten m = 1):
  - Das ist die flache Richtung der eichvermittelten Susy-Brechung in der Form V = m^4 ln(1 + |phi|^2/m^2),
    Affleck-Dine-Q-Baelle. Quellen aus dem Gedaechtnis, nicht nachgeprueft **[L?]**:
    - Dvali, Kusenko, Shaposhnikov, PLB 417 (1998) 99, hep-ph/9707423
    - Kusenko, Shaposhnikov, PLB 418 (1998) 46, hep-ph/9709492
    - als Standard-Testpotential u. a. bei Tsumagari, Copeland, Saffin, PRD 78 (2008) 065021, arXiv:0805.3233
  - Gruende:
    - Masse 1 am Ursprung wie unser Modell, glatt; dieselbe Stoerungsrechnung passt ohne Aenderung.
    - Q-Baelle fuer jedes omega in (0, 1).
    - **Unterscheidungspunkt:** sp = -S/(1+S)^2 wechselt nie das Vorzeichen. Bei beta = 1/2 wechselt sp bei S = 2/3.
      Findet sich hier trotzdem eine Nullstelle, ist der Mechanismus der Formfaktor (Oszillation der offenen Welle
      ueber den Ball), nicht der Vorzeichenwechsel von sp. Das beantwortet eine offene Frage aus L4-BIC-LITERATUR.md,
      Abschnitt 4.
  - Verworfen: die schwerkraftvermittelte Form m^2 |phi|^2 (1 + K ln(|phi|^2/M^2)) mit K < 0 (Enqvist, McDonald
    1998 **[L?]**). Sie gibt Gauss-Q-Baelle, aber U'(S) divergiert bei S -> 0 ohne Regularisierung. Dann fehlt ein
    sauberes Kontinuum mit Masse 1.
  - Profil: neues Schiessen in f(0) (profil_allg), da U = ln(1 + S) keinen Buckel hat.

## 2. Vorhersagen vorab (04:31, vor jedem Lauf)

**(a) Exaktheit, beta = 1/2:**

- A1: Umlaufzahl von W = +-1 auf beiden Rechtecken, auf allen drei Stufen, aufgeloest (Phasensprung < 0,4). 85 %.
- A2: Nullstelle von W bei omega*^2 = 0,797690 +- 0,000020 und rho* = 1,744623 +- 0,000015; die drei Stufen liegen
  innerhalb 1e-7 in omega^2 beieinander.
- A3: d_min/|A'| < 1e-8 (omega^2-Einheiten) auf jeder Stufe, also Gamma_min < 1e-16. Die Nullstelle von A_out
  stimmt mit der von W auf 1e-6 ueberein.
- A4: Die Phase von A_norm (modulo pi) aendert sich ueber +-8e-3 um weniger als 0,05 rad. Zwischen den beiden
  Nachbarn der Nullstelle springt sie um pi, bis auf die glatte Drift (Abweichung < 1e-3 rad).
- A5: Gamma_fluss = Gamma_Newton auf 1e-3 relativ, wo Gamma >= 1e-8 ist (|dx| >= 1e-4, h = 0,01). An den inneren
  Punkten folgt Gamma_fluss 1,07 (x - x*)^2 auf 2 %.
- A6: N_K > 0 an allen Punkten.

**(b) Robustheit:**

- B1: Fuer jedes beta in {0,40; 0,45; 0,55; 0,60} gibt es auf dem Ast der Atmungsresonanz genau einen
  Vorzeichenwechsel von s im gerechneten Bereich. 70 %.
- B2: Die Nullstelle wandert mit beta nach oben. Grobe Regel: Sie liegt beim gleichen Anteil des Existenzbereichs,
  (x* - x_min)/(1 - x_min) = 0,595. Das ergibt x*(0,40) = 0,75, x*(0,45) = 0,775, x*(0,55) = 0,816,
  x*(0,60) = 0,83, je +-0,03.
- B3: Log-Potential: Die Atmungsresonanz entspricht einem Ast mit Re rho zwischen omega + 0,5 und 1 + omega.
  - 50 %: Auf mindestens einem schmalen Ast wechselt s das Vorzeichen (Formfaktor-Nullstelle).
  - Sonst ist die Breite dort monoton wie in 1D.
  - Ich lege mich nicht auf eine Lage fest.

**(c) Nichtlineares Abklingen an omega*:**

- Modell "Stoss verschiebt omega" **[ES]**. Der Stoss (psi, psi_t mal 1 + eta) hebt die Ladung um 2 eta Q.
  - Mit dQ/domega^2 = -1346 (Q-Tabelle Runde 6: 191,392 bei 0,796, 190,046 bei 0,797) folgt
    delta x = -0,2815 eta.
  - Das passt zur gemessenen Linie der Ballfrequenz: -0,001576 bei eta = 0,01 ergibt delta x = 2 omega delta omega
    = -2,815e-3.
  - Der gestossene Ball sitzt also nicht bei omega*, sondern bei x_eff = x0 - 0,2815 eta. Er hat dort die lineare
    Breite 1,07 (x_eff - x*_dr)^2.
  - x*_dr ist die Nullstelle des Zeitgitters dr = 0,05. Aus fuenf alten Laeufen (Runde 6) schaetze ich
    x*_dr ~ 0,7979, also +2e-4 gegen die lineare Rechnung.
  - Nachrechnung der Runde-6-Laeufe mit diesem Modell (ohne jede nichtlineare Daempfung):

    | Lauf | x_eff | Modell | gemessen |
    |---|---|---|---|
    | 0,79768, eta = 0,001 | 0,79740 | 2,7e-7 | 2,1e-7 |
    | 0,79768, eta = 0,01 | 0,79487 | 9,9e-6 | 9,9e-6 |
    | 0,80, eta = 0 | 0,80000 | 4,7e-6 | 4,9e-6 |
    | 0,80, eta = 0,001 | 0,79972 | 3,5e-6 | 3,7e-6 |
    | 0,80, eta = 0,01 | 0,79719 | 5,5e-7 | 5,2e-7 |

    Das ist eine Nachrechnung bekannter Zahlen, keine Vorhersage. Die Vorhersagen stehen darunter.
- C1: zeit0 bei x0 = 0,79768, dr = 0,05, T = 3000; Rate der Atmungslinie (spaetes Fenster):

  | eta | 0,001 | 0,003 | 0,01 | 0,03 |
  |---|---|---|---|---|
  | Rate | 2,2e-7 (1,2e-7 bis 4e-7) | 1,1e-6 (0,6e-6 bis 2e-6) | 9,5e-6 (7e-6 bis 13e-6) | 7,9e-5 (5e-5 bis 11e-5) |

  - Potenzfit ueber alle vier: p = 1,75 (1,6 bis 1,9), nicht genau 2.
- C2: Das Abklingen ist exponentiell. Die drei Fensterraten stimmen auf 20 % ueberein; kein t^(-1/2) (dafuer muesste
  das erste Fenster etwa 3,4-mal schneller abklingen als das letzte).
- C3: T = 6000, eta = 0,01: gleiche Rate wie bei T = 3000 auf 10 %.
- C4: Kompensation: Ein Startball bei x0 = x*_dr + 0,2815 eta landet nach dem Stoss auf der Nullstelle. Bei
  eta = 0,01 und x0 in {0,8000; 0,8007; 0,8014} ist die kleinste Rate < 1e-6 (statt 9,5e-6). Die Parabel hat ihr
  Minimum bei x0 = 0,8006 +- 0,0003.
  - Dann ist die echte nichtlineare Daempfung bei eta = 0,01 kleiner als 1e-6. Die Hypothese p = 2 (Literatur-Agent)
    waere numerisch "bestaetigt", aber aus dem falschen Grund.
- C5 (L3): dr = 0,025, x0 = 0,79768, eta = 0,01, T = 1500: Rate 8,8e-6 +- 1e-6. x*_dr rueckt naeher an 0,79769.

## 3. Entscheidungsregeln fuer (a) (vorab)

Als Vergleichsstufen gelten h = 0,01 und h = 0,005 (Stufe 0,02 nur zur Konvergenzrichtung).

- **"exakt null"** (im linearen radialen Problem, bis zur genannten Aufloesung), wenn alle drei Punkte gelten:
  1. Die Umlaufzahl von W ist auf beiden Rechtecken und beiden Stufen +-1 (Rohwert auf 0,05 genau). Der groesste
     Phasensprung ist < 0,4 rad.
  2. min |W| auf der Schleife ist mindestens 100-mal groesser als der Stufenunterschied |W_0,01 - W_0,005| an
     denselben Punkten. Diesen vergleicht die Leitung aus den beiden JSON-Dateien (Pfadpunkte gleich, weil x und die
     rho-Hoehe aus J nahezu gleich sind; sonst Vergleich an den W-Gitterpunkten).
  3. d_min/|A'| < 1e-7 auf beiden Stufen, also Gamma_min < 1e-14. Die A_out-Nullstelle liegt innerhalb 1e-6 bei der
     W-Nullstelle.
- **"nur fast null"**, wenn alle drei Punkte gelten:
  1. Die Umlaufzahl ist 0 auf beiden Stufen, aufgeloest.
  2. d_min/|A'| > 1e-6.
  3. d_min/|A'| stimmt zwischen den Stufen auf 30 % ueberein. Dann ist der Boden Gamma_min = 1,07 (d_min/|A'|)^2.
- **"nicht entscheidbar"**, sonst. Beispiele:
  - Umlaufzahl nicht aufgeloest oder zwischen den Stufen verschieden
  - Newton an inneren Punkten nicht konvergiert
  - sig_min/sig_2 > 1e-6 am Pol (Eigenvektor unscharf)
  - Kernwachstum > 1e8
- Zusatz: Die Aussage gilt fuer das lineare Problem. Ob die nichtlineare Rechnung den Zustand haelt, beantwortet (c).

## 4. Gegenproben

- G1 **Runde-6-Werte:** Pol bei 0,797 und 0,798 aus exakt gegen die Runde-6-Tabelle (1,7443431507 - 4,985e-7 i
  bzw. 1,7447481 - 1,122e-7 i, h = 0,005); der Offset-Wert -6,8e-4 bzw. +3,2e-4 liegt nicht im Gitter, also nur
  ueber die Interpolation.
- G2 **Flussbilanz:** Gamma_fluss gegen Gamma_Newton (A5). Ist das eine unabhaengige Probe? Nur halb: Beides kommt
  aus derselben Diskretisierung. Aber Gamma_fluss braucht keine Nullstelle von D, nur den Eigenvektor.
- G3 **Anschlussrest:** sig_min/sig_2 der 4x4-Matrix am Pol (klein = sauberer Eigenvektor) und der relative Rest
  |M n|.
- G4 **Zwei Wege zur Nullstelle:** W-Nullstelle (linearer Fit auf dem Gitter) gegen A_out-Nullstelle (Polynom) gegen
  s(x) = 0.
- G5 **Kontrolle "keine BIC":** Fuer ein Rechteck, das die Nullstelle sicher nicht enthaelt, muss die Umlaufzahl 0
  sein. Aufruf: exakt mit --x0 0,800 --rho0 1,74555 --offsets 0,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4 (das Rechteck
  +-5e-4 um 0,800 enthaelt 0,79769 nicht).
- G6 **Log-Potential ohne sp-Vorzeichenwechsel** (Abschnitt 1): Unterscheidungspunkt der zwei Mechanismen.
- G7 **Kompensierter Stoss** (C4) als Gegenprobe zum Modell "Stoss verschiebt omega".
- G8 Zweithaus: Die Leitung vergleicht mit Codex' Feshbach-Arm B, erst nach dem Eintrag meiner Ergebnisse.

## 5. Latten

- **L1 (kann scheitern):**
  - A1 und A3 koennen scheitern (Umlaufzahl 0 und stabiler Boden).
  - B2 kann scheitern (Nullstelle wandert nach unten oder verschwindet).
  - C1/C4 koennen scheitern: Bleibt die Rate im kompensierten Lauf bei ~1e-5, ist die Daempfung wirklich
    nichtlinear und das Modell falsch.
- **L2 (Gegenprobe):** G5 (Rechteck ohne Nullstelle gibt 0), G7 (Kompensation), G6 (Log-Potential).
- **L3 (Numerik):**
  - drei Stufen h = 0,02 / 0,01 / 0,005 mit Rand 1e-6 / 1e-8 / 1e-10
  - Umlaufzahl gleich auf allen Stufen
  - x* auf 1e-7 stabil (0,01 gegen 0,005)
  - Gamma_fluss gegen Gamma_Newton (A5)
  - zeit0 dr = 0,05 gegen 0,025 (C5)
- **L4 (schon bekannt):**
  - Einzelresonanz-BIC durch Parameterabstimmung (Hsu u. a. 2016) und eingebettete Solitonen der Kodimension 1
    (Champneys u. a. 2001). Quellen laut L4-BIC-LITERATUR.md; nicht von mir gelesen.
  - Neu waere: Q-Ball, 3D, linear, mit topologischem Exaktheitsnachweis ueber W.
- **L5 (Messbezug):** keiner direkt. Das Modell ist ein Spielzeug-Q-Ball. Mittelbar zaehlt die Aussage
  "Lebensdauer einer inneren Schwingung nur durch Nichtlinearitaet begrenzt" fuer Q-Ball-Dunkle-Materie
  (Kusenko-Shaposhnikov **[L?]**). Das ist Hypothese, kein Messbezug.

## 6. Grenzen und Risiken

- **Profile sind teuer** (lokal 7 / 13,5 / 27 s bei Profilschritt 0,01 / 0,005 / 0,0025). exakt braucht 13 Profile
  je Stufe; auf der feinsten Stufe daher nur die 9 inneren Offsets.
- **Direkte Integration** statt Pluecker fuer Eigenvektor und W: Bei omega^2 ~ 0,8 ist das Kernwachstum bis r_m
  ~ 2,3 klein (Faktor ~10). Duennwandige Baelle (omega^2 nahe der Grenze) meldet das Programm ueber "wachstum_kern".
  Dort gelten W-Kandidaten nur unter Vorbehalt.
- **kurve findet nur Resonanzen**, deren L(y_b) auf dem rho-Raster (400 Punkte) das Vorzeichen wechselt. Zwei sehr
  nahe Nullstellen koennen fehlen.
- **nlfit** nimmt die zwei staerksten Linien mit |Re| > 1 als Atmungslinie. Liegen zwei Aeste nah beieinander (bei
  grossem eta), mittelt es sie.
- **Kompensation (C4)** setzt voraus, dass der Stoss auch beim Startball 0,8007 die Frequenz um -0,2815 eta
  verschiebt (dQ/dx aendert sich langsam). nlfit misst x_eff direkt aus der Linie nahe 0; die Parabel wird deshalb
  gegen x_eff aufgetragen, nicht gegen x0.

## 7. Rauchtest (lokal, nach Abschnitt 1 bis 6)

- Freigabe laut Leitung (Finn, 30.09. 02:42): CPU, 1 Thread, nice 19, timeout 120 s. Befehl:

      CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 19 timeout 120 \
        python3 bic2.py rauch --geraet cpu --out lauf-lokal/aus-rauchN

- Fuenf Laeufe, alle rc = 0 (Logs lauf-lokal/rauch1.log bis rauch5.log):

  | Lauf | Start | Ende | Aenderung davor |
  |---|---|---|---|
  | 1 | 04:32:52 | 04:33:37 | erster Stand |
  | 2 | 04:35:20 | 04:36:09 | Newton auf der direkten Determinante (siehe unten) |
  | 3 | 04:36:43 | 04:37:31 | Umlauf: rho-Seiten adaptiv verfeinert |
  | 4 | 04:37:47 | 04:38:54 | Gegenprobe G5 im Rauchtest |
  | 5 | 04:39:56 | 04:41:00 | Option --rc (feste Mitte fuer den Stufenvergleich); 61,7 s |

- Der Rauchtest rechnet alles mit h = 0,08 (Profilschritt 0,04), 5 Profile. Die Zahlen sind **keine Messung**.
- **Codefehler, die der Rauchtest gezeigt hat:**
  - Lauf 1: Am Pluecker-Pol war die direkte 4x4-Matrix nicht singulaer (sig_min/sig_2 = 3e-4). Pluecker-System
    (5 Komponenten, p24 = -p13 erzwungen) und direkte Vektoren sind verschiedene Diskretisierungen; die Pole weichen
    um 2,1e-5 ab (h = 0,08).
  - Ausserdem lag der Pluecker-Pol bei h = 0,08 in der oberen Halbebene (Gamma = -4,9e-6).
  - Behoben: newton_direkt poliert jeden Pol auf der direkten Determinante nach. Danach ist sig_min/sig_2 ~ 1e-15.
  - Lauf 2: Umlauf nicht aufgeloest (Sprung 1,9 rad auf einer rho-Seite mit nur 8 Punkten). Behoben mit adaptiver
    Verfeinerung der rho-Seiten und einer hoeheren Schleife (x-Seiten ueberstreichen hoechstens 2 atan(1/3)).
- **Nebenbefunde bei h = 0,08** (grob, gesehen nach Festlegung von Abschnitt 2; aendern keine Vorhersage):

  | omega^2 | Gamma (direkter Pol) | Gamma (Pluecker-Pol) | Gamma_fluss |
  |---|---|---|---|
  | 0,79758 | 9,517e-9 | -4,86e-6 | 9,525e-9 |
  | 0,79766 | 2,072e-10 | -4,87e-6 | 2,080e-10 |
  | 0,79768 | 4,07e-11 | -4,87e-6 | 4,04e-11 |
  | 0,79770 | 7,373e-10 | -4,87e-6 | 7,362e-10 |
  | 0,79778 | 1,2140e-8 | -4,86e-6 | 1,2139e-8 |

  - Direkter Pol und Flussbreite stimmen auf 0,1 bis 0,8 % ueberein.
  - Die Phase von A_norm ist ueber +-1e-4 auf 3e-5 rad konstant. Zwischen den Nachbarn der Nullstelle springt sie um
    pi - 6,5e-6.
  - Naechster Abstand der A_out-Kurve zum Ursprung: d_min/|A'| = 4,8e-12 in omega^2 (Fitrest 2e-11). Die diskrete
    Aufgabe bei h = 0,08 hat also eine exakte Nullstelle, soweit die Rechengenauigkeit reicht.
  - Die Umlaufzahl von W ist -1,0000 (aufgeloest, groesster Sprung 0,298 rad, min |W| = 2e-5).
    Gegenprobe G5 (Rechteck um 0,8003, ohne Nullstelle): 0,0000.
  - Drei Wege zur Nullstelle stimmen bei h = 0,08 auf 2e-7 ueberein: A_out 0,7976739; W-Fit 0,7976737; s(x) = 0 bei
    0,7976737.
  - Die grobe Stufe verschiebt omega*^2 um etwa -1,6e-5 gegen den erwarteten Feinwert 0,79769.
  - kurve (beta = 0,45; omega^2 = 0,78 und 0,80): Kandidat bei rho_b = 1,7155 bzw. 1,7217, Gamma = 7,7e-4 bzw. 1,9e-3.
    s < 0 an beiden Stellen, |s| waechst mit omega^2.
    - Der Vorzeichenwechsel liegt, falls es ihn gibt, unter 0,78.
    - Mit B2 (0,775 +- 0,03) ist das noch vertraeglich, aber knapp.
  - kurve (log; omega^2 = 0,7 und 0,8): Kandidat bei 1,5557 bzw. 1,6738, Gamma = 7,9e-5 bzw. 4,0e-6, s > 0 an beiden
    Stellen.
- Zeiten im Rauchtest: Profil bei Profilschritt 0,04 etwa 2 s; ein Pol-Newton fuer 5 Profile im Stapel 0,7 bis 0,9 s.

## 8. Aufrufe fuer die Leitung (.69, kleintest.sh)

- Vorbereitung: bic2.py nach /home/fmh/fmhc-physics-remote/runde7-bic2/ kopieren. Jeder Aufruf hat die Form

      cd /home/fmh/fmhc-physics-remote/runde7-bic2 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur> <kurzname> bic2.py <argumente>

- Ausgabe je Aufruf: <out>/<kommando>.json und <out>/<kommando>_bericht.txt. Beide werden nach jeder Stufe gesichert,
  ein Abbruch verliert nichts Fertiges. Zeitwaechter --budget 540 (Vorgabe); RuntimeMaxSec der Unit ist 600.
- Hochrechnung: lokale Zeiten aus Runde 6 (Profil 7 / 13,5 / 27 s bei Profilschritt 0,01 / 0,005 / 0,0025; ein
  Stapeldurchlauf 1 / 2,5 / 5 s) mal 1,2 fuer die .69. zeit0-Zeiten: Runde-6-Messung r6nlbic auf der .69 (212 s fuer
  T = 3000, dr = 0,05, drei Reihen).
- Jeder Aufruf laeuft auf einem Kern. Die Leitung kann jeden davon auch auf der Laptop-CPU starten (1 Thread,
  nice 19), mit denselben Argumenten nach `python3 bic2.py`.

| Nr | Teil | Spur | Kurzname | Argumente nach bic2.py | Hochrechnung |
|---|---|---|---|---|---|
| 1 | a | cpu2 | b2ex01 | `exakt --geraet cpu --h 0.01 --rc 1.7446225 --out aus-exakt-001` | ~5 min |
| 2 | a | cpu3 | b2ex005 | `exakt --geraet cpu --h 0.005 --rc 1.7446225 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4 --reserve 150 --out aus-exakt-0005` | ~7 min |
| 3 | a | cpu | b2ex02 | `exakt --geraet cpu --h 0.02 --rc 1.7446225 --out aus-exakt-002` | ~2,5 min |
| 4 | c | cpu4 | b2nla | `zeit0 --geraet cpu --omega2 0.79768 --eta 0,0.001,0.003 --T 3000 --dr 0.05 --out aus-nl-a` | ~3,6 min |
| 5 | c | cpu | b2nlb | `zeit0 --geraet cpu --omega2 0.79768 --eta 0,0.01,0.03 --T 3000 --dr 0.05 --out aus-nl-b` | ~3,6 min |
| 6 | a (G5) | cpu4 | b2g5 | `exakt --geraet cpu --h 0.01 --x0 0.8003 --rho0 1.745686 --offsets 0,2e-5,-2e-5,1e-4,-1e-4 --u-dx 1e-4 --w-dx 1e-4 --out aus-exakt-g5` | ~2 min |
| 7 | b (L2) | cpu | b2k050 | `kurve --geraet cpu --pot poly --beta 0.5 --h 0.02 --out aus-kurve-050` | ~4 min |
| 8 | b | cpu2 | b2k040 | `kurve --geraet cpu --pot poly --beta 0.40 --h 0.02 --out aus-kurve-040` | ~4,5 min |
| 9 | b | cpu3 | b2k045 | `kurve --geraet cpu --pot poly --beta 0.45 --h 0.02 --out aus-kurve-045` | ~4,5 min |
| 10 | b | cpu4 | b2k055 | `kurve --geraet cpu --pot poly --beta 0.55 --h 0.02 --out aus-kurve-055` | ~4 min |
| 11 | b | cpu | b2k060 | `kurve --geraet cpu --pot poly --beta 0.60 --h 0.02 --out aus-kurve-060` | ~3,5 min |
| 12 | b | cpu2 | b2klog | `kurve --geraet cpu --pot log --xmin 0.40 --xmax 0.905 --dx 0.05 --h 0.02 --out aus-kurve-log` | ~4 min |
| 13 | c | cpu3 | b2nl6k | `zeit0 --geraet cpu --omega2 0.79768 --eta 0,0.01 --T 6000 --dr 0.05 --out aus-nl-6000` | ~6,5 min |
| 14 | c (C4) | cpu4 | b2kp1 | `zeit0 --geraet cpu --omega2 0.8000 --eta 0,0.01 --T 3000 --dr 0.05 --out aus-nl-komp-1` | ~3,2 min |
| 15 | c (C4) | cpu | b2kp2 | `zeit0 --geraet cpu --omega2 0.8007 --eta 0,0.01 --T 3000 --dr 0.05 --out aus-nl-komp-2` | ~3,2 min |
| 16 | c (C4) | cpu2 | b2kp3 | `zeit0 --geraet cpu --omega2 0.8014 --eta 0,0.01 --T 3000 --dr 0.05 --out aus-nl-komp-3` | ~3,2 min |
| 17 | c (C5, L3) | cpu3 | b2nlf | `zeit0 --geraet cpu --omega2 0.79768 --eta 0,0.01 --T 1500 --dr 0.025 --out aus-nl-fein` | ~6,5 min |
| 18 | c | cpu4 | b2nlfit | `nlfit --geraet cpu --dateien aus-nl-a/zeit0.json,aus-nl-b/zeit0.json,aus-nl-6000/zeit0.json,aus-nl-komp-1/zeit0.json,aus-nl-komp-2/zeit0.json,aus-nl-komp-3/zeit0.json,aus-nl-fein/zeit0.json --out aus-nlfit` | < 10 s |
| 19 | a/b | frei | b2exB | je gefundener Nullstelle aus 8 bis 12: `exakt --geraet cpu --h 0.01 --beta <B> --x0 <x*> --rho0 <rho*> --out aus-exakt-b<B>` (x*, rho* aus kurve.json, Feld kurve.fein[].schritte[-1]; fuer log gibt es kein exakt, dort reicht kurve) | ~5 min |

- Reihenfolge: 1 bis 4 zugleich (vier Spuren), dann 5 bis 12, dann 13 bis 17, zuletzt 18 und 19. Zusammen etwa
  85 min Rechenzeit, auf vier Spuren etwa 25 min Wandzeit.
- Wird bei Nr. 2 die Zeit knapp, entfallen zuerst die aeusseren Offsets (+-5e-4); der Bericht nennt das unter
  "entfallen". Dann Nr. 2 mit `--offsets 0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4 --u-dx 3e-4,1e-4` wiederholen.
- Auswertung (a) nach Abschnitt 3:
  - Umlaufzahl, max. Sprung und min |W|: exakt_bericht.txt, Zeilen "Umlauf W".
  - Stufenunterschied: h{h}.W_gitter in exakt.json (bei festem --rc gleiche Punkte auf allen Stufen), max |W_0,01 - W_0,005|.
  - d_min/|A'|: Zeile "Naechster Abstand".
- Auswertung (c): nlfit_bericht.txt. Die Tabelle hat x_eff und "x* falls rein linear" je Lauf; C4 wird gegen x_eff
  aufgetragen.

## 9. Einfach gesagt

Ein Q-Ball kann atmen, und normalerweise verliert er dabei langsam Energie als Welle nach aussen. Bei einer bestimmten
Drehfrequenz hoert dieser Verlust fast ganz auf. Das neue Programm prueft, ob er dort genau null wird. Dafuer sucht es
einen Punkt, um den sich eine Rechengroesse einmal ganz herumdreht; so ein Umlauf kann durch kleine Rechenfehler nicht
verschwinden. Ausserdem prueft es, ob es die Nullstelle auch bei etwas anderen Kraeften im Ball gibt. Und es prueft, ob
die kleine Restdaempfung im vollen Modell nur daher kommt, dass der Anstoss den Ball ein wenig von der besonderen
Frequenz wegschiebt. Die grossen Rechnungen macht jetzt die Leitung auf der .69.

## Abgabe

- bic2.py (Stand nach Rauchtest 5), SHA-256 ad47922cb84f04bef159906e3fa480ec58932fce79329cc73cc9b426b73b9394.
- lauf-lokal/: rauch1.log bis rauch5.log und aus-rauch1 bis aus-rauch5 (Rauchtests, keine Messung).
- Ende 2026-09-30 04:42:32 CEST (gemessen nach dem Schreiben dieser Datei).

## 10. Version 2 (Auftrag der Leitung nach dem Absturz auf der .69; begonnen 05:08:50, gemessen)

- **Anlass:** exakt, beta = 0,55, x0 = 0,67343, rho0 = 1,69120, h = 0,01. Nach 7 min 29 s brach der Lauf in
  lin_fit_nullstelle ab: torch.linalg.solve meldete eine singulaere Matrix. Derselbe Fehler steckt im lokalen Lauf
  beta = 0,45 um 0,6334 ("ohne Fit").
  - Ursache: Die Mitte (kleinstes |A_norm|) lag am Rand des Offset-Gitters. Im festen Fenster +-1e-4 lag dann nur ein
    einziger omega^2-Wert, die dx-Spalte war null, J also singulaer.
- **Aenderungen** (Kopf von bic2.py, "Version 2"):
  - lin_fit_nullstelle bricht nie mehr ab:
    - Spalten skaliert, lstsq statt solve, Grenze cond J <= 1e10
    - sonst Rueckgabe "Fit nicht moeglich" mit Grund
  - Fit-Punkte: die bis zu 5 naechsten Profile (mindestens 2 verschiedene omega^2). Liegen weniger als 3 Profile im
    W-Fenster, nimmt das Programm die 3 naechsten (Vermerk "W-Gitter: ...").
  - **Ohne Fit:** Die Umlaufzahl wird trotzdem gerechnet, auf Rechtecken um x0 und Re rho des Pols dort (rho0, falls
    der Pol nicht konvergierte; --rc hat Vorrang). Halbe rho-Hoehe --u-drho-ohne-fit, Vorgabe 5e-4. Vermerk
    "Rechtecke ohne Fit um ...".
  - **Neu legen:** Liegt der Fit-Mittelpunkt ausserhalb eines Rechtecks oder in dessen aeusserem Fuenftel (in
    omega^2 oder rho), rechnet exakt zusaetzlich ein Rechteck um den Fit-Mittelpunkt.
    - Dafuer --neu-profile neue Profile (Vorgabe 3) bei x* + dx (-1 ... 1)
    - vorher ein zweiter linearer Fit auf dem neuen Gitter, der die rho-Mitte nachfuehrt
    - Das urspruengliche Rechteck bleibt im Bericht; das neue steht als "NEU GELEGT" und in JSON mit neu_gelegt = true.
    - Abschalten mit --neu-legen nein (z. B. fuer die Gegenprobe G5).
  - Sicherheitsnetz in main: Bei einem unerwarteten Fehler schreibt das Programm Traceback, Bericht und JSON und endet
    mit rc = 1.
  - Phasenspruenge ohne Division; phasentest gegen A' = 0 geschuetzt.
- **Lokaler Kurztest** (Rauchtest, gleiche Bedingungen wie Abschnitt 7): rauch6-v2 (05:11:08 bis 05:12:30),
  rauch7-v2 (05:12:53 bis 05:14:15), rauch8-v2 (05:14:26 bis 05:15:51), alle rc = 0, zuletzt 83,9 s. Geprueft (h = 0,08,
  keine Physik):
  - G5 um 0,8003: Das urspruengliche Rechteck gibt 0,0000 (keine Nullstelle innen). Das neu gelegte Rechteck um den
    Fit-Mittelpunkt 0,7976485 gibt -1,0000; der zweite Fit liegt bei 0,7976737.
  - Fit nicht moeglich (nur ein rho-Wert, W-Fenster 1e-6, also auch der Rand-Fall mit den 3 naechsten Profilen):
    Vermerk im Bericht; die Umlaufzahl um x0 ist -1,0000 (drho = 5e-4, groesster Sprung 0,384 rad).
  - Der Hauptfall (--rc fest) ist unveraendert: -1,0000.
- **Hinweis zur Zeit auf der .69:** 13 Profile bei h = 0,01 brauchten dort etwa 7,5 min. Ein neu gelegtes Rechteck
  kostet 3 weitere Profile.
  - Reicht der Waechter nicht, steht "neu legen: entfaellt (Zeit)" im Bericht.
  - Fuer Kandidaten-Laeufe daher `--offsets 0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4` (9 Profile) oder die
    Laptop-CPU nehmen.
- Deutung der gemeldeten Umlaufzahlen **[ES]**: +1 und -1 bedeuten beide eine regulaere Nullstelle von W, also eine
  exakte BIC. Das Vorzeichen ist nur die Orientierung (Vorzeichen von det J, d. h. wie sich die Linien L(y_a) = 0 und
  L(y_b) = 0 kreuzen). Die Folge -1, +1, -1 bei beta = 0,5 ist damit verstaendlich.
- bic2.py Version 2: SHA-256 1f8affbd68b2c312f85ebd0bfb2347795e6534956a7cb6b0ece7c0c99d9d86d0. Sicherung von
  Version 1: lauf-lokal/bic2-v1-ad47922c.py.bak.
- Ende Version 2: 2026-09-30 05:16:19 CEST (gemessen nach dem Schreiben dieses Abschnitts).
