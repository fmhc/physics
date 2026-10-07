# L4-Prüfung Runde 7: Exakte Nullstellen der Q-Ball-Atmungsbreite Γ(ω) – steht das in der Literatur?

- Auftrag: claude-primary, Runde 7 (Finn: "finden wir das in der literatur wieder?"). Bearbeiter: Anthropic-Agent (Opus),
  reine Literaturprüfung mit Schreibtischrechnung.
- Beginn: 2026-09-30 04:59:29 CEST (date). Schreibbeginn: 05:12:49 CEST (date). Ende: letzte Zeile (nach dem Schreiben
  mit date gemessen).
- Aufbauend auf: RUNDE-06/resonanz3d/L4-BIC-LITERATUR.md (Vorarbeit, 03:17 bis 03:37) und RUNDE-06.md, Abschnitt "Codex,
  Feshbach-Diagnose". Was dort schon gelesen wurde, ist hier mit **[V]** markiert und nicht wiederholt.
- Markierungen:
  - **[A]**: an der Quelle gelesen. Abstract oder Volltext roh per curl von arxiv.org geholt, also ohne
    Zusammenfassungsmodell dazwischen.
  - **[S]**: nur Suchtreffer oder Suchmaschinen-Zusammenfassung.
  - **[V]**: in der Vorarbeit gelesen, hier nicht erneut.
  - **[ES]**: eigener Schluss oder Hypothese.
- Wörtliche Zitate: höchstens 15 Wörter, aus dem Rohtext.
- Arbeitsdatei mit Abrufprotokoll (Erwartung vor jedem Abruf, B1 bis B33):
  `/tmp/claude-1000/-home-fmh-fmhc-physics/76c41c65-1089-4cc3-bcfe-f088e91d4721/scratchpad/ARBEITSFELD-L4-BIC-FAMILIE.md`
  (Scratchpad, flüchtig)
- **Zwei Verfahrensfehler, offen gemeldet:**
  1. Im ersten Abrufbefehl (05:01) stand versehentlich ein leerer Aufruf `python3 -c "print(1)"`, die Ausgabe wurde
     verworfen. Es gab keine Rechnung, trotzdem ist das ein Verstoß gegen "keine lokalen Rechnungen (python)".
  2. Die Uhrzeiten im Abrufprotokoll B3 bis B28 waren geschätzt. Das habe ich um 05:10:10 per date bemerkt und in der
     Arbeitsdatei berichtigt. In diesem Bericht stehen nur gemessene Zeiten.

## 0 Kurzantwort: TEILWEISE BEKANNT – der Q-Ball-Befund selbst ist nicht gefunden und läuft einer ausgesprochenen Erwartung der Mathematik zuwider

1. **Bekannt ist der Mechanismus.** Die Abstrahlung ist null, wo ein reeller Überlapp mit der offenen Welle das Vorzeichen
   wechselt: 3D-Blase, nichtlinear, fünf Nullstellen (Inagaki und Murakami, 2609.15056: **existiert**, roh geprüft);
   Optik 2026, computergestützt bewiesen (2609.23217); Oszillonen; eingebettete Solitonen.
2. **Bekannt ist die Zählung.** Eingebettete Eigenwerte überleben nur auf einer Menge der Kodimension m (m = offene Kanäle;
   Agmon, Herbst, Maad Sasane 2010). Bei m = 1 trifft eine Familie sie an isolierten Punkten, wie bei uns **[ES]**.
3. **Nicht gefunden** (auch in der 24-Monats-Suche): ein eingebetteter Eigenwert in der Linearisierung um einen Q-Ball oder
   ein anderes Soliton, eine 3D-Kurve Γ(ω) für Q-Bälle, ein Soliton mit mehreren solchen Parameterwerten.
4. **Kern:** Laut Cuccagna und Maeda erwartet die NLS-Mathematik bei Grundzuständen keine eingebetteten Eigenwerte
   ("unproved yet", numerisch nie gesehen). Unser knotenfreier Q-Ball mit positiver Krein-Norm stünde dagegen, allerdings im
   NLKG- statt NLS-Regime und als Familie statt Einzelsoliton (Abschnitt 5).

## 1 Erwartungsverstöße (das Wichtigste zuerst)

1. **Die Mathematik erwartet für Grundzustände keine eingebetteten Eigenwerte, und niemand hat numerisch je einen gesehen.**
   - Erwartung: Die Bedingung "keine eingebetteten Eigenwerte" steht dort nur als technische, generische Annahme.
   - Befund: Cuccagna und Maeda 2020 (arXiv:2009.00573, Bemerkung 3.2) **[A]** formulieren sie als inhaltliche Erwartung:
     - "It is expected, but unproved yet, that, since φω is a ground state"
     - "no embedded eigenvalues have been detected numerically in the case of ground states"
     - Für Nicht-Grundzustände: "cannot have positive Krein signature"
     - Bemerkung 3.3: Eingebettete Eigenwerte seien "unstable". Nach einer Störung habe der neue Operator sie "in general"
       nicht mehr.
   - Korrigierte Erwartung **[ES]**: Unser Befund ist kein Randdetail, sondern berührt eine offene Vermutung.
     - Versöhnt wird er durch zwei Moderatoren: Familie statt Einzelsoliton (Kodimension 1) und NLKG statt NLS.
     - Ob die Vermutung auf NLKG-Q-Bälle übertragbar ist, hat nach Recherchestand niemand behauptet (Gegensweep G3).
2. **In 1D gibt es keine eingebetteten Eigenwerte, und zwar als Satz, nicht nur generisch.**
   - Collot, Germain und Pacherie 2025 (arXiv:2503.02957) **[A]**, Satz 1.1: In 1D gilt für gerades, positives,
     exponentiell abfallendes Q mit Q' < 0 auf (0, ∞) für jedes λ im wesentlichen Spektrum E_λ = {0}.
   - Dazu Li und Yang, Invent. Math. 2026: keine eingebetteten Eigenwerte für die 3D-kubische NLS **[S]**, weil Springer
     den Abruf blockierte.
   - Erwartet hatte ich nur Aussagen über generische Nichtlinearitäten.
   - Folge: Unser 1D-Negativbefund passt zum Satz. Die Schreibtischrechnung im Gegensweep (G2) zeigt aber, dass unser
     1D-Raster fast ganz dort lag, wo die Kopplung ihr Vorzeichen gar nicht wechselt. Er testet also wenig.
3. **Exakte Abstrahlungsnullstellen sind 2026 rigoros bewiesen worden, aber in der Optik.**
   - Ayala, Blanco, Cakoni, Hovsepyan, Vogelius, arXiv:2609.23217 (19.09.2026) **[A]**: Es gibt diskrete Frequenzen, bei
     denen "the second-harmonic field generated does not persist outside the compact support".
   - Der Beweis ist computergestützt (Newton-Kantorovich mit Intervallarithmetik).
   - Erwartet hatte ich nichts so Nahes. Folge: Der Weg vom numerischen Umlaufzahltest zu einem Beweis ist erprobt
     (nächster Schritt, Abschnitt 10).
4. **Codex' zweite Literaturstelle hat eine verschwindende Zerfallskonstante, aber durch einen anderen Mechanismus.**
   - García Martín-Caro, Queiruga, Wereszczyński 2025 (arXiv:2501.02589) **[A]**: "the decay constant vanishes at the
     spectral wall".
   - Das ist eine Schwelle: Die Modenfrequenz erreicht die Kontinuumskante. Eine Überlapp-Nullstelle ist es nicht.
   - Es handelt sich um ein Spielmodell aus zwei Skalarfeldern mit Feshbach-Resonanzen, nicht um Q-Bälle. Erwartet hatte
     ich überhaupt keine Nullstelle.
5. **Oszillonen: Es gibt einen exakten Nullpunkt der Abstrahlung im Raum der Potentiale.**
   - Ollé, Pujolàs, Rompineve 2021 (arXiv:2012.13409) **[A]**: Die Familie hängt stetig mit einem Ausnahmepotential
     zusammen, "that admits eternal oscillon solutions".
   - Erwartet hatte ich nur "stark unterdrückt".
   - Welches Potential das ist, habe ich nicht geprüft. **[ES]** Vermutlich logarithmisch.
6. **Asad und Simpson 2011 zeigen Abwesenheit, nicht Existenz.**
   - Erwartet hatte ich ein numerisches Beispiel für einen eingebetteten Eigenwert.
   - Befund (arXiv:1101.2485) **[A]**: "we prove the absence of embedded eigenvalues", computergestützt, unter anderem für
     die 3D-kubisch-quintische NLS.
   - Die Richtung der Mathematik ist durchgehend "ausschließen", nicht "finden".

Keine Verstöße (je eine Zeile), siehe Abschnitte 2 bis 4:
- Inagaki und Murakami existieren wie beschrieben.
- Bizoń und Romańczukiewicz 2026, Léger und Pusateri, Li und Lührmann, Bambusi und Cuccagna, Tsai und Yau, Lei, Liu und
  Yang (beide Arbeiten), Maeda 2014, Cuccagna und Maeda 2024: FGR jeweils als Annahme bzw. als Schwellenmechanismus.
- Kinks (2310.15738): Nullstellen dort durch eine Schwelle.
- Bosonsterne und die Oszillon-Arbeiten von 2026: keine Nullstelle.

## 2 Frage 1: Mathematische Literatur zur asymptotischen Stabilität

**Zuerst eine Begriffstrennung [ES, gestützt auf die Quellen unten].** Frage 1 fasst zwei verschiedene Bedingungen
zusammen.

- **(i) Linear, spektral:** "Die Linearisierung hat keine eingebetteten Eigenwerte." Das ist eine Spektralannahme (H3/H4
  bei Cuccagna und Maeda). Collot, Germain und Pacherie schreiben, die asymptotische Stabilität sei bewiesen "under the
  assumption that embedded spectrum is absent" **[A]**.
- **(ii) Nichtlinear:** Die "Fermi Golden Rule" (FGR) verlangt, dass die Kopplung der ersten Harmonischen einer
  *isolierten* inneren Mode an das Kontinuum nicht null ist.
- **Unser Befund gehört zu (i).** Sofern die Nullstelle exakt ist, ist die Atmungsmode bei ω* ein echter L²-Eigenwert im
  Kontinuum.
  - Nahe ω* ist Γ ≈ C·(ω² − ω\*²)² [V] die gewöhnliche *lineare* FGR für die Auflösung eines eingebetteten Eigenwerts
    unter einer Parameterstörung.
  - Der Rahmen dafür ist Howland bzw. Agmon, Herbst und Maad Sasane.
  - Eine *nichtlineare* FGR-Nullstelle (Typ (ii)) haben Inagaki und Murakami.

| Quelle | Aussage (wörtlich ≤ 15 Wörter) | Bezug zu uns |
|---|---|---|
| Cuccagna, Maeda 2020, Survey II, arXiv:2009.00573 [A, Volltext per pdftotext] | Bem. 3.2: "no embedded eigenvalues have been detected numerically in the case of ground states"; Bem. 1.6: "The generic condition has not been proved rigorously, except in very special situations"; die Koeffizienten hängen analytisch von ω ab (bei analytischer Nichtlinearität); Gl. (2.34): \|z(t)\| = \|z(0)\|(1 + NΓ\|z(0)\|^{2N} t)^{−1/(2N)} | direkte Gegen-Erwartung (Verstoß 1). Analytizität in ω heißt: Nullstellen sind isoliert, sofern der Koeffizient nicht identisch null ist, passend zu unseren isolierten Nullstellen **[ES]** |
| Agmon, Herbst, Maad Sasane 2010, "Persistence of embedded eigenvalues", arXiv:1008.2099 [A] | Die den Eigenwert erhaltenden Störungen bilden "a smooth submanifold of co-dimension m" | abstrakter Anker für das Zählargument der Vorarbeit: m = 1 offener Kanal → Kodimension 1 → isolierte ω* in einer Familie, stetig wandernd mit β (0,700 → 0,856) **[ES]**. Einschränkung: Der Satz gilt für selbstadjungierte Operatoren. Unsere Linearisierung ist hamiltonsch; die Übertragung (reelles ρ, positive Krein-Norm) ist **[ES]** |
| Collot, Germain, Pacherie 2025, arXiv:2503.02957 [A, Satz 1.1 im Volltext] | "ground states do not have embedded eigenvalues in the essential spectrum of their linearized operators" (1D) | 1D-Regime (Verstoß 2) |
| Li, Yang 2026, "The linearized cubic NLS has no embedded eigenvalue", Invent. Math., DOI 10.1007/s00222-026-01419-3 [S] | laut Suchzusammenfassung 3D, eigene Vergleichsargumente für höhere Drehimpulse | 3D-NLS: kubisch ohne eingebetteten Eigenwert, unser Nichtrelativ-Grenzfall ω → 1 **[ES]** |
| Asad, Simpson 2011, J. Math. Phys. 52, 033511; arXiv:1101.2485 [A] | "we prove the absence of embedded eigenvalues for a collection of nonlinear Schrodinger equations" | Abwesenheit, computergestützt (Verstoß 6) |
| Soffer, Weinstein 1999 [V] | FGR ≠ 0 "for generic nonlinear Hamiltonian perturbations" | FGR ist Generizitätsannahme |
| Bambusi, Cuccagna 2009 (arXiv), arXiv:0908.4548 [A] | "a genericity assumption on the nonlinearity" | ebenso, für NLKG mit Potential |
| Léger, Pusateri (Mem. AMS 2026 laut Zitat bei Inagaki und Murakami), arXiv:2112.13163 [A] | "Provided a natural Fermi-Golden rule holds"; \|a(t)\| ≈ t^{−1/2} | quadratische Nichtlinearität, 3D |
| Li, Lührmann 2023, arXiv:2203.11371 [A] | "an explicitly verified Fermi Golden Rule" | FGR wird fallweise ausgerechnet |
| Tsai, Yau 2002, CPAM 55, 153 (Fundstelle laut Suchtreffer); arXiv:math-ph/0011036 [A] | "its eigenvalues satisfy some resonance condition"; resonanzdominiert t^{−1/2} | Nichtentartung als Annahme |
| Gang, Sigal 2006 (arXiv), arXiv:math-ph/0603060 [A, nur Abstract] | "under certain conditions on the potentials and initial conditions" | FGR-Bedingung nur im Volltext, nicht gelesen |
| Buslaev, Perelman 1993, St. Petersburg Math. J. 4, 1111 [S] | laut Suchtreffer "Wiener condition (a version of the Fermi Golden Rule)" | nicht gelesen |
| Kowalczyk, Martel, Muñoz, Van Den Bosch 2020, arXiv:2008.01276 [A, Abstract] | hinreichende Bedingung für Kinks; Anwendungen auf P(φ)₂ und Doppel-Sine-Gordon | im Abstract kein Beispiel, in dem die Bedingung versagt |
| Cornean, Jensen, Nenciu 2015 [V] | "when the Fermi Golden Rule constant vanishes": Rate O(ε⁴) | linear; Familie mit einem Parameter ε, Nullstelle vorgegeben |
| Lei, Liu, Yang 2022, arXiv:2201.06490 [A]; dieselben 2023, arXiv:2307.16191 [A] | "weak resonance regime … 0 < 3ω < m"; allgemeiner Fall mit entarteten Eigenwerten | höhere Ordnung, weil Harmonische *unter* der Schwelle liegen (Schwellentyp) |
| Cuccagna, Maeda 2024, arXiv:2405.11763 [A] | FGR 3. und 4. Ordnung; 3. Ordnung "true for generic p"; 4. Ordnung FGR für einige p *angenommen* | Ausnahmewerte von p werden nicht bestimmt |
| Maeda 2014, arXiv:1412.3213 [A] | "We prove the existence of a 2-parameter family of small quasi-periodic in time solutions" (diskrete NLS) | ohne Resonanz ewige Lösungen; Mechanismus laut Suchtreffer Nichtresonanz (Band) [S] |
| Kevrekidis, Pelinovsky, Saxena 2014 (arXiv), arXiv:1412.1522 [A] | Kopplung von "internal modes of negative energy with the wave continuum" → nichtlineare Instabilität | Krein-Vorzeichen entscheidet; bei uns laut bic2-PLAN positiv (nicht selbst geprüft) |

**Antworten auf Frage 1:**

- **(a) Versagen an isolierten Parameterwerten, eingebettete Eigenwerte:**
  - Für Typ (ii) ist das als Möglichkeit bekannt, denn "generic" schließt Ausnahmewerte ein. Ausgewiesen wird es aber
    nicht: Die Generizität ist "not proved rigorously, except in very special situations", und die numerische Prüfung hat
    "very little interest" gefunden (Cuccagna und Maeda).
  - Für Typ (i) erwartet die Literatur bei Grundzuständen Abwesenheit. Bewiesen ist sie in 1D allgemein (Collot,
    Germain, Pacherie) und in 3D für die kubische NLS (Li und Yang [S]).
  - Ein Soliton-Beispiel *mit* eingebettetem Eigenwert an isolierten Parameterwerten habe ich nicht gefunden.
- **(b) Mehrere Parameterwerte:**
  - In der Soliton-Mathematik: nicht gefunden.
  - Außerhalb gibt es Beispiele:
    - Inagaki und Murakami: fünf Nullstellen, nichtlinear
    - Ayala u. a.: diskrete Frequenzen in der Optik
    - Champneys u. a. [V]: eingebettete Solitonen bei "isolated frequency values"
- **(c) Lebensdauer:**
  - Allgemeines Gesetz (Cuccagna und Maeda, Gl. 2.34, heuristisch): \|z\| ~ t^{−1/(2N)}, wobei N + 1 die Ordnung der ersten
    offenen Harmonischen ist.
    - N = 1, quadratisch bzw. zweite Harmonische: t^{−1/2} (Léger und Pusateri; Bizoń und Romańczukiewicz 2026 [A];
      Manton und Merabet [V])
    - N = 2: t^{−1/4} (Soffer und Weinstein; Inagaki und Murakami an ihrer Nullstelle: "third-harmonic loss predicts
      A∼τ^{−1/4}, instead of the generic A∼τ^{−1/2} law" [A])
  - Linear verschwindende FGR in einer Störfamilie: Rate O(ε⁴) (Cornean u. a.).
  - Gar keine Resonanz: ewige quasiperiodische Lösungen (Maeda 2014).
  - **Für uns [ES]:** Bei ω* ist Γ linear null. Die nichtlineare Quelle zweiter Ordnung schwingt mit ω ± 2ρ, beide Kanäle
    sind offen [V]. Erwartet ist deshalb A ~ t^{−1/2} mit Rate ∝ η², solange dieser Koeffizient nicht zufällig auch
    verschwindet.

## 3 Frage 2: Physik-Literatur

**Inagaki und Murakami, arXiv:2609.15056, an der Quelle geprüft [A]:**
- Abrufe: HTTP 200 auf arxiv.org/abs und arxiv.org/html, roh per curl, ohne Zusammenfassungsmodell.
- Titel: "Open-channel radiation zeros and nonlinear damping of a critical-bubble internal mode".
- Autoren: Tomohiro Inagaki, Yuko Murakami. Eingereicht am 14.09.2026.
- Was die Arbeit zeigt:
  - System: 3+1 D, kritische O(3)-Blase (Nukleationssattel). Untersucht wird die kugelsymmetrische innere Mode.
  - Ihre *nichtlineare* Abstrahlung über die zweite Harmonische ist ein Überlapp zwischen Quelle und Kontinuums-Streuwelle:
    "This overlap can vanish through destructive interference as the supercooling is varied".
  - "A signed-overlap scan resolves five zeros in a finite parameter interval". Die Nullstellen liegen bei
    δ ≈ 0,055176 / 0,067599 / 0,087352 / 0,124166 / 0,227108 (δ in 0,05 bis 0,333). Drei davon liegen auf der Seite der
    dünneren Wand.
  - An einer Nullstelle folgt A ~ τ^{−1/4} statt τ^{−1/2}, und das Minimum verschiebt sich ∝ A².
  - Methodenwarnung, die auch für uns gilt: Ein grober Scan des nichtnegativen Γ₂ "can miss narrow zeros on the
    thinner-wall side".
  - Zitiert werden Cornean, Jensen und Nenciu: "Vanishing leading FGR constants also arise in linear metastability theory".
- Was fehlt (Volltext durchsucht): 0 Treffer für "Q-ball", "bound state in the continuum", "embedded", "Feshbach",
  "quasinormal". Ein linearer eingebetteter Eigenwert kommt nicht vor.
- **Unterschied zu uns:** Dort ist die Mode echt gebunden, und nur die Harmonische strahlt. Bei uns liegt die Mode selbst
  im Kontinuum, und die *lineare* Breite ist null.

**Q-Bälle:**
- Keine Γ(ω)-Kurve in 3D gefunden, auch nicht in der 24-Monats-Suche (Suchen B6, B25).
- Die Q-Ball-Linie bleibt 1+1-dimensional [V]:
  - Ciurla, Dorey, Romańczukiewicz, Shnir 2024: QNM nur bei einzelnen ω
  - Evslin u. a. 2026, arXiv:2604.07713: Feshbach-artige QNM, 1+1 D
  - Blaschke u. a. 2025; Canillas Martínez u. a. 2025
- Neu in den letzten 24 Monaten, jeweils ohne Breiten-Nullstelle:
  - Blaschke, Romańczukiewicz, Sławińska, Wereszczyński, "Unified theory of oscillons and modes", arXiv:2606.22680 [A]:
    Oszillon als lokalisierte Schwellen- bzw. Antibound-Mode
  - Bayarsaikhan, Evslin, Mahato, "Oscillon Floquet Modes …", arXiv:2607.15624 [A]
- Die 3D-Streuung (Azatov u. a. 2024 [V]) enthält Minima im Wirkungsquerschnitt, aber keine Polbreiten.

**Bosonsterne:**
- Macedo, Pani, Cardoso, Crispino 2013 (arXiv:1307.4812) [S]: "quasibound modes (i.e. modes with small but nonvanishing
  imaginary part)".
- Eine Nullstelle wird nicht berichtet. Volltext nicht gelesen.

**Oszillonen:**
- Inagaki und Murakami nennen als "direct precedents" Fodor u. a. 2009, Salmi und Hindmarsh 2012, Zhang u. a. 2020 [V]
  und Cyncynates und Giurgica-Tiron 2021 [V] [A, Zitatstelle].
- Dazu Ollé, Pujolàs, Rompineve 2021 [A]: Die Abstrahlung ist bei einem Ausnahmepotential exakt null (Verstoß 5).
- In allen Fällen geht es um die Abstrahlung eines ganzen Oszillons, nicht um die Breite einer eingebetteten Innenmode.

**24-Monats-Suche (Regel 7), durchgeführt:**
- Suchen: Q-Ball-QNM in 3D; "bound state in the continuum" mit Kink, Oszillon, Q-Ball oder Soliton 2025/2026; eingebettete
  Eigenwerte bei NLKG-Q-Bällen; Kink-Abstrahlungsnullstellen.
- Abrufe: 2603.18605, 2606.22680, 2607.15624, 2609.15056, 2609.23217, 2503.02957, 2405.11763.
- Ergebnis: Ein Q-Ball- oder Soliton-Pol mit linearer Breite null ist **nach Recherchestand nicht publiziert**. Das heißt
  nicht "sicher neu".

## 4 Frage 3: Kinks und Wackelmoden

| Modell | Befund | Quelle |
|---|---|---|
| φ⁴ | Wackelmode strahlt über die 2. Harmonische, Koeffizient ∝ 1/sinh(π√2), nicht null | Manton, Merabet 1997 [V]; Barashenkov, Oxtoby 2009 (zitiert bei Inagaki und Murakami) |
| gekoppeltes Zweikomponenten-φ⁴ | Abstrahlung verschwindet bei bestimmten κ, aber durch eine Schwelle: "this frequency is less than the threshold value"; "no radiation … for κ > 14.14" | Alonso-Izquierdo, Miguélez-Caballero, Nieto 2023, arXiv:2310.15738 [A, Volltext] |
| φ⁶ | der einzelne Kink hat keine Innenmode | Suchtreffer zu arXiv:1101.5951 [S] |
| Christ-Lee | schwach gebundene Kinks, Resonanzfenster; nichts zu Abstrahlungsnullstellen | Dorey, Gorina, Romańczukiewicz, Shnir 2023, arXiv:2304.11710 [S] |
| Doppel-Sine-Gordon | Wackelkinks, keine Nullstelle | Campos, Mohammadi 2021 [V]; KMMV-Kriterium [A, Abstract] |
| Kink-QNM (Dorey und Romańczukiewicz) | QNM-Breite ≈ 0,325√ε; Tunnelbarriere, keine Nullstelle | Dorey, Romańczukiewicz 2018, PLB 779, 117 [S] |
| Pöschl-Teller-Reihe σ = 3 | Amplituden endlich | Guo, Evslin, Bolognesi 2026 [V] |
| BPS-Spielmodell mit Feshbach-Resonanz | Zerfallskonstante null **an der Spektralwand** (Schwelle) | García Martín-Caro, Queiruga, Wereszczyński 2025 [A] |
| quadratisches 1D-KG-Soliton | Innenmode zerfällt mit FGR-Koeffizient ≠ 0 | Bizoń, Romańczukiewicz 2026, PRE 114, 024213; arXiv:2603.18605 [A] |

- **Antwort:** Ein Kink-Modell mit parameterabhängiger *Überlapp*-Nullstelle der Abstrahlung habe ich nicht gefunden.
- Gefunden habe ich drei andere Wege zu "strahlt nicht":
  - Schwelle bzw. Spektralwand
  - Integrabilität (Sine-Gordon)
  - Fehlen einer Innenmode (φ⁶)
- "Reflexionsfrei" heißt weiterhin nicht "abstrahlungsfrei" [V].
- **[ES]** Für Kinks spricht zusätzlich der 1D-Satz von Collot, Germain und Pacherie (für NLS bewiesen, nicht für Kinks)
  dagegen, dass *lineare* eingebettete Eigenwerte in 1D leicht auftreten. Kink-Analogien sind deshalb eher nichtlinear
  (Typ ii) zu erwarten.

## 5 Regime und Moderatoren (Regel 1)

Scheinbarer Widerspruch: Die Mathematik erwartet bei Grundzuständen keine eingebetteten Eigenwerte, und nach Störungen
verschwinden sie "in general". Wir sehen welche. Erste Hypothese: zwei Regime, keine Seite irrt.

| Moderator | Regime der Literatur | unser Regime | Wirkung **[ES]** |
|---|---|---|---|
| **Einzelsoliton gegen Familie** | fester Soliton-Parameter; ein eingebetteter Eigenwert ist nicht generisch (Bem. 3.3) | Ein-Parameter-Familie ω, dazu β | Kodimension 1 nach Agmon, Herbst, Maad Sasane: In der Familie sind isolierte Kreuzungen generisch und robust. ω\*(β) wandert stetig. Beide Aussagen gelten zugleich |
| **NLS gegen NLKG, relativistisch** | NLS-Grundzustände; Satz in 1D, 3D-kubisch | NLKG mit Re ρ ≈ 1,74 ≫ 1 − ω ≈ 0,11: kein NLS-Gegenstück | Zum Nichtrelativ-Grenzfall ω → 1 hin (3D kubisch nach Li und Yang: keine) zeigt das grobe β = 1/2-Raster zwischen 0,80 und 0,90 keine Nullstelle [V, RUNDE-06]. Passt, ist aber schwach |
| **Dimension 1 gegen 3** | 1D: Satz, nie | 3D, l = 0 | Der 1D-Beweis nutzt gerades Q mit Q' < 0. In 3D (l = 0) fehlt dieses Werkzeug, und die Translationsmode sitzt in l = 1 |
| **Vorzeichen der Kopplung sp = S(6βS − 2)** | – | wechselt bei S = 1/(3β) | ln(1 + S): kein Wechsel, keine Nullstelle. β-Trend: Die Schwelle 1/(3β) = 0,833 / 0,741 / 0,667 / 0,606 / 0,556 fällt mit β, die oberste Nullstelle steigt (0,700 bis 0,856). Die Richtung passt. Das ist eine notwendige Bedingung (Hypothese), keine Erklärung |
| **Wanddicke** | Inagaki und Murakami: weitere Nullstellen zur dünneren Wand | Folge 0,798 / 0,685 / (0,631) zur Dünnwandgrenze ω²_min = 1 − 1/(4β) = 0,5 | Formfaktor q·R ≈ nπ + φ. Mit dem Dünnwandradius R ∝ 1/(ω² − ω²_min) (Wandspannung gegen Druck) folgt 1/(ω\*² − 0,5) linear in n (Abschnitt 6) |
| **Zahl offener Kanäle m** | m ≥ 2: Kodimension ≥ 2 | m = 1 im Fenster (1 − ω, 1 + ω) | exakte Nullstellen entlang *eines* Parameters nur bei m = 1 |

- **Regel 6 [ES]:** Mindestens sechs Wege führen zu "strahlt nicht":
  - Schwelle bzw. Spektralwand
  - Symmetrie
  - Integrabilität
  - Friedrich-Wintgen
  - Überlapp-Nullstelle, linear
  - Überlapp-Nullstelle, nichtlinear
- Gemeinsame Größe ist die Projektion der Modenquelle auf die offenen On-shell-Streuzustände. Bei uns wirken zwei Wege
  zusammen: Die Drehsymmetrie trennt die Kanäle l ≠ 0 ab, danach bleibt eine akzidentelle lineare Überlapp-Null bei m = 1.

## 6 Unterscheidungspunkte (Regel 2)

| Erklärungspaar | wo sie messbar auseinanderlaufen | Stand |
|---|---|---|
| exakt null gegen Boden knapp über null | Umlauf ±1 ist nur dann ein Beweis, wenn W auf der Schleife fehlerkontrolliert ist (Intervallarithmetik wie Ayala u. a. 2026 und Asad und Simpson 2011). Ohne Fehlerschranke ist es starke Evidenz | Umlauf ±1 auf drei Schrittweiten, Gegenprobe 0 (Auftrag) |
| Formfaktor (Folge mit Häufung zur Dünnwand) gegen sp-Vorzeichen (wenige Nullstellen) | **Schreibtischvorhersage [ES]:** 1/(ω\*² − 0,5) = 3,36 und 5,40 aus den zwei exakten Nullstellen, Schritt 2,04. Nächste Nullstelle bei 1/x ≈ 7,44, also **ω² ≈ 0,634**. Das trifft den Kandidaten 0,631, der nicht in die Vorhersage einging. Mit dem Kandidaten (1/x = 7,63; Schritte 2,04 und 2,23) folgen **≈ 0,60 und ≈ 0,58**. Plausibilitätsprobe: Mit q ≈ 2,44 folgt aus Δ(1/x) ≈ 2,1 ein R ≈ 0,6/x, also R ≈ 2 bis 5 (Größenordnung plausibel, gegen die Profile nicht geprüft). Der sp-Mechanismus allein sagt keine unbegrenzte Folge voraus | offen; billig prüfbar mit der *signierten* Amplitude, nicht mit Γ ≥ 0 |
| 1D strukturell verboten (Analogon zu Collot, Germain, Pacherie) gegen "Vorzeichenwechsel nötig" | 1D, β = 1/2: S₀ = 1 − √(2ω² − 1). Ein Vorzeichenwechsel von sp braucht S₀ > 2/3, also **0,5 < ω² < 5/9 ≈ 0,556**. Allgemein 1 − 1/(4β) < ω² < 1 − 2/(9β), Breite 1/(36β). Kontrolle: ω² = 0,7 ergibt S₀ = 0,3675, der Wert aus Runde 6. Eine Nullstelle dort widerlegt die Übertragung des 1D-Satzes auf NLKG. Keine Nullstelle stützt sie | offen |
| NLS-Erwartung gegen NLKG | l = 0 mit signierter Amplitude zwischen 0,86 und 0,927 (Q_min). Die NLS-Linie erwartet dort keine Nullstelle | teilweise [V: Γ bis 0,90 ohne Nullstelle] |
| lineare Null gegen nichtlinear verbleibende Dämpfung bei ω\* | Zeitbereich: Bei ω\* A ~ t^{−1/2}, Rate ∝ η². Bei ω² = ω\*² ± δ exponentiell mit Γ ≈ 1,07·δ² [V]. Achtung: Der Stoß verschiebt ω (bic2-PLAN (c)) | Werkzeug vorhanden (zeit0, nlfit) |

## 7 Gegensweep (Regel 4): Was war so selbstverständlich, dass ich es nicht geprüft hätte?

- **G1, geprüft: "Inagaki und Murakami existiert, wie die Vorarbeit sagt."**
  - Die Vorarbeit las per WebFetch, also durch ein Zusammenfassungsmodell, das erfinden kann.
  - Hier roh per curl geprüft: Titel, Autoren, Datum und Abstract stimmen. Die Nullstellenwerte stehen im Volltext.
- **G2, geprüft (Schreibtischrechnung): "In 1D gibt es keine Nullstelle, also ist das ein Dimensionseffekt."**
  - Das 1D-Raster 0,55 bis 0,88 lag fast ganz im Bereich ω² > 0,556, in dem sp in 1D nirgends das Vorzeichen wechselt.
  - Unter der Vorzeichen-Hypothese war dort also gar keine Nullstelle zu erwarten. Der Negativbefund trennt die
    Hypothesen nicht.
  - Dazu kommt die Warnung von Inagaki und Murakami, dass Γ-Raster schmale Nullstellen übersehen.
- **G3, geprüft (Suche): "Die NLS-Mathematik lässt sich auf NLKG-Q-Bälle übertragen."**
  - Für NLKG-Q-Bälle fand ich weder einen Existenz- noch einen Abwesenheitssatz zu eingebetteten Eigenwerten.
  - Die Übertragung der Erwartung in Bemerkung 3.2 ist deshalb selbst eine Hypothese **[ES]**.
- **G4, geprüft: Codex' Referenz 2501.02589.** Sie existiert, ist aber ein BPS-Spielmodell mit Schwellen-Nullstelle
  (Verstoß 4). Die Einordnung "Zweikanal-Methodik" ist tragbar, eine Q-Ball-Parallele ist sie nicht.
- **G5, nicht geprüft:**
  - ob unsere Q-Bälle im NLKG-Sinn "Grundzustände" sind. Knotenfrei ja, die Minimalität bei fester Ladung habe ich nicht
    geprüft.
  - das Vorzeichen der Krein-Norm am Pol. Es steht in bic2-PLAN, ich habe es nicht nachgerechnet.
  - Buslaev und Perelman sowie Gang und Sigal im Volltext
  - Bosonstern-Volltexte
  - russischsprachige Literatur
  - die Identität des Ausnahmepotentials bei Ollé u. a.
  - den Springer-Volltext von Li und Yang

## 8 Kalibrierung

- **(a) Gemessen bzw. an der Quelle gelesen:**
  - Existenz und Inhalt von 2609.15056
  - die wörtlichen Aussagen von Cuccagna und Maeda (Bem. 1.6, 3.2, 3.3), Agmon, Herbst und Maad Sasane, Collot, Germain
    und Pacherie (Satz 1.1), Ayala u. a., García Martín-Caro u. a., 2310.15738
  - die Nullstellenwerte des Auftrags (nicht von mir gerechnet)
- **(b) Nützlich verdichtet:**
  - die Trennung linear (spektral) gegen nichtlinear (FGR)
  - die Versöhnung durch die Moderatoren Familie und NLKG
  - die Kodimensionszählung
  - das 1D-Fenster 0,5 < ω² < 0,556
  - die Folgevorhersage ω² ≈ 0,634 / 0,60 / 0,58
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "Der Befund ist neu": eine Abwesenheitsaussage bei begrenzter Abdeckung (englisch, arXiv, Suchmaschine)
  - "Er widerspricht einer offenen Vermutung": gilt nur, wenn die NLS-Erwartung auf NLKG übertragbar ist, und das ist
    ungeprüft
  - "exakt": gestützt durch Umlaufzahl und 2e-12, aber ohne Fehlerschranke
- **Warnzeichen:** Meine Einschätzung ist im Lauf von "teilweise bekannt" zu "interessant für die Mathematik" gestiegen.
  Ausgelöst hat das eine einzige Bemerkung in einem Übersichtsartikel (Bem. 3.2). Neue Messevidenz ist dabei nicht
  hinzugekommen. Gleichzeitig ist die Frage feiner geworden: Es geht jetzt um NLS gegen NLKG und Einzelsoliton gegen
  Familie. Das gehört in jede Weitergabe.

## 9 Offene Fragen

1. Gilt die Erwartung "Grundzustände haben keine eingebetteten Eigenwerte" auch für NLKG-Q-Bälle? Wenn ja, wäre unser
   Befund ein Gegenbeispiel, wenn nein, fehlt eine Begründung, warum NLKG anders ist.
2. Setzt sich die Nullstellenfolge zur Dünnwand fort (0,634 bzw. 0,631, dann 0,60 und 0,58)?
3. Gibt es in 1D Nullstellen im schmalen Fenster 0,5 < ω² < 0,556 (β = 1/2)?
4. Wie klingt die Mode genau bei ω\* ab, mit t^{−1/2}?
5. Gehört eine Mitteilung an Cuccagna und Maeda oder Collot, Germain und Pacherie (Mathematik) bzw. an Dorey,
   Romańczukiewicz und Shnir (Q-Bälle) auf den Tisch? Das ist eine Frage an die Leitung, nicht entschieden.

## 10 Nächster Schritt (Frage 4), nach Nutzen je Aufwand

1. **Folgevorhersage prüfen (billig, entscheidend für den Mechanismus):**
   - signierte auslaufende Amplitude für β = 1/2 auf 0,56 bis 0,65 fein rastern
   - Umlaufzahl um 0,631 bestimmen
   - Vorab gebunden **[ES]:** Nullstellen bei ≈ 0,634 (±0,01), ≈ 0,60 und ≈ 0,58.
     - Trifft die Vorhersage, ist der Formfaktor-Mechanismus gestützt, und es gibt vermutlich unendlich viele Nullstellen
       mit Häufung bei ω²_min.
     - Trifft sie nicht, ist er geschwächt.
2. **1D-Fenster testen:** β = 1/2, ω² in (0,50, 0,556), signierte Amplitude. Kleineres β verbreitert das Fenster
   (Breite 1/(36β)). Das trennt "1D strukturell verboten" von "Vorzeichenwechsel nötig".
3. **Zeitbereich (Lebensdauer):**
   - linearisierte Zeitentwicklung mit der Eigenfunktion bei ω\* gegen ω² = ω\*² ± δ: Bei ω\* kein exponentieller Zerfall,
     daneben 2Γ ≈ 2,1·δ² (δ in ω² gemessen)
   - danach nichtlinear mit η = 0,001 bis 0,01: A ~ t^{−1/2}, Rate ∝ η²
   - die ω-Verschiebung durch den Stoß mitschätzen
4. **Beweisweg (teurer):** W auf der Schleife mit Intervallarithmetik auswerten, als computergestützter Existenzbeweis
   eines eingebetteten Eigenwerts, nach dem Vorbild von Asad und Simpson 2011 sowie Ayala u. a. 2026.
5. **Analytisch:**
   - Dünnwand-Näherung der Kopplung M(ω) = ∫ χ_E·sp·φ_c dr mit verzerrter Streuwelle (Lehre aus Zhang u. a. 2020 [V])
   - daraus die Konstante im Schritt Δ(1/x) ≈ 2,1 vorhersagen

## 11 Quellenliste

**Mathematik:**
- Cuccagna S., Maeda M. (2020): A survey on asymptotic stability of ground states of nonlinear Schrödinger equations II.
  arXiv:2009.00573. https://arxiv.org/abs/2009.00573 [A]
- Cuccagna S., Maeda M. (2024): On the asymptotic stability of ground states of the pure power NLS on the line at 3rd and
  4th order Fermi Golden Rule. arXiv:2405.11763. https://arxiv.org/abs/2405.11763 [A]
- Agmon S., Herbst I., Maad Sasane S. (2010): Persistence of embedded eigenvalues. arXiv:1008.2099.
  https://arxiv.org/abs/1008.2099 [A]
- Collot C., Germain P., Pacherie E. (2025): Absence of embedded spectrum for nonlinear Schrödinger equations linearized
  around one dimensional ground states. arXiv:2503.02957. https://arxiv.org/abs/2503.02957 [A]
- Li D., Yang K. (2026): The linearized cubic NLS has no embedded eigenvalue. Invent. Math.
  https://link.springer.com/article/10.1007/s00222-026-01419-3 [S]
- Germain P. (2024): A review on asymptotic stability of solitary waves in nonlinear dispersive problems in dimension one.
  arXiv:2410.04508. https://arxiv.org/abs/2410.04508 [A, nur Abstract]
- Asad R., Simpson G. (2011): Embedded eigenvalues and the nonlinear Schrödinger equation. J. Math. Phys. 52, 033511;
  arXiv:1101.2485. https://arxiv.org/abs/1101.2485 [A]
- Léger T., Pusateri F.: Internal modes and radiation damping for quadratic Klein-Gordon in 3D. arXiv:2112.13163
  (Mem. AMS 318 (2026) laut Literaturverzeichnis bei Inagaki und Murakami). https://arxiv.org/abs/2112.13163 [A]
- Li Y., Lührmann J. (2023): Soliton dynamics for the 1D quadratic Klein-Gordon equation with symmetry. JDE 344, 172;
  arXiv:2203.11371. https://arxiv.org/abs/2203.11371 [A]
- Bambusi D., Cuccagna S.: On dispersion of small energy solutions of the nonlinear Klein Gordon equation with a
  potential. arXiv:0908.4548. https://arxiv.org/abs/0908.4548 [A]
- Tsai T.-P., Yau H.-T. (2002): Asymptotic dynamics of nonlinear Schrödinger equations: resonance dominated and radiation
  dominated solutions. CPAM 55, 153 (Fundstelle laut Suchtreffer); arXiv:math-ph/0011036. https://arxiv.org/abs/math-ph/0011036 [A]
- Gang Z., Sigal I. M. (2006, arXiv): Relaxation of solitons in nonlinear Schrödinger equations with potential.
  arXiv:math-ph/0603060. https://arxiv.org/abs/math-ph/0603060 [A, Abstract]
- Buslaev V. S., Perelman G. S. (1993): Scattering for the nonlinear Schrödinger equation: states close to a soliton.
  St. Petersburg Math. J. 4, 1111 [S]
- Kowalczyk M., Martel Y., Muñoz C., Van Den Bosch H. (2020): A sufficient condition for asymptotic stability of kinks in
  general (1+1)-scalar field models. arXiv:2008.01276. https://arxiv.org/abs/2008.01276 [A, Abstract]
- Lei Z., Liu J., Yang Z. (2022): Energy transfer, weak resonance, and Fermi's golden rule in Hamiltonian nonlinear
  Klein-Gordon equations. arXiv:2201.06490 (CPDE 51 (2026) laut Zitat bei Inagaki und Murakami).
  https://arxiv.org/abs/2201.06490 [A]
- Lei Z., Liu J., Yang Z. (2023): Energy transfer and radiation in Hamiltonian nonlinear Klein-Gordon equations: general
  case. arXiv:2307.16191. https://arxiv.org/abs/2307.16191 [A]
- Maeda M. (2014): Existence and asymptotic stability of quasi-periodic solution of discrete NLS with potential in ℤ.
  arXiv:1412.3213. https://arxiv.org/abs/1412.3213 [A]
- Kevrekidis P. G., Pelinovsky D. E., Saxena A. (2014, arXiv): When does linear stability not exclude nonlinear instability?
  arXiv:1412.1522. https://arxiv.org/abs/1412.1522 [A]
- Ayala M., Blanco D., Cakoni F., Hovsepyan N., Vogelius M. S. (2026): On the potential lack of response in a model of
  second-harmonic generation. A computer-assisted proof. arXiv:2609.23217. https://arxiv.org/abs/2609.23217 [A]
- Soffer, Weinstein 1999; Cornean, Jensen, Nenciu 2015; Champneys, Malomed, Yang, Kaup 2001; Hsu u. a. 2016 [V]: siehe
  RUNDE-06/resonanz3d/L4-BIC-LITERATUR.md

**Physik:**
- Inagaki T., Murakami Y. (2026): Open-channel radiation zeros and nonlinear damping of a critical-bubble internal mode.
  arXiv:2609.15056. https://arxiv.org/abs/2609.15056 [A, Abstract und HTML-Volltext roh]
- Bizoń P., Romańczukiewicz T. (2026): Radiation damping of the soliton internal mode in 1D quadratic Klein-Gordon
  equation. arXiv:2603.18605 (PRE 114, 024213 laut Zitat bei Inagaki und Murakami). https://arxiv.org/abs/2603.18605 [A]
- García Martín-Caro A., Queiruga J., Wereszczyński A. (2025): Feshbach resonances and dynamics of BPS solitons.
  arXiv:2501.02589. https://arxiv.org/abs/2501.02589 [A]
- Blaschke F., Romańczukiewicz T., Sławińska K., Wereszczyński A. (2026): Unified theory of oscillons and modes.
  arXiv:2606.22680. https://arxiv.org/abs/2606.22680 [A]
- Bayarsaikhan B., Evslin J., Mahato S. (2026): Oscillon Floquet modes and the operators that excite them.
  arXiv:2607.15624. https://arxiv.org/abs/2607.15624 [A]
- Ollé J., Pujolàs O., Rompineve F. (2021): Recipes for oscillon longevity. JCAP 09 (2021) 015; arXiv:2012.13409.
  https://arxiv.org/abs/2012.13409 [A]
- Alonso-Izquierdo A., Miguélez-Caballero D., Nieto L. M. (2023): Wobbling kinks and shape mode interactions in a coupled
  two-component φ⁴ theory. arXiv:2310.15738. https://arxiv.org/html/2310.15738 [A, Volltext]
- Macedo C. F. B., Pani P., Cardoso V., Crispino L. C. B. (2013): Astrophysical signatures of boson stars: quasinormal
  modes and inspiral resonances. arXiv:1307.4812. https://arxiv.org/abs/1307.4812 [S]
- Dorey P., Romańczukiewicz T. (2018): Resonant kink-antikink scattering through quasinormal modes. PLB 779, 117 [S]
- Dorey P., Gorina A., Romańczukiewicz T., Shnir Y. (2023): Collisions of weakly-bound kinks in the Christ-Lee model.
  JHEP 09 (2023) 045; arXiv:2304.11710 [S]
- Evslin J. u. a. (2026) arXiv:2604.07713; Ciurla u. a. (2024) arXiv:2405.06591; Manton, Merabet (1997); Zhang u. a.
  (2020); Cyncynates, Giurgica-Tiron (2021); Campos, Mohammadi (2021); Guo, Evslin, Bolognesi (2026); Azatov u. a. (2024)
  [V]: siehe Vorarbeit

**Projektdateien:**
- Auftrag der Leitung (30.09.2026)
- /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/resonanz3d/L4-BIC-LITERATUR.md
- /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06.md (Abschnitt Codex, Feshbach-Diagnose)
- /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-07/bic2/PLAN.md (Gleichungen, Krein-Norm), nur Kopf gelesen

## Einfach gesagt

Ein Q-Ball kann "atmen", und dabei verliert er normalerweise Energie als Welle nach außen. Wir haben ganz bestimmte
Drehfrequenzen gefunden, bei denen dieser Verlust nach unseren Tests genau null ist, bewiesen ist das noch nicht. Das
Prinzip der Auslöschung kennt man aus der Optik, von Oszillonen und seit zwei Wochen auch von Blasen (Inagaki und
Murakami, die Arbeit gibt es wirklich), für Q-Bälle steht es aber nirgends. Die Mathematiker erwarten für solche "Grundzustände" sogar, dass es das gar nicht gibt, allerdings
bisher nur für eine verwandte, einfachere Gleichung. Der nächste billige Test: Wenn unsere Erklärung stimmt, muss die
nächste Nullstelle bei etwa ω² = 0,634 liegen, dann bei 0,60 und bei 0,58.


Ende: 2026-09-30 05:18:20 CEST (date, nach dem Schreiben gemessen). Dauer 18:51 min (04:59:29 bis 05:12:49 Recherche, danach Schreiben und Gegenlesen), Budget 45 Minuten.
