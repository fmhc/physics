Gesamturteil: haelt mit Einschraenkung. 2 A-Befunde (A1 "nur am Rand", A2 DT3-Etikett), 11 B-Befunde.

- Frage 1: haelt
- Frage 2: haelt mit Einschraenkung
- Frage 3: haelt
- Frage 4: haelt mit Einschraenkung
- Frage 5: haelt mit Einschraenkung

# WINDUNG-LESER: Gegenlesen DREIECK-TAKT-1 (Runde 42)

- Leser: pruefer-opus (frischer Agent, kein Fork), Auftrag RUNDE-37/windung-leser/KARTE.md
- Beginn: 2026-10-04 17:33:16 CEST (date). Text abgeschlossen: 2026-10-04 17:55:45 CEST (date), also 22 min 29 s.
- Zeitbox: 60 min
- Arbeitsweise: nur Lesen und Papier; keine Laeufe; hoechstens 2 arXiv-Abrufe fuer Frage 1

## Gelesene Unterlagen

- RUNDE-37/windung-leser/KARTE.md (ganz).
- RUNDE-37/qca-windung-1/KARTE-2-DREIECK-TAKT.md (ganz).
- teil2-dreieck-takt/PLAN.md (ganz). Per cmp und sha256 identisch mit PLAN.md.eingefroren-20261004-170038
  (0bf35666...68f8bf8d). Ebenso sind teil2.py, windung.py und auswertung2.py identisch mit ihren eingefrorenen Kopien.
  diag_rand.py ist nach dem Einfrieren entstanden, wie angezeigt.
- teil2-dreieck-takt/ERGEBNIS.md (ganz).
- teil2-dreieck-takt/code/teil2.py: Zeilen 20 bis 160 und 415 bis 503 (Automaten, w3_box, P3, LM).
- windung.py: Klasse Grad1.
- lauf-69/auswertung2.json und p3.json per jq (vorbedingungen, urteile, vermerke, kennzahlen, higashikawa, takt).
- Quellen, gelesen per pdftotext:
  - Higashikawa u. a. 1806.06868v2: S. 1 bis 3 und Anhang D, Ausschnitte.
  - Bessho/Sato 2006.04204v3 (Teil-1-Ordner): Gl. (11), S124 und S108 bis S113.
  - Kitagawa u. a. 1010.6126 (Teil-2-Ordner): S. 8, Grenzfall des vollen Uebertrags, und die Bildunterschrift von
    Fig. 6.
- RUNDE-37/qca-windung-1/ERGEBNIS.md (Teil 1, ganz).
- RUNDE-42.md, Zeilen 221 bis 264 (Ernte DREIECK-TAKT-1).
- **Abrufe, 2 von 2, nur fuer Frage 1:**
  1. arXiv-Abstract 1608.04696 (N. Read, "Compactly-supported Wannier functions and algebraic K-theory", PRB 95,
     115309 (2017)).
  2. Volltext-PDF davon, lokal als quellen/read-1608.04696.pdf (sha256 68e5d0c9...c1cf5ee77, 29 S.); gelesen per
     pdftotext: Abschn. IV, Seiten um Gl. (39).
- Nicht geoeffnet: Ordner anderer Pruefer, versiegelte Dateien, Datendateien.

## Frage 1: K-Theorie-Argument

**Urteil: haelt.**
- T2 ist richtig.
- Der Uebergang von der Algebra zu W3 ist lueckenlos; ein eigenes unitaeres Argument ist nicht noetig.
- Der Satz steht in der Literatur: Read 2017, Abschn. IV.
- Nur Kennzeichnung und Geltungsbereich sind nachzuziehen (B1, B2).

Pruefung Schritt fuer Schritt (PLAN.md Abschn. 1 T2; ERGEBNIS.md Abschn. Schreibtisch):

1. **Unitaer und Laurent, also invertierbar ueber dem Ring.** Mit U(z) = Sum A_f z^f ist U^-1 = U^dag = Sum A_f^dag z^-f
   wieder ein Laurent-Polynom. U U^dag = I gilt auf dem Torus; der Torus ist Zariski-dicht in (C^*)^3, also gilt es
   auch als Polynomidentitaet. Damit liegt U in GL_N(R) mit R = C[z1^+-1, z2^+-1, z3^+-1]. det U ist eine Einheit
   von R, also c z^m. Richtig.
2. **SK_1(R) = 0.** Bass/Heller/Swan gilt fuer regulaere A: K_1(A[t, t^-1]) = K_1(A) + K_0(A).
   - Dreimal angewandt, jeweils mit K_0 = Z, ergibt das K_1(R) = C^x + 3 Z = R^x.
   - det ist die Identifikation, weil die Z-Summanden von den z_j selbst erzeugt werden.
   - [S] Read 2017, Abschn. IV, Gl. (39): "K1(R1^(d)) = C× ⊕ d.Z", gewonnen aus "the 'fundamental theorem' proved by
     Bass, Heller, and Swan"; "Because a Laurent polynomial ring is itself right regular, the result can be applied
     iteratively".
   - Suslins Satz (SL_n = E_n fuer n >= 3 ueber Laurent-Ringen, 1977) [L] wuerde die Stabilisierung sparen; noetig ist
     er nicht.
3. **Von der Algebra zur Topologie.** Es gilt U + I_m = diag(det U, 1, ...) E mit E = Prod e_ij(p).
   - Ersetzt man jedes p durch t p, ist H_t(k) fuer jedes t und k invertierbar (unipotente Faktoren) und polynomial
     in (t, k). Das ist eine glatte Homotopie von Abbildungen T^3 -> GL_{N+m}(C).
   - W3 ist fuer GL-wertige Abbildungen mit derselben Formel definiert. Die Form tr(g^-1 dg)^3 ist auf GL(N, C)
     geschlossen (d tr th^3 = -tr th^4 = 0), also ist W3 nach Stokes homotopieinvariant.
   - Die Polarzerlegung g -> g (g^dag g)^-1/2 zieht GL auf U(N) zurueck. Der Wert ist also die ganze Zahl der
     unitaeren Abbildung, und eine unitaere Homotopie entsteht punktweise. Gebraucht wird sie nicht.
   - W3(U + I_m) = W3(U), weil die Spur zerfaellt. W3(diag(f, 1, ...)) = 0, weil (f^-1 df)^3 fuer eine skalare 1-Form
     verschwindet. Also ist W3(U) = 0.
   - Read 2017 geht denselben Weg ueber den Ringwechsel R -> C(T^d) und Milnor [S, Abschn. IV]: "the
     polynomially-generated vector bundles with an automorphism are classified up to homotopy by π0 K1(Ri) above, and
     do not yield any nonzero element of SK1(Ci)".
   - Ein unitaeres Laurent-U ist genau ein solcher Automorphismus (Klasse AIII). Abstract [S]: Es bleibt "in each of d
     directions, the non-trivial winding that can occur in the same symmetry class in one dimension, but nothing
     else". Das ist T2 fuer d = 3.
4. **Wo die Unitaritaet eingeht: Gegenfaelle, die den Satz scharf abgrenzen.**
   - Unitaritaet wird nur in Schritt 1 gebraucht (U^-1 ist Laurent). Ohne sie faellt der Satz. Beispiel [S, Teil-1-Quelle]:
     Bessho/Sato, Supplement Gl. (S108) bis (S113), ein endlichreichweitiges nicht-hermitesches Gittermodell
     (sin k_i, cos k_i) mit Punktluecke: "w3 = 1 for d0 = γ = γ0 = 1 and m0 = −2". H - E_F ist dort punktweise
     invertierbar, die Inverse aber kein Laurent-Polynom.
   - Dasselbe steckt in der Grad-1-Kontrolle aus Teil 1 (windung.py, Klasse Grad1):
     - D(k) = d4 I + i d.sigma mit d = (sin u, 2 - Sum cos u) ist endlichreichweitig, und W3(D) = W3(U) = -1.
     - U = D/|d| ist unitaer, wegen 1/|d| aber nicht endlichreichweitig: reell-analytisch, also mit exponentiell
       abfallenden Schwaenzen [M, Leser].
     - Von den drei Eigenschaften "endliche Reichweite", "unitaer" und "W3 ungleich 0" bekommt man je zwei, nie alle
       drei.
5. **Gegenbeispiele in der Literatur:** keine, und nach dem Satz kann es keine geben. Die bekannten W3-Beispiele umgehen
   je eine Voraussetzung:
   - Higashikawa u. a.: Halbschritte U_3(k3/2), dazu ein Unterraum.
   - Bessho/Sato S124: 2D-AIII-Lauf, ebenfalls mit U_y(k_y/2).
   - Bessho/Sato Gl. (11) und (S108): nicht-hermitesch.

   Der 1D-Index (Gross/Nesme/Vogts/Werner) [L] ist der Fall d = 1 (det-Windung) und passt dazu.
6. **Geltungsbereich.** Voraussetzungen des Satzes:
   - freie Teilchen, unitaer;
   - translationsinvariant mit endlicher Zelle; jede Basis ist erlaubt, auch FCC mit 4 Plaetzen oder ein
     Halbschritt-Gitter als feineres Bravais-Gitter;
   - endliche Reichweite.

   "Netto-Haendigkeit" heisst dabei Haendigkeit im Volumen. Nach Bessho/Sato, Theorem 3' (Teil 1 [S]), ist die Ladung
   bei jeder Quasienergie gleich der Volumenzahl; bei W3 = 0 ist sie also ueberall null.

   Nicht abgedeckt sind:
   - Wechselwirkung (QCA im Vielteilchensinn);
   - fehlende Translationsinvarianz;
   - Raender;
   - nicht-unitaere Schritte;
   - quasilokale Schritte.

## Frage 2: Numerik

**Urteil: haelt mit Einschraenkung.**
- Die W3-Integration ist ausreichend geprueft.
- Als Stichprobe traegt die Rechnung die Allaussage nicht; das muss sie auch nicht, die Allaussage traegt der Satz aus
  Frage 1.
- Die Formel "an 104 Automaten bestaetigt" ueberzeichnet aber das Gewicht (B3).

**Integration (ausreichend geprueft):**
- **Exaktheit:** X_j = U^dag d_j U hat je Richtung Frequenzen bis 2M, der Integrand tr(X1 [X2, X3]) also bis 6M. Die
  Rechteckregel mit N Punkten ist exakt fuer abs(n) < N. Damit genuegt N_exakt = 6M + 1 (teil2.py, n_exakt). Die Daten
  passen dazu (p3.json): Produkte 13/19/25, Takte 7, Higashikawa 13.
- **Normierung:** w3_box und W1.w3_integral rechnen (1/8 pi^2) Int tr(X1 [X2, X3]). Wegen
  eps^ijk tr(X_i X_j X_k) = 3 tr(X1 [X2, X3]) ist das gleich (1/24 pi^2) Int eps tr(XXX). Richtig.
- **Positivkontrollen im selben Integrator wie die 104 Automaten** (w3_satz -> W1.w3_integral):
  - Teil 2, Additivitaet (auswertung2.json, vermerke.DT0.additivitaet): S1*R und R*S1 in vier Proben zwischen
    -0,99999999999997 und -0,99999999999996, also hoechstens 4,1e-14 neben -1; R allein <= 1,04e-15.
  - Teil 1: K-S1 = -1, K-S1m = +1, K-S1q = -2.
- **Zwei Integratoren gegeneinander (Higashikawa):**
  - Halbboxen mit w3_box: Abweichung von 1 bei N = 16, 32, 48, 64: 1,64e-5; 1,02e-6; 2,01e-7; 6,35e-8.
  - Die Quotienten 16,1; 5,07; 3,16 entsprechen genau N^-4: 2^4 = 16, (3/2)^4 = 5,06, (4/3)^4 = 3,16.
  - Der ganze Torus mit w3_satz gibt 3,7e-16, also die Summe der beiden Halbboxen. Damit sind Integrator und Gebiet
    gegeneinander geprueft.
- **Grenze der Pruefung:** Eine Positivkontrolle "endlichreichweitig mit W3 ungleich 0" kann es nicht geben
  (Frage 1). Die Halbzone, ein Laurent-Polynom in halben Frequenzen auf halber Periode, kommt dem am naechsten, und
  sie ist gerechnet.
- Die Unitaritaet der LM-Treffer (<= 2,3e-12) ist unkritisch, weil W3 auf GL homotopieinvariant ist.

**Stichprobe (traegt die Allaussage nicht, muss es nicht):**
- 79 der 104 Faelle waren schon vor der Rechnung durch einfachere Argumente festgelegt:
  - **T1 (Produkte aus Teilverschiebungen und Muenzen):** die 72 Zufallsprodukte und das Higashikawa-Modell auf dem
    ganzen feinen Torus.
  - **T3, ohne jede Reichweitenbedingung:** die 6 Pyrochlor-Takte. Jeder Schritt ist exp(-i theta (hop + h.c.))
    (teil2.py, bindungsschritt), also eine Hamilton-Entwicklung; theta -> 0 verbindet den Takt stetig mit der Eins.
    Bei theta = pi/2 hat der Takt nur 4 Frequenzen (p3.json, nfreq).
- Unabhaengig von T1 und T3 sind nur die 25 LM-Treffer:
  - N = 2: 23 Treffer aus 40 Starts;
  - N = 3: 2 Treffer aus 3 statt 30 Starts (Selbstanzeige 9);
  - Traeger F15, Frequenzen <= 1.

  Dass sie keine Produkte sind, ist nicht gezeigt ("kein offensichtliches Produkt").
- **Folge fuer Finns 3D-Bild (staerker als behauptet):** Ein Takt aus Bindungsdrehungen hat W3 = 0, auch bei
  unendlicher Reichweite (T3). Der Satz aus Frage 1 wird dafuer nicht einmal gebraucht.

**Wortlaut-Vorschlag** fuer ERGEBNIS Punkt 2 und RUNDE-42, Ernte Punkt 2, statt "an 104 Automaten bestaetigt":
"Die Rechnung ist eine Kontrolle: alle 104 Automaten haben abs(W3) <= 5,3e-15. 79 davon sind schon nach T1 bzw. T3
null; die 25 allgemeinen Suchtreffer sind die einzigen ohne vorgegebene Produktform. Positivkontrollen im selben
Integrator ergeben -1."

## Frage 3: Literaturmodell

**Urteil: haelt.**
- Die Lesart ist richtig.
- Sie ist allerdings die eigene Konstruktion der Quelle und keine Korrektur an ihr. So sollte sie auch formuliert sein
  (B5).

- **Quelle [S, pdftotext S. 2]:**
  - Gesamtoperator: "the total time-evolution operator U_F^wh for the whole four bands over one cycle".
  - Zerlegung: "V^wh(k) is decomposed into two 2×2 matrices: V^wh(k) = U(k) ⊕ U^H(k)", mit "U^H(k) := U(k1, k2, k3 − 2π)".
  - Auswahl: "Here we focus on U(k) as a Floquet operator of lower Floquet bands".
  - Gl. (6), W = 1, bezieht sich auf U(k). Fuer V^wh behauptet die Quelle nirgends W = 1.
- **Ganzer Automat:** Es gilt W(V^wh) = W(U) + W(U^H).
  - V^wh ist auf L_C endlichreichweitig: ein Produkt aus Teilverschiebungen auf dem feinen Gitter. Also ist
    W(V^wh) = 0 nach T1 und ebenso nach T2. Daraus folgt W(U^H) = -1.
  - Die Rechnung passt: Halbboxen W3 = -/+0,99999994 bei N = 64, ganzer feiner Torus 3,7e-16.
- **Nachbau:** Die Vorzeichenberichtigung des Agenten (e^{-+ik} statt des gedruckten "U_j^±(k) := P_j^± e^{−ik} + P_j^∓")
  ist richtig.
  - Eq. (2) und die Entwicklung "U_j^±(k) ≈ σ0 ∓ iP_j^± k" (S. 2) verlangen sie.
  - Woertlich gelesen gaebe die Entwicklung U ≈ σ0 - i(k1 + k2 + k3) σ0, also keinen Weyl-Kegel [M, Leser].
  - Bessho/Sato schreiben dieselben Pumpen als "Uj±(kj) = Pj± e∓ikj + Pj∓" (Supplement bei Gl. S124) [S].
  - Quasienergieformel auf 5,55e-16 getroffen, Randwert -sigma_0 auf 6,7e-16 (p3.json, auswertung2.json).
  - Probe des Lesers [M]: Bei k1 = k2 = 0 ist U = (U_3^- U_3^+)^2 = exp(-i k3 sigma_3). Das ist sigma_0 bei k3 = 0 und
    k3 = 2 pi und -sigma_0 bei k3 = +-pi, wie im ERGEBNIS.
- **Ergaenzung zur Lesart [S, S. 3 und Anhang D]:**
  - Die "lower Floquet bands" sind die Bloch-Zustaende des feinen Gitters mit abs(q3) < pi.
  - Der Anfangszustand kommt aus H0 mit eps0(q) = -t3 cos(q3/2) - t1 cos q1 - t2 cos q2, q in [-pi, pi]^2 x [-2pi, 2pi]:
    "In the limit t1, t2 ≪ t3, only the lower Floquet bands are occupied".
  - Anhang D: Mit Fluss "breaks the periodic boundary condition along the k3 direction, i.e., U′(k2, π) ≠ U′(k2, −π),
    due to the coupling between the lower and higher Floquet bands"; dafuer kommt ein Zusatzschritt U_s hinzu.
- **Folgerungen [M, Leser]:**
  - Beide Bloecke haben dasselbe Quasienergiespektrum: cos eps = 2 cos^2(k1/2) cos^2(k2/2) cos^2(k3/2) - 1 bleibt unter
    k3 -> k3 - 2 pi gleich. Getrennt sind sie durch ein Impulsfenster, nicht durch eine Quasienergie-Luecke.
  - In der Zone der Quelle sitzt der Partner bei k = 0 im oberen Block, ebenfalls bei Quasienergie 0. Das ganze
    Modell hat dort einen vierfachen Punkt: zwei Weyl-Punkte entgegengesetzter Chiralitaet am selben Ort.
    "k3 = 2 pi" im ERGEBNIS meint den feinen Torus; das sollte dabeistehen.
  - Der U-Block ist auf dem groben Torus stetig (U = -sigma_0 am Rand), aber kein Laurent-Polynom in e^{ik3}. Waere er
    eines, gaebe T2 W = 0. Er hat also unendliche Fourier-Schwaenze; wie schnell sie abfallen, habe ich nicht bestimmt.
  - Das ungepaarte Weyl-Teilchen haengt an der exakten Halbschritt-Translation bzw. an der Besetzung nur des
    unteren Fensters. Das stuetzt den Satz des Agenten: "Der Ort der Anomalie ist hier der abgetrennte obere
    Bandraum".
- **Vorzeichen:** Es gilt W = -W3.
  - ERGEBNIS Punkt 3 wechselt die Konvention zwischen zwei Saetzen ("W = 1 (W3 = -1) ... Die andere Haelfte hat +1",
    gemeint W3).
  - RUNDE-42 bleibt bei W ("die andere Haelfte hat -1").
  - Beides ist richtig, aber leicht falsch zu lesen (B5).

## Frage 4: 2D-Teil

**Urteil: haelt mit Einschraenkung.**
- Der Inhalt haelt: einseitige Randwelle, deren Richtung der Drehsinn festlegt.
- Das Zaehlverfahren ist nicht validiert.
- Das Urteilsetikett "nach Kartenwortlaut eingetroffen" ist nachtraeglich gelockert (A2).

**Was den Inhalt traegt (unabhaengig vom Zaehlfehler):**
1. **Quelle [S, Kitagawa u. a. 2010, S. 8, lokal per pdftotext gelesen]:** Grenzfall des vollen Uebertrags:
   - "a particle starting at any site in the bulk comes back to the starting site after two complete driving periods";
   - "a particle which starts at the upper (lower) edge on sublattice B (A) propagates unidirectionally along the edge
     to the left (right)";
   - die eingeschraenkten Floquet-Operatoren "yield ν1 = 1(−1)".
2. **Volumen-Rand-Probe an den eingefrorenen Zahlen [M, Leser]:** Fuer jedes Band gilt C = W(Luecke darueber) -
   W(Luecke darunter) (anomale Floquet-Phasen, Rudner u. a. 2013 [L]). Die Oberrand-Zahlen des Hauptlaufs passen in
   allen drei Protokollen zu den getrennt gerechneten Chern-Zahlen:
   - voll: W(0) = W(pi) = -1, also C = 0, 0;
   - lam3: W(0) = -1, W(pi) = 0, also C = +1 und -1;
   - lam4: W(0) = W(pi) = -1, also C = 0, 0.

   Die Fehler liegen nur am unteren Rand: voll, pi-Luecke +2; lam4, Luecke 0: 0.
3. **Summenregel:** Die Schritte haben spurfreie Erzeuger, also gilt det U = 1, und der Netto-Durchgang durch jede
   Quasienergie ist 0. Das Argument des Agenten ist richtig, und die Zelle (-1, +2, 0) ist damit sicher falsch gezaehlt.
4. **Nachzaehlung nach dem Einfrieren** (diag_rand.json): in beiden Luecken (-1, +1, 0), umgekehrt (+1, -1, 0). Sie
   ist Diagnose und stuetzt nur.
5. **Richtungsumkehr:** Sie ist durch Symmetrie erzwungen und kein eigener dynamischer Befund.
   - Bei reellen Spruengen ist die umgekehrte Folge U_rev = K U^-1 K (ERGEBNIS, Zeitumkehr [M]; vom Leser
     nachvollzogen).
   - Ist U psi_k = e^{-i eps} psi_k, dann ist U_rev (K psi_k) = e^{-i eps} K psi_k bei -k. Die Gruppengeschwindigkeit
     wechselt also das Vorzeichen, der Rand bleibt derselbe.
   - Die Vorhersage konnte an dieser Stelle nicht scheitern. Als Code-Probe taugt sie, und sie stimmt in allen Zellen.

**Einschraenkungen:**
- **Zaehlverfahren nicht validiert:**
  - Im Hauptlauf verletzen 3 von 12 Zellen die Summenregel.
  - In der Nachzaehlung bleibt lam4 1-2-3, Luecke 0 bei (-1, 0, 0); die Ursache ist ungeklaert.
  - Die Fehler sitzen beide Male am unteren Rand.
  - Randzahlen aus diesem Zaehler sind nur zusammen mit Summenprobe und Volumen-Rand-Probe verwendbar.
- **Etikett:** PLAN Abschn. 4 hatte vor der Rechnung festgelegt: "Kartenwortlaut: DT0 bis DT3 wie oben". Das Urteil
  "nach Kartenwortlaut eingetroffen" erweitert die Akzeptanzmenge nach dem Ergebnis von "beide Luecken" auf "eine
  Luecke". Es ist deshalb Diagnose, kein Urteil (A2). Der Agent hat das selbst angezeigt (Selbstanzeige 10); in die
  Ernte ist es ohne diesen Vorbehalt gelangt.
- **Finns "Dreieck" im Modell:**
  - Gerechnet ist der Umlauf der drei Bindungsrichtungen des Wabengitters, b1 bei 120, b2 bei 240, b3 bei 0 Grad.
  - Im Volumen laeuft ein Teilchen bei vollem Uebertrag mit den Versaetzen +b1, -b2, +b3, -b1, +b2, -b3 in 2T um ein
    Sechseck [M, Leser].
  - Das "Dreieck" ist also der Stern der drei Richtungen mit Drehsinn, keine dreieckige Masche. KARTE-2 Punkt 3 laesst
    das zu ("Dreiecks- bzw. Wabengitter"); die Bedeutungssaetze sollten aber nicht nahelegen, dass Dreiecke umlaufen.
- **Neuheit:** Der Inhalt ist ein Nachbau aus der Literatur (Kitagawa u. a. 2010; anomale Phase Rudner u. a. 2013
  [L]). Neu ist nur die Umkehr, und die folgt aus der Symmetrie (B7).

**Wortlaut-Vorschlag DT3** (ERGEBNIS, Urteilstabelle und Punkt 4; RUNDE-42, Urteile):
"DT3 nach Plan nicht eingetroffen (Zaehlfehler am unteren Rand der pi-Luecke). Diagnose nach dem Einfrieren, kein
Urteil: Der Inhalt ist gestuetzt durch die Quelle (Kitagawa u. a. 2010, S. 8), durch die Volumen-Rand-Probe der
eingefrorenen Oberrand-Zahlen und durch die Nachzaehlung mit Summenprobe. Die Umkehr mit dem Drehsinn folgt aus der
Zeitumkehr."

## Frage 5: Bedeutungssatz (Ernte RUNDE-42.md)

**Urteil: haelt mit Einschraenkung.**
- Die Kernaussagen sind korrekt.
- Zwei Stellen sind zu stark:
  - die "nur am Rand"-Abschaetzung (A1);
  - das Etikett DT3 nach Kartenwortlaut (A2).
- Mehrere Stellen brauchen den Geltungsbereich (B2, B4, B6).

Durchgang durch die Ernte (RUNDE-42.md, Z. 221 bis 264):

| Stelle | Befund |
|---|---|
| Z. 226 bis 228: DT0 eingetroffen, DT1 nicht, DT2 nicht auswertbar | haelt (auswertung2.json, urteile) |
| Z. 229 bis 230: DT3 nach Plan nicht eingetroffen, "nach Kartenwortlaut eingetroffen" | erster Teil haelt; zweiter Teil ist ein nachtraegliches Etikett (A2) |
| Z. 232 bis 236: 2D [E] | haelt inhaltlich (Frage 4); ist aber ein Nachbau aus der Literatur, Kennzeichen [S, E] statt [E] (B7) |
| Z. 237 bis 239: 3D [E, M?], streng lokaler Takt traegt keine Netto-Haendigkeit | haelt (Frage 1); Kennzeichen jetzt [M, gegengelesen; Satz bei Read 2017]; Geltungsbereich ergaenzen (B2) |
| Z. 240 bis 241: 104 Automaten | Zahlen stimmen (72 + 6 + 25 + 1 = 104; max abs(W3) 5,33e-15); Gewicht ueberzeichnet (B3) |
| Z. 242 bis 243: Leitungssatz ist Sonderfall; W3 = 0 in QCA-WINDUNG-1 war vorab ableitbar | haelt. Folge fuer die Kalibrierung: WI1 (20 %) war vorab unmoeglich (B9) |
| Z. 244 bis 246: Literaturmodell | haelt (Frage 3); Wortlaut B5 |
| Z. 247 bis 248: Tick-Umkehr | haelt, auch allgemein und nicht nur fuer Produkte (B8) |
| Z. 256 bis 259: "Die Haendigkeit kann bei einem Takt nur am Rand eines hoeherdimensionalen Takt-Netzes sitzen" | **faellt als unbedingter Satz (A1)** |
| Z. 262 bis 264: Bedeutung | haelt mit Geltungsbereich; "lange Reichweite" ist irrefuehrend, die "nur"-Liste ist unvollstaendig (B4) |

**Zur Folge "der Takt-Weg zu chiralen Fermionen ist in 3D zu"** (KARTE.md Anlass) [M, Leser, aus T1 bis T3 und
Frage 1]:
- **Zu ist der Weg im Volumen**, im ganzen Zustandsraum, fuer freie Teilchen mit Translationsinvarianz, in zwei Faellen:
  - fuer jeden streng lokalen unitaeren Automaten (T2, Satz);
  - fuer jede Hamilton-Treibung, auch bei unendlicher Reichweite (T3). Finns Dreieckstakt aus Bindungsdrehungen faellt
    schon darunter.
- **"Lange Reichweite" allein hilft also nicht.** Es braucht einen nicht endlichreichweitigen Schritt, der keine
  Hamilton-Entwicklung ist. Physikalisch entsteht so etwas als effektiver Operator auf einem abgetrennten Bandraum,
  wie bei der Thouless-Pumpe in 1D und bei Higashikawa u. a. Der Ausgleich sitzt dann in den anderen Baendern.
- **Offen bleiben:**
  - Raender hoeherdimensionaler Takte [H, Folgekarte];
  - abgetrennte Bandraeume;
  - nicht-unitaere Schritte (Bessho/Sato S108: endlichreichweitig, w3 = 1);
  - Wechselwirkung und fehlende Translationsinvarianz (nicht untersucht).

**Wortlaut-Vorschlaege:**
- Fuer Z. 257 (A1): "Bei einem streng lokalen, unitaeren, translationsinvarianten Takt freier Teilchen kann die
  Haendigkeit nicht im Volumen sitzen (W3 = 0, Satz; Read 2017). Ein moeglicher Ort ist der Rand eines
  hoeherdimensionalen Takt-Netzes, wie die 1D-Randwelle am 2D-Netz [H]. Ausserhalb dieser Voraussetzungen gibt es
  weitere bekannte Wege: abgetrennter Bandraum (Higashikawa u. a.), quasilokale Nicht-Hamilton-Schritte
  (Grad-1-Kontrolle), nicht-unitaere Schritte (Bessho/Sato S108). Wechselwirkung ist nicht untersucht."
- Fuer Z. 263 bis 264 (B4): "Im Raum hebt sich die Haendigkeit bei einem streng lokalen, unitaeren Takt freier
  Teilchen im Volumen immer weg; bei einer Hamilton-Treibung des ganzen Zustandsraums sogar unabhaengig von der
  Reichweite. Ein einzelnes links- oder rechtsdrehendes Teilchen gibt es nach bekanntem Stand nur:
  - mit abgetrenntem Bandraum, dessen effektiver Takt nicht endlichreichweitig ist und dessen Partner in den anderen
    Baendern sitzt;
  - mit quasilokalen Schritten, die keine Hamilton-Entwicklung sind (mathematisch moeglich, siehe die
    Grad-1-Kontrolle mit exponentiellen Schwaenzen; physikalisch entstehen sie als Bandraum-Operatoren);
  - mit nicht-unitaeren Schritten;
  - vermutlich am Rand einer hoeheren Dimension [H].
  Wechselwirkung ist nicht untersucht."

## A-Befunde

- **A1, "nur am Rand" (RUNDE-42.md, Z. 256 bis 257, Abschaetzung):**
  - Woertlich: "Die Haendigkeit kann bei einem Takt nur am Rand eines hoeherdimensionalen Takt-Netzes sitzen, wie die
    1D-Randwelle am 2D-Netz."
  - Als unbedingter Satz faellt er. Gegenbelege:
    - die Ernte selbst, Z. 244 bis 246: Der Higashikawa-Takt traegt ein einzelnes Weyl-Teilchen im Volumen seines
      Bandblocks;
    - Teil 1: Die quasilokale Grad-1-Abbildung hat W3 = -1 im Volumen mit einem ungepaarten Weyl-Punkt bei pi;
    - Bessho/Sato (S108) bis (S113): endlichreichweitig, nicht-unitaer, w3 = 1;
    - die eigene Bedeutungszeile Z. 263 bis 264, die drei Orte nennt.
  - Er haelt nur unter den Voraussetzungen des Satzes (streng lokal, unitaer, frei, translationsinvariant, ganzer
    Zustandsraum). Auch dann ist "am Rand" Hypothese [H], nicht Folgerung.
  - Wortlaut-Vorschlag: Frage 5.
- **A2, DT3 "nach Kartenwortlaut eingetroffen":**
  - Fundstellen:
    - teil2-dreieck-takt/ERGEBNIS.md Z. 36 bis 37 ("Nach Kartenwortlaut ... ist DT3 eingetroffen"), Z. 51
      (Urteilstabelle) und Z. 53 bis 55;
    - RUNDE-42.md Z. 229 bis 230 ("nach Kartenwortlaut eingetroffen").
  - Grund: Die eingefrorene PLAN.md legt in Z. 134 fest: "**Kartenwortlaut:** DT0 bis DT3 wie oben". Die
    Akzeptanzmenge wurde nach dem Ergebnis von "beide Luecken" auf "eine Luecke" erweitert.
  - Als Urteil faellt das. DT3 bleibt "nicht eingetroffen".
  - Der Inhalt haelt als Diagnose. Ihn tragen Quelle, Volumen-Rand-Probe und Nachzaehlung (Frage 4).
  - Wortlaut-Vorschlag: Frage 4.

## B-Befunde

- **B1, Kennzeichnung T2:**
  - Fundstellen: teil2 ERGEBNIS Z. 19 ("[M, mit L]"), Z. 69 bis 72 und 183 bis 184 ("aus dem Gedaechtnis, nicht
    gegengelesen"); RUNDE-42 Z. 237 ("[E, M?]").
  - Vorschlag: "[M, gegengelesen (WINDUNG-LESER); als Satz in der Literatur: Read 2017, PRB 95, 115309, Abschn. IV,
    Gl. (39) [S]]".
  - Am Rand: "beliebig vielen inneren Zustaenden" heisst richtig "beliebig, aber endlich vielen".
- **B2, Geltungsbereich fehlt:**
  - Fundstellen: ERGEBNIS Punkt 2 und 5, Bedeutung 3D (Z. 230 bis 233); RUNDE-42 Z. 237 und 263.
  - Ergaenzen: "unitaer, freie Teilchen, translationsinvariant mit endlicher Zelle, im Volumen".
  - Grund: Die Unitaritaet ist tragend; Bessho/Sato (S108) ist endlichreichweitig, nicht-unitaer und hat w3 = 1.
    Raender und Wechselwirkung deckt der Satz nicht ab.
- **B3, Gewicht der 104 Automaten** (ERGEBNIS Punkt 2 "an 104 Automaten bestaetigt"; RUNDE-42 Z. 240):
  - 79 der 104 Faelle sind schon nach T1 bzw. T3 null. Die 6 Pyrochlor-Takte bestehen aus Bindungsdrehungen; fuer sie
    gilt W3 = 0 nach T3 sogar ohne Reichweitenbedingung. "Deshalb" in ERGEBNIS Z. 233 stimmt, der staerkere Grund
    ist aber T3.
  - Wortlaut-Vorschlag: Frage 2.
- **B4, "lange Reichweite(n)" und "nur"-Liste** (ERGEBNIS Z. 42; RUNDE-42 Z. 264):
  - Bei Hamilton-Treibung hilft keine Reichweite (T3). Mathematisch genuegen exponentielle Schwaenze (Grad-1).
  - Entscheidend ist ein nicht endlichreichweitiger Nicht-Hamilton-Schritt bzw. ein Bandraum.
  - Es fehlen nicht-unitaere Schritte und der Vermerk, dass Wechselwirkung nicht untersucht ist.
  - Wortlaut-Vorschlag: Frage 5.
- **B5, Higashikawa-Wortlaut** (ERGEBNIS Punkt 3, Z. 27 bis 33; RUNDE-42 Z. 244 bis 246):
  - Die Zerlegung ist die Konstruktion der Quelle (V^wh = U ⊕ U^H, Gl. 4 und 5) und keine Korrektur an ihr.
  - "k3 = 2 pi" bezieht sich auf den feinen Torus; in der Zone der Quelle liegt der Partner bei k = 0 im oberen Block,
    bei derselben Quasienergie.
  - Die "unteren Baender" sind ein Impulsfenster mit demselben Quasienergiespektrum wie der obere Block.
  - W bzw. W3 in jedem Satz nennen.
- **B6, Finns "Dreieck":**
  - Fundstellen: ERGEBNIS Z. 12 bis 15 und 224 bis 226; RUNDE-42 Z. 232 und 262.
  - Gerechnet ist der Umlauf der drei Bindungsrichtungen (Stern); im Volumen laeuft ein Teilchen in 2T um ein
    Sechseck.
  - Vorschlag: "Takt mit festem Umlaufsinn der drei Bindungsrichtungen".
- **B7, 2D ist Nachbau** (RUNDE-42 Z. 232 "2D [E]"):
  - Kitagawa u. a. 2010, S. 7 und 8 [S]; anomale Phase nach Rudner u. a. 2013 [L].
  - Die Richtungsumkehr ist durch die Zeitumkehr erzwungen. Kennzeichen [S, E]; nicht als neuer Befund weitergeben.
- **B8, Zeitumkehr-Begruendung** (ERGEBNIS Z. 245, "(T1)"):
  - T1 deckt nur Produkte ab. Die Aussage gilt aber allgemein [M, Leser]: W3(K U^-1 K) = W3(U).
  - Inversion gibt -1, k -> -k gibt -1. Komplexe Konjugation gibt +1, weil sie auf SU(2) zwei von vier reellen
    Koordinaten spiegelt.
- **B9, Kalibrierung:**
  - QCA-WINDUNG-1 WI1 (20 %) und KARTE-2 DT1 (35 %) waren fuer endlichreichweitige Automaten vorab unmoeglich.
  - Der Literaturweg in DT1 fuehrte nur ueber den Bandblock, und den schliesst die Planlesart aus.
  - Fuer Vorhersage-Bilanzen: Der Ausgang stand nach dem Satz vorab fest (Regel "Vertraege muessen scheitern und
    bestehen koennen").
- **B10, T3-Folgerung** (ERGEBNIS Z. 78 bis 79): Nach T2 genuegen auch endlichreichweitige Nicht-Hamilton-Schritte
  nicht. Vorschlag: "braucht Schritte, die weder endlichreichweitig noch Hamilton-Entwicklungen sind, einen
  abgetrennten Unterraum oder nicht-unitaere Schritte."
- **B11, Randzaehler fuer kuenftige Laeufe:**
  - Summenprobe und Volumen-Rand-Probe (C = W(darueber) - W(darunter)) als Vorbedingung in die eingefrorene Regel
    aufnehmen.
  - Die lam4-Zelle (-1, 0, 0) ist ungeklaert.

## Einfach gesagt

Der Agent sagt: Ein Takt, bei dem jedes Teilchen pro Schritt nur ein kurzes Stueck springen darf, kann im Raum nie
mehr links- als rechtsdrehende Teilchen erzeugen. Das stimmt. Es ist sogar ein bekannter mathematischer Satz (Read
2017), und die Herleitung des Agenten ist richtig. Der Satz gilt aber nur fuer verlustfreie Takte freier Teilchen im
Inneren des Raums. Mit abgetrennten Baendern wie im Literaturmodell, mit Verlusten oder vielleicht am Rand einer
vierten Dimension geht es doch. Deshalb ist der Ernte-Satz, die Haendigkeit koenne "nur am Rand" sitzen, zu stark. In
der Flaeche erzeugt der Dreiecks-Takt wirklich eine Randwelle, die nur in eine Richtung laeuft. Das war aber schon aus
der Literatur bekannt, und das Urteil darf nicht nachtraeglich von "nicht eingetroffen" auf "eingetroffen" umgestellt
werden. Alles sind Rechnungen an Modellen, keine Messungen.
