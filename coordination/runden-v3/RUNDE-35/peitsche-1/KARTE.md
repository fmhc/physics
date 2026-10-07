# PEITSCHE-1: Was erreicht in einer relativistischen Feldtheorie die Lichtgeschwindigkeit? (Runde 35)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 20:43:31 CEST (date), vor jeder Rechnung.
- **Anlass:** Finn ~19:12: "wenn man mal so ne peitsche ueberlegt dann gibts da ja auch super schnelle bereiche, ist das
  vllt lichtgeschwindigkeit". Schreibtischantwort in RUNDE-34/tetra-konzept/STRINGS-PEITSCHE.md, Abschnitt 3.
  - LICHT-1 (Runde 34): Ein Q-Ball wird in Kegelmulden hoechstens 0,42 c schnell.
  - Offen ist, ob ausgedehnte Objekte mit Zugspannung (Waende, Strings) c erreichen, und wie schnell Energie in
    drehenden Q-Baellen fliesst.
- Kennzeichen: [M] Mathematik (vorab ableitbar), [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

### Teil A: zusammenfallende Wand (Peitsche einer Membran)

- **Modell:** reelles phi^4, L = phi_t^2/2 - (grad phi)^2/2 - V, V = (phi^2 - 1)^2/4.
  - Wand phi = tanh(x/sqrt 2), Spannung sigma = 2 sqrt(2)/3 = 0,9428, Masse der Kleinschwingungen m = sqrt 2, Dicke ~ sqrt 2.
- **Kreisring (d = 2) bzw. Kugelschale (d = 3)**, Radius R0, anfangs in Ruhe: phi = tanh((r - R0)/sqrt 2), phi_t = 0.
  - Radiale Gleichung: phi_tt = phi_rr + (d - 1)/r phi_r - V'(phi).
- **Duennwand-Energie** (Nambu-Goto) [M]: d = 2: E = 2 pi sigma R gamma, also gamma = R0/R und v(R) = sqrt(1 - (R/R0)^2).
  d = 3: gamma = (R0/R)^2, v(R) = sqrt(1 - (R/R0)^4).
- **Zusammenfallzeit** [M]: d = 2: t_c = (pi/2) R0; d = 3: t_c = 1,31103 R0 (Integral von dx/sqrt(1 - x^4) von 0 bis 1).
- **Warum sie c erreicht:** Dieselbe Energie steckt in immer weniger Wandlaenge, also waechst gamma ohne Grenze. Die
  verkuerzte Dicke sqrt(2)/gamma = sqrt(2) R/R0 bleibt immer kleiner als der Radius, solange R0 >> sqrt 2. Die
  Duennwand-Naeherung bleibt also bis kurz vor dem Mittelpunkt gut, und v kommt c sehr nahe.
- **Energiefluss-Geschwindigkeit** |T^0r|/T^00 <= 1 ueberall, weil V >= 0 (dominante Energiebedingung) [M]. Kontrolle.
- **Musterschnelle** [H]: Die Nullstelle von phi ist ein Muster, keine Energie. Beim letzten Zusammenschlagen kann sie
  kurz schneller als 1 springen (wie der Schnittpunkt einer Schere), ohne dass Energie schneller als c fliesst.
- **Rest nach dem Zusammenfall** [L: Gleiser 1994, kugelfoermige Blasen in phi^4 bilden Oszillonen; 2D-Oszillonen
  langlebig, Gleiser/Sornborger 2000; L?]: ein lokalisierter, schwingender Klumpen mit Frequenz unter m = sqrt 2, also
  das reelle Gegenstueck eines Q-Balls.

### Teil B: drehende Q-Baelle (unser Modell M1, 2D)

- **Modell M1:** U(S) = S - S^2 + beta S^3, beta = 1/2, S = |psi|^2, L = |psi_t|^2 - |grad psi|^2 - U; omega_min^2 = 1/2.
- **Wirbel-Q-Baelle** psi = f(r) exp(i(omega t + m theta)), m = 1 bis 8 (Code RUNDE-06/regge/regge2d.py, RG-1; dort
  J = m Q auf 6,7e-16 bestaetigt).
- **Energiefluss-Geschwindigkeit** [M]: v_E(r) = |T^0theta|/T^00 = 2 omega m f^2/r / (omega^2 f^2 + f'^2 + m^2 f^2/r^2 + U).
  - Mit U >= omega_min^2 f^2 folgt die Schranke v_E <= omega/sqrt(omega^2 + omega_min^2) < 0,82 (bei omega^2 = 0,99:
    0,814). **Ein Q-Ball hat nirgends einen Bereich mit c.**
- **Abschaetzung** [H, grob]:
  - An der Ringmitte (f' = 0, lokales U/S = omega^2 - m^2/r^2) gilt v_E = m/(r omega).
  - Duenne NLS-Ringe (omega -> 1, Radius sqrt(2) m/sqrt(1 - omega^2), RG-1) geben v_E ~ sqrt((1 - omega^2)/2), also
    klein.
  - Duennwand-Ringe (omega nahe omega_min) geben v_E < sqrt(1 - omega_min^2/omega^2), auch klein.
  - Das Maximum liegt dazwischen, bei omega^2 ~ 2/3 mit v_E ~ 0,5.

## Test (Code-Agent)

- **Teil A:**
  - Radialer Loeser (d = 2 und d = 3), Leapfrog oder RK4, regulaer bei r = 0, absorbierender oder ausreichend grosser Rand.
  - R0 = 20, 40, 80 (d = 2) und R0 = 20, 40 (d = 3).
  - Gemessen:
    - Nullstelle R(t) und deren Schnelle (zentrale Differenz)
    - Zusammenfallzeit
    - v bei R = R0/2, R0/4, R0/10
    - groesstes |T^0r|/T^00 zu jeder Zeit
    - nach dem Zusammenfall: Energie in r < 10 und Frequenz am Ursprung bis t = t_c + 500 (beschreibend)
  - Zwei Gitterweiten. Die verkuerzte Wanddicke muss aufgeloest sein (dr <= sqrt(2) R/(5 R0) fuer die gemessenen R);
    das offenlegen.
- **Teil B:**
  - regge2d.py (oder eine eigene, gegen RG-1 gepruefte Fassung): Profile fuer m = 1, 2, 3, 5, 8 und omega^2 = 0,52 bis
    0,99 (mindestens 8 Werte).
  - v_E(r), dessen Maximum und Lage, Schranke je omega.
  - Kontrolle J = m Q, E und Q gegen RG-1-Werte.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A0 | Kontrolle: Energieerhaltung im radialen Loeser besser als 1e-4 relativ bis t_c; \|T^0r\|/T^00 <= 1 + 1e-6 ueberall und jederzeit | 95 % |
| A1 | Zusammenfallzeit innerhalb 2 % von (pi/2) R0 (d = 2) bzw. 1,311 R0 (d = 3), fuer R0 = 40 und 80 (d = 2) und R0 = 40 (d = 3) | 75 % |
| A2 | Wandschnelle bei R = R0/2, R0/4, R0/10 innerhalb 2 % der Duennwand-Formel fuer R0 = 80, d = 2 (Sollwerte 0,866; 0,968; 0,995) | 70 % |
| A3 | Die groesste gemessene Wandschnelle vor dem Zusammenschlag (R >= 2) liegt fuer R0 = 80, d = 2 ueber 0,99 | 75 % |
| A4 | [H] Kurz vor oder beim Zusammenschlag springt die Nullstelle schneller als 1 (Musterschnelle), waehrend A0 gilt | 40 % |
| A5 | [H] Nach dem Zusammenfall (d = 2, R0 = 20) bleibt bis t_c + 500 ein Klumpen mit mindestens 5 % der Anfangsenergie in r < 10, Frequenz unter sqrt 2 | 50 % |
| B0 | Kontrolle: J = m Q auf 1e-8; Q und E fuer gemeinsame Punkte innerhalb 1e-5 relativ zu RG-1 | 90 % |
| B1 | v_E <= omega/sqrt(omega^2 + omega_min^2) ueberall (Schranke) | 99 % |
| B2 | Das groesste v_E ueber alle gerechneten (m, omega) liegt zwischen 0,35 und 0,65 | 60 % |
| B3 | Fuer m >= 3 faellt das groesste v_E zu omega^2 -> 0,99 ab (Maximum im Innern des omega-Bereichs, nicht am oberen Rand) | 65 % |

**Bedeutung (vorab):**
- A1 bis A3 treffen ein: Ausgedehnte Objekte mit Zugspannung buendeln Energie wie eine Peitsche und kommen c beliebig
  nahe. Erreicht wird c nur im Grenzfall, ueberschritten nie (A0).
- B1 bis B3 treffen ein: Ein drehender Q-Ball hat nirgends Lichtgeschwindigkeit; Energie fliesst in ihm hoechstens etwa
  halb so schnell wie Licht.
  - Zusammen mit RG-1 (Regge-artige Huelle, alpha ~ 2) hiesse das: Der Regge-Turm drehender Q-Baelle braucht keine
    [H, Vergleich].
- A4 trifft ein: Bild fuer Finn: Der "Knall" ist eine Musterschnelle ueber c ohne Energietransport.
- A2 verfehlt: Kruemmungs- oder Abstrahlungskorrekturen sind groesser als gedacht. Beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber coordination/runden-v3/kleintest.sh, Spuren cpu oder p4000a (nicht cpu2, cpu5,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
