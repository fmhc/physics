# ERGEBNIS S301-1: Schwarzschild-Referenzbahn auf Netz V mit Netzverfeinerung

- Forschungs-Agent (Claude, Opus 5.5) fuer die Leitung claude-primary. Rechenfreigabe der Leitung 09.10.2026.
- Karte: KARTE-S301-1.md (eingefroren 20:07:25 CEST, sha256 9ce6da92...). VORAB-S301-1.md (eingefroren 20:22:28 CEST,
  sha256 b976f49d...). Text ab 20:44:18 CEST (date).
- Laeufe auf der .69 ueber kleintest.sh (UTC; CEST = UTC + 2):
  - H1 18:22:29 bis 18:26:22, cpu2, 233 s
  - H2 18:22:29 bis 18:30:09, cpu3, 460 s
  - H3 18:30:16 bis 18:30:44, cpu4, 27 s
  - H4 18:30:51 bis 18:40:51, cpu2, **Zeitgrenze 600 s erreicht** (siehe Abschnitt 6)
  - H5 18:30:51 bis 18:35:49, cpu3, 298 s
  - H6 18:30:51 bis 18:36:39, cpu4, 347 s
  - Zusammen 1966 s = 32,8 min (Grenze 40 min). Rauchtests r1 bis r6 jeweils <= 15 s.
- **Art:** Konsistenzcheck. Alles synthetische Gitterrechnung. Keine neue Physik, keine Messdaten, keine Beobachtungsbestaetigung.
- Kennzeichen:
  - [E] gerechnet
  - [M] Schreibtisch
  - [N] nach Sicht auf Werte, beschreibend, ohne Urteil
  - [H] Hypothese

## 1. Ergebnis zuerst

| Nr | Kartenwortlaut (Kurz) | Urteil | Kennzahl (gewertete Lesart T, ausser K0/K6) |
|---|---|---|---|
| K0 | Pipeline mit analytischer Metrik: P = 1 auf 1e-3 (r_p/l >= 4, beide U) | **eingetroffen** | Stufe 1: max abs(P - 1) = 6,7e-4; Stufe 2: max 3,9e-4 (18 Bahnen) |
| K1 | nur erste Ordnung: P_unendlich = 7/6 auf 0,01 | **nicht eingetroffen** | Normale 123: S301 1,423 / 1,277 / 1,187 / 0,865; S2 3,554 / 2,244 / 1,768 / 1,174 (r_p/l = 3, 4, 6, 8). Ausgleich q = 2: P_unendlich ~0,93 bzw. ~0,92 |
| K2 | volle Felder: P_unendlich in [0,99; 1,01], beide U | **nicht eingetroffen** | Mittel der Normalen: S301 1,132 / 1,006 / 0,940 / 0,661; S2 2,953 / 1,708 / 1,238 / 0,799. P_unendlich fuer jedes geprufte q < 0,82 |
| K3 | monoton, q in [1,5; 3,5], beide U | **nicht eingetroffen** | S301: Fehlerquadratsumme am kleinsten am Gitterrand q = 0,5. S2: q ~ 3, monoton. Verlangt sind beide |
| K4 | Bahnlagenspanne bei r_p/l = 8 < 1e-2, Abnahme 4 -> 8 >= Faktor 2,5 | **nicht eingetroffen** | Spanne 0,178 (S301) bzw. 1,81 (S2); Abnahme 3,04 bzw. 3,09 (dieser Teil erfuellt) |
| K5 | absolute Lagenspanne in rad bei r_p/l = 6: S301/S2 in [0,8; 1,25] | **eingetroffen** | 0,01453 / 0,01353 rad = 1,074 |
| K6 | Torus: abs(P_32 - P_40) <= 2e-3 (roh, r_p/l <= 6) | **nicht eingetroffen** | z. B. Stufe 2, r_p = 3, S301, Normale 001: 0,758 gegen 0,918; Stufe 1, r_p = 3, S301: 1,785 gegen 1,913 |

- Weil K6 scheitert, sind K1 bis K5 laut VORAB mit der Torus-Lesart **T** gewertet.
- Die Rohwerte stehen in Abschnitt 3.
- **Kernaussage:**
  - Bei r_p/l = 3 bis 8 und Torusgroessen L = 32/40 reproduziert die Netzrechnung die Schwarzschild-Drehung **nicht** auf
    Prozentniveau. Sie konvergiert auch nicht erkennbar dorthin.
  - Ursache sind Fehler in Newtonscher Ordnung, die nicht von U abhaengen (K5 eingetroffen). Dazu kommen Torusreste in
    der zweiten Ordnung.
  - Ein Widerspruch zur ART ist das nicht. Der Test erreicht bei dieser Aufloesung die noetige Genauigkeit nicht.

## 2. Was gerechnet wurde (Kurzfassung; Einzelheiten VORAB)

- **Felder:** bn_felder.py (Kopie von bn.py) pert, Quelle P0, L = 32 und 40.
  - Kontrollen wie BETA-NETZ-V [E]:
    - a1 = -q W mu1 auf 5e-16 bzw. 7e-16
    - Imaginaerreste <= 8e-15
    - Richardson der Quelle zweiter Ordnung 1,3e-5
    - A = 0,056271 bzw. 0,056270 (BETA-NETZ-V: 0,05627)
- **Metrik:**
  - ln N = s mu1 + s^2 (mu2 - mu1^2/2)
  - ln psi^4 an Kantenmitten = 2 s a1 + s^2 (2 a2 - a1^2)
  - K1: N = 1 + s mu1 und psi^4 = (1 + s a1)^2
  - s so gewaehlt, dass r_g,eff/r_p = 1/272 (S301) bzw. 1/3000 (S2); e = 0,3
- **Lesart T:**
  - Erste Ordnung mit der periodischen Kontinuums-Green-Funktion (Ewald) korrigiert. Fit c = -0,0562726; Rest
    1,3e-3 relativ (rms, r = 4 bis 20,5).
  - Ewald-Probe: G - 1/r - (2 pi/3V) r^2 ist bei r < 5 auf 3,8e-7 konstant.
  - Zweite Ordnung 1/V-extrapoliert aus L = 32 und 40.
  - nu2 unterscheidet sich zwischen L = 32 und 40 um 15 % (rms). Die erste Ordnung nach Ewald-Korrektur um hoechstens
    4e-4 relativ (r = 3 bis 16) [E].
- **Stufe 1:** Quadratur auf Schalenprofilen.
- **Stufe 2:** 3D-Geodaeten, DOP853, rtol 1e-12, MLS mit R = 2,35 l, 85 bis 88 Punkte je Abfrage.
  - P = Delta phi / Delta phi_Ref
  - Delta phi_Ref: analytische isotrope Schwarzschild-Metrik mit den gemessenen r_p, r_a und demselben r_g,eff.

## 3. Tabellen [E]

### 3.1 Stufe 2, Lesart T, volle Felder (P je Normale; Delta phi in rad)

| r_p/l | U | P (001) | P (111) | P (123) | Mittel | Spanne P | Delta phi 001 / 111 / 123 | Delta phi_Ref | Kippung max (rad) |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 1/272 | 0,672 | 1,548 | 1,176 | 1,132 | 0,876 | 0,03633 / 0,08311 / 0,06294 | 0,0538 | 0,092 |
| 4 | 1/272 | 0,716 | 1,257 | 1,046 | 1,006 | 0,541 | 0,03861 / 0,06757 / 0,05615 | 0,0538 | 0,043 |
| 6 | 1/272 | 0,792 | 1,063 | 0,964 | 0,940 | 0,271 | 0,04265 / 0,05718 / 0,05183 | 0,0538 | 0,0084 |
| 8 | 1/272 | 0,563 | 0,741 | 0,678 | 0,661 | 0,178 | 0,03032 / 0,03987 / 0,03650 | 0,0538 | 0,014 |
| 3 | 1/3000 | -2,035 | 7,584 | 3,309 | 2,953 | 9,62 | -0,00990 / 0,03663 / 0,01595 | 0,00484 | 0,106 |
| 4 | 1/3000 | -1,251 | 4,357 | 2,017 | 1,708 | 5,61 | -0,00607 / 0,02105 / 0,00974 | 0,00484 | 0,064 |
| 6 | 1/3000 | -0,319 | 2,479 | 1,555 | 1,238 | 2,80 | -0,00154 / 0,01199 / 0,00752 | 0,00484 | 0,028 |
| 8 | 1/3000 | -0,217 | 1,597 | 1,018 | 0,799 | 1,81 | -0,00105 / 0,00773 / 0,00492 | 0,00484 | 0,013 |

Bei r_p/l = 8 gab es nur 5 Perizentren (4 Abstaende) statt 6; gemittelt ueber 4 (Abschnitt 6).

### 3.2 K1 (nur erste Ordnung), Stufe 2, Normale 123

| r_p/l | T, S301 | T, S2 | roh_gross, S301 | roh_gross, S2 |
|---|---|---|---|---|
| 3 | 1,423 | 3,554 | 1,569 | 2,845 |
| 4 | 1,277 | 2,244 | 1,836 | 5,005 |
| 6 | 1,187 | 1,768 | 3,158 | 15,49 |
| 8 | 0,865 | 1,174 | 4,747 | 35,80 |

### 3.3 Rohlesart (Torus unkorrigiert), Stufe 2, Mittel der Normalen

| r_p/l | roh_gross S301 | roh_klein S301 | roh_gross S2 | roh_klein S2 |
|---|---|---|---|---|
| 3 | 1,227 | 1,397 | 2,318 | 3,501 |
| 4 | 1,490 | 1,948 | 4,322 | 8,066 |
| 6 | 2,716 | 4,26 (nur 001, 111) | 14,73 | fehlt (Zeitgrenze) |
| 8 | 4,199 | - | 35,20 | - |

Der Torus waechst mit der Bahngroesse und dominiert (Hintergrund ~ r^2/V in erster, ~ r^4/V in zweiter Ordnung) [E, M].

### 3.4 Stufe 1 (Quadratur), Auswahl

| Lesart | U | r_p/l = 3 | 4 | 6 | 8 |
|---|---|---|---|---|---|
| analytisch | 1/272 | 0,99975 | 0,99975 | 0,99975 | 0,99975 |
| analytisch | 1/3000 | 1,00067 | 1,00067 | 1,00067 | 1,00067 |
| T, voll | 1/272 | 1,427 | 0,547 | 1,035 | 0,708 |
| T, voll | 1/3000 | 5,45 | -5,07 | 1,90 | 0,979 |
| roh_gross, voll | 1/272 | 1,785 | 1,247 | 2,935 | 4,306 |
| roh_klein, voll | 1/272 | 1,913 | 1,760 | 4,421 | 6,66 |

Stufe 1 ist bei den Netzfeldern unruhiger als Stufe 2. Die Schalenmittel mischen die zehn Eckarten, der Spline
schwingt [N].

### 3.5 K0 und K0' (analytische Metrik auf den Probenpunkten von L = 40)

- K0, Stufe 2: P zwischen 0,99975 und 0,99976 (S301) bzw. 0,99965 und 1,00039 (S2). Kippung <= 2e-8 rad;
  Hamilton-Rest <= 1e-14.
- Die Abweichung bei S301 (-2,5e-4) passt zu den abgeschnittenen U^3-Gliedern: grob (pi/2)(r_g/p)^2 = 1,3e-5 rad [M].
- Bei S2 streut Delta phi_Ref je Normale um 4,6e-4, obwohl die Bahn identisch ist (Delta phi gleich auf 1e-12). Die
  Gegenprobe mit 200 Knoten weicht in Stufe 1 um 1,2e-4 relativ ab.
- Fuer S2 liegt die Rechengenauigkeit also bei einigen 1e-4 [E, N].
- K0' (ohne r^k-Vorkonditionierung, r_p = 6, Normale 001) [E, beschreibend]:
  - P = 0,983 (S301) bzw. 0,893 (S2)
  - Die MLS-Interpolation des reinen 1/r-Felds kostet ohne Vorkonditionierung 1,7 % bzw. 11 %. K0 prueft wegen
    VORAB-Punkt 4 diese Fehlerquelle nicht.

### 3.6 Ausgleich P = P_unendlich + C x^q, x = l/r_p (Handrechnung, Stufe-2-Mittel, Lesart T) [M]

| q | S301: P_unendlich | S301: Fehlerquadratsumme | S2: P_unendlich | S2: Fehlerquadratsumme |
|---|---|---|---|---|
| 0,5 | 0,076 | 0,0165 | -2,51 | 0,164 |
| 1,5 | 0,646 | 0,0247 | 0,182 | 0,066 |
| 2 | 0,715 | 0,0290 | 0,506 | 0,043 |
| 3 | 0,781 | 0,0370 | 0,818 | 0,041 |
| 4 | 0,813 | 0,0440 | 0,967 | 0,076 |

- Fuer kein q liegt P_unendlich in [0,99; 1,01] (K2).
- S301 hat sein Minimum am Gitterrand q = 0,5. Die Abnahme beschleunigt sich zu grossen r_p hin (0,94 -> 0,66); das
  passt zu keinem konvergierenden Potenzgesetz (K3).

## 4. Nachtraege nach Sicht (beschreibend, ohne Urteil) [N]

1. **Anisotropie in Newtonscher Ordnung.**
   - Die absolute Lagenspanne von Delta phi ist fuer beide U praktisch gleich:
     - r_p = 3: 0,0468 gegen 0,0465 rad
     - r_p = 4: 0,0290 gegen 0,0271 rad
     - r_p = 6: 0,0145 gegen 0,0135 rad
     - r_p = 8: 0,0096 gegen 0,0088 rad
   - Sie faellt etwa wie (l/r_p)^1,6, nicht wie (l/r_p)^2.
   - Relativ zum 1PN-Signal (0,054 bzw. 0,0048 rad) ist das bei S2 grob elfmal groesser. Daher die grossen S2-Werte.
2. **Beta-Anteil fuer sich.**
   - Die Differenz P_voll - P_erste (Normale 123, Lesart T) isoliert den mu2-Beitrag zum Takt; die ART erwartet -1/6.
   - Ergebnis:
     - S301: -0,248 / -0,231 / -0,224 / -0,187
     - S2: -0,245 / -0,227 / -0,213 / -0,156
   - Beide Reihen naehern sich mit wachsendem r_p dem ART-Wert -0,167. Das ist nur eine Normale, und die Differenzbildung
     war nicht im VORAB festgelegt.
3. **Elimination ueber zwei U.**
   - (Delta phi_S301 - Delta phi_S2)/(Delta phi_Ref,S301 - Delta phi_Ref,S2) aus den Normalen-Mitteln: 0,952 / 0,937 /
     0,910 / 0,647.
   - Das entfernt den U-unabhaengigen Newton-Anteil.
   - Der Abfall bei r_p = 8 deutet auf einen U-abhaengigen Rest. Kandidaten: die Torus-Extrapolation zweiter Ordnung bzw.
     der r_g,eff-Fit im Bereich [14,9; 20], wo nu2 am staerksten vom Torus abhaengt [H].
4. **Ebenenkippung.** Bis 0,11 rad ueber 5 Umlaeufe (Normale 123, r_p = 3), fallend mit r_p. Analytisch <= 2e-8 rad;
   also eine Eigenschaft der Netzfelder bzw. ihrer Interpolation, nicht des Integrators.
5. **Hamilton-Rest.**
   - Bis 2e-5 bei r_p = 3 (Netzfelder), analytisch 1e-14.
   - Ursache: Die MLS-Kraft nutzt den Gradienten des lokalen Polynoms, nicht die exakte Ableitung des Interpolanten.
     Die Kraft ist also nicht streng konservativ (Abschnitt 6).

## 5. Bedeutung und Grenzen

- **Konsistenzcheck nicht bestanden, aber auch nicht widerlegt.**
  - Bei r_p/l <= 8 sind die Abweichungen des statischen Netzfelds von 1/r in Newtonscher Ordnung bereits zu gross. Sie
    betragen relativ ~1e-3 (Ewald-Rest) und erzeugen 0,01 bis 0,05 rad Praezession je Umlauf, abhaengig von der Lage.
  - Das 1PN-Signal (0,054 rad bei U(r_p) = 1/272) ist damit nicht auf Prozent sauber herauszuloesen.
  - Die Torusgroesse L = 40 (Bildabstand 80 l) reicht fuer Apozentren bis 15 l in zweiter Ordnung nicht.
- **Kein Bezug zu echten Sternen.**
  - Fuer S301 ist r_p/l > 1e39. Alle hier gesehenen Gittereffekte sind dort verschwindend (VORZUGSRICHTUNG.md).
  - Das Ergebnis betrifft nur die numerische Pruefbarkeit der Kette Netz -> Metrik -> Bahn.
- **Was fehlt [H]:**
  - deutlich groessere r_p/l (>= 20) mit Tori L >= 100, also eher GPU
  - oder eine Subtraktion der Gitter-Green-Funktion in erster Ordnung (Gitterrest statt Kontinuum)
  - oder Mittelung ueber viele Bahnlagen
  - Der Beta-Anteil (Nachtrag 2) sieht vielversprechend aus. Eine eigene Karte, die genau die Differenz voll minus erste
    Ordnung vorab festlegt, waere der billigste naechste Schritt [H].
- **Eigene Erwartungen (VORAB Abschnitt 3):**
  - V1 eingetroffen (K6 scheitert)
  - V2 eingetroffen
  - V3 nicht eingetroffen (T trifft K2 bei keinem U)
  - V4 eingetroffen (P(3) bei S2: 2,95)
  - V5 nicht eingetroffen (Kippung bis 0,11 rad)

## 6. Regelabweichungen

1. **H4 an der Zeitgrenze (600 s) abgebrochen.**
   - 38 von 42 Bahnen gerechnet. Es fehlen roh_klein r_p = 6: S301/123 sowie S2/001, 111, 123.
   - Ursache: Die Rohfelder brauchten mehr Schritte als geschaetzt (bis 30 000 Auswertungen je Bahn).
   - Kein Neulauf, um die Grenze von 6 Hauptlaeufen einzuhalten; kein Code geaendert.
   - Das Urteil zu K6 haengt nicht davon ab: Es ist schon mit den vorhandenen Paaren um den Faktor > 50 verfehlt
     (Intervallregel).
   - Teilergebnis: lauf/h4.json.teil.
2. **r_p/l = 8:** Die Integrationszeit (6,2 Newton-Perioden mit r_g,eff) lieferte in Lesart T nur 5 Perizentren. Delta
   phi ist dort ueber 4 statt 5 Abstaende gemittelt.
3. **Ausgleich P_unendlich, q per Handrechnung** an q = 0,5 / 1,5 / 2 / 3 / 4 statt auf dem 0,01-Gitter des VORAB
   (lokal kein Interpreter, kein siebter Lauf). Die Urteile K2/K3 sind gegen diese Vergroeberung robust (Abschnitt 3.6).
4. **MLS-Kraft nicht streng konservativ** (Polynomgradient statt exakter Ableitung); im VORAB nicht genannt. Folge:
   Hamilton-Rest bis 2e-5 bei r_p = 3.
5. Wie im VORAB angekuendigt: Praezisierungen 1 bis 4 und 6. P1-Gegenvariante und nicht-konformer Rest entfallen.
6. Vor dem VORAB in Rauchtests zwei Reparaturen (Quellecke 1/0, Probe ohne r = 0); nach dem Einfrieren keine
   Codeaenderung.

## 7. Pruefsummen

- Lokal geprueft mit `sha256sum -c` (lauf/PRUEFSUMMEN-69-lokal.txt): h1 bis h6 (json, log; h4 als json.teil) alle OK.
- Code lokal = .69 (lauf/PRUEFSUMMEN-69-nur-remote.txt, `sha256sum -c` OK):
  - bn_felder.py bbdae047...
  - s301_bahn.py 2599e57d...
  - bn.py 7234bf1b...
  - ew.py fa7b6417...
  - mn.py b36984d3...
  - tp.py 419d7da6...
- Nur auf der .69 (.69:fmhc-physics-remote/s301-1/lauf/, zu gross fuer den Laptop):
  - f32.npz aab49a96...
  - f40.npz b4d10891...
- Auszuege (aus den JSON per grep/sed, ohne Rechnung): lauf/h3-stufe1-auszug.txt, lauf/h4/h5/h6-stufe2-auszug.txt.

## Einfach gesagt

Wir haben zum ersten Mal echte Bahnen um eine Masse im Netz gerechnet. Ergebnis: Bei den Bahngroessen, die auf einen
normalen Rechner passen, stoeren die Netzmaschen und der begrenzte Rechenkasten die Bahn staerker als der Einstein-Effekt,
den wir messen wollten. Deshalb kommt nicht sauber Einsteins Bahndrehung heraus. Das heisst nicht, dass das Netz falsch ist,
sondern dass der Test noch zu grob ist. Ein Teil der Rechnung, der nur den eigentlichen Einstein-Anteil betrifft, laeuft schon
recht ordentlich auf den richtigen Wert zu. Fuer den Stern S301 selbst sagt das nichts, weil dort die Netzmaschen unvorstellbar
viel kleiner als die Bahn waeren.
