# HOPF-1 (Runde 10): Ergebnis — bindet ein Hopf-Knoten an den Q-Ball? (Modell B.5, Produktansatz)

- **Schreibbeginn: 2026-09-30 11:22:21 CEST (date).** Plan, Schreibtischpruefung (D1 bis D7) und Entscheidungsregeln:
  PLAN.md, geschrieben ab 10:48:07, vor der ersten Rechnung. Erste Rechnung: Rauchtest um 10:52:46 CEST.
- Bearbeiter: Code-Agent HOPF-1 (Claude). Auftrag: Leitung claude-primary (Finn: "prüfe q-ball hopf verbund noch mal").
- Alles [H]: explorativ, klassisch, nur Produktansatz. Die Rechnung sagt nichts ueber Spin, Fermionen oder Quarks.
  Bindung ist nicht Stabilitaet.
- **Belegstufe:** S1, explorativ. Eigene Ausfuehrung mit drei Gegenproben:
  - Algebra: direkte Differenz gegen die Kreuztermformel, <= 7,5e-14 relativ.
  - Quadratur: 3D-Gitter gegen 2D-Achsensymmetrie, <= 5,2e-5.
  - Gitterstufen h = 0,2 und 0,1.
  - Codex' unabhaengiger zentrierter Produktwert stimmt in der Groesse (Abschnitt 6).
  - Keine Relaxation (Stufe B offen), keine Fremdhaus-Lesung.

## 1. Ergebnis zuerst

- **Anziehung ueberall.** Alle 283 Lagen ergeben E_int < 0, beide Baelle (omega^2 = 0,6 gross, 0,8 klein) und
  beide v (0,5 und 1,0).
- **Die Wand bindet am staerksten, nicht die Mitte.**
  - Ein fester kleiner Knoten, vom Ballzentrum nach aussen verschoben, bindet am tiefsten, wenn seine koppelnde Schale
    (n3 ~ 0) bei S_phi ~ 0,62 bis 0,84 liegt (v = 0,5), also in der Wand.
  - Beim grossen Ball bindet die Mitte je nach Knoten 59 bis 73 % so stark wie die Wand (v = 0,5), bei v = 1 nur noch
    32 bis 45 %.
  - Die Vorhersage der Leitung sagte etwa 75 %, meine Schreibtischkorrektur D3 sagte 60 bis 67 %.
- **v-Schwelle (3) knapp verletzt, aber nur fuer eine Knotenform.**
  - Die Bindung waechst von v = 0,5 zu v = 1 ueberall.
  - Fuer den kompakten Torus-Ansatz ganz im Inneren des grossen Balls kippt das Vorzeichen aber schon bei
    v^2/4 = 0,328, also knapp unter 1/3.
  - Ursache ist D4: Die Ballmitte hat S0 = 1,088 > 1.
- **gJ-Term (4):** In allen koaxialen Lagen exakt null (<= 1e-16 relativ). Neben der Achse ist er zu festem Zeitpunkt
  nicht null, bis 48 % von |E_U| (weit aussen); im Zeitmittel ist er null.
- **Stufe B (Relaxation) offen:**
  - Mein Relaxierer verliert auf dem Gitter die Hopfzahl, in 3D und in der 2D-Reduktion.
  - Kostenschaetzung: Abschnitt 7.

## 2. Vorab gegen Ausgang, je Punkt der Leitung (Vorhersage unveraendert, RUNDE-10.md 10:37:41)

| Punkt | Vorhersage | Ausgang | Urteil |
|---|---|---|---|
| (1) | E_int im Produktansatz negativ | 283 von 283 Lagen negativ, beide v, beide Baelle, Gitterfehler <= 5e-5 | **bestanden** |
| (2) | am staerksten mit der Roehre in der Wand (S_phi ~ 2/3), nicht in der Mitte; Mitte ~75 % der Wand je Ueberlappvolumen | Minimum bei <S_phi>_s/S0 = 0,57 bis 0,77, also S_phi = 0,62 bis 0,84 (Wand), fuer jeden Knoten, der ins Innere passt; Mitte/Wand 0,59 bis 0,73 (v = 0,5), 0,32 bis 0,45 (v = 1); je Knotenmenge 0,65 bis 0,71 | **bestanden**; Zahl 75 % zu hoch (D3). Zu buchstabengetreuen Faellen mit Minimum bei d = 0 siehe unten |
| (3) | Bindung waechst mit v^2, anziehend solange v^2/4 < 1/3 | Waechst in allen Lagen von v = 0,5 zu 1; Vorzeichenwechsel c* >= 0,378 fuer beide Hopfabbildungs-Ansaetze, aber **c* = 0,328 bis 0,332 < 1/3** fuer den Torus-Ansatz mit R_h = 2 bis 3 im grossen Ball | **knapp gescheitert** (Fenster 1,146 < v < 1,155; E_int(v^2/4 = 1/3) = +0,09 gegen -1,06 bei v = 1) |
| (4) | gJ traegt raeumlich gemittelt nichts bei | koaxial exakt null; neben der Achse zu festem t bis 0,26 |A1| (Momentaufnahme), im Zeitmittel null | **bestanden** (koaxial exakt, sonst nur im Zeit- oder Phasenmittel, wie D2) |

- Zu (2), buchstabengetreu: Mit dem mittleren Knoten (R_h = 1,5) liegt beim **kleinen** Ball (R = 2,29) das Minimum
  bei d = 0.
  - Dort sitzt die koppelnde Schale aber schon bei zentriertem Knoten in der Wand (<S_phi>_s = 0,535 S0 = 0,56).
  - Der Knoten ist groesser als das Ballinnere (S > 0,9 S0 nur bis r = 1,05).
  - In keinem Fall bindet eine Schale im Ballinneren tiefer als eine Schale in der Wand.
- Zu (3): Fuer Knoten ganz im Ballinneren trifft die Formel aus D4 auf 1 %: c* ~ (4/3 - S0) / (<s^2>/<s>).
  - Hopfabbildung R_h = 1,5, w = 0,75: <s^2>/<s> = 0,618, also c* = 0,397 (gemessen 0,399).
  - Torus R_h = 2,5, a = 1,5: <s^2>/<s> = 0,750, also c* = 0,327 (gemessen 0,330).
  - Wo die Grenze liegt, haengt also an der Schalenform. Die Schwelle 1/3 der Leitung gilt nur fuer S0 = 1.

## 3. Tabelle: E_int gegen Lage, fester kleiner Knoten, Verschiebung entlang der Knotenachse (F2z_klein)

Knoten: Hopfabbildung, R_h = 0,75, w = 0,35 (Kernring 0,75; koppelnde Schale in der Ebene bei 0,44 bis 1,06).
- d = Abstand Knotenzentrum zu Ballzentrum.
- <S_phi>_s/S0 = mittlere Ballbelegung dort, wo der Knoten koppelt.
- Regionen: innen S_phi > 0,9 S0; Wand 0,1 bis 0,9 S0; aussen <= 0,1 S0; Aufteilung fuer v = 1.
- Werte aus der 2D-Quadratur h = 0,01; das 3D-Gitter h = 0,1 stimmt auf <= 5e-9 ueberein.

**Grosser Ball omega^2 = 0,6** (S0 = 1,088, R(S0/2) = 7,21, r(S = 2/3) = 6,90, Q = 2873, E_Q = 2333):

| d | Lage | <S_phi>_s/S0 | E_int v = 0,5 | E_int v = 1 | innen | Wand | aussen |
|---|---|---|---|---|---|---|---|
| 0 | (a) Mitte | 1,000 | -0,1662 | -0,2870 | -0,2870 | 0 | 0 |
| 3,0 | innen | 0,996 | -0,1686 | -0,2978 | -0,2978 | 0 | 0 |
| 5,0 | Innenrand der Wand | 0,946 | -0,2005 | -0,4428 | -0,3350 | -0,1077 | 0 |
| 6,0 | Wand | 0,815 | -0,2556 | -0,7106 | -0,1485 | -0,5622 | 0 |
| 6,5 | Wand | 0,694 | -0,2793 | -0,8507 | -0,0473 | -0,8033 | 0 |
| 6,90 | (b) Wand, S_phi(d) = 2/3 | 0,574 | **-0,2812** | -0,9049 | -0,0067 | -0,8980 | -0,0002 |
| 7,0 | Wand | 0,544 | -0,2785 | **-0,9060** | -0,0039 | -0,9019 | -0,0003 |
| 7,21 | Wand, S_phi(d) = S0/2 | 0,477 | -0,2682 | -0,8912 | -0,0011 | -0,8892 | -0,0009 |
| 8,0 | Aussenrand | 0,247 | -0,1863 | -0,6537 | 0 | -0,6149 | -0,0387 |
| 9,0 | (c) aussen | 0,077 | -0,0724 | -0,2618 | 0 | -0,1413 | -0,1205 |
| 10,0 | aussen | 0,020 | -0,0200 | -0,0731 | 0 | -0,0016 | -0,0714 |
| 12,0 | aussen | 0,001 | -0,0012 | -0,0043 | 0 | 0 | -0,0043 |

**Kleiner Ball omega^2 = 0,8** (S0 = 1,045, R(S0/2) = 2,29, r(S = 2/3) = 1,93, Q = 186,1, E_Q = 181,9):

| d | Lage | <S_phi>_s/S0 | E_int v = 0,5 | E_int v = 1 | innen | Wand | aussen |
|---|---|---|---|---|---|---|---|
| 0 | (a) Mitte | 0,876 | -0,2510 | -0,6757 | -0,1828 | -0,4929 | 0 |
| 1,0 | innen/Wand | 0,778 | -0,2750 | -0,8074 | -0,1076 | -0,6998 | 0 |
| 1,5 | Wand | 0,661 | **-0,2855** | -0,8932 | -0,0468 | -0,8463 | 0 |
| 1,93 | (b) Wand, S_phi(d) = 2/3 | 0,539 | -0,2776 | **-0,9084** | -0,0087 | -0,8995 | -0,0002 |
| 2,29 | Wand, S_phi(d) = S0/2 | 0,431 | -0,2554 | -0,8610 | -0,0010 | -0,8587 | -0,0013 |
| 3,0 | Aussenrand | 0,242 | -0,1804 | -0,6331 | 0 | -0,6014 | -0,0317 |
| 4,0 | (c) aussen | 0,084 | -0,0758 | -0,2734 | 0 | -0,1514 | -0,1220 |
| 5,0 | aussen | 0,025 | -0,0246 | -0,0896 | 0 | -0,0023 | -0,0872 |
| 7,0 | aussen | 0,002 | -0,0023 | -0,0083 | 0 | 0 | -0,0083 |

**Alle festen Knoten, Minimum und Verhaeltnis Mitte/Minimum** (F2 = Verschiebung; z entlang der Achse, x in der
Knotenebene; mittel = R_h 1,5, w 0,7):

| Ball | Familie | v = 0,5: d_min, Mitte/Min | v = 1: d_min, Mitte/Min | <S_phi>_s/S0 am Min (v = 0,5) |
|---|---|---|---|---|
| 0,6 | F2z klein | 6,90; 0,59 | 7,0; 0,32 | 0,57 |
| 0,6 | F2x klein | 6,5; 0,62 | 6,90; 0,34 | 0,68 |
| 0,6 | F2z mittel | 6,0; 0,68 | 6,5; 0,40 | 0,70 |
| 0,6 | F2x mittel | 5,5; 0,73 | 6,5; 0,45 | 0,77 |
| 0,8 | F2z klein | 1,5; 0,88 | 1,93; 0,74 | 0,66 |
| 0,8 | F2x klein | 1,5; 0,91 | 1,93; 0,79 | 0,67 |
| 0,8 | F2z/F2x mittel | 0; 1 | 0; 1 | 0,535 (Schale schon bei d = 0 in der Wand) |

## 4. Radius-Reihe, gleiches Zentrum: (a) Knoten in der Mitte, (b) Roehre in der Wand, (c) Knoten umschliesst den Ball

Ansatz F1A: Hopfabbildung, feste Roehre w = 0,75; R_h = Kernringradius. g = A1/M_b ist die Bindung je Knotenmenge
(Grenzfall kleiner v). Ausgewaehlte Zeilen; alle Zeilen stehen in laeufe/A-w060.json und A-w080.json, Feld "tabelle".

**Grosser Ball (0,6):**

| R_h | Lage | <S_phi>_s/S0 | E_int v = 0,5 | E_int v = 1 | v = 1: innen / Wand / aussen | g je Knotenmenge | c* |
|---|---|---|---|---|---|---|---|
| 1,0 | (a) Mitte | 0,999 | -0,822 | -1,604 | -1,603 / -0,001 / 0 | -0,401 | 0,429 |
| 3,0 | innen | 0,992 | -4,92 | -8,01 | -7,83 / -0,18 / 0 | -0,411 | 0,379 |
| 5,0 | innen/Wand | 0,906 | -16,19 | -35,31 | -15,05 / -20,25 / -0,01 | -0,493 | 0,475 |
| 6,5 | Schale bei S_phi = 0,68 | 0,629 | -32,91 | -96,42 | -9,74 / -86,28 / -0,40 | **-0,568** | 0,763 |
| 7,21 | (b) R_h = R_Ball | 0,439 | **-36,32** | -115,48 | -2,97 / -110,05 / -2,45 | -0,502 | 0,976 |
| 7,5 | Wand/aussen | 0,364 | -35,78 | **-116,77** | -1,49 / -110,44 / -4,84 | -0,454 | 1,081 |
| 9,0 | (c) umschliesst | 0,090 | -18,78 | -66,87 | -0,03 / -46,83 / -20,01 | -0,162 | 1,769 |
| 11,0 | umschliesst | 0,007 | -2,45 | -9,00 | 0 / -0,54 / -8,47 | -0,014 | 2,394 |

**Kleiner Ball (0,8):**

| R_h | Lage | <S_phi>_s/S0 | E_int v = 0,5 | E_int v = 1 | v = 1: innen / Wand / aussen | g je Knotenmenge | c* |
|---|---|---|---|---|---|---|---|
| 0,5 | Mitte | 0,757 | -0,509 | -1,575 | -0,186 / -1,387 / -0,002 | -0,585 | 0,892 |
| 1,0 | Schale bei S_phi = 0,66 | 0,632 | -1,328 | -4,127 | -0,170 / -3,944 / -0,013 | **-0,595** | 0,904 |
| 2,29 | (b) R_h = R_Ball | 0,334 | -3,649 | -12,02 | -0,085 / -11,49 / -0,44 | -0,440 | 1,123 |
| 3,0 | Wand/aussen | 0,202 | **-4,200** | **-14,30** | -0,016 / -12,17 / -2,11 | -0,308 | 1,321 |
| 5,0 | (c) umschliesst | 0,027 | -1,971 | -7,104 | 0 / -1,51 / -5,60 | -0,054 | 1,956 |

- Je Knotenmenge ist die Bindung am staerksten, wenn die koppelnde Schale bei S_phi ~ 0,66 bis 0,76 sitzt.
  - Grosser Ball: F1A -0,568 bei R_h = 6,5; Torus F1B -0,603 bei R_h = 6,5, <S_phi>_s = 0,74.
  - Das bestaetigt (2) im Kern. Die Hand-Zahl -2/3 wird nicht erreicht, weil die Schale einen Bereich von S_phi
    ueberstreicht.
  - Mitte je Knotenmenge: -0,401. Verhaeltnis Mitte/Wand: 0,71 (F1A), 0,67 (F1B), 0,65 (F2z klein).
- Die Gesamtenergie waechst mit dem Knotenvolumen. Ihr Minimum liegt knapp ausserhalb von R_Ball: R_h = 7,5 (gross)
  bzw. 3,0 (klein) bei v = 1. Die Schale liegt dann noch ueberwiegend in der Wand.
- Eine selbstaehnliche Reihe (F1S, w = R_h/2) entspricht einer kappa-Reihe. Ihr Minimum der Gesamtenergie liegt dort,
  wo der dicke Knoten den ganzen Ball umhuellt. M_b ist dort vom Kasten abgeschnitten, deshalb nur E_int berichtet.

## 5. gJ-Term und Gegenproben

- **gJ:**
  - Koaxial (Radius-Reihe, Verschiebung entlang der Achse): |G|/|A1| <= 1,1e-16. Das Azimutintegral von e^{2 i phi}
    ist exakt null, auch auf dem symmetrischen Gitter.
  - Verschiebung in der Knotenebene (F2x): |G|/|A1| bis 0,095 (klein) bzw. 0,26 (mittel), am groessten weit aussen,
    wo E_U klein ist.
  - Der moegliche Anteil |gJ| c |G| / |E_U| mit |gJ| = 1,657 (Codex' Schranke) und v = 1:
    - in der Wand <= 0,07 (klein) bzw. 0,03 bis 0,18 (mittel)
    - am Aussenrand der Wand (d = 8, grosser Ball) bis 0,29
    - weit aussen bis 0,48
  - Im Zeitmittel ist der Term null (e^{2 i omega t}). Ein Knoten, der mit omega isorotiert, koennte ihn neben der Achse
    als statischen Gewinn mitnehmen. Das liegt ausserhalb des statischen Produktansatzes.
- **Algebra:** Die direkte Differenz Int [U(S_phi + S_b) - U(S_phi) - U(S_b)] gegen c A1 + c^2 A2 stimmt in allen
  Lagen auf <= 7,5e-14 relativ. Die Kreuztermformel der Leitung ist damit auch numerisch bestaetigt (D1).
- **Quadratur:**
  - 3D h = 0,1 gegen 2D h = 0,01: <= 5,2e-5 relativ (Torus-Knick), sonst <= 1e-8.
  - 3D h = 0,2 gegen 0,1: <= 1,4 % (kleinster Knoten), Radius-Reihe <= 0,11 %.
- **Hopfzahl der Ansatzknoten** (N = 128, h = 0,06 bis 0,09):
  - Whitehead-Integral: -0,978; -0,958; -0,976; +0,978.
  - Fluss durch die Halbebene: -0,988; -0,978; -0,987; +0,986.
  - Also |h| = 1 bis auf den Diskretisierungsfehler.

## 6. Vergleich mit Codex (zentriert; resonance-20260930/qball-hopf-pilot/BINDING-CHECK.json, nur gelesen)

- **Codex:**
  - Ball: omega^2 = 0,797677, q = 189,14.
  - Knoten: kompakte Hedgehog-Hopftextur, Traegerradius R; Kernring bei etwa 0,28 R, also ~1,07 bei R = 3,80.
  - Parameter: v = mu = kappa = gJ = 1.
  - Produktansatz beim getrennten Optimum R = 3,803: Ueberlapp **-4,01**.
  - Mit gemeinsamer Isorotation, optimaler Ladungsteilung und freiem R: -4,31 bei R = 3,89. Vorteil 4,16, also
    0,96 % von E_sep = 431,8.
- **Hier, gleiche Kopplung, v = 1:**
  - Ball: omega^2 = 0,8 (Q = 186,1, E_Q = 181,9).
  - Statischer Knoten, keine Ladungsteilung, feste Formen.
  - Zentrierter Knoten mit Kernring 1,0 (F1A, w = 0,75): **-4,13**. Zum Vergleich: Kernring 1,5 gibt -7,26; ein
    dicker Knoten mit Kernring 1,0 (F1S, w = 0,5) -2,12; der Torus R_h = 2, a = 1,5 -4,68.
  - Die Zahl mit Kernring ~1 stimmt mit Codex' -4,01 auf 3 % ueberein, bei anderem Profil. Relativ zu
    E_Q + E_H (E_H ~ 250 bis 276) sind das etwa 0,9 %.
- **Unterschiede:**
  - Profil: Polynom mit kompaktem Traeger gegen sinh-Profil mit exponentiellem Schwanz.
  - Isorotation, Ladungsteilung und freies R nur bei Codex; sie vergroessern dort den Vorteil von 4,01 auf 4,16.
  - omega^2 = 0,7977 gegen 0,8.
  - R bei Codex optimiert, hier gerastert.
- **Was hier neu dazukommt, die Lageabhaengigkeit:**
  - Beim kleinen Ball (Codex' omega) liegt die koppelnde Schale eines Knotens mit Kernring ~1 schon bei zentrierter
    Lage in der Wand (<S_phi>_s = 0,63 S0). "Zentriert" und "Schale in der Wand" sind dort fast dasselbe.
  - Beim grossen Ball bindet ein Knoten derselben Groesse (F2z mittel) in der Wand 2,5-mal so tief wie in der Mitte:
    -5,81 gegen -2,32 bei v = 1.

## 7. Stufe B: offen (mit Kostenschaetzung)

Der Stufe-A-Code lief um 10:52:46 (Rauchtest), vor der 60-min-Grenze. Nach der Abstimmung mit Codex (Nachricht der
Leitung waehrend Stufe B) sollte Stufe B nur die aussermittige Lage mit der Schale in der Wand pruefen, "falls billig". Parameter wie Codex:
v = mu = kappa = 1, grosser Ball. Versucht habe ich:

| Lauf (.69, Zeit UTC) | Methode | Ausgang |
|---|---|---|
| hopf1b06, 09:05 bis 09:07 | 3D, Kasten um den Knoten L = 5, h = 0,1, L-BFGS | Knoten abgewickelt: E 284 auf 0, Hopfzahl -0,96 auf 0 |
| hopf1b06f, 09:08 bis 09:11 (von mir gestoppt) | 3D, gebremster Newton-Fluss (arrested Newton flow), dt = 0,008 | Hopfzahl blieb bei -0,87, aber E fiel auf 147,6, unter die bekannte h = 1-Untergrenze ~191 (Sutcliffe E_1 = 1,21, umgerechnet auf v = kappa = 1), also Gitterartefakt |
| hopf1crauch bis crauch4, 09:13 bis 09:20, cpu6 | 2D-Achsensymmetrie-Reduktion, exakt fuer koaxiale Lagen (Startenergie 286,6 gegen 3D 284,0, also Reduktion geprueft); Achse und Rand fest | Fluss bei dt = 0,004 und 0,003 instabil; L-BFGS wickelt ab (Grad 0,07); stabiler Fluss dt = 0,001 wickelt ebenfalls ab (Grad 1 auf 0, E auf 14,6 < 84 = strenge Vakulenko-Kapitansky-Schranke) |

- **Folgerung:** Mein Relaxierer haelt den h = 1-Knoten auf diesen Gittern nicht. Die Ursache ist nicht gefunden.
  Verdacht: Der Vorwaertsdifferenz-FS-Term unterschaetzt die Energie der schrumpfenden Roehre. Das ist numerisch,
  nicht physikalisch, denn die Kontinuumsschranke ist verletzt. **Keine Stufe-B-Zahl wird berichtet.**
- **Kosten bis zu einer belastbaren Stufe B:**
  - Zuerst eine Eichprobe: das bekannte h = 1-Minimum des reinen Faddeev-Skyrme-Modells (mu = 0, E = 1,21 in
    Sutcliffe-Einheiten, also ~191 bei v = kappa = 1) reproduzieren, bevor der Ball dazukommt.
  - Moeglicher Weg: 2D-Reduktion mit symmetrischer Diskretisierung des q^2-Terms (zentrierte Ableitungen auf versetztem
    Gitter) oder 3D mit h <= 0,05 (8 Mio. Punkte; auf der P4000 bei 1,5 GB freiem Speicher nicht, auf der P5000 nur mit
    Ollama-Pause).
  - Geschaetzt 1 bis 2 h Code und Tests, danach unter 10 min je Lage.
- **Was ohne Relaxation gilt (D6, Standardargument):**
  - Mit exakten Einzelloesungen (Ball bei festem Q, relaxierter Knoten) liegt die relaxierte Verbundenergie
    hoechstens bei E_Q + E_H + E_int^prod.
  - Die Anziehung bleibt als obere Schranke also erhalten, sobald E_int^prod mit dem relaxierten Knoten negativ ist.
  - Ob sich der bevorzugte Ort nach Relaxation verschiebt, ist offen.

## 8. Latten (v3)

- **L1 kann scheitern:** ja. (3) ist fuer eine Knotenform tatsaechlich knapp gescheitert. (2) haette mit einem Minimum
  im Ballinneren scheitern koennen.
- **L2 Gegenprobe:**
  - Algebra-Gegenprobe und 2D gegen 3D.
  - Codex' zentrierter Wert, unabhaengig: -4,01 gegen -4,13.
  - SPIN-1 kommt schriftlich auf dieselbe Kreuzterm-Formel.
- **L3 Numerik:** zwei 3D-Stufen und 2D-Referenz, Fehler <= 1,4 % grob und <= 5e-5 fein.
- **L4 schon bekannt:**
  - Die Kreuzterm-Algebra ist elementar.
  - Die Lageabhaengigkeit Wand vor Mitte folgt aus g(S) = S(-2 + 1,5 S) mit Minimum bei 2/3 und ist fuer dieses
    Modell neu gerechnet.
  - Naechster Literaturverwandter nach SPIN-1: Bai et al. 2022 (Q-Ball am Monopol).
- **L5 Messbezug:** keiner. Das ist eine modellinterne Aussage (Neuausrichtung 22.09.: kein Datenanschluss).

## 9. Grenzen

- Produktansatz ohne Rueckwirkung: Ball und Knoten sind starr, Q ist fest und phi unveraendert.
- Die Knoten sind Ansaetze, keine Loesungen. Ihre Groesse ist als Parameter gerastert (entspricht kappa/v).
- Nur statisch: keine Isorotation, keine Ladungsteilung (die rechnet Codex).
- Der gJ-Term ist nur fuer statische Knoten ausgewertet.
- Bindung im Produktansatz ist weder eine gebundene Loesung noch Stabilitaet. Ueber Spin und Fermionen sagt die
  Rechnung nichts.

## 10. Dateien

- Code:
  - hopf1.py (Stufe A)
  - hopf1b.py (Stufe B 3D, verworfen)
  - hopf1c.py (Stufe B 2D, verworfen)
  - kette-a.sh
- Rechenort: .69, /home/fmh/fmhc-physics-remote/runde10-hopf1/, Spuren p4000a (GPU, float64) und cpu6; Zeiten UTC:
  - Rauchtest cpu6: 08:52:46 bis 08:52:52.
  - Zeittest p4000a: 08:53:45 bis 08:54:06.
  - Stufe A omega^2 = 0,6: 08:54:31 bis 08:56:25.
  - Stufe A omega^2 = 0,8: 08:56:25 bis 08:56:55.
- Ausgaben in laeufe/:
  - A-w060.json und A-w080.json (alle Lagen, drei Gitter, Hopfzahlen, Tabelle)
  - LAUF-*.log
  - B-w060.json und CRAUCH4.json (Stufe-B-Fehlversuche)

## Einfach gesagt

Wir haben ausgerechnet, ob ein verknoteter Wirbel (Hopf-Knoten) an einem Q-Ball kleben bleibt, wenn man die beiden
einfach uebereinanderlegt. Er wird immer angezogen, und am staerksten dort, wo der Ball an seinem Rand ausduennt, nicht
in seiner Mitte. Die Leitung hatte das so vorhergesagt; nur ihr Zahlenwert fuer die Mitte war etwas zu hoch. Bei einer
von drei Knotenformen kippt die Anziehung schon knapp unter der vorhergesagten Grenze in Abstossung, weil die Ballmitte
etwas dichter ist als angenommen. Ob der Knoten auch nach dem "Zurechtruckeln" beider Objekte am Rand bleibt, konnten
wir noch nicht pruefen, weil unser Rechenverfahren den Knoten dabei kaputtmacht.
