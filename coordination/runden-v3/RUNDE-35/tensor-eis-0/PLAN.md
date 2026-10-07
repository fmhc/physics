# TENSOR-EIS-0: Plan des Code-Agenten (Runde 35)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-03 21:37:48 CEST (date). Plan geschrieben ab 21:58 CEST
  (date vor dem Schreiben: 21:57:10), vor jeder Hauptrechnung.
- Karte: KARTE.md (unveraendert). Vorhersagen T0 bis T4 und ihre Schwellen sind woertlich uebernommen.
- Kennzeichen: [L] Literatur, [L?] Literatur ungeprueft, [S] an der Quelle gelesen, [H] Hypothese,
  **[A]** = vom Agenten festgelegt, weil die Karte es offenlaesst.

## 1. Was gerechnet wird (unabhaengig von den Schreibtischformeln)

- **Gitter [A]:** periodisch kubisch, Gitterabstand 1, gestaffelt (Yee-artig):
  - E_xx, E_yy, E_zz auf den Knoten n
  - E_xy auf der Plakette n + (1/2, 1/2, 0), E_yz auf n + (0, 1/2, 1/2), E_zx auf n + (1/2, 0, 1/2)
  - Vektorladung rho_j auf dem j-Link n + e_j/2; Skalarladung auf dem Knoten n.
- **Gitterableitung [A]:** Differenz naechster Nachbarn im Abstand 1, zentriert auf dem Zwischenort
  (z. B. d_x E_xx am x-Link = E_xx(n + x) - E_xx(n); d_y E_yx am x-Link = E_xy(n) - E_xy(n - y)).
  - Fourier-Symbol mit der physikalischen Fouriertransformierten (Ort n + delta): i k_i, k_i = 2 sin(q_i/2), wie die
    Karte verlangt.
  - Begruendung: Nur diese Staffelung erfuellt Symmetrie, Spurfreiheit (alle Diagonalen am selben Ort) und das
    Symbol 2 sin(q/2) zugleich exakt. Eine reine Vorwaertsdifferenz auf ungestaffeltem Gitter gibt den Diagonalen
    verschiedene Phasen und zerstoert die ortsgleiche Spurbedingung; die symmetrische Differenz (Symbol sin q) haette
    Nullstellen bei q = pi (Verdopplung).
- **Unbekannte [A]:** Koeffizienten in einer Orthonormalbasis (Frobenius) der symmetrischen spurfreien Tensoren
  (5 Freiheitsgrade: (xy+yx)/sqrt2, (yz+zy)/sqrt2, (zx+xz)/sqrt2, (xx-yy)/sqrt2, (xx+yy-2zz)/sqrt6).
  - Kleinste Koeffizientennorm = kleinste Frobeniusnorm sum_ij E_ij^2.
  - Energie F = (K/2) sum_n sum_ij E_ij^2 (Nebendiagonale doppelt gezaehlt), K = 1, |p| = 1, Ladung 1.
- **Loesung je q:** lineares System A(q) e = rho(q) (Vektor: 3 x 5, A = i Bm, Bm_ja = sum_i k_i B_a,ij);
  e = pinv(A) rho mit numpy.linalg.pinv (SVD). Skalar: 1 x 6 (ohne Spurbedingung) bzw. 1 x 5 (spurfrei), Zeile
  -sum_ij k_i k_j B_a,ij.
  - Danach inverse FFT je Komponente mit Phasen exp(i q.delta) in den Ortsraum, F im Ortsraum summiert.
- **Kontrolle der Spurfreiheit:** Die 5er-Basis ist spurfrei per Konstruktion (Pruefung dort trivial, offengelegt).
  Nichttrivial: Kontrollvariante mit 6 symmetrischen Freiheitsgraden plus Spur als vierte Gleichungszeile
  (pinv eines 4 x 6-Systems) fuer 6 Paare; Spur und Abstand zur 5er-Loesung werden gemessen.
- **Neutralitaet [A]:** q = 0 wird nicht geloest (pinv der Nullmatrix ist 0). Das ist gleichbedeutend mit einem
  gleichfoermigen Neutralisierungshintergrund -sum(Ladung)/N, fuer Einzelladung und Paar gleich behandelt.
  Das Gauss-Gesetz wird gegen rho - Mittelwert geprueft.
- **Ladungsdarstellung [A]:** Punktladungen auf genau einem Link (Vektor) bzw. Knoten (Skalar), keine Glaettung.
- **Wechselwirkung:** U = F(Paar) - F(einzeln, 1) - F(einzeln, 2), alle drei auf demselben Torus und mit derselben
  q = 0-Behandlung.
- **Kreuzprobe Kernweg:** Gleiche pinv, aber U ueber Parseval als inverse FFT von (pinv Bm)^T pinv Bm; muss mit dem
  Ortsraumweg auf L = 32 und 64 uebereinstimmen. Fuer L = 128, 192, 256 nur Kernweg (halbes Gitter, irfftn).

## 2. Konfigurationen und Gittergroessen

- **Gitter:** L = 64 (Haupt, Ortsraumweg), L = 32 (Kontrolle, Ortsraumweg).
  - [A] Zusaetzlich L = 128, 192, 256 nur fuer die Endlichkeitskorrektur (Kernweg).
- **Parallele Vektorladungen:** p = z bei Link (0,0,0)+z/2 und bei v + z/2.
  - Richtungen (15): (0,0,1), (1,0,4), (1,0,3), (1,0,2), (1,1,2), (1,0,1), (1,1,1), (2,0,1), (2,1,1), (2,2,1), (3,0,1),
    (4,0,1), (1,0,0), (1,1,0), (2,1,0). Theta = Winkel zwischen p und r von 0 bis 90 Grad, 13 verschiedene Werte.
  - Fuer r = 2, 3, ..., 16 je Richtung v = rint(r * Richtung) mit 1,5 <= |v| <= 16,5; Duplikate entfernt:
    189 Vektoren.
  - Verglichen wird immer am tatsaechlichen v (|v| und Winkel des Gittervektors).
- **Antiparallele Vektorladungen:** 11 Vektoren auf den Achsen und der Raumdiagonale.
- **Senkrechte Vektorladungen:** p1 = z, p2 = x; 18 Paare, tatsaechlicher Abstand s = v + (1/2, 0, -1/2).
- **Skalarladungen:** gleich (+1, +1) und ungleich (+1, -1).
  - Ortsraumweg mit 6 Freiheitsgraden (ohne Spurbedingung).
  - Abstandsvektoren (m,0,0) fuer m = 1 bis 16, (m,m,0) fuer m = 1 bis 11, (m,m,m) fuer m = 1 bis 9.
  - Spurfreie Variante (5 Freiheitsgrade) fuer 6 Vektoren als Formfaktorprobe.
- **Pinch-Punkte:**
  - Transversalprojektor P_T = 1 - pinv(Bm) Bm in der 5er-Basis; <E_xy E_xy> = P_T[xy,xy]/2.
  - Karten: Ebenen [hk0] (q_z = 0) und [0kl] (q_x = 0), q von -2 pi bis 2 pi, 401 x 401 Punkte.
  - Winkelprofile auf Kreisen eps = 0,02, 0,05 und 0,1 um q = 0, mit 720 Winkeln.

## 3. Laeufe (alle ueber kleintest.sh auf der .69)

- R1 explizit (Spur cpu): L = 32 und 64, alle Konfigurationen. Rauchzeit: 0,24 s je Vektorpaar bei L = 64,
  also etwa 1,5 min.
- R2 kern-a (Spur cpu): L = 32, 64, 128.
- R3 kern-b (Spur cpu oder p4000a, nur CPU-numpy): L = 192, 256. Rauchzeit fuer L = 64 1,8 s, hochgerechnet etwa
  2 bis 3 min fuer L = 256.
- R4 pinch (Spur cpu). R5 Auswertung (Spur cpu): te0_auswertung.py --lauf lauf.
- Hoechstens zwei Laeufe zugleich.

## 4. Vorab-Ueberlegung des Agenten zur Torusgroesse [A], vor jeder Hauptrechnung

- Auf dem Torus mit ausgelassenem q = 0 enthaelt U zusaetzlich zum Kontinuumsterm einen Hintergrundbeitrag.
  - Fuer den Coulomb-Teil gilt [L]: G_L(r) = 1/(4 pi r) + xi/(4 pi L) + r^2/(6 L^3) + ..., mit der Ewald-Konstante
    xi = -2,837297 fuer das einfach kubische Gitter.
  - Fuer den Kern der Karte folgt daraus (eigene Rechnung, ueber d_i d_j des biharmonischen Torus-Kerns):
    - parallele Ladungen: U_L - U_unendlich = (2 K p^2/(4 pi)) (11/12) xi / L + O(r^2/L^3)
    - Wert bei L = 64: -0,00647 K p^2
    - Das ist 19 % des Kontinuumswerts bei r = 4 (theta = 90 Grad) und 74 % bei r = 16. Die Verschiebung ist
      isotrop, kuerzt sich im Verhaeltnis von T2 also nicht heraus.
  - Fuer ungleiche Skalarladungen (6 Freiheitsgrade): U_L = r/(8 pi) + (xi/(24 pi L)) r^2 + r^4/(120 L^3) + ... + const.
    - Der r^2-Term ist keine Konstante; U(r) - U(4) entfernt ihn nicht.
- **Folge:** Woertlich auf L = 64 (Rohwerte) werden T0, T2 und T3 voraussichtlich nicht eintreffen. Der Grund ist
  dann der Torushintergrund, nicht die Kontinuumsformel. Die Karte nennt fuer T0 ausdruecklich L = 64 und regelt den
  Hintergrund nicht.
- Deshalb werden zwei Ebenen vorab festgelegt:
  1. **Urteile T0 bis T4 woertlich** nach der Karte (L = 64, Rohwerte, q = 0 ausgelassen). Diese Urteile kommen in
     auswertung.json unter "urteile".
  2. **Zusatz [A], ebenfalls vorab fest:** Z0 bis Z3 pruefen dieselben Aussagen mit denselben Schwellen an
     endlichkeitskorrigierten Werten.
     - U_FS(v) aus L = 128, 192, 256 durch exakte Loesung von U_L = a + b/L + c/L^3, U_FS = a.
     - Unsicherheit: Abstand zur gleichen Anpassung mit L = 64, 128, 256.
     - Die Zusatzwerte kommen unter "zusatz". Sie ersetzen kein woertliches Urteil.

## 5. Urteilsregeln (eingefroren)

- Kontinuumsformeln der Karte, erst in der Auswertung benutzt (K = p = 1):
  - U_par(r, theta) = (2/(4 pi r)) (7/8 + cos^2 theta/8)
  - U_senk = (2/(4 pi |s|)) (1/8)(s_z s_x/|s|^2) (nur Zusatz)
  - Skalar: Steigung 1/(8 pi) (6 Freiheitsgrade)
- **T0 (woertlich):** eingetroffen genau dann, wenn (a) und (b) gelten.
  - (a) Gauss-Gesetz: max |Gitterdivergenz - (rho - Mittel)| <= 1e-10 (relativ zu max |rho| = 1) ueber alle
    Ortsraumloesungen auf L = 32 und 64, Vektor und Skalar.
  - (a) Spurfreiheit: max |Spur| / max |E| <= 1e-10, und zwar fuer:
    - alle 5er-Loesungen (trivial, offengelegt)
    - die 6er-Kontrolle mit Spurzeile (nichttrivial)
    - nicht fuer die Skalarloesung mit 6 Freiheitsgraden, die bewusst keine Spurbedingung hat [A]
  - (b) Parallele Vektorladungen auf L = 64, Rohwerte, alle v mit |v| >= 4: max |U/U_par - 1| <= 0,03.
    - [A] Die "Kontinuumsformel" der Karte ist die Vektorformel; der Skalarfall steckt in T3.
- **T1 (woertlich):** eingetroffen, wenn U > 0 fuer alle 2 <= |v| <= 16 der Parallelliste auf L = 64 (Rohwerte).
- **T2 (woertlich):** R = U(0,0,8)/U(8,0,0) auf L = 64 (Rohwerte); eingetroffen, wenn |R/(8/7) - 1| <= 0,03.
- **T3 (woertlich):** ungleiche Skalarladungen, 6 Freiheitsgrade, L = 64 (Rohwerte), D(v) = U(v) - U((4,0,0)).
  - Je Richtung (100), (110) und (111) [A]:
    - s_a = Steigung der Ausgleichsgeraden D gegen |v| fuer 8 <= |v| <= 12
    - s_b = dasselbe fuer 12 <= |v| <= 16,5
  - Eingetroffen, wenn fuer alle drei Richtungen gilt:
    - |s_b/s_a - 1| < 0,10
    - D steigt laengs der Richtung ab |v| >= 4 streng ("waechst").
- **T4:** <E_xy E_xy> aus dem numerischen Projektor.
  - Auf jedem Kreis werden gezaehlt:
    - Keulen: lokale Maxima >= 0,5 x Maximum
    - Nullstellen: lokale Minima <= 0,01 x Maximum
  - Eingetroffen, wenn alle drei Bedingungen gelten:
    - [hk0] ergibt auf allen drei Kreisen (4 Keulen, 4 Nullstellen), also vierzaehlig.
    - [0kl] ergibt auf allen drei Kreisen (2, 2), also zweizaehlig.
    - In beiden Ebenen ist max |C(eps = 0,02) - C(eps = 0,1)| <= 0,05 x Maximum: die Richtungsabhaengigkeit haengt
      nicht vom Betrag ab (Pinch-Punkt statt glatter Funktion).
  - Bildvergleich mit Fig. 1b/c von Yan u. a. zusaetzlich in ERGEBNIS.md, beschreibend; die Zaehlung entscheidet [A].
  - Abstand zu Gl. 17 [S] wird berichtet, ist aber kein Kriterium.
- **Z0 bis Z3 [A]:** wie T0(b), T1, T2 und T3, aber mit U_FS bzw. D_FS (D je L gebildet, dann angepasst).
  Schwellen unveraendert. Z0 verlangt zusaetzlich T0(a).
- "nicht auswertbar" nur, wenn ein Lauf fehlt oder abbricht.

## 6. Agenten-Vorhersagen [A] (vorab, nur zur Pruefung meiner Torus-Ueberlegung, keine Kartenvorhersagen)

| Nr | Vorhersage | Urteilsregel |
|---|---|---|
| A1 | Roh-L64 minus U_FS liegt fuer alle Parallelvektoren 4 <= \|v\| <= 16 nahe -0,00647 | alle Werte in [1,15; 0,85] x (-0,006468) |
| A2 | 1/L-Koeffizient b der Anpassung ist richtungs- und abstandsunabhaengig, b = (2/(4 pi))(11/12) xi = -0,4139 | alle \|b/b_soll - 1\| <= 0,10 fuer \|v\| >= 4 |
| A3 | T3 woertlich auf L = 64: Steigungsverhaeltnis laengs (100) etwa 0,84 | Verhaeltnis in [0,75; 0,92] |
| A4 | Auf L = 32 wird U parallel bei v = (16,0,0) negativ (Scheinanziehung durch den Torus) | U < 0 |

## 7. Rauchlaeufe vor dem Einfrieren (offengelegt)

- **rauch1** (19:53 UTC, L = 12, wenige Paare):
  - Kontrollen: Gauss-Rest <= 4e-16, Spur 5er 3e-17, 6er mit Spurzeile 6e-17, Abstand der 5er- zur 6er-Loesung
    4e-17, Parseval 3e-16 relativ, Kernweg gegen Ortsraumweg 1,4e-16, Imaginaerteile <= 2e-17.
  - Skalar 5er/6er = 1,5000.
  - Die U-Werte auf L = 12 sind vom Torus beherrscht und nicht urteilsrelevant. Beispiele: U(0,0,2) = 0,0533,
    U(2,0,0) = 0,0407.
  - Zeiten: siehe Abschnitt 3.
- Gefundene Codefehler vor dem Einfrieren, behoben:
  1. Die q = 0-Kennzahl schloss die Spurzeile der 6er-Kontrolle ein (Wert 1/3, kein Rechenfehler: deren rechte
     Seite ist 0). Sie prueft jetzt nur die Gauss-Spalten.
  2. Die Spurpruefung der Auswertung haette die bewusst spurbehaftete Skalar-6er-Einzelladung mitgezaehlt.
  3. irfftn mit expliziten Achsen (Warnung von numpy 2.x).
  4. "steigt" in T3 nur laengs jeder Richtung, nicht gegen den Achsenwert U(4,0,0) quer zur Richtung.
- **rauch2** (19:57 UTC; Kette mit L = 16/24, Anpassung 32/48/64): prueft nur, dass Rechnung, Auswertung und Bilder
  durchlaufen.
  - Die Zahlen sind ohne Bedeutung fuer die Urteile.
  - Die T4-Profile werden dort mitgerechnet (deterministisch, identisch zum Hauptlauf), vor dem Einfrieren aber nicht
    angesehen.
  - Weitere Codefehler, behoben:
    1. Klammerfehler in der Bildzeile.
    2. numpy-bool nicht JSON-faehig.
    3. Die Parseval-Kennzahl war relativ zu F. Bei L = 16 faellt v = (16,0,0) auf den Startpunkt, +1 und -1 heben sich
       auf (F ~ 1e-31) und die Kennzahl wird sinnlos (0,12). Nenner jetzt mindestens 1e-12. Keine Urteilsgroesse.
  - **Gesehen und offengelegt:**
    - Kontrollen der Probe: Gauss-Rest 2e-15, Spur 3e-16, Kernweg gegen Ortsraumweg 5e-16, pinv bei q = 0 genau 0.
    - Bild bild-U-theta.png der Probe (Beschriftung "L = 64" stammt dort aus der festen Bildzeile, gezeigt ist L = 24):
      - Die Rohwerte von L = 24 liegen weit unter der Kontinuumskurve, bei grossem r bis ins Negative.
      - Die mit 32/48/64 korrigierten Werte liegen nahe an der Kurve.
    - Das entspricht der Vorab-Ueberlegung in Abschnitt 4. Schwellen und Regeln wurden danach nicht geaendert; die
      Abschnitte 4 bis 6 standen vor rauch2 fest.
