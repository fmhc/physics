# QCA-DIAMANT-4: Ergebnis (Runde 38)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date):**
  - Start 2026-10-04 06:48:09 CEST; Code ab 07:09:51, Plantext ab 07:14:18; Text dieser Datei ab 07:56:43 CEST.
  - Rauchlaeufe 05:17 bis 05:33 UTC (PLAN.md Abschnitt 7). Plan und Code eingefroren 07:33:24 CEST
    (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe auf der .69 ueber kleintest.sh, je ein ssh-Aufruf, alle rc = 0 (UTC = CEST − 2 h):

    | Lauf | Spur | Inhalt | Start bis Ende (UTC) | Dauer |
    |---|---|---|---|---|
    | H-Ba | cpu5 | Teil B frei: eindimensionale Summen, T:1+3, T:2+2 | 05:33:46 bis 05:39:38 | 351,4 s |
    | H-Bb | p4000b | Teil B frei: T:1'+3, T:2+2' | 05:33:47 bis 05:39:44 | 355,7 s |
    | H-Bc | cpu5 | Teil B frei: T:2+2'' | 05:39:46 bis 05:41:43 | 116,1 s |
    | H-Bw | p4000b | Teil B w0, alle zehn | 05:39:52 bis 05:47:37 | 464,1 s |
    | H-A1f | cpu5 | Teil A Fassung 1 frei | 05:41:51 bis 05:45:39 | 227,0 s |
    | H-A2f | cpu5 | Teil A Fassung 2 frei | 05:45:46 bis 05:47:19 | 91,9 s |
    | H-A1w | p4000b | Teil A Fassung 1 w0 | 05:47:45 bis 05:54:27 | 401,3 s |
    | H-A2w | cpu5 | Teil A Fassung 2 w0 | 05:47:47 bis 05:52:17 | 269,0 s |
    | H-0 | cpu5 | Teil 0 (Kontrolle s = 2) | 05:52:24 bis 05:53:45 | 80,0 s |
    | Auswertung, Bilder | cpu5, p4000b | auswertung.py, bild.py | 05:54:35 bis 05:54:48 | |

- **Kennzeichen:** [S] an der Quelle gelesen (D'Ariano/Perinotti, PRA 90, 062106 (2014); Lesung aus QCA-TETRA-1,
  kein neuer Abruf); [L] Literatur aus dem Gedaechtnis; [L?] unsicher; [M] eigene Mathematik; [H] Hypothese;
  [R] im Rauchlauf gesehen.
- **Art des Ergebnisses:**
  - Synthetische Rechnung an einem selbst gebauten Modell, keine Messdatenbestaetigung.
  - QD0, QD1 und QD2 waren vor jeder Rechnung am Schreibtisch ableitbar (PLAN.md Abschnitt 3, D1 bis D4).
  - QD3 war offen; der Ausgang war in den Rauchlaeufen vor dem Einfrieren zu sehen [R] und ist danach am Schreibtisch
    erklaert [M].

## Ergebnis zuerst

1. **Diamantnetz mit 4 Zustaenden: Regeln gibt es nur fuer vier Arten von Darstellungen [M, numerisch bestaetigt].**
   - Isotrope unitaere Automaten gibt es genau dann, wenn die Drehungen die vier Striche wie vier Geraden im
     Zustandsraum vertauschen (monomiale Darstellung).
   - Das sind unter T die Darstellungen 1+3 und 2+2' (Spin 3/2 auf T), unter L_2 die regulaere und Pauli+Pauli.
   - Jede solche Regel hat die Form "Muenze, Sprung A → B, Muenze, Sprung zurueck":
     W(k) ≅ C_2 S(−k) C_1 S(k).
   - In den zwoelf anderen Darstellungen gab es in 1920 Starts keinen Treffer (kleinster Defekt ≥ 1,03).
2. **Spin-1/2-Kegel auf dem Diamant gibt es generisch nur mit der kleinen Gruppe L_2 [M, numerisch bestaetigt]:**
   - L2:P+P, Fassung 1, frei: 40 von 40 Treffern haben bei k = 0 zwei Weyl-Kegel entgegengesetzter Chiralitaet.
     360 Grad wirken als −1. Die Kegel sind aber anisotrop (Richtungsstreuung 7 bis 52 %).
   - Mit der vollen Tetraedergruppe T heben sich Hin- und Rueckschritt in erster Ordnung auf: Die Entartungen bei
     k = 0 spalten hoechstens quadratisch auf, es gibt keinen Kegel.
   - Kegel entstehen unter T erst am abgestimmten Punkt W(0) = I (Eq. 19 der Quelle), und zwar als Vierfachpunkte.
   - Bei 1+3 ist das der Grover-Typ: ein isotroper Kegel mit zwei flachen Baendern, linear, 360 Grad wirken als +1.
   - Deshalb: QD1 eingetroffen, QD2 nicht eingetroffen. Nur mit der Variante "frei" waere QD2 eingetroffen.
3. **BCC mit 4 Zustaenden traegt die volle Tetraeder-Symmetrie (auch 120 Grad) mit Weyl-Kegeln [R, M]:**
   - Gefunden ist die "Muenze mal Tetraederverschiebung" W(k) = C·diag(e^{ik·h_a}): Jeder Zustand springt nur in
     eine der vier Richtungen von S_+ (oder S_−), danach mischt eine feste Muenze C.
   - Mit der Spinordarstellung 2+2' (38 + 35 Treffer) hat sie bei k = 0 zwei exakt isotrope Weyl-Kegel mit
     Geschwindigkeit 1/3 und entgegengesetzter Chiralitaet. 360 Grad wirken als −1, die 120-Grad-Drehung ist
     implementierbar. Verdoppler liegen an H, P und P'.
   - Die Geschwindigkeit 1/3 folgt am Schreibtisch aus einer Spurformel und ist fuer jede Muenze dieselbe.
   - Deshalb: QD3 eingetroffen.
   - Eine Dirac-Masse, also eine Kopplung der beiden Weyl-Anteile, verbietet die Symmetrie (2 und 2' sind
     inaequivalent). Mit 2+2, wo sie erlaubt waere, fand die Suche keinen Automaten (kleinster Defekt 4/45).
4. **Kontrollen und Regelaenderung:**
   - QD0 eingetroffen: BCC-Weyl der Quelle wiedergefunden (56 von 100), Diamant mit 2 Zustaenden ohne Treffer.
   - Die Kegelregel habe ich nach Rauchlauf 1 verschaerft: Reine Verschiebungen zaehlen nicht als Kegel. Nach der
     alten Regel waeren alle vier Urteile gleich.
5. **Nicht gezeigt:** Masse, Wechselwirkung, Messbezug. Ob die T-kovariante Muenze-mal-Verschiebung auf BCC in der
   Literatur steht, weiss ich nicht [L?].

## Urteile (lauf-69/auswertung.json, Vorbedingungen erfuellt)

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil |
|---|---|---|---|
| QD0 | Kontrolle: QCA-TETRA-1 wiedergefunden | 90 % | eingetroffen |
| QD1 | [H] Diamant, 4 Zustaende: nichttrivialer isotroper unitaerer Automat mit Kegel bei k = 0 | 50 % | eingetroffen |
| QD2 | [H] Bei jedem solchen Treffer wirken die Drehungen projektiv (360 Grad → −1) | 60 % | nicht eingetroffen |
| QD3 | [H] BCC, 4 Zustaende: Automat mit Kegel, kovariant unter der vollen Gruppe T | 35 % | eingetroffen |

- **QD0:** BCC L2:Pauli 56 Treffer von 100, alle mit Kegel bei 0 (kleinster Defekt 7,4e−32); Diamant mit
  2 Zustaenden, Fassung 1: 0 Treffer in allen zwoelf Darstellungen (kleinster Defekt 12/7 bzw. 4/3).
- **QD1:** 335 nichttriviale Treffer mit Kegel bei 0 in 13 Faellen. Fassung 1 frei nur L2:P+P (40); Fassung 1 w0
  alle sechs loesbaren Faelle (191); Fassung 2 w0 alle sechs (104); Fassung 2 frei keiner.
- **QD2:** Von den 335 Treffern wirken 214 projektiv und 121 linear, keiner ist mehrdeutig. Die linearen sind T:1+3,
  T:1'+3 und L2:1+x+y+z, jeweils mit W(0) = I in beiden Fassungen.
- **QD3:** Kegel in Teil B frei bei T:1+3, T:1'+3, T:2+2' und T:2+2'' (165 Treffer, alle mit Kegel bei 0); w0 ohne
  Kegel.
- **Vermerke der Auswertung:**
  - QD1 nur Fassung 1 (Kartenwortlaut, = gleichzeitiger Sprung): eingetroffen.
  - QD2 nur Variante frei: eingetroffen; nur Fassung 1 (Kartenwortlaut): nicht eingetroffen.
  - Nach der Kegelregel vor Rauchlauf 1: QD1 eingetroffen, QD2 nicht eingetroffen, QD3 eingetroffen. Die
    Verschaerfung hat kein Urteil veraendert; nach alter Regel zaehlten zusaetzlich die w0-Verschiebungen in Teil B.
- **Woran QD2 haengt:** an meiner Festlegung, die Variante w0 (Eq. 19 auf reduzible Darstellungen uebertragen)
  mitzuzaehlen (PLAN.md 1.5). Ohne sie sind alle Kegel bei 0 auf dem Diamant Weyl-Paare unter L_2 mit Pauli+Pauli,
  also projektiv.

## Tabellen

### Teil A: Diamantnetz, 4 Zustaende (40 Starts je Fall)

Treffer / davon Kegel bei 0 (in Klammern: davon trivial). dim = komplexe Dimension des kovarianten Raums je Block.

| Fall | dim | F1 frei | F1 w0 | F2 frei | F2 w0 |
|---|---|---|---|---|---|
| T:1+3 | 6 | 22 / 0 | 19 / 19 | 30 / 0 | 32 / 16 (16) |
| T:1'+3 | 6 | 15 / 0 | 20 / 20 | 30 / 0 | 26 / 5 (21) |
| T:2+2' | 6 | 36 / 0 | 37 / 37 | 36 / 0 | 35 / 12 (23) |
| T:2+2'' | 6 | 35 / 0 | 35 / 35 | 39 / 0 | 38 / 18 (20) |
| L2:1+x+y+z | 16 | 40 / 0 | 40 / 40 | 40 / 0 | 40 / 21 (19) |
| L2:P+P | 16 | 40 / 40 | 40 / 40 | 40 / 0 | 40 / 32 (8) |
| zwoelf andere | 6 bis 16 | 0 (D_min ≥ 2,06) | 0 (≥ 2,14) | 0 (≥ 1,03) | 0 (≥ 1,07) |

- Die zwoelf anderen: alle eindimensionalen Summen von T und L_2, T:2+2 und die L_2-Klassen mit zwei oder drei
  Charakteren. Die Defektminima sind rational: 24/7, 8/3, 64/21, 72/35 (F1 frei) und 12/7, 4/3, 32/21, 36/35 (F2 frei).
- **Kegeltypen** (v = Steigung der Eigenphasen-Spreizung je Zweischritt; je Schritt die Haelfte; Streuung bei
  |k| = 1e−5):

| Fassung, Variante, Fall | Kegel | v | Streuung | 360 Grad |
|---|---|---|---|---|
| F1 frei L2:P+P | zwei Weyl-Kegel (je 2-fach), Chiralitaet entgegengesetzt in 40 von 40 | 0,008 bis 1,05 | 0,07 bis 0,52 | −1 |
| F1 w0 T:1+3, T:1'+3 | 4-fach, zwei flache Zweige (Grover-Typ) | 0,14 bis 1,15 (≤ 2/√3) | < 1e−3 | +1 |
| F1 w0 T:2+2', T:2+2'' | 4-fach, in manchen Richtungen zwei flache Zweige (im Bild laengs Γ–L, also der C3-Achse) | 0,02 bis 1,33 | 0,061 bei allen | −1 |
| F1 w0 L2:1+x+y+z | 4-fach, 0 bis 2 flache Zweige | 0,36 bis 1,61 | 0,008 bis 0,25 | +1 |
| F1 w0 L2:P+P | 4-fach, 0 bis 2 flache Zweige | 0,07 bis 1,60 | 0,07 bis 0,26 | −1 |
| F2 w0 T:1+3, T:1'+3, L2:1+x+y+z | Grover-Lauf, 4-fach mit zwei flachen Zweigen | 2/√3 = 1,1547 | ~1e−11 | +1 |
| F2 w0 T:2+2', T:2+2'' | 4-fach | 0,94 bis 1,33 | 0,061 | −1 |
| F2 w0 L2:P+P | 4-fach | 0,21 bis 1,62 | 0,08 bis 0,27 | −1 |

- Ohne Kegel bei 0: F1 frei T:1+3 dreifach mit quadratischer Aufspaltung (Verhaeltnis sp(2ε)/sp(ε) = 4,000);
  T:2+2' zweimal zweifach ohne lineare Aufspaltung; L2:1+x+y+z ohne Entartung bei 0; Fassung 2 frei ueberall ohne
  lineare Aufspaltung. Genau so stand es vor der Rechnung in D4.
- Bild lauf-69/treffer_teilA.png (Treffer je Darstellung und Klasse), lauf-69/omega_teilA.png (Eigenphasen von W(k)
  laengs Γ–X–W–L–Γ–K, ein Treffer je Fall). Die Grover-Faelle zeigen das exakt flache Band, T:2+2' w0 die
  entarteten Zweige laengs Γ–L (C3-Achse).

### Teil B: BCC, 4 Zustaende, volle Gruppe T (100 Starts je Fall)

| Fall | dim | frei: Treffer / Kegel bei 0 | Kegel | v | w0: Treffer / Kegel |
|---|---|---|---|---|---|
| T:1+3 | 12 | 45 / 45 | Dreifachpunkt, linear | 0,50 bis 0,577 (Streuung 0,026) | 57 / 0 |
| T:1'+3 | 12 | 47 / 47 | Dreifachpunkt, linear | 0,50 bis 0,577 | 53 / 0 |
| T:2+2' | 12 | 38 / 38 | zwei Weyl-Kegel, projektiv | 1/3 (0,33331 bis 0,33335; Streuung 3e−5) | 28 / 0 |
| T:2+2'' | 12 | 35 / 35 | zwei Weyl-Kegel, projektiv | 1/3 (Streuung 2e−5) | 40 / 0 |
| T:2+2 | 16 | 0 (D_min 4/45) | | | 0 (D_min 0,0974) |
| eindimensionale Summen (5) | 12 bis 32 | 0 (D_min 12/7) | | | 0 (D_min 1,996) |

- **Bau der Treffer:** Alle 165 frei-Treffer haben ihr ganzes Gewicht in S_+ oder ganz in S_− (Rest ≤ 7,1e−12), sind
  also W(k) = C·S_±(k) bis auf Konjugation. Die Suche blieb bei Defekt ~1e−21 stehen; die Nachpolitur bringt alle auf
  ≤ 5,1e−30, es sind echte Loesungen.
- **Chiralitaet** (T:2+2', T:2+2''): det = ±1/27 = ±(1/3)³; in jedem der 73 Treffer haben die beiden Weyl-Kegel
  entgegengesetztes Vorzeichen. Sie liegen bei verschiedenen Eigenphasen von W(0) (auf 2 und auf 2').
- **Isotropie bei |k| = 0,05** (beschreibend): T:2+2' 1e−4 bis 0,16, T:1+3 0,026 bis 0,042, BCC-Weyl der Quelle
  2,8e−3 (wie QCA-TETRA-1). Vermutlich ist die Streuung bei T:2+2' umso groesser, je naeher die beiden Eigenphasen
  von W(0) beieinander liegen [H, nicht geprueft].
- **w0:** alle Treffer sind (fast) reine Verschiebungen: Eigenphasen k·h_a, Gegenrichtung mit Gewicht ≤ 6e−11,
  Kommutatorwert erster Ordnung ≤ 1,5e−5. Nach der Regel kein Kegel. Mit W(0) = C = I bleibt von der
  Muenze-mal-Verschiebung nur die Verschiebung.
- Bild lauf-69/treffer_teilB_0.png, lauf-69/omega_teilB.png (Pfad Γ–H–N–Γ–P–H; frei mit gekruemmten Baendern,
  w0 mit geraden Linien).

### 360 Grad (aus jedem Treffer selbst bestimmt)

- Implementierende Unitaere fuer C2x und C2y: eindeutig bei allen Treffern mit Kegel und allen Treffern der Teile A und
  B frei; mehrdeutig bei allen 178 fast reinen Verschiebungen in Teil B w0 (ohne Kegel, ohne Wirkung auf ein Urteil).
- Kommutator K = U_x U_y U_x^† U_y^†:
  - projektive Faelle K = −I mit Abweichung ≤ 1,6e−14
  - lineare Faelle K = +I mit Abweichung ≤ 1,9e−14
- Die 120-Grad-Drehung (C3 um (1,1,1)) ist bei allen nichttrivialen Treffern der T-Faelle implementierbar
  (kleinster Singulaerwert ≤ 1,9e−15), bei L2:P+P nicht (≥ 0,087).
- Die 21 Grover-Treffer von L2:1+x+y+z in Fassung 2 w0 sind zusaetzlich T-symmetrisch (C3 implementierbar).
- Produkt dreier 120-Grad-Drehungen: Fuer die Spinor-Lifts gilt U(C3)³ = −I exakt (Gruppenpruefung in jedem Lauf).
  Am Treffer selbst ist U(C3)³ in 4 Dimensionen nur bis auf eine Phase bestimmt; deshalb urteilt der Kommutator.

### Verdoppler und Linien (je Fall die ersten drei nichttrivialen Treffer)

- **BCC (Teil 0 und Teil B frei):** je vier Kegelpunkte Γ, H, P, P'. Bei T:2+2' sitzt an jedem zwei Weyl-Kegel
  entgegengesetzter Chiralitaet.
- **Diamant F1 frei L2:P+P:** neben Γ weitere Kegelpunkte an den X-Punkten (2 bis 3 gefunden).
- **Diamant F1 frei L2:1+x+y+z:** keine Entartung bei 0, aber 4 bis 6 Kegelpunkte an allgemeinen Stellen, etwa
  (4,03; 0; 0), mit linearer Darstellung.
- **Alle T-Faelle auf dem Diamant:** 13 bis 20 Entartungspunkte ohne Kegel je untersuchtem Treffer (zwei
  Zweifachpaare 385-mal, ein Paar 430-mal, dreifach 9-mal). Das deutet auf Knotenlinien wie in KITAEV-DIAMANT-1; als
  Linien nachverfolgt habe ich sie nicht [H].

## Schreibtisch gegen Rechnung

- **D1** (eindimensionale Summen, L_2 mit zwei Charakteren): keine Loesung. Rechnung: 0 Treffer in allen Faellen,
  Teile A und B.
- **D2** (Fassung 1 nur bei monomialem V): Treffer genau bei T:1+3, T:1'+3, T:2+2', T:2+2'', L2:1+x+y+z und L2:P+P;
  T:2+2 und die L_2-Klassen mit drei Charakteren ohne Treffer, obwohl D1 sie nicht ausschliesst.
- **D4** (erste Ordnung):
  - frei: nur L2:P+P mit Kegel bei 0 (Weyl-Paar, Chiralitaet ±)
  - T:1+3 dreifach, quadratisch
  - Grover-Kegel ±(2|sin(ψ/2)|/√3)|k| mit zwei flachen Zweigen, Hoechstwert 2/√3 bei ψ = π: Rechnung 0,14 bis 1,145,
    Grover-Lauf genau 1,1547
  - Fassung 2 frei ohne Kegel
  - Alles eingetroffen wie vorab abgeleitet.
- **D5 (Dimensionen der kovarianten Raeume auf BCC):** vorab 12, 16, 12 fuer 1+3, 2+2, 2+2'; gerechnet ebenso.
- **Teil B, nachtraeglich [M]:**
  - Fuer V = Ind χ (Stabilisator C_3) ist W(k) = C·diag(e^{ik·h_a}) mit C im Kommutanten unitaer und T-kovariant.
  - Auf der Komponente 2 gilt ⟨a|P_2|a⟩ = 1/2, |⟨a|P_2|b⟩|² = 1/12 (a ≠ b). Damit
    tr(P_2 K' P_2 K') = (1/4 − 1/12) Σ_a (k·h_a)² = (1/6)(4/3)|k|² = (2/9)|k|².
  - Mit P_2K'P_2 = c k·σ (unter T zwingend) folgt 2c² = 2/9, also c = 1/3. Gerechnet: 0,33331 bis 0,33335.
  - Gleiches gilt fuer 2'. Die Muenze faellt heraus, weil sie auf 2 nur eine Phase ist.
  - Auf dem Diamant hebt der Rueckschritt genau diesen Term auf (H_1 = K − C_1^†KC_1); auf BCC gibt es keinen
    Rueckschritt.
- **Nicht vorab bewiesen:** dass es auf BCC unter T nur Muenze-mal-Verschiebung gibt (alle 165 Treffer sind von dieser
  Form, aber das ist keine Herleitung) und dass T:2+2 auf BCC keine Loesung hat (0 von 200 Starts, Defekt 4/45 bzw.
  0,097) [H].

## Kontrollen

- **Positivkontrolle QD0:** BCC-Weyl der Quelle mit dem neuen, auf s verallgemeinerten Code:
  - 56 von 100 Treffern, v = 0,577350 in allen Richtungen, Chiralitaet ±(1/√3)³, Verdoppler Γ, H, P, P'
  - Richtungsstreuung bei 0,05: 2,817e−3, gleich QCA-TETRA-1
- **Negativkontrollen:** BCC L2:1+chi_x (0,400) und T:2 (2/45) ohne Treffer, wie in QCA-TETRA-1.
- **Gleichwertige Darstellungen:**
  - 1'+3 gegen 1+3 und 2+2'' gegen 2+2' geben in allen sechs Teilrechnungen dieselben Klassen und Kegeltypen und
    Geschwindigkeiten im selben Bereich (die Treffer sind zufaellige Punkte derselben Familien).
  - Die drei L_2-Klassen mit drei Charakteren geben dieselben Defektminima.
- **Darstellungstabelle:** Kommutator −I genau bei den projektiven, +I bei den linearen; alle V unitaer und
  projektiv geschlossen (≤ 1e−15); Projektoren idempotent.
- **Defekt-Codepruefung:** Gitter gegen exakte Koeffizienten und X̂Ŷ gegen Koeffizientenform ≤ 5,1e−14 relativ.
- **Nachpolitur:** Treffer bei ~1e−21 gehen auf ≤ 5,1e−30; es sind keine Beinahe-Loesungen.
- **Abstand der Treffer:** Treffer bei ≤ 1,6e−29 (Teil B nach der Nachpolitur; vorher bis 2,3e−19), Nicht-Treffer
  bei ≥ 0,044. Die Kommutatorwerte trennen echte Kegel (≥ 0,32) von entkoppelten Kreuzungen (≤ 1,5e−5) um mehr als
  vier Groessenordnungen.

## Kartenberichtigungen und Festlegungen (vor dem Einfrieren, PLAN.md Abschnitt 1)

1. **Zweite Fassung:**
   - Das Kartenbeispiel "gleichzeitiger Sprung beider Untergitter" ist dieselbe Regel wie Fassung 1.
   - Gerechnet als zweite Fassung: die Cayley-Graph-Fassung mit denselben Matrizen auf beiden Untergittern.
   - Urteil nach Kartenwortlaut = nur Fassung 1: QD1 eingetroffen, QD2 nicht eingetroffen.
2. **C-2-Lesart** (nur Zweischritt unitaer) nicht gerechnet. Sie kann nur Treffer hinzufuegen; QD1 und QD2 sind mit
   Fassung 1 schon entschieden.
3. **"Unzerlegbare" 4-dim Darstellungen** gibt es fuer L_2, T und 2T nicht. Spin 3/2 (Γ_8) ist auf 2T gleich 2'+2'',
   in der Konjugation gleich 2+2'.
4. **Kegel fuer s = 4:** Mehrfachpunkte zaehlen. Nach Rauchlauf 1 verschaerft: echte Kopplung erster Ordnung,
   reine Verschiebungen trivial (siehe Selbstanzeige 3).
5. **Eq. (19) als Variante w0;** Treffer beider Varianten zaehlen. Daran haengt QD2.
6. **Teil B:** Die Karte nennt "Dirac mit Massenkopplung", QD3 fragt nach einem Kegel. Geurteilt nach QD3.
7. **QD2 ohne QD1-Treffer** waere "nicht auswertbar" gewesen; nicht eingetreten.

## Latten (v3)

- **L1 kann scheitern:** teilweise.
  - QD0 bis QD2 waren am Schreibtisch ableitbar. Scheitern konnten der Code (Positivkontrolle) und meine Beweise
    D1 bis D4: ein Treffer in einer nicht monomialen Darstellung, ein Kegel bei T frei, ein fehlender Grover-Kegel.
    Nichts davon trat ein.
  - QD3 war vor dem Rauchlauf offen und konnte in beide Richtungen ausgehen.
- **L2 Gegenprobe:**
  - Positivkontrolle BCC-Weyl
  - Gleichwertigkeitspaare
  - Kommutator +I/−I
  - C3-Test (T ja, L2:P+P nein)
  - Nachpolitur
  - Spurformel c = 1/3 gegen Rechnung
  - alte gegen neue Kegelregel (gleiche Urteile)
- **L3 Numerik:** Treffer ≤ 1,6e−29 (nach Nachpolitur) gegen Nicht-Treffer ≥ 0,044; Geschwindigkeiten auf 2e−5;
  Kommutatoren 1e−14.
- **L4 schon bekannt:**
  - Weyl-Automat und L_2-Isotropie [S].
  - Grover-Lauf mit flachen Baendern und Lokalisierung ist Standard in der Quantenlauf-Literatur [L].
  - Mehrfach-Fermionen (Spin 1, Spin 3/2) unter T in chiralen Kristallen (etwa CoSi, RhSi) sind bekannt [L].
    Muenzlaeufe auf dem Diamantgitter vermute ich in der Literatur [L?].
  - Ob die T-kovariante Muenze-mal-Tetraederverschiebung mit isotropen Weyl-Kegeln v = 1/3 veroeffentlicht ist und ob
    die Aufhebung der ersten Ordnung im Diamant-Zweischritt bekannt ist, weiss ich nicht [L?].
- **L5 Messbezug:** keiner. Die Richtungsabhaengigkeit der Geschwindigkeit (L_2-Kegel auf dem Diamant bis 52 %) waere
  bei Planck-Maschenweite durch Laufzeitmessungen an Gammablitzen begrenzt [H, L?, nicht geprueft]. Die T-Kegel auf BCC
  sind in erster Ordnung exakt isotrop.

## Bedeutung fuer Finns Bild

- **Belegt im Modell [M, numerisch bestaetigt]:**
  - Auf Finns Diamantnetz traegt die einfachste richtungsgleiche Quantenregel mit vier Zustaenden Spin-1/2-Kegel nur
    mit den drei 180-Grad-Drehungen als Symmetrie. Dann entstehen bei k = 0 zwei Weyl-Teilchen entgegengesetzter
    Haendigkeit, eine Art Dirac-Paar ohne Masse, aber mit richtungsabhaengiger Geschwindigkeit.
  - Mit der vollen Tetraeder-Symmetrie heben sich auf dem Diamant Hin- und Rueckschritt in erster Ordnung auf. Kegel
    gibt es dann nur am abgestimmten Punkt, und sie sind nicht zwingend spinoriell: Der Grover-Lauf hat einen
    bosonischen Kegel mit flachen Baendern.
  - Auf BCC (acht Tetraederrichtungen je Knoten) geht die volle Tetraeder-Symmetrie mit vier Zustaenden. Die
    Spinorvariante gibt exakt isotrope Weyl-Kegel. Das spricht im Modell fuer BCC als Fermionen-Netz, wie es die Karte
    fuer "QD1 verfehlt" vorhergesagt hatte, obwohl QD1 eingetroffen ist.
- **Nicht gezeigt:** Masse (unter T mit 2+2' durch Schur verboten, 2+2 ohne Loesung), Wechselwirkung, gekruemmte
  Netze, ob die T-Loesungen auf BCC vollstaendig sind.
- **Vorschlag [H, nicht gerechnet]:** Diamant mit 8 Zustaenden je Knoten oder mit Verweilterm, um die
  Aufhebung der ersten Ordnung unter T zu umgehen; BCC mit 2+2 und Selbstwechselwirkung fuer eine Dirac-Masse.

## Selbstanzeigen

1. **QD3 vor dem Einfrieren gesehen.** Die Rauchlaeufe zeigten die T-kovarianten Kegel in Teil B schon vor dem
   Einfrieren. Das Urteil ist deshalb keine blinde Vorhersage. Offengelegt in PLAN.md Abschnitt 7.
2. **QD0 bis QD2 vorab ableitbar.** Die Beweise D1 bis D4 sind meine eigenen und nicht von einem frischen Leser
   gegengelesen; die Numerik bestaetigt sie nur.
3. **Regelaenderung nach Rauchlauf 1:**
   - Trivialitaet um vertauschende W(k) ergaenzt, Kegel um den Kommutatortest erster Ordnung.
   - Beide machen die Regel strenger. Die Schwellen 1e−8 und 1e−2 habe ich an Rauch-2-Werten geeicht.
   - Die Urteile nach alter Regel stehen daneben und sind gleich.
   - Grenze: Die w0-Treffer in Teil B sind fast reine Verschiebungen (Kommutator ~1e−6). Die Trivialitaetsschwelle
     1e−8 erfasst sie nicht; sie landen als "Entartung ohne Kegel", nicht als "trivial". Auf kein Urteil wirkt das.
4. **Weitere Aenderungen vor dem Einfrieren:** Nachpolitur, Chiralitaet, Gewicht S_+/S_−, Fallauswahl per Index,
   Zusammenfuehren aufgeteilter Laeufe. Starts in Teil A auf 40 gesenkt (Zeitbox; Teil A war am Schreibtisch
   entschieden).
5. **Laufbuchhaltung:**
   - Nach dem Einfrieren keine Aenderung an Plan, Code oder Regeln.
   - Hauptlaeufe je einmal, jeder Starteraufruf ein eigener ssh-Aufruf.
   - In den Rauchlaeufen habe ich zwei bis drei Starteraufrufe in einer ssh-Zeile nacheinander gekettet (Rauch 1,
     3 und 4), ohne nohup und ohne Hintergrund auf der .69.
   - Hoechstens zwei Laeufe zugleich, nur cpu5 und p4000b.
6. **Werkzeuge:**
   - Lokal: jq, ssh, scp, sha256sum, date, grep, sed (auch mit -f-Skriptdateien im Scratchpad), dazu mkdir, cp, ls,
     cat, tr, cut. Lokale ssh-Aufrufe liefen teils im Hintergrund.
   - Auf der .69 ausserhalb des Starters: mkdir, mv, ls, sha256sum, tail, grep, ein lesendes systemctl --user
     list-units, ein ls auf site-packages und Warteschleifen "until grep ...; do sleep 3; done" im Vordergrund einer
     ssh-Sitzung.
   - Kein Python ausserhalb des Starters, lokal kein Interpreter.
7. **Bild:** In omega_teilA.png ueberdeckt die Gesamtueberschrift die Titel der ersten Bildzeile (nur Darstellung).
8. **Quelle:** keine neue Lesung; Eq. (5) und (19) aus der QCA-TETRA-1-Lesung uebernommen [S].
9. **Gegenlesen:** Beim Abgleich mit den JSON-Dateien habe ich in meiner ersten Textfassung neun Stellen berichtigt,
   darunter die kleinste Nicht-Treffer-Zahl (0,089 statt 0,044), die Untergrenze der echten Kegel (0,4 statt 0,32),
   die Eindeutigkeit der Unitaeren (falsch fuer Teil B w0) und eine ungepruefte Deutung der Streuung (jetzt [H]).
   Urteile sind nicht betroffen.
10. **Zeitbox:** 120 min ab 06:48:09 CEST; Text abgeschlossen um 08:01:46 CEST (date).

## Dateien

- **Plan:** PLAN.md und PLAN.md.eingefroren-20261004-073324; Pruefsummen in EINGEFROREN-SHA256.txt.
- **Code:** code/qca_diamant.py, code/auswertung.py, code/bild.py, je mit .eingefroren-20261004-073324.
- **Rauchlaeufe:** rauch-69/ (rauch1 bis rauch4: json, log, png, rauch3/4_auswertung.json).
- **Hauptlaeufe:** lauf-69/haupt_{0,A1f,A1w,A2f,A2w,Ba,Bb,Bc,Bw}.json/.log, auswertung.json/.log, bild.log,
  treffer_teilA.png, treffer_teilB_0.png, omega_teilA.png, omega_teilB.png, PRUEFSUMMEN.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/runde38-qca-diamant/ (code/, rauch/, lauf/).

## Einfach gesagt

Wir wollten wissen, ob auf Finns Netz mit vier Strichen je Knoten eine einfache Quanten-Spielregel Teilchen mit
halbem Spin ergibt, wenn jeder Knoten vier innere Zustaende hat. Das geht, aber nur, wenn man als Symmetrie die drei
halben Drehungen um die Achsen verlangt: Dann entstehen zwei masselose Teilchen mit entgegengesetzter Haendigkeit,
die allerdings je nach Richtung verschieden schnell laufen. Verlangt man die volle Tetraeder-Symmetrie mit den
Dritteldrehungen, hebt sich auf Finns Netz beim Hin- und Zurueckspringen der entscheidende Effekt auf, und die
wenigen Kegel, die dann noch entstehen, koennen auch zu ganz gewoehnlichen Teilchen ohne halben Spin gehoeren. Auf
dem Netz mit acht Tetraederrichtungen je Knoten klappt die volle Symmetrie dagegen: Dort laufen zwei
Spin-1/2-Teilchen in alle Richtungen genau gleich schnell, mit einem Drittel der Schrittweite pro Takt. Das ist eine
Rechnung an einem Modell, keine Messung.
