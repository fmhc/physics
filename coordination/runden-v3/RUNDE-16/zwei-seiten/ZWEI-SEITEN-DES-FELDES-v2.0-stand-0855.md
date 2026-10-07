# Zwei Seiten des Feldes – Formeln und Arbeitsmodell (v2)

**Stand:** 2. Oktober 2026, überarbeitet ab 08:12:49 CEST (claude-primary, auf Finns „review das mal … improve“)
**Berichtigt** 02.10., eingetragen 08:49:06 CEST: Vorzeichen der Ladung Q in §1, §2 und §22. Die alte Form ergab Q = −2ω∫f². Gefunden beim Abgleich mit Codex' eigener Fassung (RUNDE-16/two-sides-review/codex/ARBEITSMODELL-V2.md, Zweifeldmodell ψ, χ).
**Ergänzt** 02.10., eingetragen 08:55:58 CEST: geprüfte Zahlen aus den Versuchen V1–V5 (ausprobieren/ERGEBNIS.md) und Codex' Berichtigung der Zählregel, in §2, §4, §6, §7 und §14.
**Status:** Exploratives mathematisches Spielzeugmodell. Etablierte Mathematik wird mit unbestätigten Modellhypothesen kombiniert. Hypothesen sind mit **[H]** markiert, Literatur aus dem Gedächtnis mit **[L?]** (vor Verwendung an der Quelle prüfen).

## Was sich gegenüber v1 geändert hat

1. **Feld:** kinetischer Term für komplexes Φ korrigiert. Existenzfenster der Q-Bälle und Erhaltungsladung ergänzt. Bezug zu unserem Projektmodell (U = S − S² + S³/2) hergestellt.
2. **Diskrete Seite:** Die Dynamik ist jetzt die echte Diskretisierung von §1 (gleiches Potential). Die Kopplung hängt von der Geometrie ab, sonst reden Feld und Geometrie nicht miteinander.
3. **Symbole:** In v1 stand λ für drei Dinge. Jetzt: λ, g = Feldkopplungen, μ_n = Eigenwerte, Λ = Lyapunov-Exponent.
4. **Schnitte:** Es wird unterschieden zwischen *Sonden-Schnitten* (Beobachterebene, wie im Tetra-Bündel) und *intrinsischen* Schnitten (bewegte Teile untereinander). Ticks sind jetzt als generische Ereignisse der Kodimension 1 in der Zeit definiert und werden über Vorzeichenwechsel von Orientierungsdeterminanten detektiert. Das macht sie unabhängig von der Schrittweite.
5. **Energie:** Mit positiven α kollabiert alles; deshalb jetzt Ruhelängen. Eine Schnittenergie über Punktzahlen hat keinen Gradienten, deshalb jetzt glatte Ersatzterme.
6. **Rotation und Stabilität:** relative Gleichgewichte aus der Kräftebilanz im mitrotierenden System. Stabilität mit gyroskopischem Term, Krein-Signatur und fester Ladung statt reiner Hesse-Matrix. Maxwells Ringproblem als Positivkontrolle.
7. **Namenskonflikt:** „11+1/19+1“ ist hier ein ebener Ring mit Zentrum, im Tetra-Bündel vom 02.10. dagegen eine Tetraederkette mit 12/20 Ecken. Beide Varianten sind jetzt getrennt benannt.
8. **Neu:** eine Brücke zum Projekt. Erster Test ist, ob die bewiesene stille Stelle des Q-Balls eine Diskretisierung überlebt.
9. **Leitidee ehrlicher:** In diesem Modell sind Zeit und 3D-Einbettung vorausgesetzt; „→ Raumzeit“ ist hier nicht testbar. Für Dimensionsfragen gibt es zusätzlich eine einbettungsfreie Variante.

## Leitidee

Geometrie → Feld → Schnitte → stabile Moden → teilchenartige Objekte → *(effektive Zeit- und Dimensionsgrößen)*

Ziel ist zu testen, ob aus einfachen lokalen geometrischen Regeln langlebige lokalisierte Moden, charakteristische Frequenzen, Schnitt-Ereignisse („Ticks“) und effektive Wechselwirkungen entstehen.

**Grenze dieses Modells:** Die Wirkung in §8 setzt eine äußere Zeit t und, in Variante A, Koordinaten x_i ∈ ℝ³ voraus. Ob Raumzeit *entsteht*, kann dieses Modell nicht zeigen. Prüfbar sind nur effektive Größen: Taktraten, spektrale Dimension und Wechselwirkungen.

## 1. Kontinuierliches Feld

Komplexes Skalarfeld, Signatur (+,−,−,−), mit s = |Φ|²:

$$
\mathcal L=\partial_\mu\Phi^*\,\partial^\mu\Phi-V(|\Phi|^2),\qquad V(s)=m^2 s-\lambda s^2+g\,s^3
$$

Feldgleichung:

$$
\partial_\mu\partial^\mu\Phi+V'(|\Phi|^2)\,\Phi=0,\qquad V'(s)=m^2-2\lambda s+3g s^2
$$

Erhaltene U(1)-Ladung (Noether):

$$
Q=2\,\mathrm{Im}\int d^3x\,\Phi^*\dot\Phi=i\int d^3x\,\big(\dot\Phi^*\Phi-\Phi^*\dot\Phi\big)
$$

(Für Φ = f e^{iωt} ist Q = 2ω∫f² d³x, also positiv für ω > 0.)

**Q-Bälle:** Φ = f(r) e^{iωt}. Sie existieren für

$$
\omega_{min}^2<\omega^2<m^2,\qquad \omega_{min}^2=\min_s\frac{V(s)}{s}=m^2-\frac{\lambda^2}{4g}
$$

Dabei ist λ > 0 nötig, und für ein stabiles Vakuum Φ = 0 zusätzlich λ² ≤ 4m²g. Stabil sind sie gegen Zerfall, weil Q erhalten ist.

**Projektmodell:** m² = 1, λ = 1, g = 1/2, also V = S − S² + S³/2. Dann ist ω_min² = 1/2. Dafür sind die „stillen Stellen“ bewiesen: Atmungsmoden, die nicht abstrahlen (l = 0, n = 1 bei ω² = 0,797677; l = 0, n = 2; l = 1, n = 1). Siehe §9a.

## 2. Diskrete Geometrie

Zellkomplex K = (V, E, F, C) mit Knoten, Kanten, Flächen und Volumenzellen. Am Knoten i:

- Ort x_i (Variante A, eingebettet) bzw. kein Ort (Variante B, nur Graph)
- komplexer Zustand Ψ_i(t) = A_i(t) e^{iθ_i(t)}

**Dynamik als Diskretisierung von §1:**

$$
\ddot\Psi_i+\sum_{j\sim i}J_{ij}(x)\,(\Psi_i-\Psi_j)+V'(|\Psi_i|^2)\,\Psi_i=0
$$

- Die Kopplung hängt von der Geometrie ab, z. B. J_ij = J(|x_i − x_j|). Erst dadurch wirken Feld und Geometrie aufeinander.
- Bei festen J_ij und V' = m² − 2λ|Ψ|² + 3g|Ψ|⁴ ist das der diskrete Partner von §1. Das Vorzeichen von λ entscheidet, ob die Nichtlinearität weich oder hart ist, und damit, ob lokalisierte Moden unterhalb oder oberhalb des Bandes liegen.
- Diskrete Ladung:

$$
Q=2\,\mathrm{Im}\sum_i\Psi_i^*\dot\Psi_i
$$

- **Existenzfenster: diskret breiter als im Kontinuum** (gerechnet am 02.10., V5; Schreibtischrechnung der Leitung):
  - Bei schwacher Kopplung (J → 0) sitzt die Mode auf einem Knoten. Dann gilt ω² = V'(S), und für das Projektmodell liegt das Fenster bei ω² ∈ (1/3, 1), denn das Minimum von V' ist 1/3 bei S = 2/3.
  - Im Kontinuum zählt dagegen min V(S)/S = 1/2.
  - Gerechnet: [0,475; 0,96] bei J = 0,05 und [0,59; 0,92] bei J = 0,1.
  - Das ist eine erste messbare Brücke zwischen den zwei Seiten des Feldes.

Zu testen: Tetraeder, 6er, 8er, geschlossene N-Ketten, die Varianten „Ring N+1“ und „Tetraederkette“ (§6), jeweils frei und rotierend.

## 3. Schnittmengen

$$
I_S=\bigcap_{i\in S}M_i,\qquad \dim(A\cap B)=\dim A+\dim B-\dim X\quad(\text{transversal})
$$

In 3D generisch: 2D ∩ 2D → 1D, 2D ∩ 1D → 0D, 1D ∩ 1D → leer.

**Welche M_i? (in v1 offen)** Innerhalb *eines* eingebetteten Zellkomplexes schneiden sich Zellen nur in gemeinsamen Teilzellen. Das ist reine Nachbarschaft, keine Dynamik. Sinnvoll sind zwei Arten:

- **Sonden-Schnitte:** Eine Beobachterebene oder -linie schneidet die Struktur, wie im Tetra-Bündel (Ebene ∩ Kanten). Das Ergebnis hängt von der Wahl der Sonde ab. Es ist eine Beobachtungsgröße, keine Eigenschaft des Systems.
- **Intrinsische Schnitte:** Bewegte Teile durchdringen einander. Das können verschiedene Komplexe sein, ein Komplex mit Selbstdurchdringung (nicht eingebettet) oder rotierende Kopien.

Zu messen: Schnittzahl N_I(t), Dimension d_I, Lebensdauer τ_I, Geburt und Vernichtung, räumliche Verteilung. Bei Sonden-Schnitten immer mit dem Sondenmaß, z. B. der Verteilung der Ebenennormalen.

## 4. Ticks aus Schnitt-Ereignissen

**Generische Ereignisse.** In einer zeitabhängigen Familie treten Schnitte mit erwarteter Dimension −1 nur zu einzelnen Zeitpunkten auf. In 3D sind das:

- Ecke durch Fläche (0 + 2 − 3 = −1)
- Kante durch Kante (1 + 1 − 3 = −1)

Ein Tick ist so ein Ereignis.

**Detektion, unabhängig von der Schrittweite:** über die Orientierungsdeterminante vierer Punkte,

$$
\chi_{abcd}(t)=\det\big[x_b-x_a,\;x_c-x_a,\;x_d-x_a\big]
$$

Ein Vorzeichenwechsel von χ zusammen mit einem Innen-Test (Punkt in der Fläche bzw. Kreuzung innerhalb beider Kanten) ist ein Tick. Der Zeitpunkt wird per Nullstellensuche verfeinert, nicht durch Vergleich zweier Zeitschritte.
- [H] Die Folge der Vorzeichenwechsel ist eine kombinatorische Uhr: ein Wechsel des Chirotops der Punktmenge.

**Rate** als Langzeitmittel:

$$
\nu=\frac{N_{events}(T)}{T},\qquad T\to\infty
$$

Ein Grenzwert Δt → 0 eines Zählers liefert nur Deltaspitzen.

**Gerechnet am 02.10. (V4, zwei sich durchdringende Tetraeder):**
- Ereignisgenau ergeben sich 1226 Ticks (229 Ecke-durch-Fläche, 997 Kante-durch-Kante) bei jedem Δt ≤ 0,1. Die Ereigniszeiten stimmen auf 4·10⁻¹³ überein.
- Die naive Zählung über Zeitschritte verliert Ereignisse etwa proportional zu Δt: 13 % bei Δt = 0,2.

**Hypothese [H]:**

$$
d\tau(x)\propto\nu(x)\,dt
$$

Das ist keine etablierte Physik. Bedingungen, bevor man sie ernst nimmt:

1. ν hängt nicht an Δt (Konvergenz bei Δt, Δt/2, Δt/4).
2. ν ist robust gegen kleine Störungen.
3. Bei Sonden-Schnitten: ν hängt nicht an der Sonde, oder die Abhängigkeit ist verstanden.
4. Das Modell ist galileisch. Ein Vergleich mit relativistischer Eigenzeit ist hier nicht möglich.
5. Prüfbar ist ein Analogon: Sinkt ν dort, wo die Energiedichte hoch ist? Mit welchem Exponenten? Erst eine Vorhersage dieser Art wäre mit Uhrenmessungen vergleichbar (gravitative Rotverschiebung).

## 5. Energie der Geometrie

**v1 (lineare Spannungen)** E = α_E ΣL + α_F ΣA + α_V ΣV kollabiert für positive α: Alle Längen gehen gegen 0. Für negative α bläht es sich auf. Deshalb mit Ruhegrößen:

$$
E_{geo}=\frac{k_E}{2}\sum_{e}(L_e-L_0)^2+\frac{k_F}{2}\sum_{f}(A_f-A_0)^2+\frac{k_V}{2}\sum_{c}(V_c-V_0)^2
$$

Alternativ: lineare Spannung plus abstoßender Kern.

**Schnittenergie:** Eine Energie aus Punktzahlen, Längen oder Flächen von Schnittmengen ist stückweise konstant oder springt. Ihr Gradient ist fast überall null, an Ereignissen unendlich. Deshalb glatt ersetzen, z. B. durch eine weiche Überlapp- oder Abstandsfunktion:

$$
E_{int}=\sum_{(a,b)}\beta\,\sigma\!\big(d_{ab}/\ell\big)
$$

d_ab ist der vorzeichenbehaftete Abstand bzw. die Eindringtiefe, σ eine glatte Stufe, ℓ die Glättungslänge. Die Grenzfälle ℓ → 0 werden geprüft.

**Feld-Geometrie-Kopplung:**

$$
E_{field}=\sum_{\langle ij\rangle}J(|x_i-x_j|)\,|\Psi_i-\Psi_j|^2+\sum_i V(|\Psi_i|^2)
$$

(Summe über Paare ⟨ij⟩, jedes Paar einmal. Dann folgt aus §8 genau die Gleichung in §2.)

Daraus folgen die Kräfte F_i = −∇_i E. Eine „Anziehung“ entsteht daraus, wenn sie entsteht, und wird nicht nachträglich eingesetzt.

## 6. Rotierende Systeme: zwei getrennt benannte Varianten

**Variante R („Ring N+1“):** N Punkte auf einem Kreis plus ein Zentrum.

$$
x_j(t)=R\,(\cos\theta_j,\sin\theta_j,0),\qquad \theta_j=\frac{2\pi j}{N}+\Omega t,\qquad x_{N+1}=0
$$

- Das ist nur dann eine Lösung (relatives Gleichgewicht), wenn die Kräftebilanz im mitrotierenden System erfüllt ist: m R Ω² = F_innen(R). Daraus folgt R(Ω) und nicht frei wählbar.
- **Positivkontrolle [L?]:** Mit Gravitation ist das Maxwells Ringproblem (Saturnringe, 1859). Mit dominanter Zentralmasse ist der Ring nur für N ≥ 7 linear stabil (Moeckel 1994). Maxwells Grenze für großes N ist etwa M > 0,435 N³ m. Ein Code muss das reproduzieren, bevor er Neues behauptet.
  - **Gerechnet am 02.10. (Versuch V2):**
    - N = 3 bis 6 ist bei jedem Massenverhältnis instabil. Ab N = 7 ist der Ring stabil, solange m/M < c_N N⁻³ gilt.
    - c_N fällt von 2,45 (N = 7) auf 2,30 (N = 64) und nähert sich Maxwells 2,298, also M > 0,435 N³ m.
    - Das Abstract von Vanderbei/Kolemen (astro-ph/0606510) bestätigt die Grenze N ≥ 7 [S]. Die Zahl 0,435 bleibt [L?], ist jetzt aber nachgerechnet.

**Variante T („Tetraederkette“):** flächenverbundene Tetraederkette mit N_T Tetraedern, N_T + 3 Ecken und 3N_T + 3 Kanten. Das Tetra-Bündel vom 02.10. hat 9 bzw. 17 Tetraeder, also 12 bzw. 20 Ecken. Dort heißt das „11+1/19+1“.
- Zählregel für generische Ebenenschnitte: P = T3 + 2T4 + 2C, mit C = Zahl der Komponenten im Flächengraphen der geschnittenen Tetraeder.
  - Sie gilt unter Einbettungs- und Stapelbedingungen allgemein (Codex, 02.10.).
  - Die konvexe Doppelpyramide braucht man nur, um C mit der Zahl der Indexläufe gleichzusetzen.

Parameter: Ω, J, R, N, λ, g, Ruhegrößen, Phasenversätze, Kopplungsreichweite, Dämpfung, Störungen.

## 7. Stabilität

**Statische Lösungen:** Linearisierung δẍ = −K δx mit K = Hesse-Matrix der Energie. Eigenwerte μ_n > 0 bedeuten Schwingung (ω_n² = μ_n), μ_n < 0 Instabilität. Nullmoden entsprechen Symmetrien (Translation, Rotation, Phase).

**Rotierende Lösungen** (relative Gleichgewichte), im mitrotierenden System:

$$
\big(s^2 M+s\,G+K_{eff}\big)\,v=0,\qquad G=-G^T\ \text{(gyroskopisch, Coriolis)}
$$

- Stabil heißt: alle s rein imaginär und nicht entartet.
- Eine positive K_eff ist hinreichend, aber nicht nötig. Rotation kann stabilisieren, gyroskopische Stabilisierung.
  - Gerechnet (02.10., V3): Ein Federring mit gleichen Ruhelängen knickt schon in Ruhe ein, in der Ebene ab N = 10. Rotation stabilisiert ihn wieder, ab Ω ≈ 0,38 (N = 10) bis 0,89 (N = 32).
- Instabilitäten entstehen, wenn Moden mit entgegengesetzter Krein-Signatur zusammenstoßen.

**Phasenrotierende Moden** (Q-Ball-artig, Ψ = φ e^{iωt}): Man linearisiert im mitrotierenden Phasenbild. Die Stabilität gilt bei fester Ladung Q.
- Kriterium: Man zählt die negativen Richtungen des linearisierten Operators und nimmt das Vorzeichen von dQ/dω dazu (Grillakis-Shatah-Strauss-Typ [L?]).
- „dQ/dω < 0“ allein (Vakhitov-Kolokolov) reicht nur, wenn es genau eine negative Richtung gibt.
- Gerechnet (02.10., V5, diskretes Feld auf dem Ring-Graphen): Die kombinierte Regel traf an allen 3954 Punkten. Das reine dQ/dω < 0 wäre auf dem großen Zweig falsch gewesen.
- Dazu kommt die Krein-Signatur der Innenmoden.

**Zeitperiodische Lösungen**, die nicht auf ein stationäres Bild zurückführbar sind: Floquet-Multiplikatoren.

## 8. Gemeinsame Wirkung

$$
S=\int dt\left[\sum_i\frac{m_i}{2}|\dot x_i|^2+\sum_i|\dot\Psi_i|^2-E_{geo}(x)-E_{field}(x,\Psi)-E_{int}(x)\right],\qquad\delta S=0
$$

Die Normierung |Ψ̇_i|² ohne 1/2 passt zu §1 und §2.

Erhaltungsgrößen, wenn E die entsprechende Symmetrie hat:
- Energie (immer)
- Impuls und Drehimpuls (wenn E nur von Abständen abhängt)
- U(1)-Ladung Q (wenn E nur von |Ψ_i| und Ψ_i*Ψ_j abhängt)

Sie sind zugleich Kontrollen der Numerik und die Grundlage der Stabilitätsaussagen.

**Einheiten:** dimensionslos rechnen, mit m = 1, L_0 = 1, m_Feld = 1. Die Zahl der freien Parameter steht explizit dabei.

## 9. Teilchenartige Moden

Arbeitsdefinition: eine robuste, lokalisierte Mode, die Energie und eine Erhaltungsladung trägt, viele Perioden überlebt, Störungen toleriert und reproduzierbar wechselwirkt.

- Kontinuum: Ψ ≈ φ(x) e^{iωt}. Diskret: Ψ_i = A_i e^{i(ωt+θ_i)}.
- Lokalisierung über das Teilnahmeverhältnis

$$
PR=\frac{\big(\sum_i|\Psi_i|^2\big)^2}{\sum_i|\Psi_i|^4}\quad(\text{klein }=\text{ lokalisiert})
$$

- **Bekannte Physik [L?]:** Q-Bälle sind nichttopologische Solitonen (Coleman 1985). Diskrete Breather sind bekannt (Flach/Willis 1998, MacKay/Aubry 1994). Neu ist erst, was darüber hinausgeht.

### 9a. Brücke zum Projekt (neu)

Die „zwei Seiten“ lassen sich an einer bewiesenen Größe verbinden:

1. **Kontinuum:** Für V = S − S² + S³/2 ist die stille Stelle l = 0, n = 1 bei ω² = 0,797677, ρ = 1,744618 rechnergestützt bewiesen. Unter schwacher Eigengravitation verschiebt sie sich um etwa −0,47 × Kompaktheit (Projekt, Runden 14 und 15).
2. **Diskret [H]:** derselbe Q-Ball auf einem Gitter mit Abstand a. Das Gitter ändert die Dispersion (Band statt Kontinuum), damit Lage und Zahl der offenen Kanäle.
3. **Test:** Bis zu welchem a überlebt die stille Stelle? Wie wandert sie, Δω²(a)? Vorhersage und Scheiterregel werden vor dem Lauf festgelegt; Kontrolle ist a → 0.

Das wäre die erste Rechnung, die beide Seiten des Feldes an einer bewiesenen Zahl verbindet.

## 10. Frequenzen und Dimension

Normalmoden: ω_n² = μ_n (Eigenwerte aus §7).

Zwei Dimensionsbegriffe, getrennt messen:

- **Hausdorff- bzw. Wachstumsdimension** d_H aus der Ballgröße im Graphen: |B(r)| ∼ r^{d_H}.
- **Spektrale Dimension** d_s aus der Rückkehrwahrscheinlichkeit der Diffusion, P(t) ∼ t^{−d_s/2}, bzw. aus der Zustandsdichte ρ(ω) ∼ ω^{d_s−1} bei kleinem ω.

Gesucht, nicht vorausgesetzt: ν_tick = f(ω_n, N_I, d_I, E, d_s).

## 11. Dimensionswahrscheinlichkeiten der Schnitte

Zeitbasiert P(d = k) = T_{d=k}/T_total. Ereignisbasiert P(d = k) = N_{d=k}/Σ_j N_{d=j}. Gemeinsam P(d, ω, τ_I | N, Ω, J, …). Bei Sonden-Schnitten immer mit Angabe des Sondenmaßes.

## 12. Schnittstabilität

τ_k = t_death − t_birth und σ_I = (1/N_I) Σ_k τ_k/T_sim, dazu die Überlebensfunktion P(τ_I > τ). Gesucht ist eine robuste Trennung zwischen kurzlebigen Zufallsschnitten und langlebigen gebundenen Schnittstrukturen, immer gegen Nullmodelle (§18).

## 13. Korrelationen

C_{I,ν}(Δt) = ⟨δN_I(t) δν(t+Δt)⟩, C_{E,ν} = corr(E, ν_tick), C_{ω,ν} = corr(ω_dominant, ν_tick). Mehrfachvergleiche korrigieren. Korrelationen nur mit vorab festgelegter Hypothese werten.

## 14. „11+1“ und „19+1“ sauber testen

- N-Scan einheitlich N = 4 … 32, für beide Varianten R und T.
- Kennzahlen:

$$
Q(N)=\frac{\tau_{life}}{\tau_{rotation}},\qquad S(N)=\min_n\mu_n\ \ (\text{bzw. größter Realteil von }s),\qquad T(N)=\frac{N_{stabile\ Schnitte}}{N_{mögliche\ Schnitte}}
$$

- Positivkontrolle: Variante R mit Gravitation muss die Stabilitätsgrenze N ≥ 7 zeigen (§6). Am 02.10. bestanden (V2).
- **Erste Scans am 02.10.:** 11 und 19 waren nirgends besonders, weder im Federring (V3) noch im diskreten Feld auf dem Ring-Graphen (V5).
  - Eine scheinbare „11“ trat einmal auf. Es war die Schwelle J·N ≈ 0,55, ab der die Nabe keine Mode mehr hält, und sie wandert mit J: Das größte N ist 20, 15, 11, 9, 7 für J = 0,03 bis 0,08.
  - Genau so eine Parameterabhängigkeit muss man ausschließen, bevor man eine Zahl auszeichnet.
- Sonderrollen bestimmter N (Primzahlen, 11, 19) müssen aus dem Scan entstehen, nicht aus den Regeln. Vor dem Scan schriftlich festlegen, was als „außergewöhnlich“ gilt, etwa: S(N) liegt mehr als 3σ außerhalb des Verlaufs der Nachbarn.

## 15. Störungen und Chaos

x_i → x_i + ε_i, θ_i → θ_i + δ_i. Abstand zweier Trajektorien ‖δX(t)‖ ∼ e^{Λt}; Λ > 0 deutet auf Chaos. Lineare Instabilität (§7) und Chaos getrennt berichten. Bei Hamiltonschen Systemen lange Läufe und viele Seeds.

## 16. Messgrößen pro Lauf

| Größe | Bedeutung |
|---|---|
| N, Variante | Zahl der äußeren Elemente; R oder T |
| d_H, d_s | Wachstums- bzw. spektrale Dimension |
| Ω | Rotationsfrequenz |
| E(t), Q(t), L(t) | Energie, Ladung, Drehimpuls (Erhaltung als Kontrolle) |
| N_I(t), d_I | Schnittzahl, Schnittdimension (mit Sondenmaß) |
| ν_tick | Ereignisrate (event-lokalisiert) |
| ω_n, μ_n, s_n | Eigenfrequenzen, Eigenwerte, Stabilitätsexponenten |
| PR | Teilnahmeverhältnis (Lokalisierung) |
| τ_life | Lebensdauer der Mode |
| ΔE/E, ΔQ/Q | numerische Fehler |

Zusätzlich: Floquet-Multiplikatoren, Λ, Phasenkohärenz, Geburts- und Sterberate der Schnitte, Spektraldichte.

## 17. Laufplan

- **A – Positivkontrollen zuerst:**
  - Federtetraeder: ω² = (k/m){1,1,2,2,2,4} (Codex, 01.10.).
  - Maxwell-Ring: Grenze N ≥ 7.
  - Kontinuums-Q-Ball: bekannte stille Stelle.
- **B – Baseline:** Tetraeder → 6er → 8er → Varianten R und T, jeweils statisch, frei und rotierend.
- **C – N-Scan:** N = 4 … 32.
- **D – Parameter-Sweep:** Ω, J, R, λ, g, Ruhegrößen.
- **E – Störungen:** jede Kandidatenlösung mit vielen kleinen zufälligen Störungen.
- **F – Schnittanalyse:** event-lokalisierte Ticks, Persistenz, Spektrum, Stabilität.
- **G – Skalierung und Konvergenz:** N, Systemgröße, Δt, Glättungslänge ℓ.
- **H – Brücke (§9a):** stille Stelle auf dem Gitter, a → 0.

## 18. Kontrollen gegen Scheineffekte

- **Konvergenz:** Δt, Δt/2, Δt/4. Ticks über Ereignissuche, nicht über Schrittvergleich.
- **Erhaltung:** ΔE/E, ΔQ/Q, ΔL/L klein in konservativen Varianten.
- **Nullmodelle:** dieselbe Analyse auf zufälligen Geometrien gleicher Kanten- und Knotenzahl.
- **Positivkontrollen:** bekannte Antworten zuerst (§17 A).
- **Sondenabhängigkeit:** Ergebnisse von Sonden-Schnitten für mehrere Sondenmaße.
- **Einheiten:** dimensionslos; alle Terme verträglich.
- **Seeds:** viele Anfangsbedingungen. Ein Effekt aus einer einzigen handgewählten Konfiguration ist schwach.
- **Vorab festlegen:** je Lauf Vorhersage und Scheiterregel schriftlich vor dem Start. So arbeitet das Projekt; das schützt vor nachträglich passend gemachten Kriterien.

## 19. Status der Ideen

### Mathematisch etablierte Werkzeuge
Graphen/Zellkomplexe, diskrete Laplace-Operatoren, Variationsprinzip, transversale Dimensionszählung, Orientierungsdeterminanten, Eigenwert-, gyroskopische und Floquet-Analyse, Krein-Signatur, Lyapunov- und Störungstests, spektrale Dimension.

### Bekannte Physik, an die das anschließt [L?, an der Quelle prüfen]
- Q-Bälle und nichttopologische Solitonen; Q-Bälle in diesem sextischen Modell (Projekt; Battye/Sutcliffe 2000)
- diskrete Breather (MacKay/Aubry; Flach/Willis)
- Maxwells Ringproblem, relative Gleichgewichte im (N+1)-Körperproblem (Moeckel)
- Regge-Kalkül, Spinschäume, Quantum Graphity, spektrale Dimension in kausalen dynamischen Triangulationen

### Offene Modellhypothesen
- Schnitt-Ereignisse als fundamentale Ticks; Eigenzeit proportional zur Ereignisrate
- Teilchen als stabile Schnitt- bzw. Feldmoden
- besondere Stabilität bestimmter N+1-Strukturen
- Zusammenhang zwischen Dimension, Schnittwahrscheinlichkeit und Frequenz
- effektive Anziehung aus Kanten-, Flächen- und Volumenenergie

### Noch nicht gezeigt
- Reproduktion realer Elementarteilchen, bekannter Quantenzahlen, Massen oder Kopplungen
- Spin 1/2: im Projektmodell nicht möglich, weil der Konfigurationsraum zusammenziehbar ist (Projekt, geprüft). Topologische Modelle wie das Skyrme-Modell können es über die Finkelstein-Rubinstein-Bedingung [L?].
- emergente Lorentz-Invarianz; korrekter Einstein-Grenzfall
- fundamentale Auszeichnung von 11 oder 19
- Identität von Tickrate und physikalischer Zeit
- Entstehung von Raumzeit (in Variante A vorausgesetzt)

## 20. Minimaler Simulationskern

Zustand X = (x_i, ẋ_i, Ψ_i, Ψ̇_i), Dynamik Ẋ = F(X; Θ), Θ = (N, Variante, Ω, J, R, λ, g, k_E, k_F, k_V, L_0, β, ℓ, …). Symplektischer Integrator, z. B. Velocity-Verlet, wegen der Erhaltungsgrößen.

Pro Zeitschritt:

1. Geometrie und Feld fortschreiben.
2. Orientierungsdeterminanten χ aller relevanten Quadrupel auswerten (Nachbarlisten).
3. Bei Vorzeichenwechsel und bestandenem Innen-Test: Ereigniszeit per Nullstellensuche bestimmen und Tick protokollieren.
4. Energie, Ladung und Drehimpuls protokollieren.
5. Phasen- und Modendaten speichern.
6. Stabilitätsdiagnostik in festen Abständen: mitrotierende Linearisierung bzw. Floquet.

## 21. Kernfragen

1. Welche Schnitte sind physikalisch: Sonde oder intrinsisch?
2. Wie viele Schnittkomponenten können gleichzeitig stabil bestehen?
3. Welche Schnittdimensionen dominieren für welche Geometrien?
4. Gibt es charakteristische Ereignisfrequenzen? Sind sie unabhängig von Δt und Sonde?
5. Skalieren sie mit N, d_H oder d_s?
6. Erzeugen Kanten-, Flächen- und Volumenterme verschiedene Stabilitätsklassen?
7. Gibt es langlebige rotierende N+1-Moden, über die Maxwell-Grenze hinaus verstanden?
8. Sind 11+1 oder 19+1 gegenüber benachbarten N außergewöhnlich, nach vorab festgelegtem Maß?
9. Überleben Kandidaten zufällige Störungen?
10. Gibt es ein sinnvolles Kontinuumslimit, und überlebt die stille Stelle des Q-Balls die Diskretisierung (§9a)?

## 22. Kompakte Formelkarte

$$
\mathcal L=\partial_\mu\Phi^*\partial^\mu\Phi-V,\quad V=m^2s-\lambda s^2+gs^3,\quad \omega_{min}^2=m^2-\tfrac{\lambda^2}{4g}
$$

$$
\ddot\Psi_i+\sum_{j\sim i}J_{ij}(x)(\Psi_i-\Psi_j)+V'(|\Psi_i|^2)\Psi_i=0,\qquad Q=2\,\mathrm{Im}\sum_i\Psi_i^*\dot\Psi_i
$$

$$
I_S=\bigcap_{i\in S}M_i,\qquad \dim(A\cap B)=\dim A+\dim B-\dim X
$$

$$
\text{Tick: } \chi_{abcd}(t)=\det[x_b-x_a,x_c-x_a,x_d-x_a]\ \text{wechselt das Vorzeichen (mit Innen-Test)}
$$

$$
\nu=\lim_{T\to\infty}\frac{N_{events}(T)}{T},\qquad d\tau\propto\nu\,dt\ \ \text{[H]}
$$

$$
E_{geo}=\tfrac{k_E}{2}\sum(L-L_0)^2+\tfrac{k_F}{2}\sum(A-A_0)^2+\tfrac{k_V}{2}\sum(V-V_0)^2,\qquad F_i=-\nabla_iE
$$

$$
(s^2M+sG+K_{eff})v=0\ \ \text{(rotierend)},\qquad \omega_n^2=\mu_n\ \ \text{(statisch)}
$$

$$
S=\int dt\,(T-E),\qquad \delta S=0
$$

---

## Nächster konkreter Schritt

Ein reproduzierbarer, kleiner Benchmark, mit Vorhersagen vor jedem Lauf:

**Positivkontrollen (Federtetraeder, Maxwell-Ring, Q-Ball-Stelle) → Tetraeder → 6/8 → N-Scan für R und T → 11+1/19+1 im Vergleich zu den Nachbarn → event-lokalisierte Ticks → gyroskopische und Floquet-Stabilität → Störungen → Konvergenz.**

Parallel und als erste echte Brücke: die stille Stelle des Q-Balls auf dem Gitter (§9a).

Erst danach wird geprüft, ob robuste Strukturen Analogien zu bekannten physikalischen Systemen haben.
