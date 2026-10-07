# FA-1 Farb-Analogie (Runde 8): Ergebnis

- Bearbeiter: Anthropic-Agent (Opus 5.5) im Auftrag der Leitung claude-primary.
- Ablauf:
  - Beginn 06:36 CEST
  - Plan eingefroren 06:54:05 (PLAN.md.eingefroren-20260930-0654)
  - Nachtrag A 07:07:53, vor jedem dyn-Ergebnis
  - Bericht geschrieben ab 2026-09-30 07:18:28 CEST (alles date)
- Explorativ (v3). Belegstufen:
  - [ES] exakte Schreibtischaussage mit Beweisskizze in PLAN.md
  - [N+K] numerisch mit Kontrolle
  - [N] numerisch
  - [H] Hypothese
  - [L] an der Quelle gelesen
  - [L?] nicht an der Quelle geprueft
- Rechnungen auf der .69 ueber kleintest.sh, Skript fa1.py (sha256 a78744c4557e174e...):

  | Lauf | Spur | Laufzeit | Log |
  |---|---|---|---|
  | ref | p4000a | 5 min 44 s | /home/fmh/fmhc-physics-remote/runde8-fa1/LAUF-ref.log |
  | dyn | p4000b | 6 min 45 s | /home/fmh/fmhc-physics-remote/runde8-fa1/LAUF-dyn.log |
  | fluss | p4000a | 5 min 31 s | /home/fmh/fmhc-physics-remote/runde8-fa1/LAUF-fluss.log |

  - Alle mit rc = 0.
  - Kopien liegen in lauf-69/, dazu die Ergebnisdateien ERGEBNIS-ref.json (8854d29b...), ERGEBNIS-fluss.json
    (2a836d1b...) und ERGEBNIS-dyn.json (4e1d1e9e...).
  - Rauchtests lokal: lauf-lokal/rauch.log und rauch2.log.
- Bezug:
  - Q_ref = 473,41306: einkomponentiger Ball bei g = 0 und omega^2 = 0,70 (Schiessverfahren, f0 = 1,0653921840576)
  - Gitter h = 0,1; J_ab = 1 fuer alle Paare
  - I_4 = int f^4 d^3x des Bezugsballs = 169,80

## 0. Ergebnis in fuenf Punkten

1. **Das 120-Grad-Dreieck ("Farbneutralitaet") gibt es als exakte ruhende Loesung, aber nicht als Grundzustand.**
   - Bei g < 0 ist der tiefste Ball bei gleicher Ladung der **gegenphasige Zweierball**: ein Kanal leer, zwei Kanaele
     mit psi_2 = +-i psi_1. Das entspricht eher einem "Meson" als einem "Baryon".
   - Der 120-Grad-Ball liegt dazwischen: um |g| I_4/12 ueber dem Zweierball, um |g| I_4/6 unter dem einkomponentigen
     Ball.
   - [ES], numerisch fuer 7 von 7 g-Werten bestaetigt [N+K].
2. **Der Stern traegt einen stationaeren Kreisstrom.**
   - Die Paarstroeme T_ab sind gleich gross, rund 10,95 bei g = -0,3, und haben denselben Umlaufsinn.
   - Je Kanal heben sie sich auf. Die Formel |T_ab| = (sqrt3/9)|g| I_4 trifft auf 0,03 % [N+K].
3. **Er ist ein Energiesattel, bleibt aber in der reibungsfreien Dynamik stabil, solange die Kopplung klein ist.**
   - Ueber T = 8000 bleiben Stoerungen beschraenkt bei g = -0,1 / -0,3 / -0,6 / +0,1. Bei g = -1,0 / +0,3 / +0,6 waechst
     die Stoerung.
   - Grund: gyroskopische Stabilisierung durch die Eigendrehung omega des Balls.
   - Die gemessenen langsamen Frequenzen treffen die Galerkin-Rechnung auf 3 bis 7 %: bei |g| = 0,1 beide Moden, bei
     g = -0,3 die Mode negativer Energie. Bei groesserem |g| weicht Galerkin um bis zu rund 40 % ab.
   - Mit Reibung (Gradientenfluss) zerfaellt der Stern immer zum Zweierball: 12 von 12 freien Laeufen [N+K].
4. **Die beiden Drehsinne bilden einen exakt entarteten inneren Zweizustand, also einen Pseudospin und keinen Raumspin.**
   - Eine Energiebarriere dazwischen gibt es nur bei festgehaltenen gleichen Amplituden (|g| I_4/18, gemessen 3,10 bei
     g = -0,3). Mit freien Amplituden gibt es keine: Der Weg fuehrt bergab ueber den Zweierball.
   - Geschuetzt ist der Drehsinn nur dynamisch. Eine Anfangsabweichung von 0,037 bleibt stehen, bei 0,128 kippt der
     Drehsinn hin und her [N].
5. **Reichweite:**
   - Die Analogie ist strukturell (Z_3-Phasen, Summe null, Chiralitaet wie im Dreiecks-XY-Magneten).
   - Es gibt keine SU(3)-Ladung, keine Eichfelder und keinen Einschluss. Der Ball ist weder Quark noch Nukleon.
   - Soll das Dreieck der Grundzustand sein, braucht die Formel einen Zusatzterm lambda sum|psi_a|^4 mit
     lambda > |g|/2 [Hand, H]. Das waere eine Erweiterung, keine Folgerung.

## 1. (a) Schreibtisch

| Aussage | Stufe | Beleg |
|---|---|---|
| Kopplungsenergie der Leitung bei gleichen Amplituden: -g A^4 sum cos(2 Delta theta), g < 0 frustriert, Minimum 120 Grad | [ES] | PLAN 1.1; stimmt |
| Mit freien Amplituden: punktweises Minimum bei g < 0 ist (S/2, S/2, 0) gegenphasig, -\|g\| S^2/4; 120 Grad nur -\|g\| S^2/6 | [ES] | PLAN 1.2 |
| Vollstaendige Liste der stationaeren Baelle mit festem innerem Vektor: K in {1/3, 1/4, 0, -1/6, -1/5, -1/4}, jeweils exakt N = 1 mit b = 1 + gK | [ES] + [N] | Stationaritaetsrest je Typ <= 1,1e-16 (ref); K-Werte auf 1e-16 |
| Grundzustand bei festem Q: g < 0 gegenphasig-2, g > 0 gleichphasig-3 (Kato + Cauchy-Schwarz + punktweise Schranke) | [ES] + [N+K] | Fluss E2/E4 unten |
| KANDIDAT 5.2 fuer N = 3, g < 0: Vakuumgrenze \|g\| <= 4(sqrt2 - 1) = 1,657 statt 1,243; Fenster omega^2_min = 1 - (1 + \|g\|/4)^2/2 | [ES] | "genau dann" in 5.2 gilt nur fuer g > 0 |
| 120 Grad ist stationaer (Z = sum c_a^2 = 0) und bricht C und die ungeraden Permutationen spontan; es bleibt eine verdrehte Z_3 | [ES] | PLAN 1.6 |
| Zu KANDIDAT Zeile 182: alpha_b - alpha_a in pi Z beschreibt Symmetrien, nicht Loesungen. Die 120-Grad-Phasen sind eine eigene Loesung, kein Symmetriebild | [ES] | |
| KANDIDAT 4.2 Folgerung 3 ("stationaer, kein Kanalstrom") gilt nur fuer reelle relative Phasen. Der Stern ist das Gegenbeispiel | [ES] + [N+K] | T_ab = 10,9495 im stationaeren Zustand (Fluss) |

**Energien bei Q_ref (ref, E_K - E_1; E_1 = 428,6268):**

| g | gleichph.-3 | gleichph.-2 | K = -1/9 (Weg) | **120 Grad** | kollinear | **gegenph.-2** | Reihenfolge |
|---|---|---|---|---|---|---|---|
| -1,0 | +38,68 | +32,03 | -21,38 | **-34,21** | -42,72 | **-56,80** | wie vorhergesagt |
| -0,6 | +27,15 | +21,55 | -12,20 | **-19,00** | -23,33 | **-30,19** | wie vorhergesagt |
| -0,3 | +15,19 | +11,72 | -5,87 | **-8,98** | -10,90 | **-13,85** | wie vorhergesagt |
| -0,1 | +5,45 | +4,13 | -1,91 | **-2,88** | -3,47 | **-4,37** | wie vorhergesagt |
| +0,1 | -5,87 | -4,37 | +1,86 | +2,78 | +3,32 | +4,13 | wie vorhergesagt (umgekehrt) |
| +0,3 | -19,00 | -13,85 | +5,45 | +8,03 | +9,53 | +11,72 | wie vorhergesagt |
| +0,6 | -42,72 | -30,19 | +10,51 | +15,19 | +17,83 | +21,55 | wie vorhergesagt |

- Alle 32 Profile konvergiert: Newtonrest <= 8e-14, Virial \|T + 3V\|/T zwischen 3,3e-4 und 8,7e-4.
- Erste Ordnung bei \|g\| = 0,1: Verhaeltnis (E_K - E_1)/(-g K I_4) zwischen 0,964 und 1,038 fuer alle Typen.
- Bei \|g\| >= 0,3 ist die zweite Ordnung sichtbar: Konkavitaet in gK, zum Beispiel 120 gegen Zweierball bei g = -1 mit
  22,59 gegen 14,15 in erster Ordnung.
- Gitterkontrollen:
  - Energiedifferenzen bei h = 0,05 weichen von h = 0,1 um hoechstens 0,003 ab (g = -0,3, alle Typen).
  - FD gegen Schiessverfahren: omega^2 0,699972 gegen 0,70, E 428,6268 gegen 428,6416 (3,5e-5 relativ).

## 2. (b) Kleiner Test

### 2.1 Gradientenfluss bei festem Q (fluss, tau = 600, 28 Laeufe)

| Laeufe | Start | Ende | Energie gegen Bezug |
|---|---|---|---|
| g = -0,3 frei, 6 Saaten | zufaellige Phasen, gleiche Amplituden (+1e-3) | **6 x gegenphasig-2**, alle drei Kanalpaare kommen vor | E = 414,77462 = E_anti2 auf <= 3e-16 |
| g = -0,3 frei, 3 Saaten | zufaellige Amplituden und Phasen | 3 x gegenphasig-2 | ebenso |
| g = -0,6 frei, 3 Saaten | wie oben | 3 x gegenphasig-2 | E = 398,43199 = E_anti2 |
| g = -0,3 gleiche Amplituden erzwungen, 6 Saaten | wie oben | **6 x 120 Grad** (5 x chi+, 1 x chi-), \|chi\| = 1,0000, Zw ~ 1e-14 | E = 419,64858802 = E_120; chi+ und chi- gleich auf 1e-16 |
| g = -0,6 erzwungen, 3 Saaten | wie oben | 3 x 120 Grad (1 x chi+, 2 x chi-) | E = 409,62524 = E_120 |
| g = +0,3 frei, 3 Saaten | wie oben | 3 x gleichphasig-3 (Zw = 1,00) | E = E_al3 |
| g = 0, 3 Saaten | wie oben | innerer Vektor unveraendert (n_a, Zw, chi gleich dem Start auf alle ausgegebenen Stellen), T_ab = 0 | E = E_1 |
| N = 1-Grenze, g = -0,3 | c = (1, 0, 0) | bleibt einkomponentig, Kanaele 2 und 3 exakt 0,0 | E = E_1 |

- Sattelpassage, gesehen in Lauf 1 (g = -0,3, frei):
  - tau = 1: Startnaehe zum Stern (chi = 0,95, Zw = 0,11, E = 419,95, also nahe E_120 = 419,65)
  - Danach trennen sich die Amplituden: n_min 0,32, dann 0,16 (tau 21), 0,017 (tau 41), 0 (tau 100).
  - Ende: E = 414,77 (Zweierball).
- Bei erzwungen gleichen Amplituden erbt der Endzustand das Vorzeichen der Startchiralitaet: 9 von 9 Laeufen.
- Stationaere Reste der Endzustaende <= 8e-14.

### 2.2 Zeitentwicklung ohne Daempfung (dyn, T = 8000, dt = 0,05, Schwamm ab r = 45)

| Lauf | Stoerung | max Abweichung (Start -> max) | chi-Bereich | Ende | Befund |
|---|---|---|---|---|---|
| 120 Grad, g = -0,1 | 1e-3 | 9,3e-4 -> 2,4e-3, Fenstermaxima flach (2,34e-3 bis 2,38e-3 in 8 Fenstern) | [0,99998; 1] | 120 Grad | **beschraenkt** |
| 120 Grad, g = -0,3 | 1e-3 | 6,9e-4 -> 2,0e-3, flach (1,98e-3 bis 2,02e-3) | [0,99999; 1] | 120 Grad | **beschraenkt** |
| 120 Grad, g = -0,6 | 1e-3 | 1,04e-3 -> 2,2e-3 | [0,99999; 1] | 120 Grad | **beschraenkt** |
| 120 Grad, g = -1,0 | 1e-3 | Rate 0,044, n_min -> 1e-4 | [-0,92; 1] | gegenphasig-2 | **instabil** |
| 120 Grad, g = +0,1 | 1e-3 | 1,2e-4 -> 9,6e-4, flach (9,44e-4 bis 9,56e-4) | [0,999998; 1] | 120 Grad | **beschraenkt** |
| 120 Grad, g = +0,3 | 1e-3 | Rate 0,0079, dann Schwappen (n_min 0,07) | [0,63; 1] | Schwappen | **instabil** |
| 120 Grad, g = +0,6 | 1e-3 | Rate 0,029, dann Schwappen | [-0,11; 1] | Schwappen | **instabil** |
| 120 Grad, g = 0 | 1e-3 | konstant 5,786e-4, T_ab = 0 exakt | 0,9999997 | 120 Grad | Kontrolle |
| einkomponentig, g = -0,3, Keim 1e-6 | - | lambda = 0,1138 (Zwei-Moden-Formel 0,1074) | - | Schwappen | Positivkontrolle |
| einkomponentig, g = -0,3, Keim 0 | - | Kanaele 2 und 3 exakt 0,0; dE 8e-8, dQ 1,6e-8 | - | einkomponentig | N = 1-Kontrolle |
| gegenphasig-2, g = -0,3 | 1e-3, Keim 1e-3 in Kanal 3 | 2,2e-3 -> 3,0e-3 | - | gegenphasig-2 | beschraenkt |
| 120 Grad, g = -0,3 | **0,05** | 0,037 -> 0,065 | [0,992; 1], kein Wechsel | 120 Grad (gestoert) | beschraenkt |
| 120 Grad, g = -0,3 | **0,15** | 0,128 -> 0,47, n_min 0,007 | [-0,995; 0,83], 11 bis 12 Wechsel je 500 | Schwappen zwischen chi+ und chi- | **Drehsinn kippt** |
| 120 Grad chi-, g = -0,3 | 1e-3 | 6,4e-4 -> 1,1e-3 | [-1; -0,999998] | 120 Grad chi- | beschraenkt, T_ab gespiegelt (-10,95) |

- **Kreisstrom:**

  | g | T_ab gemessen (Mittel) | Formel |
  |---|---|---|
  | -0,1 | 3,3920 | 3,3910 |
  | -0,3 | 10,9523 | 10,9495 |
  | -0,6 | 24,4503 | 24,4445 |
  | +0,1 | -3,1492 | 3,1483 im Betrag |

  - Die Kanalbilanz dQ_a/dt = sum_b T_ab gilt auf 4e-5 relativ.
  - Umlaufsinn bei g < 0 und chi = +1: 1 -> 3 -> 2 -> 1. Er kehrt sich mit chi um und mit dem Vorzeichen von g.
- **Langsame Frequenzen gegen Galerkin** (FFT von n_1, Aufloesung 0,0008):

  | g | gemessen | Galerkin | Abweichung |
  |---|---|---|---|
  | -0,1 | 0,0165 und 0,0526 | 0,0159 (-) und 0,0565 (+) | 4 % und 7 % |
  | -0,3 | 0,0558 | 0,0528 (-) | 6 % |
  | +0,1 | 0,0605 und 0,0141 | 0,0567 (-) und 0,0145 (+) | 7 % und 3 % |

  - Groesser werden die Abweichungen erst bei grossem e:
    - g = -0,3, (+)-Mode: 0,137 gegen 0,168
    - g = -0,6: 0,139 gegen 0,125 und 0,209 gegen 0,331
  - Galerkin ist nur in erster Ordnung in g genau.
- **Stabil gegen instabil** (7 von 7 wie in Nachtrag A):
  - Beschraenkt waren genau die Laeufe, in denen die Mode negativer Energie unter der Kontinuumsschwelle 1 - omega liegt:
    g = -0,1, -0,3, -0,6, +0,1.
  - Instabil waren genau die Laeufe, in denen sie darueber liegt: g = -1,0 / +0,3 / +0,6.
  - Grobe Frequenzen der wachsenden Schwingung (Nulldurchgaenge): 0,30 / 0,21 / 0,46, jeweils ueber der Schwelle
    0,258 / 0,141 / 0,120.
  - Das stuetzt den Mechanismus "Mode negativer Energie strahlt und waechst" [H, gestuetzt, nicht bewiesen]. Das lineare
    Spektrum der vollen Gleichung ist nicht gerechnet.
- **Mit Reibung:**
  - Im Galerkin-Modell gilt fuer gamma = 1e-3 bei allen g max Re lambda > 0 (1,1e-5 bis 4,5e-4). Das ist die
    Thomson-Tait-Chetaev-Instabilitaet, im Gradientenfluss (2.1) bestaetigt.

## 3. (c) Zweizustand

- **Gleich tief: ja, exakt.**
  - Eine ungerade Kanalpermutation bildet chi+ auf chi- bei gleichem Q ab [ES].
  - Numerisch E(chi+) = E(chi-) = 419,6485880153959 auf 1e-16 relativ, aus unabhaengigen Startwerten (Fluss).
- **Barriere:**
  - Bei festgehaltenen gleichen Amplituden (XY-artig) fuehrt der Weg ueber die kollineare Lage K = -1/9:

    | g | gemessen | \|g\| I_4/18 | Verhaeltnis |
    |---|---|---|---|
    | -0,1 | 0,973 | 0,943 | 1,03 |
    | -0,3 | 3,104 | 2,830 | 1,10 |

    Das sind 0,23 % bzw. 0,74 % der Ballenergie.
  - **Mit freien Amplituden keine Barriere:** K faellt monoton von -1/6 auf -1/4 zum Zweierball, dort entartet das
    Dreieck, dann steigt K wieder [ES].
  - Uebergangszustand zwischen zwei Paar-Grundzustaenden: kollinear (3/5, 1/5, 1/5), K = -1/5, E_koll - E_anti2 = 2,96
    bei g = -0,3.
- **Dynamisch** (g = -0,3):
  - Anfangsabweichung 0,037: kein Wechsel ueber T = 8000.
  - Anfangsabweichung 0,128: 11 bis 12 Drehsinnwechsel je 500 Zeiteinheiten, jeweils ueber eine Lage mit fast leerem
    Kanal (n_min 0,007).
  - Die dynamische Schutzgrenze liegt also bei einer Amplitudenabweichung zwischen 0,04 und 0,13 [N].
- Pseudospin, kein Raumspin:
  - Die psi_a sind Skalare (KANDIDAT 3.4), der Zustand ist radial (J_z = 0), und eine 2-pi-Drehung ist die Identitaet.
  - Der Drehsinn ist die Windungszahl w = +-1 der verdoppelten Phase auf dem Kanalring 1 -> 2 -> 3 -> 1.

## 4. (d) Literatur

- **Nicht-abelsche Q-Baelle** [L]:
  - Safian, Coleman, Axenides, "Some non-abelian Q-balls", Nucl. Phys. B 297 (1988) 498-514. Gelesen im Abstract
    (OSTI 5266707): "We extend this work to some simple models with symmetry groups SO(3) and SU(3)."
  - Selipsky, Kennedy, Lynn, "Non-Abelian Q-Stars", SLAC-PUB-4755 (1988), S. 3 gelesen:
    - Das Modell hat phi "in the SO(3) 5 representation: real, symmetric, and traceless".
    - Safian, Coleman und Axenides zeigten, dass es "the lowest energy solitons of the very similar SU(3)" enthaelt.
  - Unterschied zu uns: Dort bleibt eine nicht-abelsche globale Symmetrie ungebrochen, und der Ball traegt nicht-abelsche
    Ladung. Bei uns bleibt fuer g != 0 nur U(1) x diskret (KANDIDAT 3.2). Bei g = 0 ist die Formel U(3)-symmetrisch
    mit Feldern im Triplett, und der Stern ist dann nur ein gedrehter Einkomponentenball.
- **Dreiecks-XY-Antiferromagnet** [L]:
  - Kawamura, arXiv:cond-mat/0202109: "a well-known 120 degree spin structure, in which each XY spin on a plane makes an
    angle equal to +-120 degree with the neighboring spins"; Chiralitaet kappa = (2/3sqrt3) sum [S_i x S_j]_z, das
    Vorzeichen unterscheidet die zwei chiralen Zustaende.
  - arXiv:1202.1042 (Abstract): zwei getrennte Uebergaenge. Der obere ist ein Z_2-Bruch durch die Chiralitaet
    (Ising-Klasse).
  - Unser chi ist genau Kawamuras kappa, mit den verdoppelten Phasen als Spinwinkeln.
  - Wesentlicher Unterschied: XY-Spins haben feste Laenge. Unsere Kanalamplituden sind frei, deshalb entkommt das System
    der Frustration durch Leeren eines Kanals.
- **BIC-Ladungen unter C_n** [L]:
  - Zhen, Hsu, Lu, Stone, Soljacic, arXiv:1408.0237, Supplement E, Tabelle S1 (im PDF als TABLE I gedruckt), fuer
    einfach entartete Baender am Gamma-Punkt:
    - C3, Darstellung A: Ladung 1 + 3n, also +1, +4, -2
    - C4: A 1 + 4n, B -1 + 4n
    - C6: A 1 + 6n, B -2 + 6n
  - Definition q = (1/2pi) Umlaufintegral von grad phi(k), phi = arg(c_x + i c_y).
  - Veroeffentlicht in PRL 2014 [L?, Band und Seite nicht geprueft].
  - Struktureller Bezug [H]: In beiden Faellen legt die C3-Darstellung eine Windungszahl modulo 3 fest. Bei uns ist
    w in {0, +1, -1} gleich dem Eigenwert der verdrehten Z_3 (gleichphasig-3: w = 0, chi+-: w = +-1). Die Raeume sind
    verschieden (Kanalring hier, k-Raum dort); ueber einen physikalischen Zusammenhang der Zahlen ist nichts gesagt.
- **Gyroskopische Stabilisierung und Reibung** [L]:
  - Krechetnikov und Marsden, Rev. Mod. Phys. 79, 519 (2007), S. 2: "if a system with an unstable potential energy is
    stabilized with gyroscopic forces, then this stability is lost after the addition of arbitrarily small dissipation."
  - Ihr Beispiel ist der Lagrange-Kreisel mit zwei instabilen Richtungen, derselbe Typ wie unser Stern.
- **Eingebettete Eigenwerte negativer Energie werden instabil** [L?]: Cuccagna, Pelinovsky, Vougalter, CPAM 58 (2005) 1-29.
  Die Quelle lieferte HTTP 403, nicht gelesen.

## 5. Vorab gegen Ausgang (eingefrorene Tabelle, PLAN 2)

| Nr. | Ausgang | Wertung |
|---|---|---|
| E1 | Reihenfolge 7 von 7 g-Werten wie vorhergesagt, alle Baelle existieren bei Q_ref | getroffen |
| E1a | 0,964 bis 1,038 | getroffen |
| E1b | <= 8,7e-4 | getroffen |
| E2 | 9 von 9 bei g = -0,3 enden gegenphasig, E auf 3e-16, nie 120 Grad | getroffen |
| E3 | 6 von 6 enden 120 Grad, beide Drehsinne, E(chi+) = E(chi-) auf 1e-16 | getroffen |
| E4 | 3 von 3 gleichphasig-3 | getroffen |
| E5 | innerer Vektor unveraendert, E = E_1 | getroffen |
| E6 | Kanaele exakt 0,0 | getroffen |
| D1 | beschraenkt (Faktor 2,1 bis 3,0 gegen Start, Fenstermaxima flach), \|chi\| > 0,99998 | getroffen |
| D1a | g = -0,1: 4 % und 7 %; g = -0,3 gebundene Mode: 6 % | getroffen |
| D1b | \|T_ab\| auf 0,03 % getroffen; **\|dQ_a/dt\|/\|T_ab\| = 2,6e-3 bis 4,6e-3 statt < 1e-3** | **teils verfehlt**; das Kriterium war schlecht gestellt: Der Rest ist die von der 1e-3-Stoerung getriebene Schwingung, etwa delta Q_a nu ~ 0,02 [Hand]. Die Bilanz dQ_a/dt = sum T_ab gilt auf 4e-5 |
| D2 | g = -1,0 instabil (Rate 0,044), Ende gegenphasig-2 | Beobachtung; Wachstum war als moeglich markiert |
| D3 | +0,1 beschraenkt; +0,3 waechst (Rate 0,0079 < 1e-2); +0,6 waechst | getroffen (+0,6 war offen) |
| D4 | lambda 0,1138 gegen 0,1074 (6 %) | getroffen |
| D5 | exakt 0,0; dE 8e-8 | getroffen |
| D6 | beschraenkt | getroffen |
| D7 | T_ab = 0 exakt, beschraenkt | getroffen |
| D8 | 0,05 beschraenkt, 0,15 Drehsinnwechsel | getroffen (als [H] markiert) |
| D9 | Energie gleich (im Fluss 1e-16), T_ab gespiegelt | teils; "Verlauf gespiegelt" nicht pruefbar, weil die Zufallsstoerung eine andere Saat hatte (Planfehler) |
| C1 | 1,03 und 1,10 | getroffen |
| Nachtrag A | stabil gegen instabil 7 von 7 wie erwartet; Raten groesser als "langsam" | getroffen in der Einordnung |

## 6. Reichweite (ein Satz)

**FA-1 zeigt eine strukturelle Analogie:** Drei Kanaele der Gesamtformel koennen ihre verdoppelten Phasen zu einem
Z_3-Stern mit Summe null ordnen, und dieser Stern hat zwei Drehsinne wie die Chiralitaet eines frustrierten Dreiecks. Es
gibt dabei keine SU(3)-Farbladung, keine Eichfelder, keinen Einschluss und keinen Raumspin. Der Stern ist nicht der
Grundzustand, und nichts davon behauptet, der Ball sei ein Quark oder ein Nukleon.

## 7. Latten und Vorschlag

- L1 kann scheitern: ja, 20 vorab gebundene Punkte; D1b und D9 teils verfehlt.
- L2 Gegenproben:
  - g = 0 und die N = 1-Grenze
  - Positivkontrolle (einkomponentige Instabilitaet)
  - Gitter h = 0,05 und Schiessverfahren gegen FD
- L3 Numerik:
  - Reste <= 8e-14
  - Energieerhaltung in stabilen Laeufen <= 1,3e-6
- L4 bekannt:
  - Dreieckschiralitaet und Thomson-Tait-Chetaev sind Lehrbuch.
  - Nicht gefunden (nur kurz gesucht [L?]): die Aufhebung der Frustration durch Leeren eines Kanals und die gyroskopische
    Stabilitaet des Sterns in Mehrkomponenten-Q-Baellen mit diesem Paarterm.
- L5 Messbezug: keiner.
- **Vorschlag: parken.** Finns Frage ist beantwortet, einen Messbezug gibt es nicht. Moegliche Folgekarten [H]:
  - Lineares Spektrum des Sterns in der vollen Gleichung (FD-Eigenwertproblem), um die Stabilitaetsgrenze zwischen
    g = -0,6 und -1,0 genau zu legen und den Strahlungsmechanismus zu pruefen.
  - Formelerweiterung lambda sum_a \|psi_a\|^4: Nach PLAN-Logik wird der Stern fuer lambda > \|g\|/2 punktweises Minimum
    [Hand, ungerechnet]. Dann waere "Farbneutralitaet" der Grundzustand, um den Preis eines neuen, U(3)-brechenden
    Terms.
  - Die Karten-Frage "Umlaufzahlen stiller Stellen modulo 3" ist hier nicht bearbeitet.
- Regelhinweis: Bei einer Anzeige der Flussbahnen (lokal, nur Ausgabe ausduennen) ist einmal awk benutzt worden, gegen
  die Auftragsregel. Danach nur jq und sed. Kein git, kein Journal, keine fremden Dateien geaendert.

## Einfach gesagt

Wir haben geprueft, ob drei Feldsorten in unserem Ball ihre Phasen wie die drei Quarkfarben anordnen, so dass sie sich
zu null aufheben. Das geht: Der "Mercedes-Stern" ist eine echte, ruhende Loesung, in der innen ein Strom im Kreis von
Sorte zu Sorte fliesst, ohne dass sich eine Sorte leert. Er ist aber nicht der tiefste Zustand. Noch billiger ist es, eine
Sorte ganz wegzulassen und zwei gegeneinander zu stellen, eher wie ein Meson als wie ein Proton. Ohne Reibung haelt die
Eigendrehung des Balls den Stern trotzdem stabil wie einen Kreisel, und seine zwei Drehrichtungen sind wie ein kleiner
innerer Schalter (ein "Pseudospin"). Mit Reibung oder einem kraeftigen Stoss kippt er jedoch um, und echte Quarkfarben
mit Eichfeldern und Einschluss steckt in der Formel nicht drin.
