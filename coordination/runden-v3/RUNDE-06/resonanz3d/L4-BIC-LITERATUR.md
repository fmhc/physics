# L4-Prüfung: Verschwindende Breite der 3D-Q-Ball-Atmungsresonanz ("BIC") – schon bekannt?

- Auftrag: claude-primary, Runde 6, resonanz3d. Bearbeiter: Anthropic-Agent (Opus), reine Literaturprüfung mit
  Schreibtischrechnung. Keine neue Rechnung, kein Python.
- Beginn: 2026-09-30 03:17:10 CEST (date). Ende: siehe Zeile darunter (nach dem Schreiben mit date gemessen).
- Ende: 2026-09-30 03:37:29 CEST (date, nach dem Schreiben gemessen). Dauer rund 20 Minuten, Budget 45 Minuten.
- Markierungen:
  - **[ES]**: eigener Schluss oder Hypothese.
  - **[S]**: nur Suchtreffer oder Suchmaschinen-Zusammenfassung, nicht an der Quelle gelesen.
  - "(Abruf)": Zitat aus einem WebFetch-Auszug der Primärquelle; der Wortlaut stammt aus dem Abrufwerkzeug und wurde nicht
    selbst im PDF nachgesehen.
  - Alle übrigen Zitate stehen wörtlich in der gelesenen Quelle (arXiv-Abstract, HTML oder lokales PDF/TXT).
- Arbeitsdatei mit Abrufprotokoll (Erwartung vor jedem Abruf):
  /tmp/claude-1000/-home-fmh-fmhc-physics/76c41c65-1089-4cc3-bcfe-f088e91d4721/scratchpad/ARBEITSFELD-L4-BIC.md
  (Session-Scratchpad, flüchtig)

## 0 Kurzantwort: TEILWEISE BEKANNT

1. **Bekannt ist der Mechanismus.** Die Abstrahlung einer lokalisierten Mode verschwindet an isolierten Parameterwerten,
   weil ein reelles, vorzeichenbehaftetes Überlappintegral mit der auslaufenden Kontinuumswelle eine Nullstelle hat.
   Belegt ist das in folgenden Gebieten:
   - Photonik: Einzelresonanz-BIC durch Parameterabstimmung (Hsu u. a. 2016)
   - eingebettete Solitonen: Kodimension 1 (Champneys u. a. 2001)
   - Oszillonen: "exceptionally stable field configurations" (Zhang u. a. 2020)
   - **ganz frisch** die Innenmode einer 3D-Blase (Inagaki & Murakami, arXiv:2609.15056, 14.09.2026: fünf Nullstellen
     der Abstrahlung)
2. **Nicht gefunden: ein Q-Ball-Pol mit Breite null.** Weder ein Q-Ball-QNM mit Breite null noch eine Kurve Γ(ω) für
   Q-Ball-Resonanzen, in keiner Dimension. Die Q-Ball-Linie 2024 bis 2026 hat folgenden Stand:
   - Ciurla, **Dorey**, Romańczukiewicz, **Shnir** (nicht Forgács/Lukács) und Folgearbeiten arbeiten nur in 1+1 D.
   - Sie geben QNM nur bei einzelnen ω an.
3. **Kinks:** Das φ⁴-Wackeln strahlt in 2. Ordnung (Manton & Merabet 1997). Ein Kinkmodell mit parameterabhängiger
   Nullstelle dieses Koeffizienten habe ich nicht gefunden (Recherchestand).
4. **Unser Befund ist quantitativ konsistent mit einer einfachen Nullstelle.**
   - Signiertes √Γ ist glatt und linear mit Vorzeichenwechsel, Nullstelle bei **ω\*² = 0,79768**, Γ ≈ 1,07·(ω² − ω\*²)².
   - Die Feinläufe der Leitung bestätigen eine vorab aus der Grobtabelle abgeleitete Vorhersage **[ES]**.
   - Ob Γ dort *exakt* null ist, ist nicht gemessen.

## 1 Erwartungsverstöße (das Wichtigste zuerst)

1. **Eine 2026er-Arbeit hat genau den Überlapp-Nullstellen-Mechanismus, in 3D und kugelsymmetrisch.**
   - Erwartung: keine direkte Parallele aus den letzten Wochen.
   - Befund: Inagaki & Murakami (arXiv:2609.15056) untersuchen die kugelsymmetrische Innenmode einer O(3)-kritischen Blase:
     "This overlap can vanish through destructive interference as the supercooling is varied".
   - Unterschied: Dort geht es um *nichtlineare* Abstrahlung der 2. Harmonischen einer echt gebundenen Mode. Bei uns
     verschwindet die *lineare* Breite eines eingebetteten Pols.
   - Korrigierte Erwartung: Der Mechanismus ist seit dem 14.09.2026 für Soliton-Innenmoden publiziert. Neu bleibt die
     lineare Q-Ball-Version.
2. **Ciurla u. a. (arXiv:2405.06591) haben keine Breiten gegen ω.**
   - Erwartung: QNM-Breiten gegen ω, ohne diskutierte Nullstelle.
   - Befund, erstens: Die Autoren sind Ciurla, Dorey, Romańczukiewicz und Shnir. Die Zuordnung "Forgács, Lukács" im
     Auftrag stimmt nicht.
   - Zweitens: Die Arbeit ist rein 1+1-dimensional.
   - Drittens: Die QNM steht dort nur bei ω = √3/2, also ω² = 0,75 (β = 1/4 und β = 0).
   - Viertens: Abb. 6 trägt die Abstrahlamplitude gegen ρ auf, nicht gegen ω.
   - Die Folgearbeiten 2025/2026 (Blaschke u. a., Canillas Martínez u. a., Evslin u. a.) rechnen ebenfalls kein Γ(ω).
3. **Die Mathematik behandelt den Fall "FGR-Konstante = 0" ausdrücklich, und dann ist die Rate nicht automatisch null.**
   - Cornean, Jensen & Nenciu (CMP 2015): Die Zerfallsrate ist dann von der Ordnung ε⁴.
   - Erwartung: Die Nicht-Verschwindensbedingung der goldenen Regel (FGR-Bedingung) wird nur als generische Annahme
     geführt (Soffer & Weinstein).
   - Korrektur: "Überlapp = 0" heißt nicht "exakt BIC". Die Exaktheit braucht ein eigenes Zählargument, siehe Abschnitt 5.
4. **Oszillonen: Die Lage der Nullstellen hängt stark vom verzerrten Wellenbild ab.**
   - Zhang u. a. 2020: Die Nullstellen liegen erst richtig mit "systematic inclusion of a spacetime-dependent effective
     mass term".
   - Die Verbesserung reicht dort "by many orders of magnitude in some cases".
   - Folge für uns **[ES]**: Eine Theorieskizze mit freier Kugelwelle legt die Nullstelle falsch. Sie muss die
     Streuwelle im Ball-Potential dp(r) benutzen.
5. **Kinks liefern die erwartete nächste Analogie nicht.**
   - Gefunden habe ich nur zwei andere Wege zu "keine Abstrahlung":
     - Schwellenmechanismen: Kanäle öffnen oder schließen mit der Kopplung (Alonso-Izquierdo u. a. 2023).
     - Integrabilität: Sine-Gordon.
   - "Reflexionsfrei" ist nicht "abstrahlungsfrei": Der φ⁴-Kink hat ein reflexionsfreies Pöschl-Teller-Potential
     (σ = 2) und strahlt trotzdem.

## 2 Literaturstand mit Belegen

### 2.1 Q-Bälle (Fragen 1 und 2)

| Quelle | Inhalt | Wörtlich (≤ 15 Wörter) | Γ(ω)? Nullstelle? |
|---|---|---|---|
| Ciurla, Dorey, Romańczukiewicz, Shnir 2024, "Perturbations of Q-balls: from spectral structure to radiation pressure", arXiv:2405.06591v2 (lokal gelesen, Abschn. 3.3 und Anhang A) | 1+1 D, V = \|φ\|² − \|φ\|⁴ + β\|φ\|⁶ (unser Modell = β = 1/2); halbpropagierende Moden; QNM | "we have found a quasinormal mode at ρ = 1.538789 + 1.180 · 10−5 i" (β = 1/4, ω = √3/2); β = 0: "ρ2 = 1.5150692+ 9.96·10−5 i" | nein, nur Einzelpunkte; keine Nullstelle diskutiert |
| Evslin, Liu, Romańczukiewicz, Shnir, Wereszczyński, Ziobro 2026, "Linearized Q-Ball Perturbations", arXiv:2604.07713v1 (lokal) | 1+1 D, dickwandiger Grenzfall, führende Ordnung, geschlossene Formen | "unbinding them and turning them into Feshbach-type quasinormal modes" | nein; keine Breiten |
| Kovtun, Nugaev, Shkerin 2018, "Vibrational modes of Q-balls", arXiv:1805.03518v2 (lokal) | 3D, analytische Potentiale; dünnwandige Moden über Bessel-Nullstellen, nur gebundene Moden unter der Schwelle gezählt | "large Q-balls possess soft excitations"; k über "nth zero of the Bessel function of the first kind" | nein; Resonanzen oberhalb der Schwelle nicht behandelt |
| Azatov, Ho, Khalil 2024, "Q-ball perturbations with more details: linear analysis vs lattice", arXiv:2412.13885v1 (lokal; PRD 111, 096010 (2025) [S]) | 3D-Streuung an Q-Bällen, Phasenverschiebungen | "there are some local minima in the total cross section dependence on energy" | Streu-Nullstellen (Ramsauer-artig), keine Pol-Breiten |
| Blaschke, Romańczukiewicz, Sławińska, Wereszczyński 2025, "Q-ball polarization – a smooth path to oscillons", arXiv:2502.20519 | 1+1 D, β = 0,26 | (Abruf) "complex-valued with a very small imaginary part, responsible for slow damping" | nein |
| Canillas Martínez, Dorey, Romańczukiewicz, Saffin, Sławińska, Wereszczyński 2025, "Oscillons and bubbles in Q-ball dynamics", arXiv:2509.03192 (JHEP 12 (2025) 154 [S]) | 1+1 D, Stöße | (Abruf) "there are no modes that could participate in the resonant energy transfer" (dickwandig) | nein |
| Chen, Andersson, Li 2025, "Stability analysis for Q-balls with spectral method", arXiv:2509.18656 (Abstract) | Instabilitäten angeregter Q-Bälle | "manifested in the appearance of complex and imaginary modes" | nein, keine Resonanzbreiten |
| Saffin, Xie, Zhou 2022, "Q-ball Superradiance", arXiv:2212.03269v2 (lokal, nur gegrept) | Zweikanal-Verstärkung | – | nicht einschlägig; nur relevant, wenn beide Kanäle offen sind (Abschn. 3) |

- **24-Monats-Suche (Regel 7):**
  - Websuchen zu "Q-ball quasinormal … width vanishes / bound state in the continuum", zu Folgearbeiten der
    Ciurla-Gruppe 2025 und zu "3+1 … resonance … omega dependence". Dazu Abrufe der Arbeiten oben.
  - Ergebnis: Eine Q-Ball-Resonanz mit Breite null ist **nach Recherchestand nicht publiziert**. Das heißt nicht
    "widerlegt" und nicht "sicher neu".
- **Bosonsterne:**
  - QNM-Literatur mit Gravitation, z. B. Yoshida, Eriguchi & Futamase 1994, PRD 50, 6235 [S], nicht gelesen.
  - Eine Breiten-Nullstelle ist dort nicht aufgetaucht [S].
  - Die "quasi-resonances" massiver Felder um Schwarze Löcher sind ein Schwellenmechanismus, kein Überlapp-Null [S].

### 2.2 Kinks (Frage 3)

| Quelle | Aussage | Wörtlich |
|---|---|---|
| Manton & Merabet 1997, "φ⁴ kinks – gradient flow and dynamics", Nonlinearity 10, 3; arXiv:hep-th/9605038 (Anhang A lokal gelesen) | Wackelmode strahlt in 2. Ordnung ab, dA₀/dt = −0,010 A₀³, also A ~ t^(−1/2); Amplitude ∝ 1/sinh(π√2): klein, nicht null | "couples to the continuum radiation modes and eventually all its energy is radiated away" |
| Alonso-Izquierdo, Miguélez-Caballero, Nieto 2023, arXiv:2310.15738 (Abstract) | Zweikomponenten-φ⁴: Zahl der Formmoden hängt von der Kopplung ab; Abstrahlung bei 2ω, 3ω und Summenfrequenzen | "This coupling causes the kink to emit radiation with twice the frequency" |
| Campos & Mohammadi 2021, "Wobbling double sine-Gordon kinks", arXiv:2103.04908 (Abstract) | Resonanzfenster; keine Aussage zu Abstrahlungsnullstellen | – |
| Guo, Evslin, Bolognesi 2026, "(De-)Exciting the Third Pöschl-Teller Kink", arXiv:2603.12590 (Abstract) | PT-Reihe σ = 1, 2, 3; führende Amplituden endlich | "The cases σ=1 and 2 are the well-known Sine-Gordon and φ⁴ double-well models" |
| Timmermans & Kalmykov 2026, Zenodo 22686301 (**selbstpubliziert**, geringes Gewicht) | φ⁴-Formfaktor bei der 2. Harmonischen nicht null | (Abruf) "is nonzero at the second‑harmonic shell" |
| [S] Suchzusammenfassung zu 2310.15738 bzw. verwandten Arbeiten | "κ < 6: 2ω nicht im Kontinuum" | nicht an der Quelle geprüft; das wäre ein Schwellen-, kein Überlapp-Mechanismus |

- **Antwort auf Frage 3:**
  - Beim φ⁴-Kink verschwindet der Koeffizient nicht.
  - Ein Modell mit parameterabhängiger Nullstelle des Wackel-Abstrahlkoeffizienten habe ich nicht gefunden.
  - Die nächste belegte Analogie ist nicht ein Kink, sondern die kritische Blase (Abschn. 2.3).
  - Die gesuchten Stichworte "radiation-free" und "reflectionless" führen in die Irre: Der φ⁴-Kink ist reflexionsfrei
    (PT σ = 2) und strahlt trotzdem (Manton & Merabet).

### 2.3 Analogien mit parameterabhängigen Abstrahlungsnullstellen

| Quelle | System | Wörtlich | Nähe zu unserem Befund |
|---|---|---|---|
| **Inagaki & Murakami 2026**, "Open-channel radiation zeros and nonlinear damping of a critical-bubble internal mode", arXiv:2609.15056 (eingereicht 14.09.2026; Abstract, HTML per Abruf) | 3+1 D, reelles Skalarfeld, V̂ = s²(1−s)² − δ(3s²−2s³); kugelsymmetrische Innenmode; 2.-Harmonische-Abstrahlung | "A signed-overlap scan resolves five zeros in a finite parameter interval"; "third-harmonic loss predicts A∼τ⁻¹/⁴, instead of the generic A∼τ⁻¹/² law" | **sehr hoch** im Mechanismus (reeller, vorzeichenbehafteter FGR-Überlapp; mehr Nullstellen zur dünnen Wand hin). Unterschied: nichtlinear statt linear eingebettet. Q-Bälle und BIC werden laut Abruf nicht zitiert |
| Zhang, Amin, Copeland, Saffin, Lozanov 2020, "Classical Decay Rates of Oscillons", arXiv:2004.01202 (Abstract) | Oszillonen: Zerfallsrate gegen Konfiguration | "exceptionally stable field configurations where their decay rate is highly suppressed" | hoch (Nullstelle der Abstrahlung eines ganzen Solitons entlang seiner Familie) |
| Cyncynates & Giurgica-Tiron 2021, "The Structure of the Oscillon…", PRD 103, 116011; arXiv:2104.02069 (Abstract) | Oszillonen | "imposing realistic boundary conditions naturally selects a near-minimally radiating solution" | mittel. "Destruktive Selbstinterferenz der 3. Harmonischen bei Ausnahmefrequenzen" steht **nicht** im Abstract, nur in einer Suchzusammenfassung [S] |
| Champneys, Malomed, Yang, Kaup 2001, "'Embedded solitons': solitary waves in resonance with the linear spectrum", Physica D 152–153, 340; arXiv:nlin/0005056 (Abstract) | eingebettete Solitonen (Yang, Malomed & Kaup 1999, PRL 83, 1958 [S]) | "codimension-one solitons (i.e., those existing at isolated frequency values)"; "An embedded soliton (ES) is obtained when the latter component exactly vanishes" | hoch in der Zählung (Kodimension 1, isolierte Frequenzen), aber für das Soliton selbst, nicht für eine Innenmode |

### 2.4 BIC-Theorie und Mathematik

| Quelle | Wörtlich | Bedeutung |
|---|---|---|
| Hsu, Zhen, Stone, Joannopoulos, Soljačić 2016, "Bound states in the continuum", Nature Reviews Materials; https://www.mit.edu/~soljacic/BIC_review-NatRevMat.pdf (S. 5–8 gelesen) | "a single resonance can also evolve into a BIC when enough parameters are tuned" | Einzelresonanz-BIC durch Parameterabstimmung = unser Typ **[ES]** |
| dieselbe, Friedrich-Wintgen-Abschnitt (Gl. 5, "first derived by Friedrich and Wintgen"; Originalarbeit Friedrich & Wintgen 1985, PRA 32, 3231 [S]) | "one of the two eigenvalues becomes purely real and turns into a BIC" | Konkurrenzhypothese (zwei Resonanzen, ein Kanal) |
| dieselbe | "the required number of tuning parameters also grows with M" | Moderator: Zahl der offenen Kanäle |
| dieselbe, S. 7 | "can be understood through the concept of topological charges" | Grundlage für den Windungszahltest (Abschn. 4) |
| Soffer & Weinstein 1999, "Resonances, Radiation Damping and Instability in Hamiltonian Nonlinear Wave Equations", Invent. Math.; arXiv:chao-dyn/9807003 (Abstract) | "for generic nonlinear Hamiltonian perturbations, all small amplitude solutions decay to zero"; "a nonlinear analogue of the Fermi golden rule" | FGR ≠ 0 ist eine **Generizitätsannahme**, also an Sonderpunkten verletzbar |
| Cornean, Jensen, Nenciu 2015, "Metastable states when the Fermi Golden Rule constant vanishes", CMP 334, 1189; arXiv:1311.7502 (Abstract) | "in the case when the Fermi Golden Rule constant vanishes"; "both the decay rate and the error term of order ε⁴" | Eine FGR-Nullstelle allein erzwingt kein exaktes Γ = 0 |
| Cuccagna, Pelinovsky, Vougalter 2005, "Spectra of positive and negative energies in the linearized NLS problem", CPAM [S] | [S] Bifurkation eingebetteter Eigenwerte positiver/negativer Energie | Krein-Signatur entscheidet: Resonanz oder oszillatorische Instabilität (Abschn. 6, N7) |

## 3 Regime und Moderatoren (Regel 1)

Die Literatur widerspricht sich nicht direkt. Sie zerfällt aber in Regime, die man nicht vermischen darf:

| Moderator | Regime A | Regime B | unser Fall |
|---|---|---|---|
| **Ordnung der Kopplung** | linear eingebettet: der Pol selbst liegt im Kontinuum, Γ unabhängig von der Amplitude (Ciurla-QNM, unser Pol) | nichtlinear: nur Harmonische liegen im Kontinuum, Γ ∝ A² (Manton-Merabet, Inagaki-Murakami, Soffer-Weinstein) | A (Re ρ ≈ 1,745 > 1 − ω) |
| **Zahl offener Kanäle N_offen** | N = 1: reelle Ein-Zahl-Bedingung, exakte Nullstellen entlang *eines* Parameters generisch **[ES]** | N = 2 (\|ω − ρ\| > 1 zusätzlich offen, Superradianz-Regime nach Saffin u. a.): exakte Nullstelle braucht einen weiteren Parameter | N = 1 für ω² = 0,76 … 0,84 (Abstand 1 + ω − Re ρ = 0,144 … 0,157, aus den Logs). Lineare Extrapolation Re ρ ≈ 1,64 bei ω² = 0,55 < 1 + ω = 1,74: bleibt vermutlich im ganzen stabilen Bereich N = 1 **[ES]** |
| **Wanddicke** | dünnwandig: große Radien, die Phase der Quelle ändert sich schnell, mehr Nullstellen (Inagaki-Murakami: mehr Wurzeln auf der dünnwandigen Seite; Kovtun: Bessel-Nullstellen) | dickwandig: wenige oder keine Nullstellen | Übergangsbereich (S(0) = 1,135 bei ω² = 0,7) |
| **Vorzeichen der Kopplung sp = S(3S − 2)** | 3D: S(0) > 2/3, sp wechselt radial das Vorzeichen, Kern- und Wandbeiträge können sich aufheben **[ES]** | 1D bei ω² = 0,7: S(0) = 0,3675 < 2/3, sp überall negativ **[ES]** | möglicher Grund für den nicht monotonen Verlauf der d-Brücke **[ES]** |
| **Symmetrie** | symmetriegeschützte BIC (Paritäts- oder Drehimpuls-Fehlanpassung) | akzidentelle BIC (keine Symmetrie) | akzidentell (l = 0 koppelt an l = 0) |

- **Regel 6 (Kopplung vor Bauteil) [ES]:** Es gibt mindestens fünf Wege zu "Mode strahlt nicht":
  - Schwelle (Kanal geschlossen)
  - Symmetrie
  - Integrabilität
  - Friedrich-Wintgen-Interferenz zweier Resonanzen
  - akzidentelle Überlapp-Nullstelle
  - Alle fünf sind Wege, **eine** Größe zu null zu machen: die Projektion M der Modenquelle auf die on-shell-Streuzustände
    der offenen Kanäle. Nach dieser Größe sollte man fragen, nicht nach dem "Bauteil".
  - Bei uns ist nach allem, was vorliegt, der letzte Weg realisiert.

## 4 Unterscheidungspunkte (Regel 2)

| Erklärungspaar | wo sie messbar auseinanderlaufen | Stand |
|---|---|---|
| **H0 exakte Nullstelle** gegen **H2 tiefes Minimum mit Boden Γ_min > 0** | nur bei \|ω² − ω\*²\| ≲ 1e-4 (Γ ≲ 1e-8), numerisch schwer. **Besser:** topologisch. Die halbpropagierende Lösung (regulär, geschlossener Kanal abklingend) hat bei reellem ρ das Fernfeld c₁ cos(qr) + c₂ sin(qr). Umlaufzahl von (c₁, c₂) auf einer kleinen Schleife um (ρ\*, ω\*²): ±1 heißt exakt, 0 heißt Beinahe-Null **[ES]** | offen. Glätte-Indiz spricht für H0 (Abschn. 7, G1), ist aber kein Exaktheitsnachweis |
| **Einzelresonanz-Nullstelle** gegen **Friedrich-Wintgen** (zweiter Pol am selben Kanal) | FW verlangt einen Partnerpol, dessen Breite bei ω\* maximal wird, und eine Niveauabstoßung in Re ρ | Leitungsläufe: Argumentprinzip zählt **genau 1** l = 0-Pol im Kasten [1 − ω + 0,002, 1 + ω − 0,002] × Im ∈ [−0,1, 0,001]. Re ρ läuft glatt (dRe ρ/dω² ≈ 0,40, kein Knick). **FW mit Partner Γ < 0,1 zwischen den Schwellen ausgeschlossen**. Nicht ausgeschlossen: ein breiterer Partner oder einer oberhalb 1 + ω |
| Nullstelle durch **Vorzeichenwechsel von sp bei S = 2/3** gegen **Oszillation der offenen Welle über den Ball (Formfaktor)** | Formfaktor sagt eine *Folge* von Nullstellen mit Δ(q·R) ≈ π voraus, die sich zur dünnen Wand hin (ω² → 0,5) häufen. Der sp-Mechanismus sagt wenige, an die S = 2/3-Geometrie gebundene Nullstellen voraus. Theorie-Experiment: sp → \|sp\| im Code | offen **[ES]** |
| **linear exakt null** gegen **nichtlinear verbleibende Dämpfung** bei ω\* | Amplitudenabhängigkeit: bei ω\* Abklingrate ∝ η² und A ∝ t^(−1/2); abseits (z. B. 0,76) η-unabhängig exponentiell | offen; Werkzeug zeit0 mit η = 0,001 und 0,01 vorhanden |
| **d-Brücke:** Kreuzung der Nullstellenkurve gegen glattes Extremum | signiertes M(d) bei festem ω² wechselt das Vorzeichen (Kreuzung) oder nicht | offen |

## 5 Theorieskizze für die Nullstelle (Frage 4) [ES, gestützt auf die Quellen in 2.3 und 2.4]

**Gleichungen** (aus PLAN.md):
- U'' = [dp + l(l+1)/r² − (ω+ρ)²] U + sp V
- V'' = sp U + [dp + l(l+1)/r² − (ω−ρ)²] V
- dp = 1 − 4S + 4,5 S², sp = −2S + 3S² = S(3S − 2)
- Für reelles ρ im Fenster (1 − ω, 1 + ω) sind alle Koeffizienten **reell**.

**(i) Feshbach- und Goldene-Regel-Bild (qualitativ; die starke Kernkopplung sp ≈ 1,6 macht es nur zu einer Skizze):**
- Γ(ω) ≈ π·M(ω)²·n(E), mit M(ω) = ∫ χ_E(r) sp(r) φ_c(r) dr.
  - φ_c ist der Zustand des geschlossenen V-Kanals.
  - χ_E ist die reguläre Streulösung des offenen U-Kanals bei E = (ω+ρ)², **im verzerrten Potential dp** (Lehre aus
    Zhang u. a. 2020).
- M ist reell und stetig in ω. Ein Vorzeichenwechsel ist darum generisch, nicht fein abgestimmt.
- Daraus folgt **Γ ≈ C·(ω² − ω\*²)²**.
- Genau diese Struktur ("signed overlap", reeller Formfaktor) nutzen Inagaki & Murakami für die nichtlineare Version.

**(ii) Warum die Nullstelle exakt sein kann, trotz Cornean u. a. (Zählargument):**
- Bei reellem ρ hat das System vier reelle Lösungen, zwei davon sind regulär bei r = 0.
- Ein L²-Zustand verlangt drei lineare Bedingungen auf diesem 2D-Raum:
  - kein e^{+κr} im geschlossenen Kanal
  - kein cos(qr) im offenen Kanal
  - kein sin(qr) im offenen Kanal
- Das heißt: Die reelle 3×2-Matrix hat höchstens Rang 1. Das sind **zwei reelle Bedingungen für zwei reelle
  Unbekannte (ρ, ω²)**.
- Folge: Isolierte exakte BIC sind generisch (Kodimension 1 im Parameter ω²). Das passt zur Zählung bei eingebetteten
  Solitonen ("codimension-one") und zur Einzelresonanz-BIC der Photonik.
- Bei N_offen = 2 wären es vier Bedingungen, also Kodimension 3. Entlang ω allein gäbe es dann nur Minima.
- Cornean u. a. betrachten eine Störungsfamilie εW, in der nur ε läuft und die FGR-Nullstelle vorgegeben ist. Dort
  bleibt eine Breite O(ε⁴). Mit einem zusätzlichen frei wählbaren Parameter (bei uns ω²) verschiebt sich die exakte
  Nullstelle nur um einen Betrag höherer Ordnung, statt zu verschwinden.
- In (ρ, ω², d) ist die Nullstellenmenge eine Kurve ω\*²(d). Das erklärt einen nicht monotonen Verlauf der d-Brücke,
  falls die Kurve bei ω² = 0,7 gekreuzt wird.

**(iii) Quantitativer Abgleich mit unseren Zahlen (Schreibtischrechnung ohne Python):**
- Grobtabelle, signiertes √Γ:

  | ω² | 0,76 | 0,78 | 0,79 | 0,80 | 0,81 | 0,82 | 0,84 |
  |---|---|---|---|---|---|---|---|
  | √Γ | +0,0447 | +0,0200 | +0,00837 | ∓0,00237 | −0,01183 | −0,01949 | −0,0295 |

- Ein quadratisches M(x), x = ω², gefittet **ohne** den Punkt 0,80 aus 0,78/0,79/0,81/0,82: M ≈ −0,00239 − 1,0·(x − 0,80)
  + 6,6·(x − 0,80)².
- Es sagt Γ(0,80) = 5,7e-6 voraus, gemessen 5,6e-6.
- Vorab daraus vorhergesagt: x\* ≈ 0,7977 und Γ(0,796/0,797/0,798/0,799/0,7995/0,801) ≈
  3,3e-6/5,6e-7/1,0e-7/1,9e-6/3,7e-6/1,25e-5.
- Feinläufe der Leitung (lauf-lokal/bic-c,d,e.log, Stufe h = 0,005): 3,10e-6 / 4,99e-7 / 1,12e-7 / 1,86e-6 / 3,50e-6 /
  1,14e-5.
- Signierte Steigungen: −1,054, −1,041, −1,028, −1,016, −1,003 (glatt).
- Ergebnis: **ω\*² = 0,79768 (ω\* ≈ 0,8931), Re ρ\* ≈ 1,7446, Γ ≈ 1,07·(ω² − 0,79768)²**.
- An der Nullstelle: offene Wellenzahl q = √((ω+ρ)² − 1) ≈ 2,44, geschlossener Abfall κ = √(1 − (ω−ρ)²) ≈ 0,52.

**(iv) Was an der Nullstelle nichtlinear übrig bleibt:**
- Die Quellen 2. Ordnung schwingen mit ω ± 2ρ (≈ 4,38 und −2,60). Beide Kanäle sind offen.
- Der nichtlineare FGR-Koeffizient ist dann eine Summe zweier Quadrate. Generisch ist er ≠ 0.
- Vorhersage: bei ω\* algebraisches Abklingen A ∝ t^(−1/2) (Manton-Merabet-Typ), nicht exponentiell.
- Das Dämpfungsminimum verschiebt sich ∝ A², analog zur "A² displacement" bei Inagaki & Murakami.
- Zusätzlich verschiebt eine endliche Störung Ladung und ω des Balls. Ein realer Ball sitzt also nicht genau auf ω\*.

## 6 Was eine Rechnung als nächstes prüfen sollte

- **N1 Exaktheit, entscheidend:** Windungszahl von (c₁, c₂), dem Fernfeld der halbpropagierenden Lösung nach
  Ciurla-Randbedingungen (3.14), auf einer kleinen Schleife um (ρ, ω²) = (1,7446, 0,79768).
  - Die Normierung der halbpropagierenden Lösung darf auf der Schleife nicht durch null gehen. Ciurla u. a. sehen bei
    η₂(0) = 1 einen solchen Normierungspol (Abb. 6), also z. B. auf die Gesamtnorm im Ball normieren.
  - Alternative: min_ρ A_rad(ρ; ω²) muss linear in \|ω² − ω\*²\| gegen null gehen.
  - Kosten: billig, radiale ODE.
- **N2 Eigenfunktion:** Bei (ρ\*, ω\*) die Norm ∫(\|U\|² + \|V\|²)dr gegen den Rand R prüfen. Konvergenz heißt L²-Zustand.
- **N3 Weitere Nullstellen:** l = 0-Scan über ω² = 0,55 … 0,92 in 3D.
  - Zahl und Abstände gegen q·R_Q auftragen.
  - Das trennt Formfaktor- und sp-Vorzeichen-Mechanismus.
  - Zusätzlich das Überlappintegral bei r(S = 2/3) aufteilen.
- **N4 1D und d-Brücke:** Signiertes M(d) bei ω² = 0,7 und Γ(ω²) in 1D.
  - Liegt der schmale 1D-Pol (Γ = 6,7e-5) nahe einer 1D-Nullstelle?
  - Der Ciurla-Wert 1,18e-5 (β = 1/4, ω² = 0,75) ebenfalls?
- **N5 β-Familie:** U = S − S² + βS³. Die Nullstellenlinie ω\*²(β) muss stetig sein, wenn der Mechanismus generisch ist.
  Bei β = 1/4 wäre der Anschluss an publizierte Zahlen möglich.
- **N6 Nichtlinear:** zeit0 bei ω\*² = 0,7977 und bei 0,76, mit η = 0,001, 0,003, 0,01.
  - Bei ω\*: Abklingrate ∝ η², A ∝ t^(−1/2).
  - Bei 0,76: η-unabhängig, Rate 2Γ = 4e-3.
  - Zusätzlich die Lage des Dämpfungsminimums gegen η².
- **N7 Krein-Signatur** der Eigenfunktion bei ω\* (symplektische Norm).
  - Positiv passt zu "Resonanz auf beiden Seiten", wie gemessen.
  - Negativ hieße nach Cuccagna u. a. [S]: Instabilität statt Resonanz. Das widerspräche den Daten.
- **N8** Wenn Zeit bleibt: l = 1 und l = 2 auf analoge Nullstellen prüfen.

## 7 Gegensweep-Befunde (Regel 4): Was war zu selbstverständlich?

- **G1, geprüft: "Die Tabelle zeigt einen Pol, und der Einbruch ist eine einfache Nullstelle."**
  - Die Vorhersage aus der Grobtabelle habe ich in der Arbeitsdatei eingetragen, bevor ich die Feinwerte vollständig las.
  - Sie trifft die Leitungsläufe auf ≤ 12 % in Γ.
  - Re ρ ist glatt, das Argumentprinzip zählt 1 Pol. Damit ist Pol-Identität plausibel und FW (Partner Γ < 0,1)
    ausgeschlossen.
  - Grobe Schranke für einen Boden: Γ_min ≲ 1e-8 **[ES]**. Sie setzt ein glattes M voraus.
  - Der numerische Stufenunterschied bei 0,798 ist 1e-10 (h = 0,01 gegen 0,005).
- **G2, geprüft: Autoren von 2405.06591.** Ciurla, Dorey, Romańczukiewicz, Shnir. Forgács und Lukács sind keine
  Autoren; die Zuordnung im Auftrag ist falsch. Forgács, Lukács und Romańczukiewicz sind Autoren von "Negative
  radiation pressure exerted on kinks", arXiv:0802.0080 [S].
- **G3, geprüft: "Nur ein Kanal offen".** Das gilt für 0,76 … 0,84 mit Reserve 0,14 … 0,16. Die Extrapolation in den
  dünnwandigen Bereich ist **[ES]**.
- **G4, teilgeprüft: "Bosonsterne haben nichts".** Nur Suchtreffer [S]. Gravitationsgekoppelte QNM-Literatur ist nicht
  gelesen.
- **G5, nicht geprüft:**
  - Konvention Γ = −Im ρ gegen 2·Im ρ. Für die Lage der Nullstelle egal, für Vergleiche mit Ciurla (+Im-Konvention) nicht.
  - Innenmoden der kubisch-quintischen NLS (unser nichtrelativistischer Grenzfall).
  - Russischsprachige Q-Ball-Literatur.
  - Annales Henri Poincaré 2026 "Resonances, Energy Transfer and Radiation in Hamiltonian Nonlinear…" (hinter
    Anmeldung) [S].

## 8 Kalibrierung

- **(a) Gemessen:**
  - Γ-Werte aus Auftrag und Leitungsläufen (bic-a … e)
  - Kleinster Wert 1,12e-7 bei ω² = 0,798
  - Die zitierten Literaturaussagen
- **(b) Nützlich verdichtet:**
  - Fit Γ ≈ 1,07·(ω² − 0,79768)²
  - Zählargument (Kodimension)
  - FGR-Bild
  - Einordnung in fünf Wege zu "keine Abstrahlung"
  - Regime-Tabelle
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "Γ ist *exakt* null": nicht gemessen. Die Glätte des signierten M ist mit einem Boden ≲ 1e-8 ebenso verträglich.
  - "In der Literatur unbekannt": eine Abwesenheitsaussage mit begrenzter Suchabdeckung (englisch, arXiv, 2024–2026 plus
    Klassiker).
  - Welcher Untermechanismus (sp-Vorzeichen oder Formfaktor) wirkt: ungetestet.
- **Warnzeichen:** Meine Sicherheit ist im Lauf gestiegen, nachdem die Vorhersage die Feinwerte traf, von "Nullstelle
  plausibel" zu "exakte BIC". Gleichzeitig ist die Frage feiner geworden: Es geht jetzt um exakt null gegen Boden
  ≤ 1e-8. Der Treffer prüft aber nur die Glätte, nicht die Exaktheit. Erst N1 entscheidet.

## 9 Offene Fragen

1. Ist (ρ\*, ω\*²) ≈ (1,7446, 0,79768) ein echter L²-Eigenwert (N1, N2)?
2. Wie viele Nullstellen hat Γ(ω²) im stabilen Bereich, und häufen sie sich zur dünnen Wand hin (N3)?
3. Kreuzt die Nullstellenkurve ω\*²(d) die Linie ω² = 0,7 (d-Brücke, N4)?
4. Ist der Ciurla-Pol bei β = 1/4 nahe einer 1D-Nullstelle (N4, N5)?
5. Nichtlineares Zerfallsgesetz bei ω\* (N6), Krein-Signatur (N7).
6. Literatur nicht abgedeckt: siehe G4 und G5.
7. Sollte eine L4-Mitteilung an Ciurla u. a. oder Inagaki & Murakami gehen? Das ist eine Frage an die Leitung, nicht
   entschieden.

## 10 Quellenliste

- Ciurla D., Dorey P., Romańczukiewicz T., Shnir Y. (2024): Perturbations of Q-balls: from spectral structure to
  radiation pressure. arXiv:2405.06591v2. https://arxiv.org/abs/2405.06591
  - lokal: coordination/resonance-20260930/papers/
- Evslin J., Liu H., Romańczukiewicz T., Shnir Y., Wereszczyński A., Ziobro P. (2026): Linearized Q-Ball Perturbations.
  arXiv:2604.07713. https://arxiv.org/abs/2604.07713
- Kovtun A., Nugaev E., Shkerin A. (2018): Vibrational modes of Q-balls. arXiv:1805.03518.
  https://arxiv.org/abs/1805.03518
- Azatov A., Ho Q. T., Khalil M. M. (2024): Q-ball perturbations with more details: linear analysis vs lattice.
  arXiv:2412.13885; PRD 111, 096010 (2025) [S]. https://arxiv.org/abs/2412.13885
- Blaschke F., Romańczukiewicz T., Sławińska K., Wereszczyński A. (2025): Q-ball polarization – a smooth path to
  oscillons. arXiv:2502.20519. https://arxiv.org/abs/2502.20519
- Canillas Martínez D., Dorey P., Romańczukiewicz T., Saffin P. M., Sławińska K., Wereszczyński A. (2025): Oscillons and
  bubbles in Q-ball dynamics. arXiv:2509.03192; JHEP 12 (2025) 154 [S]. https://arxiv.org/abs/2509.03192
- Chen Q., Andersson L., Li L. (2025): Stability analysis for Q-balls with spectral method. arXiv:2509.18656.
  https://arxiv.org/abs/2509.18656
- Saffin P. M., Xie Q.-X., Zhou S.-Y. (2022): Q-ball Superradiance. arXiv:2212.03269. https://arxiv.org/abs/2212.03269
- Inagaki T., Murakami Y. (2026): Open-channel radiation zeros and nonlinear damping of a critical-bubble internal mode.
  arXiv:2609.15056. https://arxiv.org/abs/2609.15056
- Zhang H.-Y., Amin M. A., Copeland E. J., Saffin P. M., Lozanov K. D. (2020): Classical Decay Rates of Oscillons.
  arXiv:2004.01202. https://arxiv.org/abs/2004.01202
- Cyncynates D., Giurgica-Tiron T. (2021): The Structure of the Oscillon: The Dynamics of Attractive Self-Interaction.
  PRD 103, 116011; arXiv:2104.02069. https://arxiv.org/abs/2104.02069
- Champneys A. R., Malomed B. A., Yang J., Kaup D. J. (2001): "Embedded solitons": solitary waves in resonance with the
  linear spectrum. Physica D 152–153, 340. https://arxiv.org/abs/nlin/0005056
- Yang J., Malomed B. A., Kaup D. J. (1999): Embedded solitons in second-harmonic-generating systems. PRL 83, 1958 [S].
  https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.83.1958
- Manton N. S., Merabet H. (1997): φ⁴ kinks – gradient flow and dynamics. Nonlinearity 10, 3; arXiv:hep-th/9605038.
  https://arxiv.org/abs/hep-th/9605038
- Alonso-Izquierdo A., Miguélez-Caballero D., Nieto L. M. (2023): Wobbling kinks and shape mode interactions in a
  coupled two-component φ⁴ theory. arXiv:2310.15738. https://arxiv.org/abs/2310.15738
- Campos J. G. F., Mohammadi A. (2021): Wobbling double sine-Gordon kinks. arXiv:2103.04908.
  https://arxiv.org/abs/2103.04908
- Guo H., Evslin J., Bolognesi S. (2026): (De-)Exciting the Third Pöschl-Teller Kink. arXiv:2603.12590.
  https://arxiv.org/abs/2603.12590
- Timmermans A., Kalmykov A. (2026, selbstpubliziert): Exact Radiation Form Factor and Open-System Quantisation of the φ⁴
  Kink Shape Mode. Zenodo 22686301. https://zenodo.org/records/22686301
- Hsu C. W., Zhen B., Stone A. D., Joannopoulos J. D., Soljačić M. (2016): Bound states in the continuum. Nature Reviews
  Materials. https://www.mit.edu/~soljacic/BIC_review-NatRevMat.pdf
- Friedrich H., Wintgen D. (1985): Interfering resonances and bound states in the continuum. PRA 32, 3231 [S, zitiert
  nach Hsu u. a.]
- Soffer A., Weinstein M. I. (1999): Resonances, Radiation Damping and Instability in Hamiltonian Nonlinear Wave
  Equations. Invent. Math.; arXiv:chao-dyn/9807003. https://arxiv.org/abs/chao-dyn/9807003
- Cornean H. D., Jensen A., Nenciu G. (2015): Metastable states when the Fermi Golden Rule constant vanishes. CMP 334,
  1189; arXiv:1311.7502. https://arxiv.org/abs/1311.7502
- Cuccagna S., Pelinovsky D. E., Vougalter V. (2005): Spectra of positive and negative energies in the linearized NLS
  problem. CPAM [S]. https://onlinelibrary.wiley.com/doi/abs/10.1002/cpa.20050
- Yoshida S., Eriguchi Y., Futamase T. (1994): Quasinormal modes of boson stars. PRD 50, 6235 [S].
  https://journals.aps.org/prd/abstract/10.1103/PhysRevD.50.6235
- Projektdateien:
  - Auftrag claude-primary 30.09.2026 (Γ-Tabelle)
  - /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/resonanz3d/lauf-lokal/bic-a.log bis bic-e.log (Feinläufe der
    Leitung)
  - /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/resonanz3d/PLAN.md (Gleichungen, S(0)-Werte)

## Einfach gesagt

Ein Q-Ball kann "atmen". Dabei gibt er normalerweise langsam Energie als Welle nach außen ab. Bei einer ganz bestimmten
Drehfrequenz (ω² ≈ 0,798) verschwindet diese Abgabe fast vollständig, weil sich die Wellen aus verschiedenen Teilen des
Balls gegenseitig auslöschen. So ein Auslöschen ist aus der Optik bekannt ("gefangenes Licht", BIC) und seit zwei Wochen
auch für Blasen in einem ähnlichen Feldmodell. Für Q-Bälle haben wir es in der Literatur nicht gefunden. Ob die Abgabe
dort genau null ist oder nur winzig, muss noch eine gezielte, billige Rechnung zeigen (Windungszahltest).
