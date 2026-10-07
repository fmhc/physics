# KITAEV-DIAMANT-1: Plan des Code-Agenten (Runde 37)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 04:58:56 CEST (date). Karte, STRINGENDE-1 (ERGEBNIS,
  PLAN, Code) und IDEEN-EVOLUTION/GEN-04-SPIN-HALB.md gelesen ab 04:58:56. Plantext ab 05:34:10 CEST (date).
- Rechnungen nur auf der .69 in /home/fmh/fmhc-physics-remote/runde37-kitaev/, Start nur ueber kleintest.sh, Spur p4000a.
  Reine CPU-Rechnung.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (Ryu 2009, Volltext arXiv:0811.2036v2)
  - [L] Literatur aus dem Gedaechtnis; [L?] unsicher
  - [M] eigene Mathematik
  - [F] Festlegung dieses Plans (die Karte laesst es offen)
  - [H] Hypothese; [R] im Rauchlauf gesehen (vor dem Einfrieren)
- Die Vorhersagen KD0 bis KD3 und ihre Wahrscheinlichkeiten stehen unveraendert auf der Karte. Hier stehen Modell,
  Messvorschrift und Urteilsregeln.

## 0. Quelle [S]

- **Abrufe (2 von 5, keine Websuche):**
  1. arXiv-Schnittstelle, eine Abfrage mit drei Suchgliedern (Titel, Autoren, Zeitschrift, Abstract):
     - S. Ryu, "Three-dimensional topological phase on the diamond lattice", Phys. Rev. B 79, 075124 (2009),
       arXiv:0811.2036v2. Gedaechtnis der Leitung: richtig.
     - C. Wu, D. Arovas, H.-H. Hung, "A Γ-matrix generalization of the Kitaev model", Phys. Rev. B 79, 134427 (2009),
       arXiv:0811.1380v4. Richtig. Laut Abstract: auf dem Diamantgitter "gapless 3D Dirac cone-like excitations and
       gapped topological insulating states". Nur Abstract gelesen.
     - H. Yao, S.-C. Zhang, S. A. Kivelson, "Algebraic spin liquid in an exactly solvable spin model", Phys. Rev. Lett.
       102, 217202 (2009), arXiv:0810.5347: Spin 3/2 auf dem Quadratgitter. Richtig. Nur Abstract.
  2. Volltext Ryu (PDF v2, 9 Seiten). Das Abrufwerkzeug lieferte keinen Text. Ich habe das abgelegte PDF seitenweise
     als Bild gelesen; Kopie in quelle/ryu-2009-arXiv-0811.2036v2.pdf (sha256 829fcc7f...19ba).
- Kitaev 2006 (Ann. Phys. 321, 2) ist Ryus Ref. 18; nicht abgerufen [L].
- **Modell (Ryu, woertlich uebernommen):**
  - Je Knoten ein vierdimensionaler Raum |στ⟩, σ, τ = ±1 (Eq. 1): Spin 3/2 oder zwei Spin 1/2.
  - Eq. (2): α^a = σ^a ⊗ τ^x (a = 1, 2, 3), α^0 = σ^0 ⊗ τ^z.
  - Eq. (3): ζ^a = −σ^a ⊗ τ^z, ζ^0 = σ^0 ⊗ τ^x; ζ^μ = iα^μ(σ^0 ⊗ τ^y); beide Saetze erfuellen {α^μ, α^ν} = 2δ^μν
    bzw. dasselbe fuer ζ (Eq. 4).
  - Eq. (15) bis (17), Gitter: r_A = Σ m_i a_i, r_B = r_A + s_0; a_1 = (a/2)(1,1,0), a_2 = (a/2)(0,1,1),
    a_3 = (a/2)(1,0,1). Die vier Nachbarvektoren sind s_1 = (a/4)(1,1,1), s_2 = (a/4)(−1,−1,1),
    s_3 = (a/4)(1,−1,−1), s_0 = (a/4)(−1,1,−1). Vier Bindungsarten μ = 0..3, eine je Richtung.
  - Eq. (18): H = −Σ_μ J_μ Σ_{μ-Bindungen} (α^μ_j α^μ_k + ζ^μ_j ζ^μ_k).
  - Eq. (20) bis (25), Majoranas: sechs Majoranas λ^0..λ^5 je Knoten; D = iΠ_p λ^p, D² = 1. D = ±1 waehlt den
    vierdimensionalen physikalischen Raum; Γ^{pq} = iλ^pλ^q. Im physikalischen Raum α^μ = Γ^{μ4} (Eq. 23),
    Γ^{45} = α^1α^2α^3α^0 = σ^0 ⊗ τ^y (Eq. 24), ζ^μ = iα^μΓ^{45} = Γ^{μ5} (Eq. 25).
  - Eq. (27), (28): H = iΣ_μ J_μ Σ u_jk(λ^4_jλ^4_k + λ^5_jλ^5_k) mit u_jk = iλ^μ_jλ^μ_k. Die u_jk vertauschen
    untereinander und mit H. Zwei Majorana-Sorten (λ^4, λ^5) huepfen im selben statischen Z_2-Feld.
  - Abschnitt V: "According to Lieb's theorem the Z_2 gauge field configuration that gives the lowest ground state
    energy has zero Z_2 vortex for all hexagons, and hence we can take u_jk = 1 for all links."
  - Eq. (30), (31): H(k) = ((0, iΦ), (−iΦ*, 0)) je Sorte, Φ(k) = Σ_μ J_μ e^{ik·s_μ}, E(k) = ±|Φ(k)|, zweifach entartet.
  - Abschnitt VI: "When one of the coupling J_μ is strong enough compared to the others, the spectrum for the
    Majorana fermions is gapped" (starke Paarung, Windungszahl 0).
  - Abschnitt VII: "When all J_μ are equal ... the energy spectrum ... has lines of zeros (line nodes) in momentum
    space." Die topologische Phase (ν = ±1) entsteht erst mit Zusatztermen K^{x,z} (Eq. 45 bis 48, uebernaechste
    Nachbarn) und einer Verzerrung δJ_1.
  - Abschnitt III und VIII: U(1)-Symmetrie (Drehung um die τ^y-Achse).

## 1. Kartenpruefung (vor dem Einfrieren offengelegt)

1. **Modell:** Die Karte schreibt H = Σ J_a Γ^a_iΓ^a_j "plus ggf. Zusatzterme aus der Quelle". Die Quelle hat je
   Bindung zwei Terme, αα + ζζ, mit Minuszeichen (Eq. 18), also zwei Majorana-Sorten. Ich rechne Eq. (18). Die
   Zusatzterme K^{x,z} (Eq. 45 bis 48) gehoeren zur topologischen Phase, nicht zur Karte, und werden nicht gerechnet [F].
   Die Einterm-Fassung haette dasselbe Φ(k) mit nur einer Sorte; KD1 und KD2 aendert das nicht [M].
2. **"Γ^5 = Γ^1Γ^2Γ^3Γ^4 bis auf Phase":** In der Quelle ist Γ^{45} = α^1α^2α^3α^0 = σ^0 ⊗ τ^y; es braucht keine
   Phase. Keine Berichtigung.
3. **Majorana-Form der Karte (Γ^a = i b^a c):** Entspricht α^μ = iλ^μλ^4: b^μ ↔ λ^μ, c ↔ λ^4. Dazu kommt λ^5 fuer ζ.
   Keine Berichtigung.
4. **Vorzeichen in der Quelle [M, vor dem ersten Rauchlauf abgeleitet]:**
   - Mit Γ^{pq} = iλ^pλ^q gilt α^1α^2α^3α^0 = −D·Γ^{45} und iα^μ(α^1α^2α^3α^0) = D·Γ^{μ5}.
   - Im Sektor D = +1 gilt also Eq. (25), aber Eq. (24) nur mit Minuszeichen; im Sektor D = −1 ist es umgekehrt.
   - H (Eq. 27) bleibt in beiden Sektoren richtig, weil ζ nur quadratisch auf einer Bindung vorkommt.
   - Der Code prueft das exakt; es geht in kein Urteil ein, nur in die Abbildungspruefung (gleiches Vorzeichen fuer
     alle μ in jedem Sektor).
5. **KD1 [L?]:** Die Quelle sagt "line nodes" [S]. Am Schreibtisch [M]: Bei J_μ = 1 ist
   Φ(k) = 4[cos(k_x a/4) cos(k_y a/4) cos(k_z a/4) − i sin(k_x a/4) sin(k_y a/4) sin(k_z a/4)]. Die Nullstellen
   bilden also die Linien X–W (z. B. k = (2π/a)(1, 0, t)). Der Spektralteil von KD1 war damit vor der Rechnung
   ableitbar.
6. **KD2, "deutlich groesser" (offen):**
   - Schreibtisch [M]: Φ = e^{ik·s_0}(J_0 + J_1e^{iφ_1} + J_2e^{iφ_2} + J_3e^{iφ_3}). Die Phasen φ_μ = k·(s_μ − s_0)
     laufen unabhaengig ueber den ganzen Torus (s_μ − s_0 = a_3, a_3 − a_1, a_3 − a_2 ist eine Gitterbasis).
   - Daraus folgt: Luecke genau dann, wenn J_max > Summe der drei anderen; dann min|Φ| = J_max − Summe.
   - Festlegung [F]: Urteil mit J = (J_0, J_1, J_2, J_3) = (4, 1, 1, 1). Begruendung: Die Quelle beschreibt die
     Luecke fuer "J_0 ≫ J_{1,2,3}" (Abschnitt VI).
   - Offenlegung: Bei der Lesart "Faktor 2" (J_0 = 2) gibt es keine Luecke, KD2 waere "nicht eingetroffen". Beide
     Ausgaenge waren vor der Rechnung ableitbar. Die Lesart J_0 = 2 steht als Vermerk im Urteil.
   - Berichtigung der Karte: Die Bedingung lautet nicht "deutlich groesser", sondern "groesser als die Summe der
     anderen drei". Urteil nach Kartenwortlaut: mit der Festlegung J_0 = 4.
7. **KD3 (Vertauschungsphase):**
   - Die Quelle nennt keine String-Operatoren. Die Karte sagt fuer diesen Fall: "Sonst nur Spektrum und
     Erhaltungsgroessen."
   - Die Huepfer stehen aber in der Quelle: Nach Eq. (27) ist der Bindungsterm α^μ_jα^μ_k = −iu_jkλ^4_jλ^4_k ein
     Majorana-Huepfer (Sorte 4), ζ^μ_jζ^μ_k einer der Sorte 5. Strings bilde ich als Produkte der Huepfer nach
     Levin/Wen Abschnitt IV (gelesen in STRINGENDE-1); die Zuordnung ist [M].
   - Ich messe deshalb mit dieser gekennzeichneten Ergaenzung. Geurteilt wird mit dem Messwert. Vermerk: Nach strengem
     Kartenwortlaut waere KD3 "nicht auswertbar".
   - Vorab [M]: Am gemeinsamen Knoten tragen die drei Beine drei verschiedene, paarweise antikommutierende α. Das
     ergibt −1, algebraisch festgelegt. Gegenproben siehe 4.4.
8. **Schleifenoperatoren [F]:** W_p ist das geordnete Produkt der sechs Bindungsoperatoren α^μ_aα^μ_b entlang des
   Rings, mal i, falls nicht hermitesch. Die ζ-Fassung ist dasselbe Operatorprodukt, denn α^μα^ν = ζ^μζ^ν [M]; der
   Code prueft das.
9. **Gittergroesse der Karte (2×2×2 fcc-Zellen, 16 Knoten):** wird als L = 2 mitgerechnet, dazu L = 3 und 4.
10. **Flussfreier Sektor:** Ryu begruendet ihn mit Lieb. Liebs Satz gilt fuer ebene Gitter [L]; in 3D ist das eine
    Annahme. Ich pruefe sie beschreibend im Ortsraum (4.3). Das geht in kein Urteil ein, weil die Karte "im
    fluss-freien Sektor (bzw. dem von der Quelle angegebenen Grundzustandssektor)" vorgibt.

## 2. Gitter und Operatoren [S: Eq. 2, 3, 15 bis 18; F: Indizes]

- **Zellen** m ∈ Z_{L1} × Z_{L2} × Z_{L3}. A(m) ist mit B(m + Δ_μ) ueber eine μ-Bindung verbunden; Δ_0 = (0,0,0),
  Δ_1 = (0,0,1), Δ_2 = (−1,0,1), Δ_3 = (0,−1,1) (aus s_μ − s_0 = r_A(Δ_μ)).
- **Sechserringe:** von A(m) ueber die Richtungsfolge μνρμνρ (alle 24 geordneten Tripel), doppelte entfernt.
  Erwartung [M]: 4 Ringe je Zelle, 12 je Knoten, Typmuster μνρμνρ.
- **Spin:** Knoten s → Qubits 2s (σ) und 2s+1 (τ). Paulioperatoren exakt als i^k X^x Z^z (wie STRINGENDE-1).
- **Majoranas:** Knoten s → Moden 3s, 3s+1, 3s+2 einer globalen Jordan-Wigner-Kette; λ^{2r} = X_q Π_{q'<q} Z_{q'},
  λ^{2r+1} = Y_q Π_{q'<q} Z_{q'}.

## 3. Rechenwege

- **Exakt (Pauli-Algebra, ganzzahlig):** Antikommutatoren, Kommutatoren, Operatoridentitaeten, GF(2)-Rang. A = B
  auf dem Unterraum D = s genau dann, wenn A = B oder A = s·B·D (Pauli-Strings) [M].
- **ED (numpy, float64):**
  - Sechserring (offen, nur Ringbindungen): 6 Knoten, 4096 Zustaende. Spektrum von H + 1000·W trennt W = ±1.
  - Periodischer Haufen L = (1,1,2): 4 Knoten, 8 Bindungen, jede Richtung je Knoten einmal (Multigraph),
    256 Zustaende.
- **Impulsraum:** |Φ(θ)| mit θ_i = k·a_i auf N³-Gittern und mit Minimierern (BFGS plus Gauss-Newton auf
  (Re Φ, Im Φ)).
- Die Vertauschungsphase wird dreifach berechnet wie in STRINGENDE-1: V1 Quelle (Levin/Wen Eq. 4), V2 Kartenform,
  V3 symplektisch.

## 4. Messungen [F]

### 4.1 KD0

- **Dirac-Matrizen:** α^μ und ζ^μ hermitesch, Quadrat 1, paarweise antikommutierend.
- **Lesepruefung:** Eq. (24) als α^1α^2α^3α^0 = σ^0 ⊗ τ^y und ζ^μ = iα^μ(σ^0 ⊗ τ^y). Dazu beschreibend das Muster
  [α^μ, ζ^ν] = 0 fuer μ ≠ ν, {α^μ, ζ^μ} = 0.
- **Gitter L = 2, 3, 4 (bzw. im Rauchlauf 2, 3):**
  - Alle Bindungsterme (αα und ζζ, J = 1) gegen alle W_p.
  - W_p paarweise; W_p hermitesch, W_p² = 1; W_p(α) = W_p(ζ).
  - Zahl der Ringe und Typmuster.
  - GF(2)-Relationen der Ringe (geschlossene Flaechen): Das Produkt der W_p muss ein Vielfaches der Eins sein;
    Vorzeichen beschreibend.

### 4.2 KD1: Abbildung auf freie Majoranas

- **Knoten:** λ hermitesch, Quadrat 1, paarweise antikommutierend; D hermitesch, D² = 1, D vertauscht mit allen
  Γ^{pq}. Je Sektor D = ±1: Beziehung von α^1α^2α^3α^0 zu Γ^{45} (Eq. 24) und von iΓ^{μ4}(α^1α^2α^3α^0) zu Γ^{μ5}
  (Eq. 25), jeweils "+", "−" oder "keine".
- **Gitter L = 3 (54 Knoten, 324 Majoranas):**
  - Γ^{μ4}_jΓ^{μ4}_k = −iu_jkλ^4_jλ^4_k und Γ^{μ5}_jΓ^{μ5}_k = −iu_jkλ^5_jλ^5_k fuer alle Bindungen (Eq. 27).
  - u hermitesch, u² = 1, alle u paarweise vertauschend, u gegen alle H-Terme vertauschend.
  - H-Terme vertauschen mit allen D_s; u antikommutiert genau mit den D seiner beiden Enden.
  - Majorana-Bild von W_p = σ_p·Π_{b∈p} u_b mit σ_p = ±1.
- **Sechserring-ED** (J = 1 und J = (1,0; 0,7; 1,3; 0,9)):
  - Vorhersage [M]: Im Sektor W = +1 sind die Niveaus Σ_{Sorte, n} s_n(2n_n − 1) mit den Singulaerwerten s_n des
    3×3-Huepfblocks fuer Π u = σ, jedes 32-fach (Eich- und Zusatz-Nullmoden). Im Sektor W = −1 dasselbe mit Π u = −σ.
  - Gemessen wird die groesste Abweichung je Sektor, dazu die vertauschte Zuordnung (Empfindlichkeit).
- **Periodischer Haufen (1,1,2)** (beide J-Saetze):
  - Spin-ED (256 Zustaende) gegen H in Majorana-Form, eingeschraenkt auf D_s = +1 fuer alle s.
  - Spin-ED gegen freie Majoranas mit Projektion: Π_s D_s = c·(Π_b u_b)·P_m mit P_m = Π_s(iλ^4_sλ^5_s); c exakt
    berechnet. Erlaubt ist je Eichkonfiguration P_m = c·Π u. Ueber alle 256 Konfigurationen: jeder Spin-Wert achtfach
    (Bahn der Eichgruppe).
- **U(1) beschreibend (L = 3):** [Σ_x Γ^{45}_x, H] = 0 exakt als Pauli-Summe; Gegenprobe Σ_x α^0_x.

### 4.3 KD1: Spektrum im flussfreien Sektor bei J = 1

- **Codepruefung:**
  - reduzierte Form gegen Eq. (31) an 200 Zufalls-k
  - J = 1 gegen 4(ccc − isss)
  - Ortsraum (Singulaerwerte des Huepfblocks, u = 1) gegen |Φ| auf dem L-Gitter, L = 4 bis 8
- **Messung:**
  - Gitterminimum fuer N = 8, 9, 16, 17, 32, 33, 64, 65, 128, 129, 256, 257
  - Minimierer mit 400 Startpunkten
  - Volumenanteil {|Φ| < δ} fuer δ = 0,4; 0,2; 0,1; 0,05 auf N = 257
  - Steigung im log-log-Bild ueber δ = 0,2; 0,1; 0,05. Erwartung [M]: etwa 2 fuer Linien, verkleinert durch einen
    Logarithmus an den Kreuzungspunkten X; 3 fuer Punkte, 1 fuer Flaechen.
  - Lage der gefundenen Nullstellen: Welche Faktoren von 4(ccc − isss) verschwinden.
  - Beschreibend: Zahl der Gitterpunkte mit |Φ| < 2π/N fuer N = 65, 129, 257. Exponent etwa 1 fuer Linien.
- **Ortsraum beschreibend (L = 4 bis 8; J = 1, (4,1,1,1), (2,1,1,1)):**
  - Grundzustandsenergie fuer u = 1, fuer ein gekipptes u je Richtung und fuer 20 Zufallsfelder
  - kleinster Singulaerwert

### 4.4 KD2

- **Faelle:** J = (4,1,1,1) (Urteil), (2,1,1,1) (Lesart Faktor 2), (1,1,1,4) und (1,4,1,1) (andere Richtung).
  Gitter wie 4.3; Minimierer mit 64 Startpunkten.
- **Skan, beschreibend:** J_0 = 1; 1,5; 2; 2,5; 2,8; 2,9; 3; 3,1; 3,2; 3,5; 4; 5; 6 gegen den Schreibtischwert
  max(0, J_0 − 3).

### 4.5 KD3

- **Huepfer:** Sorte a: α^μ_jα^μ_k; Sorte z: ζ^μ_jζ^μ_k; Verbund az: Produkt beider (bewegt λ^4 und λ^5 zusammen).
- **Lokal (L = 4):** jeder Knoten, alle 24 geordneten Tripel verschiedener Nachbarn, Eq. (4).
- **Lange Strings (L = 8):**
  - Gemeinsamer Knoten I = A(4,4,4). Die Beine kommen ueber die Richtungen 0, 1, 2 an; die Richtung 3 bleibt frei.
  - Aeussere Knoten: A(4,4,1), A(6,4,6), A(1,4,6).
  - Bereiche in Zellkoordinaten, paarweise disjunkt, jeweils mit dem Eingangsknoten:
    - j: [1,6]×[1,6]×[1,3]
    - k: [5,6]×[1,6]×[4,6]
    - l: [1,3]×[1,6]×[4,6]
  - Bezugsweg (Breitensuche) plus N = 300 schleifengeloeschte Zufallswege je Bein; Saat 37137 (Haupt), 37101 (Rauch).
- **Je String:**
  - Enden: Sorten a und z antikommutieren genau mit Γ^{45} an den beiden Enden (dort aendert sich die
    λ^4λ^5-Paritaet). Der Verbund muss gleich ±Γ^{45}_O Γ^{45}_I sein, also lokal.
  - Gleichwertigkeit mit dem Bezugsweg: Produkt im GF(2)-Spann der W_p.
  - Fluesse unberuehrt: vertauscht mit allen W_p (geprueft fuer Bezug und die ersten 10 Varianten).
- **Durchgangsprobe (Bezugswege):** W_j mal
  - einem Huepfer am aeusseren Ende von k (Richtung 1, Nachbar ausserhalb aller Bereiche): Erwartung Wechsel
    (Sorten a, z), kein Wechsel (Verbund) [M]
  - einem Huepfer am gemeinsamen Knoten in Richtung 3: Erwartung kein Wechsel
  - einem W_p am Ende von k: Erwartung kein Wechsel
- **Kontrolle bosonisch:** Verbund az, lokal und lang, Erwartung +1 [M]. Der Verbund ist ein lokales Teilchen,
  denn α^μζ^μ = iΓ^{45} [M].

## 5. Urteilsregeln (mechanisch in code/auswertung.py)

- **Moegliche Urteile:**
  - "eingetroffen" oder "nicht eingetroffen"
  - "nicht auswertbar": Lauf fehlt, rc ≠ 0, Zeitabbruch, oder eine Vorbedingung bzw. Kontrolle wie unten
- **KD0:**
  - Vorbedingungen, sonst nicht auswertbar:
    - Lesepruefung: Eq. (24) in Dirac-Form und ζ^μ = iα^μ(σ^0 ⊗ τ^y), 0 Fehler
    - Struktur fuer L ≥ 3: 4L³ Ringe, 12 je Knoten, Typmuster fehlerfrei
  - Eingetroffen genau dann, wenn
    - (a) α^μ und ζ^μ hermitesch sind, zu 1 quadrieren und paarweise antikommutieren (0 Fehler)
    - und (b) fuer alle L alle Bindungsterme mit allen W_p vertauschen, die W_p paarweise vertauschen und
      W_p hermitesch mit W_p² = 1 sind (0 Fehler).
- **KD1:**
  - Vorbedingung Codepruefung (4.3): Abweichungen < 1e−10 bzw. Ortsraum < 1e−9, sonst nicht auswertbar.
  - Eingetroffen genau dann, wenn alle drei Teile gelten:
    - (a) Abbildung, alle Teile aus 4.2:
      - Knoten: 0 Fehler, je Sektor einheitliches Vorzeichen ("+" oder "−") fuer alle μ in Eq. (25) und ein
        Vorzeichen in Eq. (24)
      - Gitter: 0 Fehler, jedes W_p = ±Π u
      - Sechserring: beide Sektoren je 2048 Werte, Abweichung < 1e−8
      - Haufen (1,1,2): Spin gegen Majorana-Form < 1e−9, Spin gegen projizierte freie Majoranas < 1e−8, c = ±1,
        256 physikalische Zustaende
    - (b) Nullstellen, keine Luecke: Minimierer findet |Φ| < 1e−8, und das Gitterminimum bei N = 257 ist kleiner als
      ein Drittel des Werts bei N = 33.
    - (c) Punkte oder Linien: Steigung des Volumenanteils ≥ 1,5. Bei < 1,5 waere es eine Flaeche oder unklar, dann
      nicht eingetroffen.
- **KD2:**
  - Vorbedingung wie KD1 (Codepruefung).
  - Eingetroffen genau dann, wenn fuer J = (4,1,1,1) eine Luecke vorliegt:
    - Minimierer ≥ 1e−3
    - Gitterminima bei N = 256 und 257 beide ≥ 1e−3 und hoechstens 2 % auseinander
    - Minimierer nicht groesser als das Gitterminimum (+1e−9)
  - Vermerk: Ergebnis fuer J_0 = 2 nach derselben Regel; groesste Abweichung des Skans von max(0, J_0 − 3);
    andere Richtungen gleich.
- **KD3:**
  - Nicht auswertbar, wenn
    - V1/V2/V3 irgendwo voneinander abweichen
    - oder die Kontrolle verfehlt wird (Verbund az lokal und lang nicht ueberall +1 oder nicht lokal)
    - oder eine Durchgangsprobe von ihrer Erwartung abweicht.
  - Sonst eingetroffen genau dann, wenn fuer die Sorten a und z gilt:
    - lokal ueberall −1, lang ueberall −1
    - 0 Endpunktfehler, 0 Gleichwertigkeitsfehler, 0 Flussverletzungen
  - Vermerk wie Abschnitt 1, Punkt 7.
- **Beschreibend, ohne Urteil:**
  - U(1)
  - Ortsraum-Flussvergleich
  - Exponent der Zahl naher Nullstellen
  - Relationsvorzeichen
  - Vorzeichen Eq. (24)/(25)
  - Grundzustand des Sechserrings

## 6. Rauchlaeufe [R] (vor dem Einfrieren, offengelegt)

- **Rauch 1** (Unit fmhc-physics-klein-kd-rauch1-032812, 03:28:12 bis 03:28:30 UTC, rc = 0, 17,4 s):
  - Code-Fehler: np.bitwise_count liefert uint8, daher wurde 1 − 2·1 zu 255. Alle dichten Matrizen waren falsch:
    Sechserring E0 = −255 020, Haufen Spin gegen Majorana-Form 2310.
  - Berichtigt: Umwandlung nach int64.
  - Die Auswertung gab KD1 "nicht eingetroffen", wegen dieses Fehlers und weil im Rauchmodus das groesste ungerade N
    gleich 33 war.
- **Rauch 2** (03:32:08 bis 03:32:26 UTC, rc = 0, 17,8 s), nach der Berichtigung:
  - Sechserring: Abweichung 9e−11 (W = +1) bzw. 1,5e−11 (W = −1), vertauscht 2,54. σ = +1 fuer alle 108 Ringe,
    Grundzustand bei W = +1 mit E0 = −8.
  - Haufen: Spin gegen Majorana-Form 4,6e−14, gegen projizierte freie Majoranas 7,9e−13, c = −1.
  - Knoten: D = +1: Eq. (24) "−", Eq. (25) "+"; D = −1 umgekehrt, wie in Abschnitt 1, Punkt 4 abgeleitet.
  - Bei J = 1 findet der Minimierer |Φ| ~ 1e−17, die Nullstellen liegen auf Linien.
  - Steigung 1,54 (N = 33, grob).
  - J_0 = 4: Luecke 1,0, J_0 = 2: keine. Der Skan trifft max(0, J_0 − 3).
  - KD3: lokal a, z −1 (je 3072), az +1; lang (N = 3) wie erwartet; Durchgangsproben passen.
  - Ortsraum: Bei L = 4 senkt ein gekipptes u die Energie (J = 1: −0,34; J_0 = 4, Richtung 0: −0,019); bei L = 5
    hebt es sie (J = 1: +0,42; J_0 = 4: +0,039). Bei J_0 = 4, L = 4 lag ein Zufallsfeld tiefer als u = 1. Gerade L
    trifft die Knotenlinien exakt (Nullmoden), das deute ich als Endlichkeitseffekt [H]. Beschreibend, kein Urteil.
- **Aenderungen nach den Rauchlaeufen (keine Schwelle, keine Regel geaendert):**
  1. uint8-Berichtigung (Code-Fehler).
  2. Volumenanteil auf N = 257 statt 256: Bei geradem N liegen Gitterpunkte genau auf den Knotenlinien und zaehlen
     fuer jedes δ (Rauch 1, N = 32: Anteil bei δ = 0,1 und 0,05 fast gleich). Deltas und Schwelle 1,5 unveraendert.
  3. Rauch-Gitter um N = 64, 65 ergaenzt (nur Rauchmodus).
  4. Ortsraum-Flussvergleich erweitert: L = 5, 7, J = (2,1,1,1), ein gekipptes u je Richtung. Beschreibend.
  5. Beschreibend ergaenzt: Exponent der Zahl naher Nullstellen.
  6. 400 statt 64 Minimierer-Starts fuer J = 1 (Lage der Linien, Bild).
- **Rauch 3** (Endfassung, 03:33:46 bis 03:34:04 UTC, rc = 0, 18,0 s):
  - alle vier Urteile im Rauchmodus "eingetroffen"
  - Code sha256 8096c1be...3064, Auswertung d8696b75...4c08
- **Wirkung auf die Vorhersagen:** keine. KD0, KD1 (Spektrum), KD2 und KD3 waren vor jeder Rechnung ableitbar
  [M, S]. Pruefbar war vor allem, ob der Nachbau der Quelle (Abbildung, Projektion, Vorzeichen) stimmt.
