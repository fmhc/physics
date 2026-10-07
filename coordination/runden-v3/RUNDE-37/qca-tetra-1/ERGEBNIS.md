# QCA-TETRA-1: Ergebnis (Runde 37)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date):**
  - Start 2026-10-04 05:55:05 CEST; Plantext ab 06:13:49; Text dieser Datei ab 06:34:47 CEST.
  - Plan und Code eingefroren 06:31:40 CEST (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe auf der .69 ueber kleintest.sh (UTC = CEST − 2 h):
    - H-AB (cpu5): 04:32:10 bis 04:33:17 UTC, rc = 0, 66,1 s
    - H-C1 (cpu5): 04:33:17 bis 04:33:49 UTC, rc = 0, 31,6 s
    - H-C2b (cpu5): 04:33:49 bis 04:39:08 UTC, rc = 0, 318,1 s
    - H-C2a (p4000b): 04:32:10 bis 04:39:32 UTC, rc = 0, 440,7 s
    - H-C2L3 (p4000b): 04:39:32 bis 04:43:28 UTC, rc = 0, 236,0 s
    - Bild Teil C (bild_c.py) 04:43:39 bis 04:43:41 UTC und Auswertung 04:43:41 UTC, beide cpu5, rc = 0
- **Kennzeichen:**
  - [S] an der Quelle gelesen: G. M. D'Ariano, P. Perinotti, Phys. Rev. A 90, 062106 (2014), arXiv:1306.1934v2,
    Volltext Seiten 1 bis 8 und 12 bis 15 (als Bild gelesen).
  - [L] aus dem Gedaechtnis; [L?] unsicher; [M] eigene Mathematik; [H] Hypothese.
- **Art des Ergebnisses:**
  - Synthetische Rechnung an einem Literaturmodell plus eine numerische Suche; keine Messdatenbestaetigung.
  - Alle vier Ausgaenge waren vor der Rechnung am Schreibtisch ableitbar (PLAN.md Abschnitt 2, Beweise M1 bis M7).
    Die Rechnung prueft den Nachbau, die Suchmaschine und meine Beweise.

## Ergebnis zuerst

1. **Spin 1/2 ist auf BCC erzwungen, aber nur mit der kleinen Symmetriegruppe [S, nachgerechnet; M]:**
   - Der Weyl-Automat der Quelle (Eq. 24) ist exakt unitaer und hat bei k = 0 einen isotropen Kegel mit
     c = 1/√3 (Abweichung ≤ 6,5e−9 in 426 Richtungen).
   - Er ist nur unter den drei 180-Grad-Drehungen um die Achsen kovariant (Klein-Vierergruppe L_2). Die
     implementierenden Unitaeren sind −iσx, −iσy, −iσz; ihr Kommutator ist −I. Die Darstellung ist also projektiv:
     360 Grad wirken als −1.
   - Die Suche (200 Starts je Fall) findet Loesungen nur fuer die projektive Pauli-Darstellung von L_2: 92 Treffer,
     alle mit Kegel, zwei Spektralklassen, naemlich die beiden Weyl-Automaten der Quelle.
   - Alle acht linearen 2-dim Darstellungen (vier von T, vier von L_2) haben gar keine Loesung. Kleinster Defekt
     0,857 bzw. 0,400 gegen 6e−32 bei den Treffern.
2. **Mit der vollen Tetraeder-Drehgruppe T (120-Grad-Drehungen) gibt es keinen 2-Zustands-Automaten [M, numerisch
   bestaetigt]:**
   - Auch mit den Spinordarstellungen 2, 2', 2'' bleibt der Defekt bei mindestens 0,0444 (= 2/45).
   - Die Quelle sagt das selbst: "none of the automata is covariant under L_3" (S. 15) [S]. Fuer die 120-Grad-
     Drehungen gibt es keinen implementierenden Unitaeren (kleinster Singulaerwert 1,0).
   - Die Karte hatte T als Isotropiegruppe angenommen. Nach Kartenwortlaut ist QT1 deshalb nicht eingetroffen.
3. **Finns Diamantnetz traegt mit 2 Zustaenden je Knoten keinen isotropen unitaeren Automaten [M, numerisch
   bestaetigt]:**
   - Das gilt fuer unitaere Halbschritte (C-1) und fuer einen nur im Zweischritt unitaeren Automaten (C-2).
   - Es gilt fuer alle zwoelf Darstellungen; kleinster Defekt 0,667 (C-1) bzw. 0,394 (C-2) gegen 1e-10 fuer einen Treffer. Es gibt also weder einen Weyl-Kegel noch
     Knotenlinien, sondern gar kein Spektrum.
   - Grund: Vier Sprungrichtungen brauchen in C-1 vier paarweise orthogonale Bilder, in C² gibt es nur zwei. In C-2
     muesste det B̂(k) ein Monom sein, und das verbietet die Isotropie.
4. **Verdoppler:** Neben Γ hat der Weyl-Automat drei weitere Kegelpunkte, H, P und P'. Dort ist W = ±I; die
   Geschwindigkeit betraegt ueberall 1/√3.
5. **Eichung der QT2-Schwelle:** Schon der Referenzautomat auf BCC hat bei |k| = 0,05 eine Richtungsstreuung von
   2,8e−3 (Standardabweichung) bzw. 1,1e−2 (Spannweite). Die Schwelle 1e−3 der Karte haette er verfehlt.

## Urteile (lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil |
|---|---|---|---|
| QT0 | Nachbau unitaer (≤ 1e−12), isotroper Kegel mit c der Quelle (≤ 1e−6), 360 Grad = −1 | 80 % | eingetroffen |
| QT1 | [H] Nichttriviale isotrope Automaten nur fuer projektive Darstellungen | 55 % | eingetroffen (berichtigt); nach Kartenwortlaut nicht eingetroffen |
| QT2 | [H] Diamantnetz: isotroper unitaerer 2-Zustands-Automat mit Kegel bei k = 0 | 45 % | nicht eingetroffen |
| QT3 | Weyl-Automat hat weitere Kegelpunkte (Verdoppler) | 70 % | eingetroffen (drei weitere: H, P, P') |

- **Urteil nach Kartenwortlaut (verlangt bei Kartenberichtigungen):**
  - **QT1:** Die Karte nimmt die Tetraeder-Drehgruppe T als Isotropiegruppe. Mit T allein gibt es fuer keine
    Darstellung einen Automaten, auch fuer die projektiven nicht; nach Kartenwortlaut ist QT1 deshalb "nicht
    eingetroffen".
    - Das Haupturteil folgt der Definition der Quelle (Eq. 5): irgendeine auf S_+ transitive Gruppe, hier L_2 oder
      L_3 = T. Damit ist QT1 "eingetroffen".
  - **QT0:** Die Karte fragt nach "360 Grad", gemeint war V(C3)³. Die 120-Grad-Drehung ist keine Symmetrie des
    Quellautomaten. Geprueft habe ich die 360-Grad-Wirkung an den 180-Grad-Drehungen von L_2, phasenfrei ueber den
    Kommutator (PLAN.md Abschnitt 1, Punkt 2).
  - **QT2, QT3:** keine Abweichung vom Kartenwortlaut. "Richtungsstreuung" ist von mir festgelegt (Standardabweichung
    durch Mittelwert ueber 400 Richtungen) [F].

## Tabellen

### QT0: Nachbau des Weyl-Automaten (Eq. 24, ζ = (1 ± i)/4)

| Pruefung | A^+ (ζ = (1+i)/4) | A^− (ζ = (1−i)/4) | Regel |
|---|---|---|---|
| Unitaritaet: Koeffizienten von W^†W − I, max-abs | 0 | 0 | ≤ 1e−12 |
| Unitaritaet: k-Gitter 24³, max ‖W^†W − I‖₂ | 1,2e−15 | 1,2e−15 | ≤ 1e−12 |
| det W − 1 auf dem Gitter; Σ A_h − I | 1,1e−15; 0 | 1,1e−15; 0 | beschreibend |
| W(0) − I | 0 | 0 | ≤ 1e−12 |
| linearer Teil: M_j hermitesch; {M_i, M_j} − (2/3)δ_ij I | 0; 2,2e−16 | 0; 2,2e−16 | ≤ 1e−12 |
| ω/\|k\| bei \|k\| = 1e−7, 426 Richtungen: groesste Abweichung von 1/√3 | 6,5e−9 | 6,5e−9 | ≤ 1e−6 |
| implementierende Unitaere C2x, C2y, C2z: kleinster / zweitkleinster Singulaerwert | ≤ 1,6e−16 / 1,414 | ≤ 1,6e−16 / 1,414 | ≤ 1e−12 / ≥ 1e−3 |
| Kommutator K = U_x U_y U_x^† U_y^†: ‖K + I‖ (‖K − I‖) | 1,4e−16 (2,0) | 1,4e−16 (2,0) | K = −I |
| U_g² + I (det U_g = 1) | ≤ 1,3e−16 | ≤ 1,3e−16 | beschreibend |
| acht 120-Grad-Drehungen: kleinster Singulaerwert | 1,0 (keine Kovarianz) | 1,0 | beschreibend |
| Richtungsstreuung bei \|k\| = 0,05 (Std / Spannweite, relativ) | 2,82e−3 / 1,11e−2 | 2,82e−3 / 1,11e−2 | Eichung QT2 |

- Die gefundenen Unitaeren sind U(C2x) = −iσx, U(C2y) = −iσy, U(C2z) = −iσz. Das ist bis aufs Vorzeichen die
  Darstellung {I, iσx, iσy, iσz} der Quelle (S. 5) [S].

### Lesepruefung der Quelle (beschreibend, 50 Zufalls-k)

| Vergleich mit W aus Eq. (24) | Ergebnis |
|---|---|
| (A81)/(A82) mit (A78), Phase e^{−ik·h} | stimmt bis 3,5e−16; ζ = (1+i)/4 gehoert zu "+" |
| Eq. (33), Phase e^{−ik·h} | stimmt bis 3,5e−16; ζ = (1+i)/4 gehoert zu "−" |
| Haupttext (26) bis (28) | stimmt nur fuer W^T (die transponierten Loesungen B), Phase e^{−ik·h}, ζ = (1+i)/4 zu "−" |
| Eq. (16) mit e^{+ik·h} | keine der geschlossenen Formeln (26) bis (28), (A81)/(A82), (33); Abweichung ≥ 1,7 |
| Eq. (25), mit und ohne Vorfaktor 1/4 | in keiner Kombination (kleinste Abweichung 1,03, mit Vorfaktor) |
| Verschiebung um √3π e_x | W(k') = −W(k) bis 6e−16, wie S. 5 |
| Verschiebung um ±P = ±(√3π/2)(1,1,1) | A^+ → ∓A^− (bis 6e−16), nicht auf die Transponierte, wie ich S. 5 gelesen hatte |

- Folgerung [M]: Eq. (16) und Eq. (10)/(11) haben verschiedene Vorzeichenkonventionen; die geschlossenen Formeln der
  Quelle gehoeren zu e^{−ik·h}. Fuer Unitaritaet, Kegel, Kovarianz und Kegelpunkte spielt das keine Rolle (k → −k).
- Den Vorfaktor 1/4 in Eq. (25) bei ζ = (1 ± i)/4 halte ich fuer doppelt gezaehlt; Eq. (25) reproduziere ich aber
  auch ohne ihn nicht. Ob das ein Druckfehler oder mein Lesefehler ist, bleibt offen.
- Der eingefrorene Plan (Abschnitt 5, Rauch 1) sagt noch, (26) bis (28) passten in keiner Kombination. Das war vor
  dem transponierten Vergleich; mit ihm passt (26) bis (28) zu W^T.

### QT1: Suche je Gruppe und Darstellung (BCC, 8 Richtungen, 200 Starts je Fall)

| Fall | Art | dim (komplex) | Treffer (D < 1e−10) | davon Kegel | kleinster Defekt | Median |
|---|---|---|---|---|---|---|
| L3 (T): 1+1 | linear | 8 | 0 | 0 | 0,857 | 0,857 |
| L3: 1+1' | linear | 4 | 0 | 0 | 0,857 | 0,857 |
| L3: 1+1'' | linear | 4 | 0 | 0 | 0,857 | 0,857 |
| L3: 1'+1'' | linear | 4 | 0 | 0 | 0,857 | 0,857 |
| L3: 2 | projektiv | 4 | 0 | 0 | 0,0444 | 0,0444 |
| L3: 2' | projektiv | 4 | 0 | 0 | 0,0444 | 0,0444 |
| L3: 2'' | projektiv | 4 | 0 | 0 | 0,0444 | 0,0444 |
| L2: Pauli (Quelle) | projektiv | 8 | 92 | 92 | 5,8e−32 | 0,0444 |
| L2: 1+1 | linear | 8 | 0 | 0 | 0,857 | 0,857 |
| L2: 1+chi_x | linear | 8 | 0 | 0 | 0,400 | 0,400 |
| L2: 1+chi_y | linear | 8 | 0 | 0 | 0,400 | 0,400 |
| L2: 1+chi_z | linear | 8 | 0 | 0 | 0,400 | 0,400 |

- Die Treffer zerfallen in zwei Spektralklassen (57 und 35 Treffer):
  - eine spektral gleich A^− (und (A^−)^T, A^+ gespiegelt, A^+ konjugiert)
  - eine spektral gleich A^+ (und den entsprechenden Partnern)
  - beide mit je vier Kegelpunkten und v(k → 0) = 0,57735 in allen Richtungen
  - Das deckt sich mit "only four, modulo unitary conjugation" (S. 4) [S].
- Die Minima der Nicht-Treffer sind auffaellig rational: 6/7 (alle A_{h_i} gleich), 2/5 (L_2 mit diag(1, χ)), 2/45
  (Spinor unter T). Beschreibend, nicht hergeleitet.
- Grenze: Eine Suche mit 200 Starts ist kein Beweis. Die Nullbefunde stuetzen sich auf M1 bis M3 (Schreibtisch); die
  Suche haette sie widerlegen koennen und hat es nicht getan.

### QT2: Diamantnetz (2 Zustaende je Knoten, 200 Starts je Fall und Fassung)

| Fall | C-1: dim | C-1: Treffer | C-1: kleinster Defekt | C-2: dim | C-2: Treffer | C-2: kleinster Defekt |
|---|---|---|---|---|---|---|
| L3: 1+1 | 4 | 0 | 0,857 | 8 | 0 | 1,423 |
| L3: 1+1', 1+1'', 1'+1'' (je) | 2 | 0 | 0,857 | 4 | 0 | 1,423 |
| L3: 2, 2', 2'' (je) | 2 | 0 | 0,667 | 4 | 0 | 0,750 |
| L2: Pauli | 4 | 0 | 0,667 | 8 | 0 | 0,394 |
| L2: 1+1 | 4 | 0 | 0,857 | 8 | 0 | 1,423 |
| L2: 1+chi_x, 1+chi_y, 1+chi_z (je) | 4 | 0 | 0,667 | 8 | 0 | 0,947 |

- C-1: Halbschritt B̂(k) = Σ_a e^{−ik·e_a} B_a muss unitaer sein; C-2: nur W(k) = Ĉ(k)B̂(k).
- In allen 4800 Starts (zwoelf Faelle, zwei Fassungen, je 200) kein Treffer; Medianwerte gleich den Minima (Abweichung
  ≤ 3e−7). Die Minima von C-1 sind 6/7 und 2/3.
- C-2 mit L2-Pauli erreichte in allen Starts die Grenze von 400 Funktionsauswertungen; der Defekt stand dabei schon
  fest (Median 0,394098, Minimum 0,394097). Das langsame Kriechen deute ich als die flache Richtung B → λB, C → C/λ [H].
- Bild lauf-69/teil_C.png:
  - links der kleinste Defekt je Fall und Fassung
  - Mitte die Singulaerwerte von B̂(k) des besten C-1-Kandidaten
  - rechts die Betraege der Eigenwerte von W(k) des besten C-2-Kandidaten, laengs Γ–X–W–L–Γ–K
  - Fuer einen unitaeren Automaten laegen alle Kurven bei 1; bei den Kandidaten fallen sie bis auf 0 bzw. 0,13.
- Folgerung: Auf dem Diamantnetz mit 2 Zustaenden je Knoten gibt es kein Spektrum, das man auf Kegel oder Linien
  pruefen koennte. Die Frage der Karte "Kegel oder nur Knotenlinien wie in KITAEV-DIAMANT-1?" beantwortet sich mit:
  weder noch.

### QT3: Kegelpunkte des Weyl-Automaten

| Punkt | k | W(k) fuer A^+ | W(k) fuer A^− | v (min bis max ueber 126 Richtungen) |
|---|---|---|---|---|
| Γ | (0, 0, 0) | +I | +I | 0,577350 bis 0,577351 |
| P | (√3π/2)(1,1,1) = (2,721; 2,721; 2,721) | −I | +I | 0,577350 bis 0,577351 |
| H | √3π(0,0,1) = (0; 0; 5,441) | −I | −I | 0,577350 bis 0,577351 |
| P' | (2,721; 2,721; 8,162) ≡ −P | +I | −I | 0,577350 bis 0,577351 |

- Kegeltest: β(2ε)/β(ε) zwischen 1,999998 und 2,000002, also linear.
- Aequivalent unter reziproken Gittervektoren √3π·FCC; die Suche fand je Automat genau vier verschiedene Punkte.
- Bild lauf-69/omega_A.png: ±ω(k) laengs Γ–H–N–Γ–P–H | P'–Γ fuer A^+ und A^−.

## Kontrollen

- **Positivkontrolle:** Dieselbe Suche findet unter L_2-Pauli die bekannten Automaten, 92 von 200 Starts. Ein
  Nullbefund bei T oder auf dem Diamantnetz liegt also nicht an einer blinden Suchmaschine.
- **Gleichwertige Darstellungen:** 2, 2', 2'' sowie chi_x, chi_y, chi_z sowie die vier "alle gleich"-Faelle geben
  jeweils dieselben Defektminima. So war es vorab erwartet: Die Konjugation haengt nur an der projektiven Klasse bzw.
  am Quotientencharakter.
- **Darstellungstabelle:** Der Kommutator der Lifts von C2x und C2y ist bei allen vier projektiven Faellen −I und bei
  allen acht linearen +I. Konjugationskern: T mit 1+1 12, T mit den anderen linearen 4 (V_4 wirkt trivial),
  projektiv 1, L_2 linear 4 bzw. 2.
- **Gruppen:** T hat 12 Elemente, 0 Konsistenzfehler; 2T hat 24, Kern ±I; die SO(3)-Wirkung der Spinor-Lifts ist
  exakt; V(C3)³ = −I und V(C2x)² = −I exakt.
- **Defekt-Codepruefung:** Das Gittermittel von ‖W^†W − I‖_F² gegen die exakte Koeffizientensumme weicht relativ um
  2,3e−16 (BCC) bzw. 2,9e−14 (Diamant, einschliesslich Vergleich ĈB̂ gegen die Koeffizientenform) ab.
- **Spektrum gegen Eigenvektoren [M]:** ω(k) = arccos(c_xc_yc_z ± s_xs_ys_z) ist unter Vertauschung der Achsen
  invariant, hat also die volle Tetraeder-Symmetrie. Die C3-Kovarianz bricht erst an den Eigenvektoren
  (Helizitaetsstruktur); die Suche zeigt, dass sich das mit 2 Zustaenden nicht reparieren laesst.
- **Was nicht scheitern konnte [M]:** Alle vier Urteile waren am Schreibtisch ableitbar (M1 bis M7), QT3 und die
  L_3-Aussage auch aus der Quelle. Scheitern konnten der Nachbau (Lesepruefung: drei Formeln der Quelle passen nicht
  zu Eq. 24), die Suchmaschine (Positivkontrolle) und meine Beweise, falls die Suche doch Treffer bei T oder auf dem
  Diamantnetz gefunden haette.

## Kartenberichtigungen (vor dem Einfrieren, PLAN.md Abschnitt 1)

1. **Isotropiegruppe:** Die Karte setzt T; die Quelle verlangt eine beliebige auf S_+ transitive Gruppe und benutzt
   L_2 (Eq. 5, S. 3; S. 5; S. 15). Gerechnet sind beide Gruppen. Das Haupturteil folgt der Quelle; das Urteil nach
   Kartenwortlaut steht oben.
2. **360 Grad:** gemessen an L_2 (Kommutator −I, U_g² = −I), da C3 keine Symmetrie ist.
3. **"Trivial":** Mit 8 Spruengen ohne Selbstwechselwirkung kann es keine isotrope triviale Loesung geben [M]. "Nur
   trivial" heisst deshalb hier: keine Loesung.
4. **Richtungsstreuung:** von mir festgelegt; schon der Referenzautomat verfehlt 1e−3 (Eichung, Abschnitt 1, Punkt 4).
5. **Teil C:** zwei Fassungen, C-1 (Kartenwortlaut) und C-2 (Hinweis der Leitung); beide gerechnet.
6. **Literaturangaben der Leitung:** arXiv:1306.1934 und PRA 90, 062106 (2014) sind richtig [S]. Bisio et al. (Found.
   Phys. 2015; PRA 2016) habe ich nicht abgerufen.

## Latten (v3)

- **L1 kann scheitern:** teilweise. Die Ausgaenge waren am Schreibtisch ableitbar. Die Rechnung haette meine Beweise
  M1 bis M7 widerlegen koennen (ein Treffer bei T oder auf dem Diamantnetz), und der Nachbau haette scheitern
  koennen.
- **L2 Gegenprobe:**
  - Positivkontrolle L_2-Pauli
  - gleichwertige Darstellungen mit gleichen Minima
  - Kommutator +I gegen −I in der Darstellungstabelle
  - C3-Test (nicht implementierbar, wie in der Quelle)
  - Gitter gegen exakten Defekt
- **L3 Numerik:** Koeffizienten exakt 0, Gitter 1e−15, Geschwindigkeit 6,5e−9; Treffer bei D ≈ 1e−31,
  Nicht-Treffer bei D ≥ 0,044. Zwischen beiden liegen 29 Groessenordnungen.
- **L4 schon bekannt:** ja, fuer Teil A und die L_3-Aussage (Quelle, S. 5 und S. 15) [S]. Ob die Unmoeglichkeit auf
  dem Diamantnetz mit 2 Zustaenden veroeffentlicht ist, weiss ich nicht [L?]. Sie ist eine kurze Folgerung aus der
  Unitaritaet und vermutlich in der Quantum-Walk-Literatur bekannt.
- **L5 Messbezug:** keiner. [H, L?, nicht geprueft]: Die Richtungsabhaengigkeit der Geschwindigkeit ist linear in
  k·ℓ. Bei Planck-Maschenweite laege sie in der Groessenordnung, die Laufzeitmessungen an Gammablitzen fuer lineare
  Lorentz-Verletzung pruefen.

## Bedeutung fuer Finns Bild

- **Belegt im Modell [S, nachgerechnet; M]:**
  - Auf dem BCC-Netz (jeder Punkt mit den 8 Wuerfelecken verbunden, also mit beiden Tetraedern) erzwingen "2
    Zustaende + Unitaritaet + Isotropie im Sinn der Quelle" eine Spinordarstellung: Spin 1/2 ist dort keine Wahl.
  - Die Symmetrie, die das leistet, ist aber nur die Klein-Vierergruppe (drei 180-Grad-Drehungen). Die 120-Grad-
    Drehungen des Tetraeders kann kein 2-Zustands-Automat respektieren; nur das Spektrum hat sie.
  - Langwellig ist der Automat ein masseloses Weyl-Teilchen mit c = 1/√3 (Gitterschritt je Zeitschritt), mit drei
    Verdopplern an H, P, P'.
- **Fuer Finns Diamantnetz:** Mit 2 Zustaenden je Knoten gibt es keine isotrope unitaere Spielregel, weder mit
  unitaeren Teilschritten noch nur im Zweischritt. Das ist ein echter Unterschied zwischen BCC und Diamant.
- **Nicht gezeigt:**
  - ob T-Kovarianz mit 4 Zustaenden (Dirac-Automat) moeglich ist
  - ob das Diamantnetz mit 4 Zustaenden je Knoten (wie die Γ-Matrizen in KITAEV-DIAMANT-1) einen Weyl- oder
    Dirac-Kegel traegt
  - Masse, Wechselwirkung, gekruemmte Netze
- **Vorschlag fuer Folgekarten [H, nicht gerechnet]:**
  - Diamantnetz mit 4 Zustaenden je Knoten: dieselbe Suche, Kegel bei k = 0?
  - BCC mit 4 Zustaenden: Gibt es T-kovariante Dirac-Automaten?

## Selbstanzeigen

1. **Lokale Werkzeuge:**
   - Ausser jq, ssh, scp, sha256sum, date, grep und sed habe ich Dateibefehle benutzt: mkdir, cp, ls und cat (fuer
     die Ausgabedatei eines Hintergrundbefehls).
   - Dazu lokale Warteschleifen im Hintergrund (until ssh ...; do sleep N; done). Ein einzelner Befehl mit sleep 45
     wurde vom Werkzeug abgelehnt und lief nicht.
   - Lokal lief kein Interpreter, kein python, awk oder perl.
2. **Auf der .69 ausserhalb des Starters:**
   - Nur Dateiverwaltung und Abfragen: mkdir, mv, ls, cat, tail, head, grep, sha256sum, date, sleep.
   - nohup sh -c, um mehrere Starteraufrufe einer Spur hintereinander zu ketten.
   - systemctl --user list-units (nur lesend), um vor p4000b zu pruefen, dass WM-1-MB nicht laeuft.
   - Ein ls auf site-packages (matplotlib vorhanden).
   - Kein Python-Aufruf ausserhalb des Starters, auch keine Versionsprobe.
3. **Quellenabrufe (3 von 4):**
   - Abruf 1 (arXiv-Schnittstelle) gab HTTP 429 ohne Inhalt; ich habe ihn trotzdem gezaehlt.
   - Das PDF habe ich als Bild gelesen, Seiten 1 bis 8 und 12 bis 15. Nicht gelesen sind die Seiten 9 bis 11 und 16
     bis 20: Rest des relativistischen Grenzfalls, Anhaenge B und C, Rest des PC-Beweises.
4. **Aenderungen nach den Rauchlaeufen, vor dem Einfrieren:**
   - Code: NaN-Berichtigung, transponierte Lesevergleiche, Aufteilung von Teil C auf Teillaeufe, feste Farben im
     Bild zu Teil C.
   - Planwortlaut zu Saaten und Kegelsuche an den Code angepasst. Die erste Fassung beschrieb BFGS von den 32
     kleinsten Gitterpunkten; gerechnet wird Levenberg-Marquardt von lokalen Minima aus.
   - Keine Schwelle und keine Urteilsregel geaendert.
5. **Ausgang vorab bekannt:** Alle vier Urteile waren nach den Schreibtischbeweisen (vor dem ersten Rauchlauf) und
   nach den Rauchlaeufen absehbar.
6. **QT1-Hauptregel in Kenntnis des Ausgangs:**
   - Die berichtigte Regel (L_2 oder L_3) habe ich festgelegt, als M1 bis M3 schon zeigten: T laesst keinen
     Automaten zu, L_2-Pauli schon.
   - Der Auftrag verlangte die Definition der Quelle. Das Urteil nach Kartenwortlaut ("nicht eingetroffen") steht
     deshalb gleichrangig daneben.
7. **QT2-Regel:** Beide Fassungen (C-1 oder C-2) zaehlen. Festgelegt nach M6 und M7; ohne Wirkung, beide ohne Treffer.
8. **Eigene Festlegungen [F]:** Richtungsstreuung (Standardabweichung durch Mittelwert), 360-Grad-Kriterium ueber den
   Kommutator, Klassen "trivial", "Kegel" und "andere".
9. **Phasenkonvention:** Hauptkonvention ist Eq. (16), e^{+ik·h}, obwohl die geschlossenen Formeln der Quelle zu
   e^{−ik·h} gehoeren. Alle Urteilsgroessen sind davon unabhaengig [M].
10. **Beweise nicht gegengelesen:** M1 bis M7 sind meine eigenen; kein frischer Leser hat sie geprueft. Die Numerik
    bestaetigt sie, ersetzt aber keine Lesung.
11. **Laufbuchhaltung:**
    - Nach dem Einfrieren keine Aenderung an Plan, Code oder Regeln.
    - Hauptlaeufe je einmal: H-AB, H-C1, H-C2a, H-C2b, H-C2L3, danach bild_c und auswertung.
    - Rauchlaeufe: rauch1 (AB, C), rauch2 (AB, C1, C2L3, C2L2, Bild, Auswertung).
    - Hoechstens zwei Laeufe zugleich, nur die Spuren cpu5 und p4000b.
12. **Gegenlesen dieser Datei:** Beim Abgleich mit den JSON-Dateien fand ich zwei falsche Zahlen in meiner ersten
    Textfassung. Eq. (25) stand mit kleinster Abweichung 1,41 statt 1,03, Eq. (16) mit ≥ 1,8 statt ≥ 1,7. Ursache war
    sort -g unter deutscher Locale (Dezimalpunkt). Beide sind vor der Abgabe berichtigt; Urteile sind nicht betroffen.
13. **Zeitbox:** 120 min ab 05:55:05 CEST; Text abgeschlossen um 06:44:40 CEST (date), Nachtrag Gegenlesen abgeschlossen
    um 06:45:54 CEST (date).

## Dateien

- **Plan:** PLAN.md und PLAN.md.eingefroren-20261004-063140; Pruefsummen in EINGEFROREN-SHA256.txt.
- **Code:** code/qca_tetra.py, code/auswertung.py, code/bild_c.py, je mit .eingefroren-20261004-063140.
- **Quelle:** quelle/dariano-perinotti-2014-arXiv-1306.1934v2.pdf.
- **Rauchlaeufe:** rauch-69/ (rauch1 und rauch2: json, log, png, rauch2_auswertung.json).
- **Hauptlaeufe:** lauf-69/haupt_AB.json/.log, haupt_C1, haupt_C2a, haupt_C2b, haupt_C2L3 (json, log),
  omega_A.png, suche_B.png, teil_C.png, auswertung.json, auswertung.log, bild_c.log, PRUEFSUMMEN.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/runde37-qca/ (code/, rauch/, lauf/).

## Einfach gesagt

Wir haben geprueft, ob die einfachste Quanten-Spielregel mit nur zwei inneren Zustaenden je Knoten auf einem
Tetraeder-Netz von selbst Teilchen mit halbem Spin ergibt. Auf dem Netz, in dem jeder Punkt mit allen acht
Wuerfelecken verbunden ist (also mit zwei Tetraedern), klappt es nur, wenn sich die zwei Zustaende wie ein Spin 1/2
drehen: Nach einer vollen Umdrehung bekommen sie ein Minuszeichen, und bei langen Wellen laufen die Teilchen wie
masselose Neutrinos mit fester Geschwindigkeit in alle Richtungen. Die Regel vertraegt aber nur die drei halben
Drehungen um die Achsen, nicht die Dritteldrehungen des Tetraeders; verlangt man die volle Tetraeder-Symmetrie, gibt
es mit zwei Zustaenden gar keine Regel. Auf Finns eigentlichem Netz mit vier Strichen je Knoten (Diamant) gibt es mit
zwei Zustaenden ueberhaupt keine passende Regel; dafuer braucht es mehr innere Zustaende. Das ist eine Rechnung an
einem Literaturmodell und an unserem Netz, keine Messung.
