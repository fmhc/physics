Urteil: traegt mit Aenderungen (2 A, 3 B, 9 C); Langfassung erst nach A1 und A2 weitergeben; Empfehlung Fussnote oder weglassen.

# PAPIER-I-GEGENLESEN-2: Frischer Leser, Fassung 2 des Robustheitsabsatzes (letzte Schicht)

- Pruefer: pruefer-opus (Haus Anthropic, frischer Leser, nicht der Leser von Fassung 1).
- Beginn: 2026-10-04 11:05:47 CEST (date).
- Auftrag: RUNDE-37/papier-i-gegenlesen-2/KARTE.md.
- Kennzeichen: [S] an der Quelle gelesen, [M] Rechnung (im Kopf, Rechenweg gezeigt), [ES] eigener Schluss.

## 1. Ergebnis

**traegt mit Aenderungen** (2 A, 3 B, 9 C). In der Langfassung nicht an Codex weitergeben, bevor A1 und A2 behoben sind.
Empfehlung zur Form: Fussnote mit den Anforderungen aus Abschnitt 7, Frage 3, sonst weglassen.

- Zahlen: 25 gepruefte Aussagen, 23 tragen (15 ohne, 8 mit Anmerkung), 2 sind falsch dargestellt (Abschnitt 2). Jede
  Zahl selbst ist richtig gelesen.
- **A1** "the amplitude of the background tail (below) follows the same exponential": Der Schwanz folgt exp(-d k0)
  (Amplitude, eigene Wellenzahl), P folgt exp(-2dK). Zusatz der Leitung.
- **A2** Faktor 1,8 bis 2,2 und "at most 0.3 %" stehen grammatisch bei "earlier double-precision runs with boundary-fixed
  tails", stammen aber aus den jetzigen Taylor-Laeufen mit schwanzfreiem Modell D. Woertlich aus Vorschlag A1 des ersten
  Lesers.
- **B1** d wandert mit der Exponentenform (2,1 % mit abs(X)^(-1/2)); **B2** "the zero" bei X < 0 undefiniert; **B3** die
  gewaehlte Hintergrundloesung ist nur auf dem Rechengebiet eine Wand.
- Umsetzung Fassung 1 (Abschnitt 6): 17 von 21 Befunden richtig, 4 teilweise (A1, B5, B7, C6), 0 falsch.
- Gezielte Fragen (Abschnitt 7): Schwanzzahl richtig gelesen, "same exponential" falsch. Stencil-Satz gilt fuer alle drei
  Stencils des Papiers bei achsparalleler Wand; "artefact" ist nicht zu stark, "nearest-neighbour" ist zu weit fuer die
  Formel (C6). Laenge: 503 Woerter gegen 186 im ganzen Unterabschnitt.
- Zeit: Beginn 11:05:47, Ergebnisabschnitt geschrieben nach date 11:21:43 CEST, also 15 min 56 s bis hier
  [M: 21:43 - 05:47 = 15:56]. Letzte inhaltliche Aenderung vor date 11:22:43 CEST, gesamt 16 min 56 s
  [M: 22:43 - 05:47 = 16:56]; Zeitbox 35 min eingehalten.

## 2. Vorwaertspruefung (Zahl fuer Zahl, Aussage fuer Aussage)

Gegenstand: LaTeX-Block in RUNDE-37/PAPIER-I-ROBUSTHEIT-ENTWURF.md, Z. 25-78 (im Folgenden "E Z."). VW = RUNDE-36/v1-weiter,
VP = RUNDE-37/v1-praezision, WB = RUNDE-24/wand-beta, ME = Papier I stage/main.tex. Bericht zu Fassung 1 erst nach
diesem Abschnitt gelesen.

| Nr | Aussage (E Z.) | Quelle | Urteil |
|---|---|---|---|
| V1 | "single-implementation ... no independent replication" (26 f.) | [S] VP L2 Z. 172-175: anderer Integrator und anderes Zahlformat als VW, Gleichwert Modell D 1,8e-6; kein zweites Haus | Kern richtig; "single-implementation" stimmt nur fuer die Taylor-Rechnung, es gab zwei Implementierungen eines Autors (C1 neu) |
| V2 | U = S - S^2 + S^3, beta = 1, omega_min = sqrt3/2, nicht Hauptmodell; rho_z = 1.7734530718 (28-30) | [S] VP PLAN Z. 14 f.; WB ERGEBNIS Z. 17; VW .urteile.V0.werte.rho_z_A = 1.773453071806469 (jq); ME Z. 369-372 (1.77345307180, dort ebenfalls omega_min) | richtig |
| V3 | X d_x^4 in Hintergrund und Schwankungen (31-33) | [S] VP PLAN Z. 14-16; fuer X > 0 VW Kontrollen Z. 103 (max abs(f - f0) linear in eps, Hintergrund also mit X) | richtig |
| V4 | E^2 = 1 + q^2 + X q^4 (34) | [M] phi_tt - phi_xx + X phi_xxxx + phi = 0 mit e^{i(qx - Et)}: -E^2 + q^2 + X q^4 + 1 = 0; [S] VP Selbstanzeige 2 Z. 194 | richtig |
| V5 | Steigung -3.749e-3, beidseitig (34 f.) | [S] VW Z. 80, Tab. 1 Z. 70, 72; [M] (-3,743237e-6 - 3,753878e-6)/(2e-3) = -7,497115e-6/2e-3 = -3,7486e-3 | richtig |
| V6 | X = 1e-3, 3e-3, 1e-2: kein neuer Kanal, Nullstelle bleibt, Rest < 3e-15 relativ zu rho_z + 1e-3, double (35-38) | [S] VW .urteile.V1.werte[].restgroesse_rel (jq): Maximum 2,505e-15; Definition VW Z. 76 f.; Kanalzahl VW Z. 112 | richtig. VP PLAN Z. 46 f. [M]: bei einem offenen Kanal je Seite ist T = 0 bei E = 0 exakt; "persists exactly" waere belegt (C) |
| V7 | X < 0: je Seitenband ein neuer Ast ~abs(X)^(-1/2), zwei neue Kanaele je Seite (39-41) | [S] VP PLAN Z. 18 f. (aussen B alt, A neu, B neu; innen e1 alt, e1 neu, e2 neu); [M] abs(X) q^4 - q^2 + k^2 = 0 gibt q^2 = [1 -+ (1 - 4 abs(X) k^2)^(1/2)]/(2 abs(X)), "+"-Ast ~ 1/abs(X) | richtig |
| V8 | alte Innenwelle bei rho_z leckt, "only non-perturbatively" (41 f.) | [S] VW Z. 20-24: an der reellen Nullstelle von E bleibt eine Mischung aus altem und neuen Innenkanaelen exakt total reflektiert; nur die reine alte Welle leckt. VP Z. 36-41 Bedeutung als [H] | Inhalt richtig, aber was "the zero" bei X < 0 ist, sagt der Text nirgends (B2 neu); "only non-perturbatively" ist Schluss aus Ausgleichen ueber abs(X)^(-1/2) = 10 bis 22 (C2 neu) |
| V9 | Taylor, Festkomma, 133 und 200 bit, ~40 und 60 Stellen (42-44) | [S] VP PLAN Abschn. 3 und Konfigurationstabelle Z. 75-79; [M] 133 x 0,30103 = 40,0; 200 x 0,30103 = 60,2 | richtig (Festkomma-Skala intern bits + 20, VP PLAN Z. 59; muss nicht ins Papier) |
| V10 | P von 8.69e-17 (-1e-2) bis 1.55e-49 (-2e-3), Einfall Fluss 1 im alten Innenkanal; gleicher Anteil in die neuen Innenkanaele (44-48) | [S] VP Tabelle Z. 86, 91, 93, 95 (P_neu_innen = P_neu_aus auf 15 Stellen) | richtig |
| V11 | ln P auf mindestens 12 Stellen unter Genauigkeit, Schritt, Gebiet (48 f.) | [S] VP Kontrollen Z. 123-130: Genauigkeit >= 16 Stellen, Schritt 20 Stellen, Gebiet 7,3e-13 relativ (nur -2e-3, L 85 gegen 70; -1e-2 nachtraeglich 6,6e-18) | richtig (schwaechste Probe zaehlt) |
| V12 | Form ln P = a + p ln abs(X) - 2dK, sechs Punkte, Reste < 0.007 (49 f.) | [S] VP Z. 109; auswertung.json .ausgleich.FK_K_B.max_rest = 0,00629 | richtig |
| V13 | K^2 = [1 + (1 - 4 abs(X) k^2)^(1/2)]/(2 abs(X)), k aus eq:channels bei rho_z (51 f.) | [S] VP PLAN Z. 99 (K_B mit mu_B = 1 - (rho_z + om)^2); ME Z. 114-119 (k^2 = (omega + rho)^2 - 1, offener Kanal A). [M] X = -1e-2: k^2 = 2,63952^2 - 1 = 5,96706; 1 - 0,04 x 5,96706 = 0,761318; Wurzel 0,872535; K^2 = 1,872535/0,02 = 93,627; K = 9,6761 = VP-Tabelle Z. 86 | richtig. Achtung Bezeichnung: VP nennt das offene Seitenband "B", das Papier "A" (ME Z. 119). Der Entwurf vermeidet die Buchstaben zu Recht; "K ... is the new branch" meint "is the wavenumber of the new branch" (C3 neu) |
| V14 | Anteil 69 bis 87 % (52 f.) | [S] VP Tabelle Z. 86-91: 87,4 % (-1e-2) bis 69,4 % (-2e-3); Gegenrechnung Zusatz Z. 156: A neu 12,6 bis 30,6 % | richtig |
| V15 | d = 3.1328, 0.28 % unter pi (53) | [S] auswertung.json FK_K_B.d = 3,1327843, d/pi - 1 = -0,2804 %; [M] 3,14159 - 3,13278 = 0,00881, /3,14159 = 0,280 % | richtig |
| V16 | Polabstand pi, Profil S = (1/2)[1 + exp x]^(-1), S = f^2 (53-55) | [S] VP PLAN Z. 15 (f(-inf) = sqrt(1/2)), Z. 40 (f0); ME Z. 293 (beta = 1). [M] 1 + e^x = 0 bei x = i pi (2n+1), naechste Pole Abstand pi; Innenseite x -> -inf | richtig |
| V17 | kanalweise 0.35 und 0.42 % unter pi (55 f.) | [S] VP Zusatz Z. 151 f.; [M] (3,14159 - 3,13058)/3,14159 = 0,350 %; (3,14159 - 3,12840)/3,14159 = 0,420 % | richtig; Zuordnung (0,35 % offenes, 0,42 % geschlossenes Seitenband) fehlt (C4 neu) |
| V18 | "amplitude of the background tail (below) follows the same exponential with d 0.21 % above pi" (56 f.) | [S] VP Z. 28 f.: "Der Schwanz des Hintergrunds selbst folgt exp(-d k0) mit d = pi + 0,21 %"; Z. 159: ln T = a + q ln abs(eps) - d k0, d = 3,14812, q = -0,35, Rest 0,0006; Z. 96: T = Amplitude der Mode e^{i k0 x} bei x = +70, k0 = 10,012 bis 22,366. [M] (3,14812 - 3,14159)/3,14159 = 0,208 %. [M] k0 ist der neue Ast bei der Hintergrundfrequenz: k0^2 = [1 + (1 + 4 abs(X) kappa0^2)^(1/2)]/(2 abs(X)), kappa0^2 = 1 - omega^2 = 1/4; bei -1e-2: (1 + 1,0049876)/0,02 = 100,249, k0 = 10,0125 = VP | Zahl richtig gelesen, Form falsch: P folgt exp(-2dK) (Fluss, Wellenzahl K), T folgt exp(-d k0) (Amplitude, Wellenzahl k0). "the same exponential" ist um den Faktor 2 und in der Wellenzahl falsch (A1 neu) |
| V19 | p schwach bestimmt, -0.4 bis -2.0 je nach Exponentenform (58 f.) | [S] VP Z. 40; Z. 107 (F1: q = -0,389), Z. 109 (FK: q = -2,005); Z. 115 f. | richtig; aber d haengt mit p zusammen (B1 neu, Abschnitt 3) |
| V20 | Schwanz der Ordnung exp(-pi k0), Hintergrund nur bis auf ihn definiert, Loesung ohne Innenschwanz, Abhaengigkeit nicht gemessen (59-62) | [S] VP PLAN Z. 26-34; Selbstanzeige 6 Z. 210-213; T e^{pi k0} = 10,3 bis 16,8 (Z. 160) | richtig ("of order" im exponentiellen Sinn; Vorfaktor 10 bis 17) |
| V21a | frueher double, randfixierte Schwaenze, P(-1e-2) bis 27 % (63 f.) | [S] VP Vermerk PR0 Z. 54 f.; VW Z. 117; [M] (4,61/4,09)^2 = 1,1271^2 = 1,270 | richtig |
| V21b | "and removing the X term from the background changed P by a factor of 1.8 to 2.2, while the channel-wise fitted pole distances moved by at most 0.3 %" (64-66), grammatisch an "In earlier double-precision runs" gebunden | [S] VP Zusatz Z. 163-167 (Modell D, Taylor, -1e-2 bis -2e-3: 1,83 bis 2,22); Selbstanzeige 6 Z. 212 f.; kanalweise Ausgleiche gibt es nur in VP Zusatz Z. 149-154. Die frueheren double-Laeufe gaben FD/f0 = 1,6 bis 2,0 (VW Z. 158; [M] 8,14/4,95 = 1,644; 7,27/4,30 = 1,691; 9,38/4,75 = 1,975) und keine kanalweisen Polabstaende. [M] Verschiebung Karte -> D: A neu 3,12840 -> 3,12637 (0,065 %), B neu 3,13058 -> 3,12169 (0,283 %) | Zahlen richtig, Zuordnung falsch: Faktor und 0,3 % stammen aus den jetzigen Taylor-Laeufen, nicht aus den frueheren double-Laeufen; Modell D hat ueberhaupt keinen Schwanz, also auch keinen randfixierten (A2 neu) |
| V22 | Hauptmodell beta = 1/2: S = [1 + exp(sqrt2 x)]^(-1), Pole pi/sqrt2, Exponent um sqrt2 kleiner, nicht gerechnet (66-69) | [S] ME Z. 323 f.; VW Z. 155 f. [M] sqrt2 x = i pi gibt x = i pi/sqrt2. [M] gleiches K vorausgesetzt: ME Z. 327 rho_z = 1,52415, omega = 0,70711: k^2 = 2,23126^2 - 1 = 3,9785 (statt 5,967); bei X = -1e-2 K = 9,790 statt 9,676, Verhaeltnis der Exponenten sqrt2 x 0,988 = 1,398 | richtig als Hypothese; "smaller" heisst "kleiner im Betrag, ungefaehr um sqrt2" (C5 neu) |
| V23 | Naechste-Nachbar-Stencil, E^2 = 1 + (4/h^2) sin^2(qh/2), ein Ast in der Brillouin-Zone, Hoch-q-Kanal Artefakt der Abschneidung (69-74) | eigene Rechnung, siehe Abschnitt 7 Frage 2 | Kern richtig fuer alle drei Stencils des Papiers bei achsparalleler Wand (Abschnitt 7); Formulierung C6 neu |
| V24 | keine Winkelkopplung, anisotroper Mechanismus nicht darstellbar (74-76) | [S] ME Z. 451-458 (cos 4 theta, cos 6 theta; h^4 und h^8) | richtig |

Zwischenstand (date 11:15:13, nach dem Schreiben dieser Tabelle; Zaehlung beim Abschluss berichtigt): 25 Zeilen, davon 15
richtig ohne Anmerkung, 8 richtig mit Anmerkung (V1, V6, V8, V13, V17, V19, V22, V23), 2 falsch dargestellt (V18,
V21b), beide mit richtig gelesenen Zahlen.

## 3. Rueckwaertspruefung (Vorbehalte der Quellen)

Von den Quellen zum Text: Welcher Vorbehalt fehlt oder ist geglaettet?

| Nr | Vorbehalt in der Quelle | In Fassung 2 | Bewertung |
|---|---|---|---|
| R1 | d haengt an der Exponentenform und an p: F1 (fuehrende Ordnung abs(X)^(-1/2)) gibt c/2 = 3,0746, also -2,13 % (PR1 nicht eingetroffen, VP Z. 21 f., 107); FK mit p = 0 gibt -4,34 % (Z. 110); PR2 "knapp", "teils Mischungsglueck [H]" (Z. 49, 70-72); alle Ausgleiche zeigen dasselbe Vorzeichenmuster der Reste, Ursache offen (Z. 112-114) | nur d = 3.1328 (-0,28 %) aus der besten Form; p "poorly constrained", ohne dass gesagt wird, dass d mit p wandert | geglaettet (B1). Die 0,28 % sind ein Ausgleichswert einer Form, keine Messunsicherheit von d. Belegt ist "pi auf 0,2 bis 0,5 % mit der genauen Kanalwellenzahl, 2 % mit der fuehrenden" |
| R2 | Kanalweise Ausgleiche und Schwanzausgleich sind Zusatz, "beschreibend, kein Urteil", nach dem Einfrieren geschrieben (VP Z. 9 f., 145, Selbstanzeige 4) | ohne Kennzeichnung neben dem vorab festgelegten FK-Ausgleich | fehlt (Teil von B1). Das Papier kennzeichnet nachtraegliche Auswertungen sonst selbst (ME Z. 384-386: "adaptively specified follow-up runs") |
| R3 | Bei X < 0 bleibt an der reellen Nullstelle von E eine Mischung aus altem und neuen Innenkanaelen exakt total reflektiert (VW Z. 20-22 [M]); rho_z(X < 0) ist diese Nullstelle (VP PLAN Z. 20) | "On both sides of X = 0 the zero moves ..." und "leaks ... at rho_z", ohne zu sagen, welche Nullstelle bei X < 0 gemeint ist | Luecke (B2). Ohne den Satz liest man "the zero" bei X < 0 als Nullstelle der alten Transmission, die es dort nicht gibt |
| R4 | Der gewaehlte Hintergrund (instabile Mannigfaltigkeit von f_c) traegt aussen den Schwanz T und dazu einen wachsenden Anteil ~ T^2 e^{x/2}, weil H = 0 erhalten ist und der Schwanz H > 0 traegt (VP PLAN Z. 35 f. [M]); bei -1e-2 und L = 80 schon 6,6e-6, ln P trotzdem auf 6,6e-18 gleich (VP Z. 129 f.) | "we used the solution without an interior tail" | geglaettet (B3). Die gewaehlte Loesung ist keine beschraenkte Wand auf der ganzen Geraden, sondern nur auf dem Rechengebiet definiert. Belegt ist nur die Unempfindlichkeit von P gegen L = 60 bis 85 |
| R5 | Bei X > 0 ist die Nullstelle nach VP PLAN Z. 46 f. [M] exakt (ein offener Kanal je Seite); die Flussbilanz der X > 0-Laeufe war nur 1e-8 bis 4,5e-8 (VW Selbstanzeige 5) | "persists (transmitted flux at the zero below 3e-15 ...)" | nicht geglaettet. [ES] Die 3e-15 liegen sieben Groessenordnungen unter dem Flussbilanzfehler dieser Laeufe (4,5e-8); sie sind mit "exakt null plus Rundungsrauschen" vereinbar und tragen die Aussage erst zusammen mit dem Abzaehlargument. Vorschlag C7 |
| R6 | Faktor ~2 zu Modell D enthaelt auch den glatten X-Anteil des Hintergrunds, nicht nur den Schwanz (VP Selbstanzeige 6 Z. 212 f.) | "removing the X term from the background" | woertlich richtig, steht aber direkt nach "dependence ... on this choice was not measured" und wird so als Mass der Schwanzabhaengigkeit gelesen; im Vorschlag zu A2 mit erledigt |
| R7 | VW-Vorbehalt Z. 40-42: ob ein echtes Gitter denselben Kanal oeffnet, "ist damit nicht gezeigt" | Stencil-Satz geht darueber hinaus | zulaessig, weil per Schreibtischrechnung belegbar (Abschnitt 7, Frage 2); keine Glaettung, aber Evidenzart nennen (C6) |
| R8 | PR0 nicht eingetroffen: P(-1e-2) liegt 7,4 % unter dem gewerteten frueheren Wert, 1,4 % unter Variante B (VP Z. 31-33) | nicht erwaehnt | vertretbar; die Ursache (andere Schwanzwahl) steht im 27-%-Satz. Kein Befund |

## 4. Form (LaTeX, Notation, Laenge, Nutzen)

Gepruefte Fassung: PAPIER-I-ROBUSTHEIT-ENTWURF.md sha256 1d3f5c6a5e8870e48ce4a5b14604d17c73d2464089f77ceb98f7f411e663937c
(von mir gemessen); Fassung 1 .bak-fassung1 sha256 1aca386c... (stimmt mit der Angabe im Entwurf).

**LaTeX [S]:**
- Dollarzeichen: In E Z. 25-78 hat jede Zeile eine gerade Zahl von $ (Probe `sed -n '25,78{s/[^$]//g;s/\$\$//g;/./=;/./p}'`
  ohne Ausgabe); kein Mathe-Ausdruck laeuft ueber das Zeilenende.
- Befehle Standard: \paragraph, \mathcal, \omega_{\min}, \sqrt3, \partial_x, \times, \simeq, \ln, \exp, \sin, \tfrac,
  \eqref, \,\%. \eqref{eq:channels} existiert (ME Z. 114). Kommentarzeilen mit %.
- Satzbild: "$d$ $0.21\,\%$ above $\pi$" (E Z. 57) setzt zwei Mathegruppen nebeneinander; liest sich als "d 0.21 %".

**Notation gegen das Papier [S]:**
- X ist Platzhalter; epsilon (ME Z. 289), omega, k (ME Z. 115) sind belegt. Richtig so.
- E (Laborfrequenz, ME Z. 127), k aus eq:channels, omega_min (ME Z. 370), rho_z (ME Z. 327, 372), h (ME Z. 373, 452)
  passen.
- k_0 (Schwanzwellenzahl) steht optisch neben kappa_0 aus eq:channels (ME Z. 117), das hier gerade in k_0 eingeht
  ([M] k_0^2 = [1 + (1 + 4 abs(X) kappa_0^2)^(1/2)]/(2 abs(X))). Verwechslungsgefahr (C9).
- Die Ausgleichskonstante a kollidiert mit der Seitenbandfunktion a(r) (ME Z. 99) (C9).
- "static wall": das Papier sagt "stationary background" (ME Z. 85); der Q-Ball-Hintergrund rotiert mit e^{i omega t} (C9).
- "nearest-neighbour stencil": Das Papier nennt "five-point square", "weighted nine-point square" und "seven-point
  triangular" (ME Z. 452 f.). Auch der Dreiecks-Stencil ist ein Naechste-Nachbar-Stencil, hat aber eine andere Formel
  (C6).

**Laenge und Nutzen [S][M][ES]:**
- [M] Der LaTeX-Block hat 503 Woerter (E Z. 25-76, wc -w), der ganze Unterabschnitt im Papier 186 (ME Z. 446-467).
  503/186 = 2,7: Der Zusatz waere fast dreimal so lang wie der Abschnitt, an den er angehaengt wird.
- Inhaltlich sagt der Absatz am Ende selbst, dass er weder das Hauptmodell (beta = 1, pi/sqrt2 nicht gerechnet) noch
  das Gitter ("constrains the continuum model, not the lattice itself") noch den anisotropen Mechanismus des Abschnitts
  ("cannot represent") betrifft. Drei von vier Schlusssaetzen sind Abgrenzungen.
- [ES] Der Teil, der dem Abschnitt etwas bringt, ist kurz: Ein isotroper Viertordnungsterm verschiebt die ebene Nullstelle
  nur (X > 0 exakt), und der Leckkanal bei X < 0 existiert auf den Stencils des Papiers nicht. Das passt zur Deutung des
  Abschnitts, dass die Breiten aus dem anisotropen Anteil kommen, beweist sie aber nicht.
- Ausgleichsformen, K-Definition, kanalweise d, Schwanzausgleich, 27 % und Faktor 2 sind Belege fuer eine Aussage
  ueber ein Modell, das das Papier sonst nicht verwendet. Sie gehoeren, wenn ueberhaupt, in die Provenienz (ME ab Z. 517).
  Genau in diesen Detailsaetzen sitzen beide A-Befunde und B1, B3.
- Empfehlung zur Form: Abschnitt 7, Frage 3.

## 5. Befunde A/B/C mit Vorschlag im Wortlaut

Gelten nur, falls der Absatz in dieser Laenge bleibt. Bei der empfohlenen Kurzform (Abschnitt 7, Frage 3) entfallen A1,
A2, B1, B3, C3, C4 mit den gestrichenen Saetzen.

### A (muss vor Weitergabe geaendert werden)

**A1. "follows the same exponential" ist falsch.** E Z. 56 f.; Zusatz der Leitung (der Vorschlag B5 zu Fassung 1 hatte
nur "the background tail 0.21 % above").
- [S] VP Z. 159: Ausgleich ln T = a + q ln abs(eps) - d k0; Z. 96: T ist die Amplitude der Mode e^{i k0 x} des
  Hintergrunds, k0 = 10,012 bis 22,366. Z. 28 f.: "folgt exp(-d k0) mit d = pi + 0,21 %".
- [M] P folgt exp(-2dK) (Fluss, K = 9,676 bis 22,225), T folgt exp(-d k0) (Amplitude, eigene Wellenzahl k0, siehe V18).
  Gleich ist nur die Rolle von d. Vor "(below)" kennt der Leser nur exp(-2dK); er liest also den falschen Faktor 2 und
  die falsche Wellenzahl.
- Vorschlag: Schwanzausgleich aus E Z. 56 f. streichen und in den Schwanzsatz E Z. 59 f. ziehen:
  "For $X<0$ the stationary wall itself carries an oscillatory tail of wavenumber $k_0\simeq|X|^{-1/2}$ whose amplitude
  follows $\exp(-dk_0)$ with $d$ exceeding $\pi$ by $0.21\,\%$ (post hoc fit over the same six points), so the
  background is defined only up to this tail; ..."

**A2. Faktor 1,8 bis 2,2 und "at most 0.3 %" sind den falschen Laeufen zugeschrieben.** E Z. 63-66; woertlich aus
Vorschlag A1 zu Fassung 1 uebernommen.
- [S] Beide Zahlen stammen aus den jetzigen Taylor-Laeufen: Modell D gegen Kartenmodell 1,83 (-1e-2) bis 2,22 (-2e-3)
  (VP Z. 163-167, Selbstanzeige 6 Z. 212 f.); kanalweise Ausgleiche gibt es nur dort (VP Z. 149-154).
- [S][M] Die frueheren double-Laeufe gaben FD/f0 = 1,64, 1,69, 1,97 bei -2e-2, -1,5e-2, -1e-2 ([M] 9,38/4,75 = 1,975) (VW Z. 137-139, 158) und
  keine kanalweisen Polabstaende. Modell D hat keinen Schwanz, also auch keinen randfixierten.
- [S] Der Faktor misst Schwanz und glatten X-Anteil zusammen (VP Selbstanzeige 6), nicht die Schwanzwahl.
- Vorschlag: "In earlier double-precision runs with boundary-fixed tails, $P(X=-10^{-2})$ changed by up to $27\,\%$ with
  the position of the boundary. In the present runs, removing the $X$ term from the background, which removes the tail
  together with the smooth $O(X)$ change of the profile, changed $P$ by a factor of 1.8 to 2.2, while the channel-wise
  fitted pole distances moved by at most $0.3\,\%$."

### B (sollte)

**B1. Die 0,28 % klingen nach Messgenauigkeit von d; d wandert aber mit der Form.** E Z. 49-59.
- [S] VP Z. 107-114: mit der fuehrenden Wellenzahl abs(X)^(-1/2) d = c/2 = 3,0746, also 2,13 % unter pi (PR1 nicht
  eingetroffen); FK mit p = 0: -4,34 %; Restmuster in allen Formen gleich, Ursache offen; Z. 70-72 "teils
  Mischungsglueck". Kanal- und Schwanzausgleiche sind nachtraeglich und beschreibend (VP Z. 145).
- Vorschlag: "The power $p$ is poorly constrained ($-0.4$ to $-2.0$, depending on the form of the exponent), and $d$
  moves with it: with the leading-order wavenumber $|X|^{-1/2}$ in place of $K$ the fit gives $d$ $2.1\,\%$ below $\pi$."
  Dazu vor die kanalweisen Werte: "Post hoc, separate fits per channel give ...".

**B2. Was "the zero" bei X < 0 ist, steht nirgends.** E Z. 34 f. und 41.
- [S] VW Z. 20-22: Bei X < 0 bleibt an der reellen Nullstelle von E eine Mischung aus altem und neuen Innenkanaelen exakt
  total reflektiert; das ist rho_z(X) (VP PLAN Z. 20). Der erste Leser hatte das in C6 begruendet, es kam nicht in den Text.
- Vorschlag, an "... $+O(X^2)$" anhaengen: "; for $X<0$, $\rho_z$ denotes the frequency at which a suitable mixture of
  the original and the new interior channels is still totally reflected."

**B3. Die gewaehlte Hintergrundloesung ist nur auf dem Rechengebiet eine Wand.** E Z. 61 f.
- [S] VP PLAN Z. 35 f. [M]: Ohne Innenschwanz waechst aussen ein Anteil ~ T^2 e^{x/2} (H = 0 erhalten, Schwanz H > 0);
  VP Z. 129 f.: bei -1e-2 und L = 80 schon 6,6e-6, ln P dennoch auf 6,6e-18 gleich.
- Vorschlag: "we used the solution without an interior tail, which does not stay bounded as $x\to\infty$ (outside, a
  component growing like $T^2e^{x/2}$ appears, $T$ the tail amplitude; the domain-length control above covers this)."

### C (kann)

- **C1** E Z. 26 "single-implementation": Es gab zwei Implementierungen eines Autors (finite Differenzen double, Taylor
  Festkomma), im Modell D gleich auf 1,8e-6 (VP Z. 141, 173). Vorschlag: "single-author".
- **C2** E Z. 42 "but only non-perturbatively": Schluss aus sechs Punkten, abs(X)^(-1/2) = 10 bis 22 (VP Z. 36 [H]).
  Vorschlag: "but, over the computed range, only beyond all orders in $X$".
- **C3** E Z. 51 f. "K ... is the new branch": "is the wavenumber of the new branch"; "at $\rho_z(X)$".
- **C4** E Z. 55 f.: "$0.35$ (open sideband) and $0.42\,\%$ (closed sideband)". Achtung: VP "B" ist Papier-A (ME Z. 119).
- **C5** E Z. 68 f. "smaller by $\sqrt2$": "smaller in magnitude by about $\sqrt2$" ([M] bei gleichem X ist K anders,
  Verhaeltnis 1,398 bei -1e-2, V22).
- **C6** E Z. 69-74: "on a nearest-neighbour stencil" durch "on the five-point stencil" ersetzen, weil die Formel nur fuer
  das Quadratgitter gilt; "is an artefact" kann bleiben (Abschnitt 7, Frage 2). Wahlweise: "has no counterpart on that
  stencil (a desk calculation; the planar lattice problem was not computed)".
- **C7** E Z. 37: "persists exactly, as it must with a single open channel on each side" (VP PLAN Z. 46 f.); die 3e-15 dann
  als Zahlenprobe.
- **C8** E Z. 30 "its planar transmission zero": "a planar transmission zero" (Rest von A5; ME Z. 377 f.).
- **C9** Notation: "static" durch "stationary"; Ausgleichskonstante nicht a (a(r) belegt); k_0 neben kappa_0 erklaeren
  oder anders benennen; "$d$ $0.21\,\%$" umstellen ("with $d$ exceeding $\pi$ by $0.21\,\%$").

## 6. Umsetzung der Befunde aus Fassung 1

Bericht RUNDE-37/papier-i-gegenlesen/GEGENLESEN.md erst nach Abschnitt 2 und 3 gelesen (ab date 11:17:18).
Massstab: Ist der Befund in der Sache behoben, ohne neuen Fehler?

| Befund | Umsetzung in Fassung 2 | Urteil |
|---|---|---|
| A1 Schwanzwahl | Vorschlag A1 woertlich (E Z. 59-66) | **teilweise**: "a few per cent" ist weg, "not measured" steht da; der uebernommene Vorschlag schreibt aber Faktor und 0,3 % den frueheren double-Laeufen zu (A2 neu). Fehler lag im Vorschlag, nicht in der Abschrift |
| A2 10^-95 | Hochrechnung gestrichen | **richtig**; Begruendung ueber B6 traegt (Abschnitt 7, Frage 2) |
| A3 beta = 1 | "modified potential ... not the main model"; pi/sqrt2-Satz | **richtig** (Rest C5) |
| A4 zwei Kanaele je Seite | woertlich | **richtig** |
| A5 "single" | "its planar transmission zero" | **richtig** in der Sache; "its" klingt noch nach genau einer Nullstelle (C8) |
| B1 Notation | X, E, q, "transmission zero"; kein "silen" mehr (grep) | **richtig** (Rest C9) |
| B2 Profil | S = (1/2)[1 + exp x]^(-1), S = f^2 | **richtig** |
| B3 Restgroesse | woertlich | **richtig** (Rest C7) |
| B4 halbes Leck | woertlich | **richtig** |
| B5 Ausgleich | Vorschlag B5 mit einer Aenderung der Leitung im Schwanzhalbsatz | **teilweise**: Die Aenderung "the same exponential" ist falsch (A1 neu). Der Kern von B5, dass d an der K-Wahl haengt (2,1 % mit abs(X)^(-1/2)), steht weder im Vorschlag noch im Text (B1 neu) |
| B6 echtes Gitter | Vorschlag woertlich | **richtig** in der Sache, fuer alle drei Stencils des Papiers nachgerechnet (Abschnitt 7); Formel nur fuers Quadratgitter (C6) |
| B7 Lehrbuchstoff | nur LaTeX-Kommentar | **teilweise**: im Satz unsichtbar; der Leser des Papiers haelt die Pol-Regel weiter fuer einen eigenen Befund. Vor Aufnahme Zitat an der Quelle lesen (Offen-Liste des Entwurfs) |
| B8 Evidenzgrad | Satzanfang woertlich | **richtig** (Rest C1) |
| C1 "below 3e-15" | ja | richtig |
| C2 "0.28 % below" | ja | richtig |
| C3 isotrop in 1D | ja, beide Saetze | richtig |
| C4 -h^2/12 | entfaellt | richtig |
| C5 Festkomma | woertlich | richtig |
| C6 Verschiebung beidseitig | eigener Satz | **teilweise**: die Begruendung von C6 (was rho_z bei X < 0 ist) fehlt im Text (B2 neu) |
| C7 schwaechste Probe | woertlich | richtig |
| C8 P keine Breite | kein Vergleich | richtig |

Zaehlung: A 4 richtig, 1 teilweise, 0 falsch; B 6 richtig, 2 teilweise (B5, B7), 0 falsch; C 7 richtig, 1 teilweise
(C6), 0 falsch. Gesamt 17 richtig, 4 teilweise, 0 falsch von 21. Beide neuen A-Befunde sitzen in Saetzen, die aus der
Umsetzung stammen: A2 aus einem Vorschlag des ersten Lesers, A1 aus einer Aenderung der Leitung an einem Vorschlag.

## 7. Gezielte Fragen der Leitung

**Frage 1: Schwanzsatz "the same exponential with d 0.21 % above pi". Richtig gelesen?**
- Die Zahl ist richtig gelesen: VP Z. 28 f. "d = pi + 0,21 %", Z. 159 d = 3,14812 ([M] +0,208 %).
- "the same exponential" trifft nicht zu. Ausgeglichen ist ln T = a + q ln abs(eps) - d k0: eine Amplitude, mit der
  Wellenzahl k0 des Schwanzes (k0 = 10,012 bis 22,366, VP Z. 96), nicht ein Fluss mit exp(-2dK) und K = K_B (9,676 bis
  22,225). Gemeinsam ist nur das Muster "Amplitude ~ exp(-Polabstand x eigene Wellenzahl)". Befund A1, Vorschlag dort.

**Frage 2: Naechste-Nachbar-Satz. Gilt er fuer eine achsparallele ebene Wand auf den Stencils des Papiers? Zu stark?**
Eigene Schreibtischrechnung [M], Stencils nach ME Z. 452 f.; fuer eine ebene Welle e^{iqx}, theta = qh:
- Fuenfpunkt (Quadrat): Symbol von -Laplace = (2 - 2cos theta)/h^2 = (4/h^2) sin^2(theta/2). Ableitung (2/h) sin theta > 0
  auf (0, pi): monoton bis zum Zonenrand pi/h, ein laufender Ast je Frequenz. Formel des Entwurfs genau richtig.
- Neunpunkt (Quadrat), beliebige Gewichte a (Nachbarn) und b (Diagonalen) mit Konsistenz a + 2b = 1: achsparalleles
  Symbol [a(2 - 2cos theta) + b(4 - 4cos theta)]/h^2 = 2(a + 2b)(1 - cos theta)/h^2 = (4/h^2) sin^2(theta/2). Fuer eine
  achsparallele Wand also dieselbe Dispersion wie Fuenfpunkt, unabhaengig von den Gewichten (die der erste Leser in C4
  nicht kannte). Falls "nine-point" der breite Kreuz-Stencil vierter Ordnung ist: Symbol [5/2 - (8/3)cos theta + (1/6)
  cos 2theta]/h^2, Ableitung sin theta (8/3 - (2/3)cos theta) > 0, ebenfalls monoton.
- Siebenpunkt (Dreieck), Wandnormale entlang einer Bindung: Symbol (2/(3h^2))[6 - 2cos theta - 4cos(theta/2)], Ableitung
  2 sin(theta/2)[2cos(theta/2) + 1]. Monoton bis theta = 4 pi/3, das ist genau die Zonenecke in Bindungsrichtung. Die
  ebene Reduktion tastet aber x im Abstand h/2 ab (Zone bis 2 pi/h); dort faellt das Symbol von 6/h^2 auf 16/(3h^2) =
  5,33/h^2. Ein zweiter laufender Ast existiert also nur fuer E^2 - 1 > 5,33/h^2, nahe der Bandkante. Bei den
  Kanalfrequenzen hier (k^2 = 5,97) braucht das h > sqrt(5,33/5,97) = 0,94; fuer jedes brauchbare h kein zweiter Ast.
- Der abgeschnittene Ast liegt bei q ~ abs(X)^(-1/2): Fuenfpunkt X = -h^2/12, also q ~ 3,46/h > pi/h (ausserhalb der
  Zone); Dreieck isotrop X = -h^2/16, q ~ 4/h, dort hat das Gitter die Frequenz E^2 - 1 ~ 6/h^2, nicht ~ 6.
- Urteil: Der Satz gilt fuer alle drei Stencils bei achsparalleler Wand und den Frequenzen des Absatzes. Die genannte
  Formel gilt aber nur fuer das Quadratgitter, "nearest-neighbour" schliesst den Dreiecks-Stencil sprachlich ein (C6).
- "artefact of truncating the dispersion at fourth order" ist fuer den Kanal nicht zu stark: Er existiert nur im
  abgeschnittenen Polynom. Zu stark waere es erst, wenn der Leser daraus "das Gitter leckt nicht" liest; das verhindert
  der folgende Halbsatz. Ob die ebene Gitterwand eine exakte Nullstelle behaelt, ist nicht gerechnet (H des ersten
  Lesers in B6) und steht zu Recht nicht im Text. Evidenzart Schreibtischrechnung; nicht schiefe Waende, nicht 2D-Radialmoden.

**Frage 3: Ist der Absatz in dieser Laenge sinnvoll? Empfehlung an Codex.**
- Nein [ES]. 503 gegen 186 Woerter (Abschnitt 4); das Modell ist nicht das Hauptmodell, die Rechnung nicht das Gitter, und
  sie kann den Mechanismus des Abschnitts nicht darstellen. Alle Fehler dieser Runde sitzen in den Detailsaetzen.
- Empfehlung: **Fussnote** (oder ein bis zwei Saetze am Abschnittsende), sonst weglassen. Keine Fassung in voller Laenge.
- Anforderungen an die Fussnote (Wortlaut bei Leitung/Codex):
  1. Modell genannt: ebene Reduktion, modifiziertes Potential beta = 1, nicht das Hauptmodell.
  2. X > 0: Nullstelle bleibt exakt (ein offener Kanal je Seite), Verschiebung -3,7e-3 X.
  3. X < 0: Das Abschneiden bei q^4 erzeugt einen Hoch-q-Ast, den die Stencils des Papiers bei achsparalleler Wand nicht
     haben; das Leck dorthin ist 8,7e-17 bei X = -1e-2 und faellt schneller als jede Potenz (1,5e-49 bei -2e-3).
  4. Keine Winkelkopplung, das Gitter selbst nicht gerechnet, explorativ, kein zweites Haus; Provenienzeintrag.
  5. Nicht in die Fussnote: Ausgleichsformen, d, p, K, Schwanz, 27 %, Faktor 2. Wenn Codex den Polabstand pi nennen will,
     dann nur mit Zitat (B7) und mit B1.
- Gegenfall: Will Codex die Langfassung, muessen A1 und A2 vorher behoben sein, B1 bis B3 sollten.

## 8. Einfach gesagt

Fassung 2 hat fast alle Fehler der ersten Fassung richtig behoben, und die meisten Zahlen stimmen auf die letzte Stelle.
Zwei Saetze sind aber neu falsch: Einer behauptet, der Schwanz der Wand folge "derselben" Formel wie das Leck, dabei fehlt
ein Faktor 2 und die Wellenlaenge ist eine andere. Der andere schreibt zwei Ergebnisse alten Rechnungen zu, die in
Wahrheit aus den neuen stammen. Der Satz ueber das Gitter stimmt: Auf den Gittern des Papiers gibt es den kurzen Wellenweg,
durch den das Leck geht, gar nicht. Weil der Absatz fast dreimal so lang waere wie der Abschnitt und am Ende selbst sagt,
dass er weder das Hauptmodell noch das Gitter trifft, raten wir Codex zu einer kurzen Fussnote oder zum Weglassen.

## 9. Nicht geprueft

- Code, Einzel-JSONs (K_H_*, D_H_*, A_*, B_*) und lauf-69/zusatz.json von VP nicht geoeffnet; Tabellenwerte aus
  ERGEBNIS.md, Stichproben aus VW .urteile und VP .ausgleich per jq.
- RUNDE-24/wand-beta/lauf-69/auswertung.json gibt es nicht (ls); WB nur ERGEBNIS.md Z. 17 gelesen.
- Die Abschnittsdateien des Papiers (sections/*.tex) liegen nicht in stage/; Symbolkollisionen dort nicht geprueft.
- Stencil-Gewichte des Papiers nicht an den 2D-Rohdaten geprueft; die Rechnung in Abschnitt 7 deckt alle konsistenten
  kompakten Neunpunkt-Stencils und den Kreuz-Stencil vierter Ordnung ab.
- Literatur (Boyd 1998, Pomeau/Ramani/Grammaticos) nicht an der Quelle gelesen.
- Kein LaTeX-Uebersetzungslauf (keine Laeufe).
