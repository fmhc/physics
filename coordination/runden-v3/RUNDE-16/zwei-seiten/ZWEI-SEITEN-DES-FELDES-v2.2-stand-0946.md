# Zwei Seiten des Feldes – Formeln und Arbeitsmodell (v2.2)

**Stand:** 2. Oktober 2026. v2 ab 08:12:49 CEST, v2.1 ab 09:16:54 CEST (claude-primary, auf Finns „review das mal … improve“).
**v2.1:** Alle Befunde der frischen Gegenlesung (GEGENLESUNG-v2.md, 32 Befunde, darunter 4 Fehler) sind eingearbeitet. Die geprüfte Fassung v2.0 liegt als ZWEI-SEITEN-DES-FELDES-v2.0-stand-0855.md daneben.
**v2.2** (ab 09:44:01 CEST):
- Eingearbeitet sind die Auflagen der zweiten frischen Gegenlesung (GEGENLESUNG-v2.1.md): N1 Anziehung, N2 Ereignissuche, N5 „+1“ offen.
- Dazu die Empfehlungen N3, N4 sowie N6 bis N16.
- Ergänzt sind die Ergebnisse von TETRAKETTE-1 (§14) und BEUTEL-1 (§1).
- v2.1 liegt als ZWEI-SEITEN-DES-FELDES-v2.1-stand-0919.md daneben.
- Nur die geänderten Sätze sind erneut zu lesen.

**Status:** Exploratives mathematisches Spielzeugmodell. Etablierte Mathematik wird mit unbestätigten Modellhypothesen kombiniert.
- **[H]** = Hypothese
- **[L?]** = Literatur aus dem Gedächtnis, vor Verwendung an der Quelle prüfen
- **[S]** = an der Quelle gelesen (mit Angabe, was gelesen wurde)
- Zahlen aus den Versuchen V1–V5 sind berichtete Zahlen aus einem Laufsatz mit internen Gegenrechnungen, nicht unabhängig nachgerechnet (ausprobieren/ERGEBNIS.md).

## Was sich gegenüber v1 geändert hat

1. **Feld:** kinetischer Term für komplexes Φ korrigiert. Existenzfenster der Q-Bälle und Erhaltungsladung ergänzt. Bezug zum Projektmodell (U = S − S² + S³/2) hergestellt.
2. **Diskrete Seite:** Die Dynamik ist jetzt der diskrete Partner von §1: gleiches Potential, Graph-Laplace statt ∇². Eine Diskretisierung im engeren Sinn ist das nur auf einem regelmäßigen Gitter mit J = 1/a². Die Kopplung kann von der Geometrie abhängen; das ist eine zusätzliche Modellannahme.
3. **Symbole:** In v1 stand λ für drei Dinge. Jetzt gilt:
   - λ, g: Feldkopplungen; m_Φ: Feldmasse; m_i: Knotenmassen
   - μ_n: Eigenwerte der Hesse-Matrix K (nicht ω_n²); Λ: Lyapunov-Exponent; 𝒮: Wirkung
   - Doppelt belegt, aus dem Zusammenhang klar: K (Zellkomplex / Hesse-Matrix), s (Dichte / Stabilitätsexponent), P (Punktzahl / Wahrscheinlichkeit), M (Zentralmasse in §6 / Massenmatrix in §7)
   - 𝒱, ℰ, ℱ, 𝒞: Knoten, Kanten, Flächen, Zellen; Vol_c: Zellvolumen
   - Kennzahlen in §14: q_life, s_max, f_stab
4. **Schnitte:** Es wird unterschieden zwischen *Sonden-Schnitten* (Beobachterebene, wie im Tetra-Bündel) und *intrinsischen* Schnitten (bewegte Teile untereinander). Ticks sind generische Ereignisse der Kodimension 1 in der Zeit. Erkannt werden sie über Vorzeichenwechsel von Orientierungsdeterminanten mit Innen-Test und Nullstellensuche. Das ist unabhängig von der Schrittweite, solange je Schritt und Quadrupel höchstens ein Wechsel fällt.
5. **Energie:** Mit positiven α kollabiert alles; deshalb jetzt Ruhelängen. Eine Schnittenergie aus Punktzahlen hat fast überall den Gradienten null; deshalb glatte Ersatzterme.
6. **Rotation und Stabilität:** relative Gleichgewichte aus der Kräftebilanz im mitrotierenden System. Stabilität mit Massenmatrix, gyroskopischem Term, Krein-Signatur und fester Ladung statt reiner Hesse-Matrix. Maxwells Ringproblem dient als Positivkontrolle.
7. **Namenskonflikt „11+1/19+1“:** Im ChatGPT-Rahmen ist es ein ebener Ring mit Zentrum, im Tetra-Bündel vom 02.10. eine Tetraederkette mit 12/20 Ecken. Beide Varianten sind getrennt benannt (R und T). Was „+1“ bedeutet, ist offen; das muss Finn klären.
8. **Neu:** ein Vorschlag für eine Brücke zum Projekt (§9a, noch nicht gerechnet). Getestet würde, ob die bewiesene stille Stelle des Q-Balls auf einem Gitter überlebt.
9. **Leitidee ehrlicher:** Zeit und 3D-Einbettung sind in diesem Modell vorausgesetzt; „→ Raumzeit“ ist hier nicht testbar. Eine einbettungsfreie Variante B ist benannt, hat aber noch keine Dynamik. Auf einem festen Graphen sind d_H und d_s vorgegeben, nicht entstanden.

## Leitidee

Geometrie → Feld → Schnitte → stabile Moden → teilchenartige Objekte → *(effektive Zeit- und Dimensionsgrößen)*

Ziel ist zu testen, ob aus einfachen lokalen geometrischen Regeln langlebige lokalisierte Moden, charakteristische Frequenzen, Schnitt-Ereignisse („Ticks“) und effektive Wechselwirkungen entstehen.

**Was „zwei Seiten“ heißt, ist offen.** v1 definiert es nicht; das Wort steht nur im Titel. Bisher liegen zwei Deutungen vor (Finn fragen):
- Leitung: Kontinuum gegen Diskret (diese Fassung).
- Codex: zwei Felder ψ und χ (RUNDE-16/two-sides-review/codex/ARBEITSMODELL-V2.md).

**Grenze dieses Modells:** Die Wirkung in §8 setzt eine äußere Zeit t und, in Variante A, Koordinaten x_i ∈ ℝ³ voraus. Ob Raumzeit *entsteht*, kann dieses Modell nicht zeigen. Prüfbar sind nur effektive Größen: Taktraten, spektrale Dimension und Wechselwirkungen.

## 1. Kontinuierliches Feld

Komplexes Skalarfeld, Signatur (+,−,−,−), mit s = |Φ|²:

$$
\mathcal L=\partial_\mu\Phi^*\,\partial^\mu\Phi-V(|\Phi|^2),\qquad V(s)=m_\Phi^2 s-\lambda s^2+g\,s^3
$$

Feldgleichung:

$$
\partial_\mu\partial^\mu\Phi+V'(|\Phi|^2)\,\Phi=0,\qquad V'(s)=m_\Phi^2-2\lambda s+3g s^2
$$

Erhaltene U(1)-Ladung (Noether):

$$
Q=2\,\mathrm{Im}\int d^3x\,\Phi^*\dot\Phi=i\int d^3x\,\big(\dot\Phi^*\Phi-\Phi^*\dot\Phi\big)
$$

(Für Φ = f e^{iωt} ist Q = 2ω∫f² d³x, also positiv für ω > 0.)

**Q-Bälle:** Φ = f(r) e^{iωt}. Sie existieren für

$$
\omega_{min}^2<\omega^2<m_\Phi^2,\qquad \omega_{min}^2=\min_s\frac{V(s)}{s}=m_\Phi^2-\frac{\lambda^2}{4g}
$$

- Nötig ist λ > 0.
- Damit Φ = 0 das absolute Minimum ist (V ≥ 0), muss zusätzlich λ² ≤ 4m_Φ²g gelten. Bei λ² > 4m_Φ²g ist Φ = 0 nur metastabil. Lokal stabil ist es immer, weil V'(0) = m_Φ² > 0.
- **Stabilität:** Dass Q erhalten ist, ist Voraussetzung, nicht Beweis.
  - Gegen Zerfall in freie Quanten stabil heißt E < m_Φ·Q. Eine ebene Welle hat E/Q = ω ≥ m_Φ.
  - Klassisch stabil heißt: genau eine negative Richtung und dQ/dω < 0 (§7) [L?].
  - Nahe ω → m_Φ (dicke Wand) ist der 3D-Q-Ball instabil, denn dort ist dQ/dω > 0.

**Projektmodell:** m_Φ² = 1, λ = 1, g = 1/2, also V = S − S² + S³/2 und ω_min² = 1/2.
- **Stille Stellen:** Innenmoden ohne Abstrahlung, bei l = 0 Atmung, bei l = 1 Dipol.
  - Ansatz Φ = e^{iωt}(f + a e^{iρt} + b e^{−iρt}); ρ ist die Frequenz der Innenmode im mitrotierenden Bild.
  - Rechnergestützt bewiesen sind l = 0, n = 1 bei ω² = 0,797677, ρ = 1,744618, sowie l = 0, n = 2 und l = 1, n = 1. Quelle: Projekt, Stand Gesamtformel in RUNDE-12.md, je in zwei Häusern gelesen.
  - Siehe §9a.
- **Nicht verwechseln mit Codex' Zweifeldfassung** U(S, χ) = ¼(χ² − 1)² + (1 + χ²)S − S² + S³/2:
  - Bei χ = ±1 ist U = 2S − S² + S³/2. Dann ist m_Φ² = 2, und bei festem χ liegt das Fenster bei (3/2, 2).
  - Antwortet χ (χ → 0 im Inneren), sinkt die untere Grenze auf ≈ 0,728. Das ist die Dünnwand-Schranke ohne die Gradientenkosten von χ.
  - BEUTEL-1 (02.10.) bestätigt: E/Q → 0,853 = √0,728. Der Ball baut sich ab Q ≈ 370 eine Hülle, bleibt aber ein Tropfen (E ~ Q).
  - Die Projektzahlen gelten dort nicht.

## 2. Diskrete Geometrie

Zellkomplex K = (𝒱, ℰ, ℱ, 𝒞) mit Knoten, Kanten, Flächen und Volumenzellen. Am Knoten i:

- Ort x_i (Variante A, eingebettet) bzw. kein Ort (Variante B, nur Graph; noch ohne Dynamik)
- komplexer Zustand Ψ_i(t) = A_i(t) e^{iθ_i(t)}

**Dynamik, diskreter Partner von §1** (gleiches Potential, Graph-Laplace statt ∇²):

$$
\ddot\Psi_i+\sum_{j\sim i}J_{ij}(x)\,(\Psi_i-\Psi_j)+V'(|\Psi_i|^2)\,\Psi_i=0
$$

- Die Kopplung kann von der Geometrie abhängen, z. B. J_ij = J(|x_i − x_j|). Erst dadurch wirken Feld und Geometrie aufeinander. Das ist eine zusätzliche Modellannahme.
- **Weich oder hart:** Bei kleiner Amplitude entscheidet das Vorzeichen von λ, ob die Nichtlinearität weich oder hart ist.
  - „Hart“ heißt hier: Die Frequenz liegt über dem linearen Wert, V'(S) > m_Φ². Mit g > 0 gilt das für S > 2λ/(3g), im Projektmodell S > 4/3. Die Steigung von V' wird schon ab S = λ/(3g) positiv.
  - Auf einem endlichen Graphen ist das Band ω² ∈ [m_Φ², m_Φ² + J·l_max] beschränkt; l_max ist der größte Laplace-Eigenwert.
  - Deshalb gibt es zusätzlich lokalisierte Moden oberhalb des Bandes. Sie wurden in V5 nicht gerechnet. Im Kontinuum gibt es sie nicht, weil das Band dort nach oben offen ist.
- Diskrete Ladung:

$$
Q=2\,\mathrm{Im}\sum_i\Psi_i^*\dot\Psi_i
$$

- **Existenzfenster auf dem Graphen** (V5, gerechnet am 02.10.):
  - Gerechnet auf dem Rad-Graphen: Ring aus N Knoten plus Zentrum, J auf allen Kanten gleich.
  - Im Grenzfall J → 0 sitzt die Mode auf einem Knoten. Dann gilt ω² = V'(S), und das Fenster unterhalb des Bandes ist (1/3, 1). Das Minimum von V' ist 1/3 bei S = 2/3; allgemein m_Φ² − λ²/(3g). Bei kleinem J ist es breiter als das Kontinuumsfenster (1/2, 1); bei der Kontrolle J = 10⁻⁴ ist es [0,334; 0,999].
  - Ab etwa J = 0,05 ist es schmaler: [0,475; 0,945 bis 0,960 je nach N], bei J = 0,1 [0,59; 0,885 bis 0,925].
  - Allgemein [1/3 + O(J), 1 − O(J)]: Auf einem groben Gitter gilt das Kontinuumsfenster nicht.
  - Die Brücke zum Kontinuum (a → 0, J = 1/a², §9a) ist nicht gerechnet.

Zu testen: Tetraeder, 6er, 8er, offene und geschlossene N-Ketten, die Varianten „Ring N+1“ (R) und „Tetraederkette“ (T) (§6), jeweils frei und rotierend.

## 3. Schnittmengen

Für eine Menge Σ von Objekten M_i:

$$
I_\Sigma=\bigcap_{i\in\Sigma}M_i,\qquad \dim(A\cap B)=\dim A+\dim B-\dim X\quad(\text{transversal})
$$

In 3D generisch: 2D ∩ 2D → 1D, 2D ∩ 1D → 0D, 1D ∩ 1D → leer.

**Welche M_i?** (in v1 offen) Innerhalb *eines* eingebetteten Zellkomplexes schneiden sich Zellen nur in gemeinsamen Teilzellen. Das ist reine Nachbarschaft, keine Dynamik. Sinnvoll sind zwei Arten:

- **Sonden-Schnitte:** Eine Beobachterebene oder -linie schneidet die Struktur, wie im Tetra-Bündel (Ebene ∩ Kanten). Das Ergebnis hängt von der Wahl der Sonde ab. Es ist eine Beobachtungsgröße, keine Eigenschaft des Systems.
- **Intrinsische Schnitte:** Bewegte Teile durchdringen einander. Das können verschiedene Komplexe sein, ein Komplex mit Selbstdurchdringung (nicht eingebettet) oder rotierende Kopien.

Zu messen: Schnittzahl N_I(t), Dimension d_I, Lebensdauer τ_I, Geburt und Vernichtung, räumliche Verteilung. Bei Sonden-Schnitten immer mit dem Sondenmaß, z. B. der Verteilung der Ebenennormalen.

## 4. Ticks aus Schnitt-Ereignissen

**Generische Ereignisse.** In einer zeitabhängigen Familie treten Schnitte mit erwarteter Dimension −1 nur zu einzelnen Zeitpunkten auf. In 3D sind das:

- Ecke durch Fläche (0 + 2 − 3 = −1)
- Kante durch Kante (1 + 1 − 3 = −1)

Ein Tick ist so ein Ereignis.

**Erkennung** über die Orientierungsdeterminante vierer Punkte:

$$
\chi_{abcd}(t)=\det\big[x_b-x_a,\;x_c-x_a,\;x_d-x_a\big]
$$

- Ein Vorzeichenwechsel von χ zwischen zwei Schritten wird gesucht. Dann wird der Zeitpunkt per Nullstellensuche verfeinert und der Innen-Test gemacht: Punkt in der Fläche bzw. Kreuzung innerhalb beider Kanten.
- Ticks sind die Wechsel mit bestandenem Innen-Test (V4: 1226 von 4254 Vorzeichenwechseln).
- **Schrittweite:** Das Ergebnis ist unabhängig von der Schrittweite, solange je Schritt und Quadrupel höchstens ein Wechsel fällt.
  - V4, gerechnet am 02.10. mit zwei sich durchdringenden Tetraedern: 1226 Ticks (229 Ecke-durch-Fläche, 997 Kante-durch-Kante) bei allen geprüften Δt von 0,1 bis 0,001, Ereigniszeiten auf 4·10⁻¹³ gleich. Bei Δt = 0,2 fehlen 6.
  - Die naive Zählung, die nur Schnittzustände zweier Schritte vergleicht, verliert Ereignisse etwa proportional zu Δt: 13 % bei Δt = 0,2.
- [H] Die Folge *aller* Vorzeichenwechsel, also die Wechsel des Chirotops der Punktmenge, ist eine kombinatorische Uhr. Sie zählt mehr als die Ticks.

**Raten.**
- Global, als Kennzahl eines ganzen Laufs: ν = N_events(T)/T für großes T.
- Örtlich, für eine Uhr: ν_Δ(x, t) = Zahl der Ereignisse in einem festen Messvolumen um x im Zeitfenster [t, t + Δ], geteilt durch Δ. Das Fenster Δ ist die Messauflösung und von Δt zu trennen (wie bei Codex).
- Ein Grenzwert Δt → 0 eines Zählers liefert nur Deltaspitzen.

**Hypothese [H]:**

$$
d\tau(x)\propto\nu_\Delta(x)\,dt
$$

Das ist keine etablierte Physik. Bedingungen, bevor man sie ernst nimmt:

1. ν hängt nicht an Δt (Konvergenz bei Δt, Δt/2, Δt/4).
2. ν ist robust gegen kleine Störungen.
3. Bei Sonden-Schnitten: ν hängt nicht an der Sonde, oder die Abhängigkeit ist verstanden.
4. Das simulierte diskrete Modell ist galileisch (§1 selbst ist lorentzinvariant). Ein Vergleich mit relativistischer Eigenzeit ist damit nicht möglich.
5. Prüfbar ist ein Analogon: Sinkt ν_Δ dort, wo die Energiedichte hoch ist, und mit welchem Exponenten? Das wäre ein erster Schritt. Mit Uhrenmessungen (gravitative Rotverschiebung) vergleichbar wird es erst, wenn die Größen zugeordnet sind, also Potential, G und c.

## 5. Energie der Geometrie

**v1 (lineare Spannungen):** E = α_E ΣL + α_F ΣA + α_V ΣVol kollabiert für positive α, denn alle Längen gehen gegen 0. Für negative α bläht es sich auf. Deshalb mit Ruhegrößen:

$$
E_{geo}=\frac{k_E}{2}\sum_{e}(L_e-L_0)^2+\frac{k_F}{2}\sum_{f}(A_f-A_0)^2+\frac{k_V}{2}\sum_{c}(\mathrm{Vol}_c-\mathrm{Vol}_0)^2
$$

Alternativ: lineare Spannung plus abstoßender Kern.

**Schnittenergie:**
- Punktzahl: Die Energie springt an Ereignissen, ihr Gradient ist fast überall null.
- Längen: Die Energie knickt, ihr Gradient springt.
- Flächen (ebene Schnitte durch Tetraeder): Der Gradient ist stetig, knickt aber an Ereignissen. Bei glatten Körpern kann er an Berührpunkten unendlich werden.
- Für glatte Kräfte daher Ersatzterme, z. B. eine weiche Überlapp- oder Abstandsfunktion:

$$
E_{int}=\sum_{(a,b)}\beta\,\sigma\!\big(d_{ab}/\ell\big)
$$

d_ab ist der vorzeichenbehaftete Abstand bzw. die Eindringtiefe, σ eine glatte Stufe, ℓ die Glättungslänge. Die Grenzfälle ℓ → 0 werden geprüft.

**Feld-Geometrie-Kopplung:**

$$
E_{field}=\sum_{\langle ij\rangle}J(|x_i-x_j|)\,|\Psi_i-\Psi_j|^2+\sum_i V(|\Psi_i|^2)
$$

Die Summe läuft über Paare ⟨ij⟩, jedes Paar einmal. Dann folgt aus §8 genau die Gleichung in §2.

**Kräfte** F_i = −∇_i E.
- Nimmt J(r) mit dem Abstand ab, ist der Beitrag zwischen zwei verbundenen Knoten für **jeden** Feldzustand abstoßend oder null.
  - Es gilt F_i = −J'(r)·|Ψ_i − Ψ_j|²·(x_i − x_j)/r; mit J' < 0 zeigt die Kraft von j weg.
  - Das gilt auch nach Relaxation des Feldes, denn dE_eff/dr = J'·|ΔΨ|² ≤ 0.
- Anziehung zwischen Knoten liefern in diesem Modell nur E_geo, E_int oder ein J mit J' > 0.
- Effektive Anziehung zwischen teilchenartigen Moden könnte höchstens indirekt entstehen, über Feldüberlapp zweier Moden oder über die Verformung der Geometrie [H]. Sie wird nicht eingesetzt.

## 6. Rotierende Systeme: zwei getrennt benannte Varianten

**Variante R („Ring N+1“):** N Punkte auf einem Kreis plus ein Zentrum.

$$
x_j(t)=R\,(\cos\theta_j,\sin\theta_j,0),\qquad \theta_j=\frac{2\pi j}{N}+\Omega t,\qquad x_{N+1}=0
$$

- Das ist nur dann eine Lösung (relatives Gleichgewicht), wenn die Kräftebilanz im mitrotierenden System erfüllt ist: m R Ω² = F_innen(R). Daraus folgt R(Ω); R ist nicht frei wählbar.
- **Positivkontrolle:** Mit Gravitation ist das Maxwells Ringproblem (Saturnringe, 1859).
  - Literatur: Mit dominanter Zentralmasse ist der Ring nur für N ≥ 7 linear stabil (Moeckel 1994 [L?]). Das Abstract von Vanderbei/Kolemen, astro-ph/0606510, sagt dasselbe [S: Abstract über die arXiv-API, vom Code-Agenten am 02.10. gelesen].
  - Maxwells Grenze für großes N: M > 0,435 N³ m [L?].
  - **Gerechnet am 02.10. (V2):**
    - N = 3 bis 6 war im Raster m/M = 10⁻⁹ bis 10⁻¹ (81 Punkte) instabil; die Literatur sagt: für jedes m/M.
    - Ab N = 7 ist der Ring stabil, solange m/M < c_N N⁻³.
    - c_N fällt monoton von 2,45 (N = 7) auf 2,301 (N = 64). Das ist mit Maxwells 1/0,4352 = 2,298 verträglich; extrapoliert wurde nicht.

**Variante T („Tetraederkette“):** flächenverbundene Tetraederkette mit N_T Tetraedern, N_T + 3 Ecken und 3N_T + 3 Kanten. Das Tetra-Bündel vom 02.10. hat 9 bzw. 17 Tetraeder, also 12 bzw. 20 Ecken; dort heißt das „11+1/19+1“. Was „+1“ bedeutet, ist offen.
- Zählregel für generische Ebenenschnitte: P = T3 + 2T4 + 2C.
  - Bedingungen: offene Kette und generische Ebene; C wird über die geschnittenen gemeinsamen Flächen gezählt.
  - Genauer ist C die Zahl der Komponenten des Graphen, dessen Knoten die geschnittenen Tetraeder und dessen Kanten die geschnittenen gemeinsamen Flächen sind. Dieser Graph muss ein Wald sein.
  - Bei einer geschlossenen Kette fehlen je ringförmiger Komponente 2 Punkte.
  - Codex' Herleitung (TETRA-RECON-1) kommt ohne lokale Konvexität aus, setzt aber Einbettungs- und Stapelbedingungen voraus.
  - Bilden je zwei benachbarte Tetraeder eine konvexe Doppelpyramide, gilt zusätzlich: C ist gleich der Zahl der Indexläufe.

Parameter: Ω, J, R, N, λ, g, Ruhegrößen, Phasenversätze, Kopplungsreichweite, Dämpfung, Störungen.

## 7. Stabilität

**Statische Lösungen:** Linearisierung M δẍ = −K δx. K ist die Hesse-Matrix der Energie, M die Massenmatrix: m_i für die Orte, 2 für Re Ψ_i und Im Ψ_i (wegen |Ψ̇|² ohne 1/2). Die Eigenfrequenzen folgen aus

$$
K v=\omega^2 M v
$$

Nach Abzug der Symmetrie-Nullmoden (Translation, Rotation, Phase) gilt: K positiv heißt stabil, eine negative Richtung heißt instabil.

**Rotierende Lösungen** (relative Gleichgewichte), im mitrotierenden System:

$$
\big(s^2 M+s\,G+K_{eff}\big)\,v=0,\qquad G=-G^T\ \text{(gyroskopisch, Coriolis)}
$$

- **Stabilitätsbegriffe:**
  - Spektral stabil: alle s auf der imaginären Achse, nach Abzug der Symmetrie-Nullmoden.
  - Linear stabil: zusätzlich halbeinfach, also keine Jordan-Blöcke.
  - Robust: Zusammenfallende Eigenwerte haben gleiche Krein-Signatur.
- Eine positive K_eff ist hinreichend, aber nicht nötig: Gyroskopische Stabilisierung ist möglich.
  - Gerechnet (02.10., V3): Ein Federring mit gleichen Ruhelängen knickt schon in Ruhe ein, in der Ebene ab N = 10.
  - Rotation stabilisiert ihn wieder, ab Ω ≈ 0,38 (N = 10) bis 0,89 (N = 32). Laut ERGEBNIS geschieht das durch Zug statt Stauchung: Die Rotation vergrößert R und ändert so K_eff selbst.
  - Ob dabei auch gyroskopische Stabilisierung mitwirkt, ist nicht geprüft.
- **Wege in die Instabilität:**
  - Ein Paar geht durch null und wird reell; so war es in V5 am oberen Fensterende.
  - Moden entgegengesetzter Krein-Signatur stoßen zusammen (Hamilton-Hopf). Das ist möglich, aber nicht zwingend.

**Phasenrotierende Moden** (Q-Ball-artig, Ψ = φ e^{iωt}): Man linearisiert im mitrotierenden Phasenbild. Die Stabilität gilt bei fester Ladung Q.
- Kriterium [L?, Grillakis-Shatah-Strauss]: Man zählt die negativen Richtungen n der Hesse-Form von H − ωQ; im mitrotierenden Bild ist das der Operator K_u.
  - n = 0: stabil, unabhängig von dQ/dω.
  - n = 1: dQ/dω < 0 entscheidet (Vakhitov-Kolokolov [L?]).
  - n ≥ 2: dQ/dω reicht nicht, man braucht die Krein-Zählung. V5 hatte bei n = 2 eine oszillatorische Instabilität.
  - Voraussetzung: Der Kern besteht nur aus der Phasensymmetrie.
- Gerechnet (02.10., V5, Rad-Graph):
  - Die Vorhersage „stabil genau bei n = 0 oder bei n = 1 mit dQ/dω < 0“ traf an allen 3954 Punkten. Die Punkte mit n = 2 waren instabil (oszillatorisch); allgemein ist n ≥ 2 nicht zwingend instabil.
  - Das reine dQ/dω < 0 wäre auf dem großen Zweig falsch gewesen.

**Zeitperiodische Lösungen**, die nicht auf ein stationäres Bild zurückführbar sind: Floquet-Multiplikatoren.

## 8. Gemeinsame Wirkung

$$
\mathcal S=\int dt\left[\sum_i\frac{m_i}{2}|\dot x_i|^2+\sum_i|\dot\Psi_i|^2-E_{geo}(x)-E_{field}(x,\Psi)-E_{int}(x)\right],\qquad\delta\mathcal S=0
$$

Die Normierung |Ψ̇_i|² ohne 1/2 passt zu §1 und §2. Sie gibt den Feldkomponenten die Trägheit 2 (§7).

Erhaltungsgrößen:
- Energie: bei autonomer Dynamik ohne Dämpfung, Antrieb und vorgeschriebener Bewegung.
- Impuls und Drehimpuls: wenn E zusätzlich nur von Abständen abhängt.
- U(1)-Ladung Q: wenn E nur von |Ψ_i| und Ψ_i*Ψ_j abhängt.

Sie sind zugleich Kontrollen der Numerik und die Grundlage der Stabilitätsaussagen.

**Einheiten:** dimensionslos rechnen, mit m_i = 1, L_0 = 1, m_Φ = 1. Die Zahl der freien Parameter steht explizit dabei.

## 9. Teilchenartige Moden

Arbeitsdefinition: eine robuste, lokalisierte Mode, die Energie und eine Erhaltungsladung trägt, viele Perioden überlebt, Störungen toleriert und reproduzierbar wechselwirkt.

- Kontinuum: Ψ ≈ φ(x) e^{iωt}. Diskret: Ψ_i = A_i e^{i(ωt+θ_i)}.
- Lokalisierung über das Teilnahmeverhältnis

$$
PR=\frac{\big(\sum_i|\Psi_i|^2\big)^2}{\sum_i|\Psi_i|^4}\quad(\text{klein }=\text{ lokalisiert})
$$

- **Bekannte Physik [L?]:** Q-Bälle sind nichttopologische Solitonen (Coleman 1985). Diskrete Breather sind bekannt (Flach/Willis 1998, MacKay/Aubry 1994). Neu ist erst, was darüber hinausgeht.

### 9a. Vorschlag: Brücke zum Projekt (nicht gerechnet)

Unter der Deutung „zwei Seiten = Kontinuum und Diskret“ ließen sich beide Seiten an einer bewiesenen Größe verbinden:

1. **Kontinuum:** Für V = S − S² + S³/2 ist die stille Stelle l = 0, n = 1 bei ω² = 0,797677, ρ = 1,744618 rechnergestützt bewiesen (§1).
   - Unter schwacher Eigengravitation verschiebt sie sich um etwa −0,47 × Kompaktheit (Projekt, RUNDE-14 und -15, Q-STERN-2 und -2b).
2. **Diskret [H]:** derselbe Q-Ball auf einem regelmäßigen Gitter mit Abstand a, J = 1/a². Das Gitter ändert die Dispersion (Band statt Kontinuum) und damit Lage und Zahl der offenen Kanäle.
3. **Test:** Bis zu welchem a überlebt die stille Stelle? Wie wandert sie, Δω²(a)?
   - Der Test braucht ein unendliches Gitter mit ausstrahlender (transparenter) Randbedingung, z. B. über die Gitter-Green-Funktion, oder eine absorbierende Schicht. Ein endlicher Kasten reflektiert und hat kein Strahlungskontinuum (Codex).
   - Scheiterregel vorab [H]:
     - Auf dem kubischen Gitter mit J = 1/a² ist das Band [1; 1 + 12/a²].
     - Der offene Kanal (ω + ρ)² ≈ 6,96 liegt nur für a ≤ 1,42 im Band. Bei gröberem Gitter ist die Stille trivial.
   - Vorhersage und Scheiterregel werden vor dem Lauf festgelegt; Kontrolle ist a → 0.

Das wäre die erste Rechnung, die beide Seiten an einer bewiesenen Zahl verbindet.

## 10. Frequenzen und Dimension

Normalmoden: ω_n² sind die Eigenwerte von M⁻¹K (§7).

Zwei Dimensionsbegriffe, getrennt messen:

- **Wachstumsdimension** d_H aus der Ballgröße im Graphen: |B(r)| ∼ r^{d_H}.
- **Spektrale Dimension** d_s aus der Rückkehrwahrscheinlichkeit der Diffusion, P(t) ∼ t^{−d_s/2}. Gleichwertig aus der Zustandsdichte D_L(l) des Graph-Laplace-Operators: D_L(l) ∼ l^{d_s/2−1} für kleine l.

Auf einem festen Graphen sind beide vorgegeben. Messgröße werden sie erst, wenn der Graph selbst entsteht oder sich ändert.

Gesucht, nicht vorausgesetzt: ν_tick = f(ω_n, N_I, d_I, Energie, d_s).

## 11. Dimensionswahrscheinlichkeiten der Schnitte

- Zeitbasiert: P(d = k) = T_{d=k}/T_total.
- Ereignisbasiert: P(d = k) = N_{d=k}/Σ_j N_{d=j}.
- Gemeinsam: P(d, ω, τ_I | N, Ω, J, …).
- Bei Sonden-Schnitten immer mit Angabe des Sondenmaßes.

## 12. Schnittstabilität

- τ_k = t_death − t_birth.
- σ_I = (1/N_I) Σ_k τ_k/T_sim; nur für N_I > 0 definiert.
- Dazu die Überlebensfunktion P(τ_I > τ).

Gesucht ist eine robuste Trennung zwischen kurzlebigen Zufallsschnitten und langlebigen gebundenen Schnittstrukturen, immer gegen Nullmodelle (§18).

## 13. Korrelationen

- C_{I,ν}(τ_v) = ⟨δN_I(t) δν_Δ(t+τ_v)⟩, mit eigener Verzögerung τ_v bei festem Fenster Δ.
- corr(Energie, ν) ist bei erhaltener Gesamtenergie nicht definiert. Stattdessen lokale Energien oder Ensembles über Anfangsbedingungen verwenden.
- C_{ω,ν} = corr(ω_dominant, ν) über Ensembles.

Mehrfachvergleiche korrigieren. Korrelationen nur mit vorab festgelegter Hypothese werten.

## 14. „11+1“ und „19+1“ sauber testen

- N-Scan einheitlich N = 4 … 32, für beide Varianten R und T.
- Kennzahlen. s_max nur nach Abzug der Symmetriemoden und nur als Stabilitätsanzeige, nicht für den 3σ-Test:

$$
q_{life}(N)=\frac{\tau_{life}}{\tau_{rotation}},\qquad s_{max}(N)=\max_n \mathrm{Re}\,s_n,\qquad f_{stab}(N)=\frac{N_{stabile\ Schnitte}}{N_{mögliche\ Schnitte}}
$$

- Positivkontrolle: Variante R mit Gravitation muss die Stabilitätsgrenze N ≥ 7 zeigen (§6). Am 02.10. bestanden (V2).
- **Erste Scans am 02.10., nur Variante R:**
  - In den zwei gerechneten Ringvarianten, dem Federring (V3) und dem Feld auf dem Rad-Graphen (V5), waren 11 und 19 unauffällig.
  - Für V5 gilt das nur im nachträglichen, nicht eingefrorenen Nachtrag v5b (N = 4 bis 26). Im vorab festgelegten Test hatten 11 und 19 keine volle Nachbarschaft.
  - Bei V3 war die vorab gewählte Kennzahl ungeeignet; sie lag im Rauschen bzw. an Regimegrenzen.
- **Variante T am 02.10. gerechnet** (TETRAKETTE-1):
  - Gerechnet wurde für 4 bis 33 Ecken (Ecken = N_T + 3). „11+1“ entspricht 12 Ecken, „19+1“ 20 Ecken.
  - In Federsteifigkeit, Feldklumpen, Lennard-Jones-Bindung und Schnittstatistik sind 12 und 20 Ecken nicht besonders.
  - 20 ist nirgends markiert. 12 ist nur zusammen mit dem ganzen Kurzkettenbereich 8 bis 14 markiert, wo die Enden dominieren; dort war das vorab gewählte Kriterium untauglich.
  - Besonders an der 12 ist die Geometrie: Die Helix dreht je Ecke um arccos(−2/3) = 131,81°.
    - 11 Schritte sind fast genau 4 Umläufe (9,9° Versatz). Bei 12 Ecken liegen also erstmals zwei Ecken fast auf derselben Seite.
    - Besser wird das erst bei 31 Ecken: 30 Schritte sind fast 11 Umläufe (5,7°).
  - Nachträglich beobachtet [H]: Die zwei tiefsten Biegeschwingungen fallen bei 9, 12 und 15/16 Ecken fast zusammen, also dort, wo neue Fast-Ausrichtungen hinzukommen.
  - Eine scheinbare „11“ trat einmal auf (V5). Es war die Schwelle J·N ≈ 0,54 bis 0,60, ab der die Nabe keine Mode mehr hält. Sie wandert mit J: Das größte N ist 20, 15, 11, 9, 7 für J = 0,03 bis 0,08. Genau so eine Parameterabhängigkeit muss man ausschließen, bevor man eine Zahl auszeichnet.
- Sonderrollen bestimmter N (Primzahlen, 11, 19) müssen aus dem Scan entstehen, nicht aus den Regeln. Vor dem Scan schriftlich festlegen, was als „außergewöhnlich“ gilt.
  - Zum Beispiel: Eine stetige Kennzahl (q_life, PR, kleinste innere Frequenz) liegt mehr als 3σ außerhalb des Verlaufs der Nachbarn.
  - Rauschboden und Regimegrenzen vorher ausschließen.

## 15. Störungen und Chaos

- Störungen: x_i → x_i + ε_i, θ_i → θ_i + δ_i.
- Der Abstand zweier Trajektorien wächst wie ‖δX(t)‖ ∼ e^{Λt}; Λ > 0 deutet auf Chaos.
- Lineare Instabilität (§7) und Chaos getrennt berichten.
- Bei Hamiltonschen Systemen lange Läufe und viele Seeds.

## 16. Messgrößen pro Lauf

| Größe | Bedeutung |
|---|---|
| N, Variante | Zahl der äußeren Elemente; R oder T |
| d_H, d_s | Wachstums- bzw. spektrale Dimension |
| Ω | Rotationsfrequenz |
| E(t), Q(t), L(t) | Energie, Ladung, Drehimpuls (Erhaltung als Kontrolle) |
| N_I(t), d_I | Schnittzahl, Schnittdimension (mit Sondenmaß) |
| ν, ν_Δ(x) | Ereignisrate global bzw. örtlich (ereignisgenau) |
| ω_n, μ_n, s_n | Eigenfrequenzen, Eigenwerte, Stabilitätsexponenten |
| PR | Teilnahmeverhältnis (Lokalisierung) |
| τ_life | Lebensdauer der Mode |
| ΔE/E, ΔQ/Q | numerische Fehler |

Zusätzlich: Floquet-Multiplikatoren, Λ, Phasenkohärenz, Geburts- und Sterberate der Schnitte, Spektraldichte.

## 17. Laufplan

- **A – Positivkontrollen:**
  - Federtetraeder ω² = (k/m){1,1,2,2,2,4}: bestanden am 02.10. (V1, auf 2·10⁻¹⁵).
  - Maxwell-Ring, Grenze N ≥ 7: bestanden am 02.10. (V2).
  - Kontinuums-Q-Ball, bekannte stille Stelle: offen.
- **B – Baseline:** Tetraeder → 6er → 8er → Varianten R und T, jeweils statisch, frei und rotierend.
- **C – N-Scan:** N = 4 … 32.
- **D – Parameter-Sweep:** Ω, J, R, λ, g, Ruhegrößen.
- **E – Störungen:** jede Kandidatenlösung mit vielen kleinen zufälligen Störungen.
- **F – Schnittanalyse:** ereignisgenaue Ticks, Persistenz, Spektrum, Stabilität.
- **G – Skalierung und Konvergenz:** N, Systemgröße, Δt, Glättungslänge ℓ.
- **H – Brücke (§9a):** stille Stelle auf dem Gitter, a → 0, mit ausstrahlendem oder absorbierendem Rand.

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

### Bekannte Physik als Bezug [L?, an der Quelle prüfen]
- Q-Bälle und nichttopologische Solitonen.
  - Q-Bälle in einem sextischen Modell dieser Familie bei Battye/Sutcliffe 2000. Dort ist die Normierung anders (halbe Kinetik); Werte sind nur nach Umrechnung vergleichbar [S: Codex, hep-th/0003252v1 §2].
- Diskrete Breather (MacKay/Aubry; Flach/Willis).
- Maxwells Ringproblem, relative Gleichgewichte im (N+1)-Körperproblem (Moeckel).
- Ansätze mit Berührungspunkten, Bezug offen [H]: Regge-Kalkül, Spinschäume, Quantum Graphity, spektrale Dimension in kausalen dynamischen Triangulationen. Dort ist die Geometrie selbst dynamisch und nicht eingebettet; die Rolle der Zeit unterscheidet sich je Ansatz [L?]. Vergleichbar ist zunächst nur die Messgröße d_s.

### Offene Modellhypothesen
- Schnitt-Ereignisse als fundamentale Ticks; Eigenzeit proportional zur örtlichen Ereignisrate
- Teilchen als stabile Schnitt- bzw. Feldmoden
- besondere Stabilität bestimmter N+1-Strukturen
- Zusammenhang zwischen Dimension, Schnittwahrscheinlichkeit und Frequenz
- effektive Anziehung aus Kanten-, Flächen- und Volumenenergie oder indirekt über Feldüberlapp und Verformung (nicht über J(r) mit J' < 0, das stößt ab)

### Noch nicht gezeigt
- Reproduktion realer Elementarteilchen, bekannter Quantenzahlen, Massen oder Kopplungen
- Spin 1/2: im Projektmodell nicht möglich, weil der Raum endlicher Feldenergie ein Vektorraum und damit zusammenziehbar ist (Projekt, geprüft). Für das Geometriemodell dieser Fassung ist es nicht geprüft. Topologische Modelle wie das Skyrme-Modell können es über die Finkelstein-Rubinstein-Bedingung [L?].
- emergente Lorentz-Invarianz; korrekter Einstein-Grenzfall
- fundamentale Auszeichnung von 11 oder 19. In Stabilitätsgrößen ist sie weder in R noch in T gefunden; in T gibt es nur die geometrische Ausrichtung (11 Schritte ≈ 4 Umläufe).
- Identität von Tickrate und physikalischer Zeit
- Entstehung von Raumzeit (in Variante A vorausgesetzt)

## 20. Minimaler Simulationskern

- Zustand X = (x_i, ẋ_i, Ψ_i, Ψ̇_i), Dynamik Ẋ = F(X; Θ).
- Parameter Θ = (N, Variante, Ω, J, R, λ, g, k_E, k_F, k_V, L_0, β, ℓ, …).
- Symplektischer Integrator, z. B. Velocity-Verlet, wegen der Erhaltungsgrößen.

Pro Zeitschritt:

1. Geometrie und Feld fortschreiben.
2. Orientierungsdeterminanten χ aller relevanten Quadrupel auswerten (Nachbarlisten).
3. Bei Vorzeichenwechsel: Ereigniszeit per Nullstellensuche bestimmen, Innen-Test machen und bei Erfolg den Tick protokollieren.
   - Doppelte Wechsel in einem Schritt sind am Vorzeichen allein nicht erkennbar.
   - Deshalb χ und dχ/dt an beiden Schrittenden auswerten und alle Nullstellen im Schritt suchen, oder Δt über eine Schranke für d²χ/dt² begrenzen.
   - Kontrolle immer durch Halbierung von Δt (§18).
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
8. Sind 11+1 oder 19+1 gegenüber benachbarten N außergewöhnlich, nach vorab festgelegtem Maß? Welche Form Finn meint, Kette T oder Ring R, ist offen. T ist am 02.10. gerechnet (§14).
9. Überleben Kandidaten zufällige Störungen?
10. Gibt es ein sinnvolles Kontinuumslimit, und überlebt die stille Stelle des Q-Balls die Diskretisierung (§9a)?

## 22. Kompakte Formelkarte

$$
\mathcal L=\partial_\mu\Phi^*\partial^\mu\Phi-V,\quad V=m_\Phi^2s-\lambda s^2+gs^3,\quad \omega_{min}^2=m_\Phi^2-\tfrac{\lambda^2}{4g},\quad Q=2\,\mathrm{Im}\!\int\!\Phi^*\dot\Phi
$$

$$
\ddot\Psi_i+\sum_{j\sim i}J_{ij}(x)(\Psi_i-\Psi_j)+V'(|\Psi_i|^2)\Psi_i=0,\qquad Q=2\,\mathrm{Im}\sum_i\Psi_i^*\dot\Psi_i
$$

$$
I_\Sigma=\bigcap_{i\in\Sigma}M_i,\qquad \dim(A\cap B)=\dim A+\dim B-\dim X\ \ (\text{transversal})
$$

$$
\text{Tick: } \chi_{abcd}(t)=\det[x_b-x_a,x_c-x_a,x_d-x_a]\ \text{wechselt das Vorzeichen, mit Innen-Test}
$$

$$
\nu=\frac{N_{events}(T)}{T}\ (\text{global}),\qquad \nu_\Delta(x)\ (\text{örtlich, Fenster }\Delta),\qquad d\tau\propto\nu_\Delta(x)\,dt\ \ \text{[H]}
$$

$$
E_{geo}=\tfrac{k_E}{2}\sum(L-L_0)^2+\tfrac{k_F}{2}\sum(A-A_0)^2+\tfrac{k_V}{2}\sum(\mathrm{Vol}-\mathrm{Vol}_0)^2,\qquad F_i=-\nabla_iE
$$

$$
K v=\omega^2 M v\ \ \text{(statisch; } M=\mathrm{diag}(m_i;\,2,2)\text{)},\qquad (s^2M+sG+K_{eff})v=0\ \ \text{(rotierend)}
$$

$$
\mathcal S=\int dt\,(E_{kin}-E),\qquad \delta\mathcal S=0
$$

---

## Nächster konkreter Schritt

Ein reproduzierbarer, kleiner Benchmark, mit Vorhersagen vor jedem Lauf:

**Kontinuums-Q-Ball-Stelle als dritte Positivkontrolle → N-Scan für R (Variante T ist am 02.10. gerechnet) → ereignisgenaue Ticks → gyroskopische und Floquet-Stabilität → Störungen → Konvergenz.**

Welche Form Finn mit 11+1/19+1 meint, ist offen.

Federtetraeder und Maxwell-Ring sind als Positivkontrollen bestanden (V1, V2).

Parallel, als erste echte Brücke: die stille Stelle des Q-Balls auf dem Gitter (§9a).

Erst danach wird geprüft, ob robuste Strukturen Analogien zu bekannten physikalischen Systemen haben.
