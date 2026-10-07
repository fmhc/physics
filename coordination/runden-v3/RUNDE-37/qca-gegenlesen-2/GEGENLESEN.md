Urteil: TRAEGT MIT EINSCHRAENKUNG. Rechnung, Zahlen und Teilbeweis stimmen (eine unbegruendete Stelle). Die
Ableitbarkeit ist unterschaetzt: QR2 lag schon in den Daten von QCA-DIRAC-T-1. Vier Saetze der Leitung sind zu stark
oder falsch (A1 bis A4). QCA-DIRAC-RUECK-1 ist nicht noetig.

# QCA-GEGENLESEN-2: Gegenlesen QCA-BCC-RUECK-1 (frischer Leser, Haus Anthropic)

- Beginn: 2026-10-04 10:36:28 CEST (date); Text abgeschlossen 2026-10-04 10:59:08 CEST (date), also 22 min 40 s
  von 50 min Zeitbox.
- Auftrag: RUNDE-37/qca-gegenlesen-2/KARTE.md, sha256 612b50a97cf17ad840abb9c4493c29ded922e04cdd4b58058e40cce6db1ed15e
- Kennzeichen: [S] an der Quelle gelesen, [M] Mathematik, [ES] eigener Schluss, [L] Literatur aus dem Gedaechtnis.
- Schreibtisch, keine Laeufe; lokal nur cat, sed, grep, jq, ls, wc, sha256sum, date und pdftotext nach stdout (lokale
  Kopie der Quelle). Kein Interpreter, kein ssh, kein Netzabruf.

## Ergebnis zuerst (je Frage ein Satz)

1. **Teilbeweis:** R4 ist richtig (im Schritt "Frequenz h_a + h_b" fehlen zwei Terme, harmlos, weil sie im anderen
   Block liegen), beweist aber nur den Sonderfall getrennter Summanden; QR1 im Ganzen traegt nur die Suche, und die
   Luecke ist nicht geschlossen.
2. **Ableitbarkeit:** Vorab ableitbar waren Entartung und vier Cluster bei k = 0, Isotropie in erster Ordnung, 360 Grad =
   −1 (Eingabe) und die Entartung an H, P, P'; nur generisch sind Kegel und Masselosigkeit, nicht ableitbar die
   Isotropie bei 0,05. Die Existenz lag schon in den Daten von QCA-DIRAC-T-1 (16 unzerlegbare Treffer mit beiden Gruppen).
3. **Inversion:** Sie erzwingt die Matrix-Lesart, nicht die Block-Lesart (Gegenbeispiel C·S_+ ⊕ C·S_−); die massiven
   Form-P-Treffer und Konstruktionen von QCA-DIRAC-T-1 sind aber unzerlegbar und springen in beide Gruppen gleich stark,
   also ist "Masse mit Rueckspruengen" dort gezeigt und QCA-DIRAC-RUECK-1 ueberfluessig.
4. **Direkte Summe:** Die Block-Lesart ist sauber definiert und richtig angewandt; alle 17 Treffer sind unzerlegbar
   (Kommutant 1, Abstand 0,27 bis 1,48), also echt gekoppelt, aber nicht alle sind von der Bauart "Muenze mal
   Verschiebung".
5. **Verdoppler:** Erzwungen ist nur die Entartung an H, P, P'; die Kegel dort sind eine Eigenschaft dieser Loesungen
   (mit Inversion gibt es Treffer ohne sie), und Nielsen/Ninomiya gilt fuer Automaten nur abgeschwaecht.
6. **Texte der Leitung:** Alle Zahlen stimmen; falsch oder zu stark sind "nur QR0 vorab ableitbar" (A1), die Bauart als
   Beschreibung der Treffer (A2), "erst ab 8 inneren Zustaenden" (A3) und "Masse mit Rueckspruengen offen" (A4).

## Gelesene Quellen

- qca-bcc-rueck-1: KARTE.md, ERGEBNIS.md (ganz; sha256 b32054d4...), PLAN.md Abschnitte 1 bis 3 (sha256 5660b21c..., gleich der
  eingefrorenen Fassung laut EINGEFROREN-SHA256.txt), code/qca_rueck.py Zeilen 548 bis 615 (bloecke, rueck_pruefung),
  lauf-69/auswertung.json (sha256 183287c0...), lauf-69/haupt_8Na/8Oa/8Ob.json (jq).
- qca-dirac-t-1: ERGEBNIS.md Zeilen 1 bis 80, PLAN.md Zeilen 126 bis 172, code/qca_dirac.py Zeilen 463 bis 491
  (implementing, am_treffer), lauf-69/haupt_BOP.json, haupt_BN.json, haupt_BO1/BO2.json, haupt_0.json (jq).
- RUNDE-39.md Zeilen 227 bis 261 und 297; RUNDE-39/WEICHE-STAND-v2.md ganz.
- Quelle 2017: lokale Kopie quelle/dariano-erba-perinotti-2017-arXiv-1708.00826.pdf per pdftotext (Textschicht vorhanden),
  kein Netzabruf. Gelesen: "we will assume A_h ≠ 0 for all h ∈ S+ ∪ S−, whereas in general we allow for the case A_e = 0"
  und "By definition the transition matrices are nonnull" [S]. Literaturabrufe: 0 von 3.
- RUNDE-37/qca-gegenlesen/GEGENLESEN.md nur gezielt per grep (Zeilen 1, 209 bis 216, 315 bis 319). Nicht gelesen:
  qca-diamant-4, qca-tetra-1 (Zeitbox; die Befunde unten stuetzen sich nicht darauf, ausser wo D1/S2 genannt sind).

## Frage 1: Teilbeweis 4 Zustaende

**Urteil:** R4 ist richtig [M, Schritt fuer Schritt nachgeprueft], hat aber eine unbegruendete Stelle (Schritt 4) und
deckt nur zwei Eckpunkte ab. Alles andere an QR1 stuetzt sich auf die Suche. Geschlossen habe ich die Luecke nicht; ein
naheliegendes Gegenbeispiel scheitert.

**Nachpruefung** (2+2', Form N; P_a = A_{h_a}, M_a = A_{−h_a}; t_a = (±1, ±1, ±1) mit Produkt +1):
1. Π_+ = Σ P_a^†P_a vertauscht mit V, weil T die Menge S_+ permutiert; also Π_+ = x P_2 + y P_2'. Richtig.
2. Frequenz h_i − h_j (i ≠ j): Beitraege nur P_j^†P_i und M_i^†M_j. Die Frequenztypen sind getrennt: h_i − h_j ist vom
   Typ (0, ±2, ±2)/√3, h_a + h_b vom Typ (±2, 0, 0)/√3, 2h_a vom Typ (2, 2, 2)/√3. Bei Π_+ = P_2 liegen die zwei Summanden
   in End(2) bzw. End(2'), also verschwinden beide. Richtig.
3. Rang 1: vier paarweise orthogonale, nichtleere Bilder in C^4, durch Kovarianz alle gleich gross, also Rang 1. v_a ist
   Eigenvektor der Dreierdrehung um h_a (ein invarianter Rang-1-Operator verlangt das), in 2 ein Spinzustand entlang
   ±h_a: |⟨v_a|v_b⟩|² = (1 + h_a·h_b)/2 = (1 − 1/3)/2 = 1/3. Gegenprobe: Σ_a |v_a⟩⟨v_a| = 2·I + (Σ_a h_a)·σ/2 = 2·I,
   also |α|² · 2 = 1. Richtig.
4. **Frequenz h_a + h_b: unvollstaendig begruendet.** Wegen Σ_a h_a = 0 gilt h_a + h_b = −(h_c + h_d) mit dem Restpaar
   {c, d} (Beispiel t_1 + t_2 = (2, 0, 0) = −(t_3 + t_4)). Zu dieser Frequenz tragen vier Terme bei:
   M_b^†P_a + M_a^†P_b + P_d^†M_c + P_c^†M_d = 0. R4 nennt nur die ersten zwei. Der Schluss bleibt richtig: Bei
   Sektortrennung liegen die ersten zwei in Hom(2 → 2'), die letzten zwei in Hom(2' → 2), beide Gruppen verschwinden
   einzeln. Die Klammer "(Hom(2, 2'))" deutet das an, begruendet es aber nicht.
5. Frequenz 2h_a: nur M_a^†P_a (keine Gegenfrequenz). Die lineare Unabhaengigkeit von |v'_b⟩⟨v_a| und |v'_a⟩⟨v_b| folgt
   schon aus v_a ∦ v_b. Damit steht jedes u'_b senkrecht auf der Orthonormalbasis {u_a}: Widerspruch. Richtig.
6. 1+3: gleicher Gang, die v'_a in 3 sind Eigenvektoren der Dreierdrehung um h_a (Achse oder zirkular), paarweise
   unabhaengig. Richtig.
7. Form O: Die Schritte 2 bis 5 enthalten keinen Vor-Ort-Term (A_0 traegt nur zu den Frequenzen 0 und ±h_a bei). Die
   Sektortrennung ist also auch mit A_0 ausgeschlossen (Π_+ = x P_2, Π_− = z P_2', x, z > 0). Das sagt R4 nicht
   ausdruecklich, es stimmt aber.

**Was bewiesen ist:** In Form N gilt Π_− = I − Π_+. R4 schliesst von den Punkten (x, y) im Quadrat [0, 1]² nur (1, 0) und
(0, 1) aus. (0, 0) und (1, 1) sind die Einbahn-Automaten. Offen sind das ganze Innere und die Raender, also gerade der
Fall, in dem eine Muenze die Sektoren mischt. Fuer 1+3 gilt dasselbe. Vorausgesetzt ist ausserdem die Darstellungsliste
(D1, S2 aus den Vorgaengerkarten, gemischte Klassen ueber V(−1)); die habe ich nicht nachgeprueft.

**Nur durch die Suche gestuetzt:** alle Faelle mit gebrochenen Anteilen und damit QR1 im Ganzen; ebenso der Befund,
dass einseitige Treffer nur (J_+, J_−) = (4, 0) oder (0, 4) haben. Die Suche ist ordentlich: Das Minimum ist positiv und
reproduziert (Form N r50: 0,0015294 bei 2+2', 4/45 bei 1+3). Beweiskraft hat sie nicht.

**Schreibtischversuche [M]:**
- Gegenbeispielansatz W = c·C_1 S_+(k) + i s·C_2 S_−(k) auf 2+2' (c² + s² = 1, monomiale Basis p_a, D = C_1^†C_2 =
  d_1 P_2 + d_2 P_2'). Unitaritaet verlangt, dass S_+^† D S_− hermitesch ist.
  - Frequenz 2h_a: ⟨p_a|D|p_a⟩ = (d_1 + d_2)/2 = 0. Grund: p_a hat je die Haelfte Gewicht in 2 und 2' (Frobenius:
    (2/24)·6·1 = 1/2).
  - Frequenz h_a + h_b: Der Gegenterm sitzt auf den Plaetzen {c, d}, also ⟨p_a|D|p_b⟩ = 0 fuer a ≠ b.
  - Also D = 0, Widerspruch: Der einfachste gemischte Ansatz scheitert.
- Eine Ganzzahligkeit von J_+ habe ich versucht und verworfen. Wegen h_a + h_b = −(h_c + h_d) gilt nur
  B_−^†B_+ + B_+^†B_− = 0, nicht B_−^†B_+ = 0; S_+- und S_−-Teil haben also nicht je k orthogonale Bilder.
- Damit bleibt die Luecke offen. Ein Abschluss braucht eine eigene Karte (Beweis oder gezielte Suche bei festem
  (x, y) im Innern).

## Frage 2: Ableitbarkeit

**Urteil:** Die Vermutung der Leitung trifft zu und reicht noch weiter. QR2 war bis auf die Isotropie bei |k| = 0,05
am Schreibtisch ableitbar; das sagt ERGEBNIS selbst (R3, Selbstanzeige 1). Ausserdem lag QR2 in den Daten von
QCA-DIRAC-T-1 schon vor. Nicht ableitbar sind nur "masselos" als Zwang und die Isotropie bei endlichem k.

- **Entartung bei k = 0 (Schur): ja, erzwungen [M].**
  - W(0) vertauscht mit V. Alle Spinor-Irreps von 2T sind zweidimensional (2, 2', 2''; 1+1+1+9+4+4+4 = 24 = |2T|), also
    ist jeder Eigenwert von W(0) mindestens zweifach.
  - Bei K4 ist der Kommutant M_2 ⊕ M_2, also W(0) = U ⊗ I_2 ⊕ U' ⊗ I_2. Das ergibt genau vier Zweifach-Cluster (bis auf
    zufaellige Zusammenfaelle).
- **Kegel: nicht erzwungen.**
  - Die erste Ordnung auf einem Cluster liegt in Hom_T(3, End 2) = Hom_T(3, 1 ⊕ 3). Dieser Raum ist eindimensional, also
    ist die erste Ordnung c·k·σ.
  - c ≠ 0 ist generisch, c = 0 aber erlaubt (Kodimension 1 je Cluster; QCA-DIRAC-T-1 S4). Eine Inversion erzwingt c = 0.
- **Isotrop in erster Ordnung: ja, ableitbar [M].**
  - Das folgt aus demselben Schritt: Das Spektrum ist ±|c||k|.
  - Gleichwertig: Der einzige reelle T-invariante symmetrische Tensor auf 3 ist δ_ij, denn 3 ⊗ 3 = 1 + 1' + 1'' + 3 + 3,
    und 1', 1'' sind nicht trivial.
  - Bei |k| = 0,05 nicht ableitbar: T erlaubt in zweiter Ordnung b·Q·σ mit Q = (k_y k_z, k_z k_x, k_x k_y).
- **360 Grad = −1: ja, ableitbar, genauer gesagt eine Eingabe.**
  - V ist spinoriell gewaehlt (K1 bis K5), also V(−1) = −I.
  - Die Pruefung am Treffer (Implementierer eindeutig, K = −I) folgt fuer jeden unzerlegbaren Treffer: Die Loesungen von
    U A_h = A_{gh} U sind U_0 mal Kommutant. Fuer unitaere Automaten ist der Kommutant der A_h derselbe wie der der
    *-Algebra (Z vertauscht mit allen W(k), also auch mit W(k)^† = W(k)^{−1}). Bei Kommutant 1 gilt U = Phase·V(g), also
    K = V(C2x)V(C2y)V(C2x)^†V(C2y)^† = −I.
  - Die beiden Vermerke ("am Treffer" 12, "nur ueber die Darstellung" 12) mussten deshalb gleich ausfallen.
- **Masselos ohne Inversion: nur als "generisch" ableitbar, nicht als Zwang.**
  - Masse heisst c = 0 auf allen vier Clustern.
  - In der R3-Familie selbst gibt es massive Glieder: v = ||a|² − |b|²|/3 (ERGEBNIS, Teil 0) wird 0, wenn die
    Eigenvektoren ausgeglichen sind. QCA-DIRAC-T-1 Konstruktion (b), (N ⊗ C)·diag(S_+, S_−), ist genau so ein Glied, und
    es ist massiv.
  - Ob jede massive T-Loesung eine Inversion hat, ist nicht gezeigt. "Masse gibt es ohne Inversion keine" (ERGEBNIS,
    Ergebnis zuerst 2) ist deshalb zu stark (Befund B3). Der fruehere Gegenleser hatte "Masse braucht Inversion" schon
    als zu stark markiert (qca-gegenlesen/GEGENLESEN.md Zeile 209, A5).
- **Existenz von 8-Zustands-Automaten mit Rueckspruengen: ableitbar und schon in den Daten [S, jq].**
  - QCA-DIRAC-T-1 lauf-69, Felder gewicht_S+_S- und am_treffer.C2x.nullraum:
    - Form N, K4: 10 von 12 nichttrivialen Treffern mit S+/S− = 4/4
    - Form O, K4: 5 von 10 mit beiden Gruppen (3,998/3,998; 4/4 dreimal; 0,044/0,044), die anderen 5 einseitig
    - Form N, K5: einer mit 4/4
  - Alle 16 haben einen eindeutigen C2x-Implementierer (Nullraum 1, zweiter Singulaerwert 0,127 bis 0,95, also
    unzerlegbar, siehe oben), vier lineare Zweifach-Cluster bei k = 0 und Wirkung "projektiv". Stichprobe: lin_min =
    lin_max (erste Ordnung isotrop, wie Schur verlangt).
  - QR2 war damit vor der Karte (09:23:48) belegt, bis auf die Isotropie bei 0,05 und die formale Blockpruefung
    (Daten 08:52).
  - Selbstanzeige 2 nennt das Lesen dieser Gewichte, aber nicht, dass schon Treffer mit beiden Gruppen darin lagen
    (Befund B2).
  - Nebenbefund: Den K5-Treffer mit 4/4 fand die Suche von QCA-DIRAC-T-1. Das bestaetigt Selbstanzeige 7 ("Suche in K5
    unvollstaendig").
- **Entartung an H, P, P': erzwungen; Kegel dort nur generisch (Frage 5).**
  - Diese Punkte sind modulo dem reziproken Gitter T-invariant. Beispiel: C3 bildet H = √3π(1, 0, 0) auf √3π(0, 1, 0) ab.
    Die Differenz ist G = √3π(1, −1, 0) mit G·h_a ∈ {0, 2π, −2π, 0}.
  - Also vertauscht W(H) mit V, und es gilt dieselbe Schur-Rechnung wie bei k = 0.

## Frage 3: Inversion und Rueckspruenge, QCA-DIRAC-T-1

**Urteil:** Inversion erzwingt die Matrix-Lesart (die Bedingung der Quelle), nicht aber die Block-Lesart. Die massiven
Form-P-Treffer von QCA-DIRAC-T-1 erfuellen nach den Daten trotzdem auch die Block-Lesart: unzerlegbar, alle acht Spruenge
gleich stark. "Masse mit Rueckspruengen" ist dort also schon gezeigt (unter T mit Inversion, K4). QCA-DIRAC-RUECK-1 ist in
der geplanten Form ueberfluessig.

- **Matrix-Lesart: ja, von selbst [M].**
  - Aus V(Π) A_h V(Π)^† = A_{−h} folgt ||A_{−h}|| = ||A_h||, also a_+ = a_−.
  - Jeder inversionskovariante Automat mit irgendeinem Sprung hat damit alle acht Spruenge gleich stark. Das ist die
    Bedingung der Quelle (2017: "we will assume A_h ≠ 0 for all h ∈ S+ ∪ S−" [S]).
- **Block-Lesart: nein [M], Gegenbeispiel:**
  - W(k) = C·S_+(k) ⊕ C·S_−(k) auf K4 = (2+2') ⊕ (2+2') mit V(Π) = Kopientausch (die Form P von QCA-DIRAC-T-1).
  - Wegen S_+(−k) = S_−(k) gilt V(Π)W(k)V(Π)^† = C·S_−(k) ⊕ C·S_+(k) = W(−k); V(Π) vertauscht mit V(g) ⊕ V(g).
  - Der Automat ist unitaer, T- und inversionskovariant, zerfaellt aber in zwei Einbahn-Bloecke. Die Inversion
    vertauscht nur die Bloecke (das ist "K4 direkte Summe (X = I)" mit C_1 = C_2).
  - Die Vermutung in RUNDE-39.md Zeile 297 ("Inversion koennte Rueckspruenge von selbst erzwingen") stimmt also fuer die
    Matrix-Lesart und nicht fuer die Block-Lesart.
- **Daten QCA-DIRAC-T-1, haupt_BOP.json, Fall B|P|K4 (jq) [S]:**
  - 27 Treffer, davon 17 massiv und 10 trivial.
  - Alle 17 massiven haben gleiche Gewichte S+ und S− (bis auf etwa 1e−15 relativ). J_+ = J_− betraegt siebenmal etwa 4,
    sonst 3,911; 3,52; 3,49; 3,316; 1,43; 0,886; 0,69; 0,0019; 1,1e−6 und 9,2e−10.
  - C2x-Implementierer:
    - 15 eindeutig mit deutlichem Abstand (Nullraum 1, zweiter Singulaerwert 0,025 bis 1,05)
    - einer knapp (7e−4, Sprunggewicht 1,1e−6)
    - einer mehrdeutig (Sprunggewicht 9,2e−10)
    - Alle eindeutigen wirken projektiv.
  - Daraus [M, Schluss aus Frage 2]: Bei Nullraum 1 ist der Kommutant 1, also gibt es einen einzigen Block mit allen
    acht Spruengen gleich stark. Die Block-Lesart ist erfuellt (Normverhaeltnis 1, weit ueber der Mindestnorm 1e−3).
  - Isotrop: drei mit nennenswertem Sprung (J_± = 3,49; 3,911; 0,69; Kruemmungsstreuung 3,0e−7 bis 3,9e−6), dazu der fast
    triviale (Streuung 3,1e−4). Alle vier sind auch an H, P und P' quadratisch (spezialpunkte: je vier Cluster
    "quadratisch").
- **Konstruktionen (haupt_0.json, teil0) [S]:**
  - a_spiegel und b_muenze_verschiebung bei m = 0,1; 0,3; 0,6 sind massiv; der C2x-Nullraum ist 1, s_2 = 0,2 bis 0,92
    bzw. 0,14 bis 0,85; die Wirkung ist projektiv.
  - (a) E = ((nA, imI), (imI, nA^†)) springt oben mit nA nur in S_+ und unten mit nA^† nur in S_−, denn
    (Σ A_h e^{−ik·h})^† = Σ A_h^† e^{−ik·(−h)}. Der Massenterm koppelt die beiden Teile.
  - (b) ist genau die Bauart R3 von QCA-BCC-RUECK-1: Die Muenze N ⊗ C mischt die Sektoren. (b) ist massiv, weil die
    Eigenvektoren von N ausgeglichen sind.
  - Bei m = 0 zerfallen beide Konstruktionen in zwei Bloecke [M].
- **Folge:**
  - "Masse mit Rueckspruengen" ist in QCA-DIRAC-T-1 gezeigt: exakt durch (a) und (b) und in der Suche (16 unzerlegbare
    massive Form-P-Treffer, drei davon isotrop und an H, P, P' ohne Kegel).
  - Die Frage der Ernte an QCA-DIRAC-RUECK-1 ("Masse (mit Inversion) und Luecken an den Verdopplern bei Rueckspruengen?")
    ist damit beantwortet: ja, und fuer die vier isotropen Treffer ja. 13 der 17 behalten Kegel an P und P'
    (QCA-DIRAC-T-1 ERGEBNIS, Grenzen).
- **Grenzen meines Schlusses:**
  - Die Blockpruefung der BCC-RUECK-Auswertung lief nicht auf diesen Treffern; die Matrizen stehen nicht in den
    JSON-Dateien. Mein Schluss geht ueber den Nullraum des Implementierers, das ist dieselbe Groesse.
  - Wirklich offen bleibt nur eine andere Frage: Gibt es massive T-Automaten mit Rueckspruengen ohne Inversion?
    Generisch nicht (c = 0 auf vier Clustern), ausgeschlossen ist es nicht [H].

## Frage 4: Direkte Summe

**Urteil:** Die Block-Lesart ist sauber definiert und richtig angewandt. Die 17 Treffer sind keine direkten Summen; die
Muenze bzw. der allgemeinere Kopplungsterm koppelt Vorwaerts- und Rueckwaertsteil wirklich.

- **Definition [M, code/qca_rueck.py Zeilen 548 bis 615 gelesen]:**
  - Die Bloecke kommen aus dem Kommutanten der *-Algebra aller A (mit A_0 und den Adjungierten), Toleranz 1e−8.
  - Bei nichtkommutativem Kommutanten (gleiche Bloecke mehrfach) ist die Zerlegung nicht eindeutig. Gleiche Bloecke
    haben aber dasselbe Sprungmuster, das Urteil haengt also nicht von der Wahl ab.
  - Fuer unitaere Automaten ist der Kommutant der A_h gleich dem der *-Algebra (Frage 2).
- **Daten, alle 17 Rueck-Treffer (jq, haupt_8Na/8Oa/8Ob) [S]:**
  - kommutant_dim = 1, Abstand des naechsten Singulaerwerts 0,27 bis 1,48. Das liegt weit ueber der Toleranz 1e−8,
    die Treffer sind also robust unzerlegbar.
  - Ein Block mit dim 8; alle acht Spruenge gleich stark (norm_verh 1); J_+ = J_−.
  - Zum Vergleich: "K4 direkte Summe" hat Kommutant 2 (ERGEBNIS, Teil 0).
- **Gegenprobe gegen eine verkleidete Summe [ES]:**
  - Eine k-abhaengige Umbasierung erhaelt das Spektrum.
  - Einbahn-Automaten auf 2+2' in Form N haben Kegel mit v = 1/3 (QCA-DIRAC-T-1 Suchkontrolle: 15 von 40, v = 1/3
    ± 8e−7).
  - Die neun Form-N-Treffer haben Kegel mit v ≠ 1/3 (0,0087 bis 0,3696). Sie sind also nicht einmal spektral eine
    Summe von Form-N-Einbahnbloecken. Fuer Form O gilt dieser Schluss nicht, weil Einbahnbloecke mit A_0 andere v haben
    koennen.
- **Schwaeche (C):**
  - Bei trivialen Treffern mit Restspruengen um 3,4e−8 meldet der Blocktest Kommutant 1 bei einem Abstand von nur
    6,2e−8, also knapp ueber der Toleranz (Beispiel 8|K1|O|frei #0).
  - Dazu stehen rueck_block = true und rueck_matrix = true, weil die Mindestnorm relativ ist.
  - Fuer die Urteile ist das harmlos, weil das Trivialfilter (Sprunggewicht ≥ 1e−10) diese Treffer aussortiert. Es
    sollte aber im Text stehen.
- **"Muenze":** Die Treffer koppeln wirklich, sind aber nicht alle "Muenze mal Verschiebung". v = 0,3696 > 1/3 geht
  mit der Bauart R3 in K4 nicht (ERGEBNIS rechnet v = ||a|² − |b|²|/3 ≤ 1/3; das habe ich nachvollzogen [M]: W(0)^†∂W =
  ∂S_+ ⊕ ∂S_−, c_− = −c_+ auf der 2-Kopie). Auch eine Muenze auf beiden Seiten aendert die Schranke nicht.

## Frage 5: Verdoppler

**Urteil:** Erzwungen ist die Entartung an H, P, P'. Dass dort Kegel sitzen, ist eine Eigenschaft dieser Loesungen
(generisch), kein Satz. Nielsen/Ninomiya uebertraegt sich nicht eins zu eins auf Automaten.

- **Erzwungen [M]:**
  - H, P, P' sind T-invariant modulo dem reziproken Gitter (Frage 2). Deshalb vertauscht W dort mit V, und bei
    spinoriellem V ist jeder Eigenwert mindestens zweifach.
  - Bei K4 gibt es je Punkt vier Zweifach-Cluster.
- **Nicht erzwungen [S, Daten]:**
  - Die erste Ordnung dort ist wieder c'·(k − k*)·σ, und c' = 0 ist erlaubt.
  - Belege: Die drei isotropen massiven Form-P-Treffer von QCA-DIRAC-T-1 (mit Rueckspruengen, Frage 3) sind an H, P und
    P' quadratisch. Der L_2-Dirac-Automat der Quelle hat gegappte Verdoppler (QCA-DIRAC-T-1 ERGEBNIS, Kontrollen).
  - Ein masseloser Treffer ohne Kegel an H, P, P' ist damit nicht gezeigt; ausgeschlossen ist er aber auch nicht.
- **Topologie [M, eigener Schluss, nicht gegengelesen]:**
  - Fuer hermitesche Gitter-Hamiltonoperatoren summieren die Chiralitaeten zwischen je zwei benachbarten Baendern zu
    null (Nielsen/Ninomiya [L]).
  - Bei unitaeren W(k) liegen die Quasienergien auf einem Kreis, es gibt kein unterstes Band. Das Argument ueber
    Chern-Zahlen auf Schnitten gibt nur: Die Netto-Chiralitaet ist in jeder Luecke gleich, aber nicht unbedingt null
    ("anomale" Floquet-Faelle [L?]).
  - Fuer die 17 Treffer heben sich die vier Kegel bei k = 0 paarweise auf (Vorzeichen +, +, −, −; chiral_det
    z. B. ±0,0234, ±6,6e−7). Dann muessen nach diesem Argument irgendwo weitere Weyl-Punkte liegen, aber nicht zwingend
    an H, P, P'.
- **Vorschlag:** "Verdoppler an H, P und P'" als Befund der Treffer stehen lassen, mit dem Zusatz "Entartung dort durch
  T erzwungen, Kegel generisch; mit Inversion gibt es Treffer ohne Kegel an H, P, P' (QCA-DIRAC-T-1)".

## Frage 6: Texte der Leitung Satz fuer Satz

**Urteil:** Die Zahlen stimmen alle. Zu stark oder falsch sind vier Aussagen: "nur QR0 vorab ableitbar", "erst ab 8
inneren Zustaenden", "Bau: Vorwaerts + Rueckwaerts + Muenze" als Beschreibung der Treffer und "Masse mit Rueckspruengen
offen". Dazu kommen fehlende Ableitbarkeitsvermerke.

Ernte "QCA-BCC-RUECK-1" (RUNDE-39.md Zeilen 227 bis 261):

| Nr | Satz (gekuerzt) | Pruefung | Befund |
|---|---|---|---|
| E1 | Spuren, fertig 10:24:18, gegengelesen an auswertung.json | ERGEBNIS Selbstanzeige 14: 10:24:18 | stimmt |
| E2 | QR0, QR1, QR2 eingetroffen, auch nach Kartenwortlaut | auswertung.json: drei "eingetroffen", Matrix-Vermerke eingetroffen | stimmt |
| E3 | "4 Zustaende unter T: kein Automat mit Rueckspruengen." | Ueberschrift ohne Kennzeichen; erst der Unterpunkt schraenkt ein | B1 |
| E4 | zehn Klassen, 3200 Starts, 353 Treffer, 116 einseitig, 237 trivial | 10·2·4·40 = 3200; N frei 19+22+17+14 = 72, O frei 281 (1-dim Summen 183, Rest 98), 72 + 281 = 353; einseitig 72 + 16+13+8+7 = 116; 353 − 116 = 237 | stimmt |
| E5 | erzwungener Anteil: kein Treffer, Minimum 1,16e−4 | ERGEBNIS Teil 4 | stimmt |
| E6 | "Bewiesen ist nur ein Teil (Vorwaerts- und Rueckwaerts-Darstellung getrennt unmoeglich)" | inhaltlich richtig (Frage 1), aber unklar formuliert, und der Teil ist klein (zwei Eckpunkte) | B1 |
| E7 | "8 Zustaende unter T: ja. Ein Teil springt vorwaerts, einer rueckwaerts, eine Muenze schaltet um." | beschreibt die Konstruktion R3, nicht die Treffer; v = 0,3696 > 1/3 ist mit R3 in K4 unmoeglich (ERGEBNIS, Selbstanzeige 12 hat genau das berichtigt) | **A2** |
| E8 | 17 Automaten (2+2+2'+2'), je vier Weyl-Kegel, v = 0,007 bis 0,37, erste Ordnung isotrop | auswertung.json v_rueck_kegel 0,00696 bis 0,36959; 7+2+3+5 = 17 (jq) | stimmt; Ableitbarkeit fehlt (B2) |
| E9 | "12 von 17 haben einen Kegel ... (bester: alle vier bei 2e-4 bis 2,1e-3)" | n_kandidaten 12; kleinster Wert 2,488e−4 | "mindestens einen", "2,5e−4" (C1) |
| E10 | "360 Grad = -1 in allen 17." | richtig, aber durch die gewaehlte Spinordarstellung vorgegeben | B2 |
| E11 | "Keine Masse." | stimmt fuer die 17 (ohne Inversion) | C2 |
| E12 | "Verdoppler an H, P und P' (je vier Kegel)." | jq: alle 17 je vier lineare Cluster an H, P, P' | stimmt; C3 |
| E13 | K5: Suche unvollstaendig | stimmt; QCA-DIRAC-T-1 fand einen K5-Treffer mit 4/4 | C4 |
| E14 | Kontrolle 20 von 40, v = 1/√3 | 0,577350 = 1/√3 | stimmt |
| E15 | Literatur: nur s = 2, Rueckspruenge in der Definition, "eine Dreierdrehung ist bei 2 Zustaenden ausgeschlossen" | Quelle: "The case K ≅ Z3 is not consistent with Eqs. (17) and (18)" (Untergruppe K, unter ihren Bedingungen) | C5 |
| E16 | "Damit ist nur QR0 vorab ableitbar." | falsch: ERGEBNIS nennt QR2 am Schreibtisch ableitbar (bis auf 0,05), und QR2 lag in den Daten von QCA-DIRAC-T-1 vor (Frage 2) | **A1** |
| E17 | Kartenluecke direkte Summe | stimmt | stimmt |
| E18 | Selbstanzeigen | stimmen; es fehlt, dass die Gewichte aus QCA-DIRAC-T-1 schon Treffer mit beiden Gruppen zeigten | B2 |
| E19 | "traegt das BCC-Netz masselose Spin-1/2-Teilchen erst ab 8 inneren Zustaenden, mit Verdopplern" | "erst ab 8" nicht gezeigt (4 nur Suche und Sonderfall, 6 gar nicht untersucht; frueherer Gegenleser A5); "masselos" nur ohne Inversion | **A3** |
| E20 | "Gegenleser-Befund A4 ist damit beantwortet: Mit doppelter Ausstattung geht es auch nach den Regeln der Quelle." | gemeint ist die Rueckspruung-Bedingung der Quelle; die Quelle selbst rechnet nur s = 2 | C6 |
| E21 | "Folge QCA-DIRAC-RUECK-1: Masse (mit Inversion) und Luecken an den Verdopplern bei Rueckspruengen?" | in den Daten von QCA-DIRAC-T-1 beantwortet (Frage 3) | **A4** |

Nachtrag 10:26:59 (RUNDE-39/WEICHE-STAND-v2.md):

| Nr | Satz (gekuerzt) | Pruefung | Befund |
|---|---|---|---|
| W1 | Kennzeichen "[M, Teilbeweis nicht gegengelesen]" | jetzt gegengelesen | C7 |
| W2 | "mit 4 Zustaenden keinen Automaten (Suche plus Teilbeweis)" | "gibt es keinen" ist eine Existenzaussage; gezeigt ist "keinen gefunden" plus Sonderfall | B1 |
| W3 | "mit 8 Zustaenden ja: vier masselose Weyl-Kegel, in erster Ordnung isotrop, 360 Grad = -1, Verdoppler an H, P und P'" | Zahlen stimmen; liest sich als Eigenschaft aller 8-Zustands-Automaten mit Rueckspruengen; "masselos" gilt nur ohne Inversion; isotrop in erster Ordnung und 360 Grad sind vorab ableitbar | B2, zusammen mit A4 |
| W4 | "Bau: Vorwaertsteil + Rueckwaertsteil + Muenze." | wie E7 | **A2** |
| W5 | "Masse mit Rueckspruengen offen (QCA-DIRAC-RUECK-1)." | falsch nach den Daten von QCA-DIRAC-T-1 (Frage 3) | **A4** |

## Befunde A/B/C

### A (falsch oder zu stark, muss geaendert werden)

- **A1, "nur QR0 vorab ableitbar" (E16).**
  - Fundstelle: RUNDE-39.md, Ernte QCA-BCC-RUECK-1, Punkt "Literatur", letzter Satz "Damit ist nur QR0 vorab ableitbar."
  - Grund: Bezogen auf die Literatur allein ist der Satz richtig (ERGEBNIS Punkt 5: "QR1 und QR2 sind nicht aus ihr
    ableitbar"). Als Urteil ueber die Vorhersagen ist er falsch, und so liest ihn Finn: ERGEBNIS sagt "QR2 am
    Schreibtisch bis auf die Isotropie bei |k| = 0,05" (Art des Ergebnisses; Selbstanzeige 1). QR2 lag ausserdem in den
    Daten von QCA-DIRAC-T-1 vor (Frage 2).
  - Vorschlag: "Aus der Literatur ist nur QR0 ableitbar. QR2 war bis auf die Isotropie bei abs(k) = 0,05 am Schreibtisch
    ableitbar (Schur bei k = 0, Konstruktion R3) und lag in den Daten von QCA-DIRAC-T-1 schon vor (8-Zustands-Treffer mit
    Spruengen in beide Richtungsgruppen, unzerlegbar, vier Kegel). Offen war nur QR1."
- **A2, Bauart als Beschreibung der Treffer (E7, W4).**
  - Fundstellen: RUNDE-39.md, Ernte, "8 Zustaende unter T: ja. Ein Teil springt vorwaerts, einer rueckwaerts, eine Muenze
    schaltet um."; WEICHE-STAND-v2.md, Nachtrag 10:26:59, "Bau: Vorwaertsteil + Rueckwaertsteil + Muenze."
  - Grund: Das ist die Konstruktion R3. In K4 erlaubt sie v ≤ 1/3; der beste Treffer hat v = 0,3696. ERGEBNIS hat
    "alle Suchtreffer sind Muenze mal Verschiebung" selbst berichtigt (Selbstanzeige 12).
  - Vorschlag Ernte: "8 Zustaende unter T: ja. Eine Bauart ist bekannt: Vorwaertsteil, Rueckwaertsteil und eine Muenze,
    die umschaltet (wie Konstruktion (b) in QCA-DIRAC-T-1). Die 17 Suchtreffer sind teils allgemeiner (v bis 0,37, die
    Bauart erlaubt in dieser Klasse hoechstens 1/3)."
  - Vorschlag Weiche: "Eine Bauart: Vorwaertsteil + Rueckwaertsteil + Muenze; die gefundenen Automaten sind teils
    allgemeiner."
- **A3, "erst ab 8 inneren Zustaenden" (E19).**
  - Fundstellen: RUNDE-39.md, Ernte, "Bedeutung [G/H]", erster Punkt. Gleich zu stark in ERGEBNIS, "Bedeutung fuer Finns
    Bild", dritter Punkt ("braucht ein Fermion (im Modell) 8 innere Zustaende").
  - Grund: Bei 4 gibt es nur die Suche und einen Sonderfallbeweis, 6 Zustaende (z. B. 2+2'+2'') sind gar nicht
    untersucht. Der fruehere Gegenleser hat "8 Zustaende" als Minimum schon zurueckgewiesen (qca-gegenlesen, A5).
    "masselos" gilt nur ohne Inversion.
  - Vorschlag: "Mit voller Tetraeder-Symmetrie und Rueckspruengen fand die Suche mit 4 inneren Zustaenden keine Loesung
    (bewiesen nur ein Sonderfall); mit 8 Zustaenden (2+2+2'+2') gibt es Loesungen. 6 Zustaende sind nicht untersucht;
    dass 8 das Minimum ist, ist nicht gezeigt. Ohne Inversion fand die Suche nur masselose Weyl-Kegel, deren zwei
    Zustaende sich unter den Tetraederdrehungen wie Spin 1/2 transformieren (durch die gewaehlte Darstellung vorgegeben),
    mit weiteren Kegeln an H, P und P'. Mit Inversion gibt es auch massive Loesungen mit Rueckspruengen (QCA-DIRAC-T-1,
    Form P)."
- **A4, "Masse mit Rueckspruengen offen" (W5, E21).**
  - Fundstellen: WEICHE-STAND-v2.md, Nachtrag 10:26:59, letzter Satz; RUNDE-39.md, Ernte, "Abschaetzung: ... Folge
    QCA-DIRAC-RUECK-1: Masse (mit Inversion) und Luecken an den Verdopplern bei Rueckspruengen?"
  - Grund (Frage 3, jq auf haupt_BOP.json und haupt_0.json):
    - Die Konstruktionen (a) und (b) und 16 massive Form-P-Treffer springen in beide Gruppen gleich stark.
    - Sie sind unzerlegbar (C2x-Nullraum 1).
    - Drei sind isotrop und an H, P, P' quadratisch.
  - Vorschlag Weiche: "Masse mit Rueckspruengen zeigt schon QCA-DIRAC-T-1 (mit Inversion): Die Konstruktionen (a) und (b)
    und 16 massive Suchtreffer springen in beide Richtungsgruppen gleich stark und sind unzerlegbar; drei davon sind
    isotrop und haben an H, P und P' keine Kegel. Offen ist Masse ohne Inversion."
  - Vorschlag Ernte: "Folge: Eine Karte QCA-DIRAC-RUECK-1 ist nicht noetig; die Frage beantworten die Daten von
    QCA-DIRAC-T-1 (QCA-GEGENLESEN-2, Frage 3)."

### B (sollte geaendert werden)

- **B1, Existenz bei 4 Zustaenden (E3, E6, W2).**
  - Vorschlag E3: "4 Zustaende unter T: kein Automat mit Rueckspruengen gefunden (3200 Starts; bewiesen nur ein
    Sonderfall)."
  - Vorschlag E6: "Bewiesen ist nur ein Sonderfall: Vorwaertsspruenge nur auf dem einen, Rueckwaertsspruenge nur auf dem
    anderen irreduziblen Summanden geht nicht. Alle Mischfaelle stuetzen sich auf die Suche."
  - Vorschlag W2: "mit 4 Zustaenden fand die Suche keinen (3200 Starts; bewiesen ist nur der Sonderfall getrennter
    Summanden)".
- **B2, Ableitbarkeit fehlt (E8, E10, E18, W3).**
  - Vorschlag nach E10: "Vorab ableitbar waren die Entartung und die vier Zweifach-Cluster bei k = 0, die Isotropie in
    erster Ordnung (Schur), 360 Grad = −1 (gewaehlte Spinordarstellung) und die Entartung an H, P, P'. Neu sind nur die
    Isotropie bei abs(k) = 0,05, die Trefferzahlen und die Blockpruefung."
  - Zusatz zu E18: "Die Daten von QCA-DIRAC-T-1 enthielten schon 16 unzerlegbare 8-Zustands-Treffer mit Spruengen in
    beide Gruppen (10 in Form N, 5 in Form O, einer in K5)."
  - Vorschlag W3: "mit 8 Zustaenden ja (17 Suchtreffer in 2+2+2'+2', ohne Inversion): vier masselose Weyl-Kegel, in
    erster Ordnung isotrop und 360 Grad = −1 (beides durch die Symmetrie bzw. die gewaehlte Darstellung vorgegeben),
    Kegel auch an H, P und P'."
- **B3, "Masse gibt es ohne Inversion keine" (ERGEBNIS, Ergebnis zuerst 2; Datei des Code-Agenten).**
  - Vorschlag: "Ohne Inversion fand die Suche keine Masse. Unter T allein ist das generisch, aber nicht erzwungen: Die
    R3-Familie hat bei ausgeglichenen Eigenvektoren massive Glieder (z. B. QCA-DIRAC-T-1 Konstruktion (b), die
    allerdings eine Inversion hat)."
- **B4, R4 Schritt "Frequenz h_a + h_b" (PLAN.md Abschnitt 3; ERGEBNIS R4).**
  - Vorschlag (Zusatzsatz): "Zur Frequenz h_a + h_b = −(h_c + h_d) tragen auch P_d^†M_c + P_c^†M_d bei; bei
    Sektortrennung liegen diese in Hom(2' → 2) und verschwinden getrennt von M_b^†P_a + M_a^†P_b. Dasselbe gilt mit
    Vor-Ort-Term."
- **B5, Vorschlag "Rueck-Treffer mit Inversion" (ERGEBNIS, Bedeutung, letzter Punkt).**
  - Vorschlag: "Die Form-P-Treffer von QCA-DIRAC-T-1 tragen schon Masse mit Rueckspruengen (QCA-GEGENLESEN-2, Frage 3).
    Offen bleibt, ob J_+ = J_− unter T ohne Inversion erzwungen ist."

### C (kann)

- C1 (E9): "mindestens einen Kegel"; "2,5e−4 bis 2,1e−3".
- C2 (E11): "Keine Masse (ohne Inversion; mit Inversion siehe QCA-DIRAC-T-1)."
- C3 (E12): "(Entartung dort durch T erzwungen, Kegel generisch)".
- C4 (E13): "QCA-DIRAC-T-1 fand in K5 einen Treffer mit Spruengen in beide Gruppen (4/4)."
- C5 (E15): "eine Untergruppe K ≅ Z_3 der Isotropiegruppe ist bei 2 Zustaenden mit ihren Unitaritaetsbedingungen
  ausgeschlossen (Eqs. 17, 18)".
- C6 (E20): "nach der Rueckspruung-Bedingung der Quelle" statt "nach den Regeln der Quelle".
- C7 (W1): Kennzeichen "[G; Teilbeweis gegengelesen: richtig, deckt nur einen Sonderfall]".
- C8 (ERGEBNIS, Kontrollen): Bei trivialen Treffern ist der Blocktest knapp (Abstand 6,2e−8 bei Toleranz 1e−8), und
  rueck_block steht formal auf true. Das sollte als Hinweis stehen; sortiert werden diese Treffer durch das Trivialfilter.

## Ableitbarkeitstabelle

| Eigenschaft | vorab ableitbar | Begruendung |
|---|---|---|
| QR0: L_2-Weyl mit Rueckspruengen gefunden, r20 leer | ja | Prop. 5c der Quelle 2017 (laut ERGEBNIS [S]) |
| QR1: 4 Zustaende ohne Automat mit Rueckspruengen | teilweise | R4 schliesst nur die Sektortrennung aus (zwei Eckpunkte); alles andere traegt die Suche |
| Existenz eines 8-Zustands-Automaten mit Rueckspruengen | ja | Konstruktion R3; ausserdem 16 unzerlegbare Treffer mit beiden Gruppen in QCA-DIRAC-T-1 lauf-69 und dessen Konstruktionen (a), (b) |
| nur Klasse K4 getroffen | nein | R3 geht in K4 und K5; dass nur K4 getroffen wurde, ist Suchstatistik (K5 existiert: Konstruktion, QCA-DIRAC-T-1) |
| Entartung bei k = 0 (Zweifach-Cluster) | ja | Schur: alle Spinor-Irreps von 2T sind zweidimensional |
| vier Cluster bei k = 0 | ja (generisch) | Kommutant M_2 ⊕ M_2 bei K4 |
| Kegel (lineare Aufspaltung) | teilweise | erste Ordnung c·k·σ; c ≠ 0 generisch, nicht erzwungen |
| isotrop in erster Ordnung | ja | Hom_T(3, End 2) eindimensional; einziger reeller T-invarianter symmetrischer Tensor auf 3 ist δ_ij |
| isotrop bei abs(k) = 0,05 | nein | T erlaubt b·Q·σ in zweiter Ordnung |
| v = 0,007 bis 0,37 | nein | Suchergebnis; R3 gibt in K4 nur v ≤ 1/3 |
| 360 Grad = −1 ueber die Darstellung | ja | Eingabe: V spinoriell gewaehlt |
| 360 Grad = −1 am Treffer | ja | folgt fuer unzerlegbare Treffer aus Kommutant 1 |
| masselos ohne Inversion | teilweise | generisch; Masse heisst c = 0 auf allen Clustern, nicht verboten |
| Masse mit Inversion und Rueckspruengen | ja | schon in QCA-DIRAC-T-1: Konstruktionen (a), (b), Form-P-Treffer |
| Matrix-Lesart bei Inversion | ja | ‖A_{−h}‖ = ‖A_h‖ |
| Block-Lesart bei Inversion | nein | Gegenbeispiel C·S_+ ⊕ C·S_− mit Kopientausch |
| Entartung an H, P, P' | ja | T-invariant modulo reziprokem Gitter, also wieder Schur |
| Kegel an H, P, P' (Verdoppler) | teilweise | generisch; mit Inversion gibt es Treffer ohne Kegel dort |
| J_+ = J_− | teilweise | mit Inversion ja (Normgleichheit); ohne Inversion nicht bewiesen (ERGEBNIS [H]); mein Versuch einer Ganzzahligkeit scheiterte (Frage 1) |

## Einfach gesagt

Die Rechnung des Code-Agenten ist sauber, aber vieles davon stand schon vorher fest. Dass es Regeln mit acht Zustaenden
gibt, die vorwaerts und rueckwaerts springen, sich nach einer vollen Drehung mit einem Minuszeichen melden und in erster
Naeherung in alle Richtungen gleich schnell sind, folgt aus der Symmetrie. Passende Loesungen lagen sogar schon in den
Daten der Vorgaengerkarte. Der Beweis fuer vier Zustaende ist richtig, deckt aber nur einen Sonderfall ab; der Rest
beruht auf 3200 erfolglosen Suchversuchen. Masse bei Spruengen in beide Richtungen hat die Vorgaengerkarte QCA-DIRAC-T-1
schon gezeigt, deshalb braucht es dafuer keine neue Karte. Vier Saetze der Leitung sind zu stark, vor allem "erst ab 8
Zustaenden" und "Masse mit Rueckspruengen offen".
