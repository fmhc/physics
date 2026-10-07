# FA-1 Farb-Analogie (Runde 8): Plan

- Bearbeiter: Anthropic-Agent (Opus 5.5) im Auftrag der Leitung claude-primary.
- Plan begonnen 2026-09-30 06:51:44 CEST (date), **vor jeder Rechnung dieser Karte**. Explorativ (v3).
- Anlass: Finn 06:21 "kommen wir mit den umlaufzuständen irgendwie auf die quark farben analogisch?", 06:25 "bzw haben
  wir da ansätze von spins".
- Gelesen: gesamtformel-20260921/KANDIDAT.md (ganz), STAND-GF.md, RUNDE-08.md (Karte FA-1), gf-bic/PLAN.md (nur
  gelesen, nicht gedoppelt), resonance-20260930/phase-bridge/PLAN.txt, REVIEW.txt, RESULT.json (nur gelesen).
- Belegstufen: [Hand] = Herleitung hier, [ES] = exakte Schreibtischaussage mit Beweisskizze, [H] = Hypothese,
  [L?] = Literatur aus dem Gedaechtnis, nicht an der Quelle geprueft.
- Konvention: J_ab = J = 1 fuer alle drei Paare (vollstaendiger Graph), g traegt das Vorzeichen von g J.

## 1. Herleitung von Hand

### 1.1 Die Rechnung der Leitung (gleiche Amplituden)

- psi_a = A e^{i theta_a} e^{-i omega t}: Kopplungsenergiedichte -g A^4 sum_{a<b} cos(2(theta_b - theta_a)).
- Mit phi_a = 2 theta_a und Z = sum_a e^{i phi_a} gilt sum_{a<b} cos(phi_b - phi_a) = (|Z|^2 - 3)/2.
  - g > 0: Minimum bei |Z| = 3 (gleiche Phasen mod pi), -3 g A^4. Keine Frustration.
  - g < 0: Minimum bei Z = 0 (verdoppelte Phasen im 120-Grad-Dreieck), -(3/2)|g| A^4. Jedes Paar erreicht nur
    cos = -1/2 statt -1: frustriert.
- **Bei festen, gleichen Amplituden stimmt die Rechnung der Leitung. [Hand]**

### 1.2 Mit freien Amplituden ist das 120-Grad-Dreieck nicht das Minimum [ES]

- Punktweise, bei fester Dichte S = sum x_a (x_a = |psi_a|^2):
  sum_{a<b} x_a x_b cos(phi_b - phi_a) = (|sum_a x_a e^{i phi_a}|^2 - sum_a x_a^2)/2.
- g < 0: Minimum, wenn sich die drei Zeiger x_a e^{i phi_a} schliessen und sum x_a^2 moeglichst gross ist. Schliessen
  geht nur fuer max x_a <= S/2. Groesstes sum x_a^2 dann bei x = (S/2, S/2, 0): **zwei Kanaele gegenphasig
  (psi_2 = +-i psi_1), dritter leer, Kopplungsenergie -|g| S^2/4.** Das 120-Grad-Dreieck gibt nur -|g| S^2/6.
- g > 0: Minimum -g S^2/3 bei gleichen Amplituden und gleichen Phasen (KANDIDAT 5.1, Gleichheitsfall).
- **Die Frustration wird durch Leeren eines Kanals aufgehoben.** Das geht im XY-Dreieck nicht, weil dort die
  Spinlaengen fest sind; hier sind nur S und nicht die einzelnen x_a festgelegt.

### 1.3 Alle stationaeren Baelle mit festem innerem Vektor [ES]

- Ansatz psi_a = c_a f(r) e^{-i omega t}, |c| = 1. Die Bewegungsgleichung (KANDIDAT 2.2) zerfaellt genau dann in eine
  einzige Radialgleichung, wenn sum_{b != a} c_a^* c_b^2 = 2 K c_a fuer alle a, mit K(c) = sum_{a<b} Re[(c_a^* c_b)^2].
  Das ist die Stationaritaet von K auf der Einheitskugel (Lagrange-Faktor 2K).
- Dann gilt fuer f die N = 1-Gleichung mit U_eff(S) = S - b S^2 + S^3/2, **b = 1 + g K**. Mit S' = b S wird das die
  beta-Familie mit beta_eff = 1/(2 b^2), und E_b(Q) = E_beta(b Q)/b, Q_b(omega) = Q_beta(omega)/b.
- Loesungen (mit Z = sum c_a^2): Multipliziert man die Bedingung mit c_a, folgt |c_a|^2 Z = (2K + x_a) c_a^2.
  - Z = 0: alle besetzten Kanaele gleich stark mit x_a = -2K. Drei Kanaele: 120 Grad. Zwei: gegenphasig.
  - Z != 0: alle c_a^2 kollinear (verdoppelte Phasen 0 oder pi). Ausrechnen gibt die Liste unten.

| Zustand | x = (x_1, x_2, x_3) | verdoppelte Phasen | K | b bei g = -0,3 |
|---|---|---|---|---|
| gleichphasig-3 | (1/3, 1/3, 1/3) | (0, 0, 0) | +1/3 | 0,9 |
| gleichphasig-2 | (1/2, 1/2, 0) | (0, 0) | +1/4 | 0,925 |
| einkomponentig | (1, 0, 0) | - | 0 | 1 |
| **120 Grad (zwei Drehsinne)** | (1/3, 1/3, 1/3) | (0, +-120, -+120) | **-1/6** | 1,05 |
| kollinear | (3/5, 1/5, 1/5) | (0, pi, pi) | -1/5 | 1,06 |
| **gegenphasig-2** | (1/2, 1/2, 0) | (0, pi) | **-1/4** | 1,075 |

- Nicht stationaer (nur Wegpunkt): gleiche Amplituden mit verdoppelten Phasen (0, pi, pi), K = -1/9.

### 1.4 Grundzustand bei fester Ladung [ES]

- Fuer jedes Feld gilt: sum_a |grad psi_a|^2 >= |grad sqrt(S)|^2 (Kato), sum |d_t psi|^2 >= Q^2/(4 int S)
  (Cauchy-Schwarz), und die punktweise Schranke aus 1.2.
- Daraus folgt E >= E_{N=1}(Q; b_max) mit b_max = 1 + |g|/4 (g < 0) bzw. 1 + g/3 (g > 0). Der gegenphasige
  Zweierball bzw. der gleichphasige Dreierball erreicht die Schranke.
- **g < 0: Grundzustand = gegenphasig-2 ("Mesonbild": zwei Zeiger heben sich auf), nicht das 120-Grad-Dreieck.**
- g > 0: Grundzustand = gleichphasig-3 (maximale "Farbladung" |Z| = 3, keine Neutralitaet).
- Nebenfolge fuer KANDIDAT 5.2/5.3 bei N = 3 und g < 0 [ES]:
  - Die Vakuumgrenze ist |g| <= 4(sqrt2 - 1) = 1,657 statt 1,243.
  - Das Fenster lautet omega^2_min = 1 - (1 + |g|/4)^2/2.
  - KANDIDATs Werte gelten fuer g > 0 scharf und fuer g < 0 nur als hinreichende Schranke. Sein "genau dann" in 5.2
    stimmt also nur fuer g > 0.

### 1.5 Energievergleich bei gleichem Q [Hand]

- Reihenfolge fuer g < 0 (grosses b heisst tiefer, strikt):
  E(gegenphasig-2) < E(kollinear) < E(120) < E(einkomponentig) < E(gleichphasig-2) < E(gleichphasig-3).
- Fuer g > 0 gilt die umgekehrte Reihenfolge.
- Erste Ordnung (Hellmann-Feynman, dE/d(gK)|_Q = -I_4, I_4 = int f^4 d^3x des Bezugsballs):
  - E_120 - E_1 ~ -|g| I_4/6
  - E_120 - E_anti2 ~ +|g| I_4/12
- Fenster je Zustand: omega^2_min = 1 - b^2/2, zum Beispiel 120 Grad bei g = -0,3: 0,44875.
- Existenz: Fuer g < 0 hat der 120-Grad-Ball b > 1 und existiert bis zur Vakuumgrenze 1,657. Fuer g > 0 ist b < 1:
  Das Fenster schrumpft, und bei festem Q kann er fehlen.

### 1.6 Stationaritaet, Kreisstrom und KANDIDAT Zeile 182 [ES]

- 120 Grad: c = (1, e^{i pi/3}, e^{2 i pi/3})/sqrt3, also Z = 0. Die Bedingung aus 1.3 gilt mit 2K = -1/3.
  **Der Zustand ist eine exakte stationaere Loesung.**
- Kanalstroeme: T_ab = -2g int Im[(psi_a^* psi_b)^2] = -+(sqrt3/9) g I_4 fuer alle drei Paare, gleicher Umlaufsinn.
  Also dQ_a/dt = T_ab + T_ac = 0 je Kanal: **stationaerer Kreisstrom.**
- KANDIDAT 4.2 Folgerung 3 ("stationaer, kein Kanalstrom") setzt reelle relative Phasen voraus. Der 120-Grad-Zustand
  ist das Gegenbeispiel mit komplexen relativen Phasen. Das ist kein Widerspruch, sondern die Grenze der Folgerung.
- KANDIDAT Zeile 182 (alpha_b - alpha_a in pi Z) beschreibt, welche Phasendrehungen **Symmetrien** sind. Die
  120-Grad-Phasen liegen nicht in pi Z. Deshalb ist der Zustand kein Symmetriebild eines reellen Zustands, sondern
  eine eigene Loesung. Sie bricht spontan die Konjugation C und die ungeraden Permutationen. Erhalten bleibt eine
  verdrehte Z_3: die zyklische Vertauschung mal globaler Phase mal Z_2-Vorzeichen.

### 1.7 Stabilitaet des 120-Grad-Balls: Energiesattel, aber gyroskopisch stabil [Hand, H]

- Energielandschaft: K_min(x) = -|x|^2/2 im Schliessbereich. Das 120-Grad-Dreieck liegt dort in der Mitte, also
  **Morse-Index 2 in den Amplitudenrichtungen** (fuer g < 0; fuer g > 0 Index 2 in den Phasenrichtungen). Ein
  Gradientenfluss verlaesst es.
- Die echte Dynamik ist aber gyroskopisch (Coriolis-Term 2 i omega d_t im mitdrehenden System), und ein gerader
  Index kann stabilisiert werden (Kelvin-Tait-Chetaev [L?]).
- Galerkin-Rechnung (gleiches Profil f, nur innere Richtungen, e = g kappa, kappa = I_4/I_2):
  - Im Raum senkrecht zu (1,1,1) gilt fuer Amplituden p und Phasen q:
    p'' + 2 omega q' = e (p/3 + R q), q'' - 2 omega p' = e (q - R p), R = Drehung um 90 Grad.
  - Charakteristisches Polynom fuer die Frequenz nu:
    **P(nu) = nu^4 - (4 omega^2 - 4e/3) nu^2 + 4 omega e nu - 2e^2/3**; das volle Spektrum ist {Nullstellen} vereinigt
    mit {-Nullstellen}. Stabil, wenn alle vier Nullstellen reell sind.
  - Kleines |e|: nu_+- = (|e|/(2 omega))(1 +- 1/sqrt3). Beide langsamen Moden sind reell, **also stabil.**
  - Krein-Vorzeichen (Energie der Mode): Bei g < 0 hat die langsamere Mode negative Energie, bei g > 0 die schnellere.
  - Grenzen (Hand, Bisektion auf P, in e/omega^2):
    - Krein-Kollision bei g > 0 fuer e/omega^2 ~ 0,609, bei g < 0 fuer ~ 1,78
    - Frueher greift die Kontinuumsschwelle: Liegt die Mode mit negativer Energie ueber 1 - omega, strahlt sie und
      waechst [L?, Krein-Satz fuer eingebettete Eigenwerte].
    - Mit kappa ~ 0,7 und omega^2 ~ 0,7 grob: g < 0 stabil bis |g| ~ 0,8 bis 1; g > 0 nur bis g ~ 0,25.
- Kontrolle derselben Rechnung: einkomponentiger Ball. Dort ergibt sich lambda^4 + 4 omega^2 lambda^2 - e^2 = 0, also
  ein reelles Paar und Instabilitaet. Das ist die Zwei-Moden-Formel von GF-BIC 1.4, deckungsgleich; ungerader Index,
  nicht stabilisierbar.
- **Mit Daempfung** waechst die Mode negativer Energie (Thomson-Tait-Chetaev [L?]). Der Gradientenfluss ist der voll
  gedaempfte Grenzfall.

### 1.8 Zweizustand, Drehsinn als Pseudospin (Frage c) [ES]

- **Gleich tief: exakt.** Eine ungerade Kanalpermutation (Automorphismus von J) bildet chi+ auf chi- bei gleichem Q ab.
  C bildet chi+ auf chi- mit -Q ab.
- Barriere bei festen gleichen Amplituden (wie im XY-Dreieck): Der Weg muss durch eine kollineare Lage, bestenfalls
  (0, pi, pi) mit K = -1/9. Also Delta K = 1/18 und Delta E ~ |g| I_4/18.
- **Mit freien Amplituden gibt es keine Barriere:** Der Weg chi+ -> gegenphasig-2 -> chi- faellt monoton ab, K von
  -1/6 auf -1/4, und steigt dann wieder. Am Rand des Schliessbereichs entartet das Dreieck, beide Drehsinne treffen
  sich dort.
- Uebergangszustand zwischen zwei Paar-Grundzustaenden: kollinear (3/5, 1/5, 1/5), K = -1/5, Morse-Index 1.
- Der Drehsinn ist ein innerer Zweizustand (Z_2), kein Raumspin: Die psi_a sind Skalare (KANDIDAT 3.4), J_z = 0 fuer
  den Radialzustand. Geschuetzt ist er hoechstens dynamisch (gyroskopisch), nicht energetisch.

## 2. Vorab-Erwartungen (geschrieben 2026-09-30 06:51 bis 06:54 CEST, Datei zuerst gespeichert 06:54:05 laut mtime, vor jeder Rechnung dieser Karte)

Bezug: Q_ref = Q des einkomponentigen Balls bei g = 0 und omega^2 = 0,70 (Schiessverfahren). Gitter h = 0,1, R = 40
(Fluss) bzw. 70 mit Schwamm ab 45 (Dynamik).

| Nr. | Erwartung | widerlegt, wenn |
|---|---|---|
| E1 | Stationaere Baelle aller sechs Typen (1.3) bei Q_ref: Reihenfolge der Energien wie 1.5, fuer alle g in {-1; -0,6; -0,3; -0,1; 0,1; 0,3; 0,6}, sofern der Ball existiert | eine Umkehrung der Reihenfolge ueber dem Gitterfehler |
| E1a | Erste Ordnung: (E_K - E_1)/(-g K I_4) in [0,9; 1,1] bei \|g\| = 0,1 | ausserhalb |
| E1b | Virial (Derrick) je stationaerem Ball: \|T + 3V\|/T < 1e-3 | groesser |
| E2 | Fluss bei g = -0,3 aus zufaelligen Phasen (gleiche Amplituden plus 1e-3 Rauschen): **Ende gegenphasig-2** (min n_a < 1e-3, zwei n_a bei 0,5 +- 1e-3), E = E_anti2 auf 1e-6 relativ, in allen Saaten; nie 120 Grad | ein Lauf endet bei 120 Grad oder einer Energie ueber E_anti2 + 1e-6 relativ |
| E3 | Fluss mit erzwungen gleichen Amplituden, g = -0,3: Ende 120 Grad, \|Z\|/3 < 1e-3, \|chi\| > 0,999, E = E_120 auf 1e-6; beide Drehsinne kommen vor; E(chi+) = E(chi-) auf 1e-10 relativ | anderes Ende, oder Energiedifferenz der Drehsinne > 1e-10 |
| E4 | Fluss bei g = +0,3: Ende gleichphasig-3 (n_a = 1/3, Z-Mass > 0,999), E = E_al3 | anderes Ende |
| E5 | Kontrolle g = 0: innerer Vektor bleibt, wie er ist (n_a und Phasen aendern sich < 1e-8); E = E_1 fuer alle Saaten | Phasenbindung bei g = 0 |
| E6 | Kontrolle N = 1: einkomponentiger Start bleibt exakt einkomponentig (Kanaele 2, 3 exakt 0,0) und endet bei E_1 | Kanal 2 oder 3 != 0 |
| D1 | Dynamik (ohne Daempfung) 120 Grad, g = -0,1 / -0,3 / -0,6, Stoerung 1e-3: beschraenkt (max \|n_a - 1/3\| < 10 x Anfangswert bis T), \|chi\| > 0,99 durchgehend | Wachstum ueber 10 x oder Drehsinnwechsel |
| D1a | Langsame Frequenzen (FFT von n_a) bei g = -0,1: beide nu_+- aus P(nu) auf 10 %; bei -0,3 die gebundene langsamere Mode auf 15 % | ausserhalb |
| D1b | Kreisstrom: \|T_ab\| = (sqrt3/9)\|g\| I_4 auf 1 %, gleicher Umlaufsinn, \|dQ_a/dt\| < 1e-3 \|T_ab\| im Mittel | ausserhalb |
| D2 | g = -1,0: [H] unsicher (Mode negativer Energie nahe der Kontinuumsschwelle); langsames Wachstum moeglich | (nur Beobachtung) |
| D3 | g = +0,1: beschraenkt. g = +0,3: [H] langsames Wachstum (eingebettete Mode negativer Energie), Rate < 1e-2. g = +0,6: nahe Krein-Kollision, Ausgang offen | g = +0,1 waechst |
| D4 | Positivkontrolle einkomponentig bei g = -0,3 mit Keim 1e-6 in Kanal 2 und 3: exponentielles Wachstum, Rate lambda = sqrt(-2 omega^2 + sqrt(4 omega^4 + g^2 kappa^2)) auf 25 % | kein Wachstum |
| D5 | Kontrolle N = 1 (Kanaele 2, 3 exakt 0): bleiben exakt 0,0; E und Q im Innenbereich auf 1e-6 relativ | != 0 |
| D6 | Grundzustand gegenphasig-2 bei g = -0,3, gestoert: beschraenkt | Wachstum |
| D7 | g = 0, 120 Grad: T_ab = 0 exakt, beschraenkt | T_ab != 0 |
| D8 | Groessere Stoerung 0,05 und 0,15 bei g = -0,3: [H] bei 0,15 Drehsinnwechsel oder Abgleiten zum Paarzustand; bei 0,05 beschraenkt | (Beobachtung, Groessenordnung der dynamischen Barriere) |
| D9 | chi- bei g = -0,3: Energie gleich chi+ auf 1e-10, Verlauf gespiegelt | Abweichung |
| C1 | Barriere bei festen gleichen Amplituden: E(K = -1/9) - E(K = -1/6) bei Q_ref in [0,8; 1,2] x \|g\| I_4/18 fuer \|g\| <= 0,3 | ausserhalb |

## 3. Kontrollen

- g = 0: U(3)-symmetrisch, keine Phasenbindung (E5, D7).
- N = 1-Grenze: der bekannte Ball; leere Kanaele bleiben exakt leer (E6, D5). Q_ref und E_ref aus dem Schiessverfahren
  gegen den Fluss auf dem Gitter.
- Positivkontrolle Instabilitaet: einkomponentig bei g != 0 (D4). Das ist GF-BICs Befund und wird hier nur als
  Werkzeugkontrolle benutzt, nicht neu ausgewertet.
- Erhaltung: E, Q in der Dynamik; dQ_a/dt gegen sum_b T_ab (Kanalbilanz).
- Gitter: h = 0,1 gegen 0,05 fuer E1 (Energiedifferenzen).
- Virial je stationaerem Zustand (E1b).

## 4. Umsetzung und Kostenplan

- fa1.py (torch, float64/complex128; Geraet cuda, lokal nur mit --geraet cpu fuer den Rauchtest):
  - ref: Schiessverfahren fuer Q_ref, dazu N = 1-Fluss bei festem Q fuer alle b = 1 + g K (Batch), Energien, omega,
    I_4, kappa, Virial; Galerkin-Polynom (Nullstellen, Krein-Vorzeichen, Schwellen).
  - fluss: Gradientenfluss der drei Komponenten bei festem Q (E2 bis E6).
  - dyn: Zeitentwicklung (Stoermer-Verlet, Schwamm am Rand) fuer D1 bis D9.
- Rechenorte:
  - Rauchtest lokal: CPU, CUDA_VISIBLE_DEVICES leer, 1 Thread, nice 19, timeout 120, Ausgabe lauf-lokal/
  - Rechnungen auf der .69 ueber kleintest.sh, Spur p4000a (sonst p4000b), aus /home/fmh/fmhc-physics-remote/runde8-fa1/
  - je Aufruf hoechstens 10 min, eigener Zeitwaechter 540 s
- Geschaetzt:
  - ref: 1 bis 3 min
  - fluss: 2 bis 5 min
  - dyn: 3 bis 8 min
  - zusammen unter 20 min Rechenzeit

## 5. Literatur (d), nur an der Quelle Gelesenes

- nicht-abelsche Q-Baelle (SU(N)-Ladung)
- Dreiecks-XY-Antiferromagnet: 120 Grad, Chiralitaet Z_2
- C_n-Regeln fuer topologische BIC-Ladungen in der Photonik
- Unsicheres mit [L?].

## Einfach gesagt

Die Idee der Leitung stimmt, solange alle drei Feldsorten gleich stark sein muessen: Dann stellen sich ihre Phasen wie
ein Mercedes-Stern ein, und die Summe ist null wie bei den drei Quarkfarben. Unsere Formel zwingt die Sorten aber nicht
zur gleichen Staerke, und von Hand ergibt sich: Billiger ist es, eine Sorte ganz zu leeren und die beiden anderen
gegeneinander zu stellen, also eher ein "Meson" als ein "Baryon". Der Stern ist trotzdem eine echte, ruhende Loesung mit
einem inneren Kreisstrom, und die Eigendrehung des Balls koennte ihn wie einen Kreisel stabil halten. Das pruefen wir
jetzt mit einer kleinen Rechnung.

## Nachtrag A (2026-09-30 07:07:44 CEST, date): Zwischenerwartung nach ref, vor jedem dyn-Ergebnis

- Grund: ref (.69, p4000a) hat das Galerkin-Polynom an den echten omega und kappa jedes 120-Grad-Balls bei Q_ref
  ausgewertet. dyn laeuft seit 05:07:14 UTC; aus-dyn/ ist bei Niederschrift leer (ls um 07:07:44).
- Diese Zeilen ergaenzen D1 bis D3, ersetzen sie aber nicht. Gewertet wird gegen die eingefrorene Tabelle.

| g | e/omega^2 | langsame Moden (Krein) | Schwelle 1 - omega | Zwischenerwartung |
|---|---|---|---|---|
| -0,1 | 0,090 | 0,0565 (+), 0,0159 (-) | 0,171 | beide gebunden: beschraenkt |
| -0,3 | 0,296 | 0,168 (+), 0,0528 (-) | 0,188 | beide gebunden: beschraenkt |
| -0,6 | 0,685 | 0,331 (+, eingebettet), 0,125 (-) | 0,216 | Mode negativer Energie gebunden: beschraenkt; die (+)-Mode klingt ab |
| -1,0 | 1,398 | 0,506 (+, eingebettet), 0,284 (-, eingebettet) | 0,258 | [H] langsames Wachstum (Mode negativer Energie strahlt) |
| +0,1 | 0,082 | 0,0567 (-), 0,0145 (+) | 0,156 | beide gebunden: beschraenkt |
| +0,3 | 0,224 | 0,171 (-, eingebettet), 0,0396 (+) | 0,141 | [H] langsames Wachstum |
| +0,6 | 0,389 | 0,343 (-, eingebettet), 0,069 (+) | 0,120 | [H] Wachstum; keine Krein-Kollision (0,389 < 0,609) |
