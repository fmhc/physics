Urteil: traegt mit Aenderungen (A 0, B 4, C 6). Abgeschlossen 2026-10-04 11:34:52 CEST (date), Dauer 10 min 12 s.

# PAPIER-I-GEGENLESEN-3: Frischer Leser der Fussnote (Fassung 3)

- Pruefer: pruefer-opus (Haus Anthropic), frischer Leser, keiner der beiden frueheren.
- Beginn: 2026-10-04 11:24:40 CEST (date). Zeitbox 20 min.
- Auftrag: RUNDE-37/papier-i-gegenlesen-3/KARTE.md, sha256 b575d0175b94ea86acd100e1f8fb6b09109f028e5402b8112f6a13d4e59d440c.
- Gegenstand: nur der LaTeX-Block (Fussnote) in RUNDE-37/PAPIER-I-ROBUSTHEIT-ENTWURF.md.

## Ergebnis

**Traegt mit Aenderungen.** Kein A-Befund: Ich habe keine Zahl und keine Aussage gefunden, die gegen die Quellen falsch
ist. Vier B-Befunde betreffen Saetze, die mehr sagen als belegt ist oder die ohne Bezugsangabe nicht eindeutig sind:
- B1: "falls faster than any power" ist eine asymptotische Aussage aus sechs Punkten. Das Papier verbietet sich selbst
  solche Schluesse (ME Z. 366).
- B2: Fuer X > 0 fehlt der gerechnete Bereich.
- B3: Bei P fehlen Einfallskanal und Frequenz, und der Wert ist an der Nullstelle resonant ueberhoeht.
- B4: Das Vorzeichen von X ist nicht festgelegt, und es fehlt, welches Vorzeichen die Stencils haben.

Dazu kommen sechs C-Befunde. Die Anforderungen 1, 2, 3 und 5 sind erfuellt, 4 weitgehend (Abschnitt 4).

Kuerzel: E = Entwurf PAPIER-I-ROBUSTHEIT-ENTWURF.md (sha256 a6306a93...), VW = RUNDE-36/v1-weiter/ERGEBNIS.md, VWP =
RUNDE-36/v1-weiter/PLAN.md, VP = RUNDE-37/v1-praezision/ERGEBNIS.md, ME = paper-v42-beta1/stage/main.tex, G2 =
papier-i-gegenlesen-2/GEGENLESEN.md.

## 1. Vorwaerts: Zahl fuer Zahl gegen die Quellen

| Satzteil der Fussnote | Quelle | Befund |
|---|---|---|
| "exploratory single-implementation check without independent replication" | VW Latten L2 "Kein zweites Haus"; VP L2 "Anderer Integrator ... Gleichwert im Modell D auf 1,8e-6 ... Kein zweites Haus" | Inhaltlich richtig. Jede zitierte Zahl stammt aus genau einem Code: -3,7e-3 nur VW, 8,7e-17 und 1,5e-49 nur VP-Kartenmodell. VW und VP sind aber zwei Implementierungen, im Modell D gleich auf 1,8e-6. Das Papier nennt so etwas "single-house" (ME Z. 529). C1 |
| "$X\,\partial_x^4$ ... to the field equation for background and fluctuations" | VWP Z. 13: phi_tt - phi_xx + eps phi_xxxx + U' phi = 0; VP Z. 18 "Kartenmodell (eps im Hintergrund und in den Schwankungen)"; VW Zusatz "Z: Kartenmodell (FD-Hintergrund mit eps)" | Richtig, X = eps. Die Vorzeichenkonvention steht nur implizit im Text, siehe B4 |
| "$\mathcal U(S)=S-S^2+S^3$ ($\beta=1$), not of the main model" | VWP Z. 13 (beta = 1); ME Z. 83 (Hauptmodell beta = 1/2), Z. 368-372 | Richtig |
| "For $X>0$ each side keeps a single open channel" | VWP Z. 43 "eps >= 0 je Seite einer (wie WAND-BETA)", Tabelle Z. 38-41 (bei eps > 0 nur zusaetzliche schnell abklingende Loesungen); VW Kontrollen "Kanalzahl wie im Plan"; ME Z. 325 (eps = 0: "one open and one evanescent channel on each side") | **Richtig gelesen.** Bei X = 0 hat jede Seite einen offenen Kanal: aussen B alt, innen e1. X > 0 fuegt je Komponente nur schnell abklingende Loesungen hinzu (Dispersion 1 + k^2 + X k^4 ist monoton) |
| "the planar transmission zero persists" | VW Ergebnis 2 und V1: Restgroesse 1,7e-17 bis 2,5e-15 (Schwelle 1e-10), beide Varianten, X = 1e-3, 3e-3, 1e-2; E wechselt das Vorzeichen | Richtig, aber nur fuer 0 < X <= 1e-2 gerechnet. B2 |
| "shifted by $-3.7\times10^{-3}X$" | VW Tab. 1, Fussnote: d rho_z/d eps = -3,7486e-3 (zentral aus +-1e-3), zweite Ordnung +5,32e-3 | Richtig, -3,7486 gerundet -3,7. Die Probe: X = 1e-2 ergibt -3,7e-5, Tabelle -3,6964e-5. Gemeint ist rho_z wie in ME Z. 372 (1,77345307180, VW: 1,7734530718065). Die quadratische Korrektur betraegt bei 1e-2 nur 5,3e-7, das sind 1,4 % |
| "truncation ... creates a high-wavenumber branch, $q\simeq\lvert X\rvert^{-1/2}$" | VW Ergebnis 5 (k ~ sqrt(12)/h = abs(eps)^(-1/2) fuer eps = -h^2/12); VP Tabelle: K_A = 10,009, K_B = 9,676 bei abs(X)^(-1/2) = 10 | Richtig, die Abweichung betraegt hoechstens 3,2 % (K_B) |
| "which the stencils used here do not have for an axis-aligned wall" | ME Z. 452 f. (Fuenfpunkt, gewichteter Neunpunkt, Siebenpunkt-Dreieck); G2 Abschnitt 7, Frage 2; Gitterweiten: RUNDE-23/stille-auf-gitter (h = 0,5 bis 0,15, "isotroper 9-Punkt-Stern"), RUNDE-24/stille-gitter-2 (Dreieck h = 0,5 bis 0,2) | Richtig fuer die verwendeten Gitterweiten. Eigene Nachrechnung in Abschnitt 3, Frage 2. C3 |
| "flux fraction transmitted into the new exterior channels is $8.7\times10^{-17}$ at $X=-10^{-2}$" | VP Tabelle P(eps): 8,6866e-17, "P = Flussanteil in A neu + B neu (aussen) bei Einfall mit Fluss 1 im alten Innenkanal e1, an der Nullstelle rho_z von E" | Zahl und Gruppe der Kanaele richtig. Einfallskanal und Frequenz fehlen, B3. Der Wert haengt von der Wahl des Hintergrundschwanzes ab, C5 |
| "falls faster than any power of $\lvert X\rvert$" | VP Ausgleich F1: c = 6,149, Reste <= 0,022 ueber 75 Einheiten in ln P; oertliche Steigungen in 1/sqrt(abs(X)) fast konstant (-6,08 bis -6,12); FK: Reste <= 0,0063 | Die Daten zeigen exp(-c/sqrt(abs(X))) ueber den Faktor 5 in X. Die Aussage ueber "jede Potenz" ist asymptotisch. B1 |
| "($1.5\times10^{-49}$ at $X=-2\times10^{-3}$)" | VP Tabelle: 1,5486e-49 | Richtig gerundet |
| "The planar reduction has no angular coupling" | eindimensionale ODE (VWP Z. 13-25) | Richtig |
| "the lattice itself was not computed" | VW und VP rechnen nur das Kontinuum mit X | Fuer die Pruefung richtig. Im Unterabschnitt stehen aber gerechnete Gitter (ME Z. 448-453), daher missverstaendlich. C2 |

## 2. Rueckwaerts: geglaettete Vorbehalte, zu starke Saetze

1. **Asymptotik aus sechs Punkten (B1).** Die Fussnote formuliert ein Grenzgesetz ohne Einschraenkung. Dieselbe Seite
   des Papiers sagt (ME Z. 365 f.): "Finite-data agreement therefore does not establish an exact asymptotic law."
   VP selbst schreibt nur "Die Form selbst passt gut", VW Ergebnis 4 "Beschreibend, kein Urteil". Aus dem Text kann ein
   Leser schliessen, das Grenzgesetz sei gezeigt.
2. **Resonante Ueberhoehung an der Nullstelle (B3).** VW Tabelle 2 und VWP Z. 151 (r4): Bei rho_z +- 1e-3 ist die
   Amplitude nur 3,7e-11 statt 4,608e-9. Rechenweg: 4,608e-9 / 3,7e-11 = 124,5, im Fluss also ~1,6e4-fach kleiner. Ohne
   die Angabe "at the zero" kann ein Leser 8,7e-17 fuer einen frequenzunabhaengigen Leckwert halten.
3. **Bereich bei X > 0 (B2).** Gerechnet sind nur 1e-3, 3e-3 und 1e-2. "persists" ohne Bereich klingt nach "fuer alle
   X > 0".
4. **Vorzeichen und Gitterbezug (B4).** Das Papier druckt als Bewegungsgleichung nur die Profilgleichung (ME Z. 88,
   f'' + ... = rechte Seite). Wer X f'''' dort links addiert, bekommt das entgegengesetzte Vorzeichen zu VW (VWP Z. 16:
   eps f'''' - f'' + ... = 0). Dann waere X > 0 die gitterartige Erweichung. Nur ueber den Hoch-q-Satz laesst sich der
   Widerspruch aufloesen. Ausserdem sagt die Fussnote nicht, dass die Stencils dem Fall X < 0 entsprechen. Der
   Absatz des Unterabschnitts braucht aber genau diese Verbindung.
5. **Nicht geglaettet, aber weggelassen (C, nur Hinweis):**
   - Gleich viel Fluss geht in die neuen Innenkanaele (VP "P_neu_innen = P_neu_aus ... auf 15 Stellen"). Der
     Gesamtverlust der alten Welle ist also 2P (C4).
   - Die Schwanzwahl ist eine Modellwahl, ihr Einfluss wurde nicht gemessen (VP Selbstanzeige 6). FD-Werte: 9,38e-17
     (A) bzw. 8,81e-17 (B) gegen 8,69e-17, also bis 7,4 %. Zwei Stellen in "8.7" sind etwas genauer als das Modell (C5).
   - Die alte Transmission bleibt auch bei X < 0 auf Rechengrenze null (VW: T_alt(rho_z) = 3,2e-23 bei -1e-2). Fuer das
     gitterrelevante Vorzeichen waere das die eigentliche Robustheitsaussage. Sie fehlt, ist aber nicht falsch
     weggelassen.
6. **Zu stark?** Ausser B1 nicht. "do not have" ist in diesem Zusammenhang gedeckt (Abschnitt 3, Frage 2). "persists"
   ist durch V1 gedeckt, der Bereich fehlt (B2).

## 3. Die drei Unsicherheiten der Leitung

**Frage 1: "falls faster than any power of abs(X)". Gedeckt?** Nur als Befund im gerechneten Bereich, nicht als
Grenzgesetz.
- Eigene Probe mit oertlichen Potenzexponenten p = d ln P / d ln abs(X) aus VP:
  - -1e-2 nach -7e-3: Delta ln P = -48,885 + 36,982 = -11,903, Delta ln abs(X) = ln 0,7 = -0,357, also p = 33,4.
  - -3e-3 nach -2e-3: Delta ln P = -112,389 + 87,287 = -25,102, Delta ln abs(X) = ln(2/3) = -0,405, also p = 61,9.
- Der Exponent waechst also von ~33 auf ~62. Das passt zu exp(-c/sqrt(abs(X))) mit p = (c/2)/sqrt(abs(X)), und keine
  einzelne Potenz beschreibt den Verlauf.
- Der Mechanismus "jenseits aller Ordnungen" ist bekannt (VP L4, [L?]). Damit ist die Aussage plausibel, aber nicht
  gezeigt, und das Papier setzt fuer Grenzgesetze selbst die strengere Latte (ME Z. 366).
- Vorschlag B1 ohne Ausgleichsform, denn Anforderung 5 verbietet sie.

**Frage 2: Stencil-Satz, auch fuer das Dreieck?** In diesem Zusammenhang richtig, allgemein nicht. Eigene Rechnung [M]:
- Fuenfpunkt: Symbol (4/h^2) sin^2(qh/2), monoton bis pi/h. Ast des Polynoms bei q = sqrt(12)/h = 3,46/h > pi/h.
- Kompakter Neunpunkt mit Kanten a und Ecken b: Bei k_y = 0 ist das Symbol (2a + 4b)(1 - cos qh)/h^2. Mit der
  Konsistenz a + 2b = 1 ist es gleich dem Fuenfpunkt, unabhaengig von den Gewichten. Laut RUNDE-23 ist der Stern
  "isotroper 9-Punkt-Stern", also kompakt. Auch der breite Kreuz-Stencil vierter Ordnung waere monoton (Ableitung
  sin(qh)(32 - 8 cos qh)/(12h^2) > 0).
- Dreieck, Normale entlang einer Bindung: Die ebene Reduktion tastet im Abstand h/2 ab. Das Symbol
  (2/(3h^2))[6 - 2 cos qh - 4 cos(qh/2)] steigt bis qh = 4pi/3 auf 6/h^2 und faellt bis qh = 2pi auf 16/(3h^2) = 5,33/h^2.
  Ein zweiter Ast entsteht nur fuer kappa^2 > 5,33/h^2.
  - Groesstes kappa^2 hier: Aussenkanal B, (rho_z + omega)^2 - 1 = (1,7735 + 0,8660)^2 - 1 = 6,967 - 1 = 5,967.
  - Daraus h > sqrt(5,33/5,967) = sqrt(0,893) = 0,945.
  - Normale senkrecht zur Bindung: Symbol (16/(3h^2)) sin^2(sqrt(3) qh/4), monoton bis zum Zonenrand. Dort entsteht fuer
    kein h ein zweiter Ast.
  - Das Papier rechnet das Dreieck bei h = 0,5 bis 0,2 (RUNDE-24/stille-gitter-2 Z. 12). Dafuer stimmt der Satz.
  - Der Polynom-Ast des Dreiecks (X = -h^2/16) liegt bei q = 4/h. Dort hat das Gitter kappa^2 ~ 6/h^2, nicht ~6.
- Ergebnis: Fuer "the stencils used here" ist der Satz richtig, als allgemeine Stencil-Aussage nicht (Dreieck,
  h >= 0,95 entlang einer Bindung). "axis-aligned" ist beim Dreiecksgitter nicht definiert. C3.

**Frage 3: "each side keeps a single open channel" bei X > 0. Richtig gelesen?** Ja. Belege: VWP Z. 43 ("eps >= 0 je
Seite einer"), Kanaltabelle VWP Z. 38-41, VW Kontrollen ("eps > 0 aussen ein laufender Kanal"). Bei X = 0: ME Z. 325
fuer das Hauptmodell und VWP "wie WAND-BETA" fuer beta = 1. Physikalisch ist 1 + q^2 + X q^4 fuer X > 0 monoton, die
neuen Wurzeln sind rein abklingend (q ~ +-i X^(-1/2)). VP Kontrollen bestaetigen das bei +3e-3: "Neue offene Kanaele
gibt es dort nicht."

## 4. Anforderungen 1 bis 5 (Abschnitt 7, papier-i-gegenlesen-2)

| Nr | Anforderung (G2) | Erfuellt? |
|---|---|---|
| 1 | Modell: ebene Reduktion, beta = 1, nicht Hauptmodell | **ja** (Satz 1) |
| 2 | X > 0: Nullstelle bleibt exakt, ein offener Kanal je Seite, Verschiebung -3,7e-3 X | **ja**, nur der Bereich 0 < X <= 1e-2 fehlt (B2) |
| 3 | X < 0: Hoch-q-Ast durch Abschneiden, den die Stencils bei achsparalleler Wand nicht haben; Leck 8,7e-17 bei -1e-2, schneller als jede Potenz (1,5e-49 bei -2e-3) | **ja, woertlich.** Ich rate aber gegen den Wortlaut der Anforderung selbst, das Grenzgesetz abzuschwaechen (B1) und Einfall und Frequenz zu nennen (B3) |
| 4 | Keine Winkelkopplung, Gitter nicht gerechnet, explorativ, kein zweites Haus; Provenienzeintrag | **weitgehend.** "kein zweites Haus" steht als "single-implementation ... without independent replication" da (C1). "lattice not computed" ist im Unterabschnitt missverstaendlich (C2). Der Provenienzeintrag steht als Angebot ausserhalb des LaTeX-Blocks (E "Fuer Codex' Provenienztabelle"), nicht geprueft |
| 5 | Nicht in die Fussnote: Ausgleichsformen, d, p, K, Schwanz, 27 %, Faktor 2 | **ja.** Nichts davon steht drin; q ist die Ast-Wellenzahl aus Anforderung 3, nicht das K des Ausgleichs |

## 5. Form (LaTeX, Einpassung)

- **Klammern:** Alle 12 $-Paare sind geschlossen, ebenso alle {}-Gruppen. \footnote{...} schliesst nach "computed.".
  \mathcal U wie in ME Z. 83.
- **Symbole:** In ME kommen weder "$q", "q_", "\nu" noch "\Omega" vor (grep). q ist also frei, X bleibt Platzhalter
  (Leitung). sections/LITERATURE.tex habe ich nicht geprueft.
- **Laenge:** rund 125 Woerter. Als Fussnote vertretbar, mit B1 bis B4 werden es rund 150.
- **Einpassung:** Der Bezug "the stencils used here" setzt den Anker im Unterabschnitt voraus (ME Z. 446-466), am
  besten nach "a seven-point triangular stencil." (Z. 453) oder am Absatzende. "the planar transmission zero" verweist
  auf eine Stelle ausserhalb des Unterabschnitts (Z. 368-372, beta = 1), siehe C6.

## 6. Befunde A/B/C mit Vorschlag

### A (muss)

Keine.

### B (sollte)

**B1. Grenzgesetz aus sechs Punkten.** Fundstelle: "falls faster than any power of $|X|$".
- Quelle: VP F1, gerechnet nur -1e-2 bis -2e-3. Das Papier schreibt selbst (ME Z. 366): "Finite-data agreement
  therefore does not establish an exact asymptotic law."
- Vorschlag a (beschreibend, ohne Ausgleichsform, Anforderung 5 bleibt gewahrt): "... is $8.7\times10^{-17}$ at
  $X=-10^{-2}$ and drops steeply with $|X|$ ($1.5\times10^{-49}$ at $X=-2\times10^{-3}$)."
- Vorschlag b: "... and, over the computed range, is consistent with a decay faster than any power of $|X|$
  ($1.5\times10^{-49}$ at $X=-2\times10^{-3}$)."

**B2. Bereich bei X > 0.** Fundstelle: "For $X>0$ each side keeps ... persists". Quelle: VW V1, nur X = 1e-3, 3e-3,
1e-2.
- Vorschlag: "For $0<X\le10^{-2}$ each side keeps a single open channel, and the planar transmission zero persists, its
  frequency shifted by $-3.7\times10^{-3}X$."

**B3. P ohne Einfall und Frequenz.** Fundstelle: "the flux fraction transmitted into the new exterior channels".
- Quelle: VP Tabellenvermerk (Einfall Fluss 1 im alten Innenkanal e1, an rho_z). VW Tabelle 2: bei rho_z +- 1e-3 ist
  der Fluss ~1,6e4-fach kleiner.
- Vorschlag: "for unit flux incident in the original interior channel at the shifted zero, the fraction transmitted into
  the new exterior channels is ..."

**B4. Vorzeichen und Gitterbezug.** Fundstelle: "$X\,\partial_x^4$, to the field equation" und "For $X<0$".
- Quelle: VWP Z. 13-16. ME druckt nur die Profilgleichung (Z. 88), dort kehrt "addieren" das Vorzeichen um. Die
  axiale Reduktion der Stencils hat X = -h^2/12 (Fuenf- und Neunpunkt) bzw. -h^2/16 (Dreieck) [M, eigene
  Taylor-Rechnung].
- Vorschlag (Symbol fuer die Frequenz waehlt Codex, hier nu): "... to the field equation, so that vacuum plane waves
  obey $\nu^2=1+q^2+Xq^4$, for background and fluctuations ..." sowie "For $X<0$, the sign of the stencils' leading
  correction ($X=-h^2/12$ for an axis-aligned wall on the square stencils), the truncation ..."

### C (kann)

- **C1.** Statt "single-implementation check without independent replication" den Begriff des Papiers verwenden
  (ME Z. 529): "In an exploratory single-house check without independent replication, ..."
- **C2.** Statt "and the lattice itself was not computed": "and this check does not compute on a lattice." Der
  Unterabschnitt berichtet gerechnete Gitter.
- **C3.** Statt "for an axis-aligned wall": "for a wall aligned with a lattice direction at the spacings used
  ($h\le0.5$)". Grund: Das Dreieck haette entlang einer Bindung ab h ~ 0,95 einen zweiten Ast (Abschnitt 3, Frage 2).
- **C4.** Wahlweise anfuegen: ", and an equal fraction is reflected into the new interior channels". Quelle: VP
  "P_neu_innen = P_neu_aus".
- **C5.** Wahlweise "$\approx9\times10^{-17}$" statt "$8.7\times10^{-17}$". Grund: Schwanzwahl, FD 9,38e-17 bzw.
  8,81e-17 (VP Vermerk PR0). Sonst so lassen.
- **C6.** Querverweis auf die beta = 1-Nullstelle: "... persists (the zero $\rho_z\simeq1.7735$ of
  Sec.~\ref{...})". Dann ist auch klar, dass "shifted" rho_z meint.

## Einfach gesagt

Die Fussnote sagt im Kern das Richtige. Alle Zahlen stimmen mit den Rechnungen ueberein, und der Satz ueber die Gitter
gilt fuer die Gitter, die das Papier wirklich benutzt. Zwei Stellen sagen aber mehr, als gerechnet wurde. "Faellt
schneller als jede Potenz" ist ein Gesetz fuer beliebig kleine Werte, wir haben aber nur sechs Punkte. Und bei positivem
X fehlt, bis wohin geprueft wurde. Ausserdem sollte die Fussnote sagen, welches Vorzeichen ein echtes Gitter hat und bei
welcher Frequenz das winzige Leck gemessen wurde. Das sind kleine Ergaenzungen, danach kann die Fussnote an Codex gehen.
