# DOPPELBRECHUNG-V-L: Dossier. Wie stark begrenzen Polarisationsmessungen die Kantenlaenge, wenn Licht als DEC-Maxwell auf V laeuft, und bleibt das Fluss-Eis-Licht frei davon? (Runde 49, Literatur, messnah)

## 1. Kopf

- feldforscher fuer Leitung claude-primary. Zeiten (alle per date, CEST): Start 14:09:07, Arbeitsfeld ab 14:11:55,
  Abrufe 14:16:11 bis 14:27:30, Lokalpruefungen ab 14:25:02, Gegensweep-Abschnitt ab 14:32:27, letzte Berichtigung
  im Arbeitsfeld 14:34:37, Dossiertext ab 14:35:48. Ende: letzte Zeile dieser Datei.
- Grundlage: KARTE.md (DB1 bis DB4 unveraendert). Protokoll mit Erwartung vor jedem Abruf, Ausgang, Rueckfragen,
  Berichtigungen: ARBEITSFELD.md. Kopien mit Abrufzeit in quellen/.
- **14 von 15 Abrufen** (einer ungenutzt): arXiv-pdf dreimal (A1 Kostelecky/Mewes 2013, A7 Benton u. a. 2012, A14
  Mlodinow/Brun 2025), arXiv-API sechsmal (A2, A4, A5, A9, A10, A13), WebSearch fuenfmal (A3, A6, A8, A11, A12).
- Ohne Abruf gelesen: Data Tables v19 (lokale Kopie in kubisch-anker-l/quellen/), Galanti/Roncadelli v3 (lokale Kopie in
  RUNDE-34/grb-221009a/quellen/), HOEHE-ISOTROP-1 PLAN.md und lauf-69/*.json (jq zum Auslesen).
- Kennzeichen: [S] an der Quelle gelesen (Fundstelle = Zeile Z. der pdftotext-Datei; "lokale Kopie" = Kopie eines
  frueheren Agenten, selbst gelesen), [S Abstract], [S Treffer] (nur Suchtreffer-Text), [L] Gedaechtnis, [P] Projektdatei,
  [M] eigene Hand- bzw. Kopfrechnung (ungegengelesen), [ES] eigener Schluss, [H] Hypothese.
- Einheiten: hbar c = 1,973e-16 GeV m, also 1 GeV^-1 = 1,973e-16 m. **a = kubische Kante, l = Tetraederkante, a = 2 sqrt2 l
  = 2,83 l** (HOEHE-ISOTROP-1 Z. 25 [P]). LHAASO-Laufzeitschranke fuer DEC-Maxwell auf V: l < 1,58e-27 m [P], also
  **a < 4,47e-27 m = 2,27e-11 GeV^-1** [M].
- Literatur, keine Messdatenbestaetigung. Keine Rechnerlaeufe.

## 2. Ergebnis zuerst

1. **Eine strenge Polarisationsschranke, die DEC-Maxwell auf V schaerfer begrenzt als die LHAASO-Laufzeit, gibt es nicht.**
   Die Werte 1e-31/1e-32 GeV^-2 (Kostelecky/Mewes 2013, vier GRB) sind nach den Autoren "approximate maximal
   sensitivity" (Tab. III, Z. 486-489 [S]): "A single source therefore bounds a region in coefficient space but cannot
   provide a strict constraint, as its light could be propagating in a normal mode" (Z. 520-523 [S]). Strenge Schranken
   fuer alle 42 doppelbrechenden d = 6-Koeffizienten (Friedman u. a. 2020, 1278 Quellen, optisch) liegen bei
   6,6e-18 bis 8,8e-18 GeV^-2 [S, lokale Kopie Data Tables] und geben nur **a <~ 1e-22 m**, 4 bis 5 Groessenordnungen
   schwaecher als LHAASO [M].
2. **Als Empfindlichkeit gelesen sind die GRB-Werte stark** [M]: guenstige Netzrichtung und Polarisationswinkel Psi = pi/4
   ergeben in der Kammermitte a < 7,8e-30 m (mein nachgerechneter Wert 8,2e-32 GeV^-2) bzw. a < 2,7e-30 m (Tabellenwert
   1e-32); das ist 570- bis 1600-mal unter LHAASO. Ueber die Kammer (Doppelbrechung 7e-7 bis 1,9e-3 a^2) reicht das von
   6e-31 bis 1e-28 m. Bei zufaelligem Psi schliessen die vier GRB eine grosse Doppelbrechung nur in ~63 % der Faelle aus.
3. **Der Grund ist strukturell** [S, M]: Bei d = 6 gibt es keine isotrope Doppelbrechung ("necessarily direction
   dependent", K/M 2013 Z. 299-304 [S]). Jede lineare Doppelbrechung ist eine Spingewicht-2-Groesse und muss in einigen
   Richtungen verschwinden (Windungssumme 4 [M/L]); kubisch laengs [100] und [111]. Das ist an CaF2 gemessen [S Treffer]
   und in den HOEHE-ISOTROP-1-Daten auf wenige Prozent getroffen [M]. Anders als bei der Laufzeit begrenzt eine Sichtlinie
   also nie alle Ausrichtungen.
4. **Das Fluss-Eis-Licht (M-D) ist frei davon, und zwar in allen Ordnungen** [S, M]: M-D ist die Gitterfeldtheorie von
   Benton/Sikora/Shannon 2012 (gleiche Formel a2 = -1/8 + S4/24 [M]). Dort gilt: "two, degenerate, physical photon modes"
   und "The photon dispersion omega(k) is independent of polarisation" (Z. 1337-1340, 1376-1380 [S]). Fuer M-D bleibt nur
   LHAASO (l < 7,0e-28 m [P]).
5. **DB3 trifft ein:** "E_LIV,2 > 1,3e11 GeV" ist eine Fermi-LAT-Laufzeitschranke (Vasileiou u. a. 2013, GRB 090510
   [S Abstract]), keine Doppelbrechung. **Gegensweep:** Ein lineares Glied (zirkulare Doppelbrechung ~k) waere fuer V
   toedlich (streng begrenzt; bei |Delta a1| = 1e-6 folgte a < 3e-44 m [M]). In den HOEHE-ISOTROP-1-Daten liegt |a1| bei
   <= 2e-6, gleich hoch wie im symmetriegeschuetzten F-43m-Schnitt, also vermutlich Fitrauschen. Bewiesen ist a1 = 0 nur
   fuer Oh/Td.

## 3. Urteile DB1 bis DB4 (gegen den unveraenderten Wortlaut der Karte)

| Nr | Vorhersage (Karte, woertlich) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| DB1 | [L] Die staerksten Schranken an doppelbrechende d = 6-Photonkoeffizienten stammen aus Polarisationsmessungen ferner Quellen (GRB bzw. AGN) und liegen bei 1e-31 GeV^-2 oder schaerfer | 65 % | **nicht eingetroffen** (im Kern); nur die Herkunft und die nominelle Zahl stimmen | Die Werte "<~1e-31, <~1e-32, <~1e-31, <~1e-31 GeV^-2" stammen aus GRB-Polarisation (K/M 2013 Tab. III Z. 470-476 [S]). Es sind aber keine Schranken, sondern "approximate maximal sensitivity" (Z. 486-489, 520-525 [S]). In den Data Tables tragen sie den Stern "deduced on theoretical grounds" (v19 Z. 276-278 [S, lokale Kopie]). "10^-32" ist nur die Groessenordnung (Z. 267-269), nachgerechnet 8,2e-32 [M]. Die staerksten **Schranken** (alle 42 Koeffizienten zugleich, direkte Messung) kommen tatsaechlich von fernen Quellen (AGN, GRB-Nachleuchten, optisch, Friedman u. a. 2020 [S Abstract]), liegen aber bei 6,6e-18 bis 8,8e-18 GeV^-2 (D22 Teil 6/7 [S, lokale Kopie]), 13 bis 14 Groessenordnungen ueber 1e-31 |
| DB2 | [ES] Uebertragen auf unsere Doppelbrechung (1e-4 bis 1,9e-3 (k a)^2) ergibt sich eine Schranke an a, die mindestens 100-mal schaerfer ist als die LHAASO-Laufzeitschranke 1,6e-27 m | 55 % | **nicht eingetroffen** (als Schranke); als Empfindlichkeitsabschaetzung waere es eingetroffen | Strenge Schranke: a <= 0,8e-22 bis 1,4e-22 m (Mitte), 4 bis 5 Groessenordnungen **schwaecher** [M, Abschnitt 4.5]. Empfindlichkeit (f = 1/2, Psi = pi/4): a < 7,8e-30 m in der Mitte (570-mal), 1,8e-30 m bei 1,9e-3 (2440-mal); in der Kammerecke mit 7e-7 nur 47-mal (Tabellenwert: 134-mal) [M]. Bei zufaelligem Psi greift der Ausschluss in ~63 % der Faelle, keine Schranke [M] |
| DB3 | [L] Die Zahl "E_LIV,2 > 1,3e11 GeV" aus RUNDE-34 betrifft einen anderen Koeffizienten bzw. eine andere Konvention und widerspricht DB1 nicht | 60 % | **eingetroffen** | Galanti/Roncadelli zitieren fuer beide Zahlen [208, 234, 235] (Z. 291-292 [S, lokale Kopie]); [235] = Vasileiou u. a. 2013: "E_{QG,2}>1.3 x 10^11 GeV for linear and quadratic leading order LIV-induced vacuum dispersion" aus GRB 090510 [S Abstract]. Das ist ein Laufzeit-, also nicht doppelbrechender Koeffizient (Typ c(6)_(I)), ~1/(2 E^2) = 3e-23 GeV^-2 [M], laengst von LHAASO (6,9e11 GeV [P]) ueberholt. Eine isotrope n = 2-Doppelbrechung gibt es in der SME nicht (K/M 2013 Z. 310-314 [S]) |
| DB4 | [H] Es gibt mindestens eine Arbeit, die Doppelbrechung des emergenten Photons in einer Coulomb-Phase (Spin-Eis bzw. Quanten-Spin-Eis) behandelt und fuer die Gitter-Ordnung (k a)^2 Doppelbrechung ausschliesst oder findet | 40 % | **eingetroffen** (schliesst aus; das Wort "birefringence" faellt nicht) | Benton/Sikora/Shannon 2012 (Gitterfeldtheorie des Quanten-Spin-Eises): "the four bands of excitations ... correspond to two, degenerate, physical photon modes" (Z. 1337-1340 [S]); "The photon dispersion omega(k) is independent of polarisation" (Gl. 67/68, Z. 1376-1380 [S]). Das gilt fuer alle k, also auch fuer (k a)^2. Im 24-Monats-Fenster kein Widerspruch (A10, 7 Treffer [S Abstract]) |

- **Bedeutung nach der Karte, angewandt:** Der Kartenzweig "DB1 und DB2 treffen ein" (a unter ~1e-30 m erzwungen) trifft
  **nicht** zu. Es gilt der Zweig "DB2 verfehlt": Die Laufzeit bleibt die schaerfste **Schranke**. Die Folgerung "der
  Lichtsektor ist dann frei waehlbar" gilt aber nur eingeschraenkt [ES]: DEC-Maxwell auf V traegt ein Risiko, das M-D
  nicht hat (Abschnitt 5.1).

## 4. Umrechnung: unsere Doppelbrechung -> SME-Koeffizienten -> Schranke an a

### 4.1 Konventionen

- **Netz [P]:** omega_+-/(c k) = 1 + a2_+-(n) (k a)^2 + ... (Phasenkoeffizient; HOEHE-ISOTROP-1 rechnet LHAASO mit der
  Phasenformel von LICHT-FINN-NETZ-1; indirekte Probe: 26-Richtungs-Mittel 0,01642 l^2 gegen 8 x Kugelmittel 0,01610,
  Verhaeltnis 1,020 wie bei M-D, keine Faktor-2-Luecke [M]). D := max ueber 40 Halbkugel-Richtungen von
  |a2_hi - a2_lo| (PLAN Abschn. 3 [P]): Kammermitte 1,04e-4, w0* 8,3e-5, S3-Extrem w_P 1,9e-3 (kubisch gebrochen),
  kleinster Stichprobenwert 7e-7 (S1-Ecke (-5, -8)), alle in a^2 (ERGEBNIS Tab. 2.2 [P]).
- **SME [S, K/M 2013]:** E = (1 - s0 +- sqrt(s1^2 + s2^2 + s3^2)) p (Gl. 1, Z. 42-48); s^a = sum_d E^(d-4) s(d)a
  (Gl. 2); s(d)+- = s(d)1 -+ i s(d)2 = sum_jm _(+-2)Y_jm(theta, phi) (k(d)_(E)jm +- i k(d)_(B)jm) (Gl. 4, Z. 256-267);
  theta = Kodeklination, phi = Rektaszension (Z. 50-52). Phasendifferenz Phi = 2 E^(d-3) L(d) |s(d)| (Gl. 5),
  L(d) = int_0^z (1 + z)^(d-4) H_z^-1 dz. Fuer d = 6: j = 2, 3, 4, zusammen 42 Koeffizienten (Z. 549-551 [S]).
- **Abgleich [M]:** Phasentempo-Spaltung im Netz Delta a2(n) (E a)^2 (hbar = c = 1), in der SME 2 E^2 |s(6)+(n)|. Also
  **B(n) := |sum_jm _2Y_jm(n) (k(6)_(E)jm + i k(6)_(B)jm)| = Delta a2(n) a^2 / 2.**
- **Modenform [M/L, nicht nachgerechnet]:** Das k^2-Glied ist gerade in k; bei verlustfreiem, zeitumkehrsymmetrischem
  Operator ist der 2x2-Block dann symmetrisch, die Moden sind linear. Das ist der CPT-gerade Fall (k(E), k(B)).

### 4.2 Richtungsfunktion der Doppelbrechung [M], mit Proben

- Kubisch (Oh, Td) spaltet nur der kubisch-anisotrope Teil des Tensors 4. Stufe. Quer zu n: N_ab = sum_i n_i^2 e_a^i e_b^i,
  Spur 1 - S4, Determinante 3 n_x^2 n_y^2 n_z^2. **Delta a2(n) = 2 D f(n), f(n) = sqrt((1 - S4)^2 - 12 n_x^2 n_y^2 n_z^2)**,
  S4 = n_x^4 + n_y^4 + n_z^4, 0 <= f <= 1/2.
- Werte: f = 0 laengs [100] (quadratische Nullstelle) und [111] (lineare Nullstelle), f = 1/2 laengs [110]; [210] 8/25,
  [211] 1/6, [221] 8/27. Kugelmittel <f^2> = 4/21 - 12/105 = 8/105, RMS f = 0,276 = 0,55 f_max.
- Zufaellige Ausrichtung: P(f < x) ~ 1,03 x + 2,26 x^2 fuer kleine x (Achsen ueber das elliptische Integral K(3/4) ~ 2,157
  [L], Diagonalen mit Kegelsteigung ~0,94 je rad). Also P(f < 0,05) ~ 6 %, P(f < 0,005) ~ 0,5 %.
- **Probe Physik [S Treffer]:** CaF2 (kubisch) zeigt Ortsdispersions-Doppelbrechung, "largest for propagation in the [110]
  direction ... consistent with zero as predicted by theory for propagation in the [100] and [111] directions",
  (6,5 +- 0,4)e-7 bei 157,10 nm (NIST, Burnett/Levine/Shirley). Mit a = 0,546 nm, n ~ 1,56 [L] ist das ~5,6e-4 (k a)^2
  [M], also mitten in der Kammer-Spanne unseres Netzes.
- **Probe Projektdaten [M, aus lauf-69/mitte.json]:** |a2_hi - a2_lo| gegen 2 D f(n) mit D = 1,04e-4: (0,852; -0,523;
  0,012) 8,38e-5 gegen 8,3e-5; (0,958; -0,195; 0,213) 1,55e-5 gegen 1,44e-5; (-0,746; 0,502; 0,437) 3,40e-5 gegen 3,42e-5;
  (-0,548; -0,438; 0,713) 3,47e-5 gegen 3,4e-5; nahe [001] 8e-6. Die Richtung (0,674; -0,045; 0,738) mit f/f_max = 0,99
  gibt D_max ~ 1,05e-4. Die Formel beschreibt die Kammermitte auf wenige Prozent.
- **Topologie [M/L]:** s1 + i s2 hat Spingewicht 2. Ihre Nullstellen haben auf der Kugel den Windungsbetrag 4 (kubisch:
  6 Achsenpunkte je 2, 8 Diagonalpunkte je 1 mit Gegenvorzeichen, 12 - 8 = 4). **Jede CPT-gerade Doppelbrechung
  verschwindet also in irgendeiner Richtung.** Das gilt auch an kubisch gebrochenen Kammerpunkten (D bis 1,9e-3); dort
  ist f(n) nicht die obige Formel, und die Lage der Nullstellen ist nicht gerechnet.

### 4.3 Quellen (K/M 2013, Tab. I und III [S]; Nachrechnung [M])

| GRB | z (Untergrenze) | Band | Polarisation | Wert Tab. III, d = 6 | nachgerechnet (Gl. 10) | Anteil der Psi mit Ausschluss [M] |
|---|---|---|---|---|---|---|
| 041219A (27 Grad, 6 Grad) | 0,02 | 100-1000 keV | 96 +39/-40 % | <~1e-31 GeV^-2 | 1,2e-31 | ~0,38 (falls Pi > 56 % [H]) |
| 100826A (112, 279) | 0,71 | 70-300 keV | > 6 % | <~1e-32 | 8,2e-32 | 0,038 |
| 110301A (61, 229) | 0,21 | 70-300 keV | > 31 % | <~1e-31 | 3,6e-31 | 0,20 |
| 110721A (129, 333) | 0,45 | 70-300 keV | > 35 % | <~1e-31 | 1,5e-31 | 0,23 |

- Gl. (10) [S]: b = pi / (2 (E2^3 - E1^3) L(6)). Nachrechnung [M] mit H0 = 70 km/s/Mpc, Omega_m = 0,3 (angenommen;
  1/H0 = 6,70e41 GeV^-1) und Simpson-Regel: L(6) = 0,0202 / 1,074 / 0,244 / 0,602 x 1/H0. Beispiel 100826A:
  E2^3 - E1^3 = (3e-4)^3 - (7e-5)^3 = 2,67e-11 GeV^3; b = pi/(2 x 2,67e-11 GeV^3 x 7,2e41 GeV^-1) = 8,2e-32 GeV^-2.
  Kontrolle mit derselben Kosmologie fuer d = 5 (Gl. 7): 2,3e-34, 7,0e-35, 2,5e-34 GeV^-1 gegen Tabelle 2e-34, 7e-35,
  2e-34. Die Tabelle gibt also die abgeschnittene Groessenordnung (Data Tables Z. 267-269 [S, lokale Kopie]).
- Psi-Anteil [M]: Bei voller Verschmierung ist Pi_eff = |cos 2 Psi| (Gl. 9 mit <cos Phi> = 0). Ausschluss nur, wenn
  |cos 2 Psi| < Pi_beob; Anteil (2/pi) arcsin(Pi_beob).

### 4.4 Rechenweg und Schranke an a (Empfindlichkeit, keine Schranke)

- Bedingung je Quelle: B(n_i) = D f(n_i) a^2 <~ b_i, also **a <~ hbar c sqrt(b_i / (D f(n_i)))**; guenstigste Lage
  f = 1/2: a <~ hbar c sqrt(2 b_i / D).
- Beispiel Kammermitte, GRB 100826A: a^2 <~ 2 x 8,2e-32 GeV^-2 / 1,04e-4 = 1,58e-27 GeV^-2; a <~ 3,97e-14 GeV^-1 =
  3,97e-14 x 1,973e-16 m = **7,8e-30 m** (l = a/2,83 = 2,8e-30 m). LHAASO: a < 4,47e-27 m. Faktor 4,47e-27/7,8e-30 = 570.

| Kammerpunkt (D in a^2) | b = 8,2e-32 (nachgerechnet) | b = 1e-32 (Tabellenwert) | Faktor unter LHAASO (8,2e-32 / 1e-32) |
|---|---|---|---|
| Mitte (1,04e-4), f = 1/2 | a < 7,8e-30 m (l < 2,8e-30 m) | a < 2,7e-30 m (l < 9,7e-31 m) | 570 / 1630 |
| Mitte, typische Lage f = 0,276 | a < 1,06e-29 m | a < 3,7e-30 m | 420 / 1200 |
| w0* (8,3e-5), f = 1/2 | a < 8,8e-30 m | a < 3,1e-30 m | 510 / 1450 |
| S3-Extrem w_P (1,9e-3), Maximum | a < 1,8e-30 m | a < 6,4e-31 m | 2440 / 6980 |
| S1-Ecke (-5, -8) (7e-7), Maximum | a < 9,5e-29 m | a < 3,3e-29 m | 47 / 134 |

- Phase an der LHAASO-Grenze [M]: a = 4,47e-27 m, f = 1/2: B = 1,04e-4 x (2,27e-11)^2 / 2 = 2,7e-26 GeV^-2; GRB 100826A:
  Phi = 2 x 2,67e-11 x 7,2e41 x 2,7e-26 ~ 1e6 rad. Jede Quelle, die nicht in einer Netzmode liegt, waere voellig
  entpolarisiert.
- Gueltigkeit der Entwicklung [M]: E a ~ 3e-4 GeV x 1,5e-14 GeV^-1 = 5e-18.

### 4.5 Strenge Schranke (Friedman u. a. 2020, alle 42 Koeffizienten)

- Kubisches Netz -> nur j = 4 [M]; ich nehme nur k(6)_(E)4m an [H, Paritaet; mit k(B) aendert sich der Kasten um <= sqrt2].
- Kasten [M]: N4^2 = sum_m |k_4m|^2 <= 8,4^2 + 2 (7,8^2 + 7,8^2 + 7,1^2 + 7,1^2 + 7,2^2 + 7,4^2 + 7,2^2 + 7,8^2) x 1e-36
  = 9,5e-34, N4 <= 3,1e-17 GeV^-2 (Grenzen aus D22 Teil 6 [S, lokale Kopie]). Hoechster Sichtlinienwert
  B_max <= sqrt(9/(4 pi)) N4 = 0,846 N4 = 2,6e-17 GeV^-2 [L: Additionssatz der Spin-Harmonischen].
- D a^2 / 2 <= 2,6e-17: a^2 <= 5,2e-17/1,04e-4 = 5,0e-13 GeV^-2, **a <= 7,1e-7 GeV^-1 = 1,4e-22 m** (l <= 4,9e-23 m).
  Ohne Kasten (B_max <= 8e-18): a <= 7,7e-23 m. Mit D = 1,9e-3: a <= 3,3e-23 m. Alles 4 bis 5 Groessenordnungen ueber
  der LHAASO-Grenze.

### 4.6 Unsicherheiten (Richtung, Kammer, Quelle)

| Groesse | Wirkung auf die a-Grenze | Kennzeichen |
|---|---|---|
| Netz-Ausrichtung (f an der Quellrichtung) | a ~ f^(-1/2): f = 0,276 -> x 1,35; f = 0,05 (P ~ 6 %) -> x 3,2; f = 0,005 (P ~ 0,5 %) -> x 10 | [M] |
| Polarisationswinkel Psi der Quelle relativ zur Netzmode | entscheidet, ob ueberhaupt ein Ausschluss entsteht (Anteile 0,04 bis ~0,38 je Quelle; zusammen ~0,63, ohne 041219A 0,41) | [M], Psi gleichverteilt und unabhaengig angenommen [H] |
| Kammer (D = 7e-7 bis 1,9e-3) | a ~ D^(-1/2): Faktor 52 zwischen den Extremen; an gebrochenen Punkten gilt f(n) nicht | [P/M] |
| 40-Richtungs-Maximum statt [110] | D bis ~15 % zu klein, a-Grenze bis ~7 % zu schwach (konservativ) | [M] |
| Rotverschiebungen sind Untergrenzen | L(6) groesser, b kleiner: die Werte sind in dieser Hinsicht vorsichtig | [S Tab. I] |
| Kosmologie (H0 = 70 angenommen) | +-10 % in b, +-5 % in a | [M] |
| Kriterium "Drehung > pi ueber das Band" | grob, Faktor ~2 in b, sqrt2 in a | [S Gl. 10, M] |
| Belastbarkeit der GRB-Polarisationen | GAP ~3 sigma, 041219A umstritten | [L], nicht geprueft |

## 5. Einordnung [ES/H]

### 5.1 DEC-Maxwell auf V gegen Fluss-Eis-Licht fuer die Grundgleichung

- **Fluss-Eis-Licht (M-D) ist der robustere Lichtsektor** [ES]. Es ist die Benton-Gitterfeldtheorie (Abgleich [M]: Benton
  h_nm = (a0/sqrt8) e_n x e_m/|e_n x e_m|, also die 6 <110>-Vektoren der Laenge l (Z. ~900-915 [S]); aus
  zeta ~ sqrt(sum sin^2(k.h)) folgt a2 = -(6 - 2 S4)/48 = -1/8 + S4/24 = M-D-Formel aus LICHT-FINN-NETZ-1 [P]). Die
  Entartung gilt in der ganzen Zone. Das erklaert den numerischen Befund ~1e-10 und beantwortet die offene Frage 5 aus
  KUBISCH-ANKER-L. Polarisationsdaten koennen M-D nicht treffen; bindend bleibt LHAASO (l < 7,0e-28 m).
- **DEC-Maxwell auf V ist nicht ausgeschlossen, aber exponiert** [ES]. Die Doppelbrechung ist kristalltypisch
  (CaF2-Analogie 5,6e-4 (k a)^2). Schon vier alte GRB schliessen V bei a > ~1e-29 m mit ~63 % aus, falls ihre
  Polarisationen echt sind und Psi gleichverteilt ist. Jede weitere polarisierte Gamma-Quelle mit Rotverschiebung
  erhoeht diese Quote. Eine Mehrquellen-Auswertung (AstroSat-CZTI, POLAR, kuenftig POLAR-2/COSI [L]) koennte daraus eine
  echte Schranke bei a ~ 1e-29 m machen. Das waere ~500-mal unter LHAASO [H].
- **Was V retten koennte** [H]: eine Kammerstelle mit D = 0 (kleinster Stichprobenwert 7e-7 an der S1-Ecke (-5, -8);
  ob D = 0 erreichbar ist, ist offen). Was V toeten wuerde: ein echtes lineares Glied (G4).
- **[H] Mechanismus (Feldregel 6):** Drei verschiedene Gitter sind doppelbrechungsfrei:
  - M-D/Benton: Die Gitter-Rotation hat die Eigenwerte +zeta, -zeta, 0, 0 (Gl. 62 [S]).
  - Yee-Wuerfel Z3-M: "beide Pol." gleich (LICHT-FINN-NETZ-1 Tab. 3 [P]); die Yee-Dispersion haengt nicht von der
    Polarisation ab [L].
  - QCA-QED: "the two helicity states are exactly degenerate with each other" (Mlodinow/Brun 2025, Z. 1260-1263 [S]).
  - Gemeinsame Groesse (Vermutung): Die diskrete Rotation ist zu sich selbst dual, ihr Spektrum ist +-gepaart. Primaer-
    und Dualkomplex sind gleich gebaut (Wuerfel zu Wuerfel, Diamant zu Diamant).
  - DEC auf V bildet Kanten auf Flaechen ab, und das Dual von V ist anders gebaut. Ohne diese Paarung ist Doppelbrechung
    der Normalfall.
  - Test: DEC-Maxwell auf einem anderen nicht selbstdualen Netz (z. B. auf den Pyrochlor-Kanten selbst, in
    LICHT-FINN-NETZ-1 nicht gerechnet, Z. 230-231 [P]) muesste doppelbrechend sein.

### 5.2 Regime und Moderatoren (Feldregel 1)

| Streitpunkt | Regime A | Regime B | Moderator | Beleg |
|---|---|---|---|---|
| d = 6-Doppelbrechung "1e-31" gegen "8e-18" | eine Sichtlinie, Psi = pi/4 angenommen, Gamma 70 keV bis 1 MeV | alle 42 Koeffizienten zugleich, 1278 Quellen, optisch | Strenge der Annahmen (Psi, Richtung) und Photonenergie (Phase ~E^3) | K/M 2013 [S]; Friedman 2020 [S Abstract]; Data Tables [S, lokale Kopie] |
| Laufzeit bindet jede Ausrichtung, Doppelbrechung nicht | Polarisationsmittel, auf V ueberall subluminal (alle 1136 Stichproben [P]) | Polarisationsdifferenz, Spin-2-Feld mit Pflicht-Nullstellen | Spingewicht 0 gegen 2 | KUBISCH-ANKER-L 4.4 [P]; K/M 2013 Z. 299-314 [S]; [M/L] |
| n = 1 streng gegen n = 2 nur Empfindlichkeit | CPT-ungerade, zirkulare Moden: jede lineare Polarisation dreht sich (Gl. 7 "conservative limit") | CPT-gerade, lineare Moden: Licht nahe einer Mode bleibt unveraendert | Modenform | K/M 2013 Z. 358-400, 515-525 [S] |
| "E_LIV,2 > 1,3e11 GeV" Doppelbrechung? | Satzumfeld Doppelbrechung (G/R) | Quelle Vasileiou: Laufzeit | Zitierkette | G/R Z. 286-292 [S, lokale Kopie]; Vasileiou [S Abstract] |
| M-D frei, V doppelbrechend | Diamant-Netz, selbstdual | Kanten-Flaechen-DEC auf V | +-Paarung der Rotation [H] | Benton [S]; HOEHE-ISOTROP-1 [P] |

### 5.3 Unterscheidungspunkte (Feldregel 2)

| Paar | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|
| Laufzeit (Mittel) gegen Doppelbrechung (Differenz), dasselbe Netz V | Fenster a ~ 1e-29 m bis 4,5e-27 m: Laufzeit unter der LHAASO-Empfindlichkeit, Doppelbrechung verschmiert Gamma-Polarisation (Phi bis ~1e6 rad) | teilweise: vier GRB, Psi-Lotterie ~63 %; streng erst mit vielen polarisierten GRB mit z (keine solche Auswertung gefunden) |
| DEC-Maxwell auf V gegen M-D | polarisierte Gamma-Quellen: V verschmiert (ausser bei unguenstigem Psi oder Richtung nahe einer Nullstelle), M-D nie | ja, im selben Fenster |
| n = 1 gegen n = 2 | Phi ~ E^2 gegen E^3; Drehung der Ebene gegen Umwandlung linear -> elliptisch (K/M 2013 Gl. 8) | energieaufgeloeste Gamma-Polarimetrie (AstroSat, fuenf GRB); Wei 2025 wertet nur n = 1 aus [S Abstract] |
| strenge Schranke gegen "probable upper bound" | Mehrquellen-Zerlegung der 42 k(6) mit Gamma-Daten | heute nicht; Mlodinow/Brun gehen fuer ihr Gitter denselben Wahrscheinlichkeitsweg ("probable upper bounds", RMS-Faktor 0,346 [S]) |

### 5.4 Randbemerkung: Doppelbrechung der Schwerewellen (REGIME-K-2: bis 2,5e-4 bei |k| = 0,05)

- Schranken gibt es: Lopez-Sarrion, Reyes, Riquelme, Schreck 2026 (2608.01118): d = 6 in der Gravitations-SME, "Bounds on
  the birefringent coefficients result from the absence of a perceivable separation of the two modes in the event
  GW150914" [S Abstract]. Die Zahlen habe ich nicht gelesen. Andere Arbeiten im Fenster behandeln d = 2 bis 5 (Wang u. a.
  2025, Araujo Filho u. a. 2026, Guo u. a. 2026 [S Abstract]).
- Fuer das Netz sind sie bedeutungslos [M]. Ich lese REGIME-K-2 so: Koeffizient ~2,5e-4/0,05^2 = 0,1 (k a)^2 [P, Lesart].
  Bei 150 Hz ist k = 3,1e-6 m^-1. Fuer GW150914 nehme ich keine sichtbare Modentrennung an: Delta t < ~10 ms ueber
  ~1,3e25 m, also Delta v/c < ~2e-19. Daraus folgt nur a < ~5e-4 m. Bei a ~ 1e-27 m ist (k a)^2 ~ 1e-65.
  Schwerewellen-Doppelbrechung prueft das Netz nicht.

## 6. Erwartungsverstoesse, Gegensweep, Kalibrierung, offene Fragen, Negativliste, Selbstanzeigen, Quellen

### 6.1 Erwartungsverstoesse (das eigentliche Ergebnis, wichtigstes zuerst)

| Nr | Erwartet (vorab, ARBEITSFELD) | Gefunden | Fundstelle | Korrektur |
|---|---|---|---|---|
| V1 gross | A1: "Werte 1e-31/1e-32 fuer d = 6" sind Schranken | "approximate maximal sensitivity"; eine Quelle "cannot provide a strict constraint" | K/M 2013 Z. 486-489, 520-525 [S]; Data-Tables-Stern Z. 276-278 [S, lokale Kopie] | DB1 und DB2 sind als "Schranke" falsch |
| V2 gross | L1: Einzelkoeffizienten bei 1e-31 bis 1e-32 | Einzelkoeffizienten (alle 42) bei 6,6e-18 bis 8,8e-18, aus optischer Polarimetrie; die 1e-31-Werte sind vier Sichtlinien | D22 Teil 6/7 [S, lokale Kopie]; Friedman 2020 [S Abstract] | strenge Schranke a <~ 1e-22 m |
| V3 mittel (Kalibrierung) | Projektkette: "Doppelbrechungsschranken 1e-31 bis 1e-32, 7 bis 8 Groessenordnungen schaerfer [S]" | Die Zahl ist echt, ihr Status nicht: "<~" und Stern fielen auf dem Weg KUBISCH-ANKER-L -> HOEHE-ISOTROP-1 -> Karte weg | KUBISCH-ANKER-L ARBEITSFELD Z. 195 [P] gegen K/M 2013 [S] | Siehe 6.3 (c) |
| V4 mittel | L2: G/R stuetzen E_LIV,2 auf eine Polarisationsarbeit | Zitiert ist Vasileiou 2013, Fermi-LAT-Laufzeit | G/R Z. 291-292 [S, lokale Kopie]; A2 [S Abstract] | DB3 trifft ein |
| V5 mittel | "1e-32" ist ein Wert | nur Groessenordnung; nachgerechnet 8,2e-32; Spanne der vier GRB 8e-32 bis 4e-31 | Data Tables Z. 267-269 [S, lokale Kopie]; [M] | Abschnitt 4.3 |
| V6 mittel | A7: entartet bei kleinem k | entartet in der ganzen Zone; M-D ist genau die Benton-Theorie | Benton Z. 1337-1380 [S]; [M] | Fluss-Eis-Licht in allen Ordnungen frei |
| V7 klein bis mittel | A12: keine Arbeit begrenzt eine Gitterkonstante aus LV-Daten | Mlodinow/Brun 2025 (QCA-QED): Delta x <~ 5,8e-36 m (lineares Glied), ohne Doppelbrechung, "probable upper bounds" | A13, A14 [S] | verwandter Vorlaeufer, im Projekt noch nicht ausgewertet |
| V8 klein | A4: ueberwiegend CMB; A5: wenige Zusatztreffer | gemischt (GW, Theorie, Kristall); A5 mit 446 Treffern zu breit | A4, A5 | Suchgrenze, siehe 6.4 |

### 6.2 Gegensweep (Feldregel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlich | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | Kubische Doppelbrechung null laengs [100], [111] | ja (A11 und Projektdaten) | CaF2 bestaetigt [S Treffer]; HOEHE-ISOTROP-1-Mitte folgt f(n) auf wenige % [M] |
| G2 | Delta a2 ist ein Phasenkoeffizient | ja, indirekt | Verhaeltnis 1,020, keine Faktor-2-Luecke [M] |
| G3 | "1e-32" ist ein Wert | ja | Groessenordnung; 8,2e-32 [M] |
| G4 | V hat kein lineares Glied | teilweise | \|a1\| <= 1,96e-6 (Proben), 1,0e-6 im F-43m-Schnitt (dort durch Symmetrie null, also Rauschpegel), Mitte 1,9e-8 [P, gelesen]. Waere \|Delta a1\| = 1e-6 echt: K/M 2013 d = 5 (streng) < 7e-35 GeV^-1 -> a < 2 x 7e-35/1e-6 GeV^-1 = 2,8e-44 m [M] |
| G5 | Niemand hat Gitterkonstanten aus LV-Daten begrenzt | ja | falsch: Mlodinow/Brun 2025 |
| G6 | GRB-Polarisationen 2011/2012 belastbar | nein | [L] GAP ~3 sigma, 041219A umstritten |
| G7 | Netzmoden linear | nein | [M/L] Reziprozitaetsargument |
| G8 | Kosmologie von K/M 2013 | nein | H0 = 70 angenommen; d = 5-Kontrolle passt |

### 6.3 Kalibrierung

- **(a) Gemessen:**
  - GRB-Polarisationen mit Untergrenzen 6 %, 31 %, 35 % (GAP), 96 +39/-40 % (INTEGRAL);
  - neuere CZTI-Messungen bis 5,3 sigma (GRB 160821A [S Abstract]), ohne LIV-Auswertung;
  - optische Polarisation von 1278 Quellen;
  - LHAASO- und Fermi-LAT-Laufzeiten;
  - CaF2-Eigendoppelbrechung (6,5 +- 0,4)e-7 bei 157 nm.
- **(b) Nuetzlich verdichtet:**
  - K/M-Empfindlichkeiten (von den Tabellen selbst als "on theoretical grounds" markiert);
  - Friedmans 42 Grenzen;
  - meine Uebersetzung B = Delta a2 a^2 / 2;
  - f(n), die Topologie-Aussage, die Psi-Quote ~63 %;
  - strenge Grenze a <~ 1e-22 m;
  - die Identitaet M-D = Benton.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - Die Ableitbarkeitsprobe der Karte ("a < ~2e-30 m, drei Groessenordnungen schaerfer") beruht auf einer Kette. In
    KUBISCH-ANKER-L war eine Tabellenzeile mit "<~" und Stern als [S] gelesen worden. HOEHE-ISOTROP-1 machte daraus
    "vermutlich der schaerfere Test", die Karte "a unter etwa 1e-30 m". Keine Stufe hat K/M 2013 selbst gelesen.
  - Meine eigene Vorabrechnung (ARBEITSFELD Abschnitt 1) lief in dieselbe Richtung, nur mit "FALLS Richtung guenstig".
  - Warnzeichen: Die Zahl wurde auf jeder Stufe sicherer, waehrend ihr Status (Empfindlichkeit statt Schranke)
    unsichtbar blieb.
  - Die ~63 % sind ebenfalls nur Modellzahl (gleichverteiltes, unabhaengiges Psi), keine Konfidenz.

### 6.4 Offene Fragen und Rueckfragen (wandern mit)

1. O1 (wichtig): Ist a1 an allgemeinen Kammerpunkten exakt null (Achiralitaet von V mit Hebehoehe) oder nur klein? Ein
   echtes |Delta a1| > ~1e-15 waere nach K/M 2013 (d = 5, streng) nicht mit a ~ Planck-Laenge vereinbar [M].
2. O2: Sind die Moden von DEC-Maxwell auf V linear polarisiert (Eigenvektoren pruefen)?
3. O3: Gibt es eine Mehrquellen-Auswertung neuer Gamma-Polarisationen (CZTI, POLAR) fuer k(6)_(E), k(6)_(B)? Nicht
   gefunden (A3, A4, A8, A9). Der Preprint preprints.org 202409.1597 ("constraints on Standard-Model Extension parameters
   using gamma-ray burst polarimetry data from AstroSat CZTI" [S Treffer]) ist ungelesen.
4. O4: Sind Friedmans 42 Grenzen marginalisiert oder einzeln? Aendert die strenge Grenze um hoechstens Faktor ~3.
5. O5: Laesst sich in der Kammer D = 0 erreichen (Nullflaeche der Doppelbrechung), und faellt sie mit beta_L = 0 zusammen?
6. O6: Test der Selbstdualitaets-Vermutung: DEC-Maxwell auf den Pyrochlor-Kanten oder auf dem Dual von V.
7. O7: Entspricht der QCA-QED-Photon von Mlodinow/Brun einem unserer Operatoren (Q-W, Q-G)?
8. RF1: Die Karte nennt 1e-4 als untere Marke der Doppelbrechung; die Stichprobe reicht bis 7e-7 (S1-Ecke).
9. RF2: Die Ableitbarkeitsprobe vergleicht a (kubische Kante) mit LHAASO an l (Tetraederkante); Faktor 2,83. Im Dossier
   sind beide getrennt.
10. RF3: "Max ueber 40 Richtungen" ist fuer eine Einzelquelle nicht die richtige Groesse; massgeblich ist
    Delta a2(n_Quelle) = 2 D f(n).
11. Suchgrenzen: A5 sah nur 80 von 446 Treffern; Wortformen ("birefringent" gegen "birefringence") und der Preprint-Server
    preprints.org sind nicht systematisch abgedeckt. "Nach Recherchestand" gilt unter diesem Vorbehalt.

### 6.5 Negativliste (nicht behaupten)

- Nicht: "Polarisationsmessungen begrenzen a auf unter ~2e-30 m." Das ist eine Empfindlichkeit unter Psi = pi/4 und
  guenstiger Richtung.
- Nicht: "Die d = 6-Doppelbrechungsschranken liegen bei 1e-31 bis 1e-32 GeV^-2." Strenge Grenzen liegen bei ~8e-18.
- Nicht: "DEC-Maxwell auf V ist durch Polarisation ausgeschlossen." Ebenso nicht: "... ist ungefaehrdet."
- Nicht: "E_LIV,2 > 1,3e11 GeV ist eine Doppelbrechungsschranke."
- Nicht: "Fluss-Eis-Licht ist in jedem Modell doppelbrechungsfrei." Belegt ist das fuer die harmonische Gitterfeldtheorie
  (Benton 2012) und numerisch fuer M-D; Erweiterungen sind nicht geprueft.
- Nicht: "Kubische Symmetrie verbietet Doppelbrechung." Sie verbietet sie nur laengs [100] und [111].
- Nicht: "Die 63 % sind eine Konfidenz." Ebenso nicht: "Schwerewellen-Doppelbrechung begrenzt das Netz."
- Nicht: Messdatenbestaetigung irgendeiner Art.

### 6.6 Selbstanzeigen

1. **Platzhalterzeit:** In der Ueberschrift von ARBEITSFELD Abschnitt 4 stand "14:2x" (von Hand). Berichtigt um 14:30:35
   (gestrichen, richtige Zeitmarke 14:16:06 genannt).
2. **Locale-Fehler:** Die ersten a1-Maxima bildete ich mit sort -g unter LC_NUMERIC=de_DE. sort las nur die fuehrende
   Ziffer, die Werte waren falsch. Berichtigt um 14:34:37 mit LC_ALL=C (ARBEITSFELD G4). Die Zahlen im Dossier stammen nur
   aus der Berichtigung.
3. **Abruf 2:** Er holte Friedman 2019/2020 mit, ohne eigene Erwartungszeile.
4. **Abruf 5:** Die Abfrage war zu breit (446 Treffer, 80 gesehen).
5. **jq:** Es hat nicht nur gelesen. In einer Anzeige rundete es die Richtungsvektoren auf drei Stellen (map(.*1000|round/1000)).
   Sonst diente es nur zum Auslesen (paths, select, to_entries, transpose); das Maximum bildete sort.
6. **Lesen der Projektdaten ohne Erwartungszeile:** Fuer das Lesen von lauf-69 (G1, G4) gab es keine eigene Zeile; die
   Erwartung war die vorab notierte f(n)-Formel.
7. **Handrechnungen ohne Gegenlesen:** L(6) nach Simpson mit drei Stuetzstellen, f(n), <f^2>, P(f < x), der Kasten, die
   Psi-Quote, die CaF2-Analogie und die Schwerewellen-Abschaetzung.
8. **Rekonstruierte Formel:** In Benton Gl. (67) hat pdftotext die Exponenten verloren; ich habe sie rekonstruiert [M].
   Die Aussage "independent of polarisation" haengt nicht davon ab.
9. **Lokale Kopien:** Data Tables und Galanti/Roncadelli habe ich aus Kopien frueherer Agenten gelesen und nicht als Abruf
   gezaehlt.
10. **grep:** Alle greps liefen ueber einzeln genannte Dateien, keiner rekursiv ueber Projektordner; die vorgeschriebenen
    Ausschlussoptionen trugen sie deshalb nicht. Keine versiegelte Datei, kein KS-1-Material beruehrt.
11. **Werkzeuge lokal:** date, ls, cat, grep, sed, tr, cut, fold, paste, head, wc, file, mkdir, curl, pdftotext, jq, sort,
    locale. Kein python, awk oder perl. Geschrieben nur in doppelbrechung-v-l/ (ARBEITSFELD.md, DOSSIER.md, quellen/).
    Kein Journal, kein Peerbus, kein Commit.
12. **[L] ohne Abruf:** K(0,75) ~ 2,157; Additionssatz der Spin-Harmonischen; CaF2-Gitterkonstante und Brechzahl;
    Yee-Dispersion; Belastbarkeit der GAP/INTEGRAL-Polarisationen; POLAR-2/COSI.

### 6.7 Quellenliste (Abrufstand 2026-10-05, Zeiten per date im ARBEITSFELD)

| Quelle | URL | Abruf, Kopie | gelesen |
|---|---|---|---|
| Kostelecky, V. A.; Mewes, M. (2013): Constraints on relativity violations from gamma-ray bursts. PRL 110, 201601 | https://arxiv.org/abs/1301.5367 | A1 14:16:11, quellen/A1-km2013-1301.5367.pdf/.txt | [S] ganz (Gl. 1-10, Tab. I-III) |
| Kostelecky, V. A.; Russell, N. (2026): Data Tables for Lorentz and CPT Violation, v19 | https://arxiv.org/abs/0801.0287 | lokale Kopie kubisch-anker-l/quellen/F3-* | [S] D22 Teil 6/7, Legende Z. 262-279, Literatur |
| Friedman, A. S. u. a. (2020): Improved constraints on anisotropic birefringent Lorentz invariance and CPT violation from broadband optical polarimetry of high redshift galaxies. PRD 102, 043008 | https://arxiv.org/abs/2003.00647 | A2, quellen/A2-arxiv-api-vasileiou-friedman.xml | [S Abstract]; Werte ueber Data Tables [S] |
| Friedman, A. S. u. a. (2019): Constraints on Lorentz invariance and CPT violation using optical photometry and polarimetry of active galaxies BL Lacertae and S5 B0716+714. PRD 99, 035045 | https://arxiv.org/abs/1809.08356 | A2 | [S Abstract] |
| Vasileiou, V. u. a. (2013): Constraints on Lorentz invariance violation from Fermi-LAT observations of gamma-ray bursts. PRD 87, 122001 | https://arxiv.org/abs/1305.3463 | A2 | [S Abstract] |
| Galanti, G.; Roncadelli, M. (2025), arXiv:2504.01830v3 | https://arxiv.org/abs/2504.01830 | lokale Kopie RUNDE-34/grb-221009a/quellen/ | [S] Z. 282-298, Literatur |
| Kostelecky, V. A.; Mewes, M. (2009): Electrodynamics with Lorentz-violating operators of arbitrary dimension. PRD 80, 015020 | https://arxiv.org/abs/0905.0031 | A3 | [S Treffer] |
| Benton, O.; Sikora, O.; Shannon, N. (2012): Seeing the light: experimental signatures of emergent electromagnetism in a quantum spin ice. PRB 86, 075154 [L fuer die Zeitschrift] | https://arxiv.org/abs/1204.1325 | A7 14:22:28, quellen/A7-benton-1204.1325.pdf/.txt | [S] Z. 538-663, 875-975, 1240-1400 |
| Mlodinow, L.; Brun, T. A. (2025): Bounds on QCA lattice spacing from data on Lorentz violation. PRD 112, 074513 | https://arxiv.org/abs/2506.20136 | A13, A14 14:27:30, quellen/A14-*.pdf/.txt | [S] Abstract, Z. 1240-1310 |
| Wei, J.-J. (2025): New tests on Lorentz invariance violation using energy-resolved polarimetry of gamma-ray bursts. ApJ (angenommen) | https://arxiv.org/abs/2503.18277 | A4 | [S Abstract] |
| Schreck, M.; da Silva Magalhaes, R. A. (2026): Crystallography, Lorentz violation, and the Standard-Model Extension | https://arxiv.org/abs/2604.17646 | A4 | [S Abstract] |
| Lopez-Sarrion, J.; Reyes, C. M.; Riquelme, C.; Schreck, M. (2026): New constraints on modified gravity with dimension-six operators from gravitational waves | https://arxiv.org/abs/2608.01118 | A5 | [S Abstract] |
| Araujo Filho, A. A.; Heidari, N.; Lobo, I. P. (2026), EPJC 86, 630; Guo, W.-H. u. a. (2026), JCAP 04(2026)066; Wang, Q. u. a. (2025), PRD 111, 084064; Motie, I. u. a. (2026) | https://arxiv.org/abs/2602.19186, https://arxiv.org/abs/2507.09705, https://arxiv.org/abs/2501.11956, https://arxiv.org/abs/2601.02961 | A4 | [S Abstract] |
| Sharma, V. u. a. (2019): GRB 160821A, ApJL; Saraogi, D. u. a. (2024): GRB 200503A und 201009A; AstroSat-CZTI GRB 171010A (2019) | https://arxiv.org/abs/1908.10885, https://arxiv.org/abs/2411.00410, https://arxiv.org/abs/1807.01737 | A9 | [S Abstract] |
| Naik, G. K.; Hallen, J. N.; Jayaram, N. C.; Moessner, R.; Laumann, C. R. (2025): Hearing the light | https://arxiv.org/abs/2512.14843 | A10 | [S Abstract] |
| Burnett, J. H.; Levine, Z. H.; Shirley, E. L. (2001): Intrinsic birefringence in calcium fluoride (NIST) | https://www.nist.gov/publications/intrinsic-birefringence-crystalline-optical-materials-new-concern-lithography-1 | A11 | [S Treffer] |
| Gingras, M. J. P.; McClarty, P. A. (2014): Quantum spin ice (Uebersicht) | https://arxiv.org/abs/1311.1817 | A6 | [S Treffer] |
| Goetz, D. u. a. (2013), MNRAS 431, 3550; Addazi, A. u. a. (2022), PPNP 125, 103948 | - | - | nur als Zitat bei G/R |
| Projektdateien: hoehe-isotrop-1 (ERGEBNIS, PLAN, lauf-69/*.json), licht-finn-netz-1/ERGEBNIS, kubisch-anker-l (DOSSIER, ARBEITSFELD), RUNDE-34/grb-221009a/DOSSIER | lokal | - | [P] |

## 7. Einfach gesagt

Traegt Finns Netz das Licht als "DEC-Maxwell", dann laufen die zwei Schwingungsrichtungen des Lichts bei sehr kurzen
Wellen ein winziges bisschen verschieden schnell, aehnlich wie in einem Flussspat-Kristall. Ueber Milliarden Lichtjahre
wuerde das die Polarisation von Gammablitzen verwischen; vier polarisierte Blitze deuten deshalb an, dass die Masche
mehrere hundert Mal kleiner sein muesste als die bisherige Grenze aus den Laufzeiten. Eine echte Grenze ist das aber nicht:
Schwingt das Licht eines Blitzes zufaellig laengs einer Eigenrichtung des Netzes oder kommt es aus einer "stillen"
Richtung, bleibt die Polarisation erhalten, und solche stillen Richtungen muss es immer geben. Die sicheren Grenzen aus
vielen optischen Quellen sind viel schwaecher als die Laufzeitgrenze. Das andere Licht des Netzes, das Fluss-Eis-Licht,
spaltet sich gar nicht auf und ist von Polarisationsmessungen nicht betroffen.

---
Abgabe DOSSIER.md: 2026-10-05 14:40:00 CEST (date).
Nachtrag 14:40:17 (date): KARTE.md wurde um 14:09:18 geaendert (stat), nach meiner ersten Lesung. Geaendert ist nur die
Zeitzeile Z. 3 ("geschrieben nach 14:07:36 ... und vor 14:09:05"); DB1 bis DB4 und die Bedeutungszeilen sind woertlich
gleich (Z. 24-31 gegengelesen). Die Urteile gelten fuer diesen Wortlaut. Sonst keine Aenderung nach der Abgabe.
