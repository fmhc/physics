# Theorie: Nullstellen der Atmungsbreite des 3D-Q-Balls (Runde 7)

- Auftrag: claude-primary (Leitung), nach Finn: "schreib das auf mit der schwingung und den nullstellen koennten wir daraus
  eine theorie entwickeln weiter?"
- Bearbeiter: Anthropic-Agent (Opus). Nur gelesen und von Hand gerechnet; kein python, kein awk, kein ssh, kein git, keine
  Unteragenten. Explorativ (v3).
- **Beginn: 2026-09-30 05:03:31 CEST (date).** Ende: letzte Zeile (nach dem Schreiben mit date gemessen).
- Abschnitt 5 (Vorhersagen) geschrieben ab 05:25:34 CEST (date). Zum Vorab-Status siehe 5.0.
- Markierungen:
  - **[H]** Hypothese dieses Dokuments.
  - **[L?]** Literatur aus dem Gedaechtnis, nicht nachgeprueft.
  - **[L4]** zitiert nach RUNDE-06/resonanz3d/L4-BIC-LITERATUR.md (dort vom Agenten gelesen, von mir nicht an der Quelle).
  - **(abgel.)** von mir aus Berichtswerten gebildet. **(Hand)** Schreibtischrechnung; die Annahme steht dabei.
- Gelesen: RUNDE-06.md (3D-Resonanz, Berichtigung 04:05:59, Codex-Scan, Feshbach); RUNDE-06/ERGEBNISSE-R6-B.md
  (Abschnitte 1.1, 2, 4, 5); RUNDE-06/resonanz3d/L4-BIC-LITERATUR.md; resonance-20260930/3D-OMEGA-SCAN-CODEX.md,
  FESHBACH-ERGEBNIS-CODEX.txt, feshbach-20260930/{ABLEITUNG-ROOT.txt, RESULT.txt, TABLE.txt}, UMLAUF-CODEX.md;
  RUNDE-07/bic2/PLAN.md; alle exakt- und kurve-Berichte in RUNDE-07/bic2/lauf-lokal/ und lauf-69/ mit Stand 05:02 sowie
  aus-nlfit/nlfit_bericht.txt; gesamtformel-20260921/KANDIDAT.md (nur Zeilen 1 bis 60, fuer 4.6). Die Ordner, die nach
  05:02 entstanden, stehen in 5.0 und im Nachtrag.
- Nicht geoeffnet: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
- **Literatur:**
  - RUNDE-07/L4-BIC-FAMILIE-LITERATUR.md lag beim Schreiben der Abschnitte 1 bis 7 (05:25 bis 05:29) nicht vor. Diese
    Abschnitte stuetzen sich auf die erste Pruefung (L4-BIC-LITERATUR.md, Runde 6).
  - Die neue Datei (Ende 05:18:20) habe ich um 05:31 gefunden und in Teilen gelesen: Kopf, Abschnitte 0, 1, 5, 6, 9, 10.
    Was daraus folgt, steht im "Nachtrag Literatur" am Ende.

## 1. Kurzfassung

1. **Befund.**
   - Die lineare Abstrahlungsbreite der l = 0-Atmung des 3D-Q-Balls (U = S - S^2 + S^3/2) hat bei omega*^2 = 0,79767679,
     rho* = 1,7446175 eine Nullstelle.
   - Belegstufe: **zweihaeusig mit Umlauftest (verschiedene Testfunktionen), im abgeschnittenen radialen linearen
     Modell.**
   - Zwei weitere Nullstellen desselben Modells (0,631449 und 0,685129) sind **Einhaus mit Umlauftest**. Ebenso je eine
     bei beta = 0,40 (0,699702) und bei beta = 0,45 (0,755738, Umlauf nur auf dem grossen Rechteck).
   - Weitere Stellen bei beta = 0,45 / 0,55 / 0,60 waren um 05:02 **Kandidaten**. Seit 05:14 bis 05:23 sind vier davon
     Einhaus mit Umlauftest: 0,6334 (beta = 0,45), 0,6748 und 0,7261 (0,55), 0,7102 (0,60). Siehe Nachtrag.
   - Im Log-Potential U = ln(1 + S) und in 1D: **nicht gesehen**.
2. **Mechanismus (Stand).**
   - Feshbach-artig: Ein Zustand des geschlossenen Kanals omega - rho leckt ueber die Nebendiagonale sp in den offenen
     Kanal omega + rho. Der Zustand sitzt nach meiner Rechnung in der Ballwand (Abschnitt 3.2, Hand).
   - Bei reellem rho ist das Problem reell. Eine exakte Nullstelle verlangt zwei reelle Bedingungen an zwei reelle
     Groessen (rho, omega^2); sie ist deshalb ohne Feinabstimmung zu erwarten (Kodimension 1).
   - Nahe jeder Nullstelle gilt Gamma ~ C (omega^2 - omega*^2)^2 mit C = 1,08 / 8,8 / 36 fuer die drei Stellen (abgel.).
3. **Neue Hypothese [H], "Phasenregel".**
   - Die Nullstellen liegen dort, wo die auslaufende Welle (Wellenzahl q) ueber den Duennwandradius
     R_tw = 1/(2 sqrt(beta) (omega^2 - omega_c^2)) die Phase q R_tw = (n + theta) pi sammelt.
   - Dabei ist theta = 0,78 bis 0,91; mit wachsendem n naehert es sich etwa 0,83.
   - Das gilt nachtraeglich an allen 12 bekannten Stellen (5 Werte von beta, drei Familien n = 1, 2, 3). Aufeinanderfolgende
     Nullstellen liegen 0,93 pi bis 1,02 pi auseinander.
   - Zusammen mit Gamma ~ Gamma_env sin^2(...) gibt die Regel die Breite zwischen den Nullstellen auf etwa 12 % wieder
     (beta = 0,5, omega^2 = 0,62 bis 0,80).
   - Das ist eine **Nachrechnung, keine Vorhersage**.
   - Die Grundidee (Formfaktor, 1/(omega*^2 - 0,5) linear in n) hat die parallele Literaturpruefung unabhaengig und frueher
     notiert (Nachtrag Literatur).
4. **Was die Regel erklaeren wuerde [H].**
   - mehrere Nullstellen in 3D mit abwechselnder Umlaufzahl und Haeufung zur duennen Wand
   - keine in 1D: Der Radius waechst dort nur logarithmisch, und die Innenbarriere fehlt
   - keine im Log-Potential: Der geschlossene Zustand ist nicht an eine Wand gebunden. Das Kriterium ist die Innenbarriere
     dp(S0) > (omega - rho)^2.
   - die Minima der Dimensionsbruecke bei d ~ 1,5 und 2,25
5. **Pruefbar mit unseren Codes (je hoechstens 10 min).**
   - vierte Nullstelle bei beta = 0,5 und omega^2 = 0,6018 +- 0,0006 mit Umlauf +1
   - beta = 0,40 bei 0,5657 und 0,5080; beta = 0,45 bei 0,5774
   - keine Nullstelle oberhalb der Barrierengrenze (beta = 0,5: 0,878)
   - eine l = 1-Nullstelle nahe 0,75
   - Vorzeichenwechsel in d bei omega^2 = 0,7
   - Nichtlinear: An omega* bestimmt ueberwiegend die stossbedingte Verschiebung von omega das Abklingen. Mit Ausgleich
     liegt es bei hoechstens 5e-7 (obere Schranke).
   - Physikalische Deutung als "Q-Ball-Isomere": Hypothese ohne Messbezug.

## 2. Der Befund

### 2.1 Modell und Groessen

- 3D, radial, l = 0, reduzierte Funktionen U = r u, V = r v:
  - U'' = [dp - (omega + rho)^2] U + sp V (offener Kanal, Wellenzahl q = sqrt((omega + rho)^2 - 1))
  - V'' = sp U + [dp - (omega - rho)^2] V (geschlossener Kanal, Abfall kappa = sqrt(1 - (omega - rho)^2))
  - dp = 1 - 4S + 9 beta S^2, sp = S U''(S) = -2S + 6 beta S^2, mit S = f^2 (Profil). Modell der Runde: beta = 1/2.
  - Im Fenster 1 - omega < Re rho < 1 + omega ist nur ein Kanal offen (bic2/PLAN.md, Abschnitt 1).
- Gamma = -Im rho (Amplitudenrate). Fuer die Nullstellen zaehlen drei Groessen (bic2/PLAN.md, Abschnitt 1):
  - A_out: auslaufende Amplitude am komplexen Pol.
  - W(rho, omega^2) = L(y_a) + i L(y_b) bei reellem rho, mit L = Koeffizient der im geschlossenen Kanal wachsenden
    Loesung. W = 0 heisst BIC. Die Umlaufzahl von W auf einem Rechteck in (rho, omega^2) ist bei einer regulaeren
    Nullstelle +-1.
  - s(omega^2) = L(y_a) an der Stelle L(y_b) = 0: die reelle, vorzeichenbehaftete Kopplung entlang des Asts.
- Codex' unabhaengige Testfunktion F = (u(0) + i v(0))/Norm, rueckwaerts vom Rand R integriert (UMLAUF-CODEX.md).

### 2.2 Die Nullstellen

| beta | omega*^2 | rho* | Umlauf (Rechteck 5e-4 / 1e-4) | d_min/\|A'\| | Belegstufe | Quelle |
|---|---|---|---|---|---|---|
| 0,50 | 0,79767679 (A_out, h = 0,005); W-Fit 0,797676808 / 0,797676819 / 0,797676820 bei h = 0,02 / 0,01 / 0,005 | 1,7446175 | Anthropic W: -1 / -1 auf allen drei Stufen. Codex F: +1 / +1 auf R36 und R44 | 2,5e-12 | **zweihaeusig mit Umlauftest (verschiedene Testfunktionen), im abgeschnittenen radialen linearen Modell** | lauf-lokal/aus-exakt-001, -0005; lauf-69/aus-exakt-002; UMLAUF-CODEX.md |
| 0,50 | 0,685129 | 1,690357 | +1 / +1 (h = 0,01) | 1,7e-10 | Einhaus mit Umlauftest | lauf-lokal/aus-exakt-b050-0685 |
| 0,50 | 0,631449 | 1,652588 | -1 / -1 (h = 0,01) | 4,2e-10 | Einhaus mit Umlauftest | lauf-lokal/aus-exakt-b050-0631 |
| 0,40 | 0,699702 | 1,663041 | -1 / -1 (h = 0,01) | 3,0e-11 | Einhaus mit Umlauftest | lauf-lokal/aus-exakt-b040-0700 |
| 0,45 | 0,755738 | 1,709290 | -1 / 0; das kleine Rechteck um x0 = 0,75586 lag 1,2e-4 neben der Stelle (abgel.) | 1,8e-10 | Einhaus mit Umlauftest (nur grosses Rechteck) | lauf-lokal/aus-exakt-b045-0756 |
| 0,45 | 0,63338 | 1,64447 | Stand 05:02 nicht gerechnet; seit 05:21 neu gelegtes kleines Rechteck +1 (Nachtrag) | 3,9e-8 | Stand 05:02 Kandidat; jetzt Einhaus mit Umlauftest (nur kleines Rechteck) | lauf-69/aus-kurve-045; lauf-lokal/aus-exakt-b045-0633, -v2-b045-0633 |
| 0,55 | 0,674766 (fein); 0,726 und 0,831 (grob) | 1,69236; 1,7263; 1,7729 | Stand 05:02 nicht gerechnet; seit 05:14 bzw. 05:23: 0,7261 +1 / +1, 0,6748 -1 / -1 (Nachtrag) | - | 0,6748 und 0,7261 jetzt Einhaus mit Umlauftest; 0,831 Kandidat | lauf-69/aus-kurve-055, aus-exakt-b055-0726; lauf-lokal/aus-exakt-v2-b055-0673 |
| 0,60 | 0,710164 und 0,759294 (fein); 0,856 (grob) | 1,72452; 1,75524; 1,7960 | Stand 05:02 nicht gerechnet; seit 05:20: 0,7102 -1 (grosses Rechteck); 0,7593 ohne Ergebnis (Nachtrag) | - | 0,7102 jetzt Einhaus mit Umlauftest; 0,7593 und 0,856 Kandidat | lauf-69/aus-kurve-060; lauf-lokal/aus-exakt-v2-b060-0710, -0759 |

Zur ersten Zeile:
- Codex findet (rho*, omega*^2) = (1,74461754, 0,79767679) mit Q = 189,144. Der Unterschied zu Anthropics W-Fit
  (1,7446175183; 0,797676820) ist 3e-8. Anthropics A_out-Nullstelle bei h = 0,005 (0,7976767871) und Codex' Wert
  (0,7976767871) sind in den gedruckten Stellen gleich (abgel.).
- Die Vorzeichen der Umlaufzahlen unterscheiden sich nur durch Orientierung und Definition der Abbildung.
- Gegenproben:
  - Anthropic: Rechteck um 0,8003 ohne Nullstelle gibt Umlauf 0 (lauf-69/aus-exakt-g5).
  - Codex: versetzte Schleife 0, freies Modell 0.
- Codex' Grenzen (UMLAUF-CODEX.md): endlicher Aussenrand; der Grenzuebergang R -> unendlich ist nicht rigoros gezeigt;
  keine Fehlerhuelle entlang der Kontur; keine Eindeutigkeit; nichtlineare Stabilitaet und l > 0 offen.

### 2.3 Weitere Befunde, je mit Belegstufe

| Aussage | Belegstufe | Quelle |
|---|---|---|
| Scharfes Minimum der l = 0-Breite nahe 0,7977, auf allen Stufen stabil | zweihaeusig (Lage blind gleich) | ERGEBNISSE-R6-B.md, Abschn. 2; 3D-OMEGA-SCAN-CODEX.md |
| Codex' drei kleinste Breiten folgen aus der Nullstelle 0,7976768 und C = 1,079: erwartet 4,55e-10 / 3,70e-10 / 3,58e-9 bei 0,79765625 / 0,7976953125 / 0,797734375, gemessen 4,552e-10 / 3,702e-10 / 3,576e-9 | Zweithaus-Zahlen, Abgleich (abgel.), Abweichung unter 0,1 % | 3D-OMEGA-SCAN-CODEX.md; lauf-lokal/aus-exakt-001 |
| Gamma ~ C (omega^2 - omega*^2)^2: C = 1,079 (0,7977), 8,8 (0,6851), 35,6 (0,6314); beta = 0,40: 2,84 | Einhaus (abgel. aus exakt-Tabellen) | exakt-Berichte |
| Gamma_Newton = Gamma_Fluss an allen exakt-Punkten; Krein-Norm N_K > 0 | Einhaus | exakt-Berichte |
| Phase von A_norm springt an jeder Nullstelle um pi (Abweichung 6e-6 bis 9e-3 rad) | Einhaus; bei 0,7977 auch Codex (Arm B: 0,31303 -> -2,82857) | exakt-Berichte; FESHBACH-ERGEBNIS-CODEX.txt |
| Feshbach, Arm A: Kopplung eta -> 0 fuehrt den Pol in einen gebundenen Zustand des geschlossenen Kanals (bei 0,7976953: rho_c = 1,733524, Breite 4e-13) | Einhaus (Codex), nur R44 | FESHBACH-ERGEBNIS-CODEX.txt; feshbach-20260930/TABLE.txt |
| An 0,7976953 ist Gamma bei eta = 0,125 / 0,25 / 0,5 / 0,75 / 1 gleich 1,06e-6 / 3,81e-6 / 9,30e-6 / 6,62e-6 / 3,70e-10; Gamma/eta^2 bei eta = 0,125: 6,8e-5 (bei 0,8: 1,07e-4) | Einhaus (Codex), nur R44 | TABLE.txt |
| Umlaufzahlen wechseln entlang des beta = 0,5-Asts ab: -1 (0,6314), +1 (0,6851), -1 (0,7977); s wechselt dort + -> -, - -> +, + -> - | Einhaus | exakt- und kurve-Berichte |
| Log-Potential: kein Vorzeichenwechsel von s auf omega^2 = 0,40 bis 0,90 (11 Werte, h = 0,02); Gamma faellt monoton von 1,28e-3 auf 3,97e-8 | nicht gesehen | lauf-69/aus-kurve-log |
| 1D, beta = 0,5: auf 14 Rasterpunkten omega^2 = 0,55 bis 0,88 (eine Stufe) keine Nullstelle; Gamma faellt monoton, etwa exponentiell | nicht gesehen | RUNDE-06.md (1D-Tabelle), Berichtigung Punkt 5 |
| l = 1: bei 0,80 / 0,82 / 0,84 keine Nullstelle (5,87e-4 / 5,97e-4 / 4,21e-4) | nicht gesehen (3 Punkte) | RUNDE-06.md |
| Dimensionsbruecke bei omega^2 = 0,7: Minima der Breite bei d ~ 1,5 (1,2e-3) und d ~ 2,25 (2,2e-4), Raster 0,25, eine Stufe | Einhaus, Kandidat fuer Nullstellenlinien | RUNDE-06.md; ERGEBNISSE-R6-B.md, V10 |
| Oberste Nullstelle gegen beta: 0,700 / 0,756 / 0,798 / 0,831 / 0,856 (beta = 0,40 bis 0,60) | gemischt: 0,40, 0,45 und 0,5 mit Umlauftest, 0,55 und 0,60 Kandidat | wie Tabelle 2.2 |
| Zeitbereich (BIC-2 c), omega^2 = 0,79768, dr = 0,05: eta = 0,001 und 0,003 unter der Aufloesung; eta = 0,01: 4,9e-6 (T = 3000 und 6000 gleich); eta = 0,03: 4,2e-5; p = 1,94 aus zwei Punkten | Einhaus, eine Aufloesung | lauf-lokal/aus-nlfit |
| Mit ausgeglichener Verschiebung (Start 0,8000 / 0,8007 / 0,8014, eta = 0,01): 4,9e-7 / 2,8e-7 / 3,8e-7; Fensterraten dieser Laeufe alle negativ (-1,9e-6 bis -4,3e-6), also nur obere Schranken | Einhaus, obere Schranke | aus-nlfit |
| Der Stoss verschiebt den Ball um delta omega^2 ~ -0,285 eta (x_eff - x0 = -2,81e-3 bis -2,88e-3 bei eta = 0,01) | Einhaus (abgel.) | aus-nlfit |

### 2.4 Nicht belegt

- "Exakt null" fuer das unendliche Gebiet: Beide Haeuser rechnen mit endlichem Aussenrand. Der Umlauf ist numerisch
  (abgetastete Kontur), nicht intervallzertifiziert.
- Irgendeine Nullstelle ausser 0,7977 in einem zweiten Haus.
- Stabilitaet des Zustands jenseits der linearen Ordnung. Das lineare Ergebnis gilt nur fuer l = 0; die l = 1- und
  l = 2-Moden desselben Balls strahlen weiter.
- Ein Gesetz A ~ t^(-1/2) im Zeitbereich (Abschnitt 4.4).

## 3. Mechanismus (Stand)

### 3.1 Zweikanal-Linearisierung

- Die Stoerung delta phi = e^(i omega t) (u e^(i rho t) + v* e^(-i rho t)) macht aus einem komplexen Feld zwei gekoppelte
  reelle Kanaele. Im Fenster ist omega + rho offen (auslaufende Welle) und omega - rho geschlossen (abklingend).
- Die Kopplung sp = S U''(S) ist die einzige Verbindung. Ohne sp sind beide Kanaele Schroedinger-Probleme mit dem
  Potential dp (FESHBACH-ERGEBNIS-CODEX.txt, ABLEITUNG-ROOT.txt).

### 3.2 Feshbach-Bild

- Codex, Arm A: Schaltet man sp schrittweise ab, laeuft der Pol stetig in einen gebundenen Zustand V_c des geschlossenen
  Kanals (rho_c = 1,733524 bei 0,7976953). Die Resonanz ist also ein gefangener Zustand, der nur ueber sp leckt
  (Einhaus, R44).
- **Wo sitzt V_c? (Hand, Annahme: Profilwerte aus den Berichten.)**
  - Energie des geschlossenen Kanals: (omega - rho_c)^2 = (0,893128 - 1,733524)^2 = 0,7063 (abgel.).
  - Erlaubt ist, wo dp(S) < 0,7063, also 4,5 S^2 - 4 S + 0,2937 < 0, also 0,081 < S < 0,808.
  - Im Ballinneren ist S0 = 1,045 (bei 0,80, kurve-050); dort ist dp = 1,73, also verboten. Aussen ist dp = 1, ebenfalls
    verboten.
  - **V_c ist ein Schalenzustand in der Wand** (Kugelschale, in der S von 0,81 auf 0,08 faellt). Das tiefste dp liegt bei
    S = 4/9 (dp = 0,111).
- Die Kopplung sp = -2S + 3S^2 wechselt bei S = 2/3 das Vorzeichen, also mitten in dieser Schale. Die Quelle sp V_c hat
  daher eine innere positive und eine aeussere negative Haelfte.

### 3.3 Kopplung M(omega), Fano-artig, und das quadratische Gesetz

- Nach der goldenen Regel gilt Gamma ~ M^2 mit M(omega) = Integral U_reg(r) sp(r) V_c(r) dr. Dabei ist U_reg die bei r = 0
  regulaere Loesung des offenen Kanals (L4-BIC-LITERATUR.md, 5 i).
- M ist bei reellem rho reell und stetig. Wechselt es das Vorzeichen, dann gilt nahe der Stelle M ~ M' (omega^2 - omega*^2)
  und Gamma ~ C (omega^2 - omega*^2)^2. Die Messungen bestaetigen das auf allen drei beta = 0,5-Nullstellen (2.3).
- s(omega^2) aus bic2 ist die exakte Fassung dieses M. PLAN.md: L(y_b) ~ c0 (rho - rho_c) und L(y_a) ~ M.
- **Einschraenkung aus Codex' Arm A:**
  - Bei kleiner Kopplung ist Gamma/eta^2 an der Nullstelle nicht klein: 6,8e-5 gegen 1,07e-4 bei 0,8.
  - Die Nullstelle der vollen Rechnung ist also **keine** Nullstelle der nackten goldenen Regel mit dem ungekoppelten V_c.
  - Sie entsteht erst bei voller Kopplung, mit dem "angezogenen" Zustand und dem verschobenen rho (1,7335 -> 1,7446).
  - Schon bei 0,8 liegt Gamma(eta = 1) 19-mal unter der eta^2-Hochrechnung (5,6e-6 gegen 1,07e-4, abgel.). Die starke
    Kernkopplung (sp bis etwa 1,6) macht das Feshbach-Bild zu einer Skizze (L4-BIC-LITERATUR.md, 5 i).
  - Folge fuer die Theorie: Robust ist die Existenz eines vorzeichenwechselnden reellen M. Die genaue Lage haengt an der
    vollen Kopplung.

### 3.4 Warum exakte Nullstellen generisch sind (reelles Problem bei reellem rho)

- Bei reellem rho sind alle Koeffizienten reell. Die bei r = 0 regulaeren Loesungen bilden eine Ebene P.
- Ein gebundener Zustand im Kontinuum braucht eine Kombination aus P, die im geschlossenen Kanal nicht waechst und im
  offenen Kanal verschwindet.
- Satz (bic2/PLAN.md, Abschnitt 1, eigene Herleitung des bic2-Autors): Weil P lagrangesch ist, ist das gleichwertig mit
  W = L(y_a) + i L(y_b) = 0. Das sind zwei reelle Bedingungen.
- Zwei reelle Bedingungen an zwei reelle Unbekannte (rho, omega^2) haben generisch isolierte Loesungen: **Kodimension 1
  in omega^2**, ohne Symmetrie und ohne Feinabstimmung (L4: Champneys u. a. 2001; Hsu u. a. 2016).
- Die Umlaufzahl einer regulaeren Nullstelle ist +-1. Numerische Fehler kleiner als min \|W\| auf der Schleife aendern sie
  nicht; deshalb ist "exakt null" pruefbar.
- Warum der Fernfeld-Umlauf aus L4 nicht taugt: Das Fernfeld beruehrt null nur in einer Falte (Gamma >= 0) und hat
  deshalb Umlauf 0 (bic2/PLAN.md). Codex stellt dieselbe Falle fest (UMLAUF-CODEX.md).
- Bei zwei offenen Kanaelen waeren es vier Bedingungen; entlang omega gaebe es dann nur Minima (L4, 5 ii).
- Folgerung **[H]**: Aufeinanderfolgende Vorzeichenwechsel derselben reellen Funktion s(omega^2) muessen abwechselnde
  Umlaufzahlen haben. Das ist bei beta = 0,5 so (-1, +1, -1). Dasselbe Muster liefert 4.1 fuer jedes beta (Abschnitt 5,
  V2).

### 3.5 Was dieses Bild nicht sagt

- Wo die Nullstellen liegen, wie viele es gibt und warum 1D und das Log-Potential keine zeigen. Dafuer ist Abschnitt 4 da.

## 4. Theorie weiterentwickeln (Papier; alles [H])

### 4.1 (a) Duennwand-Naeherung fuer M(omega): die Phasenregel

**Bausteine (Hand).** Annahme: duenne Wand, U = S - S^2 + beta S^3.

1. **Duennwandgrenze.**
   - U(S)/S = 1 - S + beta S^2 ist bei S_c = 1/(2 beta) minimal. Der Wert dort ist omega_c^2 = 1 - 1/(4 beta)
     (0,375 / 0,444 / 0,5 / 0,545 / 0,583 fuer beta = 0,40 bis 0,60).
2. **Wandprofil bei omega = omega_c.**
   - Aus der Energieerhaltung des Teilchenbilds folgt f'^2 = beta f^2 (f_c^2 - f^2)^2.
   - Daraus ergibt sich ein logistisches Profil S = S_c / (1 + exp((r - R)/sqrt(beta))) mit der Wandbreite
     sqrt(beta) (0,71 bei beta = 0,5).
   - Codex' "logistische Startfamilie" passt dazu.
   - Wandspannung: sigma' = Integral f'^2 dr = sqrt(beta) S_c^2 / 4.
3. **Radius.**
   - Die Reibung (d - 1)/r f' muss die Hoehendifferenz S_c (omega^2 - omega_c^2)/2 aufzehren.
   - Das gibt R_d = (d - 1)/(4 sqrt(beta) epsilon) mit epsilon = omega^2 - omega_c^2, in 3D also
     **R_tw = 1/(2 sqrt(beta) epsilon)**.
   - Probe: omega^2 = 0,6 (beta = 0,5) ergibt 7,07; der Bericht nennt R_Q = 7,41 (ERGEBNISSE-R6-B.md, Abschn. 5).
4. **Wandzustand.**
   - Im Inneren ist dp(S_c) = 1 + 1/(4 beta) groesser als (omega - rho)^2 ~ 0,70 bis 0,75, also Barriere.
   - In der Wand faellt dp auf 1 - 4/(9 beta) (Topf).
   - Der geschlossene Zustand V_c sitzt an der Wand (vgl. 3.2).
5. **Kopplung.**
   - M = Integral U_reg sp V_c ist eine wandnahe Quelle, gewichtet mit der regulaeren offenen Welle.
   - Ist die Quelle schmal gegen die Wellenlaenge 2 pi/q ~ 2,6, dann gilt
     **M ~ M_env sin(Phi - theta pi)** mit Phi = q R als Phase der offenen Welle an der Wand.
   - theta fasst die Wandstruktur zusammen (innere und aeussere Haelfte von sp V_c, Phasenversatz im Inneren).
6. **Spielzeugmodell zur Probe.**
   - Ersetzt man die Wand durch eine delta-Schale bei R, gilt exakt M = g V_c(R) sin(q R).
   - Die Nullstellen liegen bei q R = n pi, und Gamma = Gamma_0 sin^2(q R).
   - Unsere theta-Werte (~0,83) messen, wie weit die echte Wand von diesem Grenzfall abweicht.

**Nachrechnung an den bekannten Stellen (Hand; Phi = q R_tw mit q aus omega*^2 und rho* der Tabelle 2.2; theta = Phi/pi -
n):**

| beta | n = 1 | n = 2 | n = 3 |
|---|---|---|---|
| 0,40 | 1,775 (0,699702) | - | - |
| 0,45 | 1,812 (0,755738) | 2,795 (0,63338, Kandidat) | - |
| 0,50 | 1,846 (0,797677) | 2,810 (0,685129) | 3,825 (0,631449) |
| 0,55 | 1,875 (0,8305, grob) | 2,822 (0,7262, grob) | 3,828 (0,674766, Kandidat) |
| 0,60 | 1,906 (0,856, grob) | 2,836 (0,759294, Kandidat) | 3,830 (0,710164, Kandidat) |

(Eintrag = Phi/pi; in Klammern omega*^2.) Beispielrechnung beta = 0,5, n = 1:
- epsilon = 0,297677, R_tw = 0,707107/0,297677 = 2,3754
- omega* = 0,893128, omega* + rho* = 2,637746, q = sqrt(6,957704 - 1) = 2,440841
- Phi = 5,7980 = 1,8456 pi

- **Muster:**
  - theta_1 steigt mit beta gleichmaessig (0,775 -> 0,906).
  - theta_2 steigt schwaecher (0,795 -> 0,836).
  - theta_3 ist fast konstant (0,825 -> 0,830).
  - Der Einfluss von beta nimmt also mit n ab. Das passt zur Duennwandgrenze: Bei grossem n ist der Ball duennwandig und
    theta universell (~0,83).
  - Die Abstaende aufeinanderfolgender Nullstellen in Phi sind 0,93 pi bis 1,015 pi (sieben Abstaende, Mittel ~0,98 pi).
- **Warnzeichen:**
  - Die Variable q R_tw habe ich nachtraeglich gewaehlt.
  - Mit der Innenwellenzahl k_in statt q driftet theta bei beta = 0,5 stark: 0,76 / 0,58 / 0,54 (Hand, Annahme:
    homogenes gekoppeltes Inneres mit S_in = S0).
  - Warum die aeussere Wellenzahl die gleichmaessige Groesse ist, ist offen. Robust ist nur der Abstand ~pi.
  - Sechs der zwoelf Stellen sind Kandidaten oder grob lokalisiert.

**sin^2-Gesetz fuer die Breite zwischen den Nullstellen.** Aus M ~ M_env sin(...) folgt
Gamma ~ Gamma_env sin^2(pi (Phi - Phi_n)/(Phi_(n+1) - Phi_n)). Nahe der Nullstelle ergibt das Gamma_env = C / (dPhi/domega^2)^2.
- Hand, beta = 0,5, jeweils mit dPhi/domega^2 = q dR/domega^2 + R dq/domega^2 und drho/domega^2 aus den exakt-Tabellen:
  - dPhi/domega^2 = -17,0 / -41,6 / -80,3
  - damit Gamma_env = 3,73e-3 (0,7977), 5,09e-3 (0,6851), 5,52e-3 (0,6314)

| omega^2 | Modell (Gamma_env linear interpoliert) | gemessen | Quelle |
|---|---|---|---|
| 0,6214 | 3,3e-3 | 3,67e-3 | aus-exakt-b050-0629 |
| 0,66 | 4,6e-3 | 5,21e-3 | kurve-050 |
| 0,70 | 1,47e-3 | 1,468e-3 | kurve-050 |
| 0,74 | 4,0e-3 | 4,08e-3 | kurve-050 |
| 0,76 | 1,97e-3 | 1,99e-3 | kurve-050 |
| 0,78 | 4,1e-4 | 4,05e-4 | kurve-050 |
| 0,82 | 4,8e-4 | 3,77e-4 | kurve-050 |
| 0,84 | 1,4e-3 | 8,7e-4 | kurve-050 |
| 0,90 | 3,5e-3 | 5,0e-4 | kurve-050 |

- Von 0,62 bis 0,80 stimmt das Modell auf etwa 12 %. Ab 0,82 liegt es zu hoch; bei 0,90 um den Faktor 7. Genau dort
  verschwindet die Innenbarriere (4.3).
- Dieselbe Probe fuer beta = 0,40 mit Gamma_env = 1,47e-2 aus C = 2,84: 0,68 -> 1,19e-3 (gemessen 1,29e-3), 0,72 ->
  1,04e-3 (9,6e-4).
- Das ist eine Nachrechnung mit zwei Kenngroessen je Abschnitt (Lage der Nullstellen, Kruemmung dort), keine Vorhersage.

**Folgerungen der Regel [H]:**
- Zahl der Nullstellen: Phi = q R_tw waechst zur duennen Wand wie 1/epsilon. Es gibt also unendlich viele Nullstellen,
  die sich bei omega_c^2 haeufen.
- In 1/epsilon liegen sie fast gleichabstaendig: beta = 0,5: 3,36 / 5,40 / 7,61, Abstaende 2,04 und 2,21 (abgel.).
- Die Umlaufzahl wechselt ab: n ungerade -1, n gerade +1 (in bic2-Konvention). Alle fuenf bisher gerechneten Umlaeufe
  folgen dem (2.2).
- Die Kruemmung C_n waechst wie (dPhi/domega^2)^2 ~ 1/epsilon^4. Die Nullstellen werden also zur duennen Wand hin
  schmaler: Ein Ball muss seine Ladung genauer treffen.

### 4.2 (b) Warum 1D keine hat und 3D mehrere: die Dimension als stetiger Parameter

- Die Dimension wirkt nach der Regel zweimal **[H]**:
  1. **Radius.**
     - R_d = (d - 1)/(4 sqrt(beta) epsilon) (Hand, 4.1).
     - In 1D faellt der Reibungsterm weg. Die Plateaulaenge waechst dann nur wie ln(1/epsilon)/mu mit mu = 1/sqrt(beta)
       (Zeit nahe dem Gipfel des Teilchenbilds).
     - Phi aendert sich deshalb in 1D ueber 0,55 bis 0,88 viel weniger als in 3D.
  2. **Kernhoehe.**
     - Die Reibung hebt den Kern: in 3D S0 = 1,10 bis 1,14 (0,62 bis 0,72, kurve-050).
     - In 1D gilt S0 = 1 - sqrt(2 omega^2 - 1) (Hand, beta = 0,5): 0,3675 bei 0,7, 0,684 bei 0,55.
     - In 1D fehlt daher im ganzen gerechneten Bereich die Innenbarriere (4.3). V_c ist dort ein Volumenzustand ohne
       scharfe Quelle.
     - Probe bei 0,55 (Hand): dp(0,684) = 0,369 < (rho - omega)^2 = (1,3767 - 0,7416)^2 = 0,403.
- **Faecher der Nullstellenlinien.**
  - Bei festem n bleibt q R_d konstant. Das gibt epsilon_n(d) ~ (d - 1) q/(4 sqrt(beta) (n + theta) pi): nahezu gerade
    Strahlen, die auf den Punkt (d = 1, omega^2 = omega_c^2) zulaufen.
  - Bei omega^2 = 0,7 und beta = 0,5 ist R_d = 1,768 (d - 1). Mit q aus linear interpoliertem Re rho(d) und theta = 0,83
    folgen Vorzeichenwechsel bei d ~ 1,68 (n = 0), 2,43 (n = 1) und 3,12 (n = 2) (Hand).
  - Die n = 2-Linie kreuzt d = 3 bei 0,685, also knapp unter 0,7. Das passt zur Stelle 0,685129.
  - Die Bruecke der Runde 6 hat Minima bei d ~ 1,5 und 2,25 (Raster 0,25). Das liegt 0,15 bis 0,2 unter den
    Duennwandwerten. Bei kleinem d ist der Ball dicker, und R_tw unterschaetzt ihn; die Richtung passt, die Groesse ist
    nicht gerechnet.
  - Nach der Regel gehoert zu jedem der beiden Minima ein echter Vorzeichenwechsel, kein glattes Minimum.
- **1D-Vorhersage:**
  - Nullstellen, wenn ueberhaupt, erst unter omega^2 ~ 0,545. Dort bekommt V_c eine Barriere (Hand, mit (rho - omega)^2
    ~ 0,40).
  - Aufeinanderfolgende 1D-Nullstellen brauchen in epsilon etwa den Faktor 10 (Hand, Delta ln(1/epsilon) ~ pi mu/q ~
    2,4). Das ist schwer zu rechnen.

### 4.3 (c) Welche Eigenschaft von U steuert die Existenz?

- **Satz (Hand, eigene Herleitung).** Hat U(S)/S ein Minimum bei endlichem S_c > 0 (Duennwandgrenze vorhanden) und ist
  U'(0) = 1, dann wechselt sp = S U''(S) zwischen 0 und S_c das Vorzeichen.
  - Beweis: U(S_c)/S_c ist der Mittelwert von U' ueber [0, S_c] und gleich U'(S_c) = omega_c^2 < 1 = U'(0).
  - Eine Funktion, die bei 1 startet und am Ende ihren eigenen Mittelwert trifft, muss vorher unter diesen Mittelwert
    gefallen sein.
  - U' faellt also erst (U'' < 0) und steigt dann (U'' > 0).
- **Folge fuer den Log-Test (G6 in bic2/PLAN.md):** Plateau und Vorzeichenwechsel von sp treten in dieser Klasse immer
  gemeinsam auf. Das Log-Potential hat keins von beiden. Sein Ausgang "keine Nullstelle" trennt die beiden Mechanismen
  aus L4 (sp-Vorzeichen gegen Formfaktor) deshalb nicht. Trennen kann nur eine Aenderung der Geometrie bei festem U
  (Dimension, Radius). Genau das tut die Phasenregel.
- **Kriterium [H], Innenbarriere:** Nullstellen braucht einen an die Wand gebundenen Zustand des geschlossenen Kanals.
  Das heisst:
  - B := dp(S0) - (omega - Re rho)^2 > 0, mit dp = (S U')'. Das Innere ist fuer den geschlossenen Kanal verboten.
  - Ausserdem muss der Radius mit omega laufen (d > 1).
  - Log-Potential: dp = 1/(1+S)^2 < 1 und bei grossem S0 nahe 0. B < 0 im ganzen Bereich; V_c ist ein Hohlraumzustand im
    Inneren. Die Quelle ist glatt, ihr Formfaktor hat keine Nullstelle (wie die Fouriertransformierte einer Gaussglocke).
    Das passt zu "nicht gesehen" und zum monotonen Abfall.
  - 1D, beta = 0,5, 0,55 bis 0,88: B < 0 (4.2). Das passt ebenso.
  - Polynomfamilie: B wechselt am oberen Rand das Vorzeichen (Hand, lineare Interpolation aus S0 und Re rho der
    kurve-Berichte):

| beta | Barrierengrenze x_B (B = 0) | oberste Nullstelle | Abstand |
|---|---|---|---|
| 0,40 | 0,848 | 0,6997 | 0,148 |
| 0,45 | 0,865 | 0,7557 | 0,109 |
| 0,50 | 0,878 | 0,7977 | 0,080 |
| 0,55 | 0,889 (aus 0,8455 bis 0,8855 hochgerechnet) | 0,8305 (grob) | 0,059 |
| 0,60 | 0,899 | 0,856 (grob) | 0,043 |

- Jede bekannte Nullstelle liegt unterhalb von x_B. Das sin^2-Modell bricht bei beta = 0,5 genau dort zusammen, wo B
  kleiner wird (0,82 bis 0,90).
- Zum Vorschlag "Ueberlappintegral mit U''": M = Integral U_reg S U''(S) V_c dr ist genau dieses Integral.
  - Sein Vorzeichenwechsel kommt nach der Regel aus der Phase von U_reg an der Wand, nicht aus dem Vorzeichen von U''.
  - Der Vorzeichenwechsel von U'' in der Wand bestimmt nur den Versatz theta.
  - Pruefbar ist das nur ueber die Geometrie (Abschnitt 5, V5).

### 4.4 (d) Nichtlineare Lebensdauer an omega*

- **Erwartetes Gesetz [H]:**
  - Fuer die Atmungsamplitude a gilt da/dt = -[C (x_eff - x*)^2] a - gamma_2 \|a\|^2 a + ...
  - Dabei ist x_eff die tatsaechliche omega^2 des angestossenen Balls.
  - Erste Ordnung: Ein Stoss aendert die Ladung und verschiebt x um -0,285 eta (2.3). Das ist ein Effekt erster Ordnung
    in eta und ergibt eine Rate ~ C (0,285 eta)^2 = 0,088 eta^2. Die Rate ist exponentiell und haengt nicht von der Zeit
    ab.
  - Zweite Ordnung: Die Quellen bei omega + 2 rho und omega - 2 rho liegen beide in offenen Kanaelen. Der Koeffizient
    gamma_2 ist eine Summe zweier Quadrate und generisch ungleich 0 (L4, 5 iv).
  - Fuer einen genau abgestimmten Ball folgt A(t) = A0/sqrt(1 + 2 gamma_2 A0^2 t), also A ~ t^(-1/2) spaet (Manton und
    Merabet, [L4]).
  - Beide Mechanismen geben p = 2. **Der Exponent trennt sie nicht**; der Ausgleich der Verschiebung trennt sie.
- **Stand der Messung:**
  - Ohne Ausgleich (eta = 0,01): 4,9e-6. Das Modell der ersten Ordnung gibt 8,5e-6 mit x* = 0,79768 (Hand). Die
    Groessenordnung stimmt, der Faktor nicht.
  - Die Lage der Nullstelle auf dem Zeitgitter dr = 0,05 ist nicht bestimmt; nlfit nennt 0,797016 als "x* falls rein
    linear" fuer eta = 0,01, aber 0,795698 fuer eta = 0,03. Das ist unvertraeglich; ein einziges x*_dr erklaert beide
    nicht.
  - Mit Ausgleich: hoechstens 5e-7 (obere Schranke, Fensterraten negativ).
- **Folgerung:** Der echte nichtlineare Anteil ist bei eta = 0,01 mindestens zehnmal kleiner als die Rate ohne Ausgleich.
  - gamma_2 <= 5e-7/eta^2 = 5e-3 (in Einheiten der Stossstaerke).
  - Das algebraische Gesetz t^(-1/2) beginnt erst nach t ~ 1/(2 gamma_2 A0^2) >= 1e6. In T = 6000 ist es vom
    exponentiellen Abklingen nicht zu unterscheiden. Die bisherigen Zeitlaeufe koennen es nicht pruefen.
- **Hoehere Ordnung [H]:**
  - Die Nullstelle wandert mit der Amplitude (mittleres S aendert sich wie A^2; "A^2 displacement" bei Inagaki und
    Murakami, [L4]).
  - Faellt auch gamma_2 an einem Punkt weg, dann folgt A ~ t^(-1/4) (dritte Harmonische, dort gezeigt [L4]).
  - Fuer uns ist das Spekulation.

### 4.5 (e) Physikalische Bedeutung (streng Hypothese)

- **"Q-Ball-Isomere" [H]:**
  - An jeder Nullstelle traegt ein Q-Ball eine Atmungsanregung, die in linearer Ordnung nicht abstrahlt.
  - Ihre Lebensdauer begrenzen nur nichtlineare Effekte: Rate hoechstens 5e-7, also mehr als 2e6 Zeiteinheiten 1/m. Das
    sind mehr als 5e5 Schwingungen (Periode 2 pi/1,7446 = 3,6).
  - Der Name lehnt sich an Kernisomere an. Dort ist der Grund meist eine Auswahlregel (Symmetrie); hier ist es zufaellige
    Ausloeschung.
- **Spektrum [H]:**
  - Zu jedem n gehoert eine Ladung Q_n = Q(omega*_n). Bekannt ist Q(0,79768) = 189,14 (UMLAUF-CODEX.md).
  - Duennwandskalierung Q ~ omega S0 R^3 (Hand; R entweder R_tw oder R = 0,68/epsilon + 0,61, geeicht an R_Q(0,6) =
    7,41 und R_Q(0,8) ~ 2,87):
    - Q_2 = Q(0,6851) ~ 600 bis 800
    - Q_3 = Q(0,6314) ~ 1400 bis 2100
  - Bei grossem n gilt Q_n^(1/3) ~ (n + theta), die Isomere sind also etwa gleichabstaendig in Q^(1/3).
- **Statistik [H]:**
  - Ist die Phase Phi fuer zufaellig entstandene Baelle gleichverteilt, dann hat der Anteil (2/pi) arcsin(sqrt(f)) aller
    Baelle eine Atmungsbreite unter f Gamma_env.
  - Beispiele: f = 1e-4 -> 0,6 %, f = 1e-6 -> 0,06 %.
  - Ein Ensemble angeregter Q-Baelle haette also einen langen Schwanz sehr langlebiger Atmung.
- **Q-Ball-Dunkle-Materie und fruehes Universum:**
  - Q-Baelle als Dunkle Materie (Kusenko, Shaposhnikov 1998 [L?]) entstehen in Affleck-Dine-Szenarien durch Zerfall des
    Kondensats (Kasuya, Kawasaki 2000 [L?]) und sind zunaechst angeregt.
  - Nach 4.3 braucht der Effekt eine Innenbarriere. Das **meistbenutzte Potential dieser Szenarien, die flache Richtung
    ln(1 + S), zeigt ihn nicht** (nicht gesehen, und B < 0).
  - Fuer duennwandige Q-Baelle (Potentiale mit Minimum von U/S) sagt die Regel dagegen viele Isomere voraus.
  - Ob das Abklingen der Anregung in einem realistischen Szenario zaehlt (Stoesse, Temperatur, Expansion), ist voellig
    offen.
- **Messbezug:** keiner. Das Modell ist ein Spielzeug-Q-Ball in Einheiten m = 1. Es gibt weder eine Beobachtung, die das
  pruefen koennte, noch eine Rechnung fuer ein realistisches Potential.

### 4.6 (f) Bezug zum Programm

- **Gesamtformel: direkter Bezug.**
  - Der Kandidat (gesamtformel-20260921/KANDIDAT.md, Zeilen 34 und 38) benutzt genau U(S) = S - S^2 + S^3/2 mit
    S = Summe \|psi_a\|^2.
  - Unser Modell ist sein Fall N = 1.
  - Fuer N > 1 und beliebiges g gilt (Hand): Linearisiert man um einen Ball in nur einer Komponente, dann haengen
    delta S und der J_ab-Term nur in zweiter Ordnung von den anderen Komponenten ab. Die Gleichungen fuer delta psi_1
    bleiben unveraendert.
  - Die l = 0-Nullstellen gelten also fuer die ganze Gesamtformel, solange der Ball einkomponentig ist.
  - Neu waere, dass die anderen Komponenten in zweiter Ordnung zusaetzliche Zerfallskanaele oeffnen koennen (paarweise
    Anregung durch die Atmung) **[H]**. Das koennte gamma_2 fuer N > 1 erhoehen.
- **Spin-2-Kette:** kein Bezug. Der Befund betrifft die lineare Abstrahlung eines Skalarfeld-Solitons, keine Aussage zu
  den zehn Annahmen.
- **Grundlagen, nur begrifflich:**
  - Die Nullstelle ist ein konkretes dynamisches Beispiel einer "nichtstrahlenden Quelle": Die Quelle hat auf der Schale
    \|k\| = q des offenen Kanals keine Komponente (Devaney, Wolf 1973 [L?]; Goedecke 1964, klassisch strahlungsfreie
    Bewegungen [L?]).
  - Das ist ein Anschluss an eine alte Frage, keine neue Aussage ueber Quantenmechanik.

## 5. Vorhersagen fuer unsere Codes

### 5.0 Vorab-Status

- Abschnitt 5 wurde ab 05:25:34 CEST geschrieben.
- Um 05:22:30 (date) existierten schon diese Ordner, von mir **ungelesen**:
  - lauf-69/aus-exakt-b055-0726
  - lauf-lokal/aus-exakt-v2-b045-0633, -v2-b055-0673, -v2-b060-0710, -v2-b060-0759
- Fuer V2 gilt daher: **nicht vorab** (die Ergebnisdateien entstanden vor dem Eintrag). Die Selbstauskunft "ungelesen" ist
  nicht belegbar.
- Fuer alle anderen Vorhersagen gab es beim Schreiben keine Ergebnisdatei (Stand der Ordnerliste 05:22).

### 5.1 Tabelle

Alle Aufrufe: `bic2.py` im Ordner RUNDE-07/bic2 (Kopie auf der .69 unter /home/fmh/fmhc-physics-remote/runde7-bic2/), Form
wie in bic2/PLAN.md, Abschnitt 8. Aufwand nach den Laufzeiten der Runde (exakt 200 bis 360 s, kurve 210 bis 470 s,
zeit0 ~3,5 min).

| Nr | Vorhersage [H] | Aufruf | Aufwand | Unterscheidungspunkt: was widerlegt |
|---|---|---|---|---|
| V1 | beta = 0,5 hat eine vierte Nullstelle (n = 4) bei **omega^2 = 0,6018 +- 0,0006**, Re rho* ~ 1,627, **Umlauf +1**, C ~ 100 +- 25. Herleitung: Phasenregel mit theta_4 = 0,82 +- 0,02 gibt 0,6019; zusammen mit Gamma(0,6) = 2,06e-4 (Runde 6) und Gamma_env ~ 5,7e-3 folgt 0,6014 | 1. `kurve --geraet cpu --pot poly --beta 0.5 --xmin 0.585 --xmax 0.625 --dx 0.005 --abstand 0.08 --h 0.02 --out aus-kurve-050-tief`; 2. `exakt --geraet cpu --beta 0.5 --x0 0.6018 --rho0 1.6273 --drho 0.85 --h 0.01 --out aus-exakt-b050-0602` | je <= 8 min | Kein Vorzeichenwechsel von s in 0,59 bis 0,615 bei Kernwachstum < 1e8 widerlegt die Regel. Eine Nullstelle ausserhalb 0,6005 bis 0,6035 widerlegt den Versatz theta. Umlauf -1 widerlegt die Paritaet |
| V2 | Paritaet: n ungerade -1, n gerade +1 (bic2-Konvention). beta = 0,55: 0,6748 -> -1, 0,726 -> +1, 0,831 -> -1. beta = 0,60: 0,7102 -> -1, 0,7593 -> +1, 0,856 -> -1. beta = 0,45: 0,6334 -> +1, und zwar als exakte Nullstelle, nicht nur als Minimum. **Nicht vorab (5.0)** | laufende exakt-Aufrufe der Leitung | laeuft | jede Umlaufzahl mit falschem Vorzeichen; Umlauf 0 auf einem Rechteck, das die Stelle sicher enthaelt |
| V3 | Weitere Nullstellen unter dem bisher gerechneten Bereich: beta = 0,40 bei **0,5657 +- 0,002** (n = 2, Umlauf +1) und **0,5080 +- 0,001** (n = 3, -1); beta = 0,45 bei **0,5774 +- 0,0012** (n = 3, -1). Annahmen: Re rho - omega = 0,828 bzw. 0,845 +- 0,006 (aus kurve); theta extrapoliert | `kurve --geraet cpu --pot poly --beta 0.40 --xmin 0.50 --xmax 0.62 --dx 0.01 --h 0.02 --out aus-kurve-040-tief`; ebenso beta 0.45 mit `--xmin 0.565 --xmax 0.62` | je <= 8 min | Fehlt der Vorzeichenwechsel oder liegt er mehr als 3 Fehlerbreiten daneben, ist die Regel ueber beta nicht uebertragbar |
| V4 | Oberhalb der Barrierengrenze (beta = 0,5: x_B = 0,878) gibt es **keine** Nullstelle. s bleibt von 0,86 bis 0,96 negativ; der Abfall von \|s\| (7,2e-3 / 6,6e-3 / 5,2e-3 bei 0,86 / 0,88 / 0,90) ist schrumpfende Einhuellende, keine nahende Nullstelle | `kurve --geraet cpu --pot poly --beta 0.5 --xmin 0.86 --xmax 0.96 --dx 0.01 --h 0.02 --out aus-kurve-050-hoch` | <= 8 min | Ein Vorzeichenwechsel oberhalb 0,88 widerlegt das Barrierenkriterium (4.3). Dann waere eine rein geometrische Phase (wachsender Radius bei omega -> 1) die bessere Erklaerung |
| V5 | Dimensionsbruecke bei omega^2 = 0,7: die Minima bei d ~ 1,5 und 2,25 sind **echte Vorzeichenwechsel**. Auf einem Raster 0,05 um sie herum fallen die Breiten unter 1e-6, und sqrt(Gamma) mit Vorzeichen verlaeuft linear. Lagen: 1,5 bis 1,68 und 2,25 bis 2,43; die naechste Linie kreuzt 0,7 knapp oberhalb d = 3 | `bruecke --geraet cpu --omega2 0.7 --dims 1,1.2,1.3,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.8 --h 0.01 --start 1.4937769645-6.716e-5j`; zweiter Aufruf mit 2,0 bis 2,5 im Abstand 0,05 (Start vom Pol bei 2,0) | je ~ wie die Runde-6-Bruecke | Glatte Minima mit Gamma_min > 1e-5 auf dem feinen Raster widerlegen die Faecher-Hypothese (4.2) |
| V6 | l = 1 hat eine Nullstelle nahe **omega^2 = 0,75 +- 0,02** (Phasenregel mit dem Zusatzversatz pi/2 der l = 1-Welle: q_1 R_tw/pi = n + theta + 1/2 = 2,33; q_1 aus Re rho_1 = 1,7635 bei 0,7 und 1,8760 bei 0,8) | `pole --geraet cpu --l 1 --omega2 0.72,0.74,0.76,0.78 --h 0.02,0.01 --bereich resonanz --out aus-pole-l1` (bei Zeitnot in zwei Aufrufe teilen) | <= 10 min | Glatter Verlauf ohne Einbruch unter 1e-5 zwischen 0,72 und 0,78 widerlegt die Uebertragung auf l > 0 (oder theta_l weicht stark ab) |
| V7 | 1D, beta = 0,5: **keine** Nullstelle fuer omega^2 > 0,545 (keine Innenbarriere). Frueheste 1D-Nullstelle darunter | `bruecke --geraet cpu --dims 1 --omega2 0.53,0.54,0.55 --h 0.01` (1D-Scan wie Runde 6) | <= 8 min | Eine Nullstelle in 1D oberhalb 0,545 widerlegt das Barrierenkriterium |
| V8 | Log-Potential: **keine** Nullstelle auch bei kleinem omega^2 (0,10 bis 0,40), weil B < 0 bleibt. Gegenhypothese (c2): Die Kopplung sp = -S/(1+S)^2 ist bei grossem S0 auf die Randschale S ~ 1 konzentriert, und dann kaeme dort ein Vorzeichenwechsel. Ich halte (c2) fuer weniger wahrscheinlich (30 %) | `kurve --geraet cpu --pot log --xmin 0.10 --xmax 0.40 --dx 0.05 --h 0.02 --out aus-kurve-log-tief` | <= 8 min | Ein Vorzeichenwechsel von s widerlegt das Barrierenkriterium und stuetzt (c2) |
| V9 | Nichtlinear: Mit Ausgleich der Verschiebung bei eta = 0,03 liegt die kleinste Rate **<= 4,5e-6** (gamma_2 <= 5e-3). Ohne Ausgleich 4,2e-5. Startwerte x0 = x*_dr + 0,285 * 0,03, also etwa 0,8056 / 0,8064 / 0,8072. Bei eta = 0,03 mass nlfit eine Verschiebung von -0,274 eta (0,79768 -> 0,789470); die Mitte liegt daher eher bei 0,8060 | `zeit0 --geraet cpu --omega2 0.8064 --eta 0,0.03 --T 3000 --dr 0.05 --out aus-nl-komp03-b`, ebenso 0.8056 und 0.8072 | je ~3,5 min | Minimum >= 1e-5 heisst: echte nichtlineare Daempfung groesser als die Schranke. Ist die Rate aufgeloest, pruefen ob Rate(0,03)/Rate(0,01) ~ 9 (p = 2 echt) |
| V10 | Isomerleiter: Q(0,6851) = 600 bis 800, Q(0,6314) = 1400 bis 2100 | Q und R_Q berechnet profil() in bic2.py (Rueckgabe "Q", "R_Q"); ob exakt.json sie speichert, habe ich nicht geprueft | Auswertung | Werte ausserhalb der Spanne widerlegen die Duennwandskalierung, nicht die Nullstellen |
| V11 | Phasenregel mit dem gemessenen R_Q statt R_tw: Die Abstaende in Phi bleiben ~pi, theta verschiebt sich um eine Konstante | Auswertung aus den Profilen (R_Q) | Auswertung | Abstaende mit R_Q deutlich ungleich pi (z. B. < 0,8 pi) zeigen, dass R_tw nur zufaellig passt |

Ausserhalb unserer Codes, nur als Hinweis: Mit Codex' eta-Werkzeug (feshbach-20260930/run.py) sollte eine
Nullstellenlinie in der Ebene (eta, omega^2) durch (1; 0,79768) laufen. Nach Arm A liegt sie bei 0,8 knapp oberhalb eta = 1
(Hand, grob).

### 5.2 Was die Theorie als Ganzes widerlegen wuerde

- V1 und V3 zusammen: Fehlen die vorhergesagten tiefen Nullstellen, ist die Phasenregel eine nachtraegliche Anpassung an
  zwoelf Punkte.
- V4 und V8: Eine Nullstelle ohne Innenbarriere widerlegt das Wandbild des Mechanismus. Dann fehlt ein anderer Grund.
- Findet die Literaturpruefung die Regel schon (Duennwand-Formfaktor fuer eingebettete Moden), ist sie nicht neu. Das
  widerlegt sie nicht.

## 6. Offene Fragen und Risiken

- **Einhaus:**
  - Nur 0,7977 ist zweihaeusig.
  - 0,6314 und 0,6851 sowie die Stellen bei beta = 0,40 und 0,45 hat nur Anthropic gerechnet, auf einer Stufe
    (h = 0,01). Nur die erste Nullstelle hat drei Stufen.
- **Numerik:**
  - Endlicher Aussenrand (R = 28 bis 49 bei uns, 36 und 44 bei Codex).
  - Der Profilschwanz ist abgeschnitten.
  - Die Umlaeufe sind abgetastet, ohne Intervallzertifikat.
  - Bei 0,6314 ist das Kernwachstum ~2e2, die Phase von A_norm driftet ueber den Offsetbereich um bis zu 1,5 rad, und
    d_min kommt aus einem Polynomfit mit Fitrest 6e-9.
  - Die Kandidaten (beta = 0,55 / 0,60 / 0,45 bei 0,633) stammen aus kurve mit h = 0,02.
- **Die Phasenregel ist nachtraeglich:**
  - Variable (q R_tw), Bezugspunkt und die Deutung von theta habe ich nach Sicht der Daten gewaehlt.
  - Mit k_in statt q driftet theta.
  - Das sin^2-Modell interpoliert Gamma_env linear.
  - Erst V1, V3 und V6 pruefen die Regel echt.
- **Modellabhaengigkeit:**
  - Gerechnet sind nur die Polynomfamilie und ein Log-Potential, nur l = 0 ernsthaft, nur radial.
  - Fuer realistische Q-Ball-Potentiale gibt es keine Rechnung.
  - Auch an einer Nullstelle strahlen die l = 1- und l = 2-Anregungen des Balls weiter. "Nichtstrahlend" gilt nur fuer die
    l = 0-Atmung.
- **Feshbach bei voller Kopplung:** Die Nullstelle ist keine Nullstelle der nackten goldenen Regel (Arm A). Eine
  analytische Formel fuer theta braucht die angezogene Kopplung; Arm A lief nur auf R44.
- **Zeitbereich:**
  - Die Lage der Nullstelle auf dem Gitter dr = 0,05 ist ungeklaert (nlfit gibt je eta ein anderes "x* falls rein
    linear").
  - Die Fensterraten der Ausgleichslaeufe sind negativ.
  - Bei eta = 0,001 und 0,003 ist alles unaufgeloest.
- **Literatur koennte es kennen:**
  - Inagaki und Murakami 2026 [L4] finden fuenf Nullstellen eines Abstrahl-Ueberlapps einer 3D-Blase, mehr zur duennen
    Wand hin. Das ist dasselbe Muster, dort nichtlinear.
  - Kovtun, Nugaev, Shkerin 2018 [L4] zaehlen Duennwandmoden ueber Bessel-Nullstellen. Das ist die gebundene Entsprechung
    der Phasenregel.
  - Die Pruefung fuer die Familie liegt inzwischen vor, siehe "Nachtrag Literatur". Sie findet den Q-Ball-Befund nicht,
    aber eine ausgesprochene Gegenerwartung der NLS-Mathematik.
- **Physik:** Die Deutung als Isomere und jeder Bezug zu Dunkler Materie ist ohne Rechnung in einem realistischen Potential
  nur eine Hypothese.

## 7. Einfach gesagt

Ein Q-Ball ist ein Klumpen aus einem Feld, der auf der Stelle schwingen kann wie eine atmende Seifenblase; normalerweise
verliert er dabei langsam Energie als Welle nach aussen. Bei bestimmten Groessen des Balls hoert dieser Verlust nach
unserer Rechnung in erster Naeherung ganz auf, und zwei unabhaengige Programme finden fuer die erste solche Stelle
denselben Punkt auf sieben Stellen genau. Unsere neue
Vermutung ist, dass die Welle, die innen entsteht, am Rand des Balls genau so ankommt, dass sich alles aufhebt, aehnlich
wie bei einer Saite, die an einem Knoten angefasst wird und dort nicht mitschwingt. Daraus folgt, dass es viele solche
Stellen gibt, immer dichter, je groesser der Ball ist, und wir haben vorhergesagt, wo die naechsten liegen muessen. Ob
das in der Natur eine Rolle spielt, wissen wir nicht; es ist ein Rechenmodell ohne Messung.

## Nachtrag: neue Umlauftests (gelesen um 05:29 nach dem Schreiben von Abschnitt 5; nicht vorab, siehe 5.0)

Quellen: lauf-69/aus-exakt-b055-0726 (Ende 05:14), lauf-lokal/aus-exakt-v2-b045-0633, -v2-b055-0673, -v2-b060-0710,
-v2-b060-0759 (Ende 05:20 bis 05:23). Alle h = 0,01, Einhaus.

**Lesart der Rechtecke (abgel.):**
- Das erste grosse Rechteck (halbe Breite 5e-4) liegt um den Startwert x0 aus kurve.
- Die weiteren Rechtecke sind um die gefittete Stelle neu gelegt. Wo x0 mehr als 5e-4 neben der Stelle liegt, muss das
  erste Rechteck 0 geben.
- Das trifft in allen drei Faellen zu (0,6334: 7,1e-4 daneben; 0,6748: 1,35e-3; 0,7593: 5,6e-4). Bei 0,7102 liegt x0
  4,4e-4 daneben, also innen, und dort ist das erste Rechteck -1.

| beta | omega*^2 (W-Fit) | rho* | Umlauf | n | V2 (Paritaet) | Belegstufe neu |
|---|---|---|---|---|---|---|
| 0,55 | 0,726130 | 1,726321 | +1 / +1 | 2 | +1 getroffen | Einhaus mit Umlauftest |
| 0,55 | 0,674782 | 1,692366 | Start-Rechteck 0 (Stelle ausserhalb); neu gelegt -1 / -1 | 3 | -1 getroffen | Einhaus mit Umlauftest |
| 0,45 | 0,633381 | 1,644471 | Start-Rechteck 0 (Stelle ausserhalb); neu gelegtes kleines Rechteck +1 | 2 | +1 getroffen | Einhaus mit Umlauftest (nur kleines Rechteck) |
| 0,60 | 0,710164 | 1,724518 | grosses Rechteck -1; kleines: "zu wenige Profile" | 3 | -1 getroffen | Einhaus mit Umlauftest (nur grosses Rechteck) |
| 0,60 | 0,759294 | 1,755242 | Start-Rechteck 0 (Stelle ausserhalb); kleines: "zu wenige Profile" | 2 | nicht pruefbar | Kandidat (d_min/\|A'\| = 6,7e-9) |

- **V2: 4 von 4 pruefbaren Umlaufzahlen haben das Vorzeichen der Paritaetsregel** (nicht vorab; die Dateien entstanden vor
  dem Eintrag).
- Die Lage aendert die Phasenregel nicht: beta = 0,55, n = 2 mit 0,726130 ergibt Phi/pi = 2,823 statt 2,822 (Hand).
- Neuer Stand der Zaehlung:
  - mit Umlauftest (Einhaus): neun Stellen, naemlich beta = 0,5: drei; 0,40: eine; 0,45: zwei; 0,55: zwei; 0,60: eine
  - davon zweihaeusig: 0,7977 (beta = 0,5)
  - Kandidaten: 0,7593 (0,60) sowie 0,831 (0,55) und 0,856 (0,60), die nur grob lokalisiert sind
- Die Kurzfassung (Punkt 1) nennt den Stand von 05:02 und dazu den Verweis auf diesen Nachtrag.

## Nachtrag Literatur (gelesen ab 05:31, nach Abschnitt 1 bis 7)

Quelle: RUNDE-07/L4-BIC-FAMILIE-LITERATUR.md (Anthropic-Agent, 04:59 bis 05:18). Die Kennzeichen [A], [S] und [ES] stammen
von dort; ich habe keine Quelle selbst geoeffnet.

1. **Die Phasenregel ist dort unabhaengig schon skizziert.**
   - Abschnitt 5 und 6 (Formfaktor q R ~ n pi + phi, R ~ 1/(omega^2 - omega_min^2), also 1/(omega*^2 - 0,5) linear in n).
   - Um 05:12 bis 05:18 aus zwei Nullstellen vorab gebunden: ~0,634 (+-0,01, getroffen: 0,6314), dann ~0,60 und ~0,58.
   - Neu in diesem Dokument sind nur:
     - der Vorfaktor von R_tw
     - theta ueber fuenf beta-Werte
     - das sin^2-Gesetz mit Gamma_env
     - die Innenbarriere als Kriterium
     - die Paritaet
     - die schaerfere Lage 0,6018 +- 0,0006 (V1)
   - V1 und die dortige Vorhersage ~0,60 pruefen dasselbe; der Vorrang liegt bei der Literaturpruefung.
2. **Gegenerwartung der Mathematik.**
   - Cuccagna und Maeda 2020 [A] erwarten fuer NLS-Grundzustaende keine eingebetteten Eigenwerte ("unproved yet"), numerisch
     nie gesehen. Eingebettete Eigenwerte gelten dort als instabil unter Stoerung.
   - Unser Befund (knotenfreier Ball, Krein-Norm > 0) stuende dagegen. Versoehnt wird er laut Datei durch zwei Moderatoren:
     Familie statt Einzelsoliton (Kodimension 1, Agmon, Herbst, Maad Sasane 2010) und NLKG statt NLS.
   - Das passt zu 3.4: In der Familie wandert die Nullstelle mit beta, statt zu verschwinden.
   - Fuer die Theorie heisst das: Die Phasenregel braucht den relativistischen Abstand (Re rho ~ 1,74 gegen 1 - omega
     ~ 0,1). Im NLS-Grenzfall omega -> 1 sagt sie mit dem Barrierenkriterium (V4) ebenfalls keine Nullstelle voraus
     **[H]**.
3. **1D als Satz.**
   - Collot, Germain und Pacherie 2025 [A] beweisen fuer die 1D-NLS-Klasse: keine eingebetteten Eigenwerte.
   - Die Datei nennt fuer 1D ein Fenster 0,5 < omega^2 < 5/9, in dem sp ueberhaupt wechseln kann. Mein Barrierenkriterium
     gibt < 0,545 (4.2). Beide Fenster sind fast gleich.
   - Ergaenzung zu V7: Unterhalb 0,545 trennt ein 1D-Test zwei Lesarten. Ist der Satz auf NLKG uebertragbar, gibt es keine
     Nullstelle. Nach dem Barrierenbild ist dort eine moeglich.
4. **Beweisweg.** Ayala u. a. 2026 [A] beweisen exakte Abstrahlungsnullstellen in der Optik computergestuetzt
   (Intervallarithmetik). Fuer unseren Umlauftest waere das der Weg von starker Evidenz zu einem Beweis (Abschnitt 6,
   "Numerik").
5. **Anderer Mechanismus.** García Martín-Caro, Queiruga, Wereszczyński 2025 [A]: Dort verschwindet die Zerfallskonstante
   an einer Spektralwand (Schwelle). Das ist nicht unser Mechanismus; unsere Stellen liegen 0,15 unter der Kante 1 + omega.

Ende: siehe letzte Zeile.

**Ende: 2026-09-30 05:32:16 CEST (date, nach dem Schreiben gemessen).** Dauer 28:45 min, Budget 60 min.
