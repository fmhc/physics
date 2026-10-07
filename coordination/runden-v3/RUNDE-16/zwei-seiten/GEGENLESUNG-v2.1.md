Urteil: mit Auflagen weitergeben. Vorher N1 (Anziehung aus Feldrelaxation haelt mechanisch nicht), N2 (§20 Schritt 3 kann doppelte Wechsel nicht erkennen) und N5 (11+1 nicht auf Variante T festlegen) berichtigen. 29 der 32 Befunde sind erledigt, 2 teilweise, 1 entfaellt; B1-B4 und U1 sind richtig erledigt.

# Gegenlesung der letzten Schicht: ZWEI-SEITEN-DES-FELDES-v2.md, Fassung v2.1

- Leser: frischer Gegenleser, Haus Anthropic (Claude), Text vorher nicht gesehen
- Beginn: 2026-10-02 09:23:58 CEST (per date gemessen)
- Ende: 2026-10-02 09:39:09 CEST (per date gemessen), Dauer also 15 min 11 s
- Gegenstand: coordination/runden-v3/RUNDE-16/zwei-seiten/ZWEI-SEITEN-DES-FELDES-v2.md (v2.1, ab 09:16:54)
- Vergleich: v2.0-stand-0855.md, GEGENLESUNG-v2.md, ausprobieren/ERGEBNIS.md, two-sides-review/codex/ARBEITSMODELL-V2.md
- Arbeitsweise: nur lesen, Zahlen im Kopf mit Rechenweg, kein Interpreter, v2.1 nicht geaendert

## 1. Status der 32 Befunde aus GEGENLESUNG-v2.md

Gelesene Fassung: v2.1, sha256 1a2da1ab80d76dee1ad4b1685e46e5b781c04646e1982e2a98318c2aa85434cc (mtime 09:19:01). Zeilen beziehen sich darauf.
Zaehlung: GEGENLESUNG-v2 nennt selbst keine Zahl. B1-B14, R1-R8, U1-U8 sind 30, mit A11 und A12 also 32. Die uebrigen A-Punkte sind unten mitgefuehrt (A1-A4, A7, A9 decken sich mit B3, B9, B10c, B4, U3, R7).

| Nr. | Kurz | Status | Neue Stelle in v2.1 | Bemerkung |
|---|---|---|---|---|
| B1 | Fenster "breiter" | erledigt | Z. 108-113 | gleichwertig; Rest "Nur hier ... breiter" siehe N8 |
| B2 | Q-Ball-Stabilitaet | erledigt | Z. 69-72 | E/Q = ω und Dickwand-Grenzfall nachgerechnet, stimmt |
| B3 | Massenmatrix | erledigt | Z. 237-243, 279, 318, 503 | M = diag(m_i; 2, 2), K v = ω²M v richtig; Rest μ_n siehe N7 |
| B4 | Schnittenergie | erledigt, neue Unschaerfe | Z. 185-188, 21 | Ableitungsordnung vertauscht, siehe N6 |
| B5 | λ-Vorzeichen, Band | erledigt | Z. 98-101, 110 | "hart" nur als V' > m_Φ² definiert, siehe N8 |
| B6 | Stabilitaetsbegriffe | erledigt | Z. 251-254 | woertlich wie Vorschlag |
| B7 | Wege in die Instabilitaet | erledigt | Z. 259-261 | woertlich wie Vorschlag |
| B8 | GSS/VK | erledigt | Z. 264-268 | Rest: "Regel traf an allen 3954 Punkten" passt nicht mehr zum n >= 2-Zweig, siehe N9 |
| B9 | Energie "immer" | erledigt | Z. 282 | Grammatik: "vorgeschriebener Bewegung" |
| B10 | Schrittweite, Chirotop, ν(x) | erledigt, neue Luecke | Z. 149-158, 164, 458 | (a) bis (c) erledigt; neue Rechenanweisung Z. 458 nicht umsetzbar, siehe N2 |
| B11 | Zaehlregel | erledigt | Z. 226-231 | Euler-Rechnung nachvollzogen; Wald folgt bei offener Kette von selbst |
| B12 | Vakuum | erledigt | Z. 68 | stimmt |
| B13 | Zustandsdichte | erledigt | Z. 323 | D_L(l) ~ l^(d_s/2-1) stimmt |
| B14 | Symbole | teilweise | Z. 15-19 | Q geloest; offen: M, K, s, P, μ_n, siehe N7 |
| R1 | V3 nicht gyroskopisch belegt | erledigt | Z. 255-258 | "vergroessert R" ist Deutung des Erstlesers, nicht ERGEBNIS-Wortlaut (gering) |
| R2 | Maxwell-Raster, "nachgerechnet" | erledigt | Z. 220-223 | 1/0,4352 = 2,298 stimmt; "monoton" nur auf 6 Tabellenpunkten |
| R3 | Rad- statt Ring-Graph | erledigt | Z. 109, 269, 363 | |
| R4 | J·N 0,54 bis 0,60 | erledigt | Z. 367 | Produkte nachgerechnet |
| R5 | Mass "S(N) > 3σ" | erledigt | Z. 355, 365, 369-370 | s_max steht weiter ohne Hinweis in der Kennzahlliste (gering) |
| R6 | Kopf, §17 A, Naechster Schritt | teilweise | Z. 9, 398-401, 516-518 | Kopf und §17 erledigt; neue Reihenfolge widerspricht §18, siehe N4 |
| R7 | Literaturmarken | erledigt | Z. 8, 218, 266, 428 | Battye/Sutcliffe ohne arXiv-Nummer, siehe Abschnitt 2 |
| R8 | Projektzahlen | erledigt (Quelle nicht pruefbar) | Z. 75-77, 307-308 | ρ definiert, Atmung/Dipol, alle drei als bewiesen; RUNDE-12.md fuer mich gesperrt |
| U1 | 11 und 19 | erledigt | Z. 362-366, 444, 472 | Kernpunkt sauber; Rest zu "+1" siehe N5 |
| U2 | "erste messbare Bruecke" | erledigt | Z. 112-113 | gestrichen, Gegenaussage steht |
| U3 | "zwei Seiten" | erledigt | Z. 33-35, 305 | "Es gibt zwei Deutungen" klingt abschliessend, siehe N10 |
| U4 | Variante B | erledigt | Z. 25, 88, 325 | |
| U5 | "echte Diskretisierung" | erledigt | Z. 14, 91 | |
| U6 | §19 "anschliessen" | erledigt, neue Ueberdehnung | Z. 431 | neuer Satz "ohne aeussere Zeit" trifft nicht auf alle vier zu, siehe N3 |
| U7 | galileisch, Uhrenvergleich | erledigt | Z. 172-173 | |
| U8 | Probe nie/immer/nur | erledigt | wie Einzelbefunde | |
| A5 | corr(E, ν), N_I = 0 | erledigt | Z. 339, 347 | Verzoegerung jetzt gleich Fensterbreite, siehe N11 |
| A6 | Bedeutung "+1" | teilweise | Z. 23, 225 | §21 Frage 8 und Naechster Schritt legen 11+1 auf T fest, siehe N5 |
| A8 | Kraft aus J(r) | erledigt, neue Ueberdehnung | Z. 204-206 | "Anziehung erst ueber Feldrelaxation" haelt mechanisch nicht, siehe N1 |
| A10 | Rand bei stiller Stelle | erledigt | Z. 311, 408 | "Bloch-Rand" unpassend, siehe N12 |
| A11 | Codex' Zweifeldfassung | erledigt | Z. 79-82 | neuer Wert ≈ 0,728 nachgerechnet, stimmt; "laeuft" veraltet, siehe N13 |
| A12 | Codex "hinreichend" | entfaellt | - | betrifft Codex' Text, nicht v2 |

Kopfsatz Z. 4 "Alle Befunde ... sind eingearbeitet": fast richtig; B14 und A6 sind nur teilweise erledigt, R6 hat eine neue Abweichung.

## 2. Neue Befunde in v2.1

Reihenfolge nach Gewicht fuer die Weitergabe. Vorschlaege sind Anforderungen, den Wortlaut waehlt der Autor.

**N1. §5 Z. 204-206 (und §19 Z. 438), "Anziehung kann erst ueber die Relaxation des Feldes entstehen". Art: Fehler (Mechanik), mittel. Kam ueber den A8-Vorschlag des Erstlesers herein.**
- Die Formel in Z. 205 stimmt: F_i = -J'(r)·|Ψ_i - Ψ_j|²·(x_i - x_j)/r.
- Bei J' < 0 ist der Vorfaktor -J'·|Ψ_i - Ψ_j|² >= 0 fuer *jeden* Feldzustand, denn |Ψ_i - Ψ_j|² >= 0. Der Kopplungsbeitrag zwischen zwei verbundenen Knoten ist also zu jedem Zeitpunkt abstossend oder null, auch nach Relaxation und im Zeitmittel. "Bei festgehaltenen Feldern" engt unnoetig ein.
- Adiabatisch gilt dasselbe: Fuer E_eff(r) = min ueber Ψ bei festem Q gibt der Einhuellendensatz dE_eff/dr = J'(r)·|ΔΨ*|² <= 0, also keine Rueckstellkraft.
- Anziehung zwischen Knoten liefern in diesem Modell nur E_geo, E_int oder ein J mit J' > 0. Effektive Anziehung zwischen teilchenartigen Moden waere nur indirekt denkbar [H]: ueber Feldueberlapp zweier Moden auf dem Graphen (phasenabhaengig wie bei Q-Baellen) oder ueber die Verformung der Geometrie (elastisch vermittelt).
- Vorschlag: "Bei J' < 0 ist der Kopplungsbeitrag zur Kraft zwischen zwei verbundenen Knoten fuer jeden Feldzustand abstossend oder null. Effektive Anziehung zwischen Moden koennte nur indirekt entstehen, ueber Feldueberlapp oder Verformung der Geometrie [H]. Sie wird nicht eingesetzt." In §19 "aus Feldrelaxation" entsprechend fassen.

**N2. §20 Z. 458, "Hoechstens ein Wechsel je Schritt und Quadrupel, sonst Schritt verkleinern". Art: Ungenauigkeit (Rechenanweisung), mittel. Neu in v2.1.**
- Zwei Wechsel in einem Schritt sind am Vorzeichen nicht sichtbar, beide Schrittenden haben dasselbe Vorzeichen. Genau so gingen in V4 bei Δt = 0,2 sechs Ticks verloren (ERGEBNIS Z. 125). Die Anweisung kann ihre eigene Verletzung nicht erkennen.
- Vorschlag: "Doppelte Wechsel sind am Vorzeichen allein nicht erkennbar. Deshalb χ und dχ/dt an beiden Schrittenden auswerten und alle Nullstellen im Schritt suchen, oder Δt ueber eine Schranke fuer d²χ/dt² begrenzen. Kontrolle immer durch Halbierung von Δt (§18)." Z. 151 kann als Bedingung bleiben.

**N3. §19 Z. 431, "Dort ist die Geometrie selbst dynamisch, ohne aeussere Zeit und Einbettung". Art: Ueberdehnung, gering bis mittel. Neu in v2.1.**
- "Ohne Einbettung" gilt fuer alle vier. "Ohne aeussere Zeit" gilt nicht fuer alle vier:
  - CDT hat eine ausgezeichnete Zeitblaetterung [L?].
  - Fuer Quantum Graphity vertritt Markopoulou "spaceless, not timeless", die Zeit bleibt also. Belegt ist das nur durch das Abstract von arXiv:0909.1861, das ich um 09:35:20 ueber die API gelesen habe. Dass Quantum Graphity selbst mit einer Hamilton-Zeit rechnet, ist [L?].
- Vorschlag: "Dort ist die Geometrie selbst dynamisch und nicht eingebettet; die Rolle der Zeit unterscheidet sich je Ansatz [L?]."

**N4. Naechster Schritt Z. 516 gegen §18 Z. 415 und §17. Art: Ungenauigkeit (innerer Widerspruch), mittel.**
- Variante T steht vor der dritten Positivkontrolle, der Kontinuums-Q-Ball-Stelle. §18 verlangt "bekannte Antworten zuerst (§17 A)", und §17 ordnet A vor B und C.
- R6 hatte "mit Kontinuums-Q-Ball-Stelle, §9a und Variante T beginnen" vorgeschlagen. Die neue Reihenfolge ist nicht gleichwertig.
- Vorschlag: entweder die Q-Ball-Kontrolle vorziehen, oder begruenden, dass der erste T-Lauf ohne Feld auskommt und nur V1, V2 und V4 als Kontrollen braucht.

**N5. §21 Frage 8 Z. 472 und Naechster Schritt Z. 516 gegen Z. 23 und Z. 225. Art: Ungenauigkeit (Festlegung trotz offener Frage), mittel fuer die Weitergabe.**
- Z. 23 und Z. 225 sagen, die Bedeutung von "+1" sei offen und Finn muesse sie klaeren. Frage 8 ("und zwar in Variante T?") und "Variante T (Tetraederkette 11+1/19+1 ...)" legen 11+1/19+1 aber auf T fest. Ein anderes KI-System liest daraus: Gemeint ist die Tetraederkette, und R ist erledigt.
- Ausserdem fehlt fuer T, was N heisst. Soll 11+1 zu 12 Ecken gehoeren, ist N = Ecken - 1 = N_T + 2, also N_T = 9 und 17. Der Scan "N = 4 ... 32" (Z. 354) und die "Nachbarn" sind fuer T dann erst definiert.
- Vorschlag: Frage 8 "... zuerst in Variante T (Form des Tetra-Bündels), dann R; welche Finn meint, ist offen". Fuer T N festlegen (z. B. N = N_T + 2) und die Nachbarn benennen.

**N6. §5 Z. 186-187 und Aenderungsliste Z. 21, Ableitungsordnung. Art: Ungenauigkeit, gering. Neu in v2.1.**
- Punktzahl: Die *Energie* springt, ihr Gradient ist dort formal eine Deltaspitze. v2.0 hatte "an Ereignissen unendlich", das war fuer Punktzahlen richtig. "Gradient ... springt" ist es nicht.
- Laengen (Schnittstrecke, Ebene durch Dreieck): Die Laenge knickt, ihr Gradient springt. Beim Durchgang einer Ecke waechst die Laenge linear mit dem Abstand.
- Flaechen generischer Ebenenschnitte durch Tetraeder: Sie sind einmal stetig differenzierbar (Flaeche ~ Abstand² beim Eckendurchgang, quadratischer Spline mit einfachen Knoten). Hier knickt der Gradient.
- Z. 21 "hat fast ueberall keinen Gradienten" heisst woertlich "nicht differenzierbar". Gemeint ist "Gradient fast ueberall null".
- Vorschlag: "Punktzahl: Energie springt, Gradient fast ueberall null. Laengen: Energie knickt, Gradient springt. Flaechen: Gradient stetig, knickt."

**N7. Symbole (Rest von B14). Art: Ungenauigkeit, gering. Bei μ_n mittel, weil B3 genau daran hing.**
- μ_n heisst in Z. 17 und Z. 389 nur "Eigenwerte" und wird im Text nicht mehr benutzt. Die Tabelle stellt ω_n und μ_n nebeneinander, das laedt zum alten ω_n² = μ_n ein. Vorschlag: "μ_n: Eigenwerte der Hesse-Matrix K (nicht ω_n²)" oder streichen.
- M ist Zentralmasse (§6 Z. 219-222, m/M) und Massenmatrix (§7, §22).
- K ist Zellkomplex (§2 Z. 86) und Hesse-Matrix (§7).
- s ist Dichte |Φ|² (§1) und Stabilitaetsexponent (§7, §14).
- P ist Punktzahl (§6), Rueckkehrwahrscheinlichkeit (§10) und Wahrscheinlichkeit (§11).

**N8. §2 Z. 99 und Z. 110, "hart" und "Nur hier ist es breiter". Art: Ungenauigkeit, gering.**
- (a) Breiter ist das Fenster auch bei kleinem J > 0, nicht nur im Grenzfall. Bei der Kontrolle J = 10⁻⁴ ([0,334; 0,999], ERGEBNIS Z. 147) ist die Breite 0,999 - 0,334 = 0,665 > 0,5. Bei J = 0,05 ist sie 0,945 - 0,475 = 0,470 bis 0,960 - 0,475 = 0,485 < 0,5, und die Unterkante liegt unter 1/2. Vorschlag: "Bei kleinem J breiter (J = 10⁻⁴: [0,334; 0,999]), ab etwa J = 0,05 schmaler."
- (b) "Hart fuer S > 2λ/(3g)" stimmt nur, wenn "hart" V'(S) > m_Φ² bedeutet, also eine Frequenz ueber dem linearen Wert. Die Steigung von V' wird schon bei S = λ/(3g) positiv, im Projektmodell bei 2/3. Rechnung: V'' = -2λ + 6gS = 0 bei S = λ/(3g). Vorschlag: die Bedeutung von "hart" in einem Halbsatz nennen.

**N9. §7 Z. 264-269, "Die Regel traf an allen 3954 Punkten". Art: Ungenauigkeit, gering.**
- In V5 lautete die Regel: "stabil, wenn K_u keine negative Richtung hat oder genau eine mit dQ/dω < 0" (ERGEBNIS Z. 156). Fuer n >= 2 sagt sie also "instabil" voraus.
- v2.1 sagt fuer n >= 2 dagegen nur, man brauche die Krein-Zaehlung, und macht keine Vorhersage. Damit passt "die Regel" nicht mehr zum geschriebenen Schema.
- Vorschlag: "Die Vorhersage 'stabil genau bei n = 0 oder bei n = 1 mit dQ/dω < 0' traf an allen 3954 Punkten. Die Punkte mit n = 2 waren instabil (oszillatorisch). Allgemein ist n >= 2 nicht zwingend instabil."

**N10. Z. 33, "Es gibt zwei Deutungen". Art: Ueberdehnung, gering.**
- Der Satz klingt abschliessend. Codex weist selbst weitere Lesarten zurueck: zweite Raumseite, Antimaterie, Re/Im (ARBEITSMODELL-V2 Z. 15-17).
- Vorschlag: "Bisher liegen zwei Deutungen vor ... Finn fragen."

**N11. §13 Z. 346, C_{I,ν}(Δ) = ⟨δN_I(t) δν_Δ(t+Δ)⟩. Art: Ungenauigkeit, gering. Neu in v2.1.**
- Die Verzoegerung ist jetzt dieselbe Groesse wie die Fensterbreite von ν_Δ. Wer die Verzoegerung variiert, aendert auch das Messfenster.
- Vorschlag: eigene Verzoegerung, etwa C_{I,ν}(τ_v) = ⟨δN_I(t) δν_Δ(t + τ_v)⟩ bei festem Δ.

**N12. §9a Z. 311 und §17 Z. 408, "unendliches Gitter (Bloch-Rand)". Art: Ungenauigkeit, gering.**
- Bloch-Randbedingungen gehoeren zu periodischen Anordnungen: eine Zelle mit Phasenfaktor, das Spektrum bleibt diskret. Fuer eine einzelne Mode im unendlichen Gitter braucht man eine ausstrahlende, transparente Randbedingung, etwa ueber die Gitter-Green-Funktion, oder eine absorbierende Schicht.
- Hinweis fuer die Vorhersage, Schreibtisch [H]:
  - Annahme: kubisches 3D-Gitter mit Naechstnachbarkopplung J = 1/a². Das Band ist dann [1; 1 + 12/a²].
  - Der offene Kanal liegt bei (ω + ρ)². Mit ω = √0,797677 ≈ 0,89313 ist ω + ρ ≈ 2,63775 und (ω + ρ)² ≈ 6,9577.
  - Er liegt nur fuer 12/a² >= 5,9577 im Band, also fuer a <= √2,0142 ≈ 1,42.
  - Bei groeberem Gitter ist der Kanal geschlossen und die Stille trivial. Das gehoert in die Scheiterregel.
- Z. 100 "Auf einem endlichen Graphen ist das Band beschraenkt": Der Grund ist die Diskretheit (beschraenkter Grad), nicht die Endlichkeit. Auch das unendliche Gitter aus §9a hat eine Oberkante.

**N13. §1 Z. 81, "Schreibtischwert der Leitung ≈ 0,728; Test BEUTEL-1 laeuft". Art: Markierung, gering.**
- Den Wert habe ich nachgerechnet, er stimmt als Duennwand-Schranke min U/S.
  - Bei festem S minimiert χ² = max(0, 1 - 2S).
  - Fuer S <= 1/2 ist U/S = 2 - 2S + S²/2. Das faellt monoton auf 1,125 bei S = 1/2.
  - Fuer S > 1/2 ist χ = 0 und U/S = 1/(4S) + 1 - S + S²/2. Das Minimum liegt bei 4S³ - 4S² - 1 = 0, also S ≈ 1,1797 (bei 1,179: -0,0047; bei 1,18: +0,0025).
  - Wert: 0,2119 + 1 - 1,1797 + 0,6958 ≈ 0,728.
- Die Gradientenkosten von χ sind nicht enthalten, deshalb "Schreibtischwert". "Laeuft" veraltet nach der Weitergabe. Vorschlag: "(Stand 09:16)" anfuegen oder den Status streichen.

**N14. §14 Z. 355-358, "Kennzahlen, alle nach Abzug der Symmetriemoden". Art: Ungenauigkeit, gering.**
- q_life und f_stab sind keine Spektralgroessen, fuer sie ergibt der Zusatz keinen Sinn.
- s_max = max Re s steht weiter ohne Hinweis in der Liste. In V3 war genau diese Groesse fuer den 3σ-Test ungeeignet (R5).
- Vorschlag: "s_max (nach Abzug der Symmetriemoden) nur als Stabilitaetsanzeige, nicht fuer den 3σ-Test".

**N15. §4 Z. 152, "bei jedem Δt <= 0,1". Art: Markierung, gering.**
- Geprueft sind nur 0,1; 0,05; 0,02; 0,01; 0,005 und 0,001 (ERGEBNIS Z. 124). Die Formulierung stammt aus ERGEBNIS Z. 16.
- Vorschlag: "bei allen geprueften Δt von 0,1 bis 0,001".

**N16. Kleinigkeiten ohne Sachfolge.**
- Z. 257: Hinter "Laut ERGEBNIS ... durch Zug statt Stauchung:" steht die Deutung des Erstlesers ("vergroessert R"), kein ERGEBNIS-Wortlaut. Mechanisch passt sie.
- Z. 231: "Mit einer konvexen Doppelpyramide" meint: Je zwei benachbarte Tetraeder bilden eine konvexe Doppelpyramide.
- Z. 282: "vorgeschriebener Bewegung".
- Z. 428: Battye/Sutcliffe ohne Nummer. Die API bestaetigt hep-th/0003252 = Battye, Sutcliffe, "Q-ball Dynamics" (09:34:53). Das Abstract nennt das Potential nicht, die "sextische Familie" stuetzt sich also allein auf Codex' Lesung. Vorschlag: "[S: Codex, hep-th/0003252v1 §2]".
- Vanderbei/Kolemen: Den Satz "always unstable for 2<=n<=6 and for n > 6 they are stable provided that the central mass is massive enough" habe ich um 09:35:09 selbst im Abstract gelesen. Die Marke in Z. 218 stimmt.

## 3. Rueckwaertsprobe: Kopf, Aenderungsliste, Paragraf 19, Naechster Schritt

**Kopf (Z. 1-9)**
- "32 Befunde, darunter 4 Fehler": Die 4 Fehler stimmen (B1-B4). Die Zahl 32 steht nicht in GEGENLESUNG-v2 und ergibt sich nur bei einer bestimmten Zaehlung (Abschnitt 1).
- "Alle Befunde ... eingearbeitet": fast. B14 und A6 sind nur teilweise erledigt (N7, N5).
- Die Zeile mit den V1-V5-Zahlen ("berichtet, nicht unabhaengig nachgerechnet") stimmt mit ERGEBNIS Z. 5 und den Selbstanzeigen.

**Aenderungsliste (Z. 13-25) gegen Haupttext**

| Punkt | Haupttext | Ergebnis |
|---|---|---|
| 1 | §1 | stimmt |
| 2 | §2 Z. 91-97 | stimmt |
| 3 | Symbolliste | unvollstaendig (N7) |
| 4 | §4 Z. 149-151 | stimmt; die Bedingung ist richtig gesetzt, §20 setzt sie falsch um (N2) |
| 5 | §5 | Wortlaut "fast ueberall keinen Gradienten" (N6) |
| 6 | §7 | stimmt |
| 7 | §6 Z. 225 | stimmt; widerspricht aber §21 Frage 8 und dem Naechsten Schritt (N5) |
| 8 | §9a | stimmt; "noch nicht gerechnet" steht beidseitig |
| 9 | §2 Z. 88, §10 Z. 325 | stimmt |

**§19 gegen Haupttext**
- Battye/Sutcliffe: richtig eingeschraenkt (N16 Nummer).
- Moeckel [L?]: stimmt.
- Ansaetze mit Beruehrungspunkten: N3.
- "Effektive Anziehung ... aus Feldrelaxation": N1.
- "11 oder 19 (Variante T ungerechnet)": deckt sich mit §14 Z. 366.
- Spin 1/2: nachgerechnet.
  - Wegen V(s)/s = 1 - s + s²/2 >= 1/2 gilt V >= s/2, und V ~ s³/2 fuer grosses s.
  - Endliche Energie heisst also: ∇Φ in L², Φ in L² und in L⁶. Diese Menge ist ein Vektorraum, also konvex und zusammenziehbar.
  - Fuer das Projektmodell haelt die Aussage. Der Zusatz "fuer das Geometriemodell nicht geprueft" ist richtig.

**Naechster Schritt (Z. 512-522)**
- Reihenfolge gegen §17 und §18: N4.
- Festlegung von 11+1 auf T: N5.
- "Federtetraeder und Maxwell-Ring bestanden (V1, V2)": stimmt mit §17 A und ERGEBNIS Z. 10-14.
- "als erste echte Bruecke": stimmt mit §9a. Die Bedingung "unter der Deutung Kontinuum/Diskret" aus §9a fehlt hier (gering, U3).

**Zahlen gegen ERGEBNIS (alle neu gesetzten)**
- 2·10⁻¹⁵: Quelle 1,8e-15 und 2e-15.
- 1226 von 4254, 229 + 997 = 1226, 6 fehlen bei 0,2, 4·10⁻¹³: Quelle <= 3,7e-13.
- 13 %: 620/4675 = 0,1326.
- Raster 10⁻⁹ bis 10⁻¹ mit 81 Punkten, c_N 2,45 und 2,301.
- Ω 0,38 und 0,89: Quelle 0,382 und 0,890.
- 3954.
- Fenster [0,475; 0,945-0,960] und [0,59; 0,885-0,925].
- J·N 0,54 bis 0,60, N_max 20/15/11/9/7, v5b N = 4 bis 26.
- Alles stimmt. Die neuen Feldformeln habe ich vorwaerts nachgerechnet, sie stimmen:
  - min V' = m_Φ² - λ²/(3g) bei S = λ/(3g)
  - hart fuer S > 2λ/(3g), im Projektmodell 4/3
  - λ² <= 4m_Φ²g
  - E/Q = ω einer ebenen Welle
  - Dickwand: Q = (ω/(λκ))∫F², dQ/dω > 0
  - D_L ~ l^(d_s/2-1) ergibt P ~ t^(-d_s/2)
  - Zweifeld bei χ = ±1: Fenster (3/2, 2)

## 4. Absolute Aussagen (nie/immer/nur/alle)

Geprueft sind die neuen oder geaenderten Saetze. Die alten Saetze stehen in U8 der Erstlesung.

| Z. | Aussage | Ergebnis |
|---|---|---|
| 4 | alle Befunde eingearbeitet | fast; B14 und A6 teilweise |
| 33 | es gibt zwei Deutungen | klingt abschliessend, N10 |
| 68 | lokal stabil immer, weil V'(0) = m_Φ² > 0 | haelt, wenn m_Φ² > 0 |
| 71 | klassisch stabil heisst: eine negative Richtung und dQ/dω < 0 | haelt fuer den 3D-Grundzustand (n = 1). Allgemein ist auch n = 0 stabil (§7). Gering |
| 101 | im Kontinuum keine Moden oberhalb des Bandes | haelt, das Band ist nach oben offen |
| 110 | nur im Grenzfall breiter | auch bei kleinem J > 0, N8 |
| 152 | bei jedem Δt <= 0,1 | nur sechs Werte geprueft, N15 |
| 186 | Gradient fast ueberall null | haelt fuer Punktzahlen; "springt" ist falsch, N6 |
| 206 | Anziehung erst ueber Feldrelaxation | haelt nicht, N1 |
| 221 | Literatur: fuer jedes m/M | haelt, Abstract selbst gelesen (N16) |
| 228 | Graph muss ein Wald sein | bei offener Kette von selbst erfuellt: Der Flaechengraph ist ein Pfad, jeder Teilgraph ein Wald. Haelt |
| 243 | K positiv stabil, eine negative Richtung instabil | haelt statisch, ohne gyroskopische Terme, M positiv definit |
| 255 | positive K_eff hinreichend, nicht noetig | haelt |
| 265 | n = 0 stabil, unabhaengig von dQ/dω | haelt (striktes Minimum von H - ωQ ohne die Phasenrichtung) |
| 282 | Energie nur bei autonomer Dynamik | haelt |
| 325 | auf festem Graphen d_H und d_s vorgegeben | haelt fuer den ungewichteten Graphen. Haengt J vom Abstand ab, aendert sich der gewichtete Laplace-Operator mit der Geometrie. Gering |
| 347 | corr(Energie, ν) bei erhaltener Energie nicht definiert | haelt innerhalb eines Laufs |
| 355 | Kennzahlen alle nach Abzug der Symmetriemoden | zu weit, N14 |
| 364 | V5-Aussage nur im Nachtrag v5b | haelt (ERGEBNIS Z. 164-165, Selbstanzeige 3) |
| 431 | ohne aeussere Zeit | nicht fuer alle vier Ansaetze, N3 |
| 442 | Spin 1/2 im Projektmodell nicht moeglich | haelt, Abschnitt 3 |
| 458 | sonst Schritt verkleinern | nicht umsetzbar, N2 |

## 5. Urteil zur Weitergabe

**Quote**
- Gezaehlt sind die 32 Befunde (B1-B14, R1-R8, U1-U8, A11, A12).
- 29 sind erledigt, 2 teilweise (B14, R6), keiner ist offen. A12 entfaellt, weil es Codex' Text betrifft.
- Ausserhalb dieser Zaehlung ist A6 nur teilweise erledigt.
- Die vier Fehler B1-B4 und die schwere Ueberdehnung U1 sind richtig und sachlich gleichwertig erledigt.

**Neue Befunde: 16**
- 1 Fehler: N1, Mechanik der Anziehung.
- 3 mittlere Ungenauigkeiten: N2 (Rechenanweisung), N4 (Reihenfolge), N5 (Festlegung auf T).
- 1 Ueberdehnung gering bis mittel: N3.
- Der Rest ist gering. N13 ist ein nachgerechneter neuer Wert, der stimmt.

**Urteil: mit Auflagen weitergeben.** Kernformeln, Normierung, Massenmatrix, Fenster und Zahlen stimmen. Ein anderes KI-System koennte aber an drei Stellen Falsches lesen oder falsch bauen:

1. **Auflage N1:** Den Satz zur Anziehung berichtigen. Sonst sucht jemand Anziehung aus Feldrelaxation bei abnehmendem J(r), und die gibt es zwischen verbundenen Knoten nicht.
2. **Auflage N2:** §20 Schritt 3 berichtigen. Sonst baut jemand eine Ereignissuche, die doppelte Wechsel still verliert, also den V4-Fehler.
3. **Auflage N5:** In §21 Frage 8 und im Naechsten Schritt offenlassen, ob 11+1 die Kette T oder den Ring R meint, und N fuer T festlegen.

Empfohlen vor der Weitergabe: N4 (Reihenfolge begruenden oder tauschen) und N3 (Satz zur Zeit). Der Rest kann mit der naechsten Fassung kommen.

Die geaenderten Saetze sind kurz. Nach dem Einarbeiten genuegt ein frischer Blick nur auf diese Saetze, keine volle dritte Lesung.

**Grenzen dieser Lesung**
- Nicht geprueft habe ich die Projektzahlen und Beweise (RUNDE-12, -14, -15), Codex' TETRA-RECON-1, das Tetra-Buendel und BEUTEL-1. Sie waren nicht freigegeben.
- arXiv-API: drei Abfragen um 09:34:53, 09:35:02 und 09:35:09 zu den Nummern sowie eine Suche um 09:35:20, alle HTTP 200. Die Abstaende waren 9 s, 7 s und 11 s, kein HTTP 429.
- v2.1 ist unveraendert: sha256 um 09:38:36 erneut 1a2da1ab...434cc.
