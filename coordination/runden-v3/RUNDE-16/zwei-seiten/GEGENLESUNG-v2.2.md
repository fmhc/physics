Urteil: mit einer Auflage weitergeben. G1: In §14/§19 fuer die 12 das formale Nichteintreffen der Vorhersage, die ungepruefte Endeffekt-Erklaerung und das fehlende faire Mass nennen. N1 bis N16: 14 erledigt, 2 teilweise (N12, N16). Alle nachgerechneten Zahlen stimmen; a ≤ 1,42 ist aufgerundet (genau 1,4192).

# Gegenlesung v2.2 von ZWEI-SEITEN-DES-FELDES-v2.md (nur geaenderte Saetze)

- Leser: frischer Gegenleser, Haus Anthropic (Claude), kannte die Texte vorher nicht
- Beginn (date): 2026-10-02 09:46:40 CEST
- Gegenstand: geaenderte Saetze laut DIFF-v2.1-v2.2.txt in ZWEI-SEITEN-DES-FELDES-v2.md
- Massstab: GEGENLESUNG-v2.1.md (N1 bis N16), Quellen tetrakette-1/ERGEBNIS.md, tetrakette-1/KARTE.md, beutel-1/ERGEBNIS.md
- Nicht gelesen: alles andere, insbesondere keine gesperrten Ordner

## 1. Statustabelle N1 bis N16

Gelesene Fassung v2.2: sha256 ce233a55...f2c06 (mtime 09:46:17). Zeilen beziehen sich darauf. Gelesen habe ich nur die Diff-Stellen mit ihrem Umfeld.

| Nr. | Kurz | Status | Neue Stelle in v2.2 | Bemerkung |
|---|---|---|---|---|
| N1 | Anziehung bei J' < 0 | erledigt | Z. 215-219, 463 | Physik und Vorzeichen stimmen (Abschnitt 2a). Kleine Randnotiz G8 |
| N2 | Ereignissuche | erledigt, mit Rest | Z. 483-486 | woertlich nach Vorschlag. Der zweite Weg (nur Schranke fuer d²χ/dt²) schliesst Doppelwechsel allein nicht aus, siehe G2 |
| N3 | Zeit in §19 | erledigt | Z. 456 | woertlich |
| N4 | Reihenfolge Naechster Schritt | erledigt | Z. 544 | Q-Ball-Kontrolle steht vorn, T als gerechnet ausgewiesen |
| N5 | "+1" offen, N fuer T | erledigt, kleiner Rest | Z. 31, 238, 385, 500, 546 | Festlegung auf T ist aufgehoben. Rest: Z. 372 "N = 4 ... 32 fuer R und T" passt nicht zu "4 bis 33 Ecken" (Z. 385); was N bei T ist, steht nicht da (G6) |
| N6 | Ableitungsordnung Schnittenergie | erledigt, neue Unschaerfe | Z. 29, 195-197 | Ordnung jetzt richtig. Der Satz zu glatten Koerpern haengt jetzt an "Flaechen", dort ist er schief (G5) |
| N7 | Symbole | erledigt | Z. 24-25 | μ_n richtig erklaert; Doppelbelegungen K, s, P, M genannt |
| N8 | Fenster; "hart" | erledigt | Z. 108, 119-120 | Rechnung nachvollzogen (2e). Den Wert bei J = 10⁻⁴ konnte ich nur plausibel machen, die Quelle war nicht freigegeben |
| N9 | V5-Regel und n = 2 | erledigt | Z. 282-284 | GSS-Logik stimmt; "n = 2 instabil (oszillatorisch)" konnte ich nicht an der Quelle pruefen |
| N10 | "zwei Deutungen" | erledigt | Z. 41 | |
| N11 | eigene Verzoegerung τ_v | erledigt | Z. 364 | |
| N12 | Rand, Scheiterregel, Bandgrund | teilweise | Z. 326-329, 433; Z. 109 unveraendert | Rand und Scheiterregel sind eingefuegt, die Zahlen stimmen (2f). Rundung und Bezeichnung siehe G3. Z. 109 "Auf einem endlichen Graphen ist das Band beschraenkt" ist unveraendert, obwohl §9a jetzt ein unendliches Gitter mit beschraenktem Band nennt (G7) |
| N13 | 0,728 und "laeuft" | erledigt | Z. 89-90 | Zahlen gegen BEUTEL-1 geprueft (2d). Der Zweig fehlt, siehe G4 |
| N14 | s_max nicht fuer 3σ | erledigt | Z. 373 | |
| N15 | geprueftes Δt | erledigt | Z. 161 | |
| N16 | Kleinigkeiten | erledigt bis auf einen Rest | Z. 244, 297, 453; Z. 270 unveraendert | Doppelpyramide, Grammatik und [S: Codex, hep-th/0003252v1 §2] sind gesetzt. Z. 270 "Die Rotation vergroessert R" steht weiter als ERGEBNIS-Aussage da; das ist gering, mechanisch passt es |

Quote: 14 von 16 erledigt, 2 teilweise (N12, N16), 0 nicht umgesetzt. Zaehlweg: N1-N11 sind 11, dazu N13, N14 und N15, also 14. N2, N5 und N6 zaehle ich als erledigt, weil ihr Kernpunkt umgesetzt ist; ihr Rest steht als G2, G6 und G5 unten.
Kopf Z. 6 "Dazu die Empfehlungen N3, N4 sowie N6 bis N16": fast richtig; N12 (Z. 109) und N16 (Z. 270) sind nur teilweise umgesetzt.

## 2. Neu eingefuegte Saetze gegen ihre Quellen

**2a. Kraft aus J(r), Z. 215-219: stimmt.**
- Aus E_field = Σ_⟨ij⟩ J(r_ij)|Ψ_i − Ψ_j|² folgt ∇_i r_ij = (x_i − x_j)/r_ij, also F_i = −J'(r)|ΔΨ|²(x_i − x_j)/r. Ein Faktor 2 entsteht nicht, weil jedes Paar einmal zaehlt.
- Bei J' < 0 ist −J'|ΔΨ|² ≥ 0, die Kraft zeigt von j weg. Das gilt fuer jeden Feldzustand.
- "Auch nach Relaxation" haelt sogar ohne Differenzierbarkeit: Fuer jedes feste Ψ faellt E(r, Ψ) in r nicht an. Das Minimum ueber Ψ (bei festem Q) solcher Funktionen faellt dann ebenfalls nicht an. dE_eff/dr = J'|ΔΨ*|² ≤ 0 ist der Einhuellendensatz dazu.
- "Nur E_geo, E_int oder J' > 0": haelt fuer die Wirkung in §8. Sie hat sonst nur konstante Massen und ein ortsfreies V.

**2b. Ereignissuche, Z. 483-486: richtig im Kern, zweiter Weg unvollstaendig (G2).**
- "Doppelte Wechsel sind am Vorzeichen allein nicht erkennbar": stimmt.
- Gegenfall zum zweiten Weg: χ(t) = c(t − t_a)(t − t_a − δ). Hier gilt |χ''| = 2|c| fuer jedes δ, die Schranke ist also fest. Fuer jedes Δt > δ haben beide Schrittenden dasselbe Vorzeichen. Eine Schranke fuer d²χ/dt² allein begrenzt Δt also nicht so, dass das Paar gefunden wird.
- Ausschliessen kann man den Doppelwechsel erst mit den Endwerten. Der Abstand zur linearen Interpolation ist hoechstens B·Δt²/8 (B = Schranke fuer |χ''|). Haben beide Enden dasselbe Vorzeichen und gilt min(|χ(t0)|, |χ(t1)|) > B·Δt²/8, liegt im Schritt keine Nullstelle.
- Der erste Weg (χ und dχ/dt an beiden Enden) faengt den Gegenfall: dχ/dt wechselt das Vorzeichen. Er sucht aber Nullstellen der Interpolante und ist ohne Fehlerschranke keine Garantie. Die Halbierungskontrolle in Z. 486 faengt den Rest als Δt-Abhaengigkeit der Zaehlung.

**2c. Tetraederkette, Z. 384-391, gegen TETRAKETTE-1 ERGEBNIS und KARTE**
- 131,81 Grad = arccos(−2/3): Es gilt cos 48,19° ≈ cos 48° − sin 48° · 0,003316 rad = 0,66913 − 0,74314 · 0,003316 = 0,66913 − 0,00246 = 0,66667, also 180° − 48,19° = 131,81°. Das stimmt mit dem ERGEBNIS (131,8103 Grad auf 1e-13).
- 11 Schritte ≈ 4 Umlaeufe, 9,9 Grad: 11 · 131,8103 = 1449,913, minus 1440 ergibt 9,913. Stimmt.
- "Erstmals": Die Versaetze fuer k = 1 bis 10 habe ich einzeln gerechnet (k·131,8103 zur naechsten vollen Drehung). Es ergeben sich 131,8 / 96,4 / 35,4 / 167,2 / 61,0 / 70,9 / 157,3 / 25,5 / 106,3 / 121,9. Das Minimum ist 25,5 bei k = 8. Also ist 12 Ecken (k bis 11) die erste Kette unter 25,5 Grad. Stimmt; v2.2 laesst nur das "vorher mindestens 25,5°" weg, darauf stuetzt sich aber das "erstmals".
- 30 Schritte ≈ 11 Umlaeufe, 5,7 Grad: 30 · 131,8103 = 3954,309, und 3960 − 3954,309 = 5,691. Stimmt. Kontrolle k = 19: 2504,396, 2520 − 2504,396 = 15,60, wie im ERGEBNIS. Dazwischen gibt es keinen besseren Wert, weil 4/11 und 11/30 aufeinanderfolgende Naeherungsbrueche sind. Den Kettenbruch [0; 2, 1, 2, 1, 2, ...] von 0,366139 habe ich bis zur fuenften Stelle nachgerechnet.
- 12 und 20 Ecken: Ecken = N_T + 3, also 9 und 17 Tetraeder. Kanten 3·9 + 3 = 30 und 3·17 + 3 = 54, das passt zu 3N − 6 in der KARTE. Stimmt.
- "4 bis 33 Ecken": stimmt (KARTE).
- "Kurzkettenbereich 8 bis 14": Das deckt sich woertlich mit ERGEBNIS Punkt 1. Die Tabellenzeilen sind aber ungleich: Bei K1-2 sind 8-12 markiert (13 und 14 nicht), bei K3 8-14 und 16, bei K4-2 9-16. Bei K2-3 ist nur N = 10 markiert. "Mit dem ganzen Bereich 8 bis 14" ist also eine Zusammenfassung, kein Befund je Groesse (G1).
- "nicht besonders" fuer 12: Das ERGEBNIS wertet "im Kern eingetroffen, formal nicht". K1-2 und K3 sind fuer 12 "nicht eingetroffen", und 12 ist in 4 von 7 Groessen markiert. "Wo die Enden dominieren" ist eine Deutung: Das faire Mass mit Endterm ~ 1/N ist "nicht gemacht" (Selbstanzeige). v2.2 nennt das Kriterium untauglich, laesst aber das formale Scheitern und die fehlende Pruefung weg (G1).
- Nachtraegliche Biegemoden-Spur [H]: 9, 12, 15/16 sowie die Verhaeltnisse 0,99 / 0,97 / 0,98 stimmen mit ERGEBNIS Punkt 3. Die Zuordnung mischt aber zwei Masse: k = 8 und 11 kommen aus "mod 360", k = 15 aus "mod 180". Probe: 15 · 131,8103 = 1977,155, und 1980 − 1977,155 = 2,85. Der mod-180-Sprung bei N = 5 (12,76) und der mod-360-Sprung bei N = 31 kommen in der Spur nicht vor. Die Verhaeltnisse bei den anderen N nennt die Quelle nicht. Fuer eine Helix mit fast drehsymmetrischem Querschnitt liegen die beiden tiefsten Biegemoden ohnehin nahe beisammen. Das [H] ist also noetig und richtig gesetzt (G9).

**2d. BEUTEL-1, Z. 89-90**
- 0,853 = √0,728: 0,853266² = 0,7225 + 2 · 0,85 · 0,003266 + 0,003266² = 0,7225 + 0,005552 + 0,000011 = 0,728063. Stimmt auf drei Stellen.
- Unabhaengig nachgerechnet bei χ = 0: U/S = 1/(4S) + 1 − S + S²/2 bei S = 1,1797 (ERGEBNIS: S(0) → 1,179653). 0,25/1,1797 = 0,21192 und 1,1797²/2 = 0,69584. Summe 0,21192 + 1 − 1,1797 + 0,69584 = 0,72806, Wurzel 0,85327. Das passt zu 0,853266. Stimmt.
- "Ab Q ≈ 370": ERGEBNIS "chi(0) = 0,098 bei Q = 372", also χ(0) < 0,1. Die Zahl stimmt. Es ist aber eine Schwelle von 0,1 auf einem stetigen Uebergang: h steigt von 0,026 an der Faltung, "Hysterese wurde nicht gesehen". Ausserdem gilt sie nur auf dem Duennwand-Ast. Am Dickwand-Ende hat χ(0) = 0,960 bei Q = 144, und in 3D waechst Q dort ebenfalls ohne Grenze (ERGEBNIS §5, B3). Siehe G4.
- "Tropfen (E ~ Q)": ERGEBNIS: p zwischen 0,896 und 0,998, kein Punkt im Band 0,70 bis 0,80. Stimmt.

**2e. "Hart" und Fenster, Z. 108, 119-120**
- V' = m² − 2λS + 3gS². V' > m² heisst S(3gS − 2λ) > 0, also S > 2λ/(3g). Mit λ = 1, g = 1/2 ist das 2/1,5 = 4/3. V'' = −2λ + 6gS > 0 ab S = λ/(3g) = 2/3. Stimmt.
- Bei J = 10⁻⁴ ist das Fenster [0,334; 0,999]. Die Breite ist 0,665 und damit groesser als 0,5. Bei J = 0,05 ist die Breite 0,470 bis 0,485 und damit kleiner als 0,5. Die Rechnung stimmt.
- Den Wert habe ich nicht an der Quelle geprueft, ausprobieren/ERGEBNIS.md war nicht freigegeben. Plausibel ist er: Am Ringknoten mit Grad 3 verschiebt sich die Unterkante um etwa 3J = 3·10⁻⁴, also 0,3333 + 0,0003 ≈ 0,334.

**2f. Scheiterregel, Z. 327-329**
- Band: Der kubische Laplace hat Eigenwerte Σ_d (2 − 2cos k_d)/a², von 0 bis 12/a². Mit m² = 1 ist das Band [1; 1 + 12/a²]. Stimmt.
- ω = √0,797677 ≈ 0,893128, denn 0,89313² = 0,797681. ω + ρ = 0,893128 + 1,744618 = 2,637746. Das Quadrat ist 6,76 + 2 · 2,6 · 0,037746 + 0,037746² = 6,76 + 0,196279 + 0,001425 = 6,957704 ≈ 6,96. Stimmt.
- Grenze: 12/a² ≥ 5,957704 heisst a² ≤ 2,01420, also a ≤ 1,4192 (1,4192² = 2,01413). "a ≤ 1,42" ist aufgerundet. Bei a = 1,42 ist 12/2,0164 = 5,9512 < 5,9577, der Kanal ist dort schon zu. Die Richtung "nur fuer" bleibt wahr, nur die Grenze ist um 0,001 zu weit (G3).
- Der Kanal ω − ρ: (0,8515)² = 0,725 < 1 ist zu. Es bleibt also bei einem offenen Kanal erster Ordnung, wie im Text.

## 3. Neue Ueberdehnungen (nie/immer/nur/alle)

Geprueft sind nur die geaenderten Saetze.

| Z. | Aussage | Ergebnis |
|---|---|---|
| 6 | Empfehlungen "N6 bis N16" eingearbeitet | fast; N12 und N16 nur teilweise |
| 90 | "baut sich ab Q ≈ 370 eine Huelle" (gilt so fuer alle Baelle ab Q 370) | nur auf dem Duennwand-Ast und nur als Schwelle χ(0) < 0,1 (G4) |
| 108 | V' > m² fuer alle S > 2λ/(3g) | haelt fuer S > 0, g > 0 |
| 119 | "bei kleinem J breiter" | belegt nur fuer J → 0 und J = 10⁻⁴; zwischen 10⁻⁴ und 0,05 offen. Gering, kein Befund |
| 161 | "bei allen geprueften Δt" | haelt |
| 195 | Gradient "fast ueberall null" | haelt |
| 197 | glatte Koerper: Gradient "kann unendlich werden", jetzt unter "Flaechen" | schief (G5) |
| 215 | "fuer jeden Feldzustand abstossend oder null" | haelt (2a) |
| 217 | "auch nach Relaxation" | haelt, sogar ohne Differenzierbarkeit (2a) |
| 218 | Anziehung "nur" aus E_geo, E_int oder J' > 0 | haelt fuer J = J(abs(x_i − x_j)) wie in §5; §2 laesst allgemeines J_ij(x) zu (G8) |
| 219 | "hoechstens indirekt", ueber Feldueberlapp oder Verformung [H] | haelt, wenn man "Feldueberlapp" weit liest als jede Wirkung ueber Ψ, auch abgestrahlte Wellen. Das Modell hat nur Ψ und x als Traeger |
| 283 | "an allen 3954 Punkten" | Quellwert, fuer mich nicht pruefbar; logisch passt er zum Schema in Z. 278-281 |
| 283 | "n ≥ 2 nicht zwingend instabil" | haelt: Bei n − p gerade schliesst die Zaehlung Krein-Stabilitaet nicht aus |
| 328 | "liegt nur fuer a ≤ 1,42 im Band" | Die Richtung haelt, die Grenze ist aufgerundet (genau 1,4192) und mit Kontinuumswerten von ω und ρ gerechnet (G3) |
| 329 | "bei groeberem Gitter ist die Stille trivial" | haelt unter derselben Annahme (G3) |
| 386 | "sind 12 und 20 Ecken nicht besonders" | fuer 20 haelt es; fuer 12 ist es eine Deutung nach formal nicht eingetroffener Vorhersage (G1) |
| 387 | "20 ist nirgends markiert" | haelt (ERGEBNIS Punkt 1) |
| 387 | "12 nur zusammen mit dem ganzen Kurzkettenbereich 8 bis 14" | "nur zusammen" haelt. "Ganzer Bereich 8 bis 14" stimmt je Groesse nicht genau (2c, G1) |
| 389 | "erstmals" | haelt (2c), der Beleg 25,5 Grad fehlt im Text |
| 390 | "erst bei 31" | haelt (2c) |
| 391 | "also dort, wo neue Fast-Ausrichtungen hinzukommen" | Die Auswahl ist nicht vollstaendig (N = 5, 31) und mischt zwei Masse; das [H] ist gesetzt (G9) |
| 463 | "nicht ueber J(r) mit J' < 0, das stoesst ab" | haelt |
| 469 | "weder in R noch in T gefunden; in T gibt es nur die geometrische Ausrichtung" | "Nur" uebergeht die eigene [H]-Spur aus Z. 391. "Nicht gefunden" haengt bei T an G1. R habe ich nicht geprueft (G10) |
| 484 | "am Vorzeichen allein nicht erkennbar" | haelt |
| 485 | "alle Nullstellen im Schritt suchen" | ohne Fehlerschranke keine Garantie; der zweite Weg reicht allein nicht (G2) |
| 500, 546 | "ist offen" | haelt |

## 4. Neue Befunde

Reihenfolge nach Gewicht fuer die Weitergabe. Die Vorschlaege sind Anforderungen, den Wortlaut waehlt der Autor.

**G1. §14 Z. 386-387 (und §19 Z. 469): "12 und 20 Ecken nicht besonders". Art: Ueberdehnung, mittel fuer die Weitergabe. Neu in v2.2.**
- Quelle: Die Gesamtvorhersage ist "im Kern eingetroffen, formal nicht". K1-2 und K3 sind fuer 12 "nicht eingetroffen", und 12 ist in 4 von 7 Groessen markiert.
- "Wo die Enden dominieren" ist eine Erklaerung, die nicht geprueft wurde. Das faire Mass (Nachbarvergleich nach Abzug eines Endterms ~ 1/N) ist laut Selbstanzeige "nicht gemacht".
- Je Groesse sind die markierten Bereiche verschieden: 8-12 (K1-2), 8-14 und 16 (K3), 9-16 (K4-2), nur 10 (K2-3). "Mit dem ganzen Kurzkettenbereich 8 bis 14" ist also die Kurzfassung des ERGEBNIS.
- Fuer 12 stuetzt die Quelle die Deutung teilweise. In K1-2 ist 12 mit z = +4,7 schwaecher markiert als 9 (+13,9) und 11 (−9,0). Fuer K3 und K4-2 nennt die Quelle keine z-Werte.
- Folge: Ein Leser liest "fuer 12 gemessen: nicht besonders". Belegt ist nur, dass das vorab festgelegte Mass 12 nicht von den kurzen Nachbarn trennen kann.
- Anforderung: Fuer 20 kann die Aussage bleiben. Fuer 12 muessen drei Dinge sichtbar sein: die formal nicht eingetroffene Vorhersage, die nicht gepruefte Endeffekt-Erklaerung und das noch fehlende faire Mass. In §19 Z. 469 entsprechend.

**G2. §20 Z. 485: zweiter Weg der Ereignissuche. Art: Ungenauigkeit (Rechenanweisung), gering bis mittel. Rest von N2, der Wortlaut stammt aus dem N2-Vorschlag.**
- Gegenfall aus 2b: Bei χ = c(t − t_a)(t − t_a − δ) ist |χ''| fest, und jedes Δt > δ verliert das Paar. Eine Schranke fuer d²χ/dt² allein begrenzt Δt also nicht wirksam.
- Anforderung: Die Schranke muss mit den Endwerten verbunden sein, z. B. ueber den Interpolationsfehler B·Δt²/8 gegen min |χ| an beiden Enden. Fuer den ersten Weg sollte stehen, dass er die Nullstellen der Interpolante findet; erst mit der Halbierungskontrolle ist er belastbar.
- Still verloren gehen Doppelwechsel jetzt nicht mehr: Z. 486 fordert die Halbierung, und dabei zeigt sich der Verlust als Δt-Abhaengigkeit. Deshalb ist G2 keine Auflage.

**G3. §9a Z. 327-329: Scheiterregel. Art: Ungenauigkeit, gering.**
- (a) Die Grenze ist aufgerundet. Genau gilt a ≤ 1,4192 (2f), und bei a = 1,42 ist der Kanal zu. Fuer eine Vorab-Regel gehoert die Grenze nach der sicheren Seite gerundet, oder die Formel a ≤ √(12/((ω+ρ)² − 1)) gehoert dazu.
- (b) Gerechnet ist mit Kontinuumswerten von ω und ρ. Auf einem Gitter mit a nahe 1,4 verschieben sich beide. Gerade dort entscheidet die Regel, die Annahme muss also im [H] genannt sein.
- (c) Inhaltlich ist es eine Trivialitaetsgrenze, also eine Gueltigkeitsbedingung des Tests, und keine Regel, wann die Bruecke scheitert. Diese Regel steht noch aus; Z. 330 kuendigt sie fuer die Zeit vor dem Lauf an. Die Bezeichnung sollte das trennen.

**G4. §1 Z. 90: "Der Ball baut sich ab Q ≈ 370 eine Huelle". Art: Ungenauigkeit, gering.**
- 370 ist die Stelle, an der χ(0) auf dem Duennwand-Ast unter 0,1 faellt. Der Uebergang ist stetig: h steigt von 0,026 an der Faltung, Hysterese wurde nicht gesehen.
- Auf dem Dickwand-Ast hat χ(0) = 0,960 bei Q = 144, und auch dort wird Q gross (ERGEBNIS §5).
- Anforderung: Ast und Schwelle nennen, z. B. "auf dem stabilen Duennwand-Ast faellt χ(0) ab Q ≈ 370 unter 0,1". Dass es kugelsymmetrische, knotenfreie Loesungen sind und "stabil" nur dQ/dω < 0 heisst, kann als Hinweis auf ERGEBNIS §5 folgen.

**G5. §5 Z. 197: "Bei glatten Koerpern kann er an Beruehrpunkten unendlich werden", jetzt unter "Flaechen". Art: Ungenauigkeit, gering. Neu durch die Umstellung.**
- Gegenfall: Eine Ebene schneidet eine Kugel im Abstand h vom Beruehrpunkt. Die Flaeche ist π(2Rh − h²), die Ableitung bei h = 0 betraegt 2πR. Sie ist endlich und springt nur.
- Unendlich wird der Gradient bei Laengen: Die Sehne 2√(2Rh − h²) und der Umfang des Schnittkreises gehen wie √h.
- Anforderung: Den Satz der Laengen-Zeile zuordnen, oder fuer Flaechen "springt" sagen.

**G6. §14 Z. 372 gegen Z. 385: Was N bei T ist. Art: Ungenauigkeit, gering. Rest von N5.**
- Z. 372 fordert "N = 4 ... 32 fuer R und T". Gerechnet ist T mit 4 bis 33 Ecken.
- Ist N = Ecken, reicht der Scan bis 33. Ist N = Ecken − 1 (wie bei "N+1"), reicht er von N = 3 bis 32. In beiden Lesarten deckt er das Soll ab. Der Mangel ist also nur, dass N fuer T nicht definiert ist und "Nachbarn von 11+1" deshalb zwei Lesarten hat.
- Anforderung: Fuer T festlegen, ob N die Ecken zaehlt oder Ecken − 1, und Z. 372 angleichen.

**G7. §2 Z. 109: "Auf einem endlichen Graphen ist das Band beschraenkt". Art: Ungenauigkeit, gering. Rest von N12, jetzt mit innerem Widerspruch.**
- §9a nennt fuer das unendliche kubische Gitter das beschraenkte Band [1; 1 + 12/a²]. Der Grund fuer die Schranke ist der beschraenkte Grad, nicht die Endlichkeit.
- Anforderung: Den Grund in Z. 109 angleichen.

**G8. §5 Z. 218: "Anziehung zwischen Knoten liefern in diesem Modell nur ...". Art: Praezisierung, gering.**
- Der Satz haelt fuer J = J(|x_i − x_j|) aus §5. §2 laesst aber J_ij(x) allgemein zu ("z. B."). Haengt J_ij auch von der Lage dritter Knoten ab, etwa ueber Flaechen oder Winkel, kann der Kopplungsterm andere Paare zusammenziehen.
- Anforderung: Die Annahme "J haengt nur vom Paarabstand ab" an den Satz binden.

**G9. §14 Z. 391: nachtraegliche Biegemoden-Spur [H]. Art: Markierung, gering.**
- Die Zuordnung nimmt k = 8 und 11 aus mod 360 und k = 15 aus mod 180. Die Spruenge bei N = 5 (mod 180) und N = 31 (mod 360) sind nicht verglichen.
- Die Verhaeltnisse an den uebrigen N nennt die Quelle nicht. Bei einer fast drehsymmetrischen Helix liegen die zwei tiefsten Biegemoden ohnehin nahe beisammen.
- Anforderung: Neben dem [H] die Auswahl offenlegen, also zwei Masse und ohne N = 5 und 31. Oder den Satz als blosse Beobachtung ohne "also" fassen.

**G10. §19 Z. 469: "in T gibt es nur die geometrische Ausrichtung". Art: Ueberdehnung, gering.**
- §14 Z. 391 nennt selbst eine schwache mechanische Spur [H]. Die ist zwar nicht 12-spezifisch, aber vorhanden.
- "In Stabilitaetsgroessen ... in T nicht gefunden" haengt an G1.
- Den R-Teil konnte ich nicht pruefen, die V5-Quelle war nicht freigegeben.
- Anforderung: "nur" einschraenken oder die [H]-Spur erwaehnen. Den Wortlaut an G1 angleichen.

## 5. Urteil

**Mit einer Auflage weitergeben: G1.**

- Die Auflagen der Vorlesung sind sachlich richtig umgesetzt:
  - N1: Die Kraftaussage stimmt in Vorzeichen und Mechanik, auch nach Relaxation.
  - N2: Der Kern ist umgesetzt, Doppelwechsel gehen nicht mehr still verloren. Rest siehe G2.
  - N5: Die Festlegung auf T ist aufgehoben.
- Alle nachgerechneten Zahlen stimmen:
  - 131,81 Grad, 9,9 Grad, 5,7 Grad, "erstmals" bei 12 und "erst" bei 31
  - 12 und 20 Ecken mit 30 und 54 Kanten
  - 0,853 = √0,728, unabhaengig ueber U/S bei S = 1,1797
  - Q ≈ 370 als Zahl
  - 6,96 und 1,42, wobei die Grenze aufgerundet ist
  - "hart" ab 4/3 und die Fensterbreiten
- **Auflage G1:** In §14 und §19 muss fuer die 12 sichtbar sein, dass die vorab festgelegte Vorhersage formal nicht eingetroffen ist. Ebenso, dass die Endeffekt-Erklaerung ungeprueft ist und ein faires Mass fuer kurze Ketten noch fehlt. Das reicht als Halbsatz. Sonst geben Finn und andere KI-Systeme "12 ist in der Stabilitaet nicht besonders" als Messergebnis weiter, und so viel traegt TETRAKETTE-1 nicht.
- Empfohlen vor der Weitergabe, je ein Halbsatz:
  - G4: Ast und Schwelle bei Q ≈ 370 nennen.
  - G3 (a, b): Grenze nach der sicheren Seite runden und die Kontinuumsannahme nennen.
  - G2: Die d²χ/dt²-Schranke an die Endwerte binden.
- G5 bis G10 sind gering und koennen mit der naechsten Fassung kommen.
- Nach G1 genuegt ein Blick nur auf diese Saetze, keine weitere Lesung.

**Grenzen dieser Lesung**
- Gelesen habe ich nur DIFF-v2.1-v2.2.txt, GEGENLESUNG-v2.1.md, die Diff-Stellen von v2.2 mit ihrem Umfeld, tetrakette-1/ERGEBNIS.md und KARTE.md sowie beutel-1/ERGEBNIS.md. Nichts Gesperrtes, keine Daten, kein Code.
- Nicht an der Quelle pruefbar waren:
  - das Fenster bei J = 10⁻⁴ (nur plausibel gemacht)
  - "3954 Punkte" und "n = 2 oszillatorisch"
  - der R-Teil von Z. 469
  - die vorher stehenden Projektzahlen ω² = 0,797677 und ρ = 1,744618, mit denen ich in 2f gerechnet habe
- Rechnungen im Kopf, Rechenwege in Abschnitt 2. Kein Interpreter, kein git, kein Peerbus, keine Literaturabfrage.
- v2.2 ist unveraendert: sha256 um 09:58:13 erneut ce233a55...f2c06.
- Ende: 2026-10-02 09:58:17 CEST (date). Dauer 11 min 37 s (09:46:40 bis 09:58:17).
