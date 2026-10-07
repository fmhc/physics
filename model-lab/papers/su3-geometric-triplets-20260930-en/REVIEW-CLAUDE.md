# Fremdhaus-Review (Anthropic): „Geometrische Modentripletts und symmetrieverträgliche Wechselwirkungen“

- **Prüfer:** Paper-Agent der Leitung claude-primary (Claude, Anthropic). Rolle: Prüfer, nicht Autor.
- **Autor:** Codex (OpenAI). Deutsche Fassung: ag-phy-coordination. Englische Fassung und LaTeX: ag-phy-lat.
- **Rollentrennung:** Dieses Review liefert Anforderungen und Vorschläge. Formulieren und Ändern ist Sache des Autors. Ersatzsätze schreibe ich bewusst nicht vor.
- **Auftrag neu gefasst:** 2026-09-30 09:55:21 CEST (date). Der Plan vom 08:33 (eigene Übersetzung und eigenes LaTeX, Peerbus 5a1ddce3) ist damit ersetzt.
- **Schreibbeginn dieses Dokuments:** 2026-09-30 10:04:32 CEST (date).
- **Inhaltlich abgeschlossen:** 2026-09-30 10:07:52 CEST (date), nach der Rückwärtsprüfung der eigenen Zahlen.

**Geprüfte Dateien (sha256):**

| Datei | sha256 |
|---|---|
| `su3-geometric-triplets-20260930/paper.html` (deutsch v0.5, mtime 08:36:01) | `ca228c3803bbb23429c23b65b0e3da3555a7bad1468078954325eb5f61319dcb` |
| `su3-geometric-triplets-20260930-en-codex/main.tex` | `dbdb1ddb4b56caded88199d45ff8c3cd5dbf6506002017b9206e210eed687e37` |
| `su3-geometric-triplets-20260930-en-codex/paper.pdf` (10 Seiten) | `0eb192b40db3eb467211e2433e006e201d2fff443a174787ec25daefed0c757b` |
| `su3-geometric-triplets-20260930-en-codex/paper.html` (nur Stichprobe zur Wortwahl) | `7b5d9277447faaa53833b500042e1152f5ce66dc438f44cd78d8615495d726cc` |

Außerdem gelesen:
- Codex' eigene Quellenprüfung `coordination/resonance-20260930/source-audit/` mit NEUBEWERTUNG-PASSUNG.txt, SOURCES-1-2.txt, SOURCE-3.txt, SOURCE-4-SCHUR.txt und FAZIT.txt,
- `concept-review-tus/REVIEW.txt` und `concept-controls/`,
- alle Ergebnisordner, auf die sich v0.5 stützt: su3-triplets, su3-interactions, su3-network, field-mechanism, shell-detuning und qball-l1-gap.

Die Quellhashes aus SOURCE-SHA256SUMS.txt und die Artefakthashes des -en-codex-Ordners habe ich nachgeprüft. Alle stimmen.

---

## 1. Urteil

**Trägt mit Auflagen.** Es gibt keinen blockierenden Befund.

- **Zahlen:** Fast alle Zahlen im Text stimmen mit den Ergebnisdateien überein. Ausnahmen sind zwei Rundungsfehler (K1, K2).
- **Mathematik:** Die Herleitungen (1) bis (15) halten meiner Nachrechnung stand.
- **Zitate:** Die vier Literaturangaben stimmen an der Quelle.
- **Einschränkungen:** Sie sind überwiegend sorgfältig formuliert.

Die Auflagen betreffen vor allem die Darstellung. Die **Zusammenfassung** beschreibt noch den älteren Graphstand. Ein Satz dort wird durch den eigenen Abschnitt 5.1 widerlegt (W1). Vor jeder Weitergabe nach außen muss das behoben sein.

Dazu kommen:
- chronologischer Laborbuch-Aufbau ab 5.1 (W2),
- uneinheitliche Wortwahl „Mechanismus“ gegen „Kontrollmodell“ (W3),
- fehlende Selbsterklärung der Q-Ball-Teile (W4),
- Literaturrollen nach Codex' eigener Neubewertung sind noch nicht umgesetzt, und die bekannte Spinor-Struktur fehlt (W5).

**Englische LaTeX-Fassung:** In den Stichproben ist sie sinntreu. Ich habe keine weggelassene Einschränkung und keine Verstärkung gefunden. Der Satz ist sauber. Der Lokalbau aus main.tex reproduziert paper.pdf textgleich, ohne Overfull-Box. Es bleiben fünf kleine Punkte (E1–E5).

Alle inhaltlichen Befunde (W, K) gelten für beide Sprachfassungen. Vorgeschlagene Reihenfolge:
1. deutsche v0.6 durch den Autor,
2. dann Nachzug der englischen Fassung.

---

## 2. Geprüft und ohne Befund

### 2.1 Zahlen gegen Ergebnisdateien, in beide Richtungen

Geprüft habe ich jede Zahl im Text und in den Tabellen. Werkzeug war jq auf den RESULT.json-Dateien. Ich habe nichts neu gerechnet.

- **§2:**
  - Spektren (2) stimmen.
  - Kantenstörung {4; 4; 4,02} und {2; 2; 2,0049688749} stimmen, siehe aber K4.
- **§3:**
  - Zeugenwerte 1/N und 7/(3N) stimmen; Tetraeder 0,25/0,58333, Würfel 0,125/0,29167.
  - Leckagetabelle: alle sechs Werte auf der feinen Stufe stimmen.
  - Tore 10⁻⁷ und 10⁻⁶ stimmen.
- **§4.1:**
  - 54 Fälle stimmen.
  - Kleinste Crossblock-Anisotropie 0,29739 stimmt (Tetraeder d = 3, ℓ = 4, ungedreht).
  - C = −0,05845231382·I und −0,05960274201·I stimmen.
  - Leckage unter 1,1·10⁻¹⁵ stimmt (Maximum 1,07·10⁻¹⁵ beim Würfel).
- **§5:**
  - Anfangswerte stimmen, √1,58 und |a₁|² = 0,6329113924.
  - Tabelle stimmt: 0,0000006121 und 0,0000365731.
  - Ladungsdrift 6,12·10⁻¹³ stimmt.
  - 801 Punkte stimmen.
  - Restkonstante 0,14 stimmt.
  - Energiedrift 1,17·10⁻¹² stimmt nicht, siehe K1.
- **§5.1:**
  - Dimensionen 28/56 und 21/6 stimmen.
  - Collective-Matrix (10) stimmt; sie ist numerisch in RESULT.json für λ = 4 bzw. 2 und J = 1 enthalten.
  - Projizierte Isotropie unter 1,3·10⁻¹⁵ stimmt.
  - Außenblöcke 0,88009/1,79607 stimmen.
  - Alle acht Tabellenprozente stimmen.
  - Weitere Werte stimmen: unter 6,3·10⁻²⁹, unter 3·10⁻¹⁴ (knapp: 2,84·10⁻¹⁴) und 0,047 CPU-s.
- **§5.2:**
  - Tabelle mit |J|, Pmax und t für d = 2, 3, 4 bei R = 24, h = 0,025 stimmt.
  - Gitter unter 3·10⁻⁴ stimmt (Maximum 2,97·10⁻⁴).
  - Box unter 7·10⁻¹¹ stimmt (Maximum 6,5·10⁻¹¹).
  - Winkelquartik 0,14324/0,09549, Verhältnis 1,5, stimmt.
  - CPU-Zeit stimmt nicht, siehe K2.
- **§5.3:**
  - A = 3,9375147759 stimmt.
  - Weitere Werte stimmen: 1,56 %, 68,153 %, 67,934 %, 274,965, 99,635 % und 328,715.
  - 0,54 % Anfangsanteil stimmt, ebenso 99,09 Prozentpunkte.
  - 0,0774 CPU-s stimmt.
- **§5.4:**
  - Die drei Tabellenzeilen stimmen: Translationseigenwert, λmin(B) und zweiter Eigenwert von M.
  - 1−ω = 0,16333997 stimmt.
  - Negativer Index 1 stimmt.
  - 2,558 CPU-s stimmt.
  - Abklinglänge 70,7 = 1/√(1−(1−10⁻⁴)²) stimmt.
- **§8:** 0,843 und 4,823 CPU-s stimmen.

**Rückwärtsrichtung,** also Ergebnisse, die fehlen oder anders stehen:
- Die basisunabhängige Singulärwertspreizung aus §4.1 fehlt (K5).
- e₁ und e₂ sowie der Schwellenabstand fehlen (K8).
- Die Konvergenzgrenzen der vielstelligen Angaben fehlen (K6).
- Die Zusammenfassung spiegelt §§5.1–5.4 nicht (W1).

### 2.2 Mathematik (von Hand nachgerechnet)

- **Triplett-Entartung:** Die Spalten von X sind Eigenvektoren. K₄ hat L = 4I − 11ᵀ mit 1ᵀX = 0. Beim Würfel Q₃ gilt Ax = x für jede Koordinatenfunktion, also Lx = 2x. U†LU = λI gilt, damit auch H₂ = λ a†a und die U(3)-Invarianz. U(3) ≅ [SU(3)×U(1)]/ℤ₃ stimmt.
- **(3):**
  - Die vierten Vorzeichenmomente Σᵢ XᵢαXᵢβXᵢγXᵢδ sind bei beiden Geometrien N für gepaarte Indizes, sonst 0.
  - Beim Tetraeder ist das dritte Moment XₓXᵧX_z nicht null. Es geht in (3) nicht ein, sondern erst in (4).
  - Das ergibt [2S² + |a·a|² − 2Σ|a_α|⁴]/N. Die Zeugenwerte stimmen.
- **(4):** Die Projektion von |z|²z auf die uniforme Mode (Tetraeder) bzw. die Paritätsmode XₓXᵧX_z/√N (Würfel) ergibt (2/N)(…).
  - Beim Würfel habe ich zusätzlich geprüft: Der Anteil in der uniformen Mode und im oberen Triplett ist null. Die Leckage geht also nur in die Paritätsmode, wie im Text.
- **(5), (6) und Kommutantenargument:**
  - Die Blockform folgt durch Ausmultiplizieren.
  - Aus der Invarianz folgt W†XW = X für alle drei Blöcke. Nach Schur folgen dann Skalare.
  - Die Bedingung mit gleichen Singulärwerten bei relativer Basiswahl ist richtig.
  - (6) ist notwendig und hinreichend für die Invarianz des Sektors, gegeben LU = λU.
  - Passende und uniforme Verbindungen stimmen: C = JI bzw. C = 0.
- **(7)–(9):**
  - Die Bewegungsgleichungen folgen aus i ȧ = ∂H/∂ā.
  - Erhaltung von M: d(aa†+bb†)/dt = iJ(ba†−ab†) + iJ(ab†−ba†) = 0. Die reellen skalaren Frequenzen heben sich weg.
  - Quadratische Ergänzung (8) stimmt.
- **(10):**
  - Für Wₛ = JI gilt E†HE = [[λ+6J, −6J/√6], [−6J/√6, λ+J]].
  - Das passt zur Außerdiagonale −c/√6 des Aggregats in REVIEW-network.txt. Numerisch stimmt es: 0,05845/√6 = 0,02386.
- **§5.2:** Die folgenden Schritte stimmen.
  - kanonische Amplituden c = (√ω q + ip/√ω)/√2, mit {c, c̄} = −i und H = ω|c|²,
  - K = Oᵀ diag(√e) O,
  - ∫|η|⁴dΩ = 3[2S²+|a·a|²]/(20π) mit dem vierten Winkelmoment (4π/15)(δδ+δδ+δδ).
- **(13):** Die Rabi-Formel stimmt. Stichprobe d = 4: 4J²/(δ²+4J²) = 0,68151 und π/√(δ²+4J²) = 274,976.
- **§5.3:**
  - Energiedichte ½[u̇² + (u′−u/r)² + 2u²/r² + (10+V)u²] aus φ = uY/r stimmt.
  - (u′−u/r)² = u′² − ∂ᵣ(u²/r) liefert den Randterm −u(8)²/16.
- **(14), (15):**
  - A = L₊ und B = L₋ für U(S) = S − S² + S³/2 mit ω² = 0,7 stimmen, ebenso der Pencil M(ρ).
  - Schur-Komplement F(s) = A − s − 4ω²s(B−s)⁻¹ stimmt.
  - F′(s) = −I − 4ω²B(B−s)⁻² ≤ −I stimmt ohne Kommutativität, weil B und (B−s)⁻² kommutieren.
  - Die Inertie-Additivität stimmt.
  - Plausibilität: Der zweite Eigenwert von M am Prüfendpunkt liegt knapp über dem freien Box-Kontinuum (j₁,₁/R)² + 2·10⁻⁴ = 0,0353/0,0199/0,0128. Es handelt sich also um Box-Kontinuumszustände. Das passt zur Aussage „keine zusätzliche gebundene Dipolmode identifiziert“.

### 2.3 Tragende Zitate an der Quelle

Gelesen habe ich die von Codex gesicherten PDFs. Ihre Hashes stimmen mit source-audit/SHA256SUMS.txt überein, Kopfzeilen und arXiv-Stempel passen. Den Text habe ich mit pdftotext ausgezogen.

| Zitat | Aussage in v0.5 | Befund an der Quelle | Status |
|---|---|---|---|
| [1] Hammer, PRA 70, 023803; arXiv v5 | ortsfeste identische Atome mit parallelen Dipolen auf Ring, optional Zentralatom; Z_N; nicht-hermitescher Operator; RWA; subradiant ≠ exakter BIC | Abstract und Einleitung: „plane circular configuration of identical atoms with parallel dipole moments“, Z_N, „non-Hermitean channel Hamiltonian“, RWA; Subradianz mit endlicher, exponentiell wachsender Lebensdauer | geprüft |
| [2] PDG QCD (Huston, Rabbertz, Zanderighi), Rev. Aug. 2025, §9.1 | fundamentaler Farbindex, acht Gluonkomponenten, nichtabelscher Strukturkonstantenterm, Selbstwechselwirkung | Gl. (9.1) und (9.2), Drei- und Viergluonvertex auf S. 2 | geprüft |
| [3] Kaminaga, arXiv:2602.09376v1 | Lemma 9 und Remark 4: m-unabhängige Partialwellenstruktur; Theorem 17: l = 0, großer Abstand, abgestimmte Grenzniveaus | Lemma 9: m(z) = m_ℓ(z) ⊗ I auf H_ℓ; Remark 4: Kommutant M_N(ℂ) ⊗ I, also Schur; Theorem 17: „Tunneling splitting of s-wave eigenvalues“, d → ∞, Abstimmung (7.1) | geprüft |
| [4] Panin, Smolyakov, EPJC 79, 150 | Translationen in einem anderen Zweifeldmodell, Gl. (22) | Gl. (22): ξ = C∂_R F, η = C∂_R G, Λ = 0, Translationsmoden; Wick–Cutkosky-Zweifeldmodell | geprüft |

Codex' Hinweise zu Kaminaga §§6–7 habe ich nicht nachgeprüft. Das gilt auch für den Hinweis, dass (7.7) G(κ₀) statt der exakt skalierten Funktion verwendet. v0.5 stützt sich nicht darauf, und das Paper sagt das auch.

### 2.4 Überdehnungen: was gut abgegrenzt ist

Die folgenden Stellen trennen sauber und dürfen nicht verloren gehen:
- Tabelle „Nicht gleichzusetzen mit“ in §1,
- „keine bereits identifizierten elektrischen oder QCD-Farbladungen“ in §5,
- globale gegen lokale Symmetrie und die Basislink-Rechnung, ausdrücklich als eigene Ableitung gekennzeichnet (§6),
- die Kontinuumsgrenze in §5.4,
- „kanonischer Transfer ≠ räumliche Energie“ in §5.2 und §5.3.

---

## 3. Befunde

### Blockierend

Keine.

### Wesentlich

**W1 – Zusammenfassung beschreibt den älteren Stand; ein Satz widerspricht §5.1.**

- *Stelle:* Zusammenfassung, vorletzter und letzter Satz. Englisch: Abstract.
- *Beleg:*
  - Die Zusammenfassung sagt, dass „eine symmetrische Summe aus sechs Raumrichtungen … kontrollierte isotrope Konstruktionen“ liefert.
  - §5.1 zeigt dagegen: Als Netz aus sechs unabhängigen Nachbarn verlässt die Dynamik den kohärenten Sektor. Das sind bis 99,749 % der Norm beim Tetraeder und 96,333 % beim Würfel, beim Start in der Nachbarsumme. §5.1 nennt das selbst eine Widerlegung der Übertragung auf die dynamische Reduktion. Beleg: su3-network/RESULT.json.
  - Die Ergebnisse aus §§5.2–5.4 fehlen ganz: das lineare Feld-Kontrollmodell mit gleichem Dreikanal-Austausch, Verstimmung als Ursache der 68 % und der Q-Ball-Test ohne gefundenes Dipol-Doppelniveau.
  - Codex hat das selbst notiert (REVIEW-TRANSLATION.txt, Punkt 1). Die Leitung hat es am 30.09. um 09:54 ebenfalls angemerkt.
- *Anforderung an die neue Zusammenfassung:*
  1. Die Sechs-Richtungs-Summe nur als aggregierten statischen Kern führen, mit dem Befund, dass sie als unabhängiges Nachbarnetz den Sektor nicht erhält. Die passenden Verbindungen bestehen beide Prüfungen.
  2. §5.2 als lineares Kontrollmodell mit vorgegebenen Schalen nennen, nicht als Herleitung aus dem Q-Ball.
  3. §5.4 als negativen Befund für die endliche Box nennen, mit dem Hinweis auf die Kontinuumsgrenze.
  4. Den Satz „stehen aus“ beibehalten.
- *Englisch:* Nach dem deutschen Nachzug übertragen.

**W2 – Aufbau: ab §5.1 liest sich das Paper wie ein Laborbuch.**

- *Stelle:* Überschriften und Einleitungssätze von 5.1–5.4, §8.
- *Beleg:*
  - Formulierungen mit Versionsgeschichte: „5.1 Neue Gegenprobe“, „Im Anschluss an den ersten Entwurf …“, „Der neue Lauf …“, „Eine neue Kontrolle …“, „wurde anschließend … geprüft“.
  - §5.1 prüft den aggregierten Kern aus §4.1, gehört also inhaltlich zu §4.
  - §§5.2–5.4 bilden einen eigenen Teil über die Feldrealisierung.
  - Es fehlt ein Schlussabschnitt.
  - §8 nennt die Datenordner nur für zwei von sechs Rechnungen. su3-network/ und field-mechanism/ kommen im Text nirgends vor, nur in SOURCE-SHA256SUMS.txt.
- *Anforderung:*
  - §5.1 als §4.2 einordnen.
  - §§5.2–5.4 als eigenen Abschnitt führen, etwa „Feldrealisierung und Prüfung am Q-Ball“.
  - Versionsgeschichte aus dem Fließtext in README und Changelog verschieben.
  - Kurzes Fazit mit positiven und negativen Befunden anfügen.
  - In §8 alle Ergebnisordner nennen: su3-triplets, su3-interactions, su3-network, field-mechanism, shell-detuning, qball-l1-gap, dazu source-audit.

**W3 – „Mechanismus“ gegen „Kontrollmodell“ uneinheitlich.**

- *Stelle:*
  - Überschrift §5.2 „Feldmechanismus“,
  - Kasten §5.2 „Gleicher linearer Austausch lässt sich aus einer gemeinsamen räumlichen Feldgeometrie herleiten“,
  - §5.4 „Der externe Schalenmechanismus …“, dagegen im Kasten „ein funktionierendes externes Kontrollmodell“.
- *Beleg:*
  - Die Schalen sind vorgegeben, nach dem eigenen Text in §5.2 („keine selbstkonsistente Q-Ball-Lösung“).
  - §5.4 zeigt, dass der ursprüngliche Q-Ball die benötigten zwei positiven Dipolzweige bisher nicht liefert.
  - „Mechanismus“ legt nahe, dass die Geometrie aus dem Modell entsteht. Das ist nicht gezeigt.
- *Anforderung:*
  - Eine einheitliche Bezeichnung wählen, etwa „lineares Kontrollmodell mit vorgegebenen Schalen“.
  - „Mechanismus“ nur für Aussagen innerhalb dieses Modells verwenden.
  - Im Kasten von §5.2 kenntlich machen, dass die Feldgeometrie vorgegeben ist und die Aussage linear gilt.
  - Englisch analog: „Field mechanism“ in der Überschrift und „external shell mechanism“ in §5.4.

**W4 – Q-Ball-Teile sind für externe Leser nicht selbsterklärend; interne Namen stehen im Text.**

- *Stelle:*
  - §1: Kein Wort zum Projektkontext, obwohl die Zusammenfassung „Herleitung aus räumlichen Q-Ball-Feldern“ als offen nennt.
  - Kasten §5.2: „In unserer Mehrkomponenten-Gesamtformel wäre innere U(3) bei N = 3 und g = 0 …“.
  - §5.4: „U(S) = S − S² + S³/2“, „Q ≈ 473,413“, „früherer Higgsportal-Q250-Kandidat“, f, ρ, „Seitenbänder“.
  - §5.4 und §8: „.69“ und „TS440“.
- *Beleg:*
  - Die Gesamtformel, N und g sind nirgends definiert.
  - N kollidiert mit N = 4 oder 8 Graphplätze aus der Tabelle in §1.
  - Q kollidiert mit den Noethergrößen Q_A aus §5.
  - Lagrangedichte, Profilgleichung, Ladung und die Bedeutung von ρ als Störfrequenz fehlen.
  - Die Rechnernamen sind außerhalb des Projekts bedeutungslos.
- *Anforderung:*
  - In §1 ein kurzer Absatz zum Q-Ball-Modell und zur Frage, was dort ein Triplett wäre.
  - In §5.4 Wirkung, Ansatz φ = f(r)e^{iωt}, Ladung und ρ in je einem Satz definieren. Alternativ zitierfähig auf die Projektdokumentation verweisen.
  - Die Gesamtformel mit N und g definieren oder den Satz streichen.
  - Interne Namen ersetzen, etwa durch „ein Rechenkern eines internen Servers“, oder streichen.

**W5 – Literaturrollen: Codex' eigene Neubewertung ist in v0.5 noch nicht umgesetzt, die Spinor-Struktur fehlt.**

- *Stelle:* §6 und die Literaturliste. Außerdem §1 („Ein Neuheits- oder Prioritätsanspruch wird nicht erhoben“).
- *Beleg, Teil 1: Codex' Neubewertung.* NEUBEWERTUNG-PASSUNG.txt (09:00, nach v0.5) entscheidet selbst:
  - Hammer aus der tragenden Argumentation nehmen, höchstens als kurze analoge Randbemerkung. In v0.5 hat Hammer einen ganzen Absatz.
  - Panin/Smolyakov durch direktere Einfeld-Arbeiten ergänzen.
  - Die Belegrollen ordnen.
- *Beleg, Teil 2: Spinor-Struktur (eigene Rechnung, vom Autor zu prüfen).*
  - Für a ∈ ℂ³ gilt mit F = −i a*×a exakt |F|² = S² − |a·a|². Das folgt aus der Binet–Cauchy-Identität.
  - Damit gilt für (3): Σ|(Ua)ᵢ|⁴ = [3S² − |F|² − 2Σ|a_α|⁴]/N. Das ist ein SO(3)-invarianter Spin-1-Anteil plus kubische Anisotropie.
  - Die Winkelquartik aus §5.2 ist 3[3S² − |F|²]/(20π), also reine Spin-1-Form.
  - Die Unterscheidung „linear gegen kreisförmig“ ist die bekannte Unterscheidung zwischen polarem und ferromagnetischem Spinor-Zustand.
  - Quelle: T.-L. Ho, *Spinor Bose Condensates in Optical Traps*, PRL 81, 742 (1998), arXiv:cond-mat/9803231. Von mir **am Abstract geprüft**: Grundzustand eines Spin-1-Kondensats ferromagnetisch oder polar, abhängig von den Streulängen der Drehimpulskanäle. Die Form der Wechselwirkung aus Dichte- und Spinkopplung steht laut Codex' Neubewertung in Gl. 4–6 des Haupttextes. Von mir nicht im Volltext geprüft, daher [L?].
  - Codex' weitere neue Kandidaten habe ich nicht geprüft, alle [L?]: Smolyakov 1711.05730 und 1906.02117, Kovtun/Nugaev/Shkerin 1805.03518, Peletminskii u. a. 1911.11391.
- *Anforderung:*
  - Die Entscheidungen der Neubewertung in v0.6 umsetzen.
  - Die Spinor-Struktur als bekannte Einordnung von (3) und der Winkelquartik ergänzen, nach eigener Volltextprüfung.
  - Den Satz „kein Neuheitsanspruch“ damit konkret machen. Die natürliche Symmetrie der lokalen Nichtlinearität ist SO(3), also Spinor. U(3) verlangt das Verschwinden des |a·a|²- bzw. |F|²-Koeffizienten.
  - Das passt zu concept-review-tus §8 und concept-controls Idee 1.

### Klein

**K1 – Energiedrift falsch gerundet.**
- *Stelle:* §5, Absatz nach der Tabelle, „1,17 × 10⁻¹²“.
- *Beleg:* su3-interactions/RESULT.json, Arm J = 0,15 und h = 0,4: fein (tol 10⁻¹¹) 1,1633·10⁻¹², grob 1,1808·10⁻¹². ERGEBNIS.txt enthält dieselbe 1,17.
- *Vorschlag:* 1,16 × 10⁻¹² (fein), oder „unter 1,2 × 10⁻¹²“.

**K2 – CPU-Zeit doppelt gerundet.**
- *Stelle:* §5.2, „0,0183 CPU-s“.
- *Beleg:* field-mechanism/RESULT.json cpu_seconds = 0,0182487. ERGEBNIS rundet zuerst auf 0,01825.
- *Vorschlag:* 0,0182.

**K3 – Toleranzen unvollständig beschrieben.**
- *Stelle:* §3 „DOP853 mit Toleranzen 10⁻⁹ und 10⁻¹¹“ und §5 „zwei Genauigkeitsstufen“.
- *Beleg:* su3-triplets/run.py und su3-interactions/run.py: rtol = tol, atol = 0,01·tol.
- *Vorschlag:* rtol und atol nennen.

**K4 – „hebt die Entartung auf“ ist zu stark; Mengenschreibweise mehrdeutig.**
- *Stelle:* §2, Absatz zur Kantenstörung.
- *Beleg:* one_edge_perturbed_spectrum ergibt {4; 4; 4,02} bzw. {2; 2; 2,00497}. Ein Dublett bleibt.
- *Vorschlag:* „spaltet in Dublett und Singulett“.
- *Außerdem:* Die deutsche Schreibweise „{4,4,4,02}“ bzw. „{2,2,2,0049688749}“ ist wegen des Dezimalkommas mehrdeutig. Hier fehlt noch der Semikolon-Trenner, den das README für Vektoren erwähnt. Die englische Fassung ist eindeutig.

**K5 – Basisunabhängigkeit des 54-Fälle-Befunds nicht belegt.**
- *Stelle:* §4.1.
- *Beleg:*
  - §4 sagt selbst, dass eine relative Basiswahl bei gleichen Singulärwerten helfen könnte.
  - Laut su3-interactions/RESULT.json ist die kleinste Singulärwertspreizung 0,0144 (Würfel, d = 3, ℓ = 2), beim Tetraeder 0,0170.
  - Beim Würfel sind die Selbstblöcke in allen 27 Fällen isotrop (Anisotropie ≤ 2·10⁻¹⁶). Beim Tetraeder liegt die Anisotropie bei mindestens 0,0859.
- *Vorschlag:* Einen Satz ergänzen: Auch die basisunabhängige Singulärwertspreizung lag in allen Fällen bei mindestens 0,0144. Damit rettet keine relative Basiswahl einen Fall. Bei den gedrehten Orientierungen schließt das die naheliegende Rückfrage.

**K6 – Stellenzahl über der Konvergenz; gleiche Größe mit zwei Werten.**
- *Stelle:* §5.3 „A = 3,9375147759“, §5.2 Tabelle (|J| mit 6–7 Stellen, t = 274,976), §5.2 gegen §5.3 (68,151 % gegen 68,153 %; 274,976 gegen 274,965).
- *Beleg:*
  - shell-detuning/RESULT.json: Die Nullstelle wandert von h = 0,025 nach h = 0,0125 um 4,5·10⁻⁶ (3,93751932 → 3,93751478).
  - field-mechanism: Die relative Änderung von J bei Gitterhalbierung liegt bis 3·10⁻⁴. t ist 275,020 bei h = 0,05 gegen 274,976.
  - §5.3 verwendet h = 0,0125, §5.2 dagegen h = 0,025.
- *Vorschlag:* Stellen der Konvergenz anpassen, etwa A ≈ 3,93752. Oder den Gitterunterschied zwischen §5.2 und §5.3 ausdrücklich nennen.

**K7 – |δ|-Aussage gilt nur für das feinste Gitter.**
- *Stelle:* §5.3, „Numerisch beträgt |δ| < 5 × 10⁻¹⁴“.
- *Beleg:* h = 0,0125: 4,84·10⁻¹⁴; h = 0,025: 5,60·10⁻¹⁴.
- *Vorschlag:* „auf dem feinsten Gitter“.

**K8 – Eigenwerte und Schwellenabstand fehlen.**
- *Stelle:* §5.2, „Zwei exakte radiale Eigenfunktionen mit positiven Eigenwerten e₁,e₂“.
- *Beleg:* field-mechanism/RESULT.json: e₁ und e₂ liegen zwischen 8,03 und 8,78, also unter der Kontinuumsschwelle 10. Der dritte Boxwert liegt über 10. SOURCE-3.txt, Punkt 9, empfiehlt dasselbe.
- *Vorschlag:* e₁ und e₂ je d und den Abstand zur Schwelle 10 nennen. Das stützt „gebunden“ und die Dirichlet-Box.

**K9 – Mehrfach belegte Symbole.**
- *Stelle:* ganzer Text.
- *Beleg:*
  - λ steht für den Laplace-Eigenwert (§2, (10)), die quartische Konstante ((7)), die Gell-Mann-Matrizen und λ_min.
  - A steht für Selbstblock, Generatorindex, Bausteinlabel, Muldentiefe (§5.3) und L₊ ((14)).
  - h steht für Vermittlerkopplung und Gitterschritt.
  - K steht für Federkonstante und die 2×2-Matrix (12).
  - L steht für Laplacian und Lagrangedichte (11).
  - P steht für Impuls, Projektor, P₂ und P_B(t).
  - N steht für Plätze und Komponenten (W4).
  - Q steht für Q_A und die Q-Ball-Ladung.
  - d steht für Clusterabstand und Schalenabstand.
- *Vorschlag:* Die Symboltabelle in §1 erweitern oder gezielt umbenennen, etwa Tiefe → V_a, Gitterschritt → Δr, Vermittlerkopplung → κ.

**K10 – Schon SU(3) ist gebrochen, nicht nur U(3).**
- *Stelle:* §3 „Die lineare U(3)-Symmetrie überlebt diese lokale Nichtlinearität nicht“ und §5.2 „widerlegt die automatische U(3)-Invarianz“.
- *Beleg:*
  - SU(3) wirkt transitiv auf der Einheitssphäre in ℂ³. Zwei gleichnormige Zustände mit verschiedener Energie belegen also bereits den Bruch der SU(3)-Untergruppe.
  - concept-review-tus §8 gibt dazu das Beispiel diag(1, i, −i) ∈ SU(3).
  - concept-controls meldet SU(3)-Reste von 0,246 bis 1,948.
- *Vorschlag:* Das für ein Paper über eine SU(3)-Deutung ausdrücklich sagen.
- *Optional, eigene Ableitung, vom Autor zu prüfen:* Die Restsymmetrie der projizierten Quartik (3) ist U(1) mal den vorzeichenbehafteten Permutationen, also eine diskrete Würfelgruppe. Grund: Die Invarianz von |a·a|² erzwingt W = e^{iθ}R mit reellem orthogonalem R. Σ(Ra)_α⁴ legt R dann auf vorzeichenbehaftete Permutationen fest.

**K11 – Bezug von „dessen“ mehrdeutig.**
- *Stelle:* §2, „rechtfertigt dessen isolierte Verwendung daher nicht“.
- *Beleg:* „dessen“ kann sich auf Modus oder Triplett beziehen. main.tex übernimmt die Mehrdeutigkeit („using it in isolation“). Die englische HTML-Fassung löst sie richtig auf („treating the triplet in isolation“).
- *Vorschlag:* „des Tripletts“, im LaTeX wie im HTML.

**K12 – Abgrenzungen, die erst die Assoziation erzeugen.**
- *Stelle:*
  - Überschrift §5.3 „Was die 68 % bedeuten“,
  - §5.3 „kein eigenständiger dunkler Sektor. Kosmologische Größen kommen in diesem Modell nicht vor“,
  - Bildtitel links „68% is not a fixed value“,
  - §8 „… oder ein Millennium-Beweis wird beansprucht“.
- *Beleg:* Ohne Projektkontext sind die Sätze unverständlich. Sie legen Leser erst auf Dunkle Energie bzw. das Yang-Mills-Millenniumproblem hin.
- *Vorschlag:* Sachliche Überschrift, etwa „Verstimmung begrenzt den Transfer bei d = 4“. Kosmologie- und Millennium-Sätze ins README bzw. in die Projektnotizen verschieben.

**K13 – Box und Gitter wurden gemeinsam verändert.**
- *Stelle:* §5.4, „schrumpft ungefähr quadratisch mit h“.
- *Beleg:* qball-l1-gap/PLAN.txt verändert Box und Gitter gemeinsam (R 24/32/40 mit h 0,08/0,04/0,02). Der Faktor ist 4,00 je Stufe.
- *Vorschlag:* „bei gemeinsamer Box- und Gitterverfeinerung“.

**K14 – PDG-Zitierform.**
- *Stelle:* [2].
- *Beleg:* Die PDF-Fußzeile nennt „S. Navas et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024) and 2025 update“.
- *Vorschlag:* Die RPP-Referenz ergänzen. Die PDG bittet um diese Zitierform.

**K15 – Titel im HTML uneinheitlich.**
- *Stelle:* deutsches `<title>` „… und ihre Wechselwirkungen“ gegen H1 „… und symmetrieverträgliche Wechselwirkungen“.
- *Vorschlag:* angleichen. Die englische Fassung folgt der H1.

**K16 – Kern in §5.1 zu ungenau benannt.**
- *Stelle:* §5.1, „der Abstandskern aus Abschnitt 4.1“.
- *Beleg:* §4.1 enthält drei Reichweiten. Der Stern verwendet ℓ = 2 und Verschiebungen ±4eₖ (su3-network/run.py: exp(−|Δr|²/8)).
- *Vorschlag:* ℓ = 2 und Abstand 4 nennen.

**K17 (optional) – Die Schranke ist nur hinreichend.**
- *Stelle:* §5, „Für positive ω, J, K und λ > h²/K ist die Energie nach unten beschränkt“.
- *Beleg:* Die Aussage ist richtig, aber nur hinreichend. ω spielt für die Beschränktheit keine Rolle. Wegen ‖a−b‖² ≤ 2(S_A+S_B) genügen K > 0 und λ > h²/K für jedes reelle J.
- *Vorschlag:* Nur präzisieren, wenn gewünscht.

### Englische LaTeX-Fassung (nur -en-codex)

**E1 – Sinntreue (Stichproben): ohne inhaltlichen Befund.**
- Gegen v0.5 verglichen habe ich:
  - Abstract,
  - §1 mit Tabelle,
  - §2: Folgerung, U(3) ≅ …/ℤ₃ und Kantenstörung,
  - §3,
  - §4 mit Kommutant und relativer Basiswahl,
  - §4.1 mit Kasten,
  - §5: Schranke, statische gegen dynamische Elimination, Noethergrößen, BIC-Satz,
  - §5.1: Schluss „disproves the transfer …“,
  - §5.2: Normierung, Randbedingungen, Deutung der Prozente, Kaminaga-Absatz, Kasten,
  - §5.3,
  - §5.4 mit Kasten,
  - §6,
  - §7: Punkte 3, 5 und 6,
  - §8,
  - Literatur.
- Keine Einschränkung fehlt, keine Aussage ist verstärkt. Die Zahlen sind identisch; Codex' QA hat das zusätzlich automatisch geprüft.
- Einzige Mehrdeutigkeit ist K11.

**E2 – Wortwahl zwischen den beiden englischen Fassungen uneinheitlich.**
- *Beleg:*
  - main.tex verwendet „gate(s)“ sechsmal als ganzes Wort, das HTML „criterion“.
  - main.tex hat „four arms were computed“ und „the last arm“ (Projektjargon).
  - main.tex hat zweimal „Computing location“.
- *Vorschlag:*
  - an die HTML-Wahl angleichen: „criterion“ bzw. „acceptance criterion“, „four parameter settings (runs)“,
  - „Computation:“,
  - Hostnamen wie in W4 ersetzen.

**E3 – LaTeX-Struktur.**
- *Beleg:*
  - Alle Abschnitte sind `\section*` mit fest eingetippten Nummern. Das PDF hat daher keine Gliederung (Lesezeichen), und es gibt kein `\label`/`\ref`.
  - Die Literatur ist eine `enumerate`-Liste, deshalb sind die „[n]“ im Text nicht verlinkt.
  - Gleichungsverweise sind Text.
- *Vorschlag:*
  - nummerierte `\section`/`\subsection` mit `\label`/`\ref`,
  - `thebibliography` mit `\cite`,
  - `\eqref` für die mit `\tag` gesetzten Gleichungen.
- *Positiv:* Zwei lokale pdflatex-Läufe einer Kopie von main.tex erzeugen ein textgleiches PDF (pdftotext-Diff leer). Es sind 10 Seiten A4 mit 0 Overfull-Boxen. Die 2 Underfull-Boxen in der Pfadliste von §8 sind harmlos. Alle Schriften sind als Type 1 eingebettet.

**E4 – Abbildung (Seite 7).**
- *Beleg:*
  - Rechts überdeckt die Legende die orange Kurve nahe ihrem Maximum (t ≈ 330–450).
  - Legende und Achsenbeschriftungen sind im Druck sehr klein, etwa 5–6 pt.
  - Die y-Achse rechts, „Outer fraction / outer mode combination“, mischt zwei Größen. Die Bildunterschrift trennt sie richtig.
- *Vorschlag:*
  - Legende unter die Grafik oder außerhalb der Achsen setzen, größere Schrift.
  - Achse als „canonical population (lines) / spatial energy fraction (crosses)“ beschriften.
  - Linken Bildtitel sachlich fassen (K12).

**E5 – Herkunftsangabe im Dokument.**
- *Beleg:* Wer übersetzt hat und auf welcher deutschen Datei die Fassung beruht, steht nur im README. Im PDF steht nur „English translation of version 0.5“.
- *Vorschlag:* Eine Zeile im Kopf oder in der Fußnote: Übersetzung der deutschen Arbeitsfassung v0.5 durch Codex (OpenAI), sinntreu gegengelesen. Autorschaft weiter offen. Die Entscheidung über den Wortlaut liegt bei Codex.

---

## 4. Grenzen dieser Prüfung

- Kein Physiklauf und keine Neuberechnung. Die Zahlen habe ich mit jq gegen RESULT.json, LEAKAGE.json und ERGEBNIS.txt verglichen. Die Mathematik habe ich von Hand nachgerechnet.
- Lokal nur Darstellung und IO: pdflatex auf einer Kopie im Scratchpad, pdftoppm, pdftotext, sha256sum, jq. Kein Python außer peer_bus.py, kein awk.
- In Codex' Ordnern wurde nichts geändert.
- Die Zitate [1]–[4] habe ich an den von Codex gesicherten PDFs gelesen (Hashes stimmen), nicht neu heruntergeladen. Ho (1998) habe ich nur am arXiv-Abstract gelesen. Codex' weitere Literaturkandidaten sind nicht geprüft.
- Die englische Fassung habe ich stichprobenartig auf Sinn geprüft, main.tex aber vollständig gelesen. Das englische paper.html habe ich nur auf die Wortwahl verglichen.
- concept-review-tus und concept-controls betreffen Folgearbeiten über v0.5 hinaus. Ihr Bezug zu v0.5 ist in K10 und W5 vermerkt. Als Beispiel: Die zeitgemittelte Realfeld-Quartik behält den |a·a|²-Term, was die Aussage in §5.2 stützt. Eine eigene Prüfung dieser Dokumente habe ich nicht durchgeführt.
- Keine externe Begutachtung. Das Review ist ein Fremdhaus-Review innerhalb des Projekts.

## 5. Zustellung und Antwort des Autors

- **Versand:** Das Review ging am 30.09. um 10:09 CEST über den Peerbus an ag-phy-coordination und ag-phy-lat (kind result). Die Nachrichten wurden jeweils in die Codex-Sitzung eingereiht.
- **Antwort von ag-phy-coordination** (ack, 10:10:02 CEST):
  - W1–W5 sind angenommen. Zuerst entsteht die deutsche v0.6, ohne neue Physikrechnung.
  - K1–K17 werden einzeln dokumentiert.
  - Den optionalen Restsymmetrie-Satz aus K10 übernimmt der Autor nicht ungeprüft.
  - E2–E5 folgen danach durch ag-phy-lat.
  - Bitte: die deutsche paper.html nicht parallel bearbeiten. Das ist bestätigt (ack um 10:10:29 CEST).

## 6. Einfach gesagt

Das Paper prüft, ob kleine geometrische Körper wie Tetraeder und Würfel drei gleichwertige Schwingungen haben, die wie die drei „Farben“ der Quarks aussehen. Die Rechnungen stimmen, und die Zahlen passen zu den gespeicherten Ergebnissen. Die Autoren sagen ehrlich, wo die Idee nicht trägt. Das Hauptproblem ist die Zusammenfassung am Anfang. Sie ist älter als der Rest und verspricht bei einem Punkt mehr, als der Text später zeigt. Die englische Fassung ist gut übersetzt und sauber gesetzt; sie muss nur die Korrekturen der deutschen Fassung übernehmen.

---

## 7. Nachtrag: gezielte Nachlesung der deutschen v0.6

- **Auftrag:** Leitung, 2026-09-30 10:23:30 CEST. Nachlesung nur der neuen Absätze in §7. Dazu Stichproben, ob W1–W5 und K1–K17 umgesetzt sind. Alte Rechnungen werden nicht wiederholt.
- **Beginn:** 2026-09-30 10:24:07 CEST (date). **Schreibbeginn Nachtrag:** 2026-09-30 10:29:24 CEST (date).

**Gegenstand (sha256):**

| Datei | sha256 |
|---|---|
| `model-lab/papers/su3-geometric-triplets-20260930/paper.html` (v0.6, mtime 10:19:29; identisch mit `paper-v06/paper.html`) | `a2a1d838bfc521d88c2143a1d8cdf8b815cb66b5c86042af5f75833f67239254` |
| `coordination/resonance-20260930/paper-v06/REVISION.txt` | `ceb0908678f1b14170528d733cee4a2e65164319c59e7fe364d8b4c8d72a9c22` |
| `coordination/resonance-20260930/source-audit/V06-SPIN1-QUELLEN.txt` | `d3a4ebd9b048f95b6435840fb4ca2a5977aecd8a846c47872bc68911acf51798` |
| `coordination/resonance-20260930/source-audit/SPIN-HALB-ANSCHLUESSE.txt` | `8af994d0961ea451cb3cdfa4c35dbd360d1e23469e1f67462d0c2f05f4b2a848` |

Die Hashes stimmen mit `paper-v06/SHA256SUMS.txt` überein.

### 7.1 Urteil zu v0.6

**Trägt.** Die Auflagen W1–W5 und K1–K17 sind sachgerecht umgesetzt. Die neuen §7-Absätze sind mathematisch richtig, und ihre Quellen stimmen. Offen sind zwei Punkte:

- **N1:** Beim Revisionsschritt ist ein neuer Formelfehler entstanden.
- **N2:** Der Spin-½-Absatz bleibt hinter dem bekannten Befund zurück.

Beide Punkte vor jeder Weitergabe beheben. Sie gehen auch in die englische Fassung über, sobald ag-phy-lat nachzieht.

### 7.2 Umsetzung von W1–W5 und K1–K17 (Stichproben)

- **W1:** Die Zusammenfassung ist jetzt richtig. Sie nennt:
  - die statische Sechs-Richtungs-Summe als isotrop, aber im Netz unabhängiger Nachbarn nicht sektorerhaltend,
  - dass passende Verbindungen beide Prüfungen bestehen,
  - das Schalen-Kontrollmodell,
  - die Verstimmung,
  - den Box-Nullbefund am Q-Ball mit Kontinuumsgrenze.
  Das deckt sich mit §4.2 und §§6.1–6.3.
- **W2:** Das Netz steht jetzt als §4.2, die Feldteile als §6.1–6.3, dazu das Fazit §10. §9 nennt alle sechs Datenordner und source-audit. Laborbuch-Formulierungen habe ich nicht mehr gefunden.
- **W3:** Durchgehend heißt es „Kontrollmodell mit vorgegebenen Schalen“. Das Wort „Feldmechanismus“ kommt nicht mehr vor, und der Kasten in §6.1 ist richtig eingegrenzt.
- **W4:** Die Q-Ball-Teile sind jetzt selbsterklärend.
  - §1 hat einen Kontextabsatz.
  - §6.3 nennt Lagrangedichte, Profilgleichung, Ladung Q_φ und ρ.
  - Geprüft: Die Profilgleichung f″ + 2f′/r = (1−ω²)f − 2f³ + 3f⁵/2 und Q_φ = 2ω∫f²d³x ≈ 473,413 stimmen mit `linear3d/run.py` überein (dort Q = ∫2ωf²·4πr²dr).
  - TS440, .69, Higgsportal/Q250, Gesamtformel, Millennium, Dunkler Sektor und Kosmologie kommen nicht mehr vor.
- **W5:** Hammer steht nur noch als entfernte Analogie. Kovtun et al. und Ho sind ergänzt (siehe 7.3).
- **K1–K17:** Alle gefunden.
  - Wörtlich geprüft: 1,16·10⁻¹²; 0,0182 CPU-s; rtol/atol an beiden Stellen; Dublett/Singulett mit Semikolon; 0,0144; Va ≈ 3,937515 samt Erklärung 68,151 gegen 68,153 %; |δ| auf dem feinsten Gitter.
  - Die Eigenwerttabelle in §6.1 stimmt mit field-mechanism/RESULT.json überein: 8,03325/8,77246, 8,27069/8,47283, 8,33085/8,39694.
  - Weiter: Notationsabsatz; SU(3)-Bruch wegen Transitivität; „des Tripletts“; neutrale Überschriften; gemeinsame Box- und Gitterverfeinerung; Navas et al.; `<title>` gleich H1; ℓ = 2/Abstand 4; Schranke als hinreichende Bedingung.
- **E4 (deutsche Abbildung):** neu gesetzt. Die Legenden liegen außerhalb der Datenfläche, die Schrift ist größer, die Titel sind sachlich („Frequenzabgleich steigert den Transfer“, „Reversibler Austausch“).

### 7.3 Neue §7-Absätze: Mathematik und Quellen

- **Spin-1-Invarianten.**
  - F = −i a*×a und |F|² = S² − |a·a|² stimmen (Binet–Cauchy).
  - (3) = [3S² − |F|² − 2Σ|a_α|⁴]/N stimmt.
  - Die Winkelquartik 3[3S² − |F|²]/(20π) ist SO(3)-invariant, stimmt.
  - **Ho [5] im Volltext geprüft**, arXiv:cond-mat/9803231v1, eigene Kopie über arXiv (Kopfstempel „18 Mar 1998“):
    - Gl. (4): V = c₀ + c₂F₁·F₂ mit c₀ = (g₀+2g₂)/3 und c₂ = (g₂−g₀)/3.
    - Gl. (6): Wechselwirkung (n²/2)[c₀ + c₂⟨F⟩²] mit normiertem Spinor. Mit der unnormierten Spindichte ist das c₀n²/2 + c₂|f|²/2, wie im Paper.
    - Polarer Zustand bei c₂ > 0 (Gl. 7), ferromagnetischer bei c₂ < 0 (Gl. 8).
  - Die Abgrenzung (keine Streulängen, kein quantisierter Spin, zunächst orbitaler Drehimpuls) ist richtig und wichtig.
- **Einfeld-Linearisierung.**
  - **Kovtun, Nugaev, Shkerin [6] im Volltext geprüft**, arXiv:1805.03518v2, eigene Kopie; bibliografische Daten PRD 98, 096016 (2018) auf der arXiv-Seite bestätigt:
    - Gl. (12): h = z·d²V/dz² und g = z·d²V/dz² + dV/dz bei z = f².
    - Gl. (15): Seitenbänder ω ± γ.
    - Text nach Gl. (22): (2l+1)-Entartung.
    - Gl. (9): Q = 8πω∫r²f²dr, also dieselbe Ladung wie Q_φ.
  - Für U(S) = S − S² + S³/2 folgen h = −2f² + 3f⁴ und g = 1 − 4f² + 9f⁴/2. Stimmt.
  - Konsistenzprobe mit (14): g + h − ω² = 0,3 − 6f² + 7,5f⁴ = A und g − h − ω² = 0,3 − 2f² + 1,5f⁴ = B.
  - Den Hinweis „Ursprungsvorgaben l-abhängig“ in [6] teile ich. Gl. (16) der Quelle setzt dψ/dr(0) = 0 pauschal.
- **Spin ½.**
  - Folgende Aussagen stimmen:
    - Eine 2π-Drehung wirkt auf l = 1 als Identität.
    - SU(2) ⊂ SU(3) zerfällt als 2 ⊕ 1.
    - Sym²(ℂ²) ≅ ℂ³ ist eine Darstellungsidentität, kein Bestandteilnachweis.
  - **Krusch und Speight [7] am arXiv-Abstract geprüft:** hep-th/0503067v2, CMP 264 (2006) 391–410. Sie quantisieren Hopf-Solitonen nach Finkelstein–Rubinstein und erhalten Fermionen bei ungerader Hopf-Ladung; die Bedingungen hängen daran, ob die Schleifen kontrahierbar sind. Den Volltext habe ich nicht gelesen.
  - Zur Präzision siehe N2.

### 7.4 Neue Befunde

**N1 (wesentlich; Formelfehler, neu in v0.6).**
- *Stelle:* §6.2, „erhält die innere Teilenergie den Randterm −u(9)²/16“.
- *Beleg:*
  - Der Schnitt liegt bei r = 8 („lokale Energie für r > 8“). Der Randterm ist −½·u(8)²/8 = −u(8)²/16.
  - v0.5 hatte richtig u(8). `paper-v06/paper-v05.html` hat u(8), `paper-v06-stage.html` schon u(9).
  - Der Fehler entstand also beim Revisionsschritt, vermutlich als Nebenwirkung der Gleichungs-Umnummerierung (alte (8) wird (9)); das ist eine Hypothese.
  - Andere solche Nebenwirkungen habe ich bei den Gleichungsmarken (7)–(10) nicht gefunden.
- *Vorschlag:* auf u(8) zurücksetzen. ag-phy-lat darf den Fehler nicht ins Englische übernehmen.

**N2 (wesentlich; Präzision des Spin-½-Absatzes).**
- *Stelle:* §7, letzter Satz von „Abgrenzung zu Spin ½“: „besitzt bislang weder diesen nachgewiesenen topologischen Sektor noch diese Quantisierung …“.
- *Beleg:*
  - Codex' eigener Quellenbericht SPIN-HALB-ANSCHLUESSE.txt, Teil D, hält fest: Reguläre Konfigurationen endlicher Energie lassen sich durch Amplitudenskalierung zum Nullfeld zusammenziehen.
  - Der Konfigurationsraum des unveränderten Einfeldmodells ist also zusammenziehbar. Beispiel: φ_t = (1−t)φ. Die Energie bleibt endlich, weil U′(S) = 1 − 2S + 1,5S² > 0.
  - Deshalb ist π₁ trivial. Die Schleife einer 2π-Drehung ist zusammenziehbar, und eine Finkelstein–Rubinstein-Vorzeichenwahl existiert in diesem Modell nicht.
  - Weil der Konfigurationsraum konvex ist, ist auch H²(Q;ℤ) = 0. Damit ist zugleich ein Weg über einen Wess–Zumino- bzw. Sorkin-Term verschlossen. Das ist eigene Einordnung.
  - Das „bislang“ lässt einen Weg offen erscheinen, der für die unveränderte Theorie verschlossen ist. So hält es auch das Projekt fest: `coordination/gesamtmodell-20260927/GESAMTMODELL-ENTWURF.md`, Zeile X6 („Konfigurationsraum zusammenziehbar und nur bosonisch; Spin 1/2 braucht einen Umbau (C × S²)“, mit Verweis auf KANDIDAT 3.4).
- *Anforderung:*
  - Die bekannte Hürde ausdrücklich nennen: zusammenziehbarer Konfigurationsraum, daher bosonische Quantisierung. Spin ½ verlangt eine Modelländerung, etwa einen Zielraum mit nichttrivialer Topologie.
  - Codex' Vorbehalt zum reduzierten Phasenraum bei fester Noetherladung kann als ausdrücklich markierte offene technische Anmerkung bleiben. Aus meiner Sicht ändert die Ladungs-Superauswahl die Topologie des Konfigurationsraums nicht. Das ist eigene Einschätzung, nicht auditiert.

**N3 (klein).**
- *Stelle:* Kopfzeile „Interner Forschungsentwurf mit dokumentiertem unabhängigen Review; keine Zeitschriftenbegutachtung“ und Schlusszeile „Ein unabhängiges internes Review ist eingearbeitet“.
- *Beleg:*
  - Mein Review ist ein projektinternes Fremdhaus-Review. Es betraf v0.5 und nun die neuen §7-Absätze, nicht eine unabhängige Begutachtung im üblichen Sinn.
  - Der Vermerk „Autorschaft und Publikationsfassung noch festzulegen“ ist ohne dokumentierte Entscheidung entfallen.
- *Vorschlag:* „projektinternes Fremdhaus-Review (Anthropic)“ schreiben. Den Autorschaftsvermerk beibehalten, bis Finn entscheidet.

**N4 (klein).**
- *Stelle:* §8, Punkt 3, „Gleichung (3) ist der verpflichtende Gegenbeispiel“.
- *Vorschlag:* „das verpflichtende Gegenbeispiel“. Der Artikel blieb vom früheren „Gegenarm“ stehen.

**N5 (klein).**
- *Stelle:* Literatur [7], „Geprüft: Einleitung und Konfigurationsraum-/Hopf-Abbildung in §2“.
- *Beleg:* SPIN-HALB-ANSCHLUESSE.txt verzeichnet für dieselbe Quelle „Einleitung, §3 Gl. (3.1) … sowie §4“.
- *Vorschlag:* Den Lesevermerk mit dem Auditprotokoll abgleichen.

**N6 (klein).**
- *Stelle:* Notationsabsatz §1, „ℒ die Feldwirkung“.
- *Beleg:* In (11) ist ℒ die Lagrangefunktion (räumlich integriert), in §6.3 die Lagrangedichte. Die Wirkung wäre ∫ℒdt.
- *Vorschlag:* „ℒ die Lagrangefunktion bzw. -dichte“.

**N7 (klein, optional).**
- *Stelle:* §1, „sogenannte Q-Bälle“, ohne Beleg.
- *Vorschlag:* eine Standardreferenz ergänzen, etwa S. Coleman, Nucl. Phys. B 262, 263 (1985) [L?]. Von mir nicht an der Quelle geprüft.

### 7.5 Antwort des Autors und Kurzprüfung v0.6a

- **Versand:** Der Nachtrag ging um 10:31 CEST über den Peerbus an ag-phy-coordination und ag-phy-lat.
- **Antwort von ag-phy-coordination:** 10:33:17 CEST, als deutsche Fassung v0.6a (`paper-v06a/`, paper.html sha256 `eb04ab2fa4c6f329db550c3dbe3b15f9ce32fb0347918654fba46429989c51c0`).
- **Kurzprüfung** um 10:33:43 CEST (date), nur die betroffenen Stellen:
  - **N1 behoben:** Der Randterm lautet wieder −u(8)²/16. Laut Autor hatte eine zu breite Ersetzung aller „(8)“ die Ursache; er hat alle betroffenen Klammerausdrücke abgeglichen (PARENTHESIS-AUDIT.txt).
  - **N2 behoben, richtig begrenzt.** Der neue Wortlaut:
    - Der Konfigurationsraum ist über Hₜ(φ) = (1−t)φ zusammenziehbar, π₁ und H² sind trivial.
    - Weder eine FR-Vorzeichenwahl noch ein Wess–Zumino-Linienbündel steht zur Verfügung. Die kanonische Quantisierung ist bosonisch.
    - ℂ × S² gilt ausdrücklich als andere Theorie.
    - Der Vorbehalt zum reduzierten Phasenraum bei fester Ladung ist als offener Punkt markiert, mit dem Zusatz „liefert selbst keinen Spin-½-Nachweis“.
    - Mathematisch stimmt das, auch der Zusatz, dass die Kontraktion die Ladung nicht erhält.
  - **N3, N4 und N6 umgesetzt:** „Fremdhaus-Review“, der Autorschaftsvermerk ist wieder da, „das verpflichtende Gegenbeispiel“, „Lagrangefunktion“.
  - **N5:** laut Autor zusammengeführt. Den Wortlaut von [7] habe ich nicht erneut geprüft.
  - **N7:** bewusst nicht aufgenommen, weil die Referenz ungeprüft wäre. Das ist richtig.
- Die englische Fassung soll laut Autor auf v0.6a aufsetzen, nicht auf v0.6. Grund ist N1.

### 7.6 Grenzen der Nachlesung

- Keine Rechnung wiederholt.
- Ho und Kovtun et al. habe ich im Volltext an eigenen arXiv-Kopien gelesen. Die Kopien liegen nur im Sitzungsordner und sind nicht im Projekt abgelegt.
- Krusch–Speight nur am Abstract; Borja et al. und Krusch 2002 (in SPIN-HALB-ANSCHLUESSE.txt) nicht geprüft.
- Die übrigen Abschnitte habe ich nur stichprobenartig gegen die Revisionsliste gelesen.

### 7.7 Einfach gesagt (Nachtrag)

Codex hat fast alle unsere Hinweise gut eingebaut. Die Zusammenfassung erzählt jetzt dieselbe Geschichte wie der Rest des Papers. Beim Umnummerieren der Formeln ist aus einer 8 eine 9 geworden, an einer Stelle, wo es gar keine Formelnummer war. Beim neuen Absatz zu Spin ½ stand zuerst nur „bisher nicht gezeigt“. Für das unveränderte Modell ist aber schon klar, dass es nicht geht; man müsste das Modell selbst ändern. Codex hat beides in wenigen Minuten richtiggestellt (Fassung v0.6a).
