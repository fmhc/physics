Urteil: TRAGEN MIT EINSCHRAENKUNG (alle zwoelf geprueften Beweise und Herleitungen tragen, drei brauchen einen Zusatzschritt; zu stark gefasst sind: "Weyl-Kegel erzwungen" (nur nach der Klassifikation der Quelle), die Reichweite der Diamant-Aussage, die BCC-T-Loesung (ausserhalb der symmetrischen Nachbarschaft der Quelle), "Masse braucht Inversion" (gezeigt: Inversion reicht), "8 Zustaende" als Minimum (nicht bewiesen) und "Masse ohne Symmetriebruch" (masselose Verdoppler an P, P'); "Kramers-Weyl" ist nur eine Analogie, denn es gibt keine Zeitumkehr)

# QCA-GEGENLESEN: Gegenlesung der Beweise QCA-TETRA-1, QCA-DIAMANT-4, QCA-DIRAC-T-1

- Gegenleser: frischer Agent (keine der Karten geschrieben oder gerechnet), Auftraggeber Leitung claude-primary.
- Beginn: 2026-10-04 09:01:38 CEST (date).
- Auftrag: RUNDE-37/qca-gegenlesen/AUFTRAG.md, sha256 6e5395d432c84faed3f353f654424b754298a08b875767cf8e6723750f29ef10.
- Gelesen: AUFTRAG.md; je Karte KARTE.md, PLAN.md, ERGEBNIS.md ganz; lauf-69/auswertung.json je Ordner (jq,
  Urteile und Stichproben); Quelle D'Ariano/Perinotti (lokale PDF, pdftotext nach stdout, Ausschnitte).
  - Nicht geoeffnet: Code, haupt_*.json, Rauchlaeufe und gesperrte Pfade.
- Abrufe: 2 WebFetch (arXiv-Abstracts 1708.00826 und 1611.07925). Ihr Wortlaut kommt aus der Wiedergabe des
  Werkzeugs; Fundstellen im Text stammen nur aus selbst Gelesenem.

## 0. Eigene Nachrechnungen (Gruppentheorie)

Alles im Kopf, ohne Rechner; [M, Gegenleser].

1. **Charaktertafel 2T** (ω = e^{2πi/3}). Klassen nach SU(2)-Winkel θ: E (1), −E (1), θ = π (6), θ = 2π/3 um +ĥ (4),
   θ = 2π/3 um −ĥ (4), θ = 4π/3 um +ĥ (4), θ = 4π/3 um −ĥ (4); zusammen 24.
   - 1: (1, 1, 1, 1, 1, 1, 1); 1': (1, 1, 1, ω, ω², ω², ω); 1'': konjugiert; 3: (3, 3, −1, 0, 0, 0, 0)
   - 2: (2, −2, 0, 1, 1, −1, −1) aus 2cos(θ/2); 2' = 2⊗1': (2, −2, 0, ω, ω², −ω², −ω); 2'' konjugiert
   - Proben: ⟨2, 2⟩ = (4 + 4 + 16)/24 = 1; ⟨2, 2'⟩ = (8 + 8(ω + ω²))/24 = 0; Quadratsumme 1+1+1+9+4+4+4 = 24.
2. **Frobenius-Schur-Indikator:** fuer 2 gilt Σχ(g²) = 2 + 2 − 12 − 8 − 8 = −24, also ν = −1 (pseudoreell); fuer 2'
   gilt 2 + 2 − 12 − 8(ω + ω²) = 0, also ν = 0 (komplex, Partner 2'').
3. **Spin 3/2 auf 2T:** sin(2θ)/sin(θ/2) gibt (4, −4, 0, −1, −1, 1, 1) = 2' + 2''. Spin 1 gibt 3, Spin 0 + Spin 1 =
   2⊗2 = 1 + 3 (Permutationsdarstellung der vier Striche).
4. **Induktion aus Z_6** (Urbild von C_3, Erzeuger g mit Eigenwerten e^{∓iπ/3} auf 2): 2 ⊃ χ_1, χ_5; 2' ⊃ χ_1, χ_3;
   2'' ⊃ χ_3, χ_5. Also Ind χ_1 = 2+2', Ind χ_3 = 2'+2'', Ind χ_5 = 2+2''; 2+2 ist nicht monomial bezueglich der
   Striche.
5. **Schur fuer den Massenterm:** Ein k-unabhaengiger Term M mit VM = MV bildet 2' nach 2 nur ueber
   Hom_2T(2', 2) = 0 ab. Bei 2+2 ist Hom(2, 2) = C, eine Kopplung waere erlaubt.
6. **Kramers fuer unitaere Schritte:** Gibt es ein antiunitaeres Θ mit Θ² = −1 und ΘW(k)Θ^(−1) = W(−k)^†, dann folgt
   an k ≡ −k aus Wψ = λψ (|λ| = 1) auch W(Θψ) = λΘψ, und Θψ ⊥ ψ. Ein solches Θ, das mit V vertauscht, gibt es auf 2
   (ν = −1), aber nicht auf 2' allein (ν = 0). Ohne Θ kommt jede Zweifachentartung bei T-invarianten k aus Schur
   (Punkt 1), nicht aus Kramers.
7. **Frequenzen auf BCC (t_a ganzzahlig):** t_i − t_j vom Typ (±2,±2,0), zwoelf verschiedene; t_a + t_b vom Typ
   (±2,0,0) mit t_1 + t_2 = −(t_3 + t_4); 2t_a vom Typ (±2,±2,±2). Deshalb hat d = h_i − h_j zwei Beitraege, d = 2h_i
   einen, d = h_i + h_j vier.
8. **Q_8-Argument fuer "360 Grad = −1":** Schur-Multiplikator von Q_8 trivial; −1 ∈ [Q_8, Q_8]; daher wirkt −1 genau
   bei nichttrivialer Klasse der V_4-Darstellung als −I.

## 1. QCA-TETRA-1 (M1 bis M7)

Gelesen: KARTE.md, PLAN.md (ganz), ERGEBNIS.md (ganz); Quelle quelle/dariano-perinotti-2014-arXiv-1306.1934v2.pdf per
pdftotext nach stdout, nur Ausschnitte (Abschnitt IV um Eq. 17 bis 21, Eq. 45, Anfang Anhang A, Eq. A90, A99 bis A102).
Schwere: schwer = traegt die Aussage nicht; mittel = Aussage muss enger gefasst werden; leicht = Darstellung, Ergebnis
unberuehrt.

1. **M1 (T, linear): richtig.** Nachgerechnet mit ganzzahligen Vektoren t_a: die zwoelf Differenzen t_i − t_j sind vom
   Typ (±2,±2,0), die Summen t_a + t_b vom Typ (±2,0,0), die 2t_a vom Typ (±2,±2,±2). Fuer d = h_i − h_j gibt es genau
   die zwei Paare (h_i, h_j) und (−h_j, −h_i), also A^†A + B^†B = 0. Jede 1-dim Darstellung von A_4 faktorisiert ueber
   A_4/V_4 = Z_3, ist also auf V_4 trivial; damit gilt M1 fuer jede lineare 2-dim Darstellung (T hat nur 1, 1', 1'', 3),
   nicht nur fuer die vier gelisteten. Schwere: keine.
2. **M2 (T, Spinor): im Ergebnis richtig, Darstellungsluecke.** c*a = 0 und d*b = 0 aus d = 2h_i stimmen (2t_i kommt
   nur einmal vor). Der Satz "Summe zweier Rang-1-Terme mit verschiedenen Bildern" trifft aber nur die Faelle (a = d = 0)
   und (b = c = 0). In den Faellen (a = b = 0) und (c = d = 0) ist ein Term null und der andere ein Produkt zweier
   moeglicherweise invertierbarer Matrizen; man braucht einen Zusatzschritt (invertierbar ⇒ Produkt ≠ 0, also einer der
   Koeffizienten 0, dann Ueberlapp |⟨±n_i|±n_j⟩|² = (1 + n_i·n_j)/2 = (1 − 1/3)/2 = 1/3 ≠ 0). Fundstelle PLAN.md
   Abschnitt 2, M2. Schwere: leicht.
3. **Vollstaendigkeit der Darstellungsliste: gegeben, aber nicht begruendet.** Der Schur-Multiplikator von A_4 und von
   V_4 ist je Z_2. Damit sind die 2-dim (projektiven) Klassen genau: fuer T Summen von 1-dim Charakteren oder 2, 2', 2''
   (Doppelgruppe 2T, 1+1+1+9+4+4+4 = 24); fuer V_4 Summen von Charakteren oder Pauli. Eine reduzible 2-dim Darstellung
   mit nichttrivialer Klasse gibt es nicht (1-dim projektive Darstellungen haben triviale Klasse). Der Plan listet das
   richtig, sagt aber nicht, warum die Liste vollstaendig ist. Schwere: leicht.
4. **M3 (L_2, linear): richtig.** Jede lineare 2-dim Darstellung wirkt in der Konjugation ueber einen
   Quotientencharakter χ_a·χ_b^(−1); jeder Charakter von V_4 ist auf mindestens einer C2 trivial, diese C2 tauscht h_1
   mit einem h_j und −h_1 mit −h_j; weiter wie M1. Schwere: keine.
5. **"Erzwingen einen Weyl-Kegel": nicht eigener Beweis, sondern Quelle plus Suche.** Eigener Beweis ist nur "lineare
   Klassen scheitern" (M1 bis M3). Dass jede Pauli-kovariante Loesung ein Weyl-Automat ist (linear, isotrop, c = 1/√3),
   steht in der Quelle ("the automata satisfying our principles are only four, modulo unitary conjugation", Abschnitt
   IV) und wird von 200 Starts (92 Treffer, zwei Spektralklassen) gestuetzt. Kurz selbst beweisbar ist nur die Lage:
   Bei irreduzibler Darstellung vertauscht Ã_0 mit allen U_l, nach Schur Ã_0 ∝ I, also Entartung bei k = 0 (so auch
   die Quelle: "In the case that U is irreducible, by Schur's lemmas we have only V = I_s"). Die Herleitung der Quelle
   (Anhang A) benutzt "Since the transition matrices A_hi are rank one"; deren Begruendung habe ich nicht geprueft.
   ERGEBNIS kennzeichnet das als [S, nachgerechnet], das ist redlich. Schwere: mittel fuer die Fassung im AUFTRAG
   ("erzwingen ... einen Weyl-Kegel"), dort fehlt "nach der Klassifikation der Quelle".
6. **"360 Grad = −1": richtig, aber nur als Z_2-Klasse.** Der Kommutator K = U_xU_yU_x^†U_y^† = −I ist phasenfrei.
   Zieht man die Darstellung auf das SU(2)-Urbild Q_8 von V_4 zurueck (Schur-Multiplikator von Q_8 trivial), wirkt −1
   als −I genau bei nichttrivialer Klasse, denn −1 liegt in [Q_8, Q_8] und alle 1-dim Charaktere von Q_8 sind dort 1.
   Gezeigt ist damit: Die zwei Zustaende transformieren unter den drei 180-Grad-Drehungen wie Spin 1/2 (halbzahlige
   Klasse). Eine SU(2)-Wirkung ("Spin 1/2" im vollen Sinn) gibt es erst langwellig ueber die Weyl-Gleichung, und die 120-
   Grad-Drehungen werden ausdruecklich nicht dargestellt. "Spin 1/2 ist auf BCC erzwungen" (ERGEBNIS, Ergebnis zuerst,
   Punkt 1) ist deshalb etwas zu stark. Schwere: leicht bis mittel (Formulierung).
7. **Stille Voraussetzungen der BCC-Aussage.** Gilt fuer: genau die 8 BCC-Spruenge, keine Selbstwechselwirkung (die
   Quelle zeigt A_e = 0 nur fuer ihre Loesungen, Eq. A90), Isotropiegruppen aus eigentlichen Drehungen, die S_+ erhalten
   (Spiegelungen und S_+ ↔ S_− vertauschende Drehungen sind nicht betrachtet, PLAN.md Abschnitt 1, Punkt 1). Jede
   Gruppe, die T enthaelt (O, T_d, T_h), ist durch M1/M2 mit ausgeschlossen. Schwere: leicht (gehoert in den Satz).
8. **M6 (Diamant, ein Schritt): richtig.** Die Differenzen e_b − e_a sind die zwoelf FCC-Nachbarvektoren, als Fourier-
   Moden unabhaengig; B_b^†B_a = 0 heisst orthogonale Bilder, in C² hoechstens zwei ≠ 0; eine transitive Gruppe erhaelt
   den Rang. Der Zusatz "mit Selbstwechselwirkung folgt dasselbe" ist zu knapp: Es bleibt die Loesung U = diag(P, Q)
   ohne jeden Sprung (aus P^†P = I folgt dann X = 0). Richtig ist "keine Loesung mit Spruengen". Schwere: leicht.
9. **M7 (Diamant, Zweischritt): richtig.** det W ist Einheit des Laurent-Rings, also Monom; ein Teiler einer Einheit ist
   Einheit. Fuer 2×2 gilt det(X+Y) = det X + det Y + tr(adj(X)Y); tr(adj(B_a)B_b) ist symmetrisch und
   konjugationsinvariant; V_4 hat auf den sechs Paaren drei Bahnen der Laenge 2, A_4 ist 2-fach transitiv (eine Bahn der
   Laenge 6). Kleinigkeit: B̂ selbst ist kein Laurent-Polynom in FCC-Variablen (e_a sind keine FCC-Vektoren), erst
   z_1^(−1)B̂; harmlos. Schwere: keine.
10. **Reichweite von "auf dem Diamantnetz mit 2 Zustaenden gibt es keinen": enger als formuliert.** In C-2 verlangt
    der Plan Isotropie je Halbschritt (B_{Ra} = V B_a V^†, C_{Ra} = V C_a V^†, PLAN.md Abschnitt 1, Punkt 5), nicht nur
    fuer den Zweischritt W. M7 braucht genau diese Halbschritt-Isotropie. Ohne sie gibt es unitaere Halbschritte mit
    monomialer Determinante (Beispiel B̂ = z_1P_0 + z_2P_1, det = z_1z_2). Ob ein nur im Ganzen isotroper Zweischritt
    oder ein Mehrschritt-Protokoll (Split-Step, je Teilschritt andere Striche) existiert, ist nicht gezeigt; ebenso
    nicht: weitere Spruenge (uebernaechste Nachbarn). Fuer die Kartenfrage (eine richtungsgleiche Regel je Schritt,
    C-1) ist die Aussage bewiesen. Schwere: mittel (Satz enger fassen).
11. **Numerik gegen Beweise:** Die Suchminima (6/7, 2/5, 2/45 bzw. 2/3) passen zu Nullbefunden, die Positivkontrolle
    (92 von 200) zeigt, dass die Suche Loesungen findet. Die Rechnung konnte die Beweise widerlegen und hat es nicht
    getan; vorab ableitbar war alles (ERGEBNIS sagt das selbst). Schwere: keine.

**Fazit 1:** Die Beweise M1 bis M3, M6, M7 tragen; M2 und M6 brauchen je einen Satz mehr. Ueberzogen sind "Spin 1/2
erzwungen" (gezeigt ist die halbzahlige Z_2-Klasse unter L_2) und "erzwingen einen Weyl-Kegel" (Klassifikation der
Quelle, nicht eigener Beweis). Die Diamant-Aussage gilt fuer richtungsgleiche Halbschritte.

## 2. QCA-DIAMANT-4

Gelesen: KARTE.md, PLAN.md (ganz), ERGEBNIS.md (ganz); Quelle Abschnitt II (Lokalitaet, Homogenitaet) per pdftotext.

1. **D2 (Fassung 1 nur bei monomialem V): richtig.** Aus Ŷ^†Ŷ = ŶŶ^† = I folgen B_b^†B_a = 0 und B_aB_b^† = 0
   (a ≠ b); die B_a sind partielle Isometrien mit orthogonalen Anfangsraeumen W_a, ⊕W_a = C^s; V(g)W_a = W_{ga} ist ein
   transitives Imprimitivitaetssystem, also V ≅ Ind_Stab(λ). Selbst nachgerechnet (Frobenius, Z_6 = Urbild von C_3 in
   2T, Erzeuger g mit g³ = −1): 2 enthaelt χ_1, χ_5; 2' enthaelt χ_1, χ_3; 2'' enthaelt χ_3, χ_5. Also Ind χ_1 = 2+2',
   Ind χ_3 = 2'+2'', Ind χ_5 = 2+2''; 2+2 ist kein induziertes Bild, also ausgeschlossen. Linear: Ind 1 = 1+3 usw.
   Schwere: keine.
2. **D3 (Normalform C_2 S(−k) C_1 S(k)): richtig.** U_0 = Σ_a B_a = Ŷ(0) liegt im Kommutanten, B_a = U_0 P_{W_a}. Der
   Schritt "T: |a⟩ ↦ |p_a⟩ vertauscht mit V" braucht, dass die Ind(λ) paarweise inaequivalent sind; das trifft fuer alle
   drei Faelle zu (oben). Umkehrung: V|a⟩⟨a|V^† = |ga⟩⟨ga|, also ist C·S(k) kovariant. Schwere: keine.
3. **D4 (erste Ordnung): richtig.** H_1 = K − C_1^†KC_1 stimmt; bei kommutativem Kommutanten ist C_1 auf jeder
   isotypischen Komponente skalar, also P_E H_1 P_E = 0. Grover-Fall nachgerechnet: ⟨s|K|s⟩ = 0 wegen Σe_a = 0,
   ‖K s‖² = (1/4)Σ(k·e_a)² = |k|²/3, Eigenwerte ±|e^{iψ} − 1|·|k|/√3 = ±2|sin(ψ/2)||k|/√3, 0, 0. P+P: K =
   (1/√3)Σ_j k_j σ_j⊗σ_j^T in der Bell-Basis geprueft (Vorzeichenmuster der t_a), d = (r(v) − r(c_1v))/√3, Partner −d.
   Schwere: keine.
4. **"Kegel unter T nur am abgestimmten Punkt": nur fuer k = 0 bewiesen.** Bei T (zwei Komponenten) heisst "Eigenwerte
   von W_0 auf zwei Komponenten fallen zusammen" genau W_0 ∝ I; das ist richtig als abgestimmter Punkt erkannt. Fuer
   Punkte ausserhalb von k = 0 gibt es nur Numerik an den ersten drei Treffern je Fall (13 bis 20 Entartungspunkte ohne
   Kegel, ERGEBNIS "Verdoppler und Linien"). Ausserdem gilt alles nur fuer Fassung 1/2 (unitaere Halbschritte);
   C-2 ist nicht gerechnet (PLAN.md 1.2). Schwere: leicht (Satz um "bei k = 0" und "Fassung 1" ergaenzen).
5. **Teil B, BCC-Loesungen liegen ausserhalb der Klasse der Quelle (neuer Befund).** Alle 165 Treffer haben "ihr ganzes
   Gewicht in S_+ oder ganz in S_−" (ERGEBNIS, Teil B, Bau der Treffer), also A_{−h} = 0 fuer alle h ∈ S_+. Die Quelle
   verlangt eine symmetrische Nachbarschaft, Abschnitt II, woertlich: "In the following we will focus on those automata
   for which, if the transition from g to g' is possible, then also that from g' to g is possible, namely if A_gg' ≠ 0
   then A_g'g ≠ 0." Der T-kovariante 4-Zustands-Automat ist damit ein gueltiger unitaerer Automat, aber kein Automat
   "im Sinn der Quelle", auf die sich Karte und Plan berufen (PLAN.md 0). Damit hinkt der Vergleich mit QCA-TETRA-1
   (dort ist T mit 2 Zustaenden in der Klasse der Quelle unmoeglich). Ob es T-kovariante 4-Zustands-Automaten mit
   symmetrischer Nachbarschaft gibt, ist offen; die Suche liess gemischte Gewichte zu und fand keine. Mathematisch ist
   C·diag(e^{ik·h_a}) genau ein Diamant-Halbschritt (D3 mit einem Schritt); der Unterschied "BCC traegt Fermionen,
   Diamant nicht" ist also eigentlich "Halbschritt ohne Rueckweg gegen Hin- und Rueckschritt". Fundstellen: ERGEBNIS
   "Ergebnis zuerst" Punkt 3 und "Bedeutung fuer Finns Bild" ("Das spricht im Modell fuer BCC als Fermionen-Netz").
   Schwere: mittel (Existenzaussage richtig, Einordnung und Deutung zu stark).
6. **Spurformel v = 1/3: richtig, aber nur fuer die Familie Muenze mal Verschiebung.** Nachgerechnet: ⟨a|P_2|a⟩ = 1/2
   (Spur 2 auf vier gleichwertige Diagonalplaetze), Σ_{b≠a}|⟨a|P_2|b⟩|² = 1/2 − 1/4 = 1/4, wegen C_3 je 1/12;
   Σ_{a≠b}(k·h_a)(k·h_b) = −Σ_a(k·h_a)², also tr = (1/4 − 1/12)(4/3)|k|² = (2/9)|k|², 2c² = 2/9, c = 1/3. Dass die
   erste Ordnung c·k·σ ist, folgt aus Hom_T(3, 3) = C (3 von A_4 absolut irreduzibel) und Hom_T(3, 1) = 0. Die
   Isotropie ist damit fuer jede T-kovariante Loesung mit einer 2-dim Komponente erzwungen, der Wert 1/3 aber nur fuer
   W = C·S_±(k); dass es nur diese Familie gibt, ist nicht bewiesen (ERGEBNIS sagt das selbst, "Nicht vorab
   bewiesen"). Ergaenzung des Gegenlesers [M]: Die entgegengesetzte Chiralitaet ist erzwungen. Der Spinvektor
   J = P_2σP_2 + P_2'σP_2' hat in |a⟩ einen C_3-invarianten Erwartungswert μh_a; die Komponenten von |a⟩ auf 2 und 2'
   haben unter dem Stabilisator verschiedene Spinor-Eigenwerte (auf 2' ist V = ω·V_2), zeigen also entgegengesetzt,
   μ = 0. Aus Σ_j tr(J_j K(e_j)) = 6(c + c') = 4μ folgt c' = −c. Schwere: leicht (Reichweite benennen).
7. **"Masse verboten": richtig, sogar allgemeiner als begruendet.** W(0) vertauscht mit V; Hom_2T(2', 2) = 0 (Schur),
   also W(0) = w P_2 + w' P_2'. Jede T-kovariante Regel auf 2+2' (gleich welche Spruenge, auch mit Selbstwechselwirkung)
   hat bei k = 0 und an allen T-invarianten Punkten (Γ, H, P, P') zwei erzwungene Zweifachentartungen; eine Luecke ist
   ausgeschlossen. Aber: Die beiden Weyl-Knoten liegen bei verschiedenen Eigenphasen (w ≠ w'); "Masse = Kopplung der
   beiden Weyl-Anteile" ist deshalb das falsche Bild. Richtig ist "die Zweifachentartung jeder Komponente ist
   symmetrieerzwungen". "Mit 2+2 ... fand die Suche keinen Automaten" ist nur Numerik (der Beweis waere S2 in
   QCA-DIRAC-T-1). Schwere: leicht (Formulierung).
8. **"Spin 3/2 auf T" = 2+2': in der Konjugation richtig, woertlich nicht.** Charakter von j = 3/2 auf 2T nachgerechnet
   (4, −4, 0, −1, −1, 1, 1 auf den Klassen 1, −1, Ordnung 4, zwei Klassen θ = 2π/3, zwei Klassen θ = 4π/3): das ist
   2'+2'', gleich (2+2')⊗1'. PLAN.md 1.3 sagt das richtig, ERGEBNIS Punkt 1 verkuerzt. Schwere: leicht.
9. **QD2 haengt an der Festlegung w0** (PLAN.md 1.5), offen angezeigt. Schwere: keine fuer die Beweise.

**Fazit 2:** D2 bis D4 tragen. Die Kernaussage "genau dann monomial" stimmt fuer unitaere Halbschritte, "Kegel unter T
nur am abgestimmten Punkt" stimmt bei k = 0. Die BCC-Aussage (zwei isotrope Weyl-Kegel, v = 1/3, keine Luecke) stimmt
fuer die gefundene Familie. Diese Familie verletzt aber die symmetrische Nachbarschaft der Quelle; die Deutung "BCC als
Fermionen-Netz" ist damit nicht gedeckt.

## 3. QCA-DIRAC-T-1 (S2)

Gelesen: KARTE.md, PLAN.md (ganz), ERGEBNIS.md (ganz); auswertung.json (Urteile, Konstruktion a_spiegel).

1. **S2 (keine Spruenge bei r Kopien derselben Spinor-Irrep): richtig und vollstaendig.** Selbst nachgerechnet mit
   A_{±h_i} = I⊗α^± + N_i⊗β^± (N_i = n_i·σ, Kommutant von U(C3)⊗I):
   - d = 2h_i (nur das Paar (h_i, −h_i)): gibt F1 und F2.
   - d = h_i − h_j: Koeffizienten von I, N_i, N_j, (n_i×n_j)·σ (linear unabhaengig) geben E1 (mit n_i·n_j = −1/3), E2
     und E4.
   - d = h_1 + h_2: Hier gibt es vier Paare, nicht zwei, denn h_1 + h_2 = −(h_3 + h_4). Mit F1/F2 bleibt
     −(8/3)·I⊗(β^{−†}β^+ + β^{+†}β^−) = 0, also G1. Der Plan nennt das nicht, das Ergebnis G1 stimmt.
   - Der Vor-Ort-Term traegt zu keiner dieser Frequenzen bei (er koppelt nur an d = ±h_i).
   - Fall P invertierbar: Linksmultiplikation mit I⊗T erhaelt Unitaritaet und Kovarianz; β^− = vp, aus G1 v^† = −v,
     aus der WW^†-Fassung [v, p] = 0. Aus E2 und F2 folgen zwei Ausdruecke fuer α^−, gleichgesetzt [v, α^+] = 0. Dann
     α^+p^(−1)α^+ = p, also ist Y = α^+p^(−1) eine Involution, und E1 wird p(Y^†Y + YY^†)p = (2/3)p².
   - Die Ungleichung Y^†Y + YY^† ≥ 2I belegt der Plan ueber 2×2-Bloecke. Dafuer braucht er stillschweigend die
     Normalform einer Involution unter unitaerer Aehnlichkeit. Kuerzer und luecklos geht es mit ⟨Y^†x, Yx⟩ = x^†Y²x =
     ‖x‖² und Cauchy-Schwarz: ‖Yx‖² + ‖Y^†x‖² ≥ 2‖Yx‖‖Y^†x‖ ≥ 2‖x‖².
   - Fall P singulaer: Abspaltung richtig. W(k) bildet C²⊗supp P in das konstante Komplement von W(C²⊗ker P) ab;
     nach einer konstanten Drehung I⊗τ bleibt ein Automat derselben Form mit invertierbarem P.
   - Schwere: leicht (zwei ausgelassene Zwischenschritte).
2. **"Unter T allein ist eine zweifache Bandkante generisch ein Kramers-Weyl-Kegel": Mathematik richtig, Name
   falsch.** Die erste Ordnung auf einer 2-dim Irrep ist c·k·σ (End(2) = 1 ⊕ 3 unter T, Hom_T(3, 1 ⊕ 3) ist
   eindimensional). c = 0 ist eine reelle Bedingung je Cluster; "generisch" ist ein Kodimensionsargument und wird von
   42 von 42 Treffern gestuetzt. Der Plan kennzeichnet es selbst als [H] (S4). Aber:
   - Kramers' Satz braucht eine antiunitaere Zeitumkehr Θ mit Θ² = −1. Fuer unitaere Schritte und ΘWΘ^(−1) = W^†
     gilt er auch hier, denn W(Θψ) = λΘψ und Θψ ⊥ ψ.
   - In keiner der drei Karten ist eine Zeitumkehr verlangt oder geprueft. Die Zweifachentartung kommt aus den
     2-dim Irreps der Doppelgruppe 2T (Schur), nicht aus Kramers.
   - Mit Zeitumkehr wuerde sich das Bild sogar aendern: 2 ist pseudoreell und bliebe ein Kramers-Paar; 2' und 2''
     sind zueinander komplex konjugiert und wuerden zu einem 4-dim Block verklebt. Die Zerlegung 2+2' haette dann
     keine T-vertraegliche Zeitumkehr.
   - Richtig ist: "symmetrieerzwungener Weyl-Punkt an T-invarianten Impulsen, analog zu Kramers-Weyl".
   - Fundstelle: PLAN.md S4, ERGEBNIS Punkt 2 und L4. Schwere: leicht bis mittel (Begriff traegt eine falsche
     Ursache in Finns Bild).
3. **"Masse mit voller T braucht Inversion": zu stark, gezeigt ist "Inversion reicht".** S4 beweist: Eine Inversion Π
   mit ΠV = VΠ und ΠW(k)Π^† = W(−k) wirkt auf einem einfachen Cluster skalar (Schur) und toetet c. Das gilt nur fuer
   Cluster aus genau einer Irrep-Kopie; ein Vierfach-Cluster aus zwei gleichen Irreps kann trotz Inversion
   linear bleiben, wie ein masseloser Dirac-Kegel. Notwendigkeit ist nicht gezeigt. Ohne Inversion gab es nur Kegel,
   aber bei 40 Starts je Fall in den Formen N und O. Nach dem eigenen Kodimensionsargument (eine reelle Bedingung je Cluster, vier
   Cluster; kovariante Raeume bei K4/K5 der komplexen Dimension 44 bis 56, Tabelle Teil B) sind abgestimmte massive
   Loesungen ohne Inversion nicht ausgeschlossen, aber auch nicht gezeigt [H des Gegenlesers]. ERGEBNIS sagt selbst "Inversion (Paritaet) oder eine abgestimmte Muenze"; in Konstruktion (a) ist
   die abgestimmte Muenze C = P_2 − P_2' aber gerade die, die eine Inversion erzeugt (Γ = σ_x⊗C, C² = I). Fundstelle:
   AUFTRAG Kernaussage 3, ERGEBNIS "Bedeutung". Schwere: mittel.
4. **"(8 Zustaende)": Mindestzahl nicht bewiesen.** Nach der eigenen Definition (PLAN.md 1.4: Cluster zweifach, ohne
   lineare Aufspaltung, Luecke) waere ein 4-Zustands-Automat auf 2+2' schon "massiv", wenn auf beiden Clustern c = 0
   gilt. Eine Kopplung von 2 und 2' braucht es dafuer nicht. Schur verbietet nur die Kopplung, nicht c = 0. Bewiesen
   ist c = ±1/3 nur fuer die Familie W = C·S_±(k); dass es auf BCC mit 4 Zustaenden nur diese Familie gibt, ist offen
   (QCA-DIAMANT-4, "Nicht vorab bewiesen"). Die 8 stuetzt sich also auf S2 (2+2 scheidet aus), auf die Spurformel fuer
   eine Familie und auf Numerik. Zugleich passt "Masse verboten" in QCA-DIAMANT-4 (Kopplung) nicht zu "massiv" hier
   (Kante ohne lineare Aufspaltung); die beiden Karten benutzen verschiedene Massenbegriffe. Schwere: mittel.
5. **Konstruktion (a) ist nur bei Γ (und H) massiv.** Selbst nachgerechnet: S_+(P) = diag(e^{iP·h_a}), P·h_a =
   (π/2)(3, −1, −1, −1), also S_+(P) = −iI. A(P) = −iC hat die Eigenphasen ∓π/2, also cos ω = n·cos θ = 0: An P und P'
   liegen zwei vierfache Cluster bei ±π/2, linear aufgespalten. auswertung.json bestaetigt das ("P": [[4, "linear",
   −1.570796], [4, "linear", 1.570796]] bei a_spiegel, m = 0,3). Der Automat als Ganzes hat damit masselose Vierfach-
   Verdoppler. "Masse ohne Symmetriebruch geht" (ERGEBNIS Punkt 1) gilt fuer das Teilchen bei k = 0, nicht fuer den
   Automaten. Unter "Grenzen" steht das offen. Nur die vier isotropen P-Treffer sind auch an P und P' quadratisch, und
   ob sie in der ganzen Zone eine Luecke haben, ist nicht geprueft. Positiv: E erfuellt die symmetrische Nachbarschaft
   der Quelle (A_h ≠ 0 und A_{−h} ≠ 0), anders als der 4-Zustands-Baustein (Abschnitt 2, Punkt 5). Schwere: mittel
   (Ueberschrift).
6. **Konstruktion (a) selbst: richtig.** E^†E = I braucht nur A^†A = AA^† = I. Die Kovarianz gilt fuer A und
   A^†(k) = A(k)^† und fuer imI. A und A^† vertauschen, also zerfaellt E in 2×2-Bloecke mit cos ω = n cos θ. Bei α = 0
   ist das gerade in θ, also κ = n/(9m) aus θ² = k²/9 + O(|k|³). Inversion Γ = σ_x⊗C geprueft (braucht C² = I).
   Schwere: keine.
7. **"360 Grad = −1" in QM-D2 ist hier Wahl, nicht Befund.** V ist von vornherein spinoriell gewaehlt. Dann gilt
   PV(−1)P = −P fuer jedes Cluster automatisch, und die Pruefung "Produkt der Darstellungsmatrizen" (PLAN.md 1.4) kann
   nicht scheitern. Nicht trivial ist nur die Pruefung am Treffer selbst (implementierende Unitaere), und die ist
   beschreibend. Schwere: leicht.

**Fazit 3:** S2 traegt (zwei Zwischenschritte fehlen, beide kurz). Masse bei Γ unter voller T mit 8 Zustaenden ist durch
eine gepruefte Konstruktion belegt. Ueberzogen sind "braucht Inversion" (gezeigt: Inversion reicht), "8 Zustaende" als
Minimum (nicht bewiesen) und "Kramers" (keine Zeitumkehr im Spiel). Die Konstruktion hat masselose Verdoppler an P und
P'.

## 4. Empfohlene Formulierungen

Das sind Anforderungen an den Inhalt. Den Wortlaut legt der Autor fest.

1. **QCA-TETRA-1:** Auf BCC (acht Spruenge, ohne Selbstwechselwirkung, 2 Zustaende) gibt es isotrope unitaere Automaten
   unter L_2 nur mit der projektiven Pauli-Klasse. Die zwei Zustaende transformieren dann unter den drei
   180-Grad-Drehungen wie Spin 1/2 (360 Grad = −1), und nach der Klassifikation der Quelle sind es die Weyl-Automaten
   (Kegel bei k = 0, c = 1/√3, Verdoppler H, P, P').
   - Unter T gibt es keinen.
   - Auf dem Diamantnetz mit 2 Zustaenden gibt es keinen mit Spruengen nur laengs der Striche und richtungsgleichen
     Halbschritten.
2. **QCA-DIAMANT-4:** Auf dem Diamantnetz mit 4 Zustaenden und unitaeren Halbschritten gibt es isotrope Regeln genau
   bei monomialer Darstellung (T: 1+3, 2+2'; L_2: regulaer, Pauli+Pauli), alle von der Form C_2S(−k)C_1S(k). Unter T
   spalten die Entartungen bei k = 0 nur bei W(0) ∝ I linear auf.
   - Auf BCC gibt es mit 4 Zustaenden (2+2') T-kovariante Automaten mit Spruengen nur in S_+, also ausserhalb der
     symmetrischen Nachbarschaft der Quelle. Sie haben zwei isotrope Weyl-Kegel mit v = 1/3 und entgegengesetzter
     Chiralitaet.
   - Jede T-kovariante Regel auf 2+2' hat bei k = 0 symmetrieerzwungene Zweifachentartungen.
3. **QCA-DIRAC-T-1:** Unter T haben BCC-Automaten mit r Kopien derselben Spinor-Irrep keine Spruenge (S2).
   - Auf einem zweifachen Cluster bei k = 0 erlaubt T einen linearen Term c·k·σ (symmetrieerzwungener Weyl-Punkt;
     analog zu Kramers-Weyl, aber ohne Zeitumkehr). Eine Inversion erzwingt c = 0.
   - Mit 8 Zustaenden gibt es eine T- und inversionssymmetrische Konstruktion mit isotroper Masse bei k = 0. Sie hat
     aber masselose Vierfach-Verdoppler an P und P'.
   - Ob Masse ohne Inversion oder mit 4 Zustaenden moeglich ist, ist nicht bewiesen.

## 5. Literaturstand je Aussage

Kennzeichen: [S] selbst an der Quelle gelesen (lokale PDF, pdftotext); [L-A] Abstract per WebFetch (2 Abrufe). Den
Abstract-Wortlaut hat das Abrufwerkzeug wiedergegeben; ich habe ihn nicht selbst gesehen. Er deckt sich mit meiner
Erinnerung. [L] bzw. [L?]: aus dem Gedaechtnis.

1. **QCA-TETRA-1: Literatur, mit neuem kurzem Beweis.**
   - BCC-Weyl-Automat, L_2-Pauli-Kovarianz, "none of the automata is covariant under L_3", Verdoppler-Verschiebungen
     stehen in D'Ariano/Perinotti, PRA 90, 062106 (2014), Abschnitt IV und Anhang A [S].
   - D'Ariano, Erba, Perinotti, "Isotropic quantum walks on lattices and the Weyl equation", PRA 96, 062101 (2017),
     arXiv:1708.00826 [L-A]. Laut Abstract eine vollstaendige Klassifikation fuer s = 2, d = 1, 2, 3, "completely
     general", mit genau den zwei Weyl-Walks in d = 3. Trifft das zu, dann folgen "nur Pauli" und "unter T keiner"
     daraus. Das ist vorab ableitbar, sofern die Arbeit lineare Isotropie-Darstellungen einschliesst; das habe ich nicht
     am Volltext geprueft.
   - M1 bis M3 sind kurze, direkte Beweise in neuer Form.
   - Diamant mit 2 Zustaenden: Das Diamantnetz ist kein Bravais-Gitter, sondern der Cayley-Graph der virtuell abelschen
     Gruppe FCC ⋊ Z_2, mit den vier Punktspiegelungen an den Strichmitten als Erzeugern. Die Klassifikation von 2017 deckt
     es also nicht direkt ab. Der Beweis ist eine kurze Folgerung aus Unitaritaet (orthogonale Bilder). Ob er
     veroeffentlicht ist, weiss ich nicht; vermutlich neu, Literatur-nah [L?] (D'Ariano, Erba, Perinotti, Tosini zu
     "virtually abelian quantum walks", nicht geprueft).
2. **QCA-DIAMANT-4: Literatur in neuer Form.**
   - Imprimitivitaet/Monomialitaet (Mackey) und Grover-Lauf mit flachen Baendern sind Standard [L].
   - Die Klassifikation der Diamant-Laeufe mit 4 Zustaenden nach monomialen Darstellungen und die Aufhebung der ersten
     Ordnung unter T sind vermutlich neu [L?].
   - BCC-Teil: Dass eine 2-dim Irrep der Doppelgruppe am invarianten Punkt einen isotropen Weyl-Punkt c·k·σ erzwingt,
     ist Bandtheorie chiraler Kristalle mit Punktgruppe T (Mehrfachfermionen, Bradlyn et al., Science 2016 [L];
     Kramers-Weyl, s. u.). Schur gegen den 2-2'-Massenterm ist Lehrbuch.
   - Neu ist vermutlich die QCA-Umsetzung C·S_+(k) mit v = 1/3 [L?].
3. **QCA-DIRAC-T-1: S2 neu (soweit bekannt), Rest Literatur in neuer Form.**
   - S2 verallgemeinert M2 (r = 1) auf r Kopien; eine Vorlage kenne ich nicht [L?].
   - "Kramers-Weyl": Chang et al., "Topological quantum properties of chiral crystals", Nature Materials (2018),
     arXiv:1611.07925 [L-A]. Laut Abstract sind diese Fermionen "guaranteed by lattice translation, structural
     chirality, and time-reversal symmetry" und sitzen an TRIMs. Die Karten haben keine Zeitumkehr. Die Logik
     "Entartung erzwungen, linearer Term wegen fehlender Inversion erlaubt" ist dieselbe, die Ursache der Entartung
     nicht.
   - Inversion verbietet ungerade Terme an einem invarianten Punkt (k·p-Lehrbuch [L]).
   - Dirac-Form E = ((nA, imI), (imI, nA^†)) aus Eq. (36) der Quelle, uebertragen auf den T-kovarianten Baustein [S].

## 6. Auflagen, Quote, Grenzen dieser Lesung

- **Auflagen** (Nummern = Abschnitt.Befund):
  - A1 (1.5): "erzwingen einen Weyl-Kegel" mit "nach der Klassifikation der Quelle" kennzeichnen.
  - A2 (1.6): "Spin 1/2 erzwungen" ersetzen durch "halbzahlige (projektive) Klasse unter L_2 erzwungen".
  - A3 (1.10): Diamant-Aussage auf richtungsgleiche Halbschritte und Spruenge laengs der Striche begrenzen.
  - A4 (2.5): Die BCC-T-Loesung als ausserhalb der symmetrischen Nachbarschaft der Quelle kennzeichnen. Die Deutung
    "BCC als Fermionen-Netz" zuruecknehmen oder begruenden.
  - A5 (3.3, 3.4): "braucht Inversion" durch "Inversion reicht" ersetzen. "8 Zustaende" nicht als Minimum ausgeben.
  - A6 (3.5): In die Ueberschrift "Masse ohne Symmetriebruch" die masselosen Verdoppler an P und P' aufnehmen.
  - A7 (3.2): "Kramers-Weyl" nur als Analogie nennen (keine Zeitumkehr).
- **Quote:** 12 von 12 gepruefte Beweise bzw. Herleitungen tragen: M1, M2, M3, M6, M7, D2, D3, D4, Spurformel, S2,
  Konstruktion (a), S4-Inversionsschritt. Drei davon brauchen einen Zusatzschritt (M2, M6, S2). Bei den Fassungen
  sind 6 Stellen mittel zu stark (1.5, 1.10, 2.5, 3.3, 3.4, 3.5) und 5 leicht (1.6, 2.4, 2.6, 2.7, 3.2). Kein Befund
  der Schwere "schwer".
- **Abgleich mit lauf-69/auswertung.json:** Vorbedingungen in allen drei Ordnern true. Die Urteile stimmen mit den
  ERGEBNIS-Tabellen ueberein: QT0 bis QT3 e/e/n/e, QD0 bis QD3 e/e/n/e, QM-D0 bis QM-D3 e/e/e/e (e = eingetroffen,
  n = nicht eingetroffen). Stichproben: T:2+2 auf BCC mit D_min 0,0889 = 4/45; a_spiegel mit vierfachen linearen Clustern
  an P und P'.
- **Grenzen dieser Lesung:**
  - Die Herleitung der Quelle in Anhang A (Rang-eins-Schritt, "only four") habe ich nicht geprueft.
  - Den Volltext von 1708.00826 und 1611.07925 habe ich nicht gelesen, nur die per Abruf wiedergegebenen Abstracts.
  - Code und Rohlaeufe (haupt_*.json) habe ich nicht geoeffnet.
  - Die Normalform-Behauptung D3 habe ich in der Struktur geprueft, nicht jede Phase.
- **Zeiten (date):** Beginn 09:01:38 CEST, Befundtext abgeschlossen 09:22:12 CEST. Dauer 20 min 34 s (09:01:38 bis
  09:21:38 sind 20 min, dazu 34 s). Danach nur Kopfzeile, Urteilszeile und diese Zeile. Abrufe: 2 von 3 (WebFetch).
