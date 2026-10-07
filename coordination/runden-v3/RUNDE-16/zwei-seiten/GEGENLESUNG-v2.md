Urteil: vor der Weitergabe nachbessern. Die Kernformeln stimmen: §1-Lagrangedichte, Q mit Vorzeichen, Q-Ball-Fenster, §2-Gleichung aus §8 und §5, Fenster (1/3, 1) als J->0-Grenzfall, Maxwell-Zahlen.
Zu nachbessern sind vier Fehler (B1 diskretes Fenster "breiter", B2 Q-Ball-Stabilitaet "weil Q erhalten", B3 ω² = μ ohne Massenmatrix, B4 Schnittenergie aus Laengen und Flaechen) und eine schwere Ueberdehnung (U1 "11 und 19 nirgends besonders", obwohl Variante T nicht gerechnet ist). Dazu kommen Ungenauigkeiten und Markierungen.

# Gegenlesung ZWEI-SEITEN-DES-FELDES-v2.md (frischer Leser, Haus Anthropic)

- Beginn: 2026-10-02 08:58:51 CEST (per date)
- Ende: 2026-10-02 09:14:01 CEST (per date), Dauer also 15 min 10 s
- v2 waehrend der Pruefung unveraendert (sha256 um 09:14:01 erneut gleich)
- Gegenstand: coordination/runden-v3/RUNDE-16/zwei-seiten/ZWEI-SEITEN-DES-FELDES-v2.md,
  sha256 c574191eb1a1616b846ffece9ca2c853080aa2e0d5e4552a1454bcfb7431388e (Stand 08:55)
- Vergleich: v1-original.md (0edb86c3...), ausprobieren/ERGEBNIS.md (e651453c...),
  two-sides-review/codex/ARBEITSMODELL-V2.md (d2457db5...), ESSENZ-REVIEW.txt (2d4f5ab8...)
- Arbeitsweise: nur lesen; Rechnungen im Kopf, Rechenweg steht beim Befund; Literatur nur ueber
  die arXiv-API; v2 nicht geaendert. Der Autor formuliert, die Vorschlaege sind Anforderungen.

## 1 Vorwaertsdurchgang: Formeln

Zeilennummern beziehen sich auf v2 mit dem sha256 oben.

**B1. §2 Z. 81-85, Existenzfenster "diskret breiter als im Kontinuum". Art: Fehler.**
- Begruendung: Breiter ist das Fenster nur im Grenzfall J -> 0. Dort ist es (1/3, 1) mit Breite 2/3 gegen 1/2.
  - Bei J = 0,1 liegt [0,59; 0,92] ganz innerhalb von (0,5; 1). Das Fenster ist also schmaler, an beiden Enden.
  - Bei J = 0,05: Breite 0,96 - 0,475 = 0,485 < 0,5. Unten reicht es weiter, oben weniger weit.
  - ERGEBNIS.md sagt selbst nur "Das Fenster ist [1/3 + O(J), 1 - O(J)]". Das Wort "breiter" steht dort nicht.
  - Die angegebenen Oberkanten haengen von N ab: 0,945 bis 0,960 bzw. 0,885 bis 0,925 (ERGEBNIS Z. 148-149).
- Vorschlag: "Existenzfenster diskret verschoben: [1/3 + O(J), 1 - O(J)] (Rad-Graph, V5). Nur im Grenzfall J -> 0 ist es (1/3, 1) und damit breiter als (1/2, 1). Bei J = 0,1 ist es schmaler ([0,59; 0,885 bis 0,925] je nach N)."
- Den Satz Z. 85 ("erste messbare Bruecke") siehe U2.

**B2. §1 Z. 56, "Stabil sind sie gegen Zerfall, weil Q erhalten ist." Art: Fehler.**
- Begruendung: Dass Q erhalten bleibt, ist noetig, reicht aber nicht.
  - Gegen Zerfall in freie Quanten braucht es E < m·Q. In dieser Normierung hat eine ebene Welle Q = 2ω|A|²V und E = 2ω²|A|²V, also E/Q = ω >= m.
  - Klassisch stabil sind Q-Baelle nur bei einer negativen Richtung und dQ/dω < 0 (§7 von v2 selbst).
  - Am oberen Fensterrand ω -> m ist der 3D-Q-Ball mit anziehendem Quartikterm breit und flach (Dickwand-Grenzfall).
  - Kopfrechnung: Mit κ² = m² - ω² und f = κ F(κr)/√(2λ) wird die Gleichung zu ∇²F = F - F³, dem NLS-Grundzustand.
  - Dann ist Q = 2ω∫f² = (ω/(λκ))·∫F², also Q -> ∞ und dQ/dω > 0. Der Q-Ball ist dort instabil.
  - Diskret zeigt V5 genau das: "Instabil wird jeweils das obere Fensterende: reelles Paar, dQ/domega > 0" (ERGEBNIS Z. 151).
- Vorschlag: "Die Erhaltung von Q ist die Voraussetzung, nicht der Beweis. Stabil gegen Zerfall in freie Quanten heisst E < m·Q, klassisch stabil heisst dQ/dω < 0 bei genau einer negativen Richtung (§7). Nahe ω -> m sind die Q-Baelle instabil."

**B3. §7 Z. 200, §10 Z. 263, §22 Z. 424, "δẍ = -K δx, ω_n² = μ_n". Art: Fehler (Normierung).**
- Begruendung: Wegen |Ψ̇|² ohne 1/2 hat jede reelle Feldkomponente die Traegheit 2.
  - Beispiel: ein Knoten mit E = m²|Ψ|² und Ψ = q1 + i q2. Dann ist L = q̇1² + q̇2² - m²(q1² + q2²), also 2q̈ = -2m²q und ω² = m².
  - Die Hesse-Matrix in (q1, q2) hat aber den Eigenwert μ = 2m². Also gilt ω² = μ/2, nicht ω² = μ.
  - ω² = μ stimmt nur fuer die Orte bei m_i = 1 oder fuer die Wirtinger-Form ∂²E/∂Ψ*∂Ψ.
  - Im gekoppelten System (x, Ψ) braucht es das verallgemeinerte Problem K v = ω² M v mit M = diag(m_i, 2, 2). Codex schreibt das so (ARBEITSMODELL-V2 §8).
- Vorschlag: In §7 "M δẍ = -K δx, K v = ω² M v, M = diag(m_i fuer x; 2 fuer Re Ψ, Im Ψ)". In §10 und §22 "ω_n² = Eigenwerte von M⁻¹K". Fuer die rotierende Gleichung ist M in §7 schon richtig gesetzt, M ist nur zu erklaeren.

**B4. §5 Z. 158, "Eine Energie aus Punktzahlen, Laengen oder Flaechen von Schnittmengen ist stueckweise konstant oder springt. Ihr Gradient ist fast ueberall null, an Ereignissen unendlich." Art: Fehler.**
- Begruendung: Nur Punktzahlen (und Dimensionsindikatoren) sind stueckweise konstant.
  - Die Laenge der Schnittstrecke zweier Dreiecke und die Flaeche eines ebenen Schnitts durch einen Tetraeder aendern sich stetig mit den Orten. Ihr Gradient ist fast ueberall endlich und ungleich null.
  - An Ereignissen hat er bei Polyedern einen Knick, keine Unendlichkeit. Nur bei glatten Koerpern kann er an Beruehrpunkten unendlich werden, z. B. bei Kreisumfang 2π√(R² - d²) fuer d -> R.
  - Die Aenderungsliste Z. 14 sagt es richtig ("ueber Punktzahlen"). Haupttext und Liste widersprechen sich also. Codex §7 beschraenkt die Aussage ebenfalls auf die Punktzahl.
- Vorschlag: "Eine Energie aus Punktzahlen ist stueckweise konstant (Gradient fast ueberall null, Spruenge an Ereignissen). Laengen und Flaechen aendern sich stetig, ihr Gradient knickt aber an Ereignissen. Fuer glatte Kraefte daher Ersatzterme."

**B5. §2 Z. 74 und Z. 82, Vorzeichen von λ und Fenster (1/3, 1). Art: Ungenauigkeit.**
- Begruendung: Weich ist das Potential nur bei kleiner Amplitude.
  - Es gilt V'(S) < m² genau fuer S < 2λ/(3g). Im Projektmodell ist das 2/(3·0,5) = 4/3. Fuer S > 4/3 ist die Nichtlinearitaet hart.
  - Das Band ist diskret beschraenkt: ω² ∈ [m², m² + J·l_max], l_max = groesster Laplace-Eigenwert, beim Rad-Graphen N + 1.
  - Deshalb gibt es bei λ > 0 auch lokalisierte Moden oberhalb des Bandes. Grenzfall J -> 0: ein Knoten mit S > 4/3, ω² = V'(S) > 1.
  - Das Einknotenfenster ist also [1/3, 1) ∪ (1, ∞), nicht (1/3, 1).
  - V5 hat nur ω² <= 0,995 gerastert (ERGEBNIS Z. 145), der obere Ast ist ungeprueft. Im Kontinuum gibt es ihn nicht, weil das Band dort nach oben offen ist. Das ist ein echter Unterschied zwischen diskret und Kontinuum.
- Vorschlag: "Bei kleiner Amplitude entscheidet das Vorzeichen von λ ... Mit g > 0 wird V' fuer S > 2λ/(3g) hart. Dann gibt es zusaetzlich Moden oberhalb des Bandes (ω² > m² + J·l_max), in V5 nicht gerechnet."

**B6. §7 Z. 208, "Stabil heisst: alle s rein imaginaer und nicht entartet." Art: Ungenauigkeit.**
- Begruendung: Entartete, halbeinfache Eigenwerte sind stabil. Symmetrische Ringe haben solche Paare.
  - Relative Gleichgewichte haben in der Regel Nullmoden mit Jordan-Bloecken aus Drehung und Familie. V2 hat sie ausgeklammert (ERGEBNIS Z. 70-73).
  - Woertlich genommen waere kein relatives Gleichgewicht stabil.
- Vorschlag: "Spektral stabil: alle s auf der imaginaeren Achse, nach Abzug der Symmetrie-Nullmoden. Linear stabil: zusaetzlich halbeinfach (keine Jordan-Bloecke). Robust: zusammenfallende Eigenwerte haben gleiche Krein-Signatur."

**B7. §7 Z. 211, "Instabilitaeten entstehen, wenn Moden mit entgegengesetzter Krein-Signatur zusammenstossen." Art: Ungenauigkeit.**
- Begruendung: Das ist nur ein Weg, die Hamilton-Hopf-Instabilitaet. Der zweite Weg ist ein Paar, das durch null geht und reell wird.
  - Genau dieser Typ trat in V5 am oberen Fensterende auf ("reelles Paar", ERGEBNIS Z. 151).
  - Gegenlaeufige Signatur ist ausserdem nur noetig, nicht hinreichend.
- Vorschlag: "Instabil wird es, wenn ein Paar durch null geht (reelles Paar, so in V5) oder wenn Moden entgegengesetzter Krein-Signatur zusammenstossen (moeglich, nicht zwingend)."

**B8. §7 Z. 214-215, Kriterium und Vakhitov-Kolokolov. Art: Ungenauigkeit (gering). Die Kernaussage stimmt.**
- Begruendung: Gezaehlt werden die negativen Richtungen der Hesse-Form von H - ωQ, im mitrotierenden Bild K_u (ERGEBNIS Z. 156). "Des linearisierten Operators" ist mehrdeutig, der Evolutionsoperator hat keine negativen Richtungen in diesem Sinn.
  - Die Fallunterscheidung stimmt mit der Indextheorie: Bei n = 0 ist die Mode immer stabil, als Minimum von H - ωQ.
  - Bei n = 1 entscheidet dQ/dω < 0 allein.
  - Bei n >= 2 reicht dQ/dω nicht. V5 hatte bei n = 2 eine oszillatorische Instabilitaet (ERGEBNIS Z. 157).
  - Voraussetzung: Der Kern besteht nur aus der Phasensymmetrie.
- Vorschlag: "Man zaehlt die negativen Richtungen n der Hesse-Form von H - ωQ (K_u) ... VK allein entscheidet nur bei n = 1. Bei n = 0 ist die Mode unabhaengig von dQ/dω stabil, bei n >= 2 braucht man die Krein-Zaehlung." Vakhitov-Kolokolov ebenfalls mit [L?] markieren.

**B9. §8 Z. 230, "Energie (immer)". Art: Ungenauigkeit (nie/immer-Aussage).**
- Begruendung: Erhalten bleibt die Energie nur bei autonomer Lagrangefunktion ohne Daempfung und Antrieb.
  - §6 Z. 196 fuehrt selbst "Daempfung" als Parameter.
  - Ein vorgeschriebener Umlauf θ_j = 2πj/N + Ωt (Z. 181), kinematisch erzwungen, verletzt sie ebenfalls.
  - Codex §3: "bei autonomer, freier, geschlossener Dynamik".
- Vorschlag: "Energie (bei autonomer Dynamik ohne Daempfung, Antrieb und vorgeschriebene Bewegung)".

**B10. §4 Z. 13, 113, 119-131: Schrittweite, Chirotop, lokale Rate. Art: Ungenauigkeit.**
- (a) "Unabhaengig von der Schrittweite" gilt nur, solange je Schritt und Quadrupel hoechstens ein Vorzeichenwechsel faellt (ERGEBNIS Z. 257).
  - Bei Δt = 0,2 fehlen 6 der 1226 Ticks (Z. 125). Auch die Erkennung vergleicht zwei Schritte, erst danach folgt die Nullstellensuche.
  - Vorschlag: "unabhaengig von der Schrittweite, solange je Schritt hoechstens ein Wechsel je Quadrupel faellt (V4: bis Δt = 0,1; bei 0,2 fehlen 6 von 1226)".
- (b) Z. 120: Nicht jeder Chirotop-Wechsel ist ein Tick. Von 4254 Vorzeichenwechseln bestanden 1226 den Innen-Test (ERGEBNIS Z. 126).
  - Die [H]-Uhr zaehlt so etwas anderes als die Ticks.
  - Vorschlag: "Ticks sind die Chirotop-Wechsel mit bestandenem Innen-Test (V4: 1226 von 4254)."
- (c) Z. 124-137: ν ist als Langzeitmittel ueber alles definiert (T -> ∞). Die Hypothese verwendet aber ein ortsabhaengiges ν(x).
  - Mit dem definierten ν waere dτ = ν dt global, eine oertliche Gangabweichung (Bedingung 5) waere nicht messbar.
  - Vorschlag: ν(x) mit festem Messvolumen um x und endlichem Zeitfenster Δ definieren, wie Codex ν_Δ (§6), und Δ als Messaufloesung von Δt trennen.

**B11. §6 Z. 192-194, Zaehlregel P = T3 + 2T4 + 2C. Art: Ungenauigkeit.**
- Begruendung, Schreibtischrechnung mit Euler V - E + F = 1 je Scheibe:
  - Die Schnittpolygone (Dreiecke, Vierecke) einer Komponente bilden eine Scheibe. Innere Strecken sind geschnittene gemeinsame Flaechen.
  - Ist der Flaechengraph ein Baum, gilt E_innen = T3 + T4 - 1 und daraus P = 1 + 2T3 + 3T4 - E_innen = T3 + 2T4 + 2.
  - Die Regel braucht also (i) C = Komponenten des Graphen, dessen Kanten die geschnittenen gemeinsamen Flaechen sind, und (ii) einen Wald.
  - Bei einer geschlossenen Kette (§2 nennt "geschlossene N-Ketten") kann eine Komponente ein Ring sein. Dann gilt V - E + F = 0 und es fehlen 2 Punkte.
  - Bei nicht konvexer Doppelpyramide koennen zwei benachbarte Tetraeder geschnitten sein, ohne dass ihre gemeinsame Flaeche geschnitten ist. Dann ergeben sich 2 Komponenten statt 1.
  - "Allgemein" ist zu stark.
- Vorschlag: Bedingungen ausschreiben: "offene Kette (Wald), C ueber geschnittene gemeinsame Flaechen gezaehlt, generische Ebene. Bei geschlossener Kette: -2 je ringfoermiger Komponente."

**B12. §1 Z. 56, "fuer ein stabiles Vakuum Φ = 0 zusaetzlich λ² <= 4m²g". Art: Ungenauigkeit.**
- Begruendung: Lokal stabil ist Φ = 0 immer, denn V'(0) = m² > 0. Die Bedingung macht Φ = 0 zum globalen Minimum (V >= 0) und ω_min² >= 0.
  - Bei Gleichheit sind die Vakua entartet.
- Vorschlag: "fuer Φ = 0 als absolutes Minimum (V >= 0) zusaetzlich λ² <= 4m²g; bei λ² > 4m²g ist Φ = 0 nur metastabil".

**B13. §10 Z. 268, Zustandsdichte ρ(ω) ~ ω^(d_s - 1). Art: Ungenauigkeit.**
- Begruendung: Das gilt fuer masselose harmonische Moden mit ω² = Laplace-Eigenwert l, denn dann ist N(ω) ~ ω^(d_s).
  - Fuer das Feld mit Masse (ω² = m² + J·l) ist ρ unter m null. Man muss das Laplace-Spektrum nehmen: ρ(l) ~ l^(d_s/2 - 1).
  - ρ ist ausserdem in §9a anders belegt.
- Vorschlag: "bzw. aus der Zustandsdichte des Graph-Laplace-Operators, ρ(l) ~ l^(d_s/2 - 1) fuer kleine l".

**B14. Symbole (Aenderungsliste Z. 12 gegen Haupttext). Art: Ungenauigkeit.**
- Begruendung: Die Bereinigung ist unvollstaendig.
  - Q ist Ladung (§1, §2, §7) und Q(N) = τ_life/τ_rotation (§14).
  - S ist Wirkung (§8), Dichte S = |Φ|² im Projektmodell, Indexmenge I_S (§3) und S(N) (§14).
  - m ist Feldmasse und Knotenmasse (§6, §8), V ist Potential, Knotenmenge (§2) und Zellvolumen (§5).
  - C ist Zellmenge und Komponentenzahl (§6), T ist Zeit, Zaehler T3/T4, T(N) und kinetische Energie (§22).
  - Am gefaehrlichsten ist Q, weil §7 mit dQ/dω arbeitet.
- Vorschlag: Q(N), S(N), T(N) umbenennen (etwa q_life, s_max, f_stab) und die Feldmasse m_Φ schreiben.

## 2 Rueckwaertsdurchgang: Behauptungen, Zahlen, Literatur

**R1. §7 Z. 209-210, V3 als Beleg fuer gyroskopische Stabilisierung. Art: Ungenauigkeit (Beleg traegt die Zuordnung nicht).**
- Begruendung: ERGEBNIS Z. 181 nennt den Mechanismus "durch Zug statt Stauchung". Die Rotation vergroessert R und macht aus einem gestauchten Ring einen gespannten, aendert also K_eff selbst.
  - Gyroskopische Stabilisierung hiesse dagegen: K_eff behaelt negative Richtungen und G haelt die s trotzdem auf der Achse.
  - V3 hat weder K_eff noch Krein-Signaturen ausgegeben (ERGEBNIS Z. 256).
- Vorschlag: "Gerechnet (V3): ... Rotation stabilisiert ihn wieder, ab Ω ≈ 0,38 (N = 10) bis 0,89 (N = 32), nach ERGEBNIS durch Zug statt Stauchung. Ob dabei auch gyroskopische Stabilisierung mitwirkt, ist nicht geprueft." Den Beleg vom Satz "gyroskopische Stabilisierung" abruecken.

**R2. §6 Z. 187 und Z. 189, Maxwell-Ring. Art: Ungenauigkeit.**
- (a) "N = 3 bis 6 ist bei jedem Massenverhaeltnis instabil." Gerechnet ist nur das Raster m/M = 1e-9 bis 1e-1 mit 81 Punkten (ERGEBNIS Z. 52).
  - "Jedes" deckt nur die Literatur, und die ist [L?] bzw. vom Code-Agenten gelesen (R7).
  - Vorschlag: "im Raster m/M = 10⁻⁹ bis 10⁻¹ (81 Punkte) instabil; die Literatur sagt: fuer jedes."
- (b) "Die Zahl 0,435 ... ist jetzt aber nachgerechnet." Die Rechnung naehert sich nur: c_64 = 2,301, 2,301 - 2,298 = 0,003. Extrapoliert wurde nicht.
  - Kopfrechnung: 1/0,4352 ≈ 2,298, denn 0,4352 · 2,3 = 1,00096, also 2,3 - 0,00096/0,4352 ≈ 2,2978.
  - Vorschlag: "ist mit der Rechnung vertraeglich (c_N faellt monoton auf 2,301 bei N = 64)".

**R3. §7 Z. 216 und §14 Z. 294, "Ring-Graph"; §2 Z. 84 ohne Graph. Art: Ungenauigkeit.**
- Begruendung: V5 lief auf dem Rad-Graphen, also Ring plus Zentrum (ERGEBNIS Z. 139-142). Ein Ring-Graph ist ein Kreis ohne Nabe.
  - Gerade die Nabe ("+1") traegt den 11-Befund in §14.
- Vorschlag: ueberall "Rad-Graph (Ring aus N Knoten plus Zentrum, J auf allen Kanten gleich)". In §2 Z. 84 den Graphen und "Oberkante je nach N" ergaenzen.

**R4. §14 Z. 295, "Schwelle J·N ≈ 0,55". Art: Ungenauigkeit (gering).**
- Kopfrechnung aus den Paaren in derselben Zeile:
  - 0,03 · 20 = 0,60
  - 0,04 · 15 = 0,60
  - 0,05 · 11 = 0,55
  - 0,06 · 9 = 0,54
  - 0,08 · 7 = 0,56
- Die Spanne ist also 0,54 bis 0,60, wie in ERGEBNIS Z. 154. "≈ 0,55" greift gerade den Wert bei N = 11 heraus.
- Vorschlag: "die Schwelle J·N ≈ 0,54 bis 0,60".

**R5. §14 Z. 297, Beispielmass "S(N) liegt mehr als 3σ ausserhalb". Art: Ungenauigkeit (widerspricht der eigenen Quelle).**
- Begruendung: ERGEBNIS Z. 109 und Selbstanzeige 4 sagen dazu: "S ist als Kennzahl fuer diesen Test ungeeignet". Bei F0 war es Rauschen um 1e-8, bei F1 lagen die Treffer an Regimegrenzen.
  - Ausserdem trifft min_n μ_n ohne Abzug der Symmetrie-Nullmoden immer die triviale Null (Codex §8).
  - Die Ergaenzt-Zeile sagt, V1 bis V5 seien in §14 eingearbeitet. Dieser Befund fehlt dort.
- Vorschlag: "etwa: eine stetige Kennzahl (Q, PR, kleinste innere Frequenz; nach Abzug der Symmetriemoden) liegt mehr als 3σ ausserhalb der Nachbarn. Rauschboden und Regimegrenzen vorher ausschliessen. S(N) = max Re s war in V3 ungeeignet."

**R6. Kopf Z. 5 ("geprueft", "V1-V5"), §17 A und "Naechster Schritt" Z. 437. Art: Ungenauigkeit.**
- (a) Von V1 steht keine Zahl in v2: §17 nennt den Federtetraeder ohne "bestanden", obwohl V1 ihn auf 2·10⁻¹⁵ traf (ERGEBNIS Z. 11).
- (b) "Gepruefte Zahlen" ist zu stark. Es sind berichtete Zahlen aus je einem Laufsatz mit internen Gegenrechnungen, nicht unabhaengig nachgerechnet. V5b ist ausserdem nicht eingefroren (Selbstanzeige 3).
- (c) Der naechste Schritt beginnt mit Federtetraeder und Maxwell-Ring, die beide bestanden sind.
- Vorschlag:
  - Kopf: "berichtete Zahlen aus V1-V5 (ein Laufsatz, nicht unabhaengig nachgerechnet)".
  - §17 A: bei Federtetraeder und Maxwell-Ring "bestanden 02.10. (V1, V2)".
  - Naechster Schritt: mit Kontinuums-Q-Ball-Stelle, §9a und Variante T beginnen.

**R7. Literaturmarken. Art: Markierung.**
- **[S] ist nicht erklaert.** Die Statuszeile Z. 6 nennt nur [H] und [L?]. Vorschlag: "[S] = an der Quelle gelesen (mit Angabe, was gelesen wurde)".
- **Vanderbei/Kolemen [S], §6 Z. 189.**
  - Gelesen hat das Abstract der Code-Agent ueber die API (ERGEBNIS Z. 77), nicht die Leitung.
  - Meine eigene API-Abfrage um 09:07:08 bekam HTTP 429. Nach BRIEF habe ich abgebrochen und nichts wiederholt, das [S] konnte ich also nicht selbst bestaetigen.
  - Inhaltlich ist es nach meinem Gedaechtnis plausibel.
  - Vorschlag: "[S: Abstract, arXiv-API, Code-Agent 02.10.]".
- **Moeckel 1994 [L?].** Nach meinem Gedaechtnis plausibel: J. Dyn. Diff. Eq. 1994, "Linear stability of relative equilibria with a dominant mass".
  - Die Grenze N >= 7 wird nach meiner Erinnerung auch G. Roberts (2000) zugeschrieben [L?].
  - Marke richtig, vor Verwendung pruefen.
- **Vakhitov-Kolokolov, §7 Z. 215, ohne Marke.** Literatur aus dem Gedaechtnis, also [L?] setzen.
- **Battye/Sutcliffe 2000, §19 Z. 351.** Die Marke [L?] ist richtig.
  - Codex gibt aber an, die Quelle gelesen zu haben (hep-th/0003252v1, §2): dort halbe Kinetik und andere Faktoren. Selbst pruefen konnte ich das nicht.
  - "Q-Baelle in diesem sextischen Modell" stimmt dann nur nach Umrechnung.
  - Vorschlag: "in einem sextischen Modell dieser Familie (andere Normierung, Werte nur nach Umrechnung vergleichbar)".
- Uebrige Angaben sind richtig als [L?] markiert und nach meinem Gedaechtnis sachlich unauffaellig:
  - Coleman 1985
  - Flach/Willis 1998
  - MacKay/Aubry 1994
  - GSS
  - Finkelstein-Rubinstein
  - Maxwell 1859 mit 0,4352
  - Regge, Spinschaeume, Quantum Graphity, CDT

**R8. §1 Z. 58 und §9a Z. 255, Projektzahlen. Art: Ungenauigkeit / nicht pruefbar.**
- Begruendung, (a) Pruefbarkeit: Die Zahlen sind mit den freigegebenen Quellen nicht pruefbar und tragen keine Fundstelle. Gemeint sind ω² = 0,797677, ρ = 1,744618, "rechnergestuetzt bewiesen" und "-0,47 × Kompaktheit".
- (b) Widerspruch §1 gegen §9a: §1 nennt drei "bewiesene" stille Stellen, §9a nur die eine bei l = 0, n = 1.
- (c) ρ ist nirgends definiert und in §10 anders belegt.
- (d) "Atmungsmoden" passt nur zu l = 0. Bei l = 1 ist es eine Dipolmode.
- Pruefbar ist nur: ω² = 0,797677 liegt im Fenster (1/2, 1). Mit halber Kinetik waere das Fenster (1, 2) und die Zahl laege ausserhalb. Die Zahl passt also zur Normierung von §1.
- Vorschlag:
  - Je Zahl Datei oder Journal-ID angeben.
  - ρ definieren.
  - "Innenmoden ohne Abstrahlung (l = 0: Atmung; l = 1: Dipol)".
  - Klaeren, welche der drei als bewiesen gelten.

## 3 Ueberdehnung

**U1. §14 Z. 294, "11 und 19 waren nirgends besonders". Art: Ueberdehnung. Fuer die Weitergabe an Finn der wichtigste Punkt.**
- Begruendung: Gerechnet wurden nur Ringvarianten vom Typ R, naemlich der Federring N+1 (V3) und das Feld auf dem Rad-Graphen (V5).
  - Finns "11+1/19+1" aus dem Tetra-Buendel ist nach v2 selbst (§6 Z. 191) die Variante T, eine Tetraederkette mit 12 bzw. 20 Ecken. Sie ist nicht gerechnet.
  - Fuer V5 traegt die Aussage erst der Nachtrag v5b, und der entstand nach Sicht der Ergebnisse und ist nicht eingefroren (ERGEBNIS Selbstanzeige 3). Im vorab festgelegten V5-Test hatten 11 und 19 keine volle Nachbarschaft.
  - Bei V3 erwies sich die vorab gewaehlte Kennzahl S als ungeeignet (R5).
  - Ein anderes KI-System koennte daraus lesen, 11+1/19+1 sei geprueft und unauffaellig. Das deckt die Rechnung nicht.
- Vorschlag: "In den zwei gerechneten Ringvarianten (Federring V3, Feld auf dem Rad-Graphen V5) waren 11 und 19 unauffaellig. Fuer V5 gilt das nur im nachtraeglichen, nicht eingefrorenen Nachtrag v5b. Die Tetraederkette (Variante T), also Finns 11+1/19+1, ist noch nicht gerechnet."

**U2. §2 Z. 85, "Das ist eine erste messbare Bruecke zwischen den zwei Seiten des Feldes." Art: Ueberdehnung und innerer Widerspruch.**
- Begruendung, Widerspruch: §9a Z. 259 sagt, erst die Gitterrechnung zur stillen Stelle "waere die erste Rechnung, die beide Seiten ... verbindet". Ebenso Aenderungsliste Punkt 8 und "Naechster Schritt" Z. 439 ("als erste echte Bruecke").
- Begruendung, Quelle: ERGEBNIS Z. 188: "Kontinuumsfenster (1/2; 1): Es uebertraegt sich nicht auf ein grobes Gitter. Die Bruecke aus §9a ... bleibt der eigentliche Test und wurde hier nicht gerechnet."
- Begruendung, Mechanik: J -> 0 ist der Anti-Kontinuumsgrenzfall, das andere Ende. Das Kontinuum entspricht J ~ 1/a² -> ∞. V5 verbindet also nicht, sondern zeigt, dass das Kontinuumsfenster grob nicht gilt.
- Vorschlag: "V5 zeigt: Auf einem groben Gitter gilt das Kontinuumsfenster nicht, die Grenzen sind 1/3 + O(J) und 1 - O(J). Die Bruecke zum Kontinuum (a -> 0, §9a) ist nicht gerechnet."

**U3. §9a Z. 253, "Die 'zwei Seiten' lassen sich ... verbinden: 1. Kontinuum, 2. Diskret". Art: Ueberdehnung (Deutung als Tatsache).**
- Begruendung: v1 definiert die zwei Seiten nicht, das Wort steht nur im Titel (grep "Seite" in v1: nur Z. 1).
  - Die Leitung liest "Kontinuum gegen Diskret", Codex liest zwei Felder ψ und χ (ARBEITSMODELL-V2 §5: "χ ist kein Spiegelraum, sondern ein dynamischer Antwortkanal").
  - Beides sind Deutungen.
- Vorschlag: "Deutung der Leitung (Finn hat die zwei Seiten in v1 nicht definiert; Codex deutet sie als zwei Felder): ...". Finn fragen, was er meint.

**U4. Aenderungsliste Z. 18, "Fuer Dimensionsfragen gibt es zusaetzlich eine einbettungsfreie Variante." Art: Ueberdehnung.**
- Begruendung: Variante B ist in §2 Z. 64 nur benannt ("kein Ort, nur Graph").
  - Die Wirkung in §8 braucht x_i (ẋ_i, E_geo(x), J(|x_i - x_j|)). Fuer B gibt es weder Kopplung noch Dynamik der Geometrie.
  - Auf einem festen Graphen sind d_H und d_s Eingaben, keine Ergebnisse.
- Vorschlag: "ist als Variante B benannt, hat aber noch keine Dynamik. Auf festem Graphen sind d_H und d_s vorgegeben, nicht entstanden."

**U5. Aenderungsliste Z. 11, "Die Dynamik ist jetzt die echte Diskretisierung von §1". Art: Ueberdehnung (gering).**
- Begruendung: Eine Diskretisierung im eigentlichen Sinn ist das nur auf einem regelmaessigen Gitter mit J = 1/a² und Knotengewicht a³. Auf Tetraeder, Ring oder Rad ist es ein Graph-Modell mit demselben Potential.
  - Codex §2: "Abstandsabhaengige J,K sind eine zusaetzliche Modellannahme".
- Vorschlag: "diskreter Partner von §1 (gleiches Potential, Graph-Laplace statt ∇²). Diskretisierung im engeren Sinn nur auf regelmaessigem Gitter mit J = 1/a²."

**U6. §19 Z. 350-354, "Bekannte Physik, an die das anschliesst: Regge-Kalkuel, Spinschaeume, Quantum Graphity, spektrale Dimension in CDT". Art: Ueberdehnung (gering).**
- Begruendung: Diese Ansaetze behandeln die Geometrie selbst als dynamisch, ohne aeussere Zeit und Einbettung. v2 setzt beides voraus (Z. 26).
  - "Anschliessen" behauptet mehr als einen Vergleich von Messgroessen (d_s).
- Vorschlag: "Ansaetze mit Beruehrungspunkten (Bezug offen [H]); vergleichbar ist zunaechst nur die Messgroesse d_s".

**U7. §4 Z. 145-146, Bedingungen 4 und 5. Art: Ungenauigkeit / Ueberdehnung (gering).**
- (a) "Das Modell ist galileisch" gilt fuer das diskrete Modell aus §2 und §8. §1 ist lorentzinvariant. Vorschlag: "Das simulierte diskrete Modell ist galileisch."
- (b) "Erst eine Vorhersage dieser Art waere mit Uhrenmessungen vergleichbar". Dazu fehlt jede Zuordnung von ν, Energiedichte und Potential zu Messgroessen (kein G, kein c).
  - Vorschlag: "... waere ein erster Schritt; vergleichbar mit Uhrenmessungen wird sie erst mit einer Zuordnung der Groessen."

**U8. Probe aller nie/immer/nur-Aussagen gegen die Mechanik:**

| Stelle | Aussage | Ergebnis |
|---|---|---|
| Z. 13, 113 | Ticks unabhaengig von der Schrittweite | bedingt, B10 |
| Z. 26 | Raumzeit-Entstehung kann das Modell nicht zeigen | haelt (aeusseres t, R³) |
| Z. 56 | Q-Baelle stabil, weil Q erhalten | falsch, B2 |
| Z. 74 | Vorzeichen von λ entscheidet weich/hart | nur bei kleiner Amplitude, B5 |
| Z. 145 | Vergleich mit relativistischer Eigenzeit nicht moeglich | haelt fuer das diskrete Modell, U7 |
| Z. 158 | Gradient fast ueberall null | nur fuer Punktzahlen, B4 |
| Z. 185 | Ring nur fuer N >= 7 stabil | haelt im Rahmen (Literatur; Rechnung N = 3 bis 6 im Raster) |
| Z. 187 | bei jedem Massenverhaeltnis | nur im Raster, R2 |
| Z. 193 | Zaehlregel gilt allgemein | nur offene Kette/Wald, B11 |
| Z. 208 | stabil = rein imaginaer und nicht entartet | zu eng, B6 |
| Z. 211 | Instabilitaet durch Krein-Stoss | nur ein Weg, B7 |
| Z. 215 | VK reicht nur bei genau einer negativen Richtung | haelt, B8 |
| Z. 230 | Energie (immer) | nur autonom, B9 |
| Z. 294 | 11, 19 nirgends besonders | nur Variante R, U1 |
| Z. 365 | Spin 1/2 im Projektmodell nicht moeglich | haelt fuer das Projektmodell (Raum endlicher Feldenergie ist ein Vektorraum, also zusammenziehbar); fuer das Geometriemodell von v2 nicht geprueft |

## 4 Abgleich mit Codex' Fassung

Uebereinstimmend und beide richtig: Kinetik |∂Φ|² ohne 1/2, Q = 2 Im Σ ψ*ψ̇ mit Vorzeichen, Fenster m² - λ²/(4g) < ω² < m², Paarsumme jede Kante einmal und daraus dieselbe Feldgleichung.

| Nr. | Punkt | v2 | Codex | Wer hat recht |
|---|---|---|---|---|
| A1 | Eigenfrequenzen | ω² = μ, ohne Massenmatrix (§7, §10, §22) | H v = ω² M v, M = (m_i; 2; 2; 1) (§8) | Codex, siehe B3 |
| A2 | Energieerhaltung | "immer" (§8) | "bei autonomer, freier, geschlossener Dynamik" (§3) | Codex, siehe B9 |
| A3 | Tickrate | ν = N(T)/T, T -> ∞; Hypothese mit ν(x) | ν_Δ(t) mit Fenster Δ als Messaufloesung, Messvolumen noetig (§6) | Codex fuer eine oertliche Uhr; v2s Langzeitmittel ist als Kennzahl fuer V4 richtig, siehe B10c |
| A4 | Schnittenergie | Punktzahl, Laenge, Flaeche stueckweise konstant | nur die Punktzahl (§7) | Codex, siehe B4 |
| A5 | corr(E, ν_tick) | steht in §13 Z. 282, obwohl E erhalten ist (§8) | bei konstantem E undefiniert; lokale Energien oder Ensembles; N_I = 0 nicht teilen (§8) | Codex. Auch σ_I in §12 teilt durch N_I |
| A6 | Bedeutung von "11+1" | "Dort heisst das 11+1/19+1", also Tetraederkette mit 12/20 Ecken (§6 Z. 191) | "Die Bedeutung des urspruenglichen '+1' bleibt ungeklaert" (§1) | offen. Das Tetra-Buendel durfte ich nicht lesen. Codex' Vorsicht ist die sicherere Fassung, solange Finn die Zuordnung nicht bestaetigt hat |
| A7 | "zwei Seiten" | Kontinuum gegen Diskret (§9a) | zwei Felder ψ, χ (§5) | keiner belegt, beides Deutungen, siehe U3 |
| A8 | Kraft aus J(r) | "Anziehung entsteht, wenn sie entsteht" (§5 Z. 174) | abnehmendes J gibt bei festen Feldern einen abstossenden Beitrag (§3) | Codex. Nachgerechnet: F_i = -J'(r)·|Ψ_i - Ψ_j|²·(x_i - x_j)/r; mit J' < 0 zeigt F_i von j weg. v2 sollte den Gegenfall nennen: Anziehung nur ueber die Relaxation des Feldes |
| A9 | Battye/Sutcliffe | "in diesem sextischen Modell" [L?] | halbe Kinetik, Werte nur nach Umrechnung (§4, an der Quelle gelesen laut Codex) | Codex' Vorbehalt uebernehmen, siehe R7 |
| A10 | Rand bei stiller Stelle | §9a: Gitter, "Lage und Zahl der offenen Kanaele" | "Eine endliche Kette hat zunaechst kein raeumliches Strahlungskontinuum"; Idee 10: "endlicher Reflexionskasten reicht nicht" | Codex ergaenzt eine Bedingung, die v2 fehlt. Der Test in §9a braucht ein unendliches Gitter (Bloch-Rand) oder einen absorbierenden Rand |

**A11. Verwechslungsgefahr, kein Widerspruch.**
- Codex' Zweifeldkandidat U(S, χ) = ¼(χ² - 1)² + (1 + χ²)S - S² + S³/2 ist bei χ = ±1 nicht das Projektmodell.
  - Es ergibt sich U = 2S - S² + S³/2, also m² = 2, λ = 1, g = 1/2.
  - Damit ist ω_min² = 2 - 1/(4·½) = 3/2 und das Fenster (3/2, 2).
- Die Projektzahlen von v2 gelten dort nicht: ω² = 0,797677, (1/2, 1) und (1/3, 1). Codex sagt das selbst (§9: "die frueheren BIC- und Q-Ball-Beweise werden nicht darauf uebertragen").
- Codex' Zerlegung habe ich nachgerechnet, sie stimmt:
  - ¼(χ² - 1 + 2S)² = ¼(χ² - 1)² + S(χ² - 1) + S²
  - ½S(S - 2)² = ½S³ - 2S² + 2S
  - Summe = ¼(χ² - 1)² + (1 + χ²)S - S² + ½S³
- Da Finn mit beiden Fassungen weiterarbeitet, sollte v2 einen Satz dazu enthalten.

**A12. Kleine Unschaerfe bei Codex.**
- §4: "Fuer nichtnegatives V ist m² >= λ²/(4g) hinreichend." Die Bedingung ist auch noetig, denn V(s)/s = m² - λs + gs² hat das Minimum m² - λ²/(4g).
- v2 hat es hier richtig, abgesehen von B12.

## 5 Geprueft und in Ordnung

**§1, Feld:**
- Lagrangedichte ohne 1/2 und Feldgleichung ∂²Φ + V'(|Φ|²)Φ = 0: Euler-Lagrange nach Φ*.
- V'(s) = m² - 2λs + 3gs².
- Ladung: 2 Im ∫Φ*Φ̇ = i∫(Φ̇*Φ - Φ*Φ̇), und Φ = f e^{iωt} ergibt Q = 2ω∫f² > 0.
- Fenster: min V/s liegt bei s = λ/(2g) und ergibt m² - λ²/(2g) + λ²/(4g) = m² - λ²/(4g). Noetig ist λ > 0.
- Projektmodell: ω_min² = 1 - 1/(4·½) = 1/2. ω² = 0,797677 liegt im Fenster.

**§2, diskrete Seite:**
- Die Gleichung folgt aus §8 mit E_field aus §5, jedes Paar einmal: ∂/∂Ψ_i* von J|Ψ_i - Ψ_j|² = J(Ψ_i - Ψ_j). Mit Doppelsumme ueber geordnete Paare staende 2J.
- Diskrete Ladung: Noether mit p = Ψ̇*, δΨ = iαΨ.
- U(1)-Bedingung in §8.
- min V' = 1/3 bei S = 2/3: V'' = -2 + 3S = 0 und 1 - 4/3 + (3/2)(4/9) = 1/3. Allgemein m² - λ²/(3g).
- Kontrolle J = 1e-4 ergibt [0,334; 0,999].

**§3 und §4, Schnitte und Ticks:**
- Dimensionszaehlung. Ereignisse der Dimension -1: 0 + 2 - 3 und 1 + 1 - 3.
- χ_abcd ist das Sechsfache des orientierten Tetraedervolumens und null genau bei Koplanaritaet. Mit Innen-Test erfasst es beide Ereignisarten.
- V4-Zahlen:
  - 229 + 997 = 1226
  - 4·10⁻¹³ (Quelle <= 3,7e-13)
  - 13 % = 620/4675 bei Δt = 0,2
  - Verlust etwa proportional zu Δt: 13,3 %, 7,2 %, 3,9 %, 2,0 %, 1,1 %, 0,5 %
- Kritik am Grenzwert Δt -> 0 aus v1.

**§5, Energie:**
- E_geo mit Ruhegroessen.
- Kollaps bei positiven α.

**§6, Rotation und Ketten:**
- Kraeftebilanz bestimmt R(Ω). Nachgerechnet: Die Radialkomponente der Ringkraefte ist G m²/(4R² sin(πj/N)), das ergibt Ω² = 1 + (m/4M) Σ 1/sin(πj/N) wie in ERGEBNIS.
- 0,435 N³ ist gleichwertig mit c = 2,298.
- c_N von 2,45 (2,453) auf 2,30 (2,301).
- Variante T: N_T + 3 Ecken, 3N_T + 3 Kanten (Start 4/6, je Tetraeder +1/+3); 9 -> 12 und 17 -> 20.

**§7, Stabilitaet:**
- (s²M + sG + K_eff)v = 0 mit G = -G^T.
- Positives K_eff reicht: G leistet keine Arbeit, die Energie bleibt eine positive Form.
- VK-Aussage im Kern richtig (B8).
- 3954 Punkte, Fehlurteil von reinem dQ/dω auf dem grossen Zweig.
- V3-Zahlen 0,38 und 0,89; "in der Ebene ab N = 10".

**§8 bis §10:**
- §8: Normierungssatz.
- §9: Teilnahmeverhaeltnis.
- §10: d_H ueber Ballwachstum. d_s ueber Rueckkehrwahrscheinlichkeit, denn P(t) = ∫ρ(l) e^{-lt} dl ergibt P ~ t^(-d_s/2) bei ρ ~ l^(d_s/2 - 1).

**§14 und §17:**
- §14: N_max = 20, 15, 11, 9, 7. Positivkontrolle V2 bestanden.
- §17: Federtetraeder ω² = (k/m){1,1,2,2,2,4}. Atmung 4k/m, nachgerechnet ueber δL = u·√(8/3); Spur 12 = 6 Kanten × 2k.

**Rahmen:**
- Berichtigt-Zeile: Q ist jetzt in §1, §2 und §22 gleich und stimmt mit Codex.
- Leitidee und "Grenze dieses Modells" sind ehrlich formuliert: aeussere Zeit, Einbettung, Raumzeit nicht testbar.
- Spin-1/2-Aussage ist auf das Projektmodell begrenzt.
- §22 stimmt mit dem Haupttext. Ausnahmen: geerbtes B3, fehlendes "(transversal)" (unschaedlich) und ν statt ν(x) (B10c).

**Nicht geprueft (gesperrt oder nicht freigegeben):**
- Tetra-Buendel, Codex' Zaehlregel-Herleitung, Projektrunden 14/15 (stille Stellen, -0,47 × Kompaktheit) und Codex' Quellenlesung zu Battye/Sutcliffe.
- arXiv-API: HTTP 429 beim ersten Aufruf, abgebrochen.
