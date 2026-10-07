# TENSOR-EIS-PYRO-1: Plan (Code-Agent, Runde 40, explorativ nach v3)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 11:38:48 CEST; Plantext Abschnitt 1 ab 11:53:09 CEST (date).
  Zeitbox 150 min, also bis 14:08 CEST.
- Grundlage: KARTE.md (TE0 bis TE3, Schwellen und Wahrscheinlichkeiten unveraendert uebernommen).
- Vorlage: RUNDE-36/tensor-eis-n/code/tn.py (kubischer Gu/Wen-Nachbau); Literatur nur ueber RUNDE-35/graviton-netz-l/DOSSIER.md
  und die Ergebnisse TENSOR-EIS-N, LAMBDA-1; kein neuer Quellenabruf.
- Kennzeichen: [M] Mathematik (vorab ableitbar), [E] hier gerechnet, [P] im Projekt schon gerechnet (mit Fundstelle),
  [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese, [F] eigene Festlegung.
- Alle Rechnungen sind synthetische Gitterrechnungen, keine Messdaten.

## 1. Schritt 1 am Schreibtisch (vor jeder Rechnung)

### 1.1 Geometrie [M]

- Kubische Kante a = 1. fcc-Primitivvektoren a1 = (0, 1, 1)/2, a2 = (1, 0, 1)/2, a3 = (1, 1, 0)/2.
- Auf-Tetraeder mit Mitte R (fcc), Ecken R + r_a, r_0 = (1, 1, 1)/8, r_1 = (1, -1, -1)/8, r_2 = (-1, 1, -1)/8,
  r_3 = (-1, -1, 1)/8. Ab-Tetraeder mit Mitte R + 2 r_0, Ecken R + 2 r_0 - r_b. Die Ecke R + r_a teilen das Auf-Tetraeder R
  und das Ab-Tetraeder mit Mitte R + 2 r_a. Kantenlaenge l_P = |r_a - r_b| = sqrt2/4.
- Je **primitiver** Zelle: 4 Ecken, 2 Tetraeder, 12 Kanten (Karte: "je kubischer Elementarzelle"; je kubischer Zelle sind es
  16, 8 und 48, die Verhaeltnisse und damit die Zaehlung bleiben gleich).
- Die Kanten bilden gerade Ketten laengs der sechs <110>-Richtungen; Periode der Kette = fcc-Vektor
  a_m aus {a1, a2, a3, a1 - a2, a2 - a3, a3 - a1}.

### 1.2 Platzierung A (xi an den Ecken, Kantenwert = Kantendehnung) [M, P]

- Eichoperator = Vertraeglichkeitsmatrix des Stabnetzes, C_A(k): 12 Eckverschiebungen -> 12 Kantendehnungen.
- Calladine/Maxwell: n_0(k) - n_s(k) = 12 - 12 = 0 je k (n_0 Nullmoden, n_s Eigenspannungen = eichinvariante Kantenmoden).
- Eigenspannung = gleichmaessiger Zug laengs einer geraden Kette. Bloch-faehig nur, wenn die Phase laengs der Kette
  trivial ist: k . a_m = 0 mod 2 pi. Das sind **sechs Ebenenscharen** im k-Raum, keine Linien.
- **Projekt [P]:** EIS-1 (RUNDE-34/eis-1/ERGEBNIS.md, Lesart) hat genau das gerechnet: 12 L^2 Eigenspannungen, "Nur auf
  den sechs Ebenen q . n = 0 (n eine <110>-Richtung) bleibt je eine". TE1 ist damit vorab bekannt.
- Erwartung: Rang 12 fuer alle k ausserhalb der Ebenen; auf einer Ebene 11, auf Schnittlinien weniger, bei k = 0 Rang 6.
  Keine Volumenmoden; die Hauptaussage von TE1 trifft ein. Die Klammer der Karte "(nur Linien oder Punkte im k-Raum)"
  trifft woertlich **nicht** ein: Die Menge ist zweidimensional (Ebenen). Im Ortsraum sind es Linien (gerade Ketten);
  das ist vermutlich gemeint, steht aber so nicht da.

### 1.3 Platzierung B (xi an den Tetraedermitten): die Karte legt das Gitter-Gradient nicht fest [F1]

Zwei Bauweisen (hoechstens zwei), beide mit 6 Eichgroessen und 12 Kantenwerten je Zelle (Calladine-Index -6):

- **B1 "Ecken folgen den Mitten":** u(Ecke) = (xi(Auf-Mitte) + xi(Ab-Mitte))/2, Kantenwert = Kantendehnung wie in A.
  Also G_B1 = C_A P mit P(k): u_a = (xi_U e^{-i k.r_a} + xi_D e^{i k.r_a})/2. Begruendung: die Regge-Lesart (Kanten =
  Laengen) bleibt, nur die Eichfreiheit sitzt in den Mitten; das ist die woertlichste Fassung der Karte.
- **B2 "Winkel an der Mitte" (Keating):** Kante (a, b) des Tetraeders T traegt delta(rho_a . rho_b)/|rho|^2, rho_a =
  Vektor von der Mitte T zur Nachbarmitte durch Ecke a. Unter glatter Verzerrung H ist das 2 rho_a^T H rho_b/|rho|^2,
  also genau die Paarprodukte e_a e_b + e_b e_a aus Ue2. Begruendung: Ue2 und die Lesart "dadurch" (Fluss durch die
  Mitten).

**B1 am Schreibtisch [M]:**
- Eine Auf-Kante (a, b) sieht nur die Ab-Mitten durch ihre Ecken: delta l = n_ab . (xi_D(b) - xi_D(a))/2, mit
  xi_D(a) bei R + 2 r_a; die Auf-Mitte verschiebt alle vier Ecken gleich. Ab-Kanten sehen nur Auf-Mitten.
- **B1 zerfaellt exakt in zwei entkoppelte Kopien.** Kopie 1: Auf-Kanten mit Eichung auf den Ab-Mitten. Die Auf-Kante
  (a, b) wirkt wie ein Stab zwischen den Ab-Mitten R + 2 r_a und R + 2 r_b (parallel, doppelte Laenge, fcc-Nachbarn).
  Jede Kopie ist also das fcc-Stabnetz mit naechsten Nachbarn (6 Staebe, 3 Freiheitsgrade je Platz), das EIS-1 als
  "fcc-Netz" gerechnet hat [P]: 3 freie Spannungsmoden bei jedem k.
- Rang je Kopie: rank = dim span{n_ab : theta_a != theta_b}, theta_a = 2 k . r_a. Das ist 3, ausser alle theta_a sind
  gleich mod 2 pi, also k im reziproken Gitter. Damit **Rang G_B1 = 6 fuer alle k != 0, 6 eichinvariante Moden je k
  im Volumen**; bei k = 0 Rang 0.
- Kleines k: die Eichbilder beider Kopien sind sym(k (x) xi) auf ihren Kanten. Glatter Sektor (Auf = Ab): 6 - 3 = 3
  eichinvariante Moden (TT, TT, Spur T wie im Kontinuum); versetzter Sektor (Auf = -Ab): ebenso 3.
- Mit der skalaren Regel je Eichplatz (2 je Zelle) bleiben 12 - 6 - 2 = 4 physikalische Moden je k: zwei
  Helizitaet-2-Paare, eines je Kopie. Erwartung fuer TE2: **vier statt zwei** positive Moden, TE2 trifft nicht ein [M].
  Das ist die Zaehlung der Karte selbst ("3 je Tetraeder", "2 Helizitaeten" je Tetraeder), mit zwei Tetraedern je Zelle.

**B2 am Schreibtisch [M]:**
- Gegenlaeufiges xi (Auf +xi0, Ab -xi0) bei k = 0 gibt auf Auf- und Ab-Tetraedern dieselben Werte
  -2 xi0 . (d_a + d_b), also eine **gleichfoermige Scherung** (yz-Scherung zu x-Verschiebung usw.). Rang G_B2(0) = 3.
- Kleines k: die Scherungen (3, Ordnung 1) und sym(k (x) xi) (3, Ordnung k) erschoepfen fuer allgemeine Richtung den
  ganzen glatten Sektor. Erwartung: **0 glatte eichinvariante Moden**, 6 versetzte. B2 traegt dann keine
  Kontinuums-Gravitonen; die Winkel allein sehen keine Metrik, weil die Mitten sie ausgleichen koennen.

### 1.4 Folgerung fuer Schritt 2 (vorab)

- A: nicht weiter bauen (keine Volumenmoden).
- B2: nicht weiter bauen, falls Schritt 1 die 0 glatten Moden bestaetigt.
- B1: einzige tragende Bauweise; Schritt 2 nur fuer B1 (Abschnitt 3 folgt nach der Zaehlung).

## 2. Schritt 1 im Code: Messgroessen und Urteilsregel TE1 (vor dem ersten Lauf festgelegt)

### 2.1 Rechnung (code/tp.py zaehlung)

- Gleitkomma: BZ-Gitter L = 24 (k = Summe m_i b_i / L), dazu 20 000 Zufalls-k (gleichverteilt in der Zelle der b_i),
  2 000 Zufalls-k auf jeder der sechs Ebenen. Je k SVD von C_A (12 x 12), G_B1, G_B2 (12 x 6); numerischer Rang mit
  Schwelle 1e-9 mal groesster Singulaerwert.
- Je Gitterpunkt: n_s (eichinvariante Moden = 12 - Rang), n_0 (Nullmoden = Spalten - Rang), Zahl n_fam der
  Ebenenscharen durch k (ganzzahlig: m_i = 0 mod L bzw. m_i - m_j = 0 mod L).
- Exakt (Bruchrechnung ueber Q(i), Phasen p_j = e^{i k_j/8} rational auf dem Einheitskreis, unnormierte Kantenvektoren):
  Rang an 6 allgemeinen Punkten, 6 Punkten auf je einer Ebene (k_y = -k_x bzw. k_y = k_x), je 3 Punkten auf Linien,
  auf denen sich zwei Scharen (k || [001]) bzw. drei Scharen (k || [1 -1 -1]) treffen, und k = 0.
- Glatt/versetzt bei kleinem k: k = eps k^ mit eps = 1e-9 und 1e-4 (k^ = 20 Zufallsrichtungen und [100], [110],
  [111]). Hauptwinkel zwischen dem Bild von G und dem glatten bzw. versetzten Sektor; n_glatt = 6 - (Zahl der Kosinus
  > 1 - 1e-6) bei eps = 1e-9, ebenso n_versetzt.
- B1-Entkopplung: max |G_B1| in den Bloecken (Auf-Kanten, xi_U) und (Ab-Kanten, xi_D).
- Beschreibend: |det C_A(k)| gegen Produkt der |sin(k . a_m/2)| an 2 000 Zufalls-k (konstanter Quotient hiesse: die
  Nullstellenmenge sind genau die Ebenen).

### 2.2 Urteilsregel TE1 (Karte: "Platzierung A (Ecken) hat keine eichinvarianten Volumenmoden (nur Linien oder Punkte im k-Raum)")

- **Hauptaussage (Urteil nach Plan):** eingetroffen genau dann, wenn
  1. an allen 20 000 Zufalls-k Rang C_A = 12 (kleinster Singulaerwert > 1e-9 relativ), und
  2. jeder rangarme Gitterpunkt (L = 24) auf mindestens einer der sechs Ebenenscharen liegt, und
  3. exakt: Rang 12 an allen allgemeinen Punkten.
- **Klammer:** "nur Linien oder Punkte" gilt als verfehlt, wenn die rangarme Menge eine Flaeche enthaelt: alle 2 000
  Zufalls-k auf einer Ebene rangarm (Rang <= 11) und exakt Rang 11 auf den Ebenenpunkten.
- **Urteil nach Kartenwortlaut:** eingetroffen nur, wenn Hauptaussage und Klammer gelten.

### 2.3 Agenten-Vorhersagen Schritt 1 (vorab, mit Zahl; gehen in kein Kartenurteil ein)

| Nr | Vorhersage |
|---|---|
| Z1 | A: n_s = n_fam an allen 13 824 Gitterpunkten; Anteil rangarmer Gitterpunkte (6 L^2 - Mehrfachzaehlung)/L^3, also unter 25 % bei L = 24; alle Ebenen-Zufallspunkte Rang 11; exakt 12 / 11 / 10 / 9 / 6 (allgemein / Ebene / Linie mit zwei Scharen / Linie mit drei Scharen / k = 0) |
| Z2 | B1: Rang 6 an allen k != 0 (Gitter und Zufall), exakt 6; Bloecke (Auf, xi_U) und (Ab, xi_D) exakt 0; k = 0 Rang 0; n_glatt = 3, n_versetzt = 3 |
| Z3 | B2: Rang 6 an allen Zufalls-k; Rang 3 bei k = 0; n_glatt = 0 und n_versetzt = 6 fuer allgemeine Richtungen |
| Z4 | |det C_A| / Produkt |sin(k . a_m/2)| ist konstant auf 1e-10 relativ |

## 3. Ergebnis Schritt 1 (Vorlauf vor dem Einfrieren, rauch-69/zaehlung-vor1.json) [E]

- Lauf: p4000a, 2026-10-04 09:56:25 bis 09:56:29 UTC, rc = 0, Code code/tp-schritt1-e93ade72.py (sha256 e93ade72...).
  Geschrieben ab 12:06:31 CEST (date). Das amtliche TE1-Urteil kommt aus dem Hauptlauf ZA mit eingefrorenem Code.
- **A:** n_s = n_fam an allen 13 824 Gitterpunkten (10 626 / 3 036 / 69 / 92 / 1 Punkte mit 0 / 1 / 2 / 3 / 6 Scharen);
  kein rangarmer Punkt ausserhalb der Ebenen; alle 20 000 Zufalls-k Rang 12; alle 6 x 2 000 Ebenenpunkte Rang 11;
  exakt 12 / 11 / 10 / 9 / 6. **det C_A = 1024 Produkt sin(k . a_m/2)** auf 1e-12 (Spanne des Logarithmus): Die
  Nullstellenmenge sind genau die sechs Ebenenscharen. Z1 und Z4 eingetroffen.
- **B1:** Rang 6 an allen k != 0 (Gitter, Zufall, Ebenen, exakt), kleinster Singulaerwert >= 0,45 relativ; Bloecke
  (Auf, xi_U) und (Ab, xi_D) <= 7e-16 und exakt null; k = 0 Rang 0; n_glatt = 3, n_versetzt = 3 in allen 23 Richtungen.
  Z2 eingetroffen.
- **B2:** Rang 6 an allen Zufalls-k, 3 bei k = 0, **4 auf den 69 Gitterpunkten mit zwei Scharen** (k || [001] usw.;
  exakt bestaetigt), nicht vorhergesagt. n_glatt = 0 fuer [111] und alle 20 Zufallsrichtungen, 2 fuer [100], 1 fuer
  [110]. Z3 eingetroffen fuer allgemeine Richtungen.
- **Folgerung (wie 1.4 vorab):** A und B2 werden nicht weiter gebaut. A hat keine eichinvarianten Volumenmoden; B2 hat
  sie, aber keine glatten (Kontinuums-)Moden ausser auf Sonderrichtungen, also keine Volumen-Gravitonen. **Schritt 2
  nur fuer B1.**

## 4. Schritt 2: Plan fuer B1 (vor dem Rauchlauf r3 geschrieben)

### 4.1 Gitteroperatoren je Kopie [F2 bis F5]

- **Raum:** Kopie 1 = Auf-Kanten (6 je Zelle) als Staebe zwischen den Ab-Mitten, die ein fcc-Gitter bilden
  (Stablaenge LBAR = 2 l_P = 1/sqrt2). Variable a_m = delta l/l (Kantendehnung, gleich der Stabdehnung), konjugiert E_m.
  Kopie 2 genauso mit Ab-Kanten und Auf-Mitten. Das ganze Netz ist die direkte Summe (Abschnitt 1.3).
- **Vektorregel (Gauss je Eichplatz):** M(k)^dagger E = 0, M[m, :] = n_m (e^{i k.b_m} - 1)/LBAR. Das ist das
  Kraftgleichgewicht an der Mitte: E^ij = Summe E_e n_e n_e ist die Spannung des Stabnetzes, d_i E^ij = 0.
- **Kruemmung [F2]:** linearisierter Regge-Kalkuel auf der Tetraeder-Oktaeder-Wabe, die die Staebe der Kopie bilden
  (je fcc-Platz zwei Tetraeder und ein Oktaeder; je Stab 2 + 2 Zellen, Diederwinkel 70,53 und 109,47 Grad, Summe 2 pi).
  Alle Zellen sind starr, also haengen die Fehlwinkel eps_e nur von Finns Kantenlaengen ab; die Fuellzellen sind ein
  Rechenmittel, keine neuen Variablen. Je Zelle D_c = d theta/d l = J_c C_c^+ (komplexer Schritt, exakt);
  d eps/d l = -Summe P_c^dagger D_c P_c. Energie (g/2) a^dagger B a mit **B = -LBAR^2 d eps/d l** (Potential = minus
  Regge-Wirkung), g = 1. Damit gilt B M = 0 exakt (flache Einbettung) und B = B^dagger (Schlaefli).
  Begruendung: Gu/Wens g a_ij R^ij ist die quadratische Einstein-Hilbert-Energie; Regge ist ihre Gitterform mit
  Kanten als Laengen (Dossier E1, E2). Andere eichinvariante Kruemmungen werden nicht gerechnet.
- **Skalare Regel (Masse):** c^dagger a = Summe_{e an v} eps_e an jeder Mitte v (linearisierte Skalarkruemmung, Dossier
  RT-1), also c_row = -Summe_m (1 + e^{-i k.b_m}) B[m, :]. Masse = Verletzung c^dagger a = rho an den Mitten der Kopie.
- **Energie mit -1/2 [F3]:** je Finns Tetraeder (Kopie 1: Auf-Tetraeder = Zelle tet2; Kopie 2: tet1)
  (J/2)[E^ij E^ij - (1/2)(E^ii)^2] mit E^ij = Summe E_e n_e n_e, also A0_ef = (n_e . n_f)^2 - 1/2, J = 1.
- Offen und nur gemessen: ob die Spur-Eichung exakt ist (A c im Bild von M, wie auf dem kubischen Gitter). Wenn nicht,
  ist die 1/2 nur bei kleinem k eine Symmetrie (LAMBDA-1).
- **Kubische Kontrolle (TE0) mit demselben Werkzeug:** Operatoren aus tn.py (inc, Spurzeile, G15, A = 1 - t t^T/2),
  durch dieselbe KKT-, FFT-, Torus- und Exponentenroutine.

### 4.2 Messgroessen

- **Statik (code/tp.py statik):** je k das KKT-System [[B, c], [c^dagger, 0]] (pinv, hermitesch, rcond 1e-10) mit
  rechter Seite (0, 1); kappa = x^dagger B x; U(R) = (1/N) Summe kappa(k) e^{i k.R} per irfftn auf dem fcc- bzw.
  kubischen Torus (L^3 primitive Zellen). Minimumtest (Tangentialeigenwerte) bei L = 64.
- **Torus-Korrektur** wie TENSOR-EIS-N: U_L = U_inf + b/L + c/L^3 exakt geloest. Finns Netz: Hauptsatz
  L = 128/160/192, Gegensatz 96/128/192. Kubisch: 128/192/256 (wie TENSOR-EIS-N), Gegensatz 64/128/256.
- **Abstand:** kubisch in Gitterabstaenden; Finns Netz in Stablaengen LBAR (Abstand naechster Massenplaetze) [F4].
- **Strahlen** (Fenster 4 <= r <= 16): kubisch wie TENSOR-EIS-N; Finns Netz [100] = j (1,0,0) (r = j sqrt2, j = 3..11),
  [110] = j a3 (r = j, j = 4..16), [111] = j (1,1,1) (r = j sqrt6, j = 2..6). Schale: alle Gittervektoren im Fenster.
  Exponent p = minus Steigung von log|U_inf| gegen log r.
- **Vorfaktor:** C(R) = -U_inf(R) r; Richtungsstreuung = (max C - min C)/Mittel C ueber alle Gittervektoren im Fenster.
- **Spektrum (code/tp.py spektrum, BZ-Gitter L = 16 ohne k = 0, je Kopie):** physikalischer Raum S = Komplement von
  Bild M + span c (2 je Kopie); omega^2 = Eigenwerte von (S^dagger A S)(S^dagger B S); "positiv" = omega^2 > 1e-9
  relativ und reell [F5]. Dazu A_phys, B_phys (Geist?), Spur-Eichdefekt |(1 - P_M) A c|/|A c|, freie Dynamik ohne
  Zwang (Eigenwerte von A B, beschreibend).
- **Kleines k** (|k| = 1e-3 und 2e-3, [100], [110], [111] und 20 Zufallsrichtungen): Tensor H der Mode aus den
  Kantenwerten (Kantenmitte-Phase abgezogen); TT-Anteil = |H_TT|^2/(|H_TT|^2 + |H_T|^2) (eichinvariant in fuehrender
  Ordnung); omega^2/k^2 je Richtung (Tempo); Kontinuumsprobe: B auf dem Komplement des Eichbilds (Signatur +, +, -).

### 4.3 Urteilsregeln (mechanisch in code/tp_auswertung.py)

- **TE0** (kubisch, U = -1/(8 pi r) auf 1 % ab r = 8): eingetroffen genau dann, wenn |U_inf 8 pi r + 1| <= 0,01 fuer
  alle Gittervektoren mit 8 <= r <= 16. Nach Plan = nach Kartenwortlaut.
- **TE1:** Abschnitt 2.2 (aus dem Hauptlauf ZA).
- **TE2** (B traegt auf der Zwangsflaeche genau zwei positive Moden mit Helizitaet +-2 und linearer Dispersion),
  ganzes Netz = Kopie 1 + Kopie 2. Eingetroffen genau dann, wenn
  1. an jedem k != 0 des Gitters L = 16 die Zahl positiver omega^2 beider Kopien zusammen genau 2 ist, und
  2. jede positive Mode bei |k| = 1e-3 einen TT-Anteil >= 0,99 hat, und
  3. |omega^2(2e-3)/(4 omega^2(1e-3)) - 1| <= 0,01 fuer jede positive Mode und Richtung.
  Nach Plan = nach Kartenwortlaut ("Platzierung B" ist das ganze Netz).
- **TE3** (Newton auf Finns Netz: Exponent 1 +- 0,02 ab r = 4, Richtungsstreuung <= 3 %), Massen in derselben Kopie.
  Eingetroffen genau dann, wenn im Fenster 4 <= r <= 16 (1) U_inf < 0 an allen Gittervektoren, (2) U_inf laengs aller
  drei Strahlen nach aussen steigt (anziehend), (3) p in [0,98; 1,02] auf drei Strahlen und Schale, (4) Streuung <= 0,03.
  - **Nach Plan:** r in Stablaengen LBAR (4 bis 16).
  - **Nach Kartenwortlaut:** r in Kantenlaengen l_P von Finns Tetraedern (4 <= r/l_P <= 16, also 2 bis 8 Stablaengen);
    Strahlen [100] j = 2..5, [110] j = 2..8, [111] j = 1..3.
  - Vermerk [M]: Massen auf Auf- und Ab-Mitten liegen in verschiedenen Kopien und wechselwirken nicht.

### 4.4 Agenten-Vorhersagen Schritt 2 (vorab; gehen in kein Kartenurteil ein)

| Nr | Vorhersage |
|---|---|
| V1 | Kontrollen: Zellmatrizen symmetrisch, l^T D = 0, Diedersummen 2 pi; Ortsraum (fcc-Torus L = 4) gegen Bloch <= 1e-12; B M = 0 und c^dagger M = 0 <= 1e-14 relativ |
| V2 | TE0 eingetroffen mit max Abweichung 0,41 % (wie TENSOR-EIS-N); U_inf bitgleich bis auf Rundung (<= 1e-12) mit TENSOR-EIS-N |
| V3 | Kontinuumsprobe: B auf dem Komplement des Eichbilds hat bei kleinem k die Signatur (+, +, -) (TT, TT, Spur) in beiden Modellen |
| V4 | TE2: je Kopie 2 positive Moden an allen k, ganzes Netz 4; TE2 also nicht eingetroffen (Bedingung 1); TT-Anteil >= 0,99 und linear |
| V5 | Tempo: omega^2/k^2 der zwei TT-Zweige haengt auf Finns Netz von der Richtung ab (Spanne > 1 %), kubisch nicht (1,000) |
| V6 | Spur-Eichung auf Finns Netz nicht exakt: Defekt > 1e-3 am Zonenrand, -> 0 fuer k -> 0; kubisch <= 1e-14 |
| V7 | Freie Dynamik ohne Zwang auf Finns Netz hat wachsende Moden (wegen V6), kubisch nicht |
| V8 | Statik Finns Netz: Minimum existiert (0 negative Tangentialeigenwerte); U < 0 und anziehend; Exponenten im Fenster 4..16 in [0,98; 1,02]; Streuung <= 3 % (TE3 nach Plan eingetroffen); im Fenster 2..8 Stablaengen Streuung > 3 % (TE3 nach Kartenwortlaut nicht eingetroffen) |

### 4.5 Laeufe auf der .69 (kleintest.sh, Spuren p4000a und p4000b)

| Lauf | Aufruf | geschaetzt |
|---|---|---|
| ZA | tp.py zaehlung --L 24 --out lauf/zaehlung.json | 5 s |
| KO | tp.py kontrolle --out lauf/kontrolle.json | 1 s |
| SP | tp.py spektrum --modell pyro1,pyro2,kubisch --L 16 --out lauf/spektrum.json | 30 s |
| P1 | tp.py statik --modell pyro1 --L 64 --L 96 --mitmin --out lauf/statik-pyro-a.json --npz lauf/statik-pyro-a.npz | 60 s |
| P2 | tp.py statik --modell pyro1 --L 128 --L 160 --out lauf/statik-pyro-b.json --npz lauf/statik-pyro-b.npz | 250 s |
| P3 | tp.py statik --modell pyro1 --L 192 --out lauf/statik-pyro-c.json --npz lauf/statik-pyro-c.npz | 300 s |
| K1 | tp.py statik --modell kubisch --L 64 --L 128 --L 192 --out lauf/statik-kub-a.json --npz lauf/statik-kub-a.npz | 200 s |
| K2 | tp.py statik --modell kubisch --L 256 --out lauf/statik-kub-b.json --npz lauf/statik-kub-b.npz | 350 s |
| AW | tp_auswertung.py --lauf lauf --out lauf/auswertung.json | 10 s |

- Zeiten geschaetzt aus rauch r2 (fcc L = 32 mit Minimumtest 2,6 s; kubisch L = 32 0,4 s), skaliert mit L^3.
- Faellt ein Lauf an der 600-s-Grenze: P3 -> L = 176 (Hauptsatz 128/160/176), K2 -> L = 224 (Satz 128/192/224).
  Vorab festgelegt.

## 5. Rauchlaeufe vor dem Einfrieren (offengelegt)

- **r1** = Schritt-1-Vorlauf (Abschnitt 3): alle Zahlen gelesen; daraus folgt die Wahl von B1 fuer Schritt 2.
- **r2** (p4000a, 10:03:53 bis 10:04:11 UTC, tp.py 05f6da30...): kontrolle, statik (fcc L = 16/32 mit Minimumtest,
  kubisch L = 16/32), spektrum L = 6. Gelesen habe ich nur: Zellkontrollen (D symmetrisch 4e-16, l^T D 9e-16,
  Diederwinkel 70,528779 / 109,471221 Grad, Summen 2 pi auf 0), Ortsraum L = 4 (B symmetrisch 3e-16, B M 5e-16,
  c M 9e-16, Spektrum Ortsraum gegen Bloch 2e-14 bei Skala 8, Statik Ortsraum gegen Fourier 3e-17), Statik-Technik
  (Zwangsresiduen <= 2e-15, Imaginaerteil kappa <= 2e-14, Spiegelsymmetrie <= 7e-18, Zeiten, Speicher) und die
  Spektrum-Identitaeten (B hermitesch, B M, c M, Rang M = 3, kleinster Singulaerwert von [M, c] 0,24 relativ).
  Keine U(r)-Werte, keine Minimumtests, keine Modenzahlen.
- **r3** (p4000a, 10:07:35 bis 10:08:35 UTC, tp.py 419d7da6..., tp_auswertung.py da90c2a4...): ganze Kette mit
  kleinen Groessen (zaehlung L = 8, kontrolle, spektrum L = 6, statik L = 32/48/64, Auswertung mit Fitsatz 32/48/64).
  Gelesen: Rueckgabewerte, Zeiten, Schluessel der auswertung.json. Die erste Auswertung brach beim JSON-Schreiben ab
  (numpy-Ganzzahl); behoben mit default-Wandler, ohne Rechenaenderung. Urteile und Zahlen der Auswertung ungelesen.
- **Regelverstoss:** Beim r3-Nachlauf stand im ssh-Befehl versehentlich `python3 -c "print()"` auf der .69 ausserhalb
  des Starters (10:08:35 UTC; leere Ausgabe, keine Rechnung). Gemeldet in ERGEBNIS, Selbstanzeigen.
- Keine Schwelle und keine Urteilsregel wurde nach einem Rauchlauf geaendert. Zeiten fuer die Hauptlaeufe aus r3:
  fcc L = 64 mit Minimumtest 20 s, kubisch L = 64 2,8 s.
