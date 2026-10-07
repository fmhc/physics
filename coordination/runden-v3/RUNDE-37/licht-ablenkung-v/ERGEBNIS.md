# LICHT-ABLENKUNG-V: Ergebnis (Rechen-Agent fuer die Leitung claude-primary, Versuch ohne Karte)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-05 16:21:07 CEST. Ohne Karte, Plan-Einfrieren und frischen Leser (Finn, 05.10.: "einfach machen").
  - Kontrolllauf K und Probelauf L = 8: 14:38:15 bis 14:38:28 UTC (cpu2, cpu3; la.py Fassung 1, sha256 e794d6fd...).
  - Hauptlaeufe L = 16 (cpu2), 24 (cpu3), 32 (cpu4): 14:41:29 bis 14:43:15 UTC, la.py Fassung 2 (cca39a1b...), alle rc = 0,
    L = 32 in 105 s.
  - Zusammenfassung zf.py (0b993ca9...): 14:44:44 bis 14:44:46 UTC (cpu2). Text ab 16:47:01 CEST.
- lauf-69/PRUEFSUMMEN.txt (auf der .69 erzeugt, 14 Dateien) besteht lokal sha256sum -c.
- Alles ist eine synthetische Gitterrechnung (numpy, 1 Thread) an einem gedachten periodischen Netz. Keine Messdaten.
- **Kennzeichen:** [E] gerechnet, [M] eigene Mathematik, [P] Projektdatei, [ES] eigener Schluss, [H] Hypothese.
- **Einheiten und Vorzeichen:** r und b in l_P (Finn-Kante). Einheitsquelle mit G = 1 wie MATERIE-NETZ-1, Fernstaerke
  A = 0,028135 = 1/(8 sqrt2 pi). Phi = Lapse-Stoerung mu, nahe der Masse negativ. ART (isotrope Koordinaten):
  n = 1 - 2 Phi = 1 + 2 GM/(r c^2), also "1 + 2 Phi" der Aufgabe mit Phi als Betrag. Alles ist linear in der Masse.

## 1. Ergebnis zuerst

1. **Ja, im gerechneten Bereich bekommt das Licht die volle ART-Wirkung [E].** DEC-Licht auf V mit Sternen aus den
   geloesten Kantenlaengen und Takt-gewichteter Energie hat ab 1,5 l_P Abstand den Index n - 1 = -2 Phi. Je Schale
   weicht es um hoechstens 0,7 % vom Newton-Ziel ab, von 3 bis 20 l_P um hoechstens 0,1 % (L = 32, Quelle P0 und C1).
2. **Takt und Laengen tragen je genau die Haelfte [E].** Fit-freies Mass (Laengen-Anteil / Takt-Anteil, ART: 1):
   von 3 bis 20 l_P 0,999 bis 1,001 je Schale (L = 32). Bei der Eikonal-Ablenkung laengs [100] liegt der Median ueber
   die Saeulen mit b = 1,6 bis 5 l_P bei 0,9999 bis 1,0000; bei Shapiro-Laufzeitdifferenzen bei 0,998 bis 1,000
   (L = 32). Nur Takt oder nur Laengen ergibt je 0,483 bis 0,496 der Ziel-Ablenkung (L = 16 bis 32), also die halbe.
3. **Ablenkung und Laufzeit gegen das Newton-Ziel [E]:** Ablenkung gesamt/Ziel 0,969, 0,985, 0,990 (L = 16, 24, 32),
   Laufzeitdifferenzen 0,979 bis 0,990. Die Restabweichung steckt gleich gross schon im Takt-Anteil, der keine Laengen
   enthaelt. Sie faellt mit L. Lesart [ES]: Sie stammt aus der Torus-Naeherung des Ziels, nicht aus der Lichtkopplung.
4. **Nahfeld (unter etwa 1,5 l_P) ist nicht eindeutig [E].** In der Zelle mit der Quellecke traegt der Laengen-Anteil
   0,83 des Takt-Anteils. Mit anderen Regeln, wie die Gewichte (Hebehoehen) der Geometrie folgen, sind es 0,73, 0,68
   oder 3,9. Dort sind auch eps und mu ungleich (Faktor 4), das Licht wuerde also gestreut. Ab 4 l_P liegen alle vier
   Regeln innerhalb 0,5 %.
5. **Der Fernwert war vorab ableitbar [M].** Gemessen ist, dass das Gitter ihn traegt, wie gross das Nahfeld abweicht
   und dass die Eikonal-Summen auf dem echten Netz stimmen (Abschnitt 8). Die Identitaeten
   sum *1 l^2 t t^T = V I und sum *2 A^2 n n^T = V I und psi = -mu legen den Fernwert schon fest.

## 2. Was gerechnet ist: wie Takt und Laengen ins Licht kommen

- **Statik [E, wie MATERIE-NETZ-1]:** Punktquelle auf P0 (Finn-Ecke) oder C1 (Lochmitte), L^3 primitive Zellen,
  KKT mit Eichwahl M^H a = 0 je Gitter-k, Zerlegung a_hat = W psi + M xi (ew.ops, mn.W_of unveraendert). V1, q = 1/2.
  Daraus je Ecke der Takt N_v = 1 + mu_v und die Eck-Skalierung sigma_v = 2 q psi_v. Gemessen gilt psi = -mu
  (Abweichung 3,0e-13 relativ).
- **Laengen:** Jede Kante bekommt l_e (1 + (sigma_v + sigma_w)/2), das ist die isotrope Eichung. Der Eichteil M xi, eine
  reine Eckverschiebung, ist weggelassen [F]. Er waere nur eine Koordinatenwahl; in ihm waere der lokale Index
  anisotrop, die Strahlen-Groessen blieben gleich [M].
- **Sterne aus den Laengen:** Die gewichteten Sterne nach rv.sterne an der Kammermitte w_mid (x = -23/7, y = -32/7 in
  (a/8)^2, Marge 12/7; min *1 = 0,031, min *2 = 1,83, alle positiv) sind in linearer Ordnung je Tetraeder abgeleitet,
  nach den 4 Eck-Skalierungen.
  - Die 6 neuen Kantenlaengen sind ueber Eckverschiebungen u = C^+ dl realisiert (C Starrheitsmatrix des Tetraeders).
  - Gewichte w_i (1 + 2 sigma_i), Regel "ecke".
  - Zentrale Differenzen mit h = 1e-5.
  - Summiert ueber alle Tetraeder einer Kante bzw. eines Dreiecks: rel. Aenderung von *1 = d(duale Flaeche)/(duale Flaeche)
    - dl/l; von *2 = d(duale Laenge)/(duale Laenge) - dA_f/A_f.
- **Takt im Licht:** Die Hamilton-Dichte des Lichts tickt im Ecktakt, genau wie die Geometrie (V1: Energie in der Regel
  je Ecke). Die elektrische Energie einer Kante zaehlt mit N_e = Mittel der 2 Ecken, die magnetische eines Dreiecks mit
  N_f = Mittel der 3 Ecken. Damit gilt omega^2 (*1/N_e) A = d1^T (N_f *2) d1 A. Das ist die diskrete Form von
  H = Integral N sqrt(h) (E^2 + B^2)/2.
- **Messung (lokale Dispersion, k -> 0):** Das ungestoerte Photon bei k -> 0 ist exakt das konstante Feld. Die dualen
  Zellen sind geschlossen, deshalb braucht es keine Zellkorrektur [M]. Erste Ordnung je primitiver Zelle R, in
  Medium-Form (Plebanski):
  - eps(R) = sum_e (*1_e/N_e) l_e^2 t_e t_e^T / V und zeta(R) = 1/mu = sum_f (N_f *2_f) A_f^2 n_f n_f^T / V;
    ungestoert beide I.
  - d(omega^2)/omega^2 = b^T d_zeta b - e^T d_eps e mit b = k^ x e; n - 1 = -d(omega)/omega.
  - Isotrop: n - 1 = (tr d_eps - tr d_zeta)/6. Takt-Anteil: nur die N-Terme; Laengen-Anteil: nur die Stern-Aenderungen.
  - Gegenprobe: volles Bloch-Eigenproblem (hi.licht_op, unveraendert) mit den gestoerten Sternen der Zelle, 18 Zellen
    je Quelle, 2 Richtungen.
- **Ziel (ART):** zweimal der Takt-Anteil, berechnet mit dem Newton-Fit Phi_N = A f(r) + C an den Ecken. f enthaelt das
  kuerzeste Bild und den Torus-Hintergrund, wie in MATERIE-NETZ-1. Das ist -2 Phi_N im selben Zellmittel.
- **Eikonal:** Saeulen laengs der kubischen [100]-Achse. Jede Saeule ist eine geschlossene Schleife aus L Zellen,
  Laenge L a. T(b) = Summe (n_x - 1) dx, gemittelt ueber beide Polarisationen. Ablenkung = Quergradient von T
  (zentrale Differenz ueber 1 a = 2,83 l_P), Komponente zur Masse. Saeulen, deren Ziel die Quellecke beruehrt, sind
  ausgelassen.

## 3. Index n(r) je Schale (L = 32, Quelle P0) [E]

Zellort = gewichteter Schwerpunkt der Zellelemente; Schalenmittel ueber Zellen. Ziel enthaelt die Torus-Konstante
(C = 0,001425); 2A/r allein waere in [3; 4) 0,0162.

| Schale r (l_P) | Zellen | n - 1 (Gitter) | Takt-Anteil | Laengen-Anteil | Ziel -2 Phi_N | Gesamt/Ziel | Laengen/Takt (Zellen min..max) |
|---|---|---|---|---|---|---|---|
| [0; 1) Quellzelle | 1 | 0,0709 | 0,0388 | 0,0321 | - | - | 0,826 |
| [1,5; 2) | 5 | 0,02858 | 0,01432 | 0,01426 | 0,02855 | 1,0010 | 0,996 (0,983..1,004) |
| [2; 2,5) | 7 | 0,02264 | 0,01130 | 0,01134 | 0,02256 | 1,0034 | 1,003 (1,000..1,007) |
| [2,5; 3) | 3 | 0,01869 | 0,00935 | 0,00935 | 0,01882 | 0,9930 | 1,000 (0,996..1,003) |
| [3; 4) | 33 | 0,01332 | 0,006660 | 0,006660 | 0,01332 | 1,0002 | 1,0001 (0,996..1,003) |
| [4; 5) | 43 | 0,009558 | 0,004779 | 0,004779 | 0,009564 | 0,9994 | 1,0001 (0,998..1,002) |
| [6; 8) | 213 | 0,005171 | 0,002586 | 0,002586 | 0,005172 | 0,9999 | 1,0001 (0,999..1,001) |
| [10; 12) | 559 | 0,002329 | 0,001165 | 0,001165 | 0,002330 | 0,9999 | 1,0002 (1,000..1,001) |
| [14; 16) | 992 | 0,001041 | 0,000521 | 0,000521 | 0,001041 | 0,9998 | 1,0004 (1,000..1,001) |
| [16; 20) | 2882 | 0,000476 | 0,000238 | 0,000238 | 0,000476 | 0,9998 | 1,0009 |
| [20; 24) | 4338 | 1,3e-5 | 6,6e-6 | 6,8e-6 | 1,4e-5 | 0,989 | 1,031 (Nulldurchgang) |

- In [20; 24) geht n - 1 durch null, weil das Torus-Potential den Mittelwert null hat; die Verhaeltnisse sind dort
  nicht aussagekraeftig.
- Quelle C1 (L = 32): Laengen/Takt 1,014 in [1; 1,5) (4 Zellen, 0,971..1,046), 0,994 in [2; 2,5), 0,999 in [3; 4),
  ab 4 l_P 0,9999 bis 1,0001. Gesamt/Ziel ab 2 l_P 0,999 bis 1,001.
- L = 16 und 24 geben nahe der Quelle dieselben Verhaeltnisse (Logs H16, H24; Quellzelle P0 0,819 / 0,824). Bei P0
  steigt Laengen/Takt zum Nulldurchgang hin leicht an (L = 16: 1,0003 bei 3 l_P bis 1,0034 bei 8 bis 10 l_P; dahinter
  0,994 bis 0,998). Der Unterschied Laengen minus Takt ist dabei fast konstant, bei L = 32 rund 2e-7 bis 4e-7.
  Lesart [H]: ein Gradienten-Glied aus dem gleichmaessigen Torus-Hintergrund (Laplace von mu konstant); nicht geprueft.

## 4. Ablenkung und Laufzeit (Eikonal laengs [100]) [E]

Median ueber die Saeulen (P0: 35 Saeulen, b = 1,6 bis 5,0 l_P; C1: 28, b = 2,9 bis 5,0). Shapiro: Differenz
T(b1) - T(b2), b1 aus den 12 naechsten Saeulen, b2 = 6,4 l_P (L = 32).

| L | Quelle | Ablenkung gesamt/Ziel | nur Takt/Ziel | nur Laengen/Ziel | Laengen/Takt (Einzelsaeulen) | Shapiro gesamt/Ziel | Shapiro Laengen/Takt |
|---|---|---|---|---|---|---|---|
| 16 | P0 | 0,969 | 0,486 | 0,485 | 1,0000 (0,85..1,08) | 0,979 | 0,992 |
| 16 | C1 | 0,968 | 0,485 | 0,483 | 0,9999 (0,98..1,09) | 0,979 | 1,013 |
| 24 | P0 | 0,985 | 0,493 | 0,492 | 1,0000 (0,85..1,07) | 0,986 | 0,997 |
| 24 | C1 | 0,983 | 0,493 | 0,491 | 0,9999 (0,98..1,09) | 0,979 | 0,999 |
| 32 | P0 | 0,990 | 0,496 | 0,495 | 1,0000 (0,85..1,07) | 0,990 | 0,998 |
| 32 | C1 | 0,990 | 0,496 | 0,494 | 0,9999 (0,98..1,09) | 0,984 | 1,000 |

- Gegen die Formel der unendlichen Geraden: Ziel/(4A/b) Median 0,99 (L = 32, P0), Einzelsaeulen bis 0,58 herunter
  (grobe Differenz bei kleinem b). Shapiro Ziel/(4A ln(b2/b1)) 0,977, Gitter/(4A ln) 0,965. Das sind Torus- und
  Schleifeneffekte des Ziels selbst.
- Die absolute Laufzeit je Saeule ist nicht aussagekraeftig: Gitter/Ziel 0,92, 0,94, 0,95 (L = 16, 24, 32). Die Saeule
  laeuft durch die Torus-Ecken, wo das Ziel (kuerzestes Bild plus r^2-Hintergrund) am schlechtesten ist [ES].
  Differenzen und Gradienten leiden weniger darunter.
- Bild: lauf-69/bild-licht-ablenkung.png (L = 32). Links oben n - 1 je Schale mit Takt- und Laengen-Anteil; rechts
  oben Laengen/Takt mit Gewichts-Varianten; unten die Saeulen-Ablenkung und ihr Verhaeltnis zum Ziel. Die Linien bei
  1 und 0,5 sind ART und halbe Ablenkung.

## 5. Kontrollen [E]

| Kontrolle | Wert |
|---|---|
| Ohne Masse: c aus hi.licht_op bei k a = 0,05, [100]/[110]/[111], beide Polarisationen | 0,999996 / 0,999995 / 0,999994 (Gitterdispersion (ka)^2) |
| Nur Takt bzw. nur Laengen: Ablenkung/Ziel (L = 32) | 0,496 bzw. 0,495 (P0), also halbe Ablenkung |
| Gleichmaessiges sigma = 1: rel. Aenderung *1 = +1, *2 = -1; Laengen-Anteil n - 1 = +1 | auf 1,3e-9 / 1,2e-9 / 4,6e-11 |
| Gleichmaessiger Takt: n - 1 = -1 (isotrop und je Richtung) | auf 4e-16 / 9e-16 |
| Summe der Tetraeder-Beitraege gegen hi.sterne_licht (*1 l, *2 A_f, A_f) | 1,4e-16 / 1,0e-16 / 0 |
| Identitaeten sum *1 l^2 t t^T / V = I, sum *2 A^2 n n^T / V = I | 2,2e-16 / 6,7e-16 |
| roll-Zusammensetzung gegen explizites Torus-Netz rv.netz_V(4), zufaelliges sigma | 2,2e-16 (Kanten), 2,4e-16 (Dreiecke), alle 4352 + 7424 zugeordnet |
| Erste Ordnung (Formel) gegen volles Bloch-Eigenproblem, 18 Zellen x 2 Richtungen je Quelle | rel. Abweichung <= 9,8e-5 (Stoerung 1e-4, zweite Ordnung) |
| Statik L = 32: KKT-Rest, Zerlegung, psi + mu, Imaginaerteil | 9,9e-14, 2,5e-13, 3,0e-13, 9,3e-16 |
| Fernstaerke A (L = 16 / 24 / 32, P0) | 0,028147 / 0,028135 / 0,028135 (soll 0,0281349) |

## 6. Nahfeld, Gewichtsregel, Doppelbrechung [E]

Laengen/Takt je Schale (L = 32, P0) fuer vier Regeln, wie die Gewichte der Geometrie folgen:

| Schale | ecke (Haupt): w_i (1 + 2 sigma_i) | tet: w_i (1 + 2 sigma_Tetraeder), eichinvariant | ecke, alle w + 1 a^2 | fest: w bleibt |
|---|---|---|---|---|
| [0; 1) | 0,826 | 0,733 | 3,908 | 0,682 |
| [1,5; 2) | 0,996 | 1,014 | 0,561 | 0,993 |
| [2; 2,5) | 1,003 | 1,002 | 0,921 | 1,008 |
| [2,5; 3) | 1,000 | 0,998 | 1,089 | 0,975 |
| [3; 4) | 1,000 | 1,000 | 0,995 | 1,001 |
| [4; 5) bis [8; 10) | 1,000 | 1,000 | 0,999 | 1,000 |

- Die Regel "ecke" haengt von der Gewichts-Eichung ab (Konstante auf alle w). Bei rauem Zufalls-sigma aendert eine
  Konstante 1 a^2 die *1-Aenderung um bis 461 bei Skala 15 (Kontrolllauf). Am glatten statischen Feld wirkt das nur
  nahe der Quelle. 1 a^2 ist etwa 14-mal die groesste Gewichtsdifferenz von w_mid (4,6 (a/8)^2); in erster Ordnung
  waechst die Wirkung linear mit der Konstante.
- "fest" ist nicht skalierungstreu (Jacobi-Summenprobe verfehlt um bis 2,8 je Tetraeder). Fern gibt es trotzdem 1,000:
  Die Identitaet sum *1 l^2 t t^T = V I gilt fuer jede Hebehoehe und fixiert den Tensor bei glattem sigma [M].
- Quelle C1 mit "ecke, alle w + 1 a^2": 1,670 / 1,155 / 1,043 / 1,056 / 0,995 in [1; 1,5) bis [4; 5); die anderen
  Regeln wie bei P0.
- **Impedanz:** eps_L = mu_L auf hoechstens 0,4 % ab 2,5 l_P (beide Quellen). Naeher weichen sie ab: P0 [1,5; 2) 9 %,
  C1 [1; 1,5) 3 %, C1 [2; 2,5) 1,7 %; in der P0-Quellzelle Faktor 4 (0,0125 gegen 0,0517). Ungleiche eps und mu
  bedeuten Reflexion bzw. Streuung.
- **Doppelbrechung:** Fuer Strahlen quer zum Radius ist n_radial - n_tangential im Schalenmittel, relativ zu n - 1:
  - 24 % in der P0-Quellzelle, 13 % bei C1 in [1; 1,5)
  - 6 bis 7 % bei 1,5 bis 2,5 l_P
  - 1,5 bis 5,5 % bei 2,5 bis 4 l_P
  - 1 bis 2 % bei 4 bis 6 l_P
  - 0,4 bis 0,9 % ab 6 l_P (L = 32)
- Das ist eine Obergrenze: Die Zuordnung ganzer Elemente zu einer Zelle erzeugt einen Gradienten-Fehler der Ordnung
  a/r. Er hebt sich im Schalenmittel nur naeherungsweise auf. Je Zelle betraegt er 4 bis 23 %; das ist kein
  physikalischer Wert [M]. Getrennt ist der Fehler hier nicht.

## 7. Grenzen

- Lineare Ordnung in der Masse, statisch, nur V1 mit Kammermitte w_mid. Eikonal (k -> 0 je Zelle) setzt
  Wellenlaenge >> a und << r voraus; unter einigen l_P ist "n(r)" deshalb eine Gitterkennzahl und keine
  Strahlenoptik.
- Torus L^3 mit Mittelwert-null-Potential: Ziel, absolute Laufzeiten und Vergleiche mit 4A/b bzw. 4A ln enthalten
  Torus-Fehler von 1 bis 5 %, die mit L fallen. Fit-frei sind nur die Verhaeltnisse Laengen/Takt.
- Eichteil M xi weggelassen (isotrope Eichung). Gezeigt ist das nur fuer Strahlen-Groessen [M], nicht nachgerechnet.
- Takt je Element als einfaches Eckmittel. Gewichtet nach Volumenanteilen waere das Nahfeld anders; es unterscheidet
  sich in Ordnung a^2 grad^2 Phi.
- Keine Zeitentwicklung eines Wellenpakets. Die Eikonal-Saeulen sind Summen erster Ordnung, keine Wellenoptik
  (Beugung, Streuung am Nahfeld).
- Saeulen nur laengs [100]; Quergradient mit 2,83 l_P Schrittweite, also grob bei kleinem b.
- Die Lichtzeit ist dieselbe Ecktakt-Uhr wie die Geometrie, aber die Geometrie ist hier nur statisch (Regime H, aeussere
  Zeit). Der Vergleich mit dem Tempo der Schwerewellen (Pruefliste Nr. 4) ist damit nicht gerechnet.

## 8. Ableitbarkeit

- **Vorab ableitbar [M]:** Fern gilt Laengen-Anteil = Takt-Anteil = -Phi.
  - Mit psi = -mu (V1-Identitaet, MATERIE-NETZ-1) ist sigma = -Phi.
  - Bei glattem sigma legen die Identitaeten sum *1 l^2 t t^T = V I und sum *2 A^2 n n^T = V I die Tensoren fest:
    eps_L = +sigma I, zeta_L = -sigma I. Die Takt-Gewichtung gibt eps_T = -Phi I, zeta_T = +Phi I.
  - Zusammen n - 1 = sigma - Phi = -2 Phi, mit eps = mu (keine Reflexion).
  - Das ist die Skalierung aus MATERIE-NETZ-1 Abschnitt 5, verallgemeinert auf beliebige Hebehoehen. Die Werte 1,0000
    fern sind deshalb eine Kontrolle, keine Messung.
- **Gerechnet und vorab nicht festgelegt:**
  - wie nah am Kern die Gleichheit haelt: ab 1,5 l_P auf 0,7 %, von 3 bis 20 l_P auf 0,1 %
  - Nahfeld-Werte und ihre Abhaengigkeit von der Gewichtsregel
  - Impedanz- und Doppelbrechungs-Verlauf
  - Eikonal-Summen auf dem echten Netz
  - Gegenprobe mit dem vollen Eigenproblem
- **Projektbezug:** schliesst Pruefliste Nr. 6 und 7 (GR-PRUEFLISTE-v2) fuer Licht auf V im Regime H mit Ecktakt,
  linear. Nr. 4 (gleiches Tempo wie Schwerewellen) bleibt offen.

## 9. Regelabweichungen und Selbstanzeigen

1. **Zwei Fassungen von la.py:** Kontrolllauf und Probelauf L = 8 liefen mit Fassung 1 (e794d6fd...). Die Hauptlaeufe
   liefen mit Fassung 2 (cca39a1b...): Gewichtsregel als Parameter, Varianten, radial/tangential, Impedanz.
   - Den Anlass zu den Varianten gab der Kontrolllauf: Die Gewichts-Eichung wirkte stark.
   - Die Funktion der Kontrollen ist in Fassung 2 unveraendert.
   - Die sha256 je Lauf stehen im _meta der JSON-Dateien.
2. **zf.py lief zweimal:** Fassung 1 (ab377eef...) wurde nach Sicht der Werte um fit-freie Verhaeltnisse ergaenzt
   (Fassung 2, 0b993ca9...). zusammenfassung.json und ZF.log stammen aus Fassung 2; die Ausgabe von Fassung 1 ist
   ueberschrieben, ihre Werte stehen unveraendert in Fassung 2.
3. **Nach Sicht ergaenzt:** die Varianten der Gewichtsregel, die radial/tangential-Doppelbrechung (statt nur je Zelle)
   und das Verhaeltnis Laengen/Takt je Saeule. Keine Karte, also kein Urteil betroffen.
4. **Eichteil und Takt-Mittel sind Festlegungen [F]**, nicht aus dem Projekt vorgegeben.
5. Lokal kein python, awk oder perl. jq nur zum Anzeigen (Auszuege und Hash-Kuerzung), ohne damit Werte zu berechnen.
   Nichts nach /tmp, /dev/null oder /dev/shm geschrieben. Eine Hilfsdatei (code/.neu_haupt.txt) lag kurz im Codeordner
   und ist geloescht. Code aus materie-netz-1 und hoehe-isotrop-1 ist nur kopiert (sha256 gleich), dort nichts
   geaendert.
6. **Nicht gegengelesen.** Kein Journal-Eintrag, kein Peerbus, kein Commit; das macht die Leitung.

## 10. Einfach gesagt

Wir haben am Computer Licht durch Finns gefuelltes Netz mit einer Masse geschickt; das Licht benutzt dabei dieselbe
Uhr und dieselben Kantenlaengen wie die Schwerkraft. Ab etwa zwei Kantenlaengen Abstand wird es genau so stark
abgelenkt und verzoegert, wie Einstein es vorhersagt, und je zur Haelfte kommt das von der langsameren Uhr und von den
laengeren Kanten. Nur ganz nah an der Masse haengt das Ergebnis davon ab, wie man das Netz im Detail baut, und der
Wert in der Ferne war schon vorher aus den Formeln absehbar.

## 11. Dateien

- code/: la.py (Rechnung), zf.py (Zusammenfassung, Bild); unveraendert kopiert: mn.py, ew.py, tp.py (materie-netz-1),
  rv.py, hi.py, danzer_naeherung.py, licht_netz.py (hoehe-isotrop-1).
- lauf-69/: kontrolle.json, haupt-L8.json (Probe), haupt-L16.json, haupt-L24.json, haupt-L32.json,
  zusammenfassung.json, bild-licht-ablenkung.png, K.log, H8.log, H16.log, H24.log, H32.log, ZF.log, code-sha256.txt
  (Stand Fassung 1), PRUEFSUMMEN.txt.
- Auf der .69: /home/fmh/fmhc-physics-remote/licht-ablenkung-v/ (code/, lauf/).

Abschluss des Textes 2026-10-05 16:50:17 CEST (date). Zeitrahmen 90 min ab 16:21:07 eingehalten. Kein Lauf mehr aktiv,
letzter Lauf endete 14:44:46 UTC.
