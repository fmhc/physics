# DOPPELBRECHUNG-V-L: Arbeitsfeld (eine Datei, vor jedem Schritt neu gelesen; Gestrichenes bleibt stehen, markiert ~~so~~)

- feldforscher fuer Leitung claude-primary. Start 2026-10-05 14:09:07 CEST (date). Arbeitsfeld angelegt 14:11:55 (date).
- Zeitbox 90 min (bis ~15:39), hoechstens 15 Abrufe. Abrufzaehler steht in Abschnitt 3.
- Karte KARTE.md gelesen (DB1 bis DB4 unveraendert, nicht anfassen).
- Kennzeichen: [S] Quelle gelesen (Fundstelle), [S Abstract], [S Treffer] nur Suchtreffer-Text, [S-lokal] lokale
  Kopie eines frueheren Agenten, selbst gelesen, [P] Projektdatei, [L] Gedaechtnis, [M] eigene Rechnung, [ES] eigener
  Schluss, [H] Hypothese.

## 0. Projektlage (gelesen 14:09 bis 14:11)

- [P] HOEHE-ISOTROP-1 ERGEBNIS Z. 25: a = kubische Kante; a2 und beta in a^2; Umrechnung auf die Finn-Tetraederkante
  l_P: mal 8 (also a = 2 sqrt2 l, a/l = 2,83 [M]). Probe: Kugelmittel -2,012e-3 a^2 * 8 = 0,0161 l^2 = Tabelle 2.3
  "Kugelmittel 0,01610" [M]. Passt.
- [P] HOEHE-ISOTROP-1 Tab. 2.2: "Doppelbrechung = max ueber 40 Richtungen von abs(a2_hi - a2_lo)". Mitte 1,04e-4 a^2,
  w0* 8,3e-5, S3 Extrem w_P 1,9e-3 (dort l = 2 bis 2,5e-4, "kubisch gebrochen"), S1-Ecke (-5,-8) nur 7e-7.
  Also: Spanne der Doppelbrechung in der Stichprobe 7e-7 bis 1,9e-3 a^2, nicht 1e-4 bis 1,9e-3 (Karte nennt die Mitte
  als untere Marke). -> Rueckfrage RF1 unten.
- [P] LHAASO-Laufzeitschranke 1,58e-27 m gilt fuer l (Tetraederkante), nicht fuer a (kubische Kante). Die
  Ableitbarkeitsprobe der Karte vergleicht "a < ~2e-30 m" mit "1,6e-27 m" (l). -> Rueckfrage RF2: gleiche Laenge?
- [P] LICHT-FINN-NETZ-1: a2 = Phasenkoeffizient von omega/(c k) = 1 + a2 (k l)^2. HOEHE-ISOTROP-1 rechnet die
  LHAASO-Schranke mit derselben Formel l = hbar c/(E_QG,2 sqrt(2 abs(a2))), also auch dort Phasenkoeffizient [P/ES].
- [P] KUBISCH-ANKER-L: SME nicht doppelbrechend s0 = sum p^(d-4) Y_jm c^(d)_(I)jm, Phasentempo 1 - s0.
  ARBEITSFELD Z. 195: "Teil 6/7: doppelbrechende d = 6-Koeffizienten k(E), k(B): Spektropolarimetrie ~8e-18,
  GRB-Polarisation (K/M 2013 [207]*) 1e-31 bis 1e-32 GeV^-2; CMB k(E)20,30,40 = +-(11 +4/-5)e-10 [19]*".
- [P] RUNDE-34 DOSSIER Z. 105: Galanti/Roncadelli (G/R, 2504.01830v3) S. 4: n = 1 fuehrt "in conventional physics" zu
  Doppelbrechung, Schranken E_LIV,1 > 3,6e34 GeV, E_LIV,2 > 1,3e11 GeV. Z. 140: Goetz u. a. 2013 GRB 061122 n = 1.

## 1. Schreibtisch vor jedem Abruf (Ableitbarkeitsprobe, eigene) [L/M]

- [L] SME-Photonsektor (Kostelecky/Mewes 2009): omega = (1 - s0 +- sqrt(s1^2 + s2^2 + s3^2)) p. s0 nicht
  doppelbrechend (c_(I), d gerade); s1 +- i s2 = sum p^(d-4) _(+-2)Y_jm (k_(E)jm -+ i k_(B)jm), d gerade, CPT-gerade,
  lineare Doppelbrechung; s3 = sum p^(d-4) Y_jm k_(V)jm, d ungerade, CPT-ungerade, zirkulare Doppelbrechung.
  [L, zu pruefen] Spingewicht 2 verlangt j >= 2: fuer d gerade gibt es KEINE isotrope Doppelbrechung.
- [M] Folgerung fuer unser Netz: Phasentempo-Differenz der Moden Delta(omega/k) = 2 s(n) omega^(d-4) mit
  s = sqrt(s1^2+s2^2+s3^2). Netz: Delta(omega/k) = Delta a2(n) (k a)^2. Also bei d = 6:
  **2 s(n) = abs(Delta a2(n)) a^2** (n = Richtung; hbar = c = 1).
- [L/M] Kubische Symmetrie: Doppelbrechung bei k^2 nur aus dem kubisch-anisotropen Tensor 4. Stufe; laengs [100]
  (C4v) und [111] (C3v) erzwingt die 2D-Darstellung Entartung -> Doppelbrechung null; laengs [110] (C2v) erlaubt
  (CaF2, Burnett u. a. 2001 [L]). Folge: die Netz-Doppelbrechung verschwindet in mindestens 14 Richtungen. Das
  "Allrichtungs-Argument" von KUBISCH-ANKER-L (min/max-Verhaeltnis 3/4) gilt hier NICHT (min/max = 0) [ES].
- [M] Grobe Groesse: Phase Delta phi = 2 s omega^3 L. GRB bei E = 3e-4 GeV, L ~ 1,5e41 GeV^-1 (~1 Gpc): Delta phi < 1
  -> s < ~1e-31 GeV^-2. Passt zu "1e-31 bis 1e-32".
- [M] Grobe Schranke: a^2 < 2 s_max / Delta a2. s_max = 1e-31, Delta a2 = 1,04e-4: a^2 < 1,9e-27 GeV^-2,
  a < 4,4e-14 GeV^-1 = 8,7e-30 m (kubische Kante), l = a/2,83 < 3,1e-30 m. Mit 1e-32: a < 2,8e-30 m, l < 9,8e-31 m.
  Mit Delta a2 = 1,9e-3 und 1e-32: a < 6,4e-31 m. -> alle >= 100-mal unter 1,6e-27 m, FALLS Richtung guenstig.
- Nicht ableitbar ohne Abruf: (i) Konvention der Data-Tables-/K-M-2013-Zahlen (s oder 2 s? Betrag eines Einzel-
  koeffizienten oder Norm?), (ii) Energien/Entfernungen/Richtungen der Quellen, (iii) ob es eine Mehrrichtungs-Zerlegung
  fuer k(6)_(E,B) gibt (unbekannte Netz-Ausrichtung), (iv) Herkunft und Konvention von E_LIV,2 > 1,3e11 GeV,
  (v) Spin-Eis-Literatur zur Photon-Doppelbrechung, (vi) 24-Monats-Stand.

## 2. Rueckfragen (wandern mit, verschwinden nicht)

- RF1: Karte "1e-4 bis 1,9e-3 a^2": Die Stichprobe hat auch Punkte mit 7e-7 (S1-Ecke (-5,-8)). Untere Marke ist also
  nicht 1e-4. Nennen, nicht aendern.
- RF2: Karte/Ableitbarkeitsprobe vergleicht eine Schranke an a (kubische Kante) mit LHAASO an l (Tetraederkante).
  Faktor 2,83. Im Dossier beide Laengen ausweisen.
- RF3: Ist "Doppelbrechung max ueber 40 Richtungen" die richtige Groesse fuer eine Einzelquelle? Nein, wenn die
  Doppelbrechung richtungsabhaengig ist (siehe Abschnitt 1). Braucht Mehrrichtungs-Schranke oder Ausrichtungsargument.

## 3. Lesungen und Abrufe (Erwartung vor jedem Schritt)

- Abrufzaehler: 0 von 15.
- 14:12:39 Erwartung vor Lokal-Lesung L1 (Data Tables v19, D22 Teil 6/7, lokale Kopie KUBISCH-ANKER-L, kein Abruf): Zeilen
  fuer k(6)_(E)jm und k(6)_(B)jm mit j = 2, 3, 4 aus GRB-Polarisation (Kostelecky/Mewes 2013), Betraege 1e-31 bis
  1e-32 GeV^-2, je Koeffizient einzeln; dazu schwaechere Spektropolarimetrie-Zeilen.
- L1 Ergebnis [S-lokal, F3-datatables-D22-layout-S63-69.txt Z. 343-470 (Teil 6/7) und Z. 438-445]:
  - Teil 6/7: alle 42 doppelbrechenden d = 6-Koeffizienten k(6)_(E)jm, k(6)_(B)jm, j = 2, 3, 4, einzeln
    |...| < 6,6e-18 bis 8,8e-18 GeV^-2, "Spectropolarimetry" [204] = Friedman u. a., PRD 102, 043008 (2020),
    arXiv:2003.00647.
  - Teil 7: Sichtlinien-Kombinationen |sum_jm _2Y_jm(theta, phi)(k(E)jm + i k(B)jm)| an VIER Richtungen
    (27 Grad, 6 Grad) ~1e-31, (112, 279) ~1e-32, (61, 229) ~1e-31, (129, 333) ~1e-31 GeV^-2, "Astrophysical
    birefringence" [207] = Kostelecky/Mewes, PRL 110, 201601 (2013), arXiv:1301.5367. Zeichen vor der Zahl im Text
    "." (Layout), vermutlich "<~" [H]. Dazu [18] = K/M 2009 (0905.0031) zwei Richtungen ~1e-29; [206] Friedman u. a.
    2019 (1809.08356) zwei Richtungen 5e-15 und 1e-14; CMB [19] = K/M 2007 k(E)20,30,40 = +-(11)e-10.
  - Keine Zeile nach 2020 fuer d = 6 doppelbrechend in v19 (Literatur bis Ende 2025 laut KUBISCH-ANKER-L).
  - **Erwartung teils verletzt (V1 vorlaeufig):** Die 1e-31/1e-32-Werte sind KEINE Einzelkoeffizienten-Schranken,
    sondern vier Sichtlinien. Die Einzelschranken (alle 42 zugleich) liegen bei ~8e-18 GeV^-2, 13 bis 14
    Groessenordnungen schwaecher. Gleiches Muster wie KUBISCH-ANKER-L V3 (Himmelsabdeckung). Fuer ein Netz mit
    unbekannter Ausrichtung zaehlt, ob die vier GRB-Richtungen zufaellig nahe den Nullrichtungen des Netzes liegen.
  - Korrigierte Erwartung: Schranke an a haengt an einer Ausrichtungsannahme; ohne sie nur die 8e-18-Schranke.
- 14:13:29 Erwartung vor Lokal-Lesung L2 (Galanti/Roncadelli 2504.01830v3, lokale Kopie RUNDE-34, kein Abruf): G/R nennen
  fuer n = 2 eine Polarisations-Arbeit mit isotroper, helizitaetsabhaengiger Parametrisierung (nicht SME); 1,3e11 GeV
  entspricht dann ~1/(2 E^2) = 3e-23 GeV^-2, also viel schwaecher als K/M 2013 -> andere Konvention/anderer Datensatz.
- L2 Ergebnis [S-lokal, galanti-roncadelli-2504.01830v3.txt Z. 286-298, Literatur Z. 639, 686-691]: "In conventional
  physics n = 1 LIV gives rise to birefringence ... the most updated bounds are E_LIV,1 > 3.6 x 10^34 GeV and
  E_LIV,2 > 1.3 x 10^11 GeV [208, 234, 235]". [208] = Addazi u. a., PPNP 125, 103948 (2022) (Uebersicht);
  [234] = Goetz u. a., MNRAS 431, 3550 (2013) (GRB 061122, Polarisation); [235] = Vasileiou u. a., PRD 87, 122001 (2013)
  (Fermi-LAT, Laufzeit [L]). Kein Satz, der E_LIV,2 an eine Polarisationsmessung bindet.
  - **Erwartung verletzt (V2 vorlaeufig):** Ich erwartete eine Polarisationsarbeit fuer n = 2. Stattdessen deutet die
    Zitierung auf Vasileiou 2013, eine LAUFZEIT-Arbeit; [L] dort E_QG,2 > 1,3e11 GeV aus GRB 090510. Dann waere die Zahl
    gar keine Doppelbrechungsschranke. Pruefen mit Abruf (Vasileiou-Abstract).
  - [L/M] Passt zur SME-Struktur: bei d = 6 (n = 2) gibt es keine isotrope Helizitaets-Aufspaltung (s3 nur fuer d
    ungerade). Eine "isotrope n = 2-Doppelbrechungsschranke E_LIV,2" haette in der SME keinen Koeffizienten.

## 4. Schreibtisch: Richtungsfunktion der kubischen k^2-Doppelbrechung [M] (vor den Abrufen, ~~14:2x~~)

- Berichtigung 14:30:35 (date): Die Zeitangabe "14:2x" in der Ueberschrift war ein Platzhalter von Hand (Regelverstoss,
  Selbstanzeige). Richtig: Abschnitt 4 wurde im selben Befehl angehaengt wie die Zeile "Erwartung vor Abruf 1" mit der
  Zeitmarke 14:16:06 (date), also vor Abruf 1 (14:16:11).

- Ansatz [M]: kubischer Tensor 4. Stufe T_ijkl = A d_ij d_kl + B (d_ik d_jl + d_il d_jk) + C delta_ijkl. Quer zu n
  (Polarisationen e_a, e_b senkrecht n) bleibt M_ab = A d_ab + C N_ab, N_ab = sum_i n_i^2 e_a^i e_b^i. Nur C spaltet.
- Eigenwertabstand von N: tr N = 1 - S4 (S4 = sum n_i^4), det N = n^T adj(D) n = 3 n_x^2 n_y^2 n_z^2 =: 3 P.
  **f(n) = sqrt((1 - S4)^2 - 12 P)**.
- Proben [M]: [100] f = 0; [111] (1 - 1/3)^2 - 12/27 = 0, f = 0; [110] f = 1/2 (Maximum); [210] 8/25; [211] 1/6;
  [221] 8/27; Pfad (1,1,t): f = 2 abs(1 - t^2)/(2 + t^2)^2 (t = 1: 0, t = 0: 1/2).
- Kugelmittel [M]: <S4> = 3/5, <S4^2> = 41/105 (KUBISCH-ANKER-L), <P> = 1/105 -> <f^2> = 4/21 - 12/105 = 8/105,
  rms f = 0,276 = 0,55 f_max.
- Nullstellen: 6 Achsenpunkte (quadratisch, Windung +2 der Spin-2-Groesse), 8 Diagonalpunkte (linear, Windung -1);
  Summe 12 - 8 = 4 [M]. [L/M, Topologie] Eine glatte Spingewicht-2-Groesse auf der Kugel hat Nullstellen mit Windungs-
  summe 4: JEDE lineare (CPT-gerade) Doppelbrechung verschwindet in mindestens einer Richtung. Folge [ES]: Eine
  Sichtlinien-Schranke begrenzt eine Doppelbrechung mit unbekannter Ausrichtung nie fuer alle Ausrichtungen.
- Verteilung bei zufaelliger Ausrichtung [M, Naeherung kleine x]: P(f < x) ~ 1,03 x + 2,26 x^2 (Achsen: Flaeche
  (x/4) * 4 K(m = 3/4) = 2,16 x je Punkt, K(0,75) ~ 2,157 [L]; Diagonalen: Kegelsteigung ~0,94 je rad [M]).
  Beispiele: P(f < 0,05) ~ 6 %, P(f < 0,005) ~ 0,5 %.
- Uebersetzung [M, Konvention zu pruefen]: SME-Sichtlinie B(n) = abs(sum _2Y_jm(n)(k(E)jm + i k(B)jm)) = s(n)/p^2;
  Netz-Spaltung des Phasentempos 2 s = abs(Delta a2(n)) a^2. Kubisch: abs(Delta a2(n)) = 2 D_max f(n), D_max = Maximum
  ueber Richtungen (HOEHE-ISOTROP-1: "max ueber 40 Richtungen", Mitte 1,04e-4 a^2). Also **B(n) = D_max f(n) a^2**.
  Schranke: a^2 < b_i / (D_max f(n_i)) fuer jede Quelle i.
- 14:16:06 Erwartung vor Abruf 1 (arXiv-pdf 1301.5367, Kostelecky/Mewes 2013): Vier GRB mit Polarisationsnachweis
  (GRB 041219A, 100826A, 110301A, 110721A [L]); Schranke aus "Polarisation ueberlebt ueber das Band", Groessen-
  ordnungsangabe "<~"; Dispersion omega = (1 - s0 +- s) p mit s = Betrag der Spin-2-Summe; Werte 1e-31/1e-32 fuer d = 6
  bezogen auf s (nicht 2 s).
- 14:19:04 Abruf 1 gelesen (curl 14:16:11, quellen/A1-km2013-1301.5367.pdf/.txt, 594 Zeilen, ganz gelesen). Abrufzaehler 1 von 15.
- A1 Ergebnis [S, Kostelecky/Mewes 2013, arXiv:1301.5367v1, Zeilen der .txt]:
  - Gl. (1) Z. 42-48: E = (1 - s0 +- sqrt(s1^2 + s2^2 + s3^2)) p. Gl. (2) Z. 146-154: s^a = sum_d E^(d-4) s(d)a(theta, phi).
    Gl. (4) Z. 256-267: s(d)+- = s(d)1 -+ i s(d)2 = sum_jm _(+-2)Y_jm (k(E)jm +- i k(B)jm). theta = Kodeklination
    (90 Grad - Deklination), phi = Rektaszension (Z. 50-52).
  - Z. 299-304: "there are no j = 0 isotropic coefficients k(E)jm or k(B)jm, so the quantities s(d)+- are necessarily
    direction dependent". Z. 310-314: "isotropic birefringence occurs only in the CPT-odd case ... d is odd, so changes
    in polarization for even d necessarily depend on the source position". -> meine [L]-Annahme bestaetigt.
  - Z. 315-328: Phasendifferenz Phi = 2 E^(d-3) L(d) abs(s(d)a), L(d) = int_0^z (1+z)^(d-4) H_z^-1 dz (Gl. 5).
    (Im Text "Delta v = 2 E^(d-3) |s|" ist dimensionsmaessig E * Delta v gemeint [M].) -> Phasentempo-Spaltung
    2 E^(d-4) abs(s(d)): meine Uebersetzung 2 s = abs(Delta a2) a^2 bestaetigt.
  - Z. 394-400, 520-525: CPT-gerade: Moden linear polarisiert; Licht nahe einer Mode "could propagate essentially
    unchanged". **"A single source therefore bounds a region in coefficient space but cannot provide a strict
    constraint, as its light could be propagating in a normal mode with Psi = 0 or pi/2. ... at present the number of
    sources is insufficient for this."** Gl. (9) Z. 515: Pi_eff = sqrt(1 - (1 - <cos Phi>^2) sin^2 2Psi).
  - Gl. (10) Z. 533-547: |sum _2Y_jm (k(E)jm + i k(B)jm)| <~ pi / (2 (E2^(d-3) - E1^(d-3)) L(d)) = "maximal
    sensitivity" bei Psi = +-pi/4. Tab. III Unterschrift Z. 486-489: "The final three rows provide the approximate
    maximal sensitivity of each source to coefficients for CPT-even operators with d = 4, 6, 8." Werte d = 6 Z. 470-476:
    <~1e-31 (041219A), <~1e-32 (100826A), <~1e-31 (110301A), <~1e-31 (110721A) GeV^-2.
  - Tab. I Z. 115-133: z sind "estimated lower limit on the red shift": 041219A 0,02, 100826A 0,71, 110301A 0,21,
    110721A 0,45; Baender 100-1000 keV (041219A), 70-300 keV (GAP); Polarisation Z. 96-106: 041219A 96 +39/-40 %,
    100826A > 6 %, 110301A > 31 %, 110721A > 35 %.
  - **Erwartung verletzt (V3, gross):** Die d = 6-Werte sind keine Schranken, sondern ausdruecklich "approximate maximal
    sensitivity" fuer Psi = pi/4. Strenge Schranken aus einer Quelle gibt es fuer CPT-gerade Doppelbrechung nicht.
    Korrigierte Erwartung: DB1 "Schranken ... 1e-31 oder schaerfer" steht unter diesem Vorbehalt; DB2 wackelt.
- Nachrechnung Gl. (10) [M] (H0 = 70 km/s/Mpc, Om = 0,3, OL = 0,7 angenommen; 1/H0 = 6,70e41 GeV^-1; Simpson):
  - Probe d = 5 (CPT-ungerade, Gl. 7 pi/((E2^2 - E1^2) L(5))): 041219A 2,3e-34 (Tab. 2e-34), 100826A 7,0e-35 (7e-35),
    110301A 2,5e-34 (2e-34). Kosmologie passt also.
  - d = 6: L(6) = 0,0202 / 1,074 / 0,244 / 0,602 mal 1/H0 fuer z = 0,02 / 0,71 / 0,21 / 0,45.
    041219A: pi/(2 * 9,99e-10 GeV^3 * 1,35e40 GeV^-1) = 1,2e-31; 100826A: pi/(2 * 2,67e-11 * 7,2e41) = 8,2e-32;
    110301A: 3,6e-31; 110721A: 1,5e-31 GeV^-2. **"<~1e-32" fuer 100826A ist 8e-32**: Die Tabelle schneidet die Mantisse
    ab (alle vier Werte passen zu "Mantisse x 10^Exponent"). Spanne also 8e-32 bis 4e-31, nicht 1e-32 bis 1e-31.
- Wirksamkeit bei zufaelligem Psi [M]: Bei voller Verschmierung (<cos Phi> = 0) ist Pi_eff = abs(cos 2Psi). Eine Quelle
  schliesst nur aus, wenn abs(cos 2Psi) < Pi_beob. Anteil der Psi-Werte: 2 arcsin(Pi)/pi = 0,038 (100826A, Pi > 6 %),
  0,20 (110301A, > 31 %), 0,23 (110721A, > 35 %), 0,38 (041219A, falls Pi > 56 % als Untergrenze; Untergrenze im Text
  nicht genannt [H]). Keine der vier wirkt: 0,96 * 0,80 * 0,77 * 0,62 = 0,37 (unabhaengige Psi angenommen).
  -> [ES] Selbst ohne Netz-Ausrichtung schliessen die vier GRB eine grosse Doppelbrechung nur mit ~63 % "Wahrscheinlich-
  keit" aus; die staerkste Quelle (100826A) wirkt nur in ~4 % der Faelle.
- 14:19:04 Erwartung vor Abruf 2 (arXiv-Abstract 1305.3463, Vasileiou u. a. 2013, Fermi-LAT): Laufzeitarbeit; im
  Abstract steht fuer n = 2 subluminal E_QG,2 > 1,3e11 GeV (GRB 090510); keine Polarisation.
- A2 Ergebnis [S Abstract, quellen/A2-arxiv-api-vasileiou-friedman.xml]:
  - Vasileiou u. a. 2013 (1305.3463, PRD 87, 122001): "our most stringent limits (at 95% CL) are obtained from GRB090510
    and are E_{QG,1}>7.6 times the Planck energy (E_Pl) and E_{QG,2}>1.3 x 10^11 GeV for linear and quadratic leading
    order LIV-induced vacuum dispersion". -> Erwartung bestaetigt: 1,3e11 GeV ist eine LAUFZEIT-Schranke (Dispersion,
    nicht doppelbrechend), keine Polarisation. G/R haben sie im Doppelbrechungs-Satz mitzitiert.
  - Friedman u. a. 2020 (2003.00647, PRD 102, 043008): "constraints on all 10, 16, and 42 anisotropic birefringent SME
    coefficients for dimension d = 4, d = 5, and d = 6 ... using 7554 observations for odd d and 7376 observations for
    even d of 1278 unique sources" (optische Breitband-Polarimetrie, AGN und GRB-Nachleuchten); "our anisotropic
    constraints on all 42 birefringent SME coefficients for d = 6 are the first". -> die 42 Einzelschranken ~8e-18 der
    Data Tables sind eine gemeinsame Zerlegung aus vielen Richtungen (strenger Typ).
  - Friedman u. a. 2019 (1809.08356): zwei AGN (BL Lac z = 0,069; S5 B0716+714 z = 0,31), Sichtlinien d = 5, 6.
  - **Selbstanzeige:** Abruf 2 holte Friedman 2019/2020 mit; dafuer stand keine eigene Erwartungszeile vor dem Abruf
    (nur die korrigierte Erwartung aus L1 "ohne Ausrichtungsannahme nur die 8e-18-Schranke"). Ausgang passt zu ihr.
- Abrufzaehler: 2 von 15.
- 14:19:43 Erwartung vor Abruf 3 (WebSearch, 24 Monate, GRB-/Roentgen-Polarisation und CPT-gerade Doppelbrechung d = 6):
  Treffer betreffen fast nur d = 5 (CPT-ungerade, isotrop, POLAR/AstroSat/IXPE); keine neue strenge d = 6-Mehrquellen-
  Schranke unter 1e-31 GeV^-2.
- A3 Ergebnis [S Treffer, WebSearch]: Treffer nur bis 2020 (K/M 2009 0905.0031, Friedman 2020, Kislat/Krawczynski 2017
  1701.00437, K/M 2008 0809.2846, Kislat 2018 Symmetry 10, 596, K/M 2013). Treffertext (K/M 2009, ungelesen [S Treffer]):
  "the results for CPT-even cases cannot be interpreted as definitive bounds because the amount of birefringence in the
  CPT-even case depends on details of the source polarization"; "at d=6 it is necessary to measure polarization of
  approximately 100 MeV photons to constrain the birefringent parameters at the Planck scale".
  - Erwartung bestaetigt (kein neuer d = 6-Treffer), aber die Suche fand ueberhaupt nichts aus dem 24-Monats-Fenster ->
    schwacher Beleg. Gezielte arXiv-Abfrage mit Datumsfenster noetig.
- Abrufzaehler: 3 von 15.
- 14:20:08 Erwartung vor Abruf 4 (arXiv-API, submittedDate 2024-10-01 bis 2026-10-05, abs: birefringence UND (Lorentz ODER CPT)):
  10 bis 40 Treffer, ueberwiegend CMB-Doppelbrechung (kosmische Drehung, d = 3/Axion) und d = 5 (GRB/IXPE);
  hoechstens ein bis zwei Arbeiten zu CPT-gerader d = 6-Doppelbrechung, keine strenge Schranke unter 1e-31 GeV^-2.
- A4 Ergebnis [S Abstract, quellen/A4-arxiv-api-24m-birefringence.xml, 18 Treffer]:
  - Photon, Polarisation: Wei, J.-J. 2025 (2503.18277, ApJ): fuenf GRB, energieaufgeloeste Prompt-Polarimetrie,
    "birefringent parameter eta ... |eta| < O(10^-15 - 10^-16)" (95 %), Drehung der Polarisationsebene = isotrop,
    helizitaetsabhaengig, n = 1 (d = 5, CPT-ungerade) [S Abstract; Zuordnung n = 1 aus dem Wort "rotation of the
    polarization plane" und eta-Konvention, L]. Keine d = 6-Aussage im Abstract.
  - Motie u. a. 2026 (2601.02961): CMB, K_AF ~ 1e-41 GeV, K_F ~ 1e-32 [Einheit wie im Abstract "GeV"] -> d = 3/4, nicht 6.
  - Schreck/da Silva Magalhaes 2026 (2604.17646): Kristallographie <-> SME-Photonsektor, Punktgruppen, doppelbrechende
    Medien als Analoga. Fuer unsere Frage (Netz = Kristall) einschlaegig als Rahmen, Abstract nennt aber keine
    Ortsdispersion bei k^2 [S Abstract].
  - Schwerewellen: Araujo Filho u. a. 2026 (2602.19186): isotrop k(4)_(I), k(5)_(V); Guo u. a. 2026 (2507.09705) und
    Wang u. a. 2025 (2501.11956, d = 2, 3): Paritaets-/Lorentzverletzung, Doppelbrechung, GWTC-3. Keine d = 6-Zeile in
    den Abstracts.
  - **Erwartung bestaetigt:** keine neue strenge d = 6-Schranke fuer CPT-gerade Photon-Doppelbrechung im Fenster.
    Kleiner Verstoss: nicht "ueberwiegend CMB" (nur 1 CMB-Treffer), sondern gemischt (GW, Theorie, Kristall).
  - Suchgrenze (V8 von KUBISCH-ANKER-L): nur "birefringence" im Abstract; "birefringent" nicht abgedeckt.
- Abrufzaehler: 4 von 15.
- 14:21:10 Erwartung vor Abruf 5 (arXiv-API, gleiches Fenster, abs:birefringent ODER (abs:polarization UND abs:"Lorentz invariance
  violation")): wenige zusaetzliche Treffer, darunter GRB-/IXPE-Polarisations-Arbeiten zu d = 5; keine strenge
  d = 6-Mehrquellen-Schranke.
- A5 Ergebnis [S Abstract, quellen/A5-arxiv-api-24m-birefringent-polarization.xml]: 446 Treffer, nur die 80 neuesten
  geliefert; "birefringent" zieht Optik/Materialarbeiten (Fehlplanung der Abfrage, Selbstanzeige). Unter den 80 keine
  Photon-SME-Schranke d = 6. Fund fuer die Randbemerkung Schwerewellen: Lopez-Sarrion, Reyes, Riquelme, Schreck 2026
  (2608.01118) "New constraints on modified gravity with dimension-six operators from gravitational waves": "Two
  dimension-6 contributions of the gravitational Standard-Model Extension ... nonbirefringent and birefringent sectors
  ... Bounds on the birefringent coefficients result from the absence of a perceivable separation of the two modes in
  the event GW150914." -> Es GIBT d = 6-Doppelbrechungsschranken fuer Schwerewellen (Zahlen nicht gelesen).
  - Erwartung (wenige Zusatztreffer, keine d = 6-Photon-Schranke) bestaetigt; die 80er-Grenze laesst aeltere Treffer
    des Fensters ungesehen (Suchgrenze).
- [M] Grobe GW-Rechnung fuer REGIME-K-2 (Lesart: 2,5e-4 bei k a = 0,05 -> Koeffizient ~0,1 (k a)^2 [P, Lesart]):
  Modentrennung nicht sichtbar bei GW150914: Delta t < ~1/f ~ 10 ms ueber L ~ 410 Mpc = 1,3e25 m -> Delta v/c < 2,3e-19.
  k = 2 pi 150 Hz / c = 3,1e-6 m^-1: 0,1 (k a)^2 < 2,3e-19 -> k a < 1,5e-9 -> a < ~5e-4 m. Bedeutungslos gegen 1e-27 m.
- Abrufzaehler: 5 von 15.
- 14:21:57 Erwartung vor Abruf 6 (WebSearch, DB4: Doppelbrechung des emergenten Photons im (Quanten-)Spin-Eis): Treffer zu
  Benton/Sikora/Shannon 2012 (Photon-Dispersion im Quanten-Spin-Eis) und neueren Arbeiten; die Photon-Polarisationen
  sind bei kleinem k entartet; eine ausdrueckliche Aussage zur Aufspaltung in Ordnung k^2 (bzw. (k a)^2) finde ich
  nicht direkt im Treffertext (40 % wie DB4, eher weniger).
- A6 Ergebnis [S Treffer, WebSearch]: Benton/Sikora/Shannon 2012 "Seeing the light" (arXiv:1204.1325), Gingras/McClarty
  2014 (1311.1817), Pr2Hf2O7-Neutronen (Sibille u. a. 2018 [L]), 2109.06890, 2404.04207 (Inhalt unbekannt). Treffertext:
  omega(k -> 0) = c |k|; nichts zur Aufspaltung der Polarisationen. Erwartung bestaetigt (keine direkte Aussage im
  Treffertext). Abrufzaehler: 6 von 15.
- 14:22:28 Erwartung vor Abruf 7 (arXiv-pdf 1204.1325, Benton/Sikora/Shannon 2012): Gitterfeldtheorie auf dem Diamant-Netz
  (A auf Diamant-Kanten); zwei Photonzweige, im Minimalmodell ueber die ganze Zone entartet ("doubly degenerate"
  o. ae.); kein Wort "birefringence"; Aufspaltung erst mit weiteren Termen erwaehnt oder gar nicht.
- A7 Ergebnis [S, Benton/Sikora/Shannon 2012, arXiv:1204.1325, quellen/A7-benton-1204.1325.txt (3210 Zeilen, gezielt
  gelesen Z. 875-975, 1240-1400)]:
  - Gitterfeldtheorie: U(1)-Eichfeld A auf den Kanten des Diamant-Netzes (= Pyrochlor-Plaetze), Gitter-Rotation auf den
    Sechsring-Plaketten, E auf dem dualen Diamant-Netz (Z. 538-663, 875-893).
  - Z. 1337-1340: "the four bands of excitations zeta_lambda(k) correspond to two, degenerate, physical photon modes,
    and two unphysical, zero energy modes". Z. 1376-1380, Gl. (67)/(68): "The photon dispersion omega(k) is independent
    of polarisation", omega(k) = K sqrt((U/K) zeta^2 + (W/K) zeta^4) [Exponenten im pdftotext verloren; aus c = sqrt(UK)
    a0 und omega ~ sqrt(WK) a0^2 k^2 erschlossen, M], zeta(k) = zeta1 = -zeta2 = sqrt2 sqrt(sum_mn sin^2(k . h_mn)).
  - Z. ~900-915: h_nm = (a0/sqrt8) e_n x e_m / |e_n x e_m|: Laenge a0/(2 sqrt2) = l (Tetraederkante), Richtung <110>.
  - [M] Abgleich mit M-D: sum ueber die 6 <110>-Vektoren der Laenge l: sum (n.h)^2 = 2 l^2, sum (n.h)^4 = (l^4/4)(6 - 2 S4).
    sqrt(sum sin^2) ~ sqrt(sum (k.h)^2) (1 - sum(k.h)^4 / (6 sum(k.h)^2)) -> omega/(c k) = 1 - (k l)^2 (6 - 2 S4)/48,
    also a2 = -1/8 + S4/24. **Genau die M-D-Formel aus LICHT-FINN-NETZ-1 (Z. 107-108) [P].** M-D ist also (W = 0) die
    Benton-Gitterfeldtheorie; dort sind die Polarisationen in der GANZEN Zone entartet, nicht nur bis (k l)^4.
  - **Erwartung bestaetigt** (entartet, Wort "birefringence" fehlt). Neu gegenueber Erwartung: Aussage gilt fuer alle k
    und erklaert den numerischen Befund ~1e-10 aus LICHT-FINN-NETZ-1 (offene Frage 5 in KUBISCH-ANKER-L) [ES].
  - [ES/H] Mechanismus: Die Gitter-Rotation ist hier eine hermitesche 4x4-Matrix Z(k) mit Eigenwerten +zeta, -zeta, 0, 0
    (Gl. 62 ff.); omega haengt nur von zeta^2 ab -> beide Polarisationen gleich. Das Diamant-Netz ist zu sich selbst dual
    (A auf Diamant-Kanten, E auf den Kanten des dualen Diamanten). DEC-Maxwell auf V bildet Kanten auf Flaechen ab; ohne
    diese Selbstdualitaet gibt es keine +-Paarung, Doppelbrechung ist dann der Normalfall [H].
- Abrufzaehler: 7 von 15.
- 14:25:02 Lokalpruefungen (kein Abruf):
  - [P] HOEHE-ISOTROP-1 PLAN Abschn. 3: Licht ueber dn.operator_messen(..., dn.halbkugel(40), Fenster [0,03; 0,12]
    pi/a, gerade Potenzen bis 6); "Doppelbrechung (beschreibend): max ueber die 40 Richtungen von |a2_hi - a2_lo|".
    40 Richtungen auf der Halbkugel, nicht gezielt [110] -> D_max kann bis ~15 % unterschaetzt sein [M: f faellt 11 Grad
    neben [110] um 8 bis 14 %]. Abschn. 1.5 [P]: Oh/Td haben Spiegelebenen -> kein lineares Glied.
  - [M, indirekte Probe] Konvention von dn-a2: 26-Richtungs-Mittel aus ln (Phasenkoeffizient) 0,01642 l^2 gegen
    8 * Kugelmittel aus dn 0,01610; Verhaeltnis 1,020, wie bei M-D (0,1015/0,1000 = 1,015). Bei omega^2-Konvention
    waere Faktor 2 zu erwarten. -> dn-a2 ist Phasenkoeffizient; Delta a2 = Phasentempo-Spaltung.
  - [S-lokal, Data Tables v19 Z. 266-279]: "If no significant figures appear in the quoted limit on an absolute value,
    the order of magnitude of the limit is given as a power of 10." und "Results deduced on theoretical grounds are
    distinguished from those obtained via direct experimental measurement by an asterisk placed after the citation."
    -> [207]* (K/M 2013) gilt in den Tabellen selbst als "on theoretical grounds" abgeleitet; "10^-32" ist nur die
    Groessenordnung (meine Nachrechnung 8,2e-32 passt dazu). [204] (Friedman 2020) ohne Stern = direkte Messung.
- 14:25:02 Erwartung vor Abruf 8 (WebSearch, 24 Monate, Gegensweep: Mehr-GRB-Analysen mit AstroSat/POLAR fuer anisotrope
  CPT-gerade SME-Doppelbrechung): nur isotrope n = 1-Arbeiten (eta), keine Zerlegung der 42 k(6)-Koeffizienten aus
  Gamma-Polarimetrie.
- A8 Ergebnis [S Treffer, WebSearch]: Wei 2025 (2503.18277, eta, n = 1), AstroSat-CZTI-Polarimetrie (1707.06595,
  Gupta u. a. 2024 energieaufgeloest, fuenf GRB), Lin u. a. 2016 (1609.00193), 1807.01737, 1908.10885, 2411.00410,
  preprints.org 202409.1597 (Treffertext: "a recent preprint that discusses constraints on Standard-Model Extension
  parameters using gamma-ray burst polarimetry data from AstroSat CZTI" [S Treffer, Inhalt unbekannt]).
  - Erwartung vorerst bestaetigt (nur eta/n = 1 sichtbar); offen, was 2411.00410 und der Preprint sind. Abrufzaehler 8.
- 14:25:27 Erwartung vor Abruf 9 (arXiv-API id_list 2411.00410, 1908.10885, 1807.01737): GRB-Polarimetrie bzw. isotrope
  n = 1-LIV; keine d = 6-k(E)/k(B)-Zerlegung.
- A9 Ergebnis [S Abstract, quellen/A9-arxiv-api-idlist-grbpol.xml]: 2411.00410 (Saraogi u. a. 2024, GRB 200503A und
  201009A, CZTI, "GRB 201009A has a high degree of polarization"), 1908.10885 (Sharma u. a. 2019, GRB 160821A
  "66 +26/-27 %; 5.3 sigma", Polarisationswinkel aendert sich zweimal), 1807.01737 (GRB 171010A, zeitvariable
  Polarisation). Keine LIV-Auswertung. Erwartung bestaetigt. [ES] Es gibt heute bessere Gamma-Polarisationen als 2013
  (5,3 sigma statt ~3 sigma), aber keine d = 6-CPT-gerade Auswertung, die ich gefunden habe. Abrufzaehler 9.
- 14:25:43 Erwartung vor Abruf 10 (arXiv-API, 24 Monate, abs:"spin ice" UND abs:photon): 10 bis 40 Treffer zu Quanten-
  Spin-Eis-Photonen (Neutronen, Ce2Zr2O7, Monopole, Thermik); keiner meldet eine Aufspaltung der zwei Photon-
  Polarisationen in Ordnung k^2 im Minimalmodell.
- A10 Ergebnis [S Abstract, quellen/A10-arxiv-api-24m-spinice-photon.xml, 7 Treffer]: Quanten-Spin-Eis-Thermik
  (2608.11305), Ce2Zr2O7-Neutronen [111]-Feld (2601.03202), "Hearing the light" (Naik, Hallen, Jayaram, Moessner,
  Laumann, 2512.14843: Photonen als transversale Magnetisierungswellen, Streufeldrauschen), kuenstliche Spin-Eise
  (2603.28384, 2511.04877, 2606.03625), Spinglas (2509.08955). Keiner zur Polarisations-Aufspaltung des emergenten
  Photons. Erwartung bestaetigt; Benton 2012 bleibt im Fenster unwidersprochen (nach Recherchestand). Abrufzaehler 10.
- 14:25:57 Erwartung vor Abruf 11 (WebSearch, Gegensweep: kubische Eigen-Doppelbrechung CaF2, Burnett u. a. 2001): Doppel-
  brechung bei k^2 maximal laengs [110], null laengs [100] und [111]; Groesse ~1e-6 bei 157 nm. Bestaetigt die
  Nullstellen-Struktur von f(n).
- A11 Ergebnis [S Treffer, NIST-Seiten zu Burnett/Levine/Shirley]: "The measured effect is largest for propagation in
  the [110] direction ... and is consistent with zero as predicted by theory for propagation in the [100] and [111]
  directions." "For propagation in the [110] direction, n[001]-n[-110]=(6.5+/-0.4)x10^-7 for lambda=157.10 nm".
  Mechanismus: "symmetry-breaking effect of the finite wavevector of the photon" (Ortsdispersion).
  - Erwartung bestaetigt (Nullstellen [100], [111], Maximum [110]); Groesse 6,5e-7 statt ~1e-6 (kleine Abweichung).
  - [M] Analogzahl: CaF2 a = 0,546 nm [L], n ~ 1,56 [L]: k a = 2 pi n a/lambda = 0,034, (k a)^2 = 1,16e-3,
    Delta n/(k a)^2 ~ 5,6e-4. Liegt in der Kammer-Spanne unseres Netzes (1e-4 bis 1,9e-3 a^2): DEC-Maxwell auf V ist
    so doppelbrechend wie ein Flussspat-Kristall, in Einheiten seiner eigenen Kante.
- Abrufzaehler: 11 von 15.
- 14:26:40 Erwartung vor Abruf 12 (WebSearch, Gegensweep: gibt es schon eine Arbeit, die eine Gitterkonstante der Raumzeit
  ueber Photon-Doppelbrechung begrenzt?): keine direkte; Beane/Davoudi/Savage 2014 (Kosmische Strahlung, Rotations-
  symmetrie) und allgemeine SME-Arbeiten; keine Zahl a < ~1e-30 m aus Polarisation.
- A12 Ergebnis [S Treffer, WebSearch]: **Bounds on QCA Lattice Spacing from Data on Lorentz Violation (arXiv:2506.20136,
  Juni 2025; APS March Meeting 2026)**. Treffertext: "Using arrival-time data from high-energy gamma-ray bursts, the
  lattice spacing bound is Delta x < 5.8 x 10^-36 m ... terrestrial Michelson-Morley-type resonator experiments yield a
  weaker bound of Delta x < 6.5 x 10^-26 m". Sonst K/M 2013, Wei 2025, Brun/Mlodinow (1802.03911), Xiao/Song/Ma 2026.
  - **Erwartung verletzt (V-klein bis mittel):** Es gibt eine Arbeit im 24-Monats-Fenster, die eine Gitterkonstante
    (Quanten-Zellularautomat) aus Lorentz-Daten begrenzt. 5,8e-36 m passt nur zu einem linearen Glied (n = 1), wie
    W-D/Q-W in LICHT-FINN-NETZ-1 (2,8e-36 m) [P/ES]. Ob Doppelbrechung benutzt wird: offen -> Abruf 13.
- Abrufzaehler: 12 von 15.
- 14:27:14 Erwartung vor Abruf 13 (arXiv-API id_list 2506.20136): Dirac-/Weyl-QCA mit linearem Glied, Abbildung auf SME (d = 5
  bzw. Fermion-Koeffizienten), Schranke aus GRB-Laufzeit und Resonatoren; keine CPT-gerade d = 6-Doppelbrechung.
- A13 Ergebnis [S Abstract]: Mlodinow, L.; Brun, T. A. (2025): Bounds on QCA Lattice Spacing from Data on Lorentz
  Violation. PRD 112, 074513. "we analyze the QCA corresponding to QED and show that it implies both a deviation from
  the speed of light and spatial anisotropies. Using current experimental and astrophysical constraints, we place upper
  bounds on the QCA lattice spacing". Kein Wort zu Doppelbrechung/Polarisation im Abstract. Erwartung im Kern
  bestaetigt; offen, ob der QCA-Photon doppelbrechend ist und ob K/M 2013 benutzt wird -> Abruf 14. Abrufzaehler 13.
- 14:27:30 Erwartung vor Abruf 14 (arXiv-pdf 2506.20136): Doppelbrechung nur am Rand; beste Zahl 5,8e-36 m aus GRB-Laufzeit
  mit linearem Glied; K/M 2013 (d = 6, CPT-gerade) nicht als Schranke benutzt.
- A14 Ergebnis [S, Mlodinow/Brun 2025, quellen/A14-mlodinow-brun-2506.20136.txt, gezielt Z. 1240-1310, grep]:
  - Z. 1260-1263: "certain types of effects that have also been studied experimentally are not present in the QW model;
    for example, there is no birefringence, since the two helicity states are exactly degenerate with each other."
  - Z. 1264-1280: Abweichungen super- und subluminal je nach Richtung, Mittel null; "it is possible for an observation
    to be 'unlucky'"; "we can derive some probable upper bounds". Gl. (51)-(53): RMS-Faktor 0,346 ueber die Kugel,
    E_QG,1 >~ 1e20 GeV -> Delta x <~ 5,8e-36 m (linearer Term).
  - Erwartung bestaetigt. [ES] Methodisch derselbe Weg wie hier: unbekannte Ausrichtung -> Kugelmittel/RMS-Faktor und
    "probable upper bound" statt strenger Schranke. Auch dort ist das Licht des Gittermodells doppelbrechungsfrei.
- Abrufzaehler: 14 von 15 (einer in Reserve).

## 5. Gegensweep (Feldregel 4), ab 14:32:27: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- G1 Nullstellenbild [100]/[111] null, [110] maximal: GEPRUEFT (A11, CaF2 gemessen und Theorie) und an den eigenen
  Projektdaten [K]: HOEHE-ISOTROP-1 lauf-69/mitte.json, je Richtung |a2_hi - a2_lo| gegen 2 D f(n) mit D = 1,04e-4:
  n = (0,852; -0,523; 0,012): 8,38e-5 gemessen / 8,3e-5 Formel; (0,958; -0,195; 0,213): 1,55e-5 / 1,44e-5;
  (-0,746; 0,502; 0,437): 3,40e-5 / 3,42e-5; (-0,548; -0,438; 0,713): 3,47e-5 / 3,4e-5; nahe [001] (0,057; -0,147;
  0,988): 8e-6 (klein). (0,674; -0,045; 0,738) gibt 1,037e-4 bei f/f_max = 0,99 -> D_max ~ 1,05e-4. Die kubische
  Formel f(n) beschreibt die Doppelbrechung in der Kammermitte auf wenige Prozent.
- G2 Delta a2 ist Phasenkoeffizient: GEPRUEFT (lokal, indirekt, Verhaeltnis 1,020; Abschnitt 3).
- G3 "10^-32" ist ein Wert: GEPRUEFT (Data-Tables-Legende: nur Groessenordnung; Nachrechnung 8,2e-32).
- G4 Das Netz hat kein lineares Glied (keine zirkulare Doppelbrechung ~k): TEILWEISE GEPRUEFT. a1_voll_max_abs
  (lauf-69, alle Dateien, sort -g): Mitte 1,9e-8/1,6e-8 (lo/hi), Maximum ueber 474 + 960 + 960 + 30 + 975 + 15 Eintraege
  ~1e-6 (proben.json) bei Fit-Rest ~1e-10. Wahrscheinlich Fitrauschen; Symmetriebeweis nur fuer Oh/Td (Plan 1.5).
  [M] Waere es echt (|Delta a1| ~ 1e-6, d = 5, CPT-ungerade, streng, K/M 2013 Gl. 7: < 7e-35 GeV^-1):
  a < 2 * 7e-35/1e-6 GeV^-1 = 1,4e-28 GeV^-1 = 2,8e-44 m, unter der Planck-Laenge. -> Offene Frage O1, wichtig.
- G5 Niemand hat schon eine Gitterkonstante aus LV-Daten begrenzt: GEPRUEFT, falsch (A12 bis A14, Mlodinow/Brun 2025).
- G6 Die GRB-Polarisationen von 2011/2012 sind belastbar: NICHT GEPRUEFT [L: GAP ~3 sigma, INTEGRAL 041219A umstritten].
- G7 Die Netz-Moden sind linear polarisiert (CPT-gerade -> k(E), k(B)): NICHT GEPRUEFT; [M/L] k^2-Glied ist gerade in k,
  Reziprozitaet (verlustfrei, zeitumkehrsymmetrisch) -> symmetrischer 2x2-Block -> lineare Moden.
- G8 Kosmologie von K/M 2013: NICHT GEPRUEFT; H0 = 70, Om = 0,3 angenommen, reproduziert ihre d = 5-Zahlen.

## 6. Rechnungen fuer das Dossier [M] (Einheiten hbar c = 1,973e-16 GeV m; LHAASO l < 1,58e-27 m <=> a < 4,47e-27 m
   = 2,27e-11 GeV^-1)

- Uebersetzung: B(n) = |sum _2Y_jm(n)(k(E)jm + i k(B)jm)| = Delta a2(n) a^2 / 2 = D f(n) a^2 (kubisch, f <= 1/2).
- Fall A (guenstigste Lage f = 1/2, Psi = pi/4): a^2 < 2 b / D.
  - Mitte D = 1,04e-4: b = 8,2e-32 -> a^2 < 1,58e-27 GeV^-2, a < 3,97e-14 GeV^-1 = 7,8e-30 m (l = 2,8e-30 m), 570-mal
    unter LHAASO; b = 1e-32 (Tabellenwert) -> a < 2,7e-30 m (l = 9,7e-31 m), 1630-mal; b = 1,2e-31 (041219A) ->
    a < 9,5e-30 m, 470-mal.
  - D = 1,9e-3: b = 8,2e-32 -> a < 1,8e-30 m (2440-mal); b = 1e-32 -> 6,4e-31 m.
  - D = 8,3e-5 (w0*): b = 8,2e-32 -> a < 8,8e-30 m (510-mal).
  - D = 7e-7 (S1-Ecke): b = 8,2e-32 -> a < 9,5e-29 m (47-mal); b = 1e-32 -> 3,3e-29 m (134-mal).
- Fall B (typische Lage f = 0,276, Psi = pi/4, Mitte, b = 8,2e-32): a^2 < b/(D f) = 2,86e-27 -> a < 1,06e-29 m (424-mal).
- Fall C (Psi zufaellig, volle Verschmierung): Ausschluss-Anteil 1 - 0,962 * 0,799 * 0,772 * 0,622 = 0,63 (mit 041219A,
  Pi > 56 % angenommen [H]); ohne 041219A 0,41. Keine Schranke, eine Trefferquote unter gleichverteiltem Psi.
- Streng (Friedman 2020, alle 42 Koeffizienten): Kubisches Netz -> nur k(E)4m [H: paritaetsgerade]. Kasten:
  N4^2 <= 8,4^2 + 2 (7,8^2 + 7,8^2 + 7,1^2 + 7,1^2 + 7,2^2 + 7,4^2 + 7,2^2 + 7,8^2) = 954 (e-36) -> N4 <= 3,1e-17 GeV^-2;
  B_max <= sqrt(9/(4 pi)) N4 = 0,846 N4 = 2,6e-17 [L: Additionssatz fuer Spin-Harmonische]; D a^2/2 <= 2,6e-17 ->
  a <= 7,1e-7 GeV^-1 = 1,4e-22 m (l <= 4,9e-23 m). Ohne Kasten (B_max <= 8e-18): a <= 7,7e-23 m. 4 bis 5 Groessen-
  ordnungen SCHWAECHER als LHAASO.
- Phase bei der LHAASO-Grenze [M]: Phi = 2 E^3 L(6) B; bei a = 4,47e-27 m ist B = D a^2/2 (f = 1/2) = 1,04e-4 * 5,1e-22 / 2
  = 2,7e-26 GeV^-2; GRB 100826A: Phi = 2 * 2,7e-11 * 7,2e41 * 2,7e-26 ~ 1e6 rad -> voellige Verschmierung.
- EFT-Gueltigkeit: E a = 3e-4 GeV * 1,5e-14 GeV^-1 = 4,5e-18 << 1.
- Ende Gegensweep/Rechnungen 14:32:27 (date).
- Berichtigung 14:34:37 (date) zu G4: Die Maxima von a1 waren mit sort -g unter LC_NUMERIC=de_DE gebildet. Dort ist das
  Dezimalzeichen ein Komma; sort las nur die fuehrende Ziffer (alle "Maxima" begannen mit 8 oder 9). ~~Maximum ~1e-6
  (proben.json)~~. Neu mit LC_ALL=C sort -g: mitte 1,9e-8; proben 1,96e-6; f43-0 9,2e-7; f43-1 1,04e-6; null 2,0e-7;
  gitter 1,43e-6; l2 8,6e-8. [K/ES] Im F-43m-Schnitt (Td, Spiegelebenen, a1 = 0 durch Symmetrie) liegen die Werte
  ebenfalls bei ~1e-6: das ist der Rauschpegel des Fits. Die allgemeinen Stichproben (bis 2e-6) liegen im selben
  Pegel. Also kein Hinweis auf ein echtes lineares Glied, aber auch kein Beweis. Rechnung "a < 2,8e-44 m bei
  |Delta a1| = 1e-6" bleibt als Wenn-dann-Aussage. Selbstanzeige: Locale-Fehler.

## 7. Abschluss

- Dossier geschrieben (DOSSIER.md), Abgabe 14:40:00 (date). Abrufe 14 von 15. Rueckfragen RF1 bis RF3 und offene Fragen
  O1 bis O7 stehen im Dossier 6.4.
- Nachtrag 14:40:17 (date): KARTE.md um 14:09:18 geaendert (nur Zeitzeile Z. 3), DB1 bis DB4 woertlich gleich; im
  Dossier vermerkt.
